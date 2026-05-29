# sglang DeepSeek V4 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| - | no local-only commit |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 0
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| - | - | - | no local-only commit found | - |

## Per-Commit Audit Cards

### Local commit search conclusion

- Commits reachable from `sgl-project/sglang` GitHub refs were removed; no local-only commit remains in the baseline history.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 17
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-04-28 | `14671daae` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | patch for deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` 等 11 个文件 |
| 2026-04-28 | `24f89924a` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | Ignore error exceptions and allow the service to start. | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` 等 7 个文件 |
| 2026-04-28 | `bc0809390` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix jit for compress_forward | `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 4 个文件 |
| 2026-04-28 | `dbd0d5c1d` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix jit for compress_fused_norm_rope_inplace | `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor.py` |
| 2026-04-29 | `66bb0d501` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh` 等 16 个文件 |
| 2026-04-29 | `6f3103454` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题 | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h` |
| 2026-04-29 | `cf0af79d2` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix topk_transform_512 jit | `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/srt/layers/attention/dsv4/metadata.py` 等 6 个文件 |
| 2026-04-30 | `51f4fe3e1` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix mhc | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-04-30 | `53c8956fd` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors | `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 4 个文件 |
| 2026-04-30 | `83e281dc0` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | first version for fp8 block | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-06 | `0c411213f` | `v0.5.11_dev..v0.5.12_dev` | 性能/后端优化 | 删除deepgemm meta | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-05-07 | `070988441` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | support fp8 channel-wise load weight | `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-09 | `0dbd5074d` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | 接入lightop的Marlin MOE W8A8算子 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-09 | `452e413c1` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-05-09 | `7ecb521af` | `v0.5.11_dev..v0.5.12_dev` | 调度/缓存/PD | 1. add aiter moe; 2. split attn for prefill/decode | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 |
| 2026-05-20 | `139c5c455` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | backup dcu deepseek v4 debug state | `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py` |
| 2026-05-21 | `b306ccfe4` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | 适配deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh` 等 19 个文件 |

### Per-Commit Audit Cards

#### Commit `14671daae` - patch for deepseekv4

- Full hash: `14671daae3602521808d74d3a8879cc525fbb2f3`
- Date/author: 2026-04-28 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/mhc.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 10 个文件
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `24f89924a` - Ignore error exceptions and allow the service to start.

- Full hash: `24f89924ad7b1c8bf3638e369185562510848b14`
- Date/author: 2026-04-28 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `bc0809390` - fix jit for compress_forward

- Full hash: `bc0809390ff44101388966a545729bcfb47e4a33`
- Date/author: 2026-04-28 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `dbd0d5c1d` - fix jit for compress_fused_norm_rope_inplace

- Full hash: `dbd0d5c1d5487d095e0a9dcc2f85fccacb3f2fa4`
- Date/author: 2026-04-28 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/srt/layers/attention/dsv4/compressor.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `66bb0d501` - [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues

- Full hash: `66bb0d501453dbc6d3cdab54e50e120a1e49462c`
- Date/author: 2026-04-29 / YuanYuan
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/rmsnorm.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 16 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/rmsnorm.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 16 个文件
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `6f3103454` - 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题

- Full hash: `6f31034548aa5e75156ca0d11c790b52cfdb2e81`
- Date/author: 2026-04-29 / lipenghui
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/jit_kernel/include/sgl_kernel/utils.h`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `cf0af79d2` - fix topk_transform_512 jit

- Full hash: `cf0af79d2b9e5d7dde3034ae033148484137d255`
- Date/author: 2026-04-29 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `51f4fe3e1` - fix mhc

- Full hash: `51f4fe3e15958a80d5b010553e39773306ae770b`
- Date/author: 2026-04-30 / flyingdown
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/mhc.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `53c8956fd` - [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors

- Full hash: `53c8956fd09e16724610ba75e79396b68c1ea1e9`
- Date/author: 2026-04-30 / yuanyuan
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `83e281dc0` - first version for fp8 block

- Full hash: `83e281dc0fba863706e4c153364b92bf890b7a4c`
- Date/author: 2026-04-30 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`
  - other: `python/sglang/srt/managers/tp_worker.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `0c411213f` - 删除deepgemm meta

- Full hash: `0c411213f0a7d161d8b123c0cbae4937fb47ac2c`
- Date/author: 2026-05-06 / flyingdown
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/model_runner.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

#### Commit `070988441` - support fp8 channel-wise load weight

- Full hash: `070988441ce2e10efb6b1f92b6eabf26c01985bd`
- Date/author: 2026-05-07 / flyingdown
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `0dbd5074d` - 接入lightop的Marlin MOE W8A8算子

- Full hash: `0dbd5074d1c37570390f3edd2af0460d6160867e`
- Date/author: 2026-05-09 / lj1999
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `452e413c1` - [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still

- Full hash: `452e413c154ce1524a19ca3edf1c2a11a18fa059`
- Date/author: 2026-05-09 / yuanyuan
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `7ecb521af` - 1. add aiter moe; 2. split attn for prefill/decode

- Full hash: `7ecb521af66be463683f38b2ff26f9db46b477f9`
- Date/author: 2026-05-09 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
  - other: `python/sglang/srt/environ.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

#### Commit `139c5c455` - backup dcu deepseek v4 debug state

- Full hash: `139c5c455ad3b6d448b812be3ce633af6fa64d2f`
- Date/author: 2026-05-20 / lizhigong
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`; `python/sglang/srt/layers/mhc.py`
  - other: `python/sglang/srt/environ.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `b306ccfe4` - 适配deepseekv4

- Full hash: `b306ccfe4ef332f3c1b5c5cec620f6ba64998ebd`
- Date/author: 2026-05-21 / lizhigong
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 19 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 18 个文件
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
