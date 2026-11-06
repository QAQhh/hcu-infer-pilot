# vllm GLM-5/5.1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` | [#53785](https://github.com/vllm-project/vllm/pull/53785) |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-HiSparse.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-DCP4-EP.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` | [#51015](https://github.com/vllm-project/vllm/pull/51015) |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml` | no direct PR-number commit |
| `tests/models/glm5next/__init__.py` | [#55736](https://github.com/vllm-project/vllm/pull/55736) |
| `tests/models/glm5next/test_epd_metadata.py` | [#64071](https://github.com/vllm-project/vllm/pull/64071) |
| `tests/models/glm5next/test_kda_conv_weight_refit.py` | [#60991](https://github.com/vllm-project/vllm/pull/60991) |
| `tests/models/glm5next/test_kda_recurrent.py` | [#55736](https://github.com/vllm-project/vllm/pull/55736), [#56960](https://github.com/vllm-project/vllm/pull/56960), [#56974](https://github.com/vllm-project/vllm/pull/56974), [#57979](https://github.com/vllm-project/vllm/pull/57979), [#60991](https://github.com/vllm-project/vllm/pull/60991) |
| `tests/models/glm5next/test_kda_state_dtype.py` | [#59147](https://github.com/vllm-project/vllm/pull/59147) |
| `tests/models/glm5next/test_mega_moe.py` | [#60895](https://github.com/vllm-project/vllm/pull/60895) |
| `tests/models/glm5next/test_sequence_parallel.py` | [#57387](https://github.com/vllm-project/vllm/pull/57387), [#58061](https://github.com/vllm-project/vllm/pull/58061) |
| `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` | [#57327](https://github.com/vllm-project/vllm/pull/57327), [#57546](https://github.com/vllm-project/vllm/pull/57546), [#58167](https://github.com/vllm-project/vllm/pull/58167) |
| `tests/models/multimodal/processing/test_glm5next.py` | [#55389](https://github.com/vllm-project/vllm/pull/55389), [#55647](https://github.com/vllm-project/vllm/pull/55647), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#59565](https://github.com/vllm-project/vllm/pull/59565), [#64071](https://github.com/vllm-project/vllm/pull/64071), [#64644](https://github.com/vllm-project/vllm/pull/64644) |
| `tests/v1/attention/test_glm5next_indexer_block_sizes.py` | [#57169](https://github.com/vllm-project/vllm/pull/57169) |
| `tests/v1/attention/test_rocm_glm5next_sparse.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#55239](https://github.com/vllm-project/vllm/pull/55239), [#57169](https://github.com/vllm-project/vllm/pull/57169), [#58008](https://github.com/vllm-project/vllm/pull/58008) |
| `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` | [#49791](https://github.com/vllm-project/vllm/pull/49791), [#62843](https://github.com/vllm-project/vllm/pull/62843), [#64481](https://github.com/vllm-project/vllm/pull/64481) |
| `vllm/models/glm5next/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#56176](https://github.com/vllm-project/vllm/pull/56176) |
| `vllm/models/glm5next/amd/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/amd/ops/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/amd/ops/kpool_compress.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#55214](https://github.com/vllm-project/vllm/pull/55214), [#58454](https://github.com/vllm-project/vllm/pull/58454), [#60919](https://github.com/vllm-project/vllm/pull/60919) |
| `vllm/models/glm5next/amd/ops/third_party/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/amd/ops/third_party/kda/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#57979](https://github.com/vllm-project/vllm/pull/57979) |
| `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#57979](https://github.com/vllm-project/vllm/pull/57979) |
| `vllm/models/glm5next/amd/sparse_indexer.py` | [#55358](https://github.com/vllm-project/vllm/pull/55358), [#57425](https://github.com/vllm-project/vllm/pull/57425), [#57701](https://github.com/vllm-project/vllm/pull/57701), [#58167](https://github.com/vllm-project/vllm/pull/58167), [#59211](https://github.com/vllm-project/vllm/pull/59211), [#60753](https://github.com/vllm-project/vllm/pull/60753), [#60919](https://github.com/vllm-project/vllm/pull/60919) |
| `vllm/models/glm5next/common/__init__.py` | [#56176](https://github.com/vllm-project/vllm/pull/56176) |
| `vllm/models/glm5next/common/attention.py` | [#55222](https://github.com/vllm-project/vllm/pull/55222), [#55358](https://github.com/vllm-project/vllm/pull/55358), [#56176](https://github.com/vllm-project/vllm/pull/56176), [#57169](https://github.com/vllm-project/vllm/pull/57169), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#57701](https://github.com/vllm-project/vllm/pull/57701), [#58454](https://github.com/vllm-project/vllm/pull/58454), [#59211](https://github.com/vllm-project/vllm/pull/59211) |
| `vllm/models/glm5next/common/kda.py` | [#56176](https://github.com/vllm-project/vllm/pull/56176), [#56960](https://github.com/vllm-project/vllm/pull/56960), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#59147](https://github.com/vllm-project/vllm/pull/59147), [#60919](https://github.com/vllm-project/vllm/pull/60919), [#60991](https://github.com/vllm-project/vllm/pull/60991), [#61614](https://github.com/vllm-project/vllm/pull/61614) |
| `vllm/models/glm5next/common/model.py` | [#55389](https://github.com/vllm-project/vllm/pull/55389), [#56176](https://github.com/vllm-project/vllm/pull/56176), [#56983](https://github.com/vllm-project/vllm/pull/56983), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#58061](https://github.com/vllm-project/vllm/pull/58061), [#59147](https://github.com/vllm-project/vllm/pull/59147), [#59221](https://github.com/vllm-project/vllm/pull/59221), [#60763](https://github.com/vllm-project/vllm/pull/60763), [#60895](https://github.com/vllm-project/vllm/pull/60895), [#60991](https://github.com/vllm-project/vllm/pull/60991) |
| `vllm/models/glm5next/common/mtp.py` | [#56176](https://github.com/vllm-project/vllm/pull/56176), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#59221](https://github.com/vllm-project/vllm/pull/59221), [#60895](https://github.com/vllm-project/vllm/pull/60895) |
| `vllm/models/glm5next/common/multimodal.py` | [#55389](https://github.com/vllm-project/vllm/pull/55389), [#55647](https://github.com/vllm-project/vllm/pull/55647), [#56176](https://github.com/vllm-project/vllm/pull/56176), [#57387](https://github.com/vllm-project/vllm/pull/57387), [#59126](https://github.com/vllm-project/vllm/pull/59126), [#59565](https://github.com/vllm-project/vllm/pull/59565), [#64071](https://github.com/vllm-project/vllm/pull/64071) |
| `vllm/models/glm5next/common/sparse_indexer.py` | [#55358](https://github.com/vllm-project/vllm/pull/55358), [#60229](https://github.com/vllm-project/vllm/pull/60229) |
| `vllm/models/glm5next/nvidia/__init__.py` | [#55214](https://github.com/vllm-project/vllm/pull/55214) |
| `vllm/models/glm5next/nvidia/mega_moe.py` | [#60895](https://github.com/vllm-project/vllm/pull/60895) |
| `vllm/models/glm5next/nvidia/ops/__init__.py` | [#55214](https://github.com/vllm-project/vllm/pull/55214) |
| `vllm/models/glm5next/nvidia/ops/fused_eh_norm.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/nvidia/ops/kpool_compress.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#55214](https://github.com/vllm-project/vllm/pull/55214), [#57169](https://github.com/vllm-project/vllm/pull/57169), [#57477](https://github.com/vllm-project/vllm/pull/57477), [#58454](https://github.com/vllm-project/vllm/pull/58454) |
| `vllm/models/glm5next/nvidia/ops/third_party/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/nvidia/ops/third_party/kda/__init__.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906) |
| `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#55736](https://github.com/vllm-project/vllm/pull/55736), [#56974](https://github.com/vllm-project/vllm/pull/56974) |
| `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` | [#53906](https://github.com/vllm-project/vllm/pull/53906), [#55736](https://github.com/vllm-project/vllm/pull/55736), [#56974](https://github.com/vllm-project/vllm/pull/56974) |
| `vllm/models/glm5next/nvidia/sparse_indexer.py` | [#54951](https://github.com/vllm-project/vllm/pull/54951), [#55270](https://github.com/vllm-project/vllm/pull/55270), [#55358](https://github.com/vllm-project/vllm/pull/55358), [#57327](https://github.com/vllm-project/vllm/pull/57327), [#57546](https://github.com/vllm-project/vllm/pull/57546), [#57701](https://github.com/vllm-project/vllm/pull/57701), [#59211](https://github.com/vllm-project/vllm/pull/59211), [#60032](https://github.com/vllm-project/vllm/pull/60032) |
| `vllm/models/glm5next/sparse_indexer.py` | [#55358](https://github.com/vllm-project/vllm/pull/55358) |

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
| 2026-11-05 | [#60895](https://github.com/vllm-project/vllm/pull/60895) | merged | [Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts | `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/nvidia/mega_moe.py`, `vllm/models/glm5next/common/model.py` |
| 2026-11-04 | [#60919](https://github.com/vllm-project/vllm/pull/60919) | merged | [JIT][ROCm] Fully warmup GLM-5.3-Flash | `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py` |
| 2026-10-31 | [#61614](https://github.com/vllm-project/vllm/pull/61614) | merged | [Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly | `vllm/models/glm5next/common/kda.py` |
| 2026-10-30 | [#64644](https://github.com/vllm-project/vllm/pull/64644) | merged | [CI] Fix mypy errors in test_glm5next.py | `tests/models/multimodal/processing/test_glm5next.py` |
| 2026-10-30 | [#64071](https://github.com/vllm-project/vllm/pull/64071) | merged | [EPD] Metadata-only image and video inputs for GLM-5.3-Flash | `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/glm5next/test_epd_metadata.py`, `vllm/models/glm5next/common/multimodal.py` |
| 2026-10-29 | [#60229](https://github.com/vllm-project/vllm/pull/60229) | merged | [Spec Decode][GLM-5.3-Flash] Support adaptive verification | `vllm/models/glm5next/common/sparse_indexer.py` |
| 2026-10-29 | [#64481](https://github.com/vllm-project/vllm/pull/64481) | merged | [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100 | `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` |
| 2026-10-27 | [#60991](https://github.com/vllm-project/vllm/pull/60991) | merged | [Bugfix] Fuse GLM-5.3 KDA q\|k\|v convs into one conv1d parameter | `tests/models/glm5next/test_kda_conv_weight_refit.py`, `vllm/models/glm5next/common/kda.py`, `tests/models/glm5next/test_kda_recurrent.py` |
| 2026-10-22 | [#62843](https://github.com/vllm-project/vllm/pull/62843) | merged | [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107 | `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` |
| 2026-10-14 | [#60753](https://github.com/vllm-project/vllm/pull/60753) | merged | [Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk | `vllm/models/glm5next/amd/sparse_indexer.py` |
| 2026-10-11 | [#59147](https://github.com/vllm-project/vllm/pull/59147) | merged | [Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state | `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py` |
| 2026-10-11 | [#54951](https://github.com/vllm-project/vllm/pull/54951) | merged | [Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP | `vllm/models/glm5next/nvidia/sparse_indexer.py` |
| 2026-10-09 | [#57169](https://github.com/vllm-project/vllm/pull/57169) | merged | [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots | `vllm/models/glm5next/common/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py` |
| 2026-10-09 | [#60763](https://github.com/vllm-project/vllm/pull/60763) | merged | [Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config | `vllm/models/glm5next/common/model.py` |
| 2026-10-08 | [#56983](https://github.com/vllm-project/vllm/pull/56983) | merged | [Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash | `vllm/models/glm5next/common/model.py` |
| 2026-10-08 | [#60032](https://github.com/vllm-project/vllm/pull/60032) | merged | [Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer | `vllm/models/glm5next/nvidia/sparse_indexer.py` |
| 2026-10-07 | [#59221](https://github.com/vllm-project/vllm/pull/59221) | merged | [ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950 | `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py` |
| 2026-10-05 | [#59211](https://github.com/vllm-project/vllm/pull/59211) | merged | [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer | `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py` |
| 2026-10-05 | [#56974](https://github.com/vllm-project/vllm/pull/56974) | merged | [Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel | `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` |
| 2026-10-02 | [#59126](https://github.com/vllm-project/vllm/pull/59126) | merged | [Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input | `vllm/models/glm5next/common/multimodal.py` |
| 2026-10-02 | [#58167](https://github.com/vllm-project/vllm/pull/58167) | merged | [ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes | `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py` |
| 2026-10-02 | [#59565](https://github.com/vllm-project/vllm/pull/59565) | merged | [Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling | `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py` |
| 2026-10-02 | [#57387](https://github.com/vllm-project/vllm/pull/57387) | merged | [Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor | `tests/transformers_utils/processors/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py` |
| 2026-09-30 | [#58008](https://github.com/vllm-project/vllm/pull/58008) | merged | [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel | `tests/v1/attention/test_rocm_glm5next_sparse.py` |
| 2026-09-30 | [#57979](https://github.com/vllm-project/vllm/pull/57979) | merged | [ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA | `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `tests/models/glm5next/test_kda_recurrent.py` |
| 2026-09-30 | [#55389](https://github.com/vllm-project/vllm/pull/55389) | merged | [Model] Extend device-side mm normalization to GLM4V/GLM5Next | `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py` |
| 2026-09-29 | [#55222](https://github.com/vllm-project/vllm/pull/55222) | merged | [Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace | `vllm/models/glm5next/common/attention.py` |
| 2026-09-29 | [#56960](https://github.com/vllm-project/vllm/pull/56960) | merged | [Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash | `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py` |
| 2026-09-29 | [#55647](https://github.com/vllm-project/vllm/pull/55647) | merged | [Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler | `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py` |
| 2026-09-25 | [#58454](https://github.com/vllm-project/vllm/pull/58454) | merged | [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding | `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py` |
| 2026-09-25 | [#55270](https://github.com/vllm-project/vllm/pull/55270) | merged | [Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with | `vllm/models/glm5next/nvidia/sparse_indexer.py` |
| 2026-09-22 | [#58061](https://github.com/vllm-project/vllm/pull/58061) | merged | [Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard | `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py` |
| 2026-09-20 | [#57546](https://github.com/vllm-project/vllm/pull/57546) | merged | [GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher | `vllm/models/glm5next/nvidia/sparse_indexer.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` |
| 2026-09-20 | [#57477](https://github.com/vllm-project/vllm/pull/57477) | merged | [Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel | `vllm/models/glm5next/nvidia/ops/kpool_compress.py` |
| 2026-09-19 | [#57701](https://github.com/vllm-project/vllm/pull/57701) | merged | [GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved | `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py` |
| 2026-09-18 | [#57425](https://github.com/vllm-project/vllm/pull/57425) | merged | [Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash) | `vllm/models/glm5next/amd/sparse_indexer.py` |
| 2026-09-18 | [#57327](https://github.com/vllm-project/vllm/pull/57327) | merged | [Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches | `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py` |
| 2026-09-16 | [#55358](https://github.com/vllm-project/vllm/pull/55358) | merged | [Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA | `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/sparse_indexer.py` |
| 2026-09-16 | [#56176](https://github.com/vllm-project/vllm/pull/56176) | merged | [ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint | `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py` |
| 2026-09-11 | [#55239](https://github.com/vllm-project/vllm/pull/55239) | merged | [ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA | `tests/v1/attention/test_rocm_glm5next_sparse.py` |
| 2026-09-10 | [#55736](https://github.com/vllm-project/vllm/pull/55736) | merged | [Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM | `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` |
| 2026-09-04 | [#55214](https://github.com/vllm-project/vllm/pull/55214) | merged | [Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings | `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py` |
| 2026-09-03 | [#53906](https://github.com/vllm-project/vllm/pull/53906) | merged | [Model] add GLM-5.3-Flash support | `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py` |
| 2026-08-27 | [#53785](https://github.com/vllm-project/vllm/pull/53785) | merged | [Attention] Enable dense and masked MHA for GLM-5 | `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` |
| 2026-08-04 | [#51015](https://github.com/vllm-project/vllm/pull/51015) | merged | [CI] Stabilize GLM-5.2 PCP evaluation | `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` |
| 2026-08-03 | [#49791](https://github.com/vllm-project/vllm/pull/49791) | merged | [Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2 | `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` |

## Per-PR Diff Audit Cards

### PR #60895 - [Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts

- Link: https://github.com/vllm-project/vllm/pull/60895
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`, `vllm/models/glm5next/nvidia/mega_moe.py`; associated commits `7e3c015543a3`
- Diff scope read: GitHub Pull Request files API returned 5 files, +656/-3, 779 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/nvidia/mega_moe.py`, `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts"; the main implementation surface is `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/nvidia/mega_moe.py`, `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_mega_moe.py` added +277/-0 (277 lines); hunks: -0,0 +1,277; symbols: sm100_mega_moe_layout, _block_fp8, _dequant_block, _dequant_ue8m0, touching `sm100_mega_moe_layout, _block_fp8, _dequant_block`; `vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts, _create_weights, touching `Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts`; `vllm/models/glm5next/common/model.py` modified +110/-3 (113 lines); hunks: -9,7 +9,8; -24,6 +25,9; symbols: __init__, _init_mega_moe_experts, finalize_mega_moe_weights, touching `__init__, _init_mega_moe_experts, finalize_mega_moe_weights`; `vllm/models/glm5next/common/mtp.py` modified +15/-0 (15 lines); hunks: -8,6 +8,7; -211,6 +212,9 @@ def get_top_tokens(; symbols: get_top_tokens, Glm5NextMTP, __init__, load_weights, touching `get_top_tokens, Glm5NextMTP, __init__`.
- Code diff details:
  - `tests/models/glm5next/test_mega_moe.py` added +277/-0 (277 lines); hunks: -0,0 +1,277; symbols: sm100_mega_moe_layout, _block_fp8, _dequant_block, _dequant_ue8m0
  - `vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts, _create_weights
  - `vllm/models/glm5next/common/model.py` modified +110/-3 (113 lines); hunks: -9,7 +9,8; -24,6 +25,9; symbols: __init__, _init_mega_moe_experts, finalize_mega_moe_weights
  - `vllm/models/glm5next/common/mtp.py` modified +15/-0 (15 lines); hunks: -8,6 +8,7; -211,6 +212,9 @@ def get_top_tokens(; symbols: get_top_tokens, Glm5NextMTP, __init__, load_weights
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_mega_moe.py
@@ -0,0 +1,277 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.3-Flash MegaMoE: block-FP8 checkpoint shards requantized to the
+MXFP8 MegaMoE kernel layout."""
+from types import SimpleNamespace
+import pytest
diff -- vllm/models/glm5next/nvidia/mega_moe.py
@@ -0,0 +1,228 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.3-Flash adapter for the DeepGEMM MegaMoE kernel."""
+import torch
+from torch import nn
+from vllm.config import VllmConfig
diff -- vllm/models/glm5next/common/model.py
@@ -9,7 +9,8 @@
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_mega_moe.py` added +277/-0
  - runtime: `vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0; `vllm/models/glm5next/common/model.py` modified +110/-3; `vllm/models/glm5next/common/mtp.py` modified +15/-0
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60919 - [JIT][ROCm] Fully warmup GLM-5.3-Flash

- Link: https://github.com/vllm-project/vllm/pull/60919
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`; associated commits `beaa72618e3b`
- Diff scope read: GitHub Pull Request files API returned 7 files, +310/-47, 531 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[JIT][ROCm] Fully warmup GLM-5.3-Flash"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`; technical summary: Covers "[JIT][ROCm] Fully warmup GLM-5.3-Flash"; the main implementation surface is `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28 (179 lines); hunks: -12,8 +12,16; -68,7 +76,7 @@ def _hadamard128(x):; symbols: _hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs, kpool_compress_dispatch, touching `_hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs`; `vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0 (16 lines); hunks: -754,6 +754,22 @@ def __init__(; symbols: __init__, forward_hip, touching `__init__, forward_hip`; `vllm/models/glm5next/common/kda.py` modified +6/-0 (6 lines); hunks: -48,6 +48,7; -358,6 +359,11 @@ def _a_log_weight_loader(param, loaded_weight):; symbols: _a_log_weight_loader, touching `_a_log_weight_loader`.
- Code diff details:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28 (179 lines); hunks: -12,8 +12,16; -68,7 +76,7 @@ def _hadamard128(x):; symbols: _hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs, kpool_compress_dispatch
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0 (16 lines); hunks: -754,6 +754,22 @@ def __init__(; symbols: __init__, forward_hip
  - `vllm/models/glm5next/common/kda.py` modified +6/-0 (6 lines); hunks: -48,6 +48,7; -358,6 +359,11 @@ def _a_log_weight_loader(param, loaded_weight):; symbols: _a_log_weight_loader
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/ops/kpool_compress.py
@@ -12,8 +12,16 @@
+from typing import Any
+from vllm.model_executor.warmup.jit_warmup_triton_helper import (
+    DispatchSpec,
+    TritonWarmupTensor,
+    triton_kernel_dispatcher_with_warmup,
+    triton_ptr_range,
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -754,6 +754,22 @@ def __init__(
+        model_config = cfg.model_config if cfg is not None else None
+        hf_config = model_config.hf_text_config if model_config is not None else None
+        index_kpool = getattr(hf_config, "index_kpool", None) or 1
+        if index_kpool > 1:
+            kpool_ops.kpool_compress_dispatch.register_warmup(
+                k_cache=k_cache,
diff -- vllm/models/glm5next/common/kda.py
@@ -48,6 +48,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28; `vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0; `vllm/models/glm5next/common/kda.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/test_jit_warmup_triton_launcher.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61614 - [Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly

- Link: https://github.com/vllm-project/vllm/pull/61614
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/kda.py`; associated commits `602811546b03`
- Diff scope read: GitHub Pull Request files API returned 2 files, +6/-5, 26 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/common/kda.py`; technical summary: Covers "[Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly"; the main implementation surface is `vllm/models/glm5next/common/kda.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/kda.py` modified +5/-4 (9 lines); hunks: -424,11 +424,12 @@ def _flashkda_prefill(; symbols: _flashkda_prefill, touching `_flashkda_prefill`.
- Code diff details:
  - `vllm/models/glm5next/common/kda.py` modified +5/-4 (9 lines); hunks: -424,11 +424,12 @@ def _flashkda_prefill(; symbols: _flashkda_prefill
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/kda.py
@@ -424,11 +424,12 @@ def _flashkda_prefill(
-        # FlashKDA hardcodes dense q/k/v/g strides; beta may be row-strided.
+        # FlashKDA accepts row-strided q/k/v (contiguous H/D rows, aligned
+        # token stride), so the packed q|k|v views are passed without a copy.
-            q.contiguous(),
-            k.contiguous(),
-            v.contiguous(),
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/kda.py` modified +5/-4
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/common/kda.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #64644 - [CI] Fix mypy errors in test_glm5next.py

- Link: https://github.com/vllm-project/vllm/pull/64644
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_glm5next.py`; associated commits `335dd77b0916`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-5, 22 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Fix mypy errors in test_glm5next.py"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/multimodal/processing/test_glm5next.py`; technical summary: Covers "[CI] Fix mypy errors in test_glm5next.py"; the main implementation surface is `tests/models/multimodal/processing/test_glm5next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames, touching `test_glm5_raw_video_timestamps_follow_sampled_frames`.
- Code diff details:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():
-    item = raw["mm_kwargs"]["video"][0].get_data()
+    video_item = raw["mm_kwargs"]["video"][0]
+    assert video_item is not None
+    item = video_item.get_data()
-    grid_t = int(grid.reshape(-1)[0] if hasattr(grid, "reshape") else grid[0])
-    if hasattr(timestamps, "reshape"):
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64071 - [EPD] Metadata-only image and video inputs for GLM-5.3-Flash

- Link: https://github.com/vllm-project/vllm/pull/64071
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_epd_metadata.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`; associated commits `a17e79abde45`
- Diff scope read: GitHub Pull Request files API returned 4 files, +636/-52, 834 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[EPD] Metadata-only image and video inputs for GLM-5.3-Flash"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/glm5next/test_epd_metadata.py`, `vllm/models/glm5next/common/multimodal.py`; technical summary: Covers "[EPD] Metadata-only image and video inputs for GLM-5.3-Flash"; the main implementation surface is `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/glm5next/test_epd_metadata.py`, `vllm/models/glm5next/common/multimodal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1 (215 lines); hunks: -9,9 +9,14; -21,13 +26,179; symbols: _video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames, processor, touching `_video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames`; `tests/models/glm5next/test_epd_metadata.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size, touching `test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size`; `vllm/models/glm5next/common/multimodal.py` modified +8/-9 (17 lines); hunks: -713,13 +713,15 @@ def _get_video_second_idx_glm46v(; -820,10 +822,7 @@ def _get_vision_info(; symbols: _get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor, _hf_processor_applies_updates, touching `_get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor`.
- Code diff details:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1 (215 lines); hunks: -9,9 +9,14; -21,13 +26,179; symbols: _video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames, processor
  - `tests/models/glm5next/test_epd_metadata.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size
  - `vllm/models/glm5next/common/multimodal.py` modified +8/-9 (17 lines); hunks: -713,13 +713,15 @@ def _get_video_second_idx_glm46v(; -820,10 +822,7 @@ def _get_vision_info(; symbols: _get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor, _hf_processor_applies_updates
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -9,9 +9,14 @@
-The checks below are arithmetic: no weights, no GPU.
+The grid checks below are arithmetic: no weights, no GPU.
+``test_glm5_metadata_only_roundtrip`` loads the processor and compares
+raw media with metadata-only prompts.
+import json
+import numpy as np
diff -- tests/models/glm5next/test_epd_metadata.py
@@ -0,0 +1,132 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""EPD metadata-only parser contract shared by GLM-4V and GLM-5.3-Flash."""
+import pytest
+import torch
+from vllm.model_executor.models.glm4_1v import Glm4vMultiModalDataParser
diff -- vllm/models/glm5next/common/multimodal.py
@@ -713,13 +713,15 @@ def _get_video_second_idx_glm46v(
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1; `tests/models/glm5next/test_epd_metadata.py` added +132/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +8/-9
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_epd_metadata.py`, `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60229 - [Spec Decode][GLM-5.3-Flash] Support adaptive verification

- Link: https://github.com/vllm-project/vllm/pull/60229
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/sparse_indexer.py`; associated commits `cebe1097232e`
- Diff scope read: GitHub Pull Request files API returned 8 files, +287/-16, 495 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Spec Decode][GLM-5.3-Flash] Support adaptive verification"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/common/sparse_indexer.py`; technical summary: Covers "[Spec Decode][GLM-5.3-Flash] Support adaptive verification"; the main implementation surface is `vllm/models/glm5next/common/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10 (39 lines); hunks: -16,29 +16,45 @@ def _build_decode_scatter_indices(; -59,14 +75,17 @@ def _scatter_decode_tokens_by_request(; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, touching `_build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens`.
- Code diff details:
  - `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10 (39 lines); hunks: -16,29 +16,45 @@ def _build_decode_scatter_indices(; -59,14 +75,17 @@ def _scatter_decode_tokens_by_request(; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/sparse_indexer.py
@@ -16,29 +16,45 @@ def _build_decode_scatter_indices(
-    batch, with ``n == decode_lens.sum()`` as a host int (avoids a
-    device sync and keeps both repeat_interleaves sync-free).
+    batch. ``n`` is the graph-padded token count and may be larger than
+    ``decode_lens.sum()`` under adaptive verification. All graph-padding tokens
+    are mapped to a dummy request that is appended as the last one
+    (``idx=num_requests``).
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10
- Risk and verification: The diff ships test coverage in `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64481 - [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100

- Link: https://github.com/vllm-project/vllm/pull/64481
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; associated commits `1ca0dfb97612`
- Diff scope read: GitHub Pull Request files API returned 2 files, +129/-5, 176 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; technical summary: Covers "[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100"; the main implementation surface is `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3 (129 lines); hunks: -1,10 +1,11; -208,12 +209,134 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _low_latency_table, touching `build_plan, _low_latency_table`.
- Code diff details:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3 (129 lines); hunks: -1,10 +1,11; -208,12 +209,134 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _low_latency_table
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py
@@ -1,10 +1,11 @@
-"""GLM-5.2 decode GEMM selection for unquantized BF16 on SM103/SM107.
+"""GLM-5.2 decode GEMM selection for unquantized BF16 on SM100/SM103/SM107.
-:data:`GLM52_PROJECTIONS` was measured on B300 (SM103) and
-:data:`GLM52_PROJECTIONS_SM107` on VRNVL72 (SM107). The SM107 table also covers
+:data:`GLM52_PROJECTIONS` was measured on B300 (SM103),
+:data:`GLM52_PROJECTIONS_SM107` on VRNVL72 (SM107) and
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_bf16_skinny_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60991 - [Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter

- Link: https://github.com/vllm-project/vllm/pull/60991
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_kda_conv_weight_refit.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`; associated commits `de096755ad7b`
- Diff scope read: GitHub Pull Request files API returned 4 files, +184/-46, 274 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/glm5next/test_kda_conv_weight_refit.py`, `vllm/models/glm5next/common/kda.py`, `tests/models/glm5next/test_kda_recurrent.py`; technical summary: Covers "[Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter"; the main implementation surface is `tests/models/glm5next/test_kda_conv_weight_refit.py`, `vllm/models/glm5next/common/kda.py`, `tests/models/glm5next/test_kda_recurrent.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: _checkpoint_weights, _load, _kernel_view, conv1d, touching `_checkpoint_weights, _load, _kernel_view`; `vllm/models/glm5next/common/kda.py` modified +44/-44 (88 lines); hunks: -21,6 +21,9; -160,6 +163,36 @@ def _resolve_kda_prefill_backend(; symbols: _resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention, __init__, touching `_resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention`; `tests/models/glm5next/test_kda_recurrent.py` modified +3/-2 (5 lines); hunks: -303,8 +303,9 @@ def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_...; symbols: test_prefill_checkpoint_resumes_suffix, touching `test_prefill_checkpoint_resumes_suffix`; `vllm/models/glm5next/common/model.py` modified +4/-0 (4 lines); hunks: -874,6 +874,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: _checkpoint_weights, _load, _kernel_view, conv1d
  - `vllm/models/glm5next/common/kda.py` modified +44/-44 (88 lines); hunks: -21,6 +21,9; -160,6 +163,36 @@ def _resolve_kda_prefill_backend(; symbols: _resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention, __init__
  - `tests/models/glm5next/test_kda_recurrent.py` modified +3/-2 (5 lines); hunks: -303,8 +303,9 @@ def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_...; symbols: test_prefill_checkpoint_resumes_suffix
  - `vllm/models/glm5next/common/model.py` modified +4/-0 (4 lines); hunks: -874,6 +874,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_kda_conv_weight_refit.py
@@ -0,0 +1,133 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.3-Flash KDA q|k|v short convs are one fused parameter.
+The conv kernels read ``conv1d.weight`` directly, so an RL refit must reach it
+through every write path (#55087), and FULL cudagraphs capture its address, so
+it must never move.
diff -- vllm/models/glm5next/common/kda.py
@@ -21,6 +21,9 @@
+from vllm.model_executor.layers.mamba.gdn.kimi_gdn_linear_attn import (
+    _make_fused_conv1d_weight_loader,
+)
@@ -160,6 +163,36 @@ def _resolve_kda_prefill_backend(
+def _fused_qkv_conv1d(
+    conv_size: int, projection_size: int, tp_size: int, tp_rank: int, prefix: str
diff -- tests/models/glm5next/test_kda_recurrent.py
@@ -303,8 +303,9 @@ def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_first, num_spec, off
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0; `tests/models/glm5next/test_kda_recurrent.py` modified +3/-2
  - runtime: `vllm/models/glm5next/common/kda.py` modified +44/-44; `vllm/models/glm5next/common/model.py` modified +4/-0
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_kda_conv_weight_refit.py`, `tests/models/glm5next/test_kda_recurrent.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62843 - [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107

- Link: https://github.com/vllm-project/vllm/pull/62843
- Status/date: merged / 2026-10-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; associated commits `38955340b752`
- Diff scope read: GitHub Pull Request files API returned 2 files, +239/-55, 430 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; technical summary: Covers "[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107"; the main implementation surface is `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8 (150 lines); hunks: -1,6 +1,13; -64,7 +71,7 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _is_sm103, _low_latency_table, _is_supported_row_major, touching `build_plan, _is_sm103, _low_latency_table`.
- Code diff details:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8 (150 lines); hunks: -1,6 +1,13; -64,7 +71,7 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _is_sm103, _low_latency_table, _is_supported_row_major
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py
@@ -1,6 +1,13 @@
-"""GLM-5.2 decode GEMM selection for unquantized BF16 on SM103."""
+"""GLM-5.2 decode GEMM selection for unquantized BF16 on SM103/SM107.
+Dispatch is by local ``(N, K)`` weight shape and token count ``M``.
+:data:`GLM52_PROJECTIONS` was measured on B300 (SM103) and
+:data:`GLM52_PROJECTIONS_SM107` on VRNVL72 (SM107). The SM107 table also covers
+the TP4 projections (q_b, o_proj, shared expert) and the replicated indexer
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8
- Risk and verification: The diff ships test coverage in `tests/kernels/test_bf16_skinny_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60753 - [Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk

- Link: https://github.com/vllm-project/vllm/pull/60753
- Status/date: merged / 2026-10-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/sparse_indexer.py`; associated commits `3f729dafcc5a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +146/-10, 164 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/sparse_indexer.py`; technical summary: Covers "[Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk"; the main implementation surface is `vllm/models/glm5next/amd/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10 (37 lines); hunks: -396,16 +396,33 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, touching `sparse_attn_indexer_kpool`.
- Code diff details:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10 (37 lines); hunks: -396,16 +396,33 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -396,16 +396,33 @@ def sparse_attn_indexer_kpool(
-            torch.ops._C.top_k_per_row_prefill(
-                logits,
-                chunk.cu_seqlen_ks,
-                chunk.cu_seqlen_ke,
-                topk_dst,
-                num_rows,
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/amd/sparse_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #59147 - [Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state

- Link: https://github.com/vllm-project/vllm/pull/59147
- Status/date: merged / 2026-10-11
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`; associated commits `f26d9f432ced`
- Diff scope read: GitHub Pull Request files API returned 3 files, +47/-2, 64 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state"; the main implementation surface is `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_kda_recurrent_state_dtype_follows_ssm_cache_dtype, touching `test_kda_recurrent_state_dtype_follows_ssm_cache_dtype`; `vllm/models/glm5next/common/kda.py` modified +3/-1 (4 lines); hunks: -181,7 +181,9 @@ def get_state_dtype(; symbols: get_state_dtype, get_state_shape, touching `get_state_dtype, get_state_shape`; `vllm/models/glm5next/common/model.py` modified +3/-1 (4 lines); hunks: -1092,7 +1092,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config, touching `get_mamba_state_dtype_from_config`.
- Code diff details:
  - `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_kda_recurrent_state_dtype_follows_ssm_cache_dtype
  - `vllm/models/glm5next/common/kda.py` modified +3/-1 (4 lines); hunks: -181,7 +181,9 @@ def get_state_dtype(; symbols: get_state_dtype, get_state_shape
  - `vllm/models/glm5next/common/model.py` modified +3/-1 (4 lines); hunks: -1092,7 +1092,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_kda_state_dtype.py
@@ -0,0 +1,41 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""``--mamba-ssm-cache-dtype`` must reach GLM-5.3-Flash's KDA recurrent state
+(it used to be dropped, leaving the state float32 unconditionally)."""
+from types import SimpleNamespace
+import pytest
diff -- vllm/models/glm5next/common/kda.py
@@ -181,7 +181,9 @@ def get_state_dtype(
-            self.model_config.dtype, self.cache_config.mamba_cache_dtype
+            self.model_config.dtype,
+            self.cache_config.mamba_cache_dtype,
+            self.cache_config.mamba_ssm_cache_dtype,
diff -- vllm/models/glm5next/common/model.py
@@ -1092,7 +1092,9 @@ def get_mamba_state_dtype_from_config(
-            vllm_config.model_config.dtype, vllm_config.cache_config.mamba_cache_dtype
+            vllm_config.model_config.dtype,
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0
  - runtime: `vllm/models/glm5next/common/kda.py` modified +3/-1; `vllm/models/glm5next/common/model.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_kda_state_dtype.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #54951 - [Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP

- Link: https://github.com/vllm-project/vllm/pull/54951
- Status/date: merged / 2026-10-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `3e8e1364ff41`
- Diff scope read: GitHub Pull Request files API returned 4 files, +436/-38, 658 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`; technical summary: Covers "[Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP"; the main implementation surface is `vllm/models/glm5next/nvidia/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23 (63 lines); hunks: -12,7 +12,11; -169,6 +173,10 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, touching `sparse_attn_indexer_kpool`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23 (63 lines); hunks: -12,7 +12,11; -169,6 +173,10 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -12,7 +12,11 @@
-from vllm.model_executor.layers.sparse_attn_indexer import _merge_dcp_topk_global
+from vllm.model_executor.layers.sparse_attn_indexer import (
+    PrefillRowShard,
+    _merge_dcp_topk_global,
+    _reserve_row_shard_exchange_transient,
+)
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_indexer_tp_row_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57169 - [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots

- Link: https://github.com/vllm-project/vllm/pull/57169
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_glm5next_indexer_block_sizes.py`, `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; associated commits `02e55d2af38a`
- Diff scope read: GitHub Pull Request files API returned 83 files, +1281/-1987, 6039 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/common/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; technical summary: Covers "[KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots"; the main implementation surface is `vllm/models/glm5next/common/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/attention.py` modified +14/-50 (64 lines); hunks: -33,9 +33,9; -89,15 +89,9 @@ class Glm5NextIndexerCache(DeepseekV32IndexerCache):; symbols: Glm5NextIndexerCache, __init__, get_kv_cache_spec, touching `Glm5NextIndexerCache, __init__, get_kv_cache_spec`; `vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8 (8 lines); hunks: -1376,14 +1376,6 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> K...; symbols: get_kv_cache_spec, _v_up_proj, touching `get_kv_cache_spec, _v_up_proj`; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5 (5 lines); hunks: -396,11 +396,6 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, touching `_kpool_tail_seed_kernel`; `tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0 (46 lines); hunks: -313,3 +313,49 @@ def test_deepgemm_fp8_fp4_paged_mqa_logits(batch_size: int,...; symbols: test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride, touching `test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride`.
- Code diff details:
  - `vllm/models/glm5next/common/attention.py` modified +14/-50 (64 lines); hunks: -33,9 +33,9; -89,15 +89,9 @@ class Glm5NextIndexerCache(DeepseekV32IndexerCache):; symbols: Glm5NextIndexerCache, __init__, get_kv_cache_spec
  - `vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8 (8 lines); hunks: -1376,14 +1376,6 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> K...; symbols: get_kv_cache_spec, _v_up_proj
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5 (5 lines); hunks: -396,11 +396,6 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel
  - `tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0 (46 lines); hunks: -313,3 +313,49 @@ def test_deepgemm_fp8_fp4_paged_mqa_logits(batch_size: int,...; symbols: test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride
  - `tests/v1/attention/test_glm5next_indexer_block_sizes.py` added +40/-0 (40 lines); hunks: -0,0 +1,40; symbols: test_glm5next_indexer_kernel_block_sizes
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/attention.py
@@ -33,9 +33,9 @@
-from vllm.utils.deep_gemm import PAGED_MQA_PAGE_SIZES
-from vllm.v1.kv_cache_interface import KpoolTailSpec, MLAAttentionSpec
+from vllm.v1.attention.backends.mla.indexer import Glm5NextIndexerBackend
+from vllm.v1.kv_cache_interface import CircularBufferSpec, MLAAttentionSpec
@@ -89,15 +89,9 @@ class Glm5NextIndexerCache(DeepseekV32IndexerCache):
-    ``cache_config.block_size``. DeepGEMM's paged-MQA kernel
diff -- vllm/model_executor/layers/attention/mla_attention.py
@@ -1376,14 +1376,6 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
-        # SM100 FlashMLA paged kernels also express TMA coordinates in token rows.
-        uses_tma_rows = (
-            self.attn_backend.get_name() == "FLASHMLA_SPARSE"
-            and self.kv_cache_dtype in ("fp8_ds_mla", "nvfp4_ds_mla")
-            and current_platform.is_device_capability_family(100)
-        )
diff -- vllm/models/glm5next/nvidia/ops/kpool_compress.py
@@ -396,11 +396,6 @@ def _kpool_tail_seed_kernel(
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/attention.py` modified +14/-50; `vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5
  - tests: `tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0; `tests/v1/attention/test_glm5next_indexer_block_sizes.py` added +40/-0; `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60763 - [Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config

- Link: https://github.com/vllm-project/vllm/pull/60763
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/model.py`; associated commits `d095e61c0b38`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config"; the main implementation surface is `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/model.py` modified +1/-1 (2 lines); hunks: -788,7 +788,7 @@ def _aux_hidden_state(; symbols: _aux_hidden_state, forward, touching `_aux_hidden_state, forward`.
- Code diff details:
  - `vllm/models/glm5next/common/model.py` modified +1/-1 (2 lines); hunks: -788,7 +788,7 @@ def _aux_hidden_state(; symbols: _aux_hidden_state, forward
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/model.py
@@ -788,7 +788,7 @@ def _aux_hidden_state(
-        return hc_contract(completed, self.config.mhc_num_residual_streams)
+        return hc_contract(completed, self.config.hc_mult)
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/model.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/common/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56983 - [Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash

- Link: https://github.com/vllm-project/vllm/pull/56983
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/model.py`; associated commits `2274e86842d6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +47/-4, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash"; the main implementation surface is `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/model.py` modified +47/-4 (51 lines); hunks: -66,9 +66,11; -684,7 +686,7 @@ def hc_fused_post_pre(; symbols: hc_fused_post_pre, Glm5NextModel, __init__, get_layer, touching `hc_fused_post_pre, Glm5NextModel, __init__`.
- Code diff details:
  - `vllm/models/glm5next/common/model.py` modified +47/-4 (51 lines); hunks: -66,9 +66,11; -684,7 +686,7 @@ def hc_fused_post_pre(; symbols: hc_fused_post_pre, Glm5NextModel, __init__, get_layer
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/model.py
@@ -66,9 +66,11 @@
+    EagleModelMixin,
+    SupportsEagle3,
@@ -684,7 +686,7 @@ def hc_fused_post_pre(
-class Glm5NextModel(nn.Module):
+class Glm5NextModel(nn.Module, EagleModelMixin):
@@ -742,6 +744,7 @@ def get_layer(prefix: str):
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/model.py` modified +47/-4
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/common/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #60032 - [Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer

- Link: https://github.com/vllm-project/vllm/pull/60032
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `70bdce6133d0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-0, 23 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`; technical summary: Covers "[Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer"; the main implementation surface is `vllm/models/glm5next/nvidia/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0 (9 lines); hunks: -26,6 +26,7; -717,6 +718,14 @@ def __init__(; symbols: __init__, cp_kv_cache_interleave_size, touching `__init__, cp_kv_cache_interleave_size`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0 (9 lines); hunks: -26,6 +26,7; -717,6 +718,14 @@ def __init__(; symbols: __init__, cp_kv_cache_interleave_size
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -26,6 +26,7 @@
+from vllm.utils.import_utils import has_cutedsl
@@ -717,6 +718,14 @@ def __init__(
+            if current_platform.is_cuda() and has_cutedsl():
+                from vllm.model_executor.kernels.attention.dsa.dcp_indexer_cutedsl import (  # noqa: E501
+                    _PACK_DCP_TOPK_CANDIDATES_KERNEL,
+                    _STABLE_TOPK_FROM_GATHERED_CANDIDATES_KERNEL,
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/nvidia/sparse_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #59221 - [ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950

- Link: https://github.com/vllm-project/vllm/pull/59221
- Status/date: merged / 2026-10-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`; associated commits `2a54f6b625f2`
- Diff scope read: GitHub Pull Request files API returned 3 files, +213/-6, 362 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`; technical summary: Covers "[ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950"; the main implementation surface is `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/model.py` modified +82/-3 (85 lines); hunks: -23,6 +23,10; -258,7 +262,12 @@ def __init__(; symbols: __init__, get_layer, load_weights, touching `__init__, get_layer, load_weights`; `vllm/models/glm5next/common/mtp.py` modified +14/-1 (15 lines); hunks: -10,6 +10,9; -30,6 +33,8; symbols: __init__, set_moe_parameters, load_weights, touching `__init__, set_moe_parameters, load_weights`.
- Code diff details:
  - `vllm/models/glm5next/common/model.py` modified +82/-3 (85 lines); hunks: -23,6 +23,10; -258,7 +262,12 @@ def __init__(; symbols: __init__, get_layer, load_weights
  - `vllm/models/glm5next/common/mtp.py` modified +14/-1 (15 lines); hunks: -10,6 +10,9; -30,6 +33,8; symbols: __init__, set_moe_parameters, load_weights
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/model.py
@@ -23,6 +23,10 @@
+from vllm.model_executor.layers.fused_moe.utils import (
+    is_model_fused_shared_expert_compatible,
+    resolve_layer_fused_shared_expert,
+)
@@ -258,7 +262,12 @@ def __init__(
-        if config.n_shared_experts is None:
diff -- vllm/models/glm5next/common/mtp.py
@@ -10,6 +10,9 @@
+from vllm.model_executor.layers.fused_moe.utils import (
+    is_model_fused_shared_expert_compatible,
+)
@@ -30,6 +33,8 @@
+    _fused_shared_expert_name,
+    _num_fused_shared_experts,
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/model.py` modified +82/-3; `vllm/models/glm5next/common/mtp.py` modified +14/-1
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_fused_shared_expert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59211 - [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer

- Link: https://github.com/vllm-project/vllm/pull/59211
- Status/date: merged / 2026-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `30d4032363d4`
- Diff scope read: GitHub Pull Request files API returned 9 files, +242/-37, 537 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`; technical summary: Covers "[Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer"; the main implementation surface is `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27 (113 lines); hunks: -7,10 +7,12; -121,6 +123,9 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, touching `sparse_attn_indexer_kpool`; `vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0 (4 lines); hunks: -733,6 +733,10 @@ def __init__(; symbols: __init__, forward_hip, touching `__init__, forward_hip`; `vllm/models/glm5next/common/attention.py` modified +3/-0 (3 lines); hunks: -209,6 +209,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig):; symbols: get_kv_cache_spec, get_attn_backend, touching `get_kv_cache_spec, get_attn_backend`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27 (113 lines); hunks: -7,10 +7,12; -121,6 +123,9 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0 (4 lines); hunks: -733,6 +733,10 @@ def __init__(; symbols: __init__, forward_hip
  - `vllm/models/glm5next/common/attention.py` modified +3/-0 (3 lines); hunks: -209,6 +209,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig):; symbols: get_kv_cache_spec, get_attn_backend
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -7,10 +7,12 @@
+from vllm.distributed import get_dcp_group
+from vllm.model_executor.layers.sparse_attn_indexer import _merge_dcp_topk_global
@@ -121,6 +123,9 @@ def sparse_attn_indexer_kpool(
+    dcp_rank: int = 0,
+    dcp_world_size: int = 1,
+    cp_kv_cache_interleave_size: int = 1,
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -733,6 +733,10 @@ def __init__(
+        if cfg is not None and cfg.parallel_config.decode_context_parallel_size > 1:
+            raise NotImplementedError(
+                "SparseAttnIndexerKpool on ROCm does not support DCP."
+            )
diff -- vllm/models/glm5next/common/attention.py
@@ -209,6 +209,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig):
+            # Tiny per-request ring; every DCP rank keeps the full tail so the
+            # rank owning a pool can compress it.
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27; `vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0; `vllm/models/glm5next/common/attention.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/core/test_kv_cache_utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56974 - [Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel

- Link: https://github.com/vllm-project/vllm/pull/56974
- Status/date: merged / 2026-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`; associated commits `ae53b06898bc`
- Diff scope read: GitHub Pull Request files API returned 3 files, +78/-3, 109 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel"; the main implementation surface is `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0 (71 lines); hunks: -194,6 +194,77 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run, touching `test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run`; `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2 (6 lines); hunks: -87,7 +87,7 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; -260,7 +260,9 @@ def fused_recurrent_gated_delta_rule_fwd(; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd, touching `fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1 (4 lines); hunks: -95,7 +95,9 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, touching `fused_recurrent_kda_fwd`.
- Code diff details:
  - `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0 (71 lines); hunks: -194,6 +194,77 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2 (6 lines); hunks: -87,7 +87,7 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; -260,7 +260,9 @@ def fused_recurrent_gated_delta_rule_fwd(; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1 (4 lines); hunks: -95,7 +95,9 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_kda_recurrent.py
@@ -194,6 +194,77 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():
+@pytest.mark.skipif(
+    not current_platform.is_cuda(), reason="The large-grid fix is NVIDIA-only"
+)
+@pytest.mark.parametrize("num_seqs,num_heads", [(1024, 64), (2048, 48)])
+def test_fused_recurrent_kda_more_than_65535_programs(num_seqs: int, num_heads: int):
+    """Regression test for the launch grid.
diff -- vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py
@@ -87,7 +87,7 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(
-    i_k, i_v, i_nh = tl.program_id(0), tl.program_id(1), tl.program_id(2)
+    i_nh, i_v, i_k = tl.program_id(0), tl.program_id(1), tl.program_id(2)
@@ -260,7 +260,9 @@ def fused_recurrent_gated_delta_rule_fwd(
-    grid = (NK, NV, N * HV)
+    # N * HV goes in gridDim.x: gridDim.z is capped at 65535 and batch x heads exceeds it
+    # (e.g. GLM-5.3-Flash at TP=1: 1024 x 64 = 65536 -> "invalid argument" at CUDA-graph capture).
diff -- vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py
@@ -95,7 +95,9 @@ def fused_recurrent_kda_fwd(
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0
  - runtime: `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_kda_recurrent.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59126 - [Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input

- Link: https://github.com/vllm-project/vllm/pull/59126
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/multimodal.py`; associated commits `097989299222`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-3, 35 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/common/multimodal.py`; technical summary: Covers "[Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input"; the main implementation surface is `vllm/models/glm5next/common/multimodal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/multimodal.py` modified +4/-3 (7 lines); hunks: -46,6 +46,7; -395,7 +396,7 @@ def __init__(; symbols: __init__, rot_pos_emb, forward, touching `__init__, rot_pos_emb, forward`.
- Code diff details:
  - `vllm/models/glm5next/common/multimodal.py` modified +4/-3 (7 lines); hunks: -46,6 +46,7; -395,7 +396,7 @@ def __init__(; symbols: __init__, rot_pos_emb, forward
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/multimodal.py
@@ -46,6 +46,7 @@
+from vllm.utils.torch_utils import async_tensor_h2d
@@ -395,7 +396,7 @@ def __init__(
-            max_position=8192,
+            max_position=text_config.max_position_embeddings,
@@ -479,7 +480,7 @@ def rot_pos_emb(
-        pos_ids = pos_ids.to(cos.device, non_blocking=True)
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +4/-3
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/common/multimodal.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58167 - [ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes

- Link: https://github.com/vllm-project/vllm/pull/58167
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`; associated commits `98b29aa99aee`
- Diff scope read: GitHub Pull Request files API returned 8 files, +705/-240, 1241 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`; technical summary: Covers "[ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes"; the main implementation surface is `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14 (86 lines); hunks: -8,10 +8,6; -20,17 +16,10 @@ def _require_deep_gemm() -> None:; symbols: _require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build, touching `_require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build`; `vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6 (82 lines); hunks: -8,10 +8,11; -24,6 +25,7; symbols: _kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool, touching `_kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool`.
- Code diff details:
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14 (86 lines); hunks: -8,10 +8,6; -20,17 +16,10 @@ def _require_deep_gemm() -> None:; symbols: _require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6 (82 lines); hunks: -8,10 +8,11; -24,6 +25,7; symbols: _kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_sparse_indexer_topk_dispatch.py
@@ -8,10 +8,6 @@
-pytestmark = pytest.mark.skipif(
-    not current_platform.is_cuda(), reason="CUDA-only dispatch"
-)
@@ -20,17 +16,10 @@ def _require_deep_gemm() -> None:
-@pytest.mark.parametrize("backend", ["auto", "persistent", "cooperative", "torch"])
-def test_kpool_indexer_dispatches_through_shared_topk_backend(backend: str) -> None:
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -8,10 +8,11 @@
-from vllm.config import get_current_vllm_config_or_none
+from vllm.config import CUDAGraphMode, get_current_vllm_config_or_none
+from vllm.model_executor.layers.indexer_topk import get_indexer_topk
@@ -24,6 +25,7 @@
+from vllm.utils.math_utils import cdiv
@@ -37,6 +39,9 @@
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59565 - [Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling

- Link: https://github.com/vllm-project/vllm/pull/59565
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`; associated commits `5688a4dd4a1e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +75/-0, 93 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`; technical summary: Covers "[Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling"; the main implementation surface is `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0 (51 lines); hunks: -188,3 +188,54 @@ def test_mm_device_do_normalize():; symbols: test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget, test_image_encoder_cache_follows_max_pixels_override, touching `test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget`; `vllm/models/glm5next/common/multimodal.py` modified +24/-0 (24 lines); hunks: -2,6 +2,7; -672,6 +673,29 @@ def _get_video_max_pixels(self) -> int:; symbols: _get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v, touching `_get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v`.
- Code diff details:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0 (51 lines); hunks: -188,3 +188,54 @@ def test_mm_device_do_normalize():; symbols: test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget, test_image_encoder_cache_follows_max_pixels_override
  - `vllm/models/glm5next/common/multimodal.py` modified +24/-0 (24 lines); hunks: -2,6 +2,7; -672,6 +673,29 @@ def _get_video_max_pixels(self) -> int:; symbols: _get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -188,3 +188,54 @@ def test_mm_device_do_normalize():
+def _image_info(**kwargs):
+    ctx = build_model_context(
+        "zai-org/GLM-5.3-Flash",
+        limit_mm_per_prompt={"image": 1},
+        **kwargs,
+    )
diff -- vllm/models/glm5next/common/multimodal.py
@@ -2,6 +2,7 @@
+import math
@@ -672,6 +673,29 @@ def _get_video_max_pixels(self) -> int:
+    def get_image_size_with_most_features(self) -> ImageSize:
+        # The inherited square probe strands budget whenever the token
+        # ceiling is not a perfect square: with max_image_tokens=8000 the
+        # square refits to 2492x2492 (89x89 = 7921 tokens) while a
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +24/-0
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57387 - [Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor

- Link: https://github.com/vllm-project/vllm/pull/57387
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_sequence_parallel.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py` and 7 files; associated commits `e3cae8d2ac6b`
- Diff scope read: GitHub Pull Request files API returned 36 files, +365/-2384, 3571 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor"; model line: GLM-5/5.1; category: docs/tests/CI; main diff: `tests/transformers_utils/processors/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor"; the main implementation surface is `tests/transformers_utils/processors/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389 (389 lines); hunks: -1,389 +0,0; symbols: resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive, test_smart_resize_rejects_degenerate_inputs, touching `resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive`; `vllm/models/glm5next/common/multimodal.py` modified +68/-52 (120 lines); hunks: -3,13 +3,14; -44,7 +45,6; symbols: load_weights, Glm5NextProcessingInfo, _glm5_hf_processor, get_hf_processor, touching `load_weights, Glm5NextProcessingInfo, _glm5_hf_processor`; `vllm/models/glm5next/common/model.py` modified +74/-26 (100 lines); hunks: -6,6 +6,7; -83,7 +84,6; symbols: _is_moe, _is_kda_layer, _is_linear_attn, _validate_supported_config, touching `_is_moe, _is_kda_layer, _is_linear_attn`; `tests/models/multimodal/processing/test_glm5next.py` modified +16/-33 (49 lines); hunks: -15,16 +15,15; -48,27 +47,16 @@ def _pixel_path_grid(; symbols: _pixel_path_grid, test_video_placeholders_match_encoder_rows, touching `_pixel_path_grid, test_video_placeholders_match_encoder_rows`.
- Code diff details:
  - `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389 (389 lines); hunks: -1,389 +0,0; symbols: resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive, test_smart_resize_rejects_degenerate_inputs
  - `vllm/models/glm5next/common/multimodal.py` modified +68/-52 (120 lines); hunks: -3,13 +3,14; -44,7 +45,6; symbols: load_weights, Glm5NextProcessingInfo, _glm5_hf_processor, get_hf_processor
  - `vllm/models/glm5next/common/model.py` modified +74/-26 (100 lines); hunks: -6,6 +6,7; -83,7 +84,6; symbols: _is_moe, _is_kda_layer, _is_linear_attn, _validate_supported_config
  - `tests/models/multimodal/processing/test_glm5next.py` modified +16/-33 (49 lines); hunks: -15,16 +15,15; -48,27 +47,16 @@ def _pixel_path_grid(; symbols: _pixel_path_grid, test_video_placeholders_match_encoder_rows
  - `vllm/models/qwen4_exp/amd/model.py` modified +10/-37 (47 lines); hunks: -7,6 +7,7; -47,7 +48,6; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- tests/transformers_utils/processors/test_glm5next.py
@@ -1,389 +0,0 @@
-# SPDX-License-Identifier: Apache-2.0
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
-"""Unit tests for the vLLM-native GLM-5.3-Flash multimodal processor."""
-import math
-import pytest
-import torch
diff -- vllm/models/glm5next/common/multimodal.py
@@ -3,13 +3,14 @@
-from functools import cached_property, partial
+from functools import partial
+from transformers.video_utils import VideoMetadata
@@ -44,7 +45,6 @@
-from vllm.transformers_utils.processors.glm5next import glm_sample_frame_indices
@@ -616,37 +616,48 @@ def load_weights(self, weights) -> set[str]:
diff -- vllm/models/glm5next/common/model.py
@@ -6,6 +6,7 @@
```

- Reviewed files:
  - tests: `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389; `tests/models/multimodal/processing/test_glm5next.py` modified +16/-33
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +68/-52; `vllm/models/glm5next/common/model.py` modified +74/-26; `vllm/models/qwen4_exp/amd/model.py` modified +10/-37; `vllm/models/qwen4_exp/nvidia/model.py` modified +10/-37; `vllm/models/glm5next/common/attention.py` modified +18/-14; `vllm/models/glm5next/common/mtp.py` modified +4/-4
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_sequence_parallel.py`, `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_ple.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58008 - [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel

- Link: https://github.com/vllm-project/vllm/pull/58008
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_rocm_glm5next_sparse.py`; associated commits `2df122e65e87`
- Diff scope read: GitHub Pull Request files API returned 2 files, +109/-12, 165 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/v1/attention/test_rocm_glm5next_sparse.py`; technical summary: Covers "[ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel"; the main implementation surface is `tests/v1/attention/test_rocm_glm5next_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0 (44 lines); hunks: -8,6 +8,7; -26,6 +27,26 @@ def _store_sparse_kv_row_offset_kernel(slot_ptr, output_ptr,...; symbols: _store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history, touching `_store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history`.
- Code diff details:
  - `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0 (44 lines); hunks: -8,6 +8,7; -26,6 +27,26 @@ def _store_sparse_kv_row_offset_kernel(slot_ptr, output_ptr,...; symbols: _store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history
- Key code excerpts:

```diff
diff -- tests/v1/attention/test_rocm_glm5next_sparse.py
@@ -8,6 +8,7 @@
+from vllm.utils.torch_utils import set_random_seed
@@ -26,6 +27,26 @@ def _store_sparse_kv_row_offset_kernel(slot_ptr, output_ptr, stride: tl.constexp
+def _fit_kpool_indices_reference(
+    token_indices: torch.Tensor, topk_tokens: int
+) -> torch.Tensor:
+    history = token_indices[:, :topk_tokens]
```

- Reviewed files:
  - tests: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_rocm_glm5next_sparse.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57979 - [ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA

- Link: https://github.com/vllm-project/vllm/pull/57979
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`; associated commits `3627a6a12489`
- Diff scope read: GitHub Pull Request files API returned 3 files, +54/-19, 159 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `tests/models/glm5next/test_kda_recurrent.py`; technical summary: Covers "[ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA"; the main implementation surface is `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `tests/models/glm5next/test_kda_recurrent.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd, touching `token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`; `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, touching `fused_recurrent_kda_fwd, fused_recurrent_kda`; `tests/models/glm5next/test_kda_recurrent.py` modified +3/-4 (7 lines); hunks: -5,8 +5,7; -166,8 +165,8 @@ def test_fused_recurrent_kda_strided_inputs_bit_identical_to...; symbols: test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts, touching `test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts`.
- Code diff details:
  - `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda
  - `tests/models/glm5next/test_kda_recurrent.py` modified +3/-4 (7 lines); hunks: -5,8 +5,7; -166,8 +165,8 @@ def test_fused_recurrent_kda_strided_inputs_bit_identical_to...; symbols: test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py
@@ -15,6 +15,23 @@
+def token_stride(x: torch.Tensor) -> int:
+    """Token stride (elements) of a ``[B, T, H, D]`` or ``[B, T, H]`` tensor.
+    The recurrent kernel walks tokens with this stride and addresses heads
+    densely inside a token, so each token's ``[H, D]`` (or ``[H]``) block must
+    be contiguous, tokens must not overlap, and with ``B > 1`` sequence ``n``
+    must start at token ``n * T`` (dense batch). Column slices of a wider
diff -- vllm/models/glm5next/amd/ops/third_party/kda/kernels.py
@@ -24,7 +24,10 @@
-from .fused_recurrent import fused_recurrent_gated_delta_rule_fwd_kernel
+from .fused_recurrent import (
+    fused_recurrent_gated_delta_rule_fwd_kernel,
+    token_stride,
+)
@@ -70,7 +73,7 @@ def fused_recurrent_kda_fwd(
diff -- tests/models/glm5next/test_kda_recurrent.py
@@ -5,8 +5,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9; `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +3/-4
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_kda_recurrent.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55389 - [Model] Extend device-side mm normalization to GLM4V/GLM5Next

- Link: https://github.com/vllm-project/vllm/pull/55389
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/multimodal.py`; associated commits `0a30bc3f9ac3`
- Diff scope read: GitHub Pull Request files API returned 7 files, +114/-10, 279 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Extend device-side mm normalization to GLM4V/GLM5Next"; model line: GLM-5/5.1; category: docs/tests/CI; main diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Model] Extend device-side mm normalization to GLM4V/GLM5Next"; the main implementation surface is `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0 (37 lines); hunks: -13,8 +13,12; -168,3 +172,36 @@ def test_video_shorter_than_one_sampling_interval_is_reject...; symbols: test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize, touching `test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize`; `vllm/models/glm5next/common/multimodal.py` modified +4/-1 (5 lines); hunks: -19,6 +19,7; -353,6 +354,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/glm5next/common/model.py` modified +2/-0 (2 lines); hunks: -22,6 +22,7; -1103,6 +1104,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0 (37 lines); hunks: -13,8 +13,12; -168,3 +172,36 @@ def test_video_shorter_than_one_sampling_interval_is_reject...; symbols: test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize
  - `vllm/models/glm5next/common/multimodal.py` modified +4/-1 (5 lines); hunks: -19,6 +19,7; -353,6 +354,7 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/glm5next/common/model.py` modified +2/-0 (2 lines); hunks: -22,6 +22,7; -1103,6 +1104,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -13,8 +13,12 @@
+import torch
+from PIL import Image
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
+from vllm.platforms import current_platform
@@ -168,3 +172,36 @@ def test_video_shorter_than_one_sampling_interval_is_rejected(processor):
+@pytest.mark.usefixtures("default_vllm_config")
diff -- vllm/models/glm5next/common/multimodal.py
@@ -19,6 +19,7 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import IdentityInputNorm
@@ -353,6 +354,7 @@ def __init__(
+        input_norm: nn.Module | None = None,
@@ -386,6 +388,7 @@ def __init__(
+        self.input_norm = input_norm if input_norm is not None else IdentityInputNorm()
@@ -566,7 +569,7 @@ def forward(
diff -- vllm/models/glm5next/common/model.py
@@ -22,6 +22,7 @@
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +4/-1; `vllm/models/glm5next/common/model.py` modified +2/-0
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation_ppl_test/test_glm.py`, `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55222 - [Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace

- Link: https://github.com/vllm-project/vllm/pull/55222
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/common/attention.py`; associated commits `c37f86e5721f`
- Diff scope read: GitHub Pull Request files API returned 5 files, +84/-19, 206 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/common/attention.py`; technical summary: Covers "[Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace"; the main implementation surface is `vllm/models/glm5next/common/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/attention.py` modified +3/-1 (4 lines); hunks: -312,7 +312,9 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/glm5next/common/attention.py` modified +3/-1 (4 lines); hunks: -312,7 +312,9 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/attention.py
@@ -312,7 +312,9 @@ def __init__(
-        self.max_total_seq_len = get_max_prefill_buffer_size(vllm_config)
+        self.max_total_seq_len = (
+            get_max_prefill_buffer_size(vllm_config) // self.index_kpool
+        )
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/attention.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56960 - [Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash

- Link: https://github.com/vllm-project/vllm/pull/56960
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`; associated commits `3e2a7e74a556`
- Diff scope read: GitHub Pull Request files API returned 6 files, +307/-11, 478 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`; technical summary: Covers "[Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash"; the main implementation surface is `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0 (167 lines); hunks: -193,3 +193,170 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run, touching `test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run`; `vllm/models/glm5next/common/kda.py` modified +59/-3 (62 lines); hunks: -2,6 +2,8; -14,7 +16,14; symbols: Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype, _a_log_weight_loader, touching `Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype`.
- Code diff details:
  - `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0 (167 lines); hunks: -193,3 +193,170 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run
  - `vllm/models/glm5next/common/kda.py` modified +59/-3 (62 lines); hunks: -2,6 +2,8; -14,7 +16,14; symbols: Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype, _a_log_weight_loader
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_kda_recurrent.py
@@ -193,3 +193,170 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():
+@pytest.mark.parametrize("offset", [16, 144, 256])
+@pytest.mark.parametrize("dim_first", [False, True])
+@pytest.mark.parametrize("num_spec", [0, 3])
+@torch.inference_mode()
+def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_first, num_spec, offset):
+    """Restoring both cached states must reproduce an uninterrupted prefill."""
diff -- vllm/models/glm5next/common/kda.py
@@ -2,6 +2,8 @@
+from dataclasses import replace
@@ -14,7 +16,14 @@
+from vllm.model_executor.layers.mamba.checkpoint import (
+    MambaPrefillCheckpointMetadata,
+)
+from vllm.model_executor.layers.mamba.kda_checkpoint import (
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0
  - runtime: `vllm/models/glm5next/common/kda.py` modified +59/-3
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_kda_recurrent.py`, `tests/v1/attention/test_gdn_metadata_builder.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55647 - [Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler

- Link: https://github.com/vllm-project/vllm/pull/55647
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`; associated commits `65ed0a2642d2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +229/-0, 251 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler"; the main implementation surface is `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_glm5next.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows, test_video_placeholders_match_encoder_rows_when_presampled, touching `processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows`; `vllm/models/glm5next/common/multimodal.py` modified +59/-0 (59 lines); hunks: -4,6 +4,7; -42,6 +43,7; symbols: _get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info, touching `_get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info`.
- Code diff details:
  - `tests/models/multimodal/processing/test_glm5next.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows, test_video_placeholders_match_encoder_rows_when_presampled
  - `vllm/models/glm5next/common/multimodal.py` modified +59/-0 (59 lines); hunks: -4,6 +4,7; -42,6 +43,7; symbols: _get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -0,0 +1,170 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Video placeholder accounting for GLM-5.3-Flash.
+``Glm4vProcessingInfo._construct_video_placeholder`` emits one frame of
+placeholders per timestamp, so the timestamps returned by
+``_get_video_second_idx_glm46v`` decide how many placeholders the prompt gets
diff -- vllm/models/glm5next/common/multimodal.py
@@ -4,6 +4,7 @@
+from typing import Any
@@ -42,6 +43,7 @@
+from vllm.transformers_utils.processors.glm5next import glm_sample_frame_indices
@@ -656,6 +658,63 @@ def _get_video_max_pixels(self) -> int:
+    def _get_video_second_idx_glm46v(
+        self, metadata: dict[str, Any], total_frames: int
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` added +170/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +59/-0
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58454 - [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding

- Link: https://github.com/vllm-project/vllm/pull/58454
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; associated commits `2617fe938355`
- Diff scope read: GitHub Pull Request files API returned 5 files, +208/-49, 534 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding"; the main implementation surface is `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16 (34 lines); hunks: -327,37 +327,38 @@ def _kpool_tail_seed_kernel(; -385,6 +386,7 @@ def kpool_seed_tail_cache(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel, touching `_kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel`; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15 (32 lines); hunks: -387,14 +387,15 @@ def _kpool_tail_seed_kernel(; -405,18 +406,18 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel, touching `_kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel`; `vllm/models/glm5next/common/attention.py` modified +15/-3 (18 lines); hunks: -34,6 +34,7; -160,7 +161,7 @@ class Glm5NextTailCache(DeepseekV32IndexerCache):; symbols: Glm5NextTailCache, __init__, get_kv_cache_spec, get_attn_backend, touching `Glm5NextTailCache, __init__, get_kv_cache_spec`.
- Code diff details:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16 (34 lines); hunks: -327,37 +327,38 @@ def _kpool_tail_seed_kernel(; -385,6 +386,7 @@ def kpool_seed_tail_cache(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15 (32 lines); hunks: -387,14 +387,15 @@ def _kpool_tail_seed_kernel(; -405,18 +406,18 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel
  - `vllm/models/glm5next/common/attention.py` modified +15/-3 (18 lines); hunks: -34,6 +34,7; -160,7 +161,7 @@ class Glm5NextTailCache(DeepseekV32IndexerCache):; symbols: Glm5NextTailCache, __init__, get_kv_cache_spec, get_attn_backend
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/ops/kpool_compress.py
@@ -327,37 +327,38 @@ def _kpool_tail_seed_kernel(
+    RING: tl.constexpr,
-    """Copy token ``i``'s raw K + gate into its request's tail block.
+    """Copy token ``i``'s raw K + gate into its request's tail ring.
-    slot < 0). ``tslot = block * KPOOL + pos % KPOOL``; the destination is
-    ``tail[block, {0:K, 1:score}, pos % KPOOL, :]``.
+    slot < 0). ``tslot = block * RING + pos % RING``; the destination is
diff -- vllm/models/glm5next/nvidia/ops/kpool_compress.py
@@ -387,14 +387,15 @@ def _kpool_tail_seed_kernel(
+    RING: tl.constexpr,
-    """Copy token ``i``'s raw K + gate into its request's tail block.
+    """Copy token ``i``'s raw K + gate into its request's tail ring.
-    slot < 0). ``tslot = block * KPOOL + pos % KPOOL``; the destination is
-    ``tail[block, {0:K, 1:score}, pos % KPOOL, :]``.
+    slot < 0). ``tslot = block * RING + pos % RING``; the destination is
diff -- vllm/models/glm5next/common/attention.py
@@ -34,6 +34,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15; `vllm/models/glm5next/common/attention.py` modified +15/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_kpool_decode_update_batched.py`, `tests/v1/attention/test_kpool_tail_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55270 - [Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with

- Link: https://github.com/vllm-project/vllm/pull/55270
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `39724758e7b7`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`; technical summary: Covers "[Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with"; the main implementation surface is `vllm/models/glm5next/nvidia/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0 (1 lines); hunks: -558,6 +558,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, touching `sparse_attn_indexer_kpool`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0 (1 lines); hunks: -558,6 +558,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -558,6 +558,7 @@ def sparse_attn_indexer_kpool(
+            indices=decode_metadata.indices,
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/nvidia/sparse_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58061 - [Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard

- Link: https://github.com/vllm-project/vllm/pull/58061
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`; associated commits `c9b34fdb2d0c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +115/-0, 123 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard"; the main implementation surface is `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_sequence_parallel.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: _Attention, __init__, _fake_tensor_parallel_world, _forbidden_all_reduce, touching `_Attention, __init__, _fake_tensor_parallel_world`; `vllm/models/glm5next/common/model.py` modified +1/-0 (1 lines); hunks: -355,6 +355,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/models/glm5next/test_sequence_parallel.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: _Attention, __init__, _fake_tensor_parallel_world, _forbidden_all_reduce
  - `vllm/models/glm5next/common/model.py` modified +1/-0 (1 lines); hunks: -355,6 +355,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_sequence_parallel.py
@@ -0,0 +1,114 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.3-Flash sequence-parallel MoE layout.
+With DP > 1, TP > 1 and expert parallelism, ``Glm5NextModel`` shards the token
+dimension across the TP group once at the model entry and every layer runs its
+MLP on that shard. A module that still does tensor-parallel collectives there
diff -- vllm/models/glm5next/common/model.py
@@ -355,6 +355,7 @@ def __init__(
+                is_sequence_parallel=self.is_sequence_parallel,
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_sequence_parallel.py` added +114/-0
  - runtime: `vllm/models/glm5next/common/model.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_sequence_parallel.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57546 - [GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher

- Link: https://github.com/vllm-project/vllm/pull/57546
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `bf01fc4a313c`
- Diff scope read: GitHub Pull Request files API returned 4 files, +94/-83, 277 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`; technical summary: Covers "[GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher"; the main implementation surface is `vllm/models/glm5next/nvidia/sparse_indexer.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44 (64 lines); hunks: -10,6 +10,7; -39,21 +40,6; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool, __init__, forward_cuda, touching `_use_cooperative_topk, sparse_attn_indexer_kpool, __init__`; `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26 (54 lines); hunks: -1,41 +1,43; symbols: test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch, test_kpool_indexer_dispatches_through_shared_topk_backend, touching `test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44 (64 lines); hunks: -10,6 +10,7; -39,21 +40,6; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool, __init__, forward_cuda
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26 (54 lines); hunks: -1,41 +1,43; symbols: test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch, test_kpool_indexer_dispatches_through_shared_topk_backend
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -10,6 +10,7 @@
+from vllm.model_executor.layers.indexer_topk import get_indexer_topk
@@ -39,21 +40,6 @@
-def _use_cooperative_topk(
-    logits: torch.Tensor,
-    select_k: int,
-    num_rows: int,
diff -- tests/models/glm5next/test_sparse_indexer_topk_dispatch.py
@@ -1,41 +1,43 @@
-"""Focused unit tests for the GLM decode top-k dispatch."""
+"""Tests for the GLM kpool indexer's top-k backend wiring."""
-from vllm.models.glm5next.nvidia.sparse_indexer import _use_cooperative_topk
+from vllm.config import VllmConfig, set_current_vllm_config
-@pytest.mark.parametrize("num_rows", [1, 64], ids=["1row", "64rows"])
-@torch.inference_mode()
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57477 - [Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel

- Link: https://github.com/vllm-project/vllm/pull/57477
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; associated commits `db1bfdd4fb0d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +23/-5, 73 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; technical summary: Covers "[Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel"; the main implementation surface is `vllm/models/glm5next/nvidia/ops/kpool_compress.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2 (15 lines); hunks: -383,6 +383,8 @@ def _kpool_tail_seed_kernel(; -393,6 +395,11 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, touching `_kpool_tail_seed_kernel, kpool_seed_tail_cache`.
- Code diff details:
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2 (15 lines); hunks: -383,6 +383,8 @@ def _kpool_tail_seed_kernel(; -393,6 +395,11 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/nvidia/ops/kpool_compress.py
@@ -383,6 +383,8 @@ def _kpool_tail_seed_kernel(
+    TAIL_BLOCK_ELEMS: tl.constexpr,
+    KPOOL_HEAD: tl.constexpr,
@@ -393,6 +395,11 @@ def _kpool_tail_seed_kernel(
+    The tail cache aliases the indexer cache with the indexer's (padded) block
+    stride, so blocks are addressed through ``TAIL_BLOCK_ELEMS`` /
+    ``KPOOL_HEAD`` (``tail.stride(0)`` / ``tail.stride(1)``), never as a dense
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/test_kpool_decode_update_batched.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57701 - [GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved

- Link: https://github.com/vllm-project/vllm/pull/57701
- Status/date: merged / 2026-09-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `36fa72d2d0d2`
- Diff scope read: GitHub Pull Request files API returned 3 files, +17/-17, 153 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`; technical summary: Covers "[GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved"; the main implementation surface is `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8 (16 lines); hunks: -100,7 +100,7 @@ def sparse_attn_indexer_kpool(; -136,7 +136,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__, touching `sparse_attn_indexer_kpool, __init__`; `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7 (14 lines); hunks: -117,7 +117,7 @@ def sparse_attn_indexer_kpool(; -153,7 +153,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__, touching `sparse_attn_indexer_kpool, __init__`; `vllm/models/glm5next/common/attention.py` modified +2/-2 (4 lines); hunks: -296,7 +296,7 @@ def __init__(; -307,7 +307,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8 (16 lines); hunks: -100,7 +100,7 @@ def sparse_attn_indexer_kpool(; -136,7 +136,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7 (14 lines); hunks: -117,7 +117,7 @@ def sparse_attn_indexer_kpool(; -153,7 +153,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__
  - `vllm/models/glm5next/common/attention.py` modified +2/-2 (4 lines); hunks: -296,7 +296,7 @@ def __init__(; -307,7 +307,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -100,7 +100,7 @@ def sparse_attn_indexer_kpool(
-    max_model_len: int,
+    max_pool_len: int,
@@ -136,7 +136,7 @@ def sparse_attn_indexer_kpool(
-        # whose shape is [B * next_n, max_model_len]. This profiling branch
+        # whose shape is [B * next_n, max_pool_len]. This profiling branch
@@ -152,7 +152,7 @@ def sparse_attn_indexer_kpool(
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -117,7 +117,7 @@ def sparse_attn_indexer_kpool(
-    max_model_len: int,
+    max_pool_len: int,
@@ -153,7 +153,7 @@ def sparse_attn_indexer_kpool(
-        # whose shape is [B * next_n, max_model_len]. This profiling branch
+        # whose shape is [B * next_n, max_pool_len]. This profiling branch
@@ -169,7 +169,7 @@ def sparse_attn_indexer_kpool(
diff -- vllm/models/glm5next/common/attention.py
@@ -296,7 +296,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8; `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7; `vllm/models/glm5next/common/attention.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57425 - [Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)

- Link: https://github.com/vllm-project/vllm/pull/57425
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/sparse_indexer.py`; associated commits `d12c2768530a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +24/-1, 36 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/amd/sparse_indexer.py`; technical summary: Covers "[Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)"; the main implementation surface is `vllm/models/glm5next/amd/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1 (25 lines); hunks: -665,7 +665,7 @@ def __init__(; -727,3 +727,26 @@ def forward_native(; symbols: __init__, forward_native, forward_hip, touching `__init__, forward_native, forward_hip`.
- Code diff details:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1 (25 lines); hunks: -665,7 +665,7 @@ def __init__(; -727,3 +727,26 @@ def forward_native(; symbols: __init__, forward_native, forward_hip
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -665,7 +665,7 @@ def __init__(
-    def forward_native(
+    def forward_hip(
@@ -727,3 +727,26 @@ def forward_native(
+    def forward_native(
+        self,
+        hidden_states: torch.Tensor,
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/amd/sparse_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57327 - [Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches

- Link: https://github.com/vllm-project/vllm/pull/57327
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; associated commits `2bbdfcfcfea7`
- Diff scope read: GitHub Pull Request files API returned 2 files, +63/-1, 79 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`; technical summary: Covers "[Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches"; the main implementation surface is `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch, touching `test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch`; `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1 (23 lines); hunks: -38,6 +38,22; -573,7 +589,12 @@ def sparse_attn_indexer_kpool(; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool, touching `_use_cooperative_topk, sparse_attn_indexer_kpool`.
- Code diff details:
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1 (23 lines); hunks: -38,6 +38,22; -573,7 +589,12 @@ def sparse_attn_indexer_kpool(; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_sparse_indexer_topk_dispatch.py
@@ -0,0 +1,41 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Focused unit tests for the GLM decode top-k dispatch."""
+import pytest
+import torch
+from vllm.models.glm5next.nvidia.sparse_indexer import _use_cooperative_topk
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -38,6 +38,22 @@
+def _use_cooperative_topk(
+    logits: torch.Tensor,
+    select_k: int,
+    num_rows: int,
+) -> bool:
+    return (
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55358 - [Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA

- Link: https://github.com/vllm-project/vllm/pull/55358
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/sparse_indexer.py`; associated commits `4fe9e6f6e564`
- Diff scope read: GitHub Pull Request files API returned 6 files, +1008/-398, 1532 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/sparse_indexer.py`; technical summary: Covers "[Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA"; the main implementation surface is `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/sparse_indexer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0 (729 lines); hunks: -0,0 +1,729; symbols: _kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool, __init__, touching `_kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool`; `vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391 (467 lines); hunks: -2,30 +2,29; -36,16 +35,9; symbols: _kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, touching `_kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request`; `vllm/models/glm5next/common/sparse_indexer.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, _fill_causal_indices, touching `_build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens`; `vllm/models/glm5next/sparse_indexer.py` added +22/-0 (22 lines); hunks: -0,0 +1,22.
- Code diff details:
  - `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0 (729 lines); hunks: -0,0 +1,729; symbols: _kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool, __init__
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391 (467 lines); hunks: -2,30 +2,29; -36,16 +35,9; symbols: _kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens
  - `vllm/models/glm5next/common/sparse_indexer.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, _fill_causal_indices
  - `vllm/models/glm5next/sparse_indexer.py` added +22/-0 (22 lines); hunks: -0,0 +1,22
  - `vllm/models/glm5next/common/attention.py` modified +1/-1 (2 lines); hunks: -23,14 +23,14
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/sparse_indexer.py
@@ -0,0 +1,729 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Custom Sparse Attention Indexer layers."""
+import torch
+import vllm.envs as envs
+from vllm import _custom_ops  # noqa: F401  # registers the torch.ops._C kernels
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -2,30 +2,29 @@
-from typing import TYPE_CHECKING
-from vllm._aiter_ops import rocm_aiter_ops
+from vllm.models.glm5next.common.sparse_indexer import (
+    RADIX_TOPK_WORKSPACE_SIZE,
+    _build_decode_scatter_indices,
+    _decode_topk_seq_lens,
diff -- vllm/models/glm5next/common/sparse_indexer.py
@@ -0,0 +1,170 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0; `vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391; `vllm/models/glm5next/common/sparse_indexer.py` added +170/-0; `vllm/models/glm5next/sparse_indexer.py` added +22/-0; `vllm/models/glm5next/common/attention.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_sparse_indexer_decode_seq_lens.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56176 - [ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint

- Link: https://github.com/vllm-project/vllm/pull/56176
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py` and 7 files; associated commits `c8d1cf077a78`
- Diff scope read: GitHub Pull Request files API returned 8 files, +164/-4, 208 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`; technical summary: Covers "[ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint"; the main implementation surface is `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/common/model.py` renamed +14/-1 (15 lines); hunks: -1036,6 +1036,17 @@ class Glm5NextForConditionalGeneration(; -1259,7 +1270,9 @@ def _try_load_fp8_attn_proj(; symbols: Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj, touching `Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj`; `vllm/models/glm5next/__init__.py` modified +2/-2 (4 lines); hunks: -6,8 +6,8; `vllm/models/glm5next/common/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2; `vllm/models/glm5next/common/mtp.py` renamed +1/-1 (2 lines); hunks: -22,6 +22,7; -33,7 +34,6; symbols: Glm5NextMultiTokenPredictorLayer, touching `Glm5NextMultiTokenPredictorLayer`.
- Code diff details:
  - `vllm/models/glm5next/common/model.py` renamed +14/-1 (15 lines); hunks: -1036,6 +1036,17 @@ class Glm5NextForConditionalGeneration(; -1259,7 +1270,9 @@ def _try_load_fp8_attn_proj(; symbols: Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj
  - `vllm/models/glm5next/__init__.py` modified +2/-2 (4 lines); hunks: -6,8 +6,8
  - `vllm/models/glm5next/common/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/glm5next/common/mtp.py` renamed +1/-1 (2 lines); hunks: -22,6 +22,7; -33,7 +34,6; symbols: Glm5NextMultiTokenPredictorLayer
  - `vllm/models/glm5next/common/attention.py` renamed +0/-0 (0 lines)
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/common/model.py
@@ -1036,6 +1036,17 @@ class Glm5NextForConditionalGeneration(
+    # GLM-5.3-Flash stores the dense-MLP gate/up as separate tensors (like
+    # ``Glm4vMoeForConditionalGeneration``, ``glm4_moe`` and ``deepseek_v2``),
+    # so the fused ``gate_up_proj`` must expand to its real shard names for
+    # per-layer quant-scheme resolution. The identity ``gate_up_proj`` entry
+    # inherited from ``Glm4vForConditionalGeneration`` (pre-fused gate_up_proj)
+    # would otherwise route the module to ``global_quant_config`` and mismatch
diff -- vllm/models/glm5next/__init__.py
@@ -6,8 +6,8 @@
-from .nvidia.model import Glm5NextForCausalLM, Glm5NextForConditionalGeneration
-from .nvidia.mtp import Glm5NextMTP
+from .common.model import Glm5NextForCausalLM, Glm5NextForConditionalGeneration
+from .common.mtp import Glm5NextMTP
diff -- vllm/models/glm5next/common/__init__.py
@@ -0,0 +1,2 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/common/model.py` renamed +14/-1; `vllm/models/glm5next/__init__.py` modified +2/-2; `vllm/models/glm5next/common/__init__.py` added +2/-0; `vllm/models/glm5next/common/mtp.py` renamed +1/-1; `vllm/models/glm5next/common/attention.py` renamed +0/-0; `vllm/models/glm5next/common/kda.py` renamed +0/-0
- Risk and verification: The diff ships test coverage in `tests/quantization/test_quark.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55239 - [ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA

- Link: https://github.com/vllm-project/vllm/pull/55239
- Status/date: merged / 2026-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_rocm_glm5next_sparse.py`; associated commits `828f4f19b4d8`
- Diff scope read: GitHub Pull Request files API returned 2 files, +11/-5, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA"; model line: GLM-5/5.1; category: bug fix; main diff: `tests/v1/attention/test_rocm_glm5next_sparse.py`; technical summary: Covers "[ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA"; the main implementation surface is `tests/v1/attention/test_rocm_glm5next_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1 (5 lines); hunks: -76,7 +76,9 @@ def test_fit_kpool_indices_rejects_narrow_input():; -88,6 +90,7 @@ def test_rocm_sparse_triton_route(; symbols: test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route, touching `test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route`.
- Code diff details:
  - `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1 (5 lines); hunks: -76,7 +76,9 @@ def test_fit_kpool_indices_rejects_narrow_input():; -88,6 +90,7 @@ def test_rocm_sparse_triton_route(; symbols: test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route
- Key code excerpts:

```diff
diff -- tests/v1/attention/test_rocm_glm5next_sparse.py
@@ -76,7 +76,9 @@ def test_fit_kpool_indices_rejects_narrow_input():
-        ("auto", 512, 0, 2, 4, 2, False),
+        ("auto", 512, 0, 2, 4, 2, True),
+        ("auto", 512, 0, 2, 12, 6, True),
+        ("auto", 512, 0, 0, 0, 0, False),
@@ -88,6 +90,7 @@ def test_rocm_sparse_triton_route(
+    """Validate Triton routing for prefill, decode, and MTP verification."""
```

- Reviewed files:
  - tests: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_rocm_glm5next_sparse.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55736 - [Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM

- Link: https://github.com/vllm-project/vllm/pull/55736
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/glm5next/__init__.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`; associated commits `1768273c13d8`
- Diff scope read: GitHub Pull Request files API returned 8 files, +268/-27, 399 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`; technical summary: Covers "[Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM"; the main implementation surface is `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/glm5next/test_kda_recurrent.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: naive_recurrent_kda, make_inputs, run_kernel, test_fused_recurrent_kda_matches_reference, touching `naive_recurrent_kda, make_inputs, run_kernel`; `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd, touching `token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, touching `fused_recurrent_kda_fwd, fused_recurrent_kda`; `tests/models/glm5next/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2.
- Code diff details:
  - `tests/models/glm5next/test_kda_recurrent.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: naive_recurrent_kda, make_inputs, run_kernel, test_fused_recurrent_kda_matches_reference
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda
  - `tests/models/glm5next/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- Key code excerpts:

```diff
diff -- tests/models/glm5next/test_kda_recurrent.py
@@ -0,0 +1,186 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.3-Flash KDA recurrent (decode) kernel.
+The decode path hands the kernel column slices of the merged ``q|k|v`` conv
+output and of the fused ``qkvbfg_a`` projection (beta), so q/k/v/beta are
+token-strided rather than contiguous. The kernel must read them in place,
diff -- vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py
@@ -15,6 +15,23 @@
+def token_stride(x: torch.Tensor) -> int:
+    """Token stride (elements) of a ``[B, T, H, D]`` or ``[B, T, H]`` tensor.
+    The recurrent kernel walks tokens with this stride and addresses heads
+    densely inside a token, so each token's ``[H, D]`` (or ``[H]``) block must
+    be contiguous, tokens must not overlap, and with ``B > 1`` sequence ``n``
+    must start at token ``n * T`` (dense batch). Column slices of a wider
diff -- vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py
@@ -24,7 +24,10 @@
```

- Reviewed files:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` added +186/-0; `tests/models/glm5next/__init__.py` added +2/-0
  - runtime: `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6
- Risk and verification: The diff ships test coverage in `tests/models/glm5next/__init__.py`, `tests/models/glm5next/test_kda_recurrent.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55214 - [Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings

- Link: https://github.com/vllm-project/vllm/pull/55214
- Status/date: merged / 2026-09-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`, `vllm/models/glm5next/nvidia/ops/__init__.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; associated commits `78300cdabffb`
- Diff scope read: GitHub Pull Request files API returned 4 files, +12/-4, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings"; model line: GLM-5/5.1; category: bug fix; main diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`; technical summary: Covers "[Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings"; the main implementation surface is `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -631,9 +631,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched, touching `kpool_decode_update_and_maybe_write_cache_batched`; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -637,9 +637,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched, touching `kpool_decode_update_and_maybe_write_cache_batched`; `vllm/models/glm5next/nvidia/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2; `vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2.
- Code diff details:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -631,9 +631,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -637,9 +637,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched
  - `vllm/models/glm5next/nvidia/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/ops/kpool_compress.py
@@ -631,9 +631,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(
-        key / slot_score: ``[num_requests, next_n, head_dim]`` bf16.
+        key: ``[num_requests, next_n, head_dim]`` bf16.
+        slot_score: ``[num_requests, next_n, head_dim]`` bf16.
-        slot_mapping / positions: ``[num_requests, next_n]`` int32.
+        slot_mapping: ``[num_requests, next_n]`` int32.
+        positions: ``[num_requests, next_n]`` int32.
diff -- vllm/models/glm5next/nvidia/ops/kpool_compress.py
@@ -637,9 +637,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(
-        key / slot_score: ``[num_requests, next_n, head_dim]`` bf16.
+        key: ``[num_requests, next_n, head_dim]`` bf16.
+        slot_score: ``[num_requests, next_n, head_dim]`` bf16.
-        slot_mapping / positions: ``[num_requests, next_n]`` int32.
+        slot_mapping: ``[num_requests, next_n]`` int32.
+        positions: ``[num_requests, next_n]`` int32.
diff -- vllm/models/glm5next/nvidia/__init__.py
@@ -0,0 +1,2 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2; `vllm/models/glm5next/nvidia/__init__.py` added +2/-0; `vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`, `vllm/models/glm5next/nvidia/ops/__init__.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #53906 - [Model] add GLM-5.3-Flash support

- Link: https://github.com/vllm-project/vllm/pull/53906
- Status/date: merged / 2026-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/amd/__init__.py`, `vllm/models/glm5next/amd/ops/__init__.py`, `vllm/models/glm5next/amd/ops/kpool_compress.py` and 15 files; associated commits `98ed0856f31f`
- Diff scope read: GitHub Pull Request files API returned 94 files, +17926/-265, 19713 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] add GLM-5.3-Flash support"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`; technical summary: Covers "[Model] add GLM-5.3-Flash support"; the main implementation surface is `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra, touching `fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter`; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra, touching `fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter`; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0 (891 lines); hunks: -0,0 +1,891; symbols: _hadamard128_stage, _hadamard128, _fwht_stage, _fwht_quant_kernel, touching `_hadamard128_stage, _hadamard128, _fwht_stage`; `vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0 (890 lines); hunks: -0,0 +1,890; symbols: _cache_k_offset, _hadamard128_stage, _hadamard128, compute_pooled_write_locs, touching `_cache_k_offset, _hadamard128_stage, _hadamard128`.
- Code diff details:
  - `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0 (891 lines); hunks: -0,0 +1,891; symbols: _hadamard128_stage, _hadamard128, _fwht_stage, _fwht_quant_kernel
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0 (890 lines); hunks: -0,0 +1,890; symbols: _cache_k_offset, _hadamard128_stage, _hadamard128, compute_pooled_write_locs
  - `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` added +656/-0 (656 lines); hunks: -0,0 +1,656; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd, fused_recurrent_gated_delta_rule_packed_decode_kernel, fused_recurrent_gated_delta_rule_packed_decode
- Key code excerpts:

```diff
diff -- vllm/models/glm5next/amd/ops/third_party/kda/kernels.py
@@ -0,0 +1,1362 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# SPDX-FileCopyrightText: Songlin Yang, Yu Zhang
+# mypy: ignore-errors
+#
+# This file contains code copied from the flash-linear-attention project.
diff -- vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py
@@ -0,0 +1,1362 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# SPDX-FileCopyrightText: Songlin Yang, Yu Zhang
+# mypy: ignore-errors
+#
+# This file contains code copied from the flash-linear-attention project.
diff -- vllm/models/glm5next/nvidia/ops/kpool_compress.py
@@ -0,0 +1,891 @@
```

- Reviewed files:
  - runtime: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0; `vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0; `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` added +656/-0; `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` added +656/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_flashinfer_mla_decode.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/kernels/mamba/test_gdn_prefill_flashinfer.py`, `tests/kernels/test_kpool_decode_update_batched.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53785 - [Attention] Enable dense and masked MHA for GLM-5

- Link: https://github.com/vllm-project/vllm/pull/53785
- Status/date: merged / 2026-08-27
- Trace source: `git log --name-only -- <model-files>` found it through `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`; associated commits `de9250ac9e9b`
- Diff scope read: GitHub Pull Request files API returned 10 files, +527/-74, 846 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention] Enable dense and masked MHA for GLM-5"; model line: GLM-5/5.1; category: docs/tests/CI; main diff: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`; technical summary: Covers "[Attention] Enable dense and masked MHA for GLM-5"; the main implementation surface is `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0 (59 lines); hunks: -0,0 +1,59.
- Code diff details:
  - `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0 (59 lines); hunks: -0,0 +1,59
- Key code excerpts:

```diff
diff -- benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml
@@ -0,0 +1,59 @@
+mode: mha_vs_mqa
+model:
+  name: "glm-5.x"
+  num_layers: 78
+  num_q_heads: 64
+  num_kv_heads: 1
```

- Reviewed files:
  - runtime: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_backends.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51015 - [CI] Stabilize GLM-5.2 PCP evaluation

- Link: https://github.com/vllm-project/vllm/pull/51015
- Status/date: merged / 2026-08-04
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`; associated commits `a5149b2feeb7`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 7 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Stabilize GLM-5.2 PCP evaluation"; model line: GLM-5/5.1; category: performance/backend optimization; main diff: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`; technical summary: Covers "[CI] Stabilize GLM-5.2 PCP evaluation"; the main implementation surface is `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0 (1 lines); hunks: -13,5 +13,6 @@ server_args: >-.
- Code diff details:
  - `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0 (1 lines); hunks: -13,5 +13,6 @@ server_args: >-
- Key code excerpts:

```diff
diff -- tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml
@@ -13,5 +13,6 @@ server_args: >-
+  PYTORCH_CUDA_ALLOC_CONF: "expandable_segments:True"
```

- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #49791 - [Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2

- Link: https://github.com/vllm-project/vllm/pull/49791
- Status/date: merged / 2026-08-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; associated commits `c8109375733e`
- Diff scope read: GitHub Pull Request files API returned 7 files, +619/-51, 965 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2"; model line: GLM-5/5.1; category: model implementation change; main diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`; technical summary: Covers "[Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2"; the main implementation surface is `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: GLM52ProjectionSpec, build_plan, _is_sm103, _is_supported_row_major, touching `GLM52ProjectionSpec, build_plan, _is_sm103`.
- Code diff details:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: GLM52ProjectionSpec, build_plan, _is_sm103, _is_supported_row_major
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py
@@ -0,0 +1,199 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""GLM-5.2 decode GEMM selection for unquantized BF16 on SM103."""
+from __future__ import annotations
+from dataclasses import dataclass
+from typing import Literal
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_bf16_skinny_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
