# vllm GLM-5/5.1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` | [#53785](https://github.com/vllm-project/vllm/pull/53785) |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-HiSparse.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-DCP4-EP.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` | [#51015](https://github.com/vllm-project/vllm/pull/51015) |
| `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml` | 无直接 PR 号提交 |
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

## 逐 PR diff 审计卡

### PR #60895 - [Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts

- 链接: https://github.com/vllm-project/vllm/pull/60895
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`, `vllm/models/glm5next/nvidia/mega_moe.py`；关联提交 `7e3c015543a3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+656/-3，可读 patch 779 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/nvidia/mega_moe.py`, `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts」；主要实现面是 `tests/models/glm5next/test_mega_moe.py`, `vllm/models/glm5next/nvidia/mega_moe.py`, `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_mega_moe.py` added +277/-0 (277 lines); hunks: -0,0 +1,277; symbols: sm100_mega_moe_layout, _block_fp8, _dequant_block, _dequant_ue8m0，涉及 `sm100_mega_moe_layout, _block_fp8, _dequant_block`；`vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts, _create_weights，涉及 `Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts`；`vllm/models/glm5next/common/model.py` modified +110/-3 (113 lines); hunks: -9,7 +9,8; -24,6 +25,9; symbols: __init__, _init_mega_moe_experts, finalize_mega_moe_weights，涉及 `__init__, _init_mega_moe_experts, finalize_mega_moe_weights`；`vllm/models/glm5next/common/mtp.py` modified +15/-0 (15 lines); hunks: -8,6 +8,7; -211,6 +212,9 @@ def get_top_tokens(; symbols: get_top_tokens, Glm5NextMTP, __init__, load_weights，涉及 `get_top_tokens, Glm5NextMTP, __init__`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_mega_moe.py` added +277/-0 (277 lines); hunks: -0,0 +1,277; symbols: sm100_mega_moe_layout, _block_fp8, _dequant_block, _dequant_ue8m0
  - `vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: Glm5NextMegaMoEExperts, __init__, _fusable_shared_experts, _create_weights
  - `vllm/models/glm5next/common/model.py` modified +110/-3 (113 lines); hunks: -9,7 +9,8; -24,6 +25,9; symbols: __init__, _init_mega_moe_experts, finalize_mega_moe_weights
  - `vllm/models/glm5next/common/mtp.py` modified +15/-0 (15 lines); hunks: -8,6 +8,7; -211,6 +212,9 @@ def get_top_tokens(; symbols: get_top_tokens, Glm5NextMTP, __init__, load_weights
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_mega_moe.py` added +277/-0
  - runtime: `vllm/models/glm5next/nvidia/mega_moe.py` added +228/-0; `vllm/models/glm5next/common/model.py` modified +110/-3; `vllm/models/glm5next/common/mtp.py` modified +15/-0
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_mega_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60919 - [JIT][ROCm] Fully warmup GLM-5.3-Flash

- 链接: https://github.com/vllm-project/vllm/pull/60919
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`；关联提交 `beaa72618e3b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+310/-47，可读 patch 531 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[JIT][ROCm] Fully warmup GLM-5.3-Flash」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`；技术摘要: 覆盖「[JIT][ROCm] Fully warmup GLM-5.3-Flash」；主要实现面是 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28 (179 lines); hunks: -12,8 +12,16; -68,7 +76,7 @@ def _hadamard128(x):; symbols: _hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs, kpool_compress_dispatch，涉及 `_hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs`；`vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0 (16 lines); hunks: -754,6 +754,22 @@ def __init__(; symbols: __init__, forward_hip，涉及 `__init__, forward_hip`；`vllm/models/glm5next/common/kda.py` modified +6/-0 (6 lines); hunks: -48,6 +48,7; -358,6 +359,11 @@ def _a_log_weight_loader(param, loaded_weight):; symbols: _a_log_weight_loader，涉及 `_a_log_weight_loader`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28 (179 lines); hunks: -12,8 +12,16; -68,7 +76,7 @@ def _hadamard128(x):; symbols: _hadamard128, _kpool_softmax_rotate_write_cache_kernel, _kpool_compress_warmup_inputs, kpool_compress_dispatch
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0 (16 lines); hunks: -754,6 +754,22 @@ def __init__(; symbols: __init__, forward_hip
  - `vllm/models/glm5next/common/kda.py` modified +6/-0 (6 lines); hunks: -48,6 +48,7; -358,6 +359,11 @@ def _a_log_weight_loader(param, loaded_weight):; symbols: _a_log_weight_loader
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +151/-28; `vllm/models/glm5next/amd/sparse_indexer.py` modified +16/-0; `vllm/models/glm5next/common/kda.py` modified +6/-0
- 验证与风险: diff 自带测试面 `tests/model_executor/test_jit_warmup_triton_launcher.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #61614 - [Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly

- 链接: https://github.com/vllm-project/vllm/pull/61614
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/kda.py`；关联提交 `602811546b03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-5，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/common/kda.py`；技术摘要: 覆盖「[Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly」；主要实现面是 `vllm/models/glm5next/common/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/kda.py` modified +5/-4 (9 lines); hunks: -424,11 +424,12 @@ def _flashkda_prefill(; symbols: _flashkda_prefill，涉及 `_flashkda_prefill`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/kda.py` modified +5/-4 (9 lines); hunks: -424,11 +424,12 @@ def _flashkda_prefill(; symbols: _flashkda_prefill
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/kda.py` modified +5/-4
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/common/kda.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #64644 - [CI] Fix mypy errors in test_glm5next.py

- 链接: https://github.com/vllm-project/vllm/pull/64644
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm5next.py`；关联提交 `335dd77b0916`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-5，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Fix mypy errors in test_glm5next.py」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`；技术摘要: 覆盖「[CI] Fix mypy errors in test_glm5next.py」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames，涉及 `test_glm5_raw_video_timestamps_follow_sampled_frames`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64071 - [EPD] Metadata-only image and video inputs for GLM-5.3-Flash

- 链接: https://github.com/vllm-project/vllm/pull/64071
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_epd_metadata.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`；关联提交 `a17e79abde45`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+636/-52，可读 patch 834 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[EPD] Metadata-only image and video inputs for GLM-5.3-Flash」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/glm5next/test_epd_metadata.py`, `vllm/models/glm5next/common/multimodal.py`；技术摘要: 覆盖「[EPD] Metadata-only image and video inputs for GLM-5.3-Flash」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/glm5next/test_epd_metadata.py`, `vllm/models/glm5next/common/multimodal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1 (215 lines); hunks: -9,9 +9,14; -21,13 +26,179; symbols: _video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames, processor，涉及 `_video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames`；`tests/models/glm5next/test_epd_metadata.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size，涉及 `test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size`；`vllm/models/glm5next/common/multimodal.py` modified +8/-9 (17 lines); hunks: -713,13 +713,15 @@ def _get_video_second_idx_glm46v(; -820,10 +822,7 @@ def _get_vision_info(; symbols: _get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor, _hf_processor_applies_updates，涉及 `_get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1 (215 lines); hunks: -9,9 +9,14; -21,13 +26,179; symbols: _video_with_metadata, test_glm5_metadata_only_roundtrip, test_glm5_raw_video_timestamps_follow_sampled_frames, processor
  - `tests/models/glm5next/test_epd_metadata.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: test_glm5_image_metadata_requires_ec_consumer, test_glm5_video_metadata_requires_timestamps, test_glm_dict_embeds_must_match_grid_and_hidden_size
  - `vllm/models/glm5next/common/multimodal.py` modified +8/-9 (17 lines); hunks: -713,13 +713,15 @@ def _get_video_second_idx_glm46v(; -820,10 +822,7 @@ def _get_vision_info(; symbols: _get_video_second_idx_glm46v, _get_vision_info, Glm5NextMultiModalProcessor, _hf_processor_applies_updates
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +214/-1; `tests/models/glm5next/test_epd_metadata.py` added +132/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +8/-9
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_epd_metadata.py`, `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60229 - [Spec Decode][GLM-5.3-Flash] Support adaptive verification

- 链接: https://github.com/vllm-project/vllm/pull/60229
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/sparse_indexer.py`；关联提交 `cebe1097232e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+287/-16，可读 patch 495 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec Decode][GLM-5.3-Flash] Support adaptive verification」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/common/sparse_indexer.py`；技术摘要: 覆盖「[Spec Decode][GLM-5.3-Flash] Support adaptive verification」；主要实现面是 `vllm/models/glm5next/common/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10 (39 lines); hunks: -16,29 +16,45 @@ def _build_decode_scatter_indices(; -59,14 +75,17 @@ def _scatter_decode_tokens_by_request(; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens，涉及 `_build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10 (39 lines); hunks: -16,29 +16,45 @@ def _build_decode_scatter_indices(; -59,14 +75,17 @@ def _scatter_decode_tokens_by_request(; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/sparse_indexer.py` modified +29/-10
- 验证与风险: diff 自带测试面 `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64481 - [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100

- 链接: https://github.com/vllm-project/vllm/pull/64481
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；关联提交 `1ca0dfb97612`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+129/-5，可读 patch 176 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；技术摘要: 覆盖「[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100」；主要实现面是 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3 (129 lines); hunks: -1,10 +1,11; -208,12 +209,134 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _low_latency_table，涉及 `build_plan, _low_latency_table`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3 (129 lines); hunks: -1,10 +1,11; -208,12 +209,134 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _low_latency_table
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +126/-3
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60991 - [Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter

- 链接: https://github.com/vllm-project/vllm/pull/60991
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_kda_conv_weight_refit.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`；关联提交 `de096755ad7b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+184/-46，可读 patch 274 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/glm5next/test_kda_conv_weight_refit.py`, `vllm/models/glm5next/common/kda.py`, `tests/models/glm5next/test_kda_recurrent.py`；技术摘要: 覆盖「[Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter」；主要实现面是 `tests/models/glm5next/test_kda_conv_weight_refit.py`, `vllm/models/glm5next/common/kda.py`, `tests/models/glm5next/test_kda_recurrent.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: _checkpoint_weights, _load, _kernel_view, conv1d，涉及 `_checkpoint_weights, _load, _kernel_view`；`vllm/models/glm5next/common/kda.py` modified +44/-44 (88 lines); hunks: -21,6 +21,9; -160,6 +163,36 @@ def _resolve_kda_prefill_backend(; symbols: _resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention, __init__，涉及 `_resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention`；`tests/models/glm5next/test_kda_recurrent.py` modified +3/-2 (5 lines); hunks: -303,8 +303,9 @@ def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_...; symbols: test_prefill_checkpoint_resumes_suffix，涉及 `test_prefill_checkpoint_resumes_suffix`；`vllm/models/glm5next/common/model.py` modified +4/-0 (4 lines); hunks: -874,6 +874,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: _checkpoint_weights, _load, _kernel_view, conv1d
  - `vllm/models/glm5next/common/kda.py` modified +44/-44 (88 lines); hunks: -21,6 +21,9; -160,6 +163,36 @@ def _resolve_kda_prefill_backend(; symbols: _resolve_kda_prefill_backend, _fused_qkv_conv1d, Glm5NextLinearAttention, __init__
  - `tests/models/glm5next/test_kda_recurrent.py` modified +3/-2 (5 lines); hunks: -303,8 +303,9 @@ def test_prefill_checkpoint_resumes_suffix(monkeypatch, dim_...; symbols: test_prefill_checkpoint_resumes_suffix
  - `vllm/models/glm5next/common/model.py` modified +4/-0 (4 lines); hunks: -874,6 +874,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_kda_conv_weight_refit.py` added +133/-0; `tests/models/glm5next/test_kda_recurrent.py` modified +3/-2
  - runtime: `vllm/models/glm5next/common/kda.py` modified +44/-44; `vllm/models/glm5next/common/model.py` modified +4/-0
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_kda_conv_weight_refit.py`, `tests/models/glm5next/test_kda_recurrent.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62843 - [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107

- 链接: https://github.com/vllm-project/vllm/pull/62843
- 状态/时间: merged / 2026-10-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；关联提交 `38955340b752`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+239/-55，可读 patch 430 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；技术摘要: 覆盖「[Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107」；主要实现面是 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8 (150 lines); hunks: -1,6 +1,13; -64,7 +71,7 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _is_sm103, _low_latency_table, _is_supported_row_major，涉及 `build_plan, _is_sm103, _low_latency_table`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8 (150 lines); hunks: -1,6 +1,13; -64,7 +71,7 @@ def build_plan(self) -> dict[int, ResolvedCall]:; symbols: build_plan, _is_sm103, _low_latency_table, _is_supported_row_major
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` modified +142/-8
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60753 - [Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk

- 链接: https://github.com/vllm-project/vllm/pull/60753
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/sparse_indexer.py`；关联提交 `3f729dafcc5a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+146/-10，可读 patch 164 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/sparse_indexer.py`；技术摘要: 覆盖「[Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk」；主要实现面是 `vllm/models/glm5next/amd/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10 (37 lines); hunks: -396,16 +396,33 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool，涉及 `sparse_attn_indexer_kpool`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10 (37 lines); hunks: -396,16 +396,33 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +27/-10
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/amd/sparse_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #59147 - [Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state

- 链接: https://github.com/vllm-project/vllm/pull/59147
- 状态/时间: merged / 2026-10-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`；关联提交 `f26d9f432ced`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+47/-2，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state」；主要实现面是 `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_kda_recurrent_state_dtype_follows_ssm_cache_dtype，涉及 `test_kda_recurrent_state_dtype_follows_ssm_cache_dtype`；`vllm/models/glm5next/common/kda.py` modified +3/-1 (4 lines); hunks: -181,7 +181,9 @@ def get_state_dtype(; symbols: get_state_dtype, get_state_shape，涉及 `get_state_dtype, get_state_shape`；`vllm/models/glm5next/common/model.py` modified +3/-1 (4 lines); hunks: -1092,7 +1092,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config，涉及 `get_mamba_state_dtype_from_config`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_kda_recurrent_state_dtype_follows_ssm_cache_dtype
  - `vllm/models/glm5next/common/kda.py` modified +3/-1 (4 lines); hunks: -181,7 +181,9 @@ def get_state_dtype(; symbols: get_state_dtype, get_state_shape
  - `vllm/models/glm5next/common/model.py` modified +3/-1 (4 lines); hunks: -1092,7 +1092,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_kda_state_dtype.py` added +41/-0
  - runtime: `vllm/models/glm5next/common/kda.py` modified +3/-1; `vllm/models/glm5next/common/model.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_kda_state_dtype.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54951 - [Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP

- 链接: https://github.com/vllm-project/vllm/pull/54951
- 状态/时间: merged / 2026-10-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `3e8e1364ff41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+436/-38，可读 patch 658 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`；技术摘要: 覆盖「[Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP」；主要实现面是 `vllm/models/glm5next/nvidia/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23 (63 lines); hunks: -12,7 +12,11; -169,6 +173,10 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool，涉及 `sparse_attn_indexer_kpool`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23 (63 lines); hunks: -12,7 +12,11; -169,6 +173,10 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +40/-23
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_indexer_tp_row_shard.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57169 - [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots

- 链接: https://github.com/vllm-project/vllm/pull/57169
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/attention/test_glm5next_indexer_block_sizes.py`, `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；关联提交 `02e55d2af38a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 83 个文件，+1281/-1987，可读 patch 6039 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/common/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；技术摘要: 覆盖「[KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots」；主要实现面是 `vllm/models/glm5next/common/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/attention.py` modified +14/-50 (64 lines); hunks: -33,9 +33,9; -89,15 +89,9 @@ class Glm5NextIndexerCache(DeepseekV32IndexerCache):; symbols: Glm5NextIndexerCache, __init__, get_kv_cache_spec，涉及 `Glm5NextIndexerCache, __init__, get_kv_cache_spec`；`vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8 (8 lines); hunks: -1376,14 +1376,6 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> K...; symbols: get_kv_cache_spec, _v_up_proj，涉及 `get_kv_cache_spec, _v_up_proj`；`vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5 (5 lines); hunks: -396,11 +396,6 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel，涉及 `_kpool_tail_seed_kernel`；`tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0 (46 lines); hunks: -313,3 +313,49 @@ def test_deepgemm_fp8_fp4_paged_mqa_logits(batch_size: int,...; symbols: test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride，涉及 `test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/attention.py` modified +14/-50 (64 lines); hunks: -33,9 +33,9; -89,15 +89,9 @@ class Glm5NextIndexerCache(DeepseekV32IndexerCache):; symbols: Glm5NextIndexerCache, __init__, get_kv_cache_spec
  - `vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8 (8 lines); hunks: -1376,14 +1376,6 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> K...; symbols: get_kv_cache_spec, _v_up_proj
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5 (5 lines); hunks: -396,11 +396,6 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel
  - `tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0 (46 lines); hunks: -313,3 +313,49 @@ def test_deepgemm_fp8_fp4_paged_mqa_logits(batch_size: int,...; symbols: test_deepgemm_fp8_fp4_paged_mqa_logits, test_deepgemm_paged_mqa_packed_manager_block_stride
  - `tests/v1/attention/test_glm5next_indexer_block_sizes.py` added +40/-0 (40 lines); hunks: -0,0 +1,40; symbols: test_glm5next_indexer_kernel_block_sizes
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/attention.py` modified +14/-50; `vllm/model_executor/layers/attention/mla_attention.py` modified +0/-8; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +0/-5
  - tests: `tests/kernels/attention/test_deepgemm_attention.py` modified +46/-0; `tests/v1/attention/test_glm5next_indexer_block_sizes.py` added +40/-0; `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +6/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60763 - [Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config

- 链接: https://github.com/vllm-project/vllm/pull/60763
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/model.py`；关联提交 `d095e61c0b38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config」；主要实现面是 `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/model.py` modified +1/-1 (2 lines); hunks: -788,7 +788,7 @@ def _aux_hidden_state(; symbols: _aux_hidden_state, forward，涉及 `_aux_hidden_state, forward`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/model.py` modified +1/-1 (2 lines); hunks: -788,7 +788,7 @@ def _aux_hidden_state(; symbols: _aux_hidden_state, forward
- 关键代码摘录:

```diff
diff -- vllm/models/glm5next/common/model.py
@@ -788,7 +788,7 @@ def _aux_hidden_state(
-        return hc_contract(completed, self.config.mhc_num_residual_streams)
+        return hc_contract(completed, self.config.hc_mult)
```

- 已读文件:
  - runtime: `vllm/models/glm5next/common/model.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/common/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #56983 - [Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash

- 链接: https://github.com/vllm-project/vllm/pull/56983
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/model.py`；关联提交 `2274e86842d6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+47/-4，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash」；主要实现面是 `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/model.py` modified +47/-4 (51 lines); hunks: -66,9 +66,11; -684,7 +686,7 @@ def hc_fused_post_pre(; symbols: hc_fused_post_pre, Glm5NextModel, __init__, get_layer，涉及 `hc_fused_post_pre, Glm5NextModel, __init__`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/model.py` modified +47/-4 (51 lines); hunks: -66,9 +66,11; -684,7 +686,7 @@ def hc_fused_post_pre(; symbols: hc_fused_post_pre, Glm5NextModel, __init__, get_layer
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/model.py` modified +47/-4
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/common/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #60032 - [Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer

- 链接: https://github.com/vllm-project/vllm/pull/60032
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `70bdce6133d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-0，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`；技术摘要: 覆盖「[Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer」；主要实现面是 `vllm/models/glm5next/nvidia/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0 (9 lines); hunks: -26,6 +26,7; -717,6 +718,14 @@ def __init__(; symbols: __init__, cp_kv_cache_interleave_size，涉及 `__init__, cp_kv_cache_interleave_size`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0 (9 lines); hunks: -26,6 +26,7; -717,6 +718,14 @@ def __init__(; symbols: __init__, cp_kv_cache_interleave_size
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +9/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/nvidia/sparse_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #59221 - [ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950

- 链接: https://github.com/vllm-project/vllm/pull/59221
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`；关联提交 `2a54f6b625f2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+213/-6，可读 patch 362 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`；技术摘要: 覆盖「[ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950」；主要实现面是 `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/model.py` modified +82/-3 (85 lines); hunks: -23,6 +23,10; -258,7 +262,12 @@ def __init__(; symbols: __init__, get_layer, load_weights，涉及 `__init__, get_layer, load_weights`；`vllm/models/glm5next/common/mtp.py` modified +14/-1 (15 lines); hunks: -10,6 +10,9; -30,6 +33,8; symbols: __init__, set_moe_parameters, load_weights，涉及 `__init__, set_moe_parameters, load_weights`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/model.py` modified +82/-3 (85 lines); hunks: -23,6 +23,10; -258,7 +262,12 @@ def __init__(; symbols: __init__, get_layer, load_weights
  - `vllm/models/glm5next/common/mtp.py` modified +14/-1 (15 lines); hunks: -10,6 +10,9; -30,6 +33,8; symbols: __init__, set_moe_parameters, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/model.py` modified +82/-3; `vllm/models/glm5next/common/mtp.py` modified +14/-1
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_fused_shared_expert.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59211 - [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer

- 链接: https://github.com/vllm-project/vllm/pull/59211
- 状态/时间: merged / 2026-10-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `30d4032363d4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+242/-37，可读 patch 537 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`；技术摘要: 覆盖「[Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer」；主要实现面是 `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27 (113 lines); hunks: -7,10 +7,12; -121,6 +123,9 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool，涉及 `sparse_attn_indexer_kpool`；`vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0 (4 lines); hunks: -733,6 +733,10 @@ def __init__(; symbols: __init__, forward_hip，涉及 `__init__, forward_hip`；`vllm/models/glm5next/common/attention.py` modified +3/-0 (3 lines); hunks: -209,6 +209,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig):; symbols: get_kv_cache_spec, get_attn_backend，涉及 `get_kv_cache_spec, get_attn_backend`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27 (113 lines); hunks: -7,10 +7,12; -121,6 +123,9 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0 (4 lines); hunks: -733,6 +733,10 @@ def __init__(; symbols: __init__, forward_hip
  - `vllm/models/glm5next/common/attention.py` modified +3/-0 (3 lines); hunks: -209,6 +209,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig):; symbols: get_kv_cache_spec, get_attn_backend
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +86/-27; `vllm/models/glm5next/amd/sparse_indexer.py` modified +4/-0; `vllm/models/glm5next/common/attention.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/core/test_kv_cache_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56974 - [Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel

- 链接: https://github.com/vllm-project/vllm/pull/56974
- 状态/时间: merged / 2026-10-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`；关联提交 `ae53b06898bc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+78/-3，可读 patch 109 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel」；主要实现面是 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0 (71 lines); hunks: -194,6 +194,77 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run，涉及 `test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run`；`vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2 (6 lines); hunks: -87,7 +87,7 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; -260,7 +260,9 @@ def fused_recurrent_gated_delta_rule_fwd(; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd，涉及 `fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`；`vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1 (4 lines); hunks: -95,7 +95,9 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd，涉及 `fused_recurrent_kda_fwd`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0 (71 lines); hunks: -194,6 +194,77 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_fused_recurrent_kda_more_than_65535_programs, run
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2 (6 lines); hunks: -87,7 +87,7 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; -260,7 +260,9 @@ def fused_recurrent_gated_delta_rule_fwd(; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1 (4 lines); hunks: -95,7 +95,9 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +71/-0
  - runtime: `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +4/-2; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_kda_recurrent.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59126 - [Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input

- 链接: https://github.com/vllm-project/vllm/pull/59126
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/multimodal.py`；关联提交 `097989299222`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-3，可读 patch 35 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/common/multimodal.py`；技术摘要: 覆盖「[Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input」；主要实现面是 `vllm/models/glm5next/common/multimodal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/multimodal.py` modified +4/-3 (7 lines); hunks: -46,6 +46,7; -395,7 +396,7 @@ def __init__(; symbols: __init__, rot_pos_emb, forward，涉及 `__init__, rot_pos_emb, forward`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/multimodal.py` modified +4/-3 (7 lines); hunks: -46,6 +46,7; -395,7 +396,7 @@ def __init__(; symbols: __init__, rot_pos_emb, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +4/-3
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/common/multimodal.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58167 - [ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes

- 链接: https://github.com/vllm-project/vllm/pull/58167
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`；关联提交 `98b29aa99aee`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+705/-240，可读 patch 1241 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`；技术摘要: 覆盖「[ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes」；主要实现面是 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14 (86 lines); hunks: -8,10 +8,6; -20,17 +16,10 @@ def _require_deep_gemm() -> None:; symbols: _require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build，涉及 `_require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build`；`vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6 (82 lines); hunks: -8,10 +8,11; -24,6 +25,7; symbols: _kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool，涉及 `_kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14 (86 lines); hunks: -8,10 +8,6; -20,17 +16,10 @@ def _require_deep_gemm() -> None:; symbols: _require_deep_gemm, test_kpool_indexer_dispatches_through_shared_topk_backend, _build
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6 (82 lines); hunks: -8,10 +8,11; -24,6 +25,7; symbols: _kpool_compress_insert, _kpool_decode_topk_backend, sparse_attn_indexer_kpool
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +72/-14
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +76/-6
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59565 - [Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling

- 链接: https://github.com/vllm-project/vllm/pull/59565
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`；关联提交 `5688a4dd4a1e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+75/-0，可读 patch 93 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0 (51 lines); hunks: -188,3 +188,54 @@ def test_mm_device_do_normalize():; symbols: test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget, test_image_encoder_cache_follows_max_pixels_override，涉及 `test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget`；`vllm/models/glm5next/common/multimodal.py` modified +24/-0 (24 lines); hunks: -2,6 +2,7; -672,6 +673,29 @@ def _get_video_max_pixels(self) -> int:; symbols: _get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v，涉及 `_get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0 (51 lines); hunks: -188,3 +188,54 @@ def test_mm_device_do_normalize():; symbols: test_mm_device_do_normalize, _image_info, test_image_encoder_cache_covers_full_token_budget, test_image_encoder_cache_follows_max_pixels_override
  - `vllm/models/glm5next/common/multimodal.py` modified +24/-0 (24 lines); hunks: -2,6 +2,7; -672,6 +673,29 @@ def _get_video_max_pixels(self) -> int:; symbols: _get_video_max_pixels, get_image_size_with_most_features, _get_video_second_idx_glm46v
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +51/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +24/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57387 - [Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor

- 链接: https://github.com/vllm-project/vllm/pull/57387
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_sequence_parallel.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py` 等 7 个文件；关联提交 `e3cae8d2ac6b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 36 个文件，+365/-2384，可读 patch 3571 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `tests/transformers_utils/processors/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor」；主要实现面是 `tests/transformers_utils/processors/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389 (389 lines); hunks: -1,389 +0,0; symbols: resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive, test_smart_resize_rejects_degenerate_inputs，涉及 `resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive`；`vllm/models/glm5next/common/multimodal.py` modified +68/-52 (120 lines); hunks: -3,13 +3,14; -44,7 +45,6; symbols: load_weights, Glm5NextProcessingInfo, _glm5_hf_processor, get_hf_processor，涉及 `load_weights, Glm5NextProcessingInfo, _glm5_hf_processor`；`vllm/models/glm5next/common/model.py` modified +74/-26 (100 lines); hunks: -6,6 +6,7; -83,7 +84,6; symbols: _is_moe, _is_kda_layer, _is_linear_attn, _validate_supported_config，涉及 `_is_moe, _is_kda_layer, _is_linear_attn`；`tests/models/multimodal/processing/test_glm5next.py` modified +16/-33 (49 lines); hunks: -15,16 +15,15; -48,27 +47,16 @@ def _pixel_path_grid(; symbols: _pixel_path_grid, test_video_placeholders_match_encoder_rows，涉及 `_pixel_path_grid, test_video_placeholders_match_encoder_rows`。
- 代码 diff 细节:
  - `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389 (389 lines); hunks: -1,389 +0,0; symbols: resize, test_smart_resize_reference_values, test_smart_resize_stays_snapped_and_positive, test_smart_resize_rejects_degenerate_inputs
  - `vllm/models/glm5next/common/multimodal.py` modified +68/-52 (120 lines); hunks: -3,13 +3,14; -44,7 +45,6; symbols: load_weights, Glm5NextProcessingInfo, _glm5_hf_processor, get_hf_processor
  - `vllm/models/glm5next/common/model.py` modified +74/-26 (100 lines); hunks: -6,6 +6,7; -83,7 +84,6; symbols: _is_moe, _is_kda_layer, _is_linear_attn, _validate_supported_config
  - `tests/models/multimodal/processing/test_glm5next.py` modified +16/-33 (49 lines); hunks: -15,16 +15,15; -48,27 +47,16 @@ def _pixel_path_grid(; symbols: _pixel_path_grid, test_video_placeholders_match_encoder_rows
  - `vllm/models/qwen4_exp/amd/model.py` modified +10/-37 (47 lines); hunks: -7,6 +7,7; -47,7 +48,6; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/transformers_utils/processors/test_glm5next.py` removed +0/-389; `tests/models/multimodal/processing/test_glm5next.py` modified +16/-33
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +68/-52; `vllm/models/glm5next/common/model.py` modified +74/-26; `vllm/models/qwen4_exp/amd/model.py` modified +10/-37; `vllm/models/qwen4_exp/nvidia/model.py` modified +10/-37; `vllm/models/glm5next/common/attention.py` modified +18/-14; `vllm/models/glm5next/common/mtp.py` modified +4/-4
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_sequence_parallel.py`, `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_ple.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58008 - [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel

- 链接: https://github.com/vllm-project/vllm/pull/58008
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/attention/test_rocm_glm5next_sparse.py`；关联提交 `2df122e65e87`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+109/-12，可读 patch 165 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/v1/attention/test_rocm_glm5next_sparse.py`；技术摘要: 覆盖「[ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel」；主要实现面是 `tests/v1/attention/test_rocm_glm5next_sparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0 (44 lines); hunks: -8,6 +8,7; -26,6 +27,26 @@ def _store_sparse_kv_row_offset_kernel(slot_ptr, output_ptr,...; symbols: _store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history，涉及 `_store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history`。
- 代码 diff 细节:
  - `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0 (44 lines); hunks: -8,6 +8,7; -26,6 +27,26 @@ def _store_sparse_kv_row_offset_kernel(slot_ptr, output_ptr,...; symbols: _store_sparse_kv_row_offset_kernel, _fit_kpool_indices_reference, test_fit_kpool_indices_preserves_tail_and_best_history
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +44/-0
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_rocm_glm5next_sparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57979 - [ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA

- 链接: https://github.com/vllm-project/vllm/pull/57979
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`；关联提交 `3627a6a12489`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+54/-19，可读 patch 159 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `tests/models/glm5next/test_kda_recurrent.py`；技术摘要: 覆盖「[ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA」；主要实现面是 `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `tests/models/glm5next/test_kda_recurrent.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd，涉及 `token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`；`vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda，涉及 `fused_recurrent_kda_fwd, fused_recurrent_kda`；`tests/models/glm5next/test_kda_recurrent.py` modified +3/-4 (7 lines); hunks: -5,8 +5,7; -166,8 +165,8 @@ def test_fused_recurrent_kda_strided_inputs_bit_identical_to...; symbols: test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts，涉及 `test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda
  - `tests/models/glm5next/test_kda_recurrent.py` modified +3/-4 (7 lines); hunks: -5,8 +5,7; -166,8 +165,8 @@ def test_fused_recurrent_kda_strided_inputs_bit_identical_to...; symbols: test_fused_recurrent_kda_strided_inputs_bit_identical_to_contiguous, test_fused_recurrent_kda_rejects_unaddressable_layouts
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` modified +35/-9; `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` modified +16/-6
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +3/-4
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_kda_recurrent.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55389 - [Model] Extend device-side mm normalization to GLM4V/GLM5Next

- 链接: https://github.com/vllm-project/vllm/pull/55389
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/multimodal.py`；关联提交 `0a30bc3f9ac3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+114/-10，可读 patch 279 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Extend device-side mm normalization to GLM4V/GLM5Next」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Model] Extend device-side mm normalization to GLM4V/GLM5Next」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`, `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0 (37 lines); hunks: -13,8 +13,12; -168,3 +172,36 @@ def test_video_shorter_than_one_sampling_interval_is_reject...; symbols: test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize，涉及 `test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize`；`vllm/models/glm5next/common/multimodal.py` modified +4/-1 (5 lines); hunks: -19,6 +19,7; -353,6 +354,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/models/glm5next/common/model.py` modified +2/-0 (2 lines); hunks: -22,6 +22,7; -1103,6 +1104,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0 (37 lines); hunks: -13,8 +13,12; -168,3 +172,36 @@ def test_video_shorter_than_one_sampling_interval_is_reject...; symbols: test_video_shorter_than_one_sampling_interval_is_rejected, test_mm_device_do_normalize
  - `vllm/models/glm5next/common/multimodal.py` modified +4/-1 (5 lines); hunks: -19,6 +19,7; -353,6 +354,7 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/glm5next/common/model.py` modified +2/-0 (2 lines); hunks: -22,6 +22,7; -1103,6 +1104,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +37/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +4/-1; `vllm/models/glm5next/common/model.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation_ppl_test/test_glm.py`, `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55222 - [Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace

- 链接: https://github.com/vllm-project/vllm/pull/55222
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/common/attention.py`；关联提交 `c37f86e5721f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+84/-19，可读 patch 206 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/common/attention.py`；技术摘要: 覆盖「[Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace」；主要实现面是 `vllm/models/glm5next/common/attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/attention.py` modified +3/-1 (4 lines); hunks: -312,7 +312,9 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/attention.py` modified +3/-1 (4 lines); hunks: -312,7 +312,9 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/glm5next/common/attention.py
@@ -312,7 +312,9 @@ def __init__(
-        self.max_total_seq_len = get_max_prefill_buffer_size(vllm_config)
+        self.max_total_seq_len = (
+            get_max_prefill_buffer_size(vllm_config) // self.index_kpool
+        )
```

- 已读文件:
  - runtime: `vllm/models/glm5next/common/attention.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56960 - [Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash

- 链接: https://github.com/vllm-project/vllm/pull/56960
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`；关联提交 `3e2a7e74a556`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+307/-11，可读 patch 478 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`；技术摘要: 覆盖「[Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash」；主要实现面是 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0 (167 lines); hunks: -193,3 +193,170 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run，涉及 `test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run`；`vllm/models/glm5next/common/kda.py` modified +59/-3 (62 lines); hunks: -2,6 +2,8; -14,7 +16,14; symbols: Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype, _a_log_weight_loader，涉及 `Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0 (167 lines); hunks: -193,3 +193,170 @@ def test_fused_recurrent_kda_rejects_unaddressable_layouts():; symbols: test_fused_recurrent_kda_rejects_unaddressable_layouts, test_prefill_checkpoint_resumes_suffix, run
  - `vllm/models/glm5next/common/kda.py` modified +59/-3 (62 lines); hunks: -2,6 +2,8; -14,7 +16,14; symbols: Glm5NextLinearAttention, get_kv_cache_spec, get_state_dtype, _a_log_weight_loader
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` modified +167/-0
  - runtime: `vllm/models/glm5next/common/kda.py` modified +59/-3
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_kda_recurrent.py`, `tests/v1/attention/test_gdn_metadata_builder.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55647 - [Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler

- 链接: https://github.com/vllm-project/vllm/pull/55647
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`；关联提交 `65ed0a2642d2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+229/-0，可读 patch 251 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows, test_video_placeholders_match_encoder_rows_when_presampled，涉及 `processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows`；`vllm/models/glm5next/common/multimodal.py` modified +59/-0 (59 lines); hunks: -4,6 +4,7; -42,6 +43,7; symbols: _get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info，涉及 `_get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: processor, _pixel_path_grid, test_video_placeholders_match_encoder_rows, test_video_placeholders_match_encoder_rows_when_presampled
  - `vllm/models/glm5next/common/multimodal.py` modified +59/-0 (59 lines); hunks: -4,6 +4,7; -42,6 +43,7; symbols: _get_video_max_pixels, _get_video_second_idx_glm46v, _get_vision_info
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` added +170/-0
  - runtime: `vllm/models/glm5next/common/multimodal.py` modified +59/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58454 - [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding

- 链接: https://github.com/vllm-project/vllm/pull/58454
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；关联提交 `2617fe938355`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+208/-49，可读 patch 534 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding」；主要实现面是 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16 (34 lines); hunks: -327,37 +327,38 @@ def _kpool_tail_seed_kernel(; -385,6 +386,7 @@ def kpool_seed_tail_cache(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel，涉及 `_kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel`；`vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15 (32 lines); hunks: -387,14 +387,15 @@ def _kpool_tail_seed_kernel(; -405,18 +406,18 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel，涉及 `_kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel`；`vllm/models/glm5next/common/attention.py` modified +15/-3 (18 lines); hunks: -34,6 +34,7; -160,7 +161,7 @@ class Glm5NextTailCache(DeepseekV32IndexerCache):; symbols: Glm5NextTailCache, __init__, get_kv_cache_spec, get_attn_backend，涉及 `Glm5NextTailCache, __init__, get_kv_cache_spec`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16 (34 lines); hunks: -327,37 +327,38 @@ def _kpool_tail_seed_kernel(; -385,6 +386,7 @@ def kpool_seed_tail_cache(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15 (32 lines); hunks: -387,14 +387,15 @@ def _kpool_tail_seed_kernel(; -405,18 +406,18 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache, _kpool_decode_update_batched_kernel
  - `vllm/models/glm5next/common/attention.py` modified +15/-3 (18 lines); hunks: -34,6 +34,7; -160,7 +161,7 @@ class Glm5NextTailCache(DeepseekV32IndexerCache):; symbols: Glm5NextTailCache, __init__, get_kv_cache_spec, get_attn_backend
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +18/-16; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +17/-15; `vllm/models/glm5next/common/attention.py` modified +15/-3
- 验证与风险: diff 自带测试面 `tests/kernels/test_kpool_decode_update_batched.py`, `tests/v1/attention/test_kpool_tail_slot_mapping.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55270 - [Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with

- 链接: https://github.com/vllm-project/vllm/pull/55270
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `39724758e7b7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`；技术摘要: 覆盖「[Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with」；主要实现面是 `vllm/models/glm5next/nvidia/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0 (1 lines); hunks: -558,6 +558,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool，涉及 `sparse_attn_indexer_kpool`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0 (1 lines); hunks: -558,6 +558,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool
- 关键代码摘录:

```diff
diff -- vllm/models/glm5next/nvidia/sparse_indexer.py
@@ -558,6 +558,7 @@ def sparse_attn_indexer_kpool(
+            indices=decode_metadata.indices,
```

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/nvidia/sparse_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58061 - [Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard

- 链接: https://github.com/vllm-project/vllm/pull/58061
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`；关联提交 `c9b34fdb2d0c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+115/-0，可读 patch 123 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard」；主要实现面是 `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_sequence_parallel.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: _Attention, __init__, _fake_tensor_parallel_world, _forbidden_all_reduce，涉及 `_Attention, __init__, _fake_tensor_parallel_world`；`vllm/models/glm5next/common/model.py` modified +1/-0 (1 lines); hunks: -355,6 +355,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_sequence_parallel.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: _Attention, __init__, _fake_tensor_parallel_world, _forbidden_all_reduce
  - `vllm/models/glm5next/common/model.py` modified +1/-0 (1 lines); hunks: -355,6 +355,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_sequence_parallel.py` added +114/-0
  - runtime: `vllm/models/glm5next/common/model.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_sequence_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57546 - [GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher

- 链接: https://github.com/vllm-project/vllm/pull/57546
- 状态/时间: merged / 2026-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `bf01fc4a313c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+94/-83，可读 patch 277 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/nvidia/sparse_indexer.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`；技术摘要: 覆盖「[GLM-5.3-Flash] Route kpool indexer top-k through the shared SparseIndexerTopk dispatcher」；主要实现面是 `vllm/models/glm5next/nvidia/sparse_indexer.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44 (64 lines); hunks: -10,6 +10,7; -39,21 +40,6; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool, __init__, forward_cuda，涉及 `_use_cooperative_topk, sparse_attn_indexer_kpool, __init__`；`tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26 (54 lines); hunks: -1,41 +1,43; symbols: test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch, test_kpool_indexer_dispatches_through_shared_topk_backend，涉及 `test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44 (64 lines); hunks: -10,6 +10,7; -39,21 +40,6; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool, __init__, forward_cuda
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26 (54 lines); hunks: -1,41 +1,43; symbols: test_cooperative_topk_is_selected_for_supported_batch, _require_deep_gemm, test_cooperative_topk_falls_back_on_unsupported_batch, test_kpool_indexer_dispatches_through_shared_topk_backend
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +20/-44
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` modified +28/-26
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57477 - [Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel

- 链接: https://github.com/vllm-project/vllm/pull/57477
- 状态/时间: merged / 2026-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；关联提交 `db1bfdd4fb0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+23/-5，可读 patch 73 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；技术摘要: 覆盖「[Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel」；主要实现面是 `vllm/models/glm5next/nvidia/ops/kpool_compress.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2 (15 lines); hunks: -383,6 +383,8 @@ def _kpool_tail_seed_kernel(; -393,6 +395,11 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache，涉及 `_kpool_tail_seed_kernel, kpool_seed_tail_cache`。
- 代码 diff 细节:
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2 (15 lines); hunks: -383,6 +383,8 @@ def _kpool_tail_seed_kernel(; -393,6 +395,11 @@ def _kpool_tail_seed_kernel(; symbols: _kpool_tail_seed_kernel, kpool_seed_tail_cache
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +13/-2
- 验证与风险: diff 自带测试面 `tests/kernels/test_kpool_decode_update_batched.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57701 - [GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved

- 链接: https://github.com/vllm-project/vllm/pull/57701
- 状态/时间: merged / 2026-09-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `36fa72d2d0d2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+17/-17，可读 patch 153 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`；技术摘要: 覆盖「[GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved」；主要实现面是 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8 (16 lines); hunks: -100,7 +100,7 @@ def sparse_attn_indexer_kpool(; -136,7 +136,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__，涉及 `sparse_attn_indexer_kpool, __init__`；`vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7 (14 lines); hunks: -117,7 +117,7 @@ def sparse_attn_indexer_kpool(; -153,7 +153,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__，涉及 `sparse_attn_indexer_kpool, __init__`；`vllm/models/glm5next/common/attention.py` modified +2/-2 (4 lines); hunks: -296,7 +296,7 @@ def __init__(; -307,7 +307,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8 (16 lines); hunks: -100,7 +100,7 @@ def sparse_attn_indexer_kpool(; -136,7 +136,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7 (14 lines); hunks: -117,7 +117,7 @@ def sparse_attn_indexer_kpool(; -153,7 +153,7 @@ def sparse_attn_indexer_kpool(; symbols: sparse_attn_indexer_kpool, __init__
  - `vllm/models/glm5next/common/attention.py` modified +2/-2 (4 lines); hunks: -296,7 +296,7 @@ def __init__(; -307,7 +307,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +8/-8; `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +7/-7; `vllm/models/glm5next/common/attention.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #57425 - [Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)

- 链接: https://github.com/vllm-project/vllm/pull/57425
- 状态/时间: merged / 2026-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/sparse_indexer.py`；关联提交 `d12c2768530a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+24/-1，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/amd/sparse_indexer.py`；技术摘要: 覆盖「[Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash)」；主要实现面是 `vllm/models/glm5next/amd/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1 (25 lines); hunks: -665,7 +665,7 @@ def __init__(; -727,3 +727,26 @@ def forward_native(; symbols: __init__, forward_native, forward_hip，涉及 `__init__, forward_native, forward_hip`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1 (25 lines); hunks: -665,7 +665,7 @@ def __init__(; -727,3 +727,26 @@ def forward_native(; symbols: __init__, forward_native, forward_hip
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` modified +24/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/amd/sparse_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #57327 - [Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches

- 链接: https://github.com/vllm-project/vllm/pull/57327
- 状态/时间: merged / 2026-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；关联提交 `2bbdfcfcfea7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+63/-1，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`；技术摘要: 覆盖「[Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches」；主要实现面是 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch，涉及 `test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch`；`vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1 (23 lines); hunks: -38,6 +38,22; -573,7 +589,12 @@ def sparse_attn_indexer_kpool(; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool，涉及 `_use_cooperative_topk, sparse_attn_indexer_kpool`。
- 代码 diff 细节:
  - `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: test_cooperative_topk_is_selected_for_supported_batch, test_cooperative_topk_falls_back_on_unsupported_batch
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1 (23 lines); hunks: -38,6 +38,22; -573,7 +589,12 @@ def sparse_attn_indexer_kpool(; symbols: _use_cooperative_topk, sparse_attn_indexer_kpool
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py` added +41/-0
  - runtime: `vllm/models/glm5next/nvidia/sparse_indexer.py` modified +22/-1
- 验证与风险: diff 自带测试面 `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55358 - [Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA

- 链接: https://github.com/vllm-project/vllm/pull/55358
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/sparse_indexer.py`；关联提交 `4fe9e6f6e564`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+1008/-398，可读 patch 1532 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/sparse_indexer.py`；技术摘要: 覆盖「[Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA」；主要实现面是 `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/models/glm5next/common/sparse_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0 (729 lines); hunks: -0,0 +1,729; symbols: _kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool, __init__，涉及 `_kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool`；`vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391 (467 lines); hunks: -2,30 +2,29; -36,16 +35,9; symbols: _kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens，涉及 `_kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request`；`vllm/models/glm5next/common/sparse_indexer.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, _fill_causal_indices，涉及 `_build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens`；`vllm/models/glm5next/sparse_indexer.py` added +22/-0 (22 lines); hunks: -0,0 +1,22。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0 (729 lines); hunks: -0,0 +1,729; symbols: _kpool_compress_insert, sparse_attn_indexer_kpool, SparseAttnIndexerKpool, __init__
  - `vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391 (467 lines); hunks: -2,30 +2,29; -36,16 +35,9; symbols: _kpool_compress_insert, _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens
  - `vllm/models/glm5next/common/sparse_indexer.py` added +170/-0 (170 lines); hunks: -0,0 +1,170; symbols: _build_decode_scatter_indices, _scatter_decode_tokens_by_request, _decode_topk_seq_lens, _fill_causal_indices
  - `vllm/models/glm5next/sparse_indexer.py` added +22/-0 (22 lines); hunks: -0,0 +1,22
  - `vllm/models/glm5next/common/attention.py` modified +1/-1 (2 lines); hunks: -23,14 +23,14
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/sparse_indexer.py` added +729/-0; `vllm/models/glm5next/nvidia/sparse_indexer.py` renamed +76/-391; `vllm/models/glm5next/common/sparse_indexer.py` added +170/-0; `vllm/models/glm5next/sparse_indexer.py` added +22/-0; `vllm/models/glm5next/common/attention.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_sparse_indexer_decode_seq_lens.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56176 - [ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint

- 链接: https://github.com/vllm-project/vllm/pull/56176
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py` 等 7 个文件；关联提交 `c8d1cf077a78`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+164/-4，可读 patch 208 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`；技术摘要: 覆盖「[ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint」；主要实现面是 `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/common/model.py` renamed +14/-1 (15 lines); hunks: -1036,6 +1036,17 @@ class Glm5NextForConditionalGeneration(; -1259,7 +1270,9 @@ def _try_load_fp8_attn_proj(; symbols: Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj，涉及 `Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj`；`vllm/models/glm5next/__init__.py` modified +2/-2 (4 lines); hunks: -6,8 +6,8；`vllm/models/glm5next/common/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2；`vllm/models/glm5next/common/mtp.py` renamed +1/-1 (2 lines); hunks: -22,6 +22,7; -33,7 +34,6; symbols: Glm5NextMultiTokenPredictorLayer，涉及 `Glm5NextMultiTokenPredictorLayer`。
- 代码 diff 细节:
  - `vllm/models/glm5next/common/model.py` renamed +14/-1 (15 lines); hunks: -1036,6 +1036,17 @@ class Glm5NextForConditionalGeneration(; -1259,7 +1270,9 @@ def _try_load_fp8_attn_proj(; symbols: Glm5NextForConditionalGeneration, _try_load_fp8_attn_proj
  - `vllm/models/glm5next/__init__.py` modified +2/-2 (4 lines); hunks: -6,8 +6,8
  - `vllm/models/glm5next/common/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/glm5next/common/mtp.py` renamed +1/-1 (2 lines); hunks: -22,6 +22,7; -33,7 +34,6; symbols: Glm5NextMultiTokenPredictorLayer
  - `vllm/models/glm5next/common/attention.py` renamed +0/-0 (0 lines)
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/common/model.py` renamed +14/-1; `vllm/models/glm5next/__init__.py` modified +2/-2; `vllm/models/glm5next/common/__init__.py` added +2/-0; `vllm/models/glm5next/common/mtp.py` renamed +1/-1; `vllm/models/glm5next/common/attention.py` renamed +0/-0; `vllm/models/glm5next/common/kda.py` renamed +0/-0
- 验证与风险: diff 自带测试面 `tests/quantization/test_quark.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55239 - [ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA

- 链接: https://github.com/vllm-project/vllm/pull/55239
- 状态/时间: merged / 2026-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/attention/test_rocm_glm5next_sparse.py`；关联提交 `828f4f19b4d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-5，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `tests/v1/attention/test_rocm_glm5next_sparse.py`；技术摘要: 覆盖「[ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA」；主要实现面是 `tests/v1/attention/test_rocm_glm5next_sparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1 (5 lines); hunks: -76,7 +76,9 @@ def test_fit_kpool_indices_rejects_narrow_input():; -88,6 +90,7 @@ def test_rocm_sparse_triton_route(; symbols: test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route，涉及 `test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route`。
- 代码 diff 细节:
  - `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1 (5 lines); hunks: -76,7 +76,9 @@ def test_fit_kpool_indices_rejects_narrow_input():; -88,6 +90,7 @@ def test_rocm_sparse_triton_route(; symbols: test_fit_kpool_indices_rejects_narrow_input, test_rocm_sparse_triton_route
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/v1/attention/test_rocm_glm5next_sparse.py` modified +4/-1
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_rocm_glm5next_sparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55736 - [Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM

- 链接: https://github.com/vllm-project/vllm/pull/55736
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/glm5next/__init__.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`；关联提交 `1768273c13d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+268/-27，可读 patch 399 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`；技术摘要: 覆盖「[Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM」；主要实现面是 `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/glm5next/test_kda_recurrent.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: naive_recurrent_kda, make_inputs, run_kernel, test_fused_recurrent_kda_matches_reference，涉及 `naive_recurrent_kda, make_inputs, run_kernel`；`vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd，涉及 `token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd`；`vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda，涉及 `fused_recurrent_kda_fwd, fused_recurrent_kda`；`tests/models/glm5next/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2。
- 代码 diff 细节:
  - `tests/models/glm5next/test_kda_recurrent.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: naive_recurrent_kda, make_inputs, run_kernel, test_fused_recurrent_kda_matches_reference
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9 (44 lines); hunks: -15,6 +15,23; -52,6 +69,11 @@ def fused_recurrent_gated_delta_rule_fwd_kernel(; symbols: token_stride, fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6 (22 lines); hunks: -24,7 +24,10; -70,7 +73,7 @@ def fused_recurrent_kda_fwd(; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda
  - `tests/models/glm5next/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/glm5next/test_kda_recurrent.py` added +186/-0; `tests/models/glm5next/__init__.py` added +2/-0
  - runtime: `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` modified +35/-9; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` modified +16/-6
- 验证与风险: diff 自带测试面 `tests/models/glm5next/__init__.py`, `tests/models/glm5next/test_kda_recurrent.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55214 - [Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings

- 链接: https://github.com/vllm-project/vllm/pull/55214
- 状态/时间: merged / 2026-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`, `vllm/models/glm5next/nvidia/ops/__init__.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；关联提交 `78300cdabffb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+12/-4，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`；技术摘要: 覆盖「[Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings」；主要实现面是 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -631,9 +631,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched，涉及 `kpool_decode_update_and_maybe_write_cache_batched`；`vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -637,9 +637,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched，涉及 `kpool_decode_update_and_maybe_write_cache_batched`；`vllm/models/glm5next/nvidia/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2；`vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -631,9 +631,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2 (6 lines); hunks: -637,9 +637,11 @@ def kpool_decode_update_and_maybe_write_cache_batched(; symbols: kpool_decode_update_and_maybe_write_cache_batched
  - `vllm/models/glm5next/nvidia/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/ops/kpool_compress.py` modified +4/-2; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` modified +4/-2; `vllm/models/glm5next/nvidia/__init__.py` added +2/-0; `vllm/models/glm5next/nvidia/ops/__init__.py` added +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`, `vllm/models/glm5next/nvidia/ops/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #53906 - [Model] add GLM-5.3-Flash support

- 链接: https://github.com/vllm-project/vllm/pull/53906
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/amd/__init__.py`, `vllm/models/glm5next/amd/ops/__init__.py`, `vllm/models/glm5next/amd/ops/kpool_compress.py` 等 15 个文件；关联提交 `98ed0856f31f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 94 个文件，+17926/-265，可读 patch 19713 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] add GLM-5.3-Flash support」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`；技术摘要: 覆盖「[Model] add GLM-5.3-Flash support」；主要实现面是 `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra，涉及 `fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter`；`vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra，涉及 `fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter`；`vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0 (891 lines); hunks: -0,0 +1,891; symbols: _hadamard128_stage, _hadamard128, _fwht_stage, _fwht_quant_kernel，涉及 `_hadamard128_stage, _hadamard128, _fwht_stage`；`vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0 (890 lines); hunks: -0,0 +1,890; symbols: _cache_k_offset, _hadamard128_stage, _hadamard128, compute_pooled_write_locs，涉及 `_cache_k_offset, _hadamard128_stage, _hadamard128`。
- 代码 diff 细节:
  - `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra
  - `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0 (1362 lines); hunks: -0,0 +1,1362; symbols: fused_recurrent_kda_fwd, fused_recurrent_kda, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_inter, chunk_kda_scaled_dot_kkt_fwd_kernel_intra_sub_intra
  - `vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0 (891 lines); hunks: -0,0 +1,891; symbols: _hadamard128_stage, _hadamard128, _fwht_stage, _fwht_quant_kernel
  - `vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0 (890 lines); hunks: -0,0 +1,890; symbols: _cache_k_offset, _hadamard128_stage, _hadamard128, compute_pooled_write_locs
  - `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` added +656/-0 (656 lines); hunks: -0,0 +1,656; symbols: fused_recurrent_gated_delta_rule_fwd_kernel, fused_recurrent_gated_delta_rule_fwd, fused_recurrent_gated_delta_rule_packed_decode_kernel, fused_recurrent_gated_delta_rule_packed_decode
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py` added +1362/-0; `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py` added +1362/-0; `vllm/models/glm5next/nvidia/ops/kpool_compress.py` added +891/-0; `vllm/models/glm5next/amd/ops/kpool_compress.py` added +890/-0; `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py` added +656/-0; `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py` added +656/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_flashinfer_mla_decode.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/kernels/mamba/test_gdn_prefill_flashinfer.py`, `tests/kernels/test_kpool_decode_update_batched.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53785 - [Attention] Enable dense and masked MHA for GLM-5

- 链接: https://github.com/vllm-project/vllm/pull/53785
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`；关联提交 `de9250ac9e9b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+527/-74，可读 patch 846 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention] Enable dense and masked MHA for GLM-5」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`；技术摘要: 覆盖「[Attention] Enable dense and masked MHA for GLM-5」；主要实现面是 `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0 (59 lines); hunks: -0,0 +1,59。
- 代码 diff 细节:
  - `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0 (59 lines); hunks: -0,0 +1,59
- 关键代码摘录:

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

- 已读文件:
  - runtime: `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` added +59/-0
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_backends.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51015 - [CI] Stabilize GLM-5.2 PCP evaluation

- 链接: https://github.com/vllm-project/vllm/pull/51015
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`；关联提交 `a5149b2feeb7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 7 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Stabilize GLM-5.2 PCP evaluation」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`；技术摘要: 覆盖「[CI] Stabilize GLM-5.2 PCP evaluation」；主要实现面是 `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0 (1 lines); hunks: -13,5 +13,6 @@ server_args: >-。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0 (1 lines); hunks: -13,5 +13,6 @@ server_args: >-
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml
@@ -13,5 +13,6 @@ server_args: >-
+  PYTORCH_CUDA_ALLOC_CONF: "expandable_segments:True"
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #49791 - [Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2

- 链接: https://github.com/vllm-project/vllm/pull/49791
- 状态/时间: merged / 2026-08-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；关联提交 `c8109375733e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+619/-51，可读 patch 965 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2」；模型线: GLM-5/5.1；类别: 模型实现调整；主要 diff: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`；技术摘要: 覆盖「[Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2」；主要实现面是 `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: GLM52ProjectionSpec, build_plan, _is_sm103, _is_supported_row_major，涉及 `GLM52ProjectionSpec, build_plan, _is_sm103`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: GLM52ProjectionSpec, build_plan, _is_sm103, _is_supported_row_major
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py` added +199/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
