# SGLang hg-full-base..main 分支更新本地独有提交索引

## 范围与口径

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- 官方仓库: `https://github.com/sgl-project/sglang.git`
- 官方 refs: 已 fetch 到本地 `refs/remotes/github-official/*`
- 筛选方法: 每个分支更新段内，commit hash 不可从官方 GitHub refs 到达，即记录为本地 fork 独有提交。
- 说明: 合并提交也保留；合并提交没有直接文件 diff 时，`主要涉及` 标记为 `无直接文件变更/merge`。
- 生成日期: 2026-11-05

## 数量汇总

| 分支更新段 | 范围内提交数 | 本地独有提交数 | 其中 merge |
| --- | ---: | ---: | ---: |
| `hg-full-base..main` | 955 | 939 | 243 |
| 合计 | 955 | 939 | 243 |

## 分桶分布

| 桶 | 提交数 |
| --- | ---: |
| `deepseek-v3-r1` | 43 |
| `deepseek-v31` | 30 |
| `deepseek-v32` | 48 |
| `deepseek-v4` | 85 |
| `glm45` | 7 |
| `glm46-glm47` | 8 |
| `glm5-glm51` | 9 |
| `gpt-oss` | 2 |
| `hunyuan3-preview` | 25 |
| `kimi` | 14 |
| `mimo-v2-flash` | 25 |
| `minimax` | 33 |
| `mixtral-quark-int4fp8-moe` | 12 |
| `moss-vl` | 1 |
| `nemotron-super` | 2 |
| `qwen-vlm-omni-asr` | 7 |
| `qwen3-coder` | 25 |
| `qwen3-core` | 26 |
| `qwen3-next` | 3 |
| `qwen35` | 21 |
| `qwen36` | 5 |
| `shared` | 477 |
| `unclassified` | 246 |

- 同一提交可同时进入多个模型桶，所以各桶之和大于本地独有提交总数。

## 重复检查

- 本次未计算 `git patch-id`（克隆不含文件内容）；仅按「标题相同且文件集相同」检查疑似重复。
- 疑似重复: `6a705f146`, `6809e2083`, `20f106c6b`, `ce2521017`, `3f920d4e0`, `fe4e1fea3`，标题 `docs: sync LMSYS SGLang blog cards`。索引中均保留。
- 疑似重复: `62a23f050`, `d32fa4686`, `56b6eebcc`，标题 `[feat]: HY3 support PP`。索引中均保留。
- 疑似重复: `5d83cfe85`, `0536e102c`，标题 `[SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs`。索引中均保留。
- 疑似重复: `c7a4903ad`, `ca7c7c54f`, `db4759e78`, `20eb46a70`, `7d807cb22`, `8aa4b6eb5`, `21dfaaa4c`，标题 `Update dcu-manual-model-test.yml`。索引中均保留。
- 疑似重复: `93cf8edc4`, `e6d4b3378`，标题 `[Addition] deliver one validation doc`。索引中均保留。
- 疑似重复: `3b0e1b709`, `92c15b3d8`，标题 `[bug fix] hunyuanv3精度异常解决`。索引中均保留。
- 疑似重复: `e5a2dd041`, `d28069157`，标题 `[bugfix]适配新的causal_conv1d接口`。索引中均保留。
- 疑似重复: `64d1765b4`, `6c1786bc4`, `ca9b264a2`, `7482123c3`，标题 `fix(hcu): prefer hcusmi for platform detection`。索引中均保留。
- 疑似重复: `8f848be4e`, `997e64560`，标题 `ci: use configured HCU release image`。索引中均保留。
- 疑似重复: `9a4f82911`, `0305c5a3b`，标题 `fix lint`。索引中均保留。
- 疑似重复: `ff7f44b8e`, `286612da4`，标题 `Update quality gate workflow to use version v2.0.0`。索引中均保留。
- 疑似重复: `e6c410259`, `de696eab9`，标题 `Update quality gate workflow to version 2.0.1`。索引中均保留。

## 提交索引

### `hg-full-base..main`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-25 | `a28aa5f97` | lizhigong | fix some errors when init server | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8.py` 等 8 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-04-27 | `547981c68` | wangaq | fix for load model |  | unclassified |
| 2026-04-28 | `321fa6969` | wangaq | patch for deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` 等 11 个文件 | deepseek-v4 |
| 2026-04-28 | `99690f7d1` | wangaq | Ignore error exceptions and allow the service to start. | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` 等 7 个文件 | deepseek-v3-r1, deepseek-v32, deepseek-v4 |
| 2026-04-28 | `22d8caf08` | Zhangzbb | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 6 个文件 | shared |
| 2026-04-28 | `b4cb76a97` | wangaq | fix jit for compress_forward | `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 4 个文件 | deepseek-v4 |
| 2026-04-28 | `f824dca29` | wangaq | fix jit for compress_fused_norm_rope_inplace | `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor.py` | deepseek-v4 |
| 2026-04-29 | `6236ca8f5` | Zhangzbb | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` | shared |
| 2026-04-29 | `2e1710ded` | wangaq | fix jit for moe_fused_gate | `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` | shared |
| 2026-04-29 | `9c1c29919` | wangaq | fix mhc with tile 0.1.9 | `python/sglang/srt/layers/mhc.py` | shared |
| 2026-04-29 | `87c5bd880` | lipenghui | 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题 | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h` | deepseek-v4 |
| 2026-04-29 | `3230bc2bd` | YuanYuan | [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh` 等 16 个文件 | deepseek-v4 |
| 2026-04-29 | `5b6499d05` | wangaq | fix topk_transform_512 jit | `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/srt/layers/attention/dsv4/metadata.py` 等 6 个文件 | deepseek-v4 |
| 2026-04-30 | `8cfd8b5ea` | yuanyuan | [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors | `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 4 个文件 | deepseek-v4 |
| 2026-04-30 | `d0534f2f9` | wangaq | first version for fp8 block | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-04-30 | `1087fc571` | flyingdown | fix mhc | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-06 | `cc008ad80` | flyingdown | 删除deepgemm meta | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/model_runner.py` | deepseek-v3-r1, deepseek-v32, deepseek-v4 |
| 2026-05-07 | `f05917756` | flyingdown | support fp8 channel-wise load weight | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-08 | `47432fb4a` | wangaq | fix bug | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-05-09 | `fe0cc03a8` | yuanyuan | [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/moe/ep_moe/layer.py` | deepseek-v4 |
| 2026-05-09 | `ce5d45fc5` | wangaq | 1. add aiter moe; 2. split attn for prefill/decode | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 | deepseek-v4 |
| 2026-05-09 | `ddc13994f` | lj1999 | 接入lightop的Marlin MOE W8A8算子 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-14 | `5d756f982` | YuanYuan | fix the mtp issues of metadata loc size | `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` | shared |
| 2026-05-18 | `c5dd815b3` | lizhigong | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` 等 141 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, minimax, mixtral-quark-int4fp8-moe, qwen-vlm-omni-asr, qwen3-coder, qwen3-core, qwen35 |
| 2026-05-18 | `e4c9004c6` | lizhigong | fix init error when use qwen 3.5 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-05-19 | `1e8c3e843` | lj1999 | 添加aiter moe算子权重重排逻辑+优化linear_bf16_fp32算子+优化act_quant算子+融合silu_mul_fp8_quant算子 | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 5 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-05-20 | `2702c30f5` | lizhigong | backup dcu deepseek v4 debug state | `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py` | deepseek-v4 |
| 2026-05-20 | `e92c263e5` | lj1999 | add Pipeline Parallelism (PP) and PD support for DeepSeek-V4 | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-20 | `e684ee941` | wangaq | fix deepseek v4 pro blockwise && channelwise | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` 等 9 个文件 | deepseek-v4 |
| 2026-05-21 | `e170935b6` | lizhigong | 适配deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh` 等 19 个文件 | deepseek-v3-r1, deepseek-v32, deepseek-v4 |
| 2026-05-21 | `aee2b606f` | zhenggf | feat(diffusion): add ROCm SLA attention backend | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` 等 6 个文件 | shared |
| 2026-05-21 | `e797eb690` | wangaq | fix bug |  | unclassified |
| 2026-05-22 | `5cff5f5e7` | chenyue3 | [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0 | `python/sglang/srt/layers/quantization/unquant.py` | shared |
| 2026-05-22 | `1f86903ae` | wangaq | split prefill/decode for attention | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/__init__.py` 等 8 个文件 | deepseek-v4 |
| 2026-05-22 | `fc6da7e47` | lj1999 | 接入aiter的tilelang mhc_pre/mhc_post算子 | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-25 | `2f1c501c2` | wangaq | fix jit kernel for store kvcache | `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh` | deepseek-v4 |
| 2026-05-25 | `3334b3c5e` | YuanYuan | [feature support] enable cp+ep by deegemm, ensure deepgemm ver>=da4b9c1 | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-05-26 | `d1d74545b` | lj1999 | 优化quant_k_cache算子和rmsnorm算子 | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py` 等 5 个文件 | deepseek-v4 |
| 2026-05-26 | `f8dc6e03e` | liucong8560 | 支持Qwen3.5-397b-channel-fp8 EP8并行方案 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-05-26 | `5e3749568` | liucong8560 | 接入lightop layer_norm_fwd_1pass_opt算子实现 | `python/sglang/srt/layers/attention/fla/layernorm_gated.py` | shared |
| 2026-05-27 | `74ab58325` | tly123 | ci: add DCU PR CI validation flow | `.github/workflows/pr-test-dcu.yml`, `docs/dcu-pr-ci-visual-guide.html`, `python/sglang/test/ci/ci_register.py` 等 12 个文件 | shared |
| 2026-05-27 | `61c6528b4` | lj1999 | 接入fast_hadamard_transform算子 | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-05-28 | `02b73b2d3` | tly123 | ci: fix DCU local run suite execution | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`, `test/run_suite.py` | shared |
| 2026-05-28 | `93dac7daf` | yangyn1 | moe-runner-backend支持lightop_moe_w8a8 | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py` 等 5 个文件 | shared |
| 2026-05-29 | `90205d601` | tly123 | test: sync validated DCU registered cases | `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` 等 202 个文件 | unclassified |
| 2026-05-29 | `6a705f146` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-05-29 | `35522f491` | yangyn1 | 添加lightop提示信息 | `python/sglang/srt/server_args.py` | shared |
| 2026-05-29 | `4b76f0ef5` | tly123 | ci: stabilize DCU PR runner workspace cleanup | `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` | shared |
| 2026-05-29 | `91863feef` | leon.wang | [feature] support deepseek-v4-flash-int8 | `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-05-30 | `f7022899e` | liucong8560 | 增加decode_metadata sgl-kernel实现 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/attention/decode_metadata.cu` 等 9 个文件 | shared |
| 2026-06-01 | `f981141be` | yangyn1 | moe_runner适配aiter_w8a8_int8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py` | shared |
| 2026-06-01 | `f7789462f` | tly123 | ci: add DCU full enabled workflow | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-01 | `6ba549a61` | tly123 | ci: isolate DCU runner git config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `e36208020` | tly123 | ci: use static DCU git config path | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `53a10162c` | tly123 | ci: clear DCU checkout proxy config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `8f4d1af5c` | tly123 | ci: use explicit DCU checkout | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `91b09c446` | tly123 | test: allow DCU CI to override test models | `python/sglang/test/test_utils.py` | shared |
| 2026-06-01 | `faff8208c` | tly123 | fix: restore qwen2 rope config import | `python/sglang/srt/models/qwen2.py` | shared |
| 2026-06-01 | `f0cfe1740` | tly123 | ci: support DCU visible device selection | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` 等 4 个文件 | shared |
| 2026-06-01 | `584a9d245` | tianly-ci | ci: allow DCU PR workflow on dcu-ci-pr | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `c8eff9d69` | lizhigong | 优化quant_k_cache算子和rmsnorm算子 | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-01 | `0b8715f67` | lj1999 | 融合QNORM_ROPE_KV_ROPE_QUANT | `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-01 | `69dd9eb0e` | tianlinyang77 | test: align enabled DCU cases | `python/sglang/test/dcu_utils.py`, `test/registered/metrics/test_metrics.py` | shared |
| 2026-06-01 | `ada40fccf` | tianlinyang77 | ci: allow full DCU validation from run-ci label | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-01 | `ad7aece93` | tianlinyang77 | ci: expand DCU PR validation matrix | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `987a2c813` | tianly | ci: default DCU CI server backend to fa3 | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-01 | `e92324720` | DCU CI Bot | ci: route DCU validation to nmz4 runner | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `695956fc1` | DCU CI Bot | ci: apply DCU runtime defaults in CI | `python/sglang/lang/api.py` | shared |
| 2026-06-01 | `40fbcab06` | tianly-ci | ci: run DCU required include-file set on PR | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-01 | `cf08ece20` | DCU CI Bot | ci: avoid forcing DCU page size in tests | `python/sglang/lang/api.py`, `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-01 | `6809e2083` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-06-01 | `32d9bb7ae` | liucong8560 | 修复fused_sigmoid_gating_delta_rule_update冲突问题 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` | shared |
| 2026-06-02 | `fb2b0297e` | tianly-ci | ci: use dcu-ci-pr runner label directly | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-02 | `262c0c820` | lizhigong | Resolve the issue of errors during the startup service phase | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 5 个文件 | deepseek-v4 |
| 2026-06-02 | `a04b5628e` | liucong8560 | 支持triton版本flash_attn算子，方便排查PA精度问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` | shared |
| 2026-06-02 | `1e0cf19d0` | whlwhlwhl | [feature] add dspk fuse_op | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` 等 6 个文件 | deepseek-v4 |
| 2026-06-03 | `e6ed9a5b0` | lj1999 | 修改mhc_post算子传参 | `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-03 | `7b86e4afd` | liucong | 修改aiter prefill阶段的fla算子传参 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py` | shared |
| 2026-06-03 | `f13630b2e` | yangyn1 | fix 修复chunk_delta_h调用报错问题 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | shared |
| 2026-06-03 | `d6baa0809` | zhangyh15 | Add DCU wheel release workflow with CIUpload repair and devpi upload | `.github/workflows/release-pypi-nightky-dcu.yml` | shared |
| 2026-06-03 | `fba9d715f` | liucong8560 | 修复decode_metadata算子，import不起来的问题 | `sgl-kernel/python/sgl_kernel/__init__.py` | shared |
| 2026-06-03 | `45b95c0ad` | liucong8560 | Merge branch 'v0.5.12_dev_liucong' of https://developer.sourcefind.cn/codes/OpenDAS/sglang into v0.5.12_dev_liucong | 无直接文件变更/merge | unclassified |
| 2026-06-03 | `a1fd5486a` | RyeYuan | [BugFix] fix some bugs when using fused kernels | `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py` 等 4 个文件 | deepseek-v4 |
| 2026-06-03 | `fb3900b24` | lizhigong | Merge pull request #5 from HYGON-AI/zyh-test-ci | 无直接文件变更/merge | unclassified |
| 2026-06-03 | `9abf0b3f4` | RyeYuan | [BugFix] fix the running issues of tilelang in compressor_v2 mode, SGLANG_OPT_USE_COMPRESSOR_V2=false could be removed | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/dsv4/compress.py` | deepseek-v4 |
| 2026-06-03 | `40802b348` | liucong8560 | Merge remote-tracking branch 'v0.5.12_dev_liucong/v0.5.12_dev' into v0.5.12_dev | 无直接文件变更/merge | unclassified |
| 2026-06-03 | `4f14e4618` | lizhigong | Merge pull request #6 from HYGON-AI/v0.5.12_dev_liucong | 无直接文件变更/merge | unclassified |
| 2026-06-03 | `43375feaf` | tianlinyang77 | ci: stabilize DCU PR required tests | `.github/workflows/pr-test-dcu.yml`, `python/sglang/__init__.py`, `python/sglang/lang/api.py` 等 5 个文件 | shared |
| 2026-06-03 | `494b4246f` | tianlinyang77 | ci: allow DCU dispatch control jobs on runner | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-03 | `c190162be` | tianlinyang77 | ci: clean DCU dispatch validation workspace | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-03 | `48d234263` | tianlinyang77 | ci: pin DCU CI compatibility packages | `scripts/ci/dcu/dcu_ci_install_dependency.sh` | shared |
| 2026-06-03 | `9022f2c34` | shiqiang | [FIX] Initialize swa_v_head_dim in TritonAttnBackend and cleanup unused import | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` | shared |
| 2026-06-03 | `4e3fd3a35` | wujl5 | HY3修改 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-06-03 | `6ae083114` | wujl5 | add topk fused op | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-03 | `237b7de51` | LuoYao | [feat]: 添加rms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-03 | `5245654dc` | liuchy5 | Fix: DCU bypass Triton get_last_loc and use native dcu_get_last_loc | `python/sglang/srt/mem_cache/common.py` | shared |
| 2026-06-04 | `947a5554f` | lizhigong | Merge pull request #7 from HYGON-AI/v0.5.12_dev_swa_fix | 无直接文件变更/merge | unclassified |
| 2026-06-04 | `27ea55979` | zhangyh15 | 更新tilelang版本到0.1.9 | `python/pyproject.toml` | shared |
| 2026-06-04 | `e7b91b4cc` | lizhigong | Merge pull request #8 from HYGON-AI/zyh-test-ci | 无直接文件变更/merge | unclassified |
| 2026-06-04 | `113d67786` | yangyn | Update chunk_delta_h.py | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | shared |
| 2026-06-04 | `6a5a6f5e9` | lizhigong | Merge branch 'v0.5.12_dev' into v0.5.12_dev_moe_runer | 无直接文件变更/merge | unclassified |
| 2026-06-04 | `33468b69a` | lizhigong | Merge pull request #9 from HYGON-AI/v0.5.12_dev_moe_runer | 无直接文件变更/merge | unclassified |
| 2026-06-04 | `29b689574` | dddddddxl | ci: update DCU test registration state | `.github/workflows/pr-test-dcu.yml`, `test/registered/metrics/test_metrics.py` | shared |
| 2026-06-04 | `46efb284a` | dddddddxl | ci: update dcu-full-enanled.yml | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-04 | `099123603` | dddddddxl | ci: run DCU full workflow on self-hosted runner | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-04 | `598f2d61f` | tianlinyang77 | ci: use local DCU model env defaults | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-04 | `22e57a7b3` | dddddddxl | ci: verify DCU full registration in container | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-04 | `f57339642` | tly123 | ci: keep DCU test defaults official-friendly | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` 等 17 个文件 | shared |
| 2026-06-04 | `cad9d0c35` | Lv Jiajia | docs: add Apache license notices for DCU SGLang | `README.md`, `README_DCU.md`, `THIRD_PARTY_NOTICES.md` | shared |
| 2026-06-04 | `42ffb433b` | tly123 | ci: avoid ROCR device remap in DCU runner | `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` | shared |
| 2026-06-04 | `cf7567773` | tly123 | ci: map DCU Qwen2.5 0.5B model path | `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-04 | `2f7f34322` | reverie-hub | fix: sanitize AMD logs on DCU runtime paths | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/layers/attention/aiter_backend.py` 等 20 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm45, glm46-glm47, mixtral-quark-int4fp8-moe |
| 2026-06-05 | `f08ff0bab` | dddddddxl | ci: disable failed DCU full-enabled tests | `.github/workflows/pr-test-dcu.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py` 等 49 个文件 | qwen3-coder, qwen3-core |
| 2026-06-05 | `7694afa39` | tly123 | ci: refine DCU suite classification | `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/language/test_srt_backend.py` | shared |
| 2026-06-05 | `cc279bcf6` | tly123 | ci: rename DCU BW1000 tests to BW1100 | `.github/workflows/pr-test-dcu.yml`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` 等 165 个文件 | unclassified |
| 2026-06-05 | `b95046afa` | tly123 | ci: guard DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-05 | `d8f350eed` | tly123 | ci: avoid dispatch checkout permission issues | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-05 | `823bd922f` | tly123 | ci: isolate DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-05 | `d6a2b719a` | tly123 | ci: map DCU priority metrics model path | `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-05 | `51abece95` | dddddddxl | ci: remove DCU CSV coverage analyzer | `scripts/ci/dcu/analyze_dcu_csv_coverage.py` | shared |
| 2026-06-08 | `1e1d77a76` | yangyn1 | 解决aiter显存溢出问题 | `.gitignore`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` | shared |
| 2026-06-08 | `f71c2ef80` | RyeYuan | [BugFix] fix the buffer shape unalgined issues of draft model warmup and decode forward in PD phase | `python/sglang/srt/managers/overlap_utils.py` | shared |
| 2026-06-08 | `d834f0200` | lj1999 | 适配fp8—einsum算子 | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-09 | `ab857fb79` | lizhigong | Merge pull request #10 from HYGON-AI/docs/license-apache-dcu | 无直接文件变更/merge | unclassified |
| 2026-06-09 | `623d6eca1` | RyeYuan | [BugFix] fix the acc bug due to Q NaN generations, and fix the other tiny typos | `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-06-09 | `0f1ea3303` | dddddddxl | ci: add DCU wheel sync path for PR tests | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-whl-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` 等 4 个文件 | shared |
| 2026-06-09 | `6d25108ac` | yangyn1 | aiter适配moe_w8a8_fp8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` | shared |
| 2026-06-09 | `e03bc0cf8` | tianlinyang77 | fix: skip PYTHONPATH assertion in wheel mode for stage-b test | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py` | shared |
| 2026-06-09 | `a6c6527cd` | tianlinyang77 | fix: pass DCU_CI_USE_INSTALLED_WHEELS into docker container for wheel mode skip | `scripts/ci/dcu/dcu_ci_exec.sh` | shared |
| 2026-06-09 | `c4d3532db` | liuchy5 | fix:dcu bypass triton normal_decode_set_metadata use normal_decode_set_metadata_lightop | `python/sglang/srt/layers/attention/flashattention_backend.py` | shared |
| 2026-06-10 | `e6e05f322` | tianlinyang77 | ci: test auto-trigger push flow (no-op comment) | `test/registered/dcu/interface/test_dcu_smoke.py` | shared |
| 2026-06-10 | `adaf77ef9` | tianlinyang77 | ci: always prefer self-hosted runner for pre-jobs to avoid billing block | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-10 | `cbf9c1ce4` | tianlinyang77 | ci: use self-hosted runner for pr-gate to avoid billing block | `.github/workflows/pr-gate.yml` | shared |
| 2026-06-10 | `6b0e35b3f` | tianlinyang77 | ci: prefer python3.9 for verify_dcu_registration on self-hosted runner | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-10 | `c066cf42f` | tianlinyang77 | ci: add pull-requests:read permission to release-whl-dcu for PR file listing | `.github/workflows/release-whl-dcu.yml` | shared |
| 2026-06-10 | `9f7cb7060` | RyeYuan | [BugFix] fix the bug of cp/ep | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 5 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-06-10 | `1be11e42e` | RyeYuan | [BugFix] fix the bug of dp and jit kernel | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/layers/communicator.py` 等 4 个文件 | deepseek-v4 |
| 2026-06-10 | `99cb3c5c8` | reverie-hub | fix: restore AMD runtime log text | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/layers/attention/aiter_backend.py` 等 19 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm45, glm46-glm47, mixtral-quark-int4fp8-moe |
| 2026-06-10 | `af4e7a5d4` | lj1999 | 增加fp8_einsum算子环境变量控制 | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-11 | `11c0badb2` | dddddddxl | Merge dcu-ci-pr into v0.5.12_dev for DCU CI | 无直接文件变更/merge | unclassified |
| 2026-06-11 | `92a8ba840` | RyeYuan | [FEAT] cherry-pick and refactor from a0bcfe90, support moe triton backend and fix the acc issue in moe aiter backend | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` | shared |
| 2026-06-11 | `4d9dc6618` | DCU CI Bot | ci: reduce DCU CI mainline intrusion | `.github/workflows/pr-gate.yml`, `.github/workflows/release-whl-dcu.yml`, `python/sglang/__init__.py` 等 151 个文件 | unclassified |
| 2026-06-11 | `52b5b9623` | DCU CI Bot | ci: isolate DCU wheel wait checkout workspace | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-11 | `bea273016` | RyeYuan | Merge branch 'v0.5.12_dev' into v0.5.12_dev_dpsk_v4 | 无直接文件变更/merge | unclassified |
| 2026-06-11 | `890a55077` | lizhigong | Merge pull request #12 from HYGON-AI/v0.5.12_dev_dpsk_v4 | 无直接文件变更/merge | unclassified |
| 2026-06-11 | `033bc6b92` | yangyn1 | 重构aiter的重排逻辑 添加aiter log打印信息 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 5 个文件 | shared |
| 2026-06-11 | `da04ee008` | DCU CI Bot | ci: fix DCU PR required regressions | `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/models/qwen2.py`, `test/registered/core/test_hidden_states.py` 等 6 个文件 | shared |
| 2026-06-11 | `eda451b27` | DCU CI Bot | ci: pin DCU Engine tests to fa3 backend | `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/sampling/bw1100/test_original_logprobs_dcu.py` | shared |
| 2026-06-11 | `637377248` | DCU CI Bot | ci: install DCU wheel artifacts without dependencies | `scripts/ci/dcu/dcu_ci_install_dependency.sh` | shared |
| 2026-06-11 | `b3a4160a3` | maxiao1 | 修复dpskv4-flash在pd分离下mtp精度问题 | `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` | shared |
| 2026-06-11 | `c0206c7c4` | caihl | Release original layer.weight after deepgemm_weights conversion to avoid OOM | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-06-12 | `5a231f0b5` | LvJIA-RG | test: add DCU disabled smoke candidates | `test/registered/dcu/4-gpu-models/test_qwen3_next_80b_server_dcu.py`, `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/core/test_score_api_dcu.py` 等 7 个文件 | qwen3-next |
| 2026-06-12 | `04faad946` | lizhigong | Merge pull request #13 from HYGON-AI/0611-dcu-ci-merge | 无直接文件变更/merge | unclassified |
| 2026-06-12 | `82a5c469c` | caihl | fix issues of w13_weight using | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-06-13 | `2ccdb54c5` | chenyuege | [feat]增加sglang性能分析skill，注意当前还处于试用阶段 | `.claude/skills/sglang-profile-analyse/SKILL.md` | unclassified |
| 2026-06-13 | `12a30ab42` | dddddddxl | ci: stabilize DCU PR test workflow | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml` 等 8 个文件 | shared |
| 2026-06-13 | `f9f0cb23d` | tianly | ci: auto-run DCU gate for DCU-owned changes | `.github/workflows/pr-test-dcu.yml`, `python/sglang/test/dcu_utils.py` | shared |
| 2026-06-14 | `083e22033` | tianly | ci: auto-run DCU gate for impact paths | `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/server_args.py` | shared |
| 2026-06-14 | `84cc64ecd` | Lvjiajia | Create quality-gate.yml | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-14 | `06331bc25` | Lvjiajia | Refactor quality gate workflow for changed files check | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-14 | `ae315e505` | Lvjiajia | Merge pull request #22 from HYGON-AI/add-quality-gate | 无直接文件变更/merge | unclassified |
| 2026-06-15 | `0cdbfd7b0` | zhangyh15 | Add lint-dcu.yml for DCU self-hosted runner, restore original lint.yml | `.github/workflows/lint-dcu.yml`, `.github/workflows/release-pypi-nightky-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-15 | `9da8b1176` | shiqiang | [Feat] support unified fa without layout trans | `python/sglang/srt/layers/attention/flashattention_backend.py` | shared |
| 2026-06-15 | `bc649e255` | shiqiang | [BUG FIX] fix swa fa accuracy because of page_table error | `python/sglang/srt/layers/attention/flashattention_backend.py` | shared |
| 2026-06-15 | `63747e66f` | RyeYuan | [BugFix] sync to support the more args 'topk_weights' in deep_ep dispatch | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-06-15 | `548f9aa20` | tianly | ci: skip GitHub artifact upload for DCU PR wheels | `.github/workflows/release-pr-dcu.yml` | shared |
| 2026-06-15 | `bb5f2fc8a` | tianly | ci: wait for DCU wheels on release workflow changes | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-06-15 | `e98c3e175` | lizhigong | Merge pull request #15 from HYGON-AI/v0.5.12_dev_moe_runer | 无直接文件变更/merge | unclassified |
| 2026-06-15 | `26fa81060` | lizhigong | Merge pull request #25 from HYGON-AI/v0.5.12_dev_unified_attn | 无直接文件变更/merge | unclassified |
| 2026-06-15 | `b0855ae72` | zhangyh15 | Merge remote-tracking branch 'origin/v0.5.12_dev' into zyh-test-lint | 无直接文件变更/merge | unclassified |
| 2026-06-15 | `fb0a68900` | zhangyh15 | Rename lint job to lint-dcu to avoid name collision with lint.yml | `.github/workflows/lint-dcu.yml` | shared |
| 2026-06-15 | `3e0abe65f` | lizhigong | Merge pull request #16 from HYGON-AI/zyh-test-lint | 无直接文件变更/merge | unclassified |
| 2026-06-16 | `bd52e179c` | yangyn1 | fix: 修复EP bug | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` | shared |
| 2026-06-16 | `26604b031` | maxiao1 | 0.5.12版本适配glm5 && glm5.2; 修复sgl-kernel custom ar精度问题 | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/triton_kernel.py` 等 20 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm5-glm51 |
| 2026-06-16 | `2b9e811e6` | maxiao1 | 适配glm5.2 | `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/overlap_utils.py` 等 9 个文件 | deepseek-v3-r1, deepseek-v32, glm5-glm51 |
| 2026-06-16 | `224e5449f` | shiqiang | [Bug Fix] fix swa mem pool duoble release | `python/sglang/srt/mem_cache/swa_memory_pool.py` | shared |
| 2026-06-16 | `24aaafde8` | chenyuege | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_chenyue | 无直接文件变更/merge | unclassified |
| 2026-06-16 | `109d8432b` | yangyn1 | minimax适配SP | `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/srt/distributed/parallel_state.py` 等 10 个文件 | minimax |
| 2026-06-16 | `e49d0d2fb` | chenyuege | [bugfix]修复sglang0.5.12官方bug,解决因此引起的Qwen3-30B-A3B-Instruct-2507精度问题 | `python/sglang/srt/models/utils.py` | qwen3-coder, qwen3-core |
| 2026-06-16 | `bb70a2268` | yangyn1 | [Perf] Add packed paged KV varlen attention path | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`, `python/sglang/srt/server_args.py` 等 6 个文件 | shared |
| 2026-06-16 | `189d8c87e` | chenyuege | [bugfix]修复md文件中的格式问题 | `.claude/skills/sglang-profile-analyse/SKILL.md`, `python/sglang/srt/models/utils.py` | shared |
| 2026-06-16 | `dfb450ccf` | yangyn1 | gate bf16*fp32 -> FP32 gemm | `python/sglang/srt/models/minimax_m2.py` | minimax |
| 2026-06-16 | `6ba33abbc` | chenyuege | Merge pull request #17 from HYGON-AI/v0.5.12_dev_chenyue | 无直接文件变更/merge | unclassified |
| 2026-06-16 | `5149eb0e9` | yangyn1 | 优化 minimax fused_rms_quant | `python/sglang/srt/models/minimax_m2.py` | minimax |
| 2026-06-16 | `de2840d1d` | lipenghui | 更新get_scheme函数为get_linear_scheme | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` | shared |
| 2026-06-16 | `42588bb8c` | lipenghui | Merge pull request #30 from HYGON-AI/v0.5.12_dev_lph | 无直接文件变更/merge | unclassified |
| 2026-06-16 | `62a23f050` | wujl5 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-16 | `d32fa4686` | wujl5 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-16 | `56b6eebcc` | wujl5 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-17 | `5cf4efb7e` | lizhigong | Merge pull request #28 from HYGON-AI/v0.5.12_dev_maxiao | 无直接文件变更/merge | unclassified |
| 2026-06-17 | `07e426bf5` | lizhigong | Merge pull request #29 from HYGON-AI/v0.5.12_dev_swa_pool_fix | 无直接文件变更/merge | unclassified |
| 2026-06-17 | `0529afb39` | yangyn1 | sp适配minimax-fp8 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` 等 4 个文件 | minimax |
| 2026-06-17 | `e0bb491ba` | yangyn1 | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_moe_runer | 无直接文件变更/merge | unclassified |
| 2026-06-17 | `e1352aca0` | yangyn1 | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_moe_runer | 无直接文件变更/merge | unclassified |
| 2026-06-17 | `f7807d3a5` | yangyn1 | 临时适配minimax-sp8 | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` | minimax |
| 2026-06-17 | `983e644d4` | caihl | fix: avoid redundant calls to forward_aiter and fp8 groupgemm kernels | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-06-17 | `94659d14a` | SYChen123 | [dsv4] cp support megamoe | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-18 | `914d50fab` | Lvjiajia | Create quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-06-18 | `38299f5fb` | yangyn1 | 修复崩溃bug | `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-06-18 | `64fe76840` | RyeYuan | [FEAT] remove vllm allreduce and dead import related | `README_DCU.md`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 4 个文件 | shared |
| 2026-06-18 | `965fc8196` | Lvjiajia | Merge pull request #33 from HYGON-AI/add-quality-gate | 无直接文件变更/merge | unclassified |
| 2026-06-18 | `cb53b9685` | RyeYuan | Merge pull request #35 from HYGON-AI/v0.5.12_dev_rye_vllm-allreduce-deprecate | 无直接文件变更/merge | unclassified |
| 2026-06-18 | `3a3df9a47` | RyeYuan | [Fetch Back] fix the bug of cp/ep | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-06-18 | `fa22ad5ae` | Lvjiajia | Add options for encoding, dependencies, and SAST scans | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-06-18 | `e0da81b8a` | Lvjiajia | Merge pull request #37 from HYGON-AI/add-quality-gate | 无直接文件变更/merge | unclassified |
| 2026-06-18 | `e80c0644a` | Lvjiajia | Update Trivy and Semgrep commands in workflow | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-06-18 | `37a67648f` | Lvjiajia | Update Trivy scan configuration in workflow | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-06-18 | `87aa66f4f` | RyeYuan | [BugFix] workaround fix of aiter custom allreduce in cuda-graph, would revert it after driver fix it | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | shared |
| 2026-06-18 | `cae6c4496` | RyeYuan | [FEAT] implement the initial changes about w8a8 megamoe for DCU | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` 等 4 个文件 | shared |
| 2026-06-19 | `68dd6d7f2` | maxiao1 | Fix DCU NSA FlashMLA paths | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/triton_kernel.py`, `python/sglang/srt/layers/attention/nsa_backend.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-06-22 | `0fc338999` | lipenghui | 修复dpsk r1 fp8启动时的报错问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-06-22 | `5d83cfe85` | RyeYuan | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` | shared |
| 2026-06-22 | `0536e102c` | RyeYuan | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` | shared |
| 2026-06-22 | `fdd9f8ecf` | shiqiang | [BUG FIX] fix SWA mem pool issue causing accept length decrease | `python/sglang/srt/mem_cache/swa_memory_pool.py` | shared |
| 2026-06-23 | `dc4e95ea9` | lizhigong | Merge pull request #38 from HYGON-AI/v0.5.12_dev_maxiao | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `9f41a0a0a` | lizhigong | Merge pull request #39 from HYGON-AI/fix/dpsk-r1-fp8-startup | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `0fc998757` | RyeYuan | Merge official main checkpoint C01 | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `ac9332fc1` | lizhigong | Merge pull request #41 from HYGON-AI/v0.5.12_dev_swa_mem_pool_fix | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `51abf3148` | DCU CI Bot | test: add DCU AI smoke cases to PR required | `.github/workflows/pr-test-dcu.yml`, `test/registered/dcu/openai_server/test_function_calling_dcu.py`, `test/registered/dcu/openai_server/test_hidden_states_base_dcu.py` 等 13 个文件 | shared |
| 2026-06-23 | `4b8a743d3` | DCU CI Bot | ci: add wheel mode to DCU full enabled | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-23 | `ca95a26da` | DCU CI Bot | ci: add DCU nightly workflow with wheel build | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-23 | `9ed791e14` | DCU CI Bot | ci: run PR helper workflows on private runner | `.github/workflows/labeler.yml`, `.github/workflows/pr-states.yml` | shared |
| 2026-06-23 | `de24697cb` | DCU CI Bot | ci: disable PR trigger for DCU nightly workflow | `.github/workflows/nightly-test-dcu.yml` | shared |
| 2026-06-23 | `9304b9e1d` | DCU CI Bot | ci: build DCU gateway wheel by default | `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-23 | `a643b4108` | dddddddxl | Merge pull request #42 from HYGON-AI/0623-dcu-ci-merge-clean | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `e4802da34` | wangaq | [feature] c16 DeepSeek V4 BF16 KV cache support | `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 9 个文件 | deepseek-v4 |
| 2026-06-23 | `571813832` | RyeYuan | Merge official main checkpoint C02 | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `599b7490f` | Alone-wl | bugfix: fix topk vmfault issue | `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-06-23 | `be7d10f53` | liyt6 | ci: add manual DCU unattended model test workflow | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` | shared |
| 2026-06-24 | `00ce3e6d9` | tianlinyang77 | ci: stage DCU PR wheels locally | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` 等 4 个文件 | shared |
| 2026-06-24 | `f4716f8ec` | zhangyh15 | Add DCU nightly wheel release workflow | `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-24 | `595f87c93` | zhangyh15 | Restore push trigger and CIUpload devpi upload | `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-24 | `dbae6e478` | reverie-hub | fix: sanitize AMD runtime logs on DCU | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/layers/attention/aiter_backend.py` 等 13 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm45, glm46-glm47, mixtral-quark-int4fp8-moe |
| 2026-06-24 | `88ba08ad2` | shiqiang | fix expert_location_dispatch_info is not define | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-06-24 | `fa9b4be84` | shiqiang | fix mimo enable pp bug | `python/sglang/srt/models/mimo_v2.py` | mimo-v2-flash |
| 2026-06-24 | `2a6333012` | lizhigong | Merge pull request #44 from HYGON-AI/temp-pr-test | 无直接文件变更/merge | unclassified |
| 2026-06-24 | `24d0abd38` | lizhigong | Merge pull request #46 from HYGON-AI/mimo_bug_fix | 无直接文件变更/merge | mimo-v2-flash |
| 2026-06-24 | `523756bde` | RyeYuan | [docs(dcu)] log C01/C02 conflict ledger update | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-24 | `5b19ad464` | RyeYuan | [fix(deepseek-v4)]: keep DCU on non-HIP attention backend + compressor | `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py` | deepseek-v4 |
| 2026-06-24 | `1b2694156` | RyeYuan | [fix(deepseek-v4)]: remove unused codes and use ScheduleBatch extend_lens/prefix_lens in init_new | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-24 | `8303d60f7` | RyeYuan | Merge official main checkpoint C03 | 无直接文件变更/merge | unclassified |
| 2026-06-25 | `a21b0b6ef` | LvJIA-RG | test: preserve local DCU AI smoke and accuracy cases | `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py` 等 10 个文件 | qwen-vlm-omni-asr |
| 2026-06-25 | `85cd7901c` | LvJIA-RG | test: keep verified DCU smoke and accuracy cases only | `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py` 等 4 个文件 | shared |
| 2026-06-25 | `4a08e1934` | tianlinyang77 | test: add DCU nightly 1 and 2 GPU suites | `test/registered/core/test_mm_process_config.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py` 等 19 个文件 | shared |
| 2026-06-25 | `8a8ebbfc6` | maxiao1 | 修改SGLANG_USE_AITER_AR默认关闭 | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/attention/nsa/triton_kernel.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-06-25 | `d1ea0b3aa` | liyt6 | ci: support configurable manual DCU model validation | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` | shared |
| 2026-06-25 | `3dd1376ff` | liyt6 | docs: fix DCU README trailing whitespace | `README_DCU.md` | shared |
| 2026-06-25 | `4a6b5a816` | Lyt | Merge pull request #49 from HYGON-AI/feature/manual-dcu-unattended-model-test | 无直接文件变更/merge | unclassified |
| 2026-06-25 | `9abb848db` | RyeYuan | [Feat] support megamoe in the path of SGLANG_DCU_MEGA_MOE_RUNTIME=megamoe, and temporarily deepgeem path is still remained as backup | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 7 个文件 | shared |
| 2026-06-25 | `c7a4903ad` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-25 | `6844a8693` | janeeyreliu | feat: hy3 mtp support dp attention | `python/sglang/srt/models/hunyuan_v3_nextn.py` | hunyuan3-preview |
| 2026-06-26 | `54f44d298` | DCU CI Bot | test: add DCU cookbook nightly model coverage | `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py` 等 24 个文件 | deepseek-v32, glm5-glm51, kimi, mimo-v2-flash, minimax |
| 2026-06-26 | `ca7c7c54f` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `2f2abec11` | DCU CI Bot | ci: cover new DCU nightly suites in full enabled | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-26 | `db4759e78` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `20eb46a70` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `0c4fe5ebe` | DCU CI Bot | ci: align DCU full wheel wait with PR staging | `.github/workflows/dcu-full-enabled.yml` | shared |
| 2026-06-26 | `7d807cb22` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `8aa4b6eb5` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `21dfaaa4c` | Lyt | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` | shared |
| 2026-06-26 | `00febcba4` | DCU CI Bot | ci: reuse PR-staged DCU nightly wheels | `.github/workflows/nightly-test-dcu.yml` | shared |
| 2026-06-26 | `a2076d9aa` | DCU CI Bot | test: use local DCU eval datasets | `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_mmlu.py` 等 4 个文件 | shared |
| 2026-06-27 | `db4a26316` | DCU CI Bot | test: use local DCU model paths for smoke tests | `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py` | qwen-vlm-omni-asr |
| 2026-06-28 | `f40a12fb5` | liucong | 修改IPC逻辑，每个rank下都开辟内存池，解决rank0偶发变慢的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py` | shared |
| 2026-06-29 | `86d6fd542` | Lyt | Merge pull request #50 from HYGON-AI/fix/dcu-runtime-log-sanitize | 无直接文件变更/merge | unclassified |
| 2026-06-29 | `5f2985983` | lizhigong | Merge pull request #48 from HYGON-AI/v0.5.12_dev_maxiao | 无直接文件变更/merge | unclassified |
| 2026-06-29 | `395171de0` | LvJIA-RG | test: fix DCU MMMU local dataset selection | `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py` | shared |
| 2026-06-29 | `83294cba6` | zhangyh15 | Add DCU nightly wheel release workflow with vendored-openssl support | `.github/workflows/release-pypi-nightly-dcu.yml` | shared |
| 2026-06-29 | `0553e12d0` | yangyn | 修复合并分支产生的bug | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-06-29 | `06889adc0` | DCU CI Bot | Disable DCU update weights from disk nightly test | `test/registered/rl/test_update_weights_from_disk.py` | shared |
| 2026-06-29 | `01216a18f` | DCU CI Bot | Disable DCU remote weight loading nightly test | `test/registered/distributed/test_load_weights_from_remote_instance.py` | shared |
| 2026-06-29 | `347434c31` | lizhigong | Merge pull request #51 from HYGON-AI/temp-pr-test | 无直接文件变更/merge | unclassified |
| 2026-06-29 | `e23638045` | wufan3 | 为kimi-k2.6适配marlin moe | `python/sglang/srt/model_loader/weight_utils.py` | kimi |
| 2026-06-29 | `75e928284` | DCU CI Bot | Register DCU tests in categorized nightly suites | `test/registered/constrained_decoding/test_constrained_decoding.py`, `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/embedding/bw1100/test_gte_qwen2_embedding_dcu.py` 等 28 个文件 | shared |
| 2026-06-29 | `6fb7d6ec3` | lizhigong | Merge pull request #52 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.6-marlin | 无直接文件变更/merge | kimi |
| 2026-06-29 | `fa2430f45` | DCU CI Bot | Organize DCU nightly workflow modules | `.github/workflows/nightly-test-dcu.yml` | shared |
| 2026-06-29 | `1a8266b2c` | DCU CI Bot | Merge remote-tracking branch 'origin/test-pr-trigger-dcu-0625' into HEAD | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `129b3d05e` | Alone-wl | feat: Add lightop topk env & Improve multi stream overlap. | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-30 | `c4cc0a73b` | RyeYuan | fix(dsv4): preserve DCU elementwise and topk paths | `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-06-30 | `d22548eb1` | yaoht | feat(sgl-kernel): port l2norm kernel with tiled optimization for DCU | `python/sglang/srt/layers/attention/fla/l2norm.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/common_extension.cc` 等 11 个文件 | shared |
| 2026-06-30 | `93cf8edc4` | RyeYuan | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-30 | `b76f31cce` | Lvjiajia | Refactor quality-gate.yml with enhanced checks | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-30 | `631212b52` | whlwhlwhl | feat(eplb): make expert distribution collection PP-safe | `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` 等 4 个文件 | deepseek-v4 |
| 2026-06-30 | `f2e257f7a` | whlwhlwhl | feat(dcu): route sqrtsoftplus gating through LightOp | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-06-30 | `f8b2eefcf` | whlwhlwhl | feat(dsv4): generalize top-k index transformation | `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-06-30 | `bda910adb` | whlwhlwhl | feat(dcu): integrate LightOp alloc-extend kernel | `python/sglang/srt/mem_cache/allocator.py` | shared |
| 2026-06-30 | `c0b27a966` | LuoYao | [feat]: 支持pd分离下hunyuanv3 p节点ep8跑通. | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-06-30 | `ea182d81e` | Lvjiajia | Update quality gate workflow with environment variables | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-30 | `810624fbe` | RyeYuan | Merge official main checkpoint C04 | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `412236292` | Lvjiajia | Modify ruff command to use --no-cache | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-30 | `bd10f999c` | Lvjiajia | Fix formatting and improve quality gate script | `.github/workflows/quality-gate.yml` | shared |
| 2026-06-30 | `91b1aa386` | lizhigong | Merge pull request #53 from HYGON-AI/v0.5.12_dev_hy3_pd | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `f2d0e86d7` | RyeYuan | fix(dsv4): repair DCU sgl-kernel and JIT build | `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py` | deepseek-v4 |
| 2026-06-30 | `3910b3f9d` | RyeYuan | fix(scheduler): restore DCU empty-prefix location | `python/sglang/srt/managers/schedule_batch.py` | shared |
| 2026-06-30 | `ff440b897` | RyeYuan | docs(dcu): record C04 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-30 | `08c1fd5a0` | RyeYuan | Merge official main checkpoint C05 | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `445eaafe5` | shiqiang | [Perf] optimize aiter asm moe via shuffle weight | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-07-01 | `dbe95efd8` | luoyao | 修复IPC报错的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/moss_vl.py`, `python/sglang/srt/multimodal/processors/transformers_auto.py` | moss-vl |
| 2026-07-01 | `41db24a84` | Lvjiajia | Enhance quality baseline scan with new checks | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-07-01 | `20f106c6b` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-07-01 | `72f023717` | Lvjiajia | Remove credential keyword pattern from scan config | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-07-01 | `af015c4ce` | Lvjiajia | Update Trivy cache volume permissions | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-07-01 | `35456bae3` | RyeYuan | [CI] fix pre-commit lint errors on megamoe w8a8 changed files | `.codespellrc`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 7 个文件 | shared |
| 2026-07-01 | `7ced3e2c7` | RyeYuan | Merge branch 'v0.5.12_dev' into v0.5.12_dev_rye_megamoe | 无直接文件变更/merge | unclassified |
| 2026-07-01 | `2b1fbe1e6` | RyeYuan | [CI] fix pre-commit lint errors surfaced after merging v0.5.12_dev | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-07-01 | `696cae936` | lzb16 | fix(fst): use local device in fastsafetensors iterator for multi-node loading | `python/sglang/srt/model_loader/weight_utils.py` | shared |
| 2026-07-01 | `998ffb809` | lzb16 | fix(fst): reclaim reserved memory after fastsafetensors weight load | `python/sglang/srt/model_loader/loader.py` | shared |
| 2026-07-01 | `1a4b4404e` | liucong8560 | 修复qwen3.5-397b PD分离不支持的问题 | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-01 | `5eebbee0f` | lizhigong | Merge pull request #57 from HYGON-AI/lzb/fst-multinode-device-fix | 无直接文件变更/merge | unclassified |
| 2026-07-01 | `e6d4b3378` | RyeYuan | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-01 | `16cff03a2` | RyeYuan | Merge official main checkpoint C06 | 无直接文件变更/merge | unclassified |
| 2026-07-01 | `ef3571f7b` | liucong8560 | 解决CI报错问题 | `python/sglang/srt/utils/cuda_ipc_transport_utils.py` | shared |
| 2026-07-02 | `51919579e` | reverie-hub | fix: refine HCU runtime log platform labels | `python/sglang/check_env.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` 等 14 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm45, glm46-glm47, mixtral-quark-int4fp8-moe |
| 2026-07-02 | `66ed7efb4` | RyeYuan | Merge pull request #55 from HYGON-AI/v0.5.12_dev_rye_megamoe | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `71cbfd64b` | wangaq | [bugfix] fix C16 BF16 KV cache writes | `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/utils.py` 等 4 个文件 | deepseek-v4 |
| 2026-07-02 | `633270429` | DCU CI Bot | ci: extend DCU stage-b per-file timeout | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-07-02 | `758a0a989` | Lvjiajia | Add open-source compliance configuration file | `.github/open-source-compliance.json` | shared |
| 2026-07-02 | `fc2af9331` | Lvjiajia | Add open-source compliance baseline workflow | `.github/workflows/open-source-compliance-baseline.yml` | shared |
| 2026-07-02 | `4d23b7e41` | liucong521 | Merge pull request #56 from HYGON-AI/v0.5.12_dev_liucong | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `dd2685439` | sunjf | support w4a16 moe ep | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` | shared |
| 2026-07-02 | `07dbcb715` | lizhigong | Merge pull request #54 from HYGON-AI/aiter_asm_shuffle | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `4763e7a9b` | lizhigong | Merge pull request #58 from HYGON-AI/lzb/fst-empty-cache-reclaim | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `249a70dbe` | RyeYuan | [Addition] deliver one validation doc and support multi-stream in hip backend | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-02 | `1fa5343d1` | whlwhlwhl | Merge remote-tracking branch 'origin/v0.5.12_dev' into codex/pr59-review | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `84bd983ba` | dingxl | ci: use local DCU reranker model | `.github/workflows/pr-test-dcu.yml` | shared |
| 2026-07-02 | `379da22b4` | whlwhlwhl | fix: address PR review and lint failures | `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/moe/topk.py` 等 6 个文件 | deepseek-v4 |
| 2026-07-02 | `593df5e14` | RyeYuan | Merge official main checkpoint C07 | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `abc5b4e0e` | wanghl | Merge pull request #59 from HYGON-AI/sgl0512_wanghl_dev | 无直接文件变更/merge | unclassified |
| 2026-07-03 | `ce2521017` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-07-03 | `ec812cf6e` | jiafei96 | Merge pull request #60 from HYGON-AI/v0.5.12_dev_ep_w4a16 | 无直接文件变更/merge | unclassified |
| 2026-07-03 | `c3dc2e8eb` | maxiao1 | feat: validate DCU attention backend compatibility | `python/sglang/srt/server_args.py` | shared |
| 2026-07-03 | `fc241f4ad` | RyeYuan | [BugFix] Sync to official changes to remove first pre-warmup of mHC | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-03 | `00063277c` | RyeYuan | [Addition] deliver one validation doc of C07 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-03 | `01f8caf22` | RyeYuan | Merge official main checkpoint C08 | 无直接文件变更/merge | unclassified |
| 2026-07-03 | `8efd2ad46` | sunjf | update w4a16 deepgemm interface | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-07-03 | `59689b572` | jiafei96 | Merge pull request #63 from HYGON-AI/v0.5.12_dev_w4a16_deepgemm | 无直接文件变更/merge | unclassified |
| 2026-07-04 | `cd2e73a67` | Lvjiajia | 优化lint扫描规则 | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-05 | `36f323752` | reverie-hub | fix: refine HCU runtime log wording | `python/sglang/check_env.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/mxfp4.py` 等 9 个文件 | shared |
| 2026-07-05 | `1e967ec11` | Lv Jiajia | chore: add Apache headers for DCU files | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` 等 121 个文件 | deepseek-v32, deepseek-v4, glm5-glm51, gpt-oss, kimi, mimo-v2-flash, minimax, nemotron-super, qwen-vlm-omni-asr, qwen3-next |
| 2026-07-05 | `2d561a3ec` | Lv Jiajia | chore: add modification notices for DCU changes | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py` 等 254 个文件 | unclassified |
| 2026-07-05 | `107be429b` | Lv Jiajia | chore: fix encoding baseline issues | `3rdparty/amd/profiling/torch_profiler.patch`, `docs/supported_models/specialized/reward_models.md`, `docs_new/docs/developer_guide/development_guide_using_docker.mdx` 等 13 个文件 | shared |
| 2026-07-05 | `438d47e1d` | Lv Jiajia | chore: sanitize public docs examples | `benchmark/deepseek_v3/README.md`, `docs/advanced_features/sgl_model_gateway.md`, `docs/developer_guide/bench_serving.md` 等 19 个文件 | deepseek-v3-r1, deepseek-v32 |
| 2026-07-06 | `88bb5176c` | RyeYuan | [Addition] deliver one validation doc of C08 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-06 | `2ada58179` | RyeYuan | Merge official main checkpoint C09 | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `2bcf9e7e7` | reverie-hub | ci: add HCU runtime text quality gate | `.github/workflows/quality-gate.yml`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py` 等 6 个文件 | mixtral-quark-int4fp8-moe |
| 2026-07-06 | `10e17ae89` | yangwl | loader: stream FSDP state dicts for Ulysses SP | `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py` | shared |
| 2026-07-06 | `fd2163b9f` | yangwl | wan: use full VAE path for I2V and TI2V | `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py` | shared |
| 2026-07-06 | `cbb50e347` | yangwl | profiler: add profile start step parameter | `python/sglang/multimodal_gen/configs/sample/sampling_params.py` | shared |
| 2026-07-06 | `9a3c7dbb4` | yangwl | rocm: allow flash attention backend selection | `python/sglang/multimodal_gen/runtime/platforms/rocm.py` | shared |
| 2026-07-06 | `7401b75cf` | wanly young | Merge pull request #65 from HYGON-AI/v0.5.12_dev_ywl | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `9eb6129e4` | lizhigong | Merge pull request #62 from HYGON-AI/v0.5.12_dev_attnbackend | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `73f6c5740` | reverie-hub | refactor: use HCU platform detection naming | `python/sglang/check_env.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` 等 16 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm45, glm46-glm47, mixtral-quark-int4fp8-moe |
| 2026-07-06 | `fa6b75971` | RyeYuan | [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py` | shared |
| 2026-07-06 | `bc13c0a98` | yangwl | [sgl-diffusion] Fix Wan T2V VAE decode path | `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py` | shared |
| 2026-07-06 | `dd96c4cb8` | wanly young | Merge pull request #66 from HYGON-AI/v0.5.12_dev_ywl | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `ad2ff869c` | RyeYuan | [BugFix] Backport partial bugfixes from C10 and also have to assign SGLANG_USE_AITER_AG=0 to ensure accuracy now | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` 等 9 个文件 | deepseek-v4 |
| 2026-07-06 | `a1ed918ae` | RyeYuan | [Addition] deliver one validation doc of C09 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-06 | `fffe84acb` | liuchy5 | feat: support EPLB for hunyuan_v3 and hunyuan_v3_nextn | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` | hunyuan3-preview |
| 2026-07-06 | `3b0e1b709` | luoyao | [bug fix] hunyuanv3精度异常解决 | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-06 | `23cbd00e3` | luoyao | [bugfix]: 解决hy3非mtp下的精度问题 | `python/sglang/srt/disaggregation/prefill.py` | shared |
| 2026-07-06 | `ec48fa780` | luoyao | [bugfix]: 解决hy3开mtp下的精度问题. | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` 等 4 个文件 | shared |
| 2026-07-06 | `92c15b3d8` | luoyao | [bug fix] hunyuanv3精度异常解决 | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-06 | `cf59f4695` | luoyao | [bugfix]: avoid HYV3 PD KV compact remap | `python/sglang/srt/disaggregation/common/conn.py` | shared |
| 2026-07-07 | `02858213c` | LuoYao | style: fix pre-commit formatting | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` 等 4 个文件 | hunyuan3-preview |
| 2026-07-07 | `4d198708c` | yangyn1 | 解决sp下对padding的处理 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` | shared |
| 2026-07-07 | `0507e6090` | reverie-hub | fix: avoid amdsmi runtime logs on HCU | `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | shared |
| 2026-07-07 | `88fb5162e` | yangyn1 | Merge branch 'v0.5.12_dev' into merge_minimax_sp_opt | 无直接文件变更/merge | minimax |
| 2026-07-07 | `5f232f552` | RyeYuan | Merge official main checkpoint C10 | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `2285ae0a6` | lizhigong | Merge pull request #68 from HYGON-AI/v0.5.12_dev_hy3_pd_disaggregation | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `3f920d4e0` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-07-07 | `e9c2e28b5` | Lyt | Merge branch 'v0.5.12_dev' into fix/dcu-runtime-log-sanitize | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `2d48f0170` | Lyt | Merge pull request #69 from HYGON-AI/fix/dcu-runtime-log-sanitize | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `9bde26e7c` | liucong | 解耦vllm rms_norm | `python/sglang/srt/layers/layernorm.py` | shared |
| 2026-07-07 | `f33aed3c8` | liucong521 | Merge pull request #75 from HYGON-AI/v0.5.12_dev_rmsnorm | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `d5f4d1c14` | liuchy5 | fix: skip expert distribution recording during CUDA graph capture | `python/sglang/srt/eplb/expert_distribution.py` | shared |
| 2026-07-07 | `18ad4faac` | Lv Jiajia | Merge remote-tracking branch 'origin/v0.5.12_dev' into fix/open-source-compliance-202607 | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `9188d711e` | reverie-hub | ci: rename HCU runtime text check script | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/check_no_amd_runtime_text.py` | shared |
| 2026-07-07 | `ef36df96f` | Lv Jiajia | chore: add header for DCU runtime text checker | `scripts/ci/dcu/check_no_amd_runtime_text.py` | shared |
| 2026-07-07 | `0d21d1568` | zhouyu | allow atten tp size to be 1 | `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/server_args.py` | mimo-v2-flash |
| 2026-07-07 | `249ea9001` | Lyt | Merge pull request #77 from HYGON-AI/fix/hcu-runtime-log-sanitize | 无直接文件变更/merge | unclassified |
| 2026-07-07 | `fe4e1fea3` | github-actions[bot] | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` | shared |
| 2026-07-08 | `3bacdc963` | Lv Jiajia | Merge remote-tracking branch 'origin/v0.5.12_dev' into fix/open-source-compliance-202607 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `5796eff14` | Lvjiajia | Merge pull request #76 from HYGON-AI/fix/open-source-compliance-202607 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `bfaf180d1` | RyeYuan | [Addition] deliver one validation doc of C10 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `bae695b56` | RyeYuan | Merge official main checkpoints C11-C13 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `baf11236a` | liuchy5 | style: fix pre-commit formatting for hunyuan_v3 and hunyuan_v3_nextn | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` | hunyuan3-preview |
| 2026-07-08 | `5d2c6854a` | shangxl | 0.5.12 MHA、GQA类hicache适配 | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` 等 10 个文件 | shared |
| 2026-07-08 | `b6db54a9a` | RyeYuan | [Addition] deliver one validation doc of C11~C13 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `293fa64f0` | RyeYuan | Merge commit '2ad00faae1f4f413330fbc1241dc2c79f44ac4d4' into sync/official-main-C14-C16-20260616 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `1cea713a7` | RyeYuan | docs(dcu): record C14-C16 validation block | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `b452d6bd6` | RyeYuan | docs(dcu): record C14-C16 functional validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `63d3aece4` | luoyao | merge v0.5.12_dev_eplb_hy3 into v0.5.12_dev | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `5eb556f88` | liuchy5 | [feature]:hunyuan_v3 EPLB support with redundant experts | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` | hunyuan3-preview |
| 2026-07-08 | `caebec30d` | shiqiang | [perf] use aiter custom op for reduce_scatter and all_gather and fix eplb dump distribute error | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/models/mimo_v2.py` | mimo-v2-flash |
| 2026-07-08 | `1a61a9b60` | lijing | Fix the PP assertion issue | `python/sglang/srt/arg_groups/deepseek_v4_hook.py` | deepseek-v4 |
| 2026-07-09 | `01a6f1b94` | RyeYuan | [Addition] deliver one validation doc of C14~C16 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `15abf620c` | RyeYuan | Merge official SGLang C17-C19 into DCU bootstrap | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `cee45bc55` | RyeYuan | docs(dcu): record C17-C19 validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `3e254b041` | shiqiang | style(distributed): apply pre-commit formatting to parallel_state.py | `python/sglang/srt/distributed/parallel_state.py` | shared |
| 2026-07-09 | `4b0fcbd07` | RyeYuan | [Addition] deliver one validation doc of C17~C19 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `44f1d2b06` | lizhigong | Merge pull request #82 from HYGON-AI/v0.5.12_dev_lj | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `ac1f72cc5` | lizhigong | Merge pull request #81 from HYGON-AI/mimo_pref_communication_and_eplb | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-09 | `76d14014a` | RyeYuan | Merge official main bootstrap C01-C19 into main | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `fcc3e6e18` | liuchy5 | resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-09 | `8b4a7bdeb` | reverie-hub | ci: refine HCU runtime text check message | `scripts/ci/dcu/check_hcu_runtime_text.py` | shared |
| 2026-07-09 | `e2a86e8bb` | yangyn1 | pack_kv only support minimax_opt | `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py` | minimax |
| 2026-07-09 | `5fdffaac3` | liuchy5 | Revert "resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py" | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-09 | `fba577896` | liuchy5 | Revert "[feat]: HY3 support PP" | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-09 | `fda6d44a4` | reverie-hub | ci: simplify HCU runtime text check failure message | `scripts/ci/dcu/check_hcu_runtime_text.py` | shared |
| 2026-07-09 | `d7af9508d` | lizhigong | style: apply CI hook formatting | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py` | shared |
| 2026-07-09 | `616ba7b6d` | reverie-hub | ci: reduce HCU runtime text check duplicate output | `scripts/ci/dcu/check_hcu_runtime_text.py` | shared |
| 2026-07-09 | `36421829e` | lizhigong | style: apply CI hook formatting | `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/server_args.py` | mimo-v2-flash |
| 2026-07-09 | `d445921fe` | WuFan | 新增对RadixAttention层的判断 | `python/sglang/srt/layers/quantization/w8a8_int8.py` | shared |
| 2026-07-09 | `d8f3057b3` | RyeYuan | Merge official main catchup 20260623 into DCU main | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `dccf1782b` | reverie-hub | ci: disable HCU runtime text check job | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-09 | `b38f25513` | DCU CI Bot | ci: add manual HCU nightly workflow controls | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 17 个文件 | shared |
| 2026-07-09 | `dd0492dbf` | luoyao | [PD]解决qwen3.5-397b在pd分离场景下的精度问题 | `python/sglang/srt/disaggregation/common/conn.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-10 | `c946da188` | lizhigong | Merge pull request #78 from HYGON-AI/v_0.5.12_dev-mimo-pro-atten-tp1 | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-10 | `c7258ab3c` | lizhigong | Merge pull request #80 from HYGON-AI/v0.5.12_dev_sxl | 无直接文件变更/merge | unclassified |
| 2026-07-10 | `8838e5cf3` | lizhigong | Merge pull request #84 from HYGON-AI/merge_minimax_sp_opt | 无直接文件变更/merge | minimax |
| 2026-07-10 | `d2480f3eb` | lizhigong | Merge pull request #85 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.7 | 无直接文件变更/merge | kimi |
| 2026-07-10 | `0334ae99b` | lizhigong | Merge pull request #86 from HYGON-AI/v0.5.12_dev_fix_qwen3.5_397b | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-10 | `5e0409d1b` | shiqiang | [feat] support rope fuse and support w8a8_int8 for kme | `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/models/mimo_v2.py` | mimo-v2-flash |
| 2026-07-11 | `390ad18e7` | tianly | ci: 修复 packed KV 测试注册导致的 DCU CI 收集失败 (#87) | `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`, `benchmark/kernels/pack_paged_kv_to_varlen/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/bench_pack_paged_kv_to_varlen.py` 等 5 个文件 | shared |
| 2026-07-11 | `0395a2bd2` | yangql | fix: use lightop int8 deepep moe on dcu | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` | shared |
| 2026-07-13 | `a8d65f781` | lizhigong | Merge pull request #89 from HYGON-AI/v0.5.12_dev_yql | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `229546bb1` | lizhigong | Merge pull request #88 from HYGON-AI/mimo_kme_support_and_rope_fuse | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-13 | `e3fee4310` | DCU CI Bot | ci: sync HCU workflows and scripts with current main | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 33 个文件 | shared |
| 2026-07-13 | `f38f1a5d2` | DCU CI Bot | test: sync HCU registrations with current main | `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py` 等 322 个文件 | unclassified |
| 2026-07-13 | `4fb3f0939` | DCU CI Bot | runtime: migrate current main DCU interfaces to HCU | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` 等 80 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, hunyuan3-preview, mimo-v2-flash, minimax, mixtral-quark-int4fp8-moe, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-13 | `de7170db0` | DCU CI Bot | kernel: migrate DCU ops and wrappers to HCU | `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h` 等 5 个文件 | shared |
| 2026-07-13 | `9353ecb96` | DCU CI Bot | docs: complete HCU naming migration | `NOTICE`, `README.md`, `README_DCU.md` 等 7 个文件 | shared |
| 2026-07-13 | `1123fc038` | DCU CI Bot | ci: enforce HCU rename safety checks | `scripts/ci/hcu/hcu_rename_allowlist.txt`, `scripts/ci/hcu/test_verify_hcu_rename.py`, `scripts/ci/hcu/verify_hcu_registration.py` 等 4 个文件 | shared |
| 2026-07-13 | `cba9e72cc` | RyeYuan | [BugFix] skip some uncompatibal env setup in hip for DCU | `python/sglang/srt/server_args.py` | shared |
| 2026-07-13 | `48489724d` | RyeYuan | docs(dcu): record 20260623 catch-up runtime status | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-13 | `5760f5ba1` | Lv Jiajia | chore: add headers for new compliance findings | `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`, `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py` 等 4 个文件 | minimax |
| 2026-07-13 | `2da685949` | Lvjiajia | Merge pull request #91 from HYGON-AI/fix/v0512dev-compliance-headers-20260713 | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `b9cf8ac56` | RyeYuan | Merge official main catchup 20260625 into DCU main | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `40c658e8a` | reverie-hub | ci: harden HCU runtime text checker | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` | shared |
| 2026-07-13 | `bd60c0223` | Lvjiajia | Enhance quality gate workflow with new checks and branches | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-13 | `bb9bb4b2d` | DCU CI Bot | ci: rename HCU PR stage suites | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `docs/hcu-pr-ci-visual-guide.html` 等 157 个文件 | unclassified |
| 2026-07-13 | `dcd4013b3` | RyeYuan | Merge official SGLang main through 2026-06-29 | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `1c70e76d5` | DCU CI Bot | test: use verified local HCU model paths | `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`, `test/registered/hcu/lora/bw1100/test_qwen3_lora_server_hcu.py`, `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_instruct_hcu.py` 等 8 个文件 | shared |
| 2026-07-13 | `8c797abd6` | RyeYuan | Record 20260629 DCU runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-13 | `427726d60` | reverie-hub | fix: complete HCU runtime text cleanup | `python/sglang/multimodal_gen/runtime/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` 等 6 个文件 | shared |
| 2026-07-13 | `24bcdba3b` | whlwhlwhl | feat: support AITER W4A16 MOE_C prefill | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | shared |
| 2026-07-13 | `bf59e99fd` | reverie-hub | ci: harden HCU runtime text quality gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py` | shared |
| 2026-07-13 | `d8ed552da` | RyeYuan | docs(dcu): add 20260629 conflict review | `docs/internal/dcu-main-catchup-20260629-conflict-review.md` | shared |
| 2026-07-13 | `c078943aa` | whlwhlwhl | chore: fix fused_moe lint issues | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | shared |
| 2026-07-13 | `c4de02791` | RyeYuan | Merge official SGLang main through 2026-07-03 | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `6bf9d1872` | RyeYuan | fix(dcu): reconcile DSV4 prewarm and fused Q imports | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-13 | `516a35c40` | RyeYuan | docs(dcu): record 20260703 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `2981595c7` | yangyn | [FIX] 修复走非dcu_fa下的报错 | `python/sglang/srt/layers/attention/flashattention_backend.py` | shared |
| 2026-07-14 | `dacd24f57` | LvJIA-RG | ci:resolve-hcu-ci-path-rename-conflicts | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `d53953dbe` | reverie-hub | ci: clean up HCU validation checks | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/tests/test_check_hcu_runtime_text.py` | shared |
| 2026-07-14 | `b9ca7c2ad` | Lvjiajia | Refine copyright/license warning messages | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-14 | `84a8a08ac` | RyeYuan | [BugFix] skip pre-warmup of mHC for DCU and update validation docs | `docs/internal/dcu-main-catchup-20260703-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-14 | `f96aaeb79` | RyeYuan | Merge official main catch-up through 20260706 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `b5f9777d2` | RyeYuan | Fix DCU DSV4 hash top-k router dtype | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-07-14 | `962a83462` | lizhigong | Merge pull request #94 from HYGON-AI/Sherlolo-patch-1 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `e3aa204a0` | RyeYuan | docs(dcu): require catch-up conflict reviews | `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md` | shared |
| 2026-07-14 | `6cd17f3e3` | RyeYuan | Merge official SGLang main through 2026-07-09 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `412d0ef9f` | RyeYuan | docs(dcu): add 20260709 conflict review | `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `311ead633` | LvJIA-RG | fix:merge-hcu-flashattention-token-accounting | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `0d61dcb98` | janeeyreliu | fix(eplb): fix static/dynamic EPLB accuracy and layer broadcast bug in expert dump | `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-14 | `c0e8edd74` | RyeYuan | fix(dcu): initialize DeepEP dispatch dtype state | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-07-14 | `f1c5eda31` | reverie-hub | ci: require HCU runtime text check | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-14 | `48c3c0997` | reverie-hub | ci: run HCU text check in Python 3.10 container | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-14 | `77e360722` | DCU CI Bot | ci: update HCU nightly accuracy and PR coverage | `.github/workflows/pr-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/test_verify_hcu_rename.py` 等 7 个文件 | deepseek-v32, minimax |
| 2026-07-14 | `6e0a964d1` | yuchenyang | Fix DeepSeek fused RMS quant MoE path | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-14 | `88f43c7e1` | dddddddxl | test: add Qwen3.6 HCU smoke and accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py` | qwen3-coder, qwen3-core, qwen36 |
| 2026-07-14 | `57f33814f` | shiqiang | mimo eplb dump fix and resume swa mem pool | `python/sglang/srt/mem_cache/swa_memory_pool.py`, `python/sglang/srt/models/mimo_v2.py` | mimo-v2-flash |
| 2026-07-14 | `1a2c734e5` | RyeYuan | Merge official main catch-up through 20260710 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `9d7fbb017` | RyeYuan | docs: add 20260710 conflict review | `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `24894692e` | RyeYuan | fix: use runtime attention TP size in model warmup | `python/sglang/srt/model_executor/model_runner.py` | shared |
| 2026-07-14 | `6630db3cf` | RyeYuan | docs: record 20260710 pure-TP validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `3d77308ea` | RyeYuan | docs: mark 20260710 catch-up validated | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `3e335fce8` | RyeYuan | docs: correct 20260710 endpoint subject | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `2310ec541` | zhouyu | mimo mtp atten tp 1 | `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py` | mimo-v2-flash |
| 2026-07-15 | `c13cc3dea` | yangyn1 | [FIX] 修复 deepseekv3.2 mlp报错+rms_norm_quant接入问题 | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-15 | `1109d462d` | huojianqiang | [Feature] Support PD different-TP transfer for hybrid SWA/NSA and unequal K/V item lens. | `python/sglang/srt/disaggregation/mooncake/conn.py` | shared |
| 2026-07-15 | `0f6c8298b` | RyeYuan | Revert "Fix DeepSeek fused RMS quant MoE path" | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-15 | `9ec22c5c9` | RyeYuan | Merge sync/official-main-catchup-20260710 into main | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `7fa6d89c3` | RyeYuan | Merge official main catch-up through 20260712 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `baa08af59` | RyeYuan | docs(dcu): add 20260712 conflict review | `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `44f81e8f7` | RyeYuan | docs(dcu): record 20260712 runtime gate status | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `0b30b7c9d` | RyeYuan | docs(dcu): record 20260712 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `aee7f8f79` | lizhigong | Merge pull request #95 from HYGON-AI/v0.5.12_dev_mimo_pd | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-15 | `760fb1010` | lizhigong | Merge pull request #98 from HYGON-AI/fix_deepseekv32 | 无直接文件变更/merge | deepseek-v3-r1, deepseek-v32 |
| 2026-07-15 | `4cf623bfe` | lizhigong | Merge pull request #97 from HYGON-AI/v_0.5.12_dev-mimo-pro-mtp-atten-tp1 | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-15 | `522f9dfee` | lizhigong | Merge pull request #96 from HYGON-AI/mimo_eplb_fix | 无直接文件变更/merge | mimo-v2-flash |
| 2026-07-15 | `e59b241df` | lizhigong | Merge pull request #92 from HYGON-AI/fuse_moe_w4a16 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `4cc240b90` | RyeYuan | Merge official main catch-up through 20260713 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `324181561` | RyeYuan | docs(dcu): add 20260713 conflict review | `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `7f8f5cd28` | dddddddxl | test: tune HCU text accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` | kimi |
| 2026-07-15 | `21a4a455e` | RyeYuan | Merge official main through v0.5.15.post1 equivalent | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `20633db57` | RyeYuan | docs(dcu): add 20260714 conflict review | `docs/internal/dcu-main-catchup-20260714-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `f67cdf69b` | RyeYuan | docs(dcu): record 20260714 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `49a10aec8` | RyeYuan | docs(dcu): record 20260714 owner validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `d67c7e44e` | RyeYuan | merge(dcu): forward-port v0.5.12_dev step 1 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `d71a069b7` | RyeYuan | merge(dcu): forward-port v0.5.12_dev step 2 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `0d3dbd7ab` | RyeYuan | merge(dcu): forward-port v0.5.12_dev step 3 | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `69315951c` | RyeYuan | merge(dcu): forward-port v0.5.12_dev step 4 | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `bdd8d46cc` | RyeYuan | merge(dcu): forward-port v0.5.12_dev step 5 | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `dc1323ba4` | RyeYuan | docs(dcu): finalize v0.5.12_dev forward-port | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md` | shared |
| 2026-07-16 | `7df16485f` | RyeYuan | merge(dcu): land v0.5.12_dev forward-port on main | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `339dfe433` | RyeYuan | docs(dcu): define v0.5.15.post1 release workflow | `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md` | shared |
| 2026-07-16 | `8e5e785ea` | liuchy5 | style: fix pre-commit formatting in hunyuan_v3.py | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-16 | `993a79e08` | lizhigong | Merge pull request #99 from HYGON-AI/v0.5.12_dev_pp_with_eplb | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `e5a2dd041` | chenyuege | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` | shared |
| 2026-07-16 | `9b4a5e3ec` | lizhigong | Merge pull request #101 from HYGON-AI/v0.5.12_dev_chenyue_causal_conv1d | 无直接文件变更/merge | unclassified |
| 2026-07-16 | `d28069157` | chenyuege | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` | shared |
| 2026-07-16 | `09d7a1d4c` | sunjf | support fabric aiter custom allreduce | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/model_runner.py` 等 5 个文件 | shared |
| 2026-07-16 | `37074c9af` | lijing | Fix dsv4 full token pool | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` | deepseek-v4 |
| 2026-07-16 | `0769f832d` | dddddddxl | test: tighten HCU accuracy thresholds | `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py` 等 11 个文件 | kimi |
| 2026-07-17 | `592b9a4e5` | LvJIA-RG | test: add HCU coverage for GLM-5 MiMo and Qwen3.5 | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py` 等 12 个文件 | glm5-glm51, mimo-v2-flash, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-17 | `d703c086f` | RyeYuan | [BugFix] Fix the accuracy issues of DeepSeek-V4 in TP/CP/DP/EP | `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/allocator/paged.py` | deepseek-v4 |
| 2026-07-17 | `20828205d` | lizhigong | Merge pull request #103 from HYGON-AI/v0.5.12_dev_fabric_custom_all_reduce | 无直接文件变更/merge | unclassified |
| 2026-07-17 | `17f20798e` | lizhigong | Merge pull request #102 from HYGON-AI/v0.5.12_dev_chenyue_causal_conv1d | 无直接文件变更/merge | unclassified |
| 2026-07-17 | `7c22d53e3` | DCU CI Bot | ci(hcu): use local model assets and fix mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` 等 14 个文件 | glm5-glm51, kimi |
| 2026-07-17 | `e5a4e379b` | liucong8560 | Fix Qwen2.5-VL FA3 cu_seqlens | `python/sglang/srt/models/qwen2_5_vl.py` | qwen-vlm-omni-asr |
| 2026-07-17 | `3ac22ca84` | liucong8560 | Fix RMS quant residual update | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-20 | `cc0ab8f37` | liucong521 | Merge pull request #105 from HYGON-AI/v0.5.12_dev_bug | 无直接文件变更/merge | unclassified |
| 2026-07-20 | `fe9f24924` | yaoht | fix: prevent PD Decode DP hang under enable-dp-attention | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 5 个文件 | shared |
| 2026-07-20 | `079275b81` | reverie-hub | ci: add local sensitive diff text gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` | shared |
| 2026-07-20 | `c43b06722` | tianlinyang77 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 372 个文件 | unclassified |
| 2026-07-20 | `1e2fec228` | tianlinyang77 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, glm45, glm46-glm47, hunyuan3-preview, mimo-v2-flash, minimax, mixtral-quark-int4fp8-moe, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-20 | `358a33714` | tianlinyang77 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-07-20 | `248bfe347` | lizhigong | Merge pull request #106 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-20 | `b1d4bf66c` | lizhigong | Merge pull request #104 from HYGON-AI/v0.5.12_dev_dsv4_pool | 无直接文件变更/merge | unclassified |
| 2026-07-20 | `0c44c350b` | yangwl | feat: enable dynamic batching for LTX-2 T2V | `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/sample/ltx_2.py` | shared |
| 2026-07-20 | `86575d776` | yangwl | fix: support tensor-parallel transformer loading | `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/server_args.py` | shared |
| 2026-07-20 | `6182c3e35` | yangwl | fix: handle non-contiguous LTX attention outputs | `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` | shared |
| 2026-07-20 | `235b13465` | wanly young | Merge pull request #107 from HYGON-AI/feat/ltx2-dynamic-batching-tp | 无直接文件变更/merge | unclassified |
| 2026-07-20 | `416bbd9b9` | reverie-hub | chore(hcu): complete platform wording cleanup | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `docs/internal/dcu-main-catchup-20260629-conflict-review.md` 等 28 个文件 | mixtral-quark-int4fp8-moe |
| 2026-07-20 | `81e3561ae` | LvJIA-RG | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-07-20 | `e47445d2f` | yaoht | chore: clean leftover patch labels in PD Decode DP sync | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 5 个文件 | shared |
| 2026-07-20 | `811aa027d` | reverie-hub | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` | shared |
| 2026-07-20 | `5ac1f2418` | Lvjiajia | Add GitHub Actions workflow for quality gate | `.github/workflows/pr-quality-gate.yml` | shared |
| 2026-07-20 | `5543eb3df` | Lvjiajia | Rename quality-gate workflow and update triggers | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-20 | `e19d341ab` | Lvjiajia | Refactor quality gate workflow and update triggers | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-20 | `15a656ea6` | tianlinyang77 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` | shared |
| 2026-07-21 | `14da9b10e` | Lvjiajia | Update workflow reference in quality-gate.yml | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-21 | `e7ab05411` | Lvjiajia | Delete .github/workflows/pr-quality-gate.yml | `.github/workflows/pr-quality-gate.yml` | shared |
| 2026-07-21 | `c1f3f08c8` | Lvjiajia | Update workflow reference to a new commit | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-21 | `e876bb9ff` | RyeYuan | [FEAT] support cp+MegaMoE in prefill w/o cuda-graph | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 5 个文件 | deepseek-v4 |
| 2026-07-21 | `470ae85b5` | RyeYuan | style: apply pre-commit formatting (black/isort/ruff) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` 等 4 个文件 | deepseek-v4 |
| 2026-07-21 | `2d509d387` | lizhigong | Merge pull request #113 from HYGON-AI/v0.5.15.post1_dev_rye_megamoe_cp | 无直接文件变更/merge | unclassified |
| 2026-07-21 | `5dd9ba2f2` | lizhigong | Merge pull request #108 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-21 | `9864c8451` | reverie-hub | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` | shared |
| 2026-07-21 | `4859ed3b8` | RyeYuan | Merge official main daily 20260721 | 无直接文件变更/merge | unclassified |
| 2026-07-21 | `9b86479ac` | tianlinyang77 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` 等 14 个文件 | qwen35, qwen36 |
| 2026-07-21 | `53a455444` | dddddddxl | test: tune selected HCU accuracy thresholds | `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` | mimo-v2-flash |
| 2026-07-21 | `ac56ca009` | reverie-hub | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-21 | `a596be0dc` | RyeYuan | [BugFix] Fix DeepSeek-V4 pure-TP startup after official main daily 20260721 merge | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/utils/compile.py` 等 7 个文件 | deepseek-v4 |
| 2026-07-21 | `b4604b61f` | tianlinyang77 | ci(hcu): notify Feishu with accuracy results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py` 等 13 个文件 | deepseek-v32, glm5-glm51, kimi, mimo-v2-flash, minimax, qwen35 |
| 2026-07-21 | `7b6a9dd89` | lijing | 修复DeepseekV4精度问题 | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-07-22 | `e20e686c7` | tianlinyang77 | merge: sync v0.5.15.post1_dev into HCU port | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `f0d6741cc` | RyeYuan | merge(dcu): forward-port v0.5.12_dev daily 20260722 | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `6e5326678` | lizhigong | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-22 | `c32209f6d` | lizhigong | Merge pull request #115 from HYGON-AI/v0.5.15_dev_lzg | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `549cacab3` | tianlinyang77 | ci(hcu): isolate accuracy servers and share results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_server_guard.py` 等 11 个文件 | kimi |
| 2026-07-22 | `1f3d470dc` | RyeYuan | merge(dcu): integrate origin/v0.5.15.post1_dev PR#115 into forward-port 20260722 | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `c34b8da18` | LvJIA-RG | Resolve HCU rename merge conflicts | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `f5ad08f5b` | luoyao | [feat]:将lmslim算子调用切换到lightop调用. | `README_DCU.md`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` 等 16 个文件 | minimax |
| 2026-07-22 | `9fc04a7a2` | RyeYuan | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` | shared |
| 2026-07-22 | `1c40e365c` | sunjf | support mla lightop | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-07-22 | `af89ecd85` | LvJIA-RG | test: remove unstable MiMo HCU coverage and restore EAGLE | `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` 等 11 个文件 | kimi, mimo-v2-flash |
| 2026-07-22 | `5673a3972` | tianlinyang77 | ci(hcu): finalize nightly pre-merge safeguards | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py` 等 6 个文件 | shared |
| 2026-07-22 | `7941e0419` | yaoht | fix: enable HiCache layout_dcu for hybrid Mamba and EAGLE draft | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` | shared |
| 2026-07-22 | `7f488ac95` | lizhigong | Merge pull request #116 from HYGON-AI/v0.5.12_dev_mla_lightop | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `73c7e6c8f` | luoyao | [feat]:迁移lightop调用方式到新的接口. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 38 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, hunyuan3-preview, mimo-v2-flash, minimax, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-22 | `124cb938b` | lizhigong | Merge pull request #119 from HYGON-AI/0713-hcu-sglang-test | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `4783c39c6` | lizhigong | Merge pull request #118 from HYGON-AI/fix-dpskv4 | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `f391712f7` | LvJIA-RG | fix(hcu): use HCU guard for MLA KV cache storage | `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-07-22 | `0b46ed36d` | maxiaobetter | fix: apply bias after HCU DeepGEMM FP8 linear | `python/sglang/srt/layers/quantization/fp8_utils.py` | shared |
| 2026-07-22 | `b1606885e` | Lvjiajia | Fix help text for custom all-reduce backend | `python/sglang/srt/server_args.py` | shared |
| 2026-07-22 | `aa2309e22` | Lv Jiajia | chore(compliance): add HYGON headers and provenance | `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py` 等 169 个文件 | unclassified |
| 2026-07-22 | `421a13a80` | tianlinyang77 | ci(hcu): enable accuracy notification on default branch | `.github/workflows/nightly-test-hcu.yml` | shared |
| 2026-07-22 | `8b38b9a25` | Lvjiajia | Update comment for all_gather usage in scheduler | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` | shared |
| 2026-07-22 | `d8df1885d` | lizhigong | Merge pull request #117 from HYGON-AI/v0.5.12_dev_yaoht_hicache | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `4459f2e56` | lizhigong | Merge pull request #121 from HYGON-AI/fix/open-source-compliance-20260722-latest | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `ddc07f769` | lizhigong | Merge pull request #120 from HYGON-AI/fix-hcu-deepgemm-fp8-linear-bias | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `83d2a2b4b` | lizhigong | fix(hcu): rename stale DCU HiCache identifiers | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` 等 4 个文件 | shared |
| 2026-07-23 | `599610198` | tianlinyang77 | merge: sync latest v0.5.15.post1_dev into HCU port | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `bee4b423f` | lizhigong | Merge pull request #114 from HYGON-AI/hcu/v0.5.15.post1-port | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `e338cca15` | tianlinyang77 | ci(hcu): improve accuracy card and fix VLM model path | `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-07-23 | `c3755b4d4` | yht183 | fix: make DP local control broadcast opt-in via env | `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py` 等 4 个文件 | shared |
| 2026-07-23 | `540368a7d` | lizhigong | Merge pull request #123 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-24 | `b781224d4` | LvJIA-RG | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 466 个文件 | unclassified |
| 2026-07-24 | `cb01580d4` | lizhigong | Merge pull request #124 from HYGON-AI/sanitize-hcu-runtime-log-audit-20260723 | 无直接文件变更/merge | unclassified |
| 2026-07-24 | `64d1765b4` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-24 | `6c1786bc4` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-24 | `ca9b264a2` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-24 | `7482123c3` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-24 | `f76d2cea3` | Lvjiajia | Delete .github/workflows/quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` | shared |
| 2026-07-24 | `eb6a34093` | Lvjiajia | Update workflow reference to latest commit | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-24 | `9a8b1bd08` | Lvjiajia | Update quality gate workflow reference to new commit | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-24 | `2c21b95e6` | LvJIA-RG | fix(ci): align Feishu accuracy table | `.github/workflows/hcu-feishu-notify-preview.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-07-24 | `6ac12c2e5` | LvJIA-RG | ci: decouple Feishu preview from HCU runners | `.github/workflows/hcu-feishu-notify-preview.yml` | shared |
| 2026-07-24 | `65b7c4268` | LvJIA-RG | ci: use shared runner for Feishu preview | `.github/workflows/hcu-feishu-notify-preview.yml` | shared |
| 2026-07-24 | `4af810205` | LvJIA-RG | fix(ci): use card v2 metadata component | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-07-24 | `9e13c77ce` | LvJIA-RG | fix(ci): use card v2 link button | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-07-24 | `88d4501a3` | Lvjiajia | Update quality gate workflow reference | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-24 | `b746203e5` | LvJIA-RG | fix(hcu): use NSA attention for GLM-5.1 | `python/sglang/test/hcu_cookbook_utils.py` | glm5-glm51 |
| 2026-07-24 | `a3efe5e53` | luoyao | [bugfix]:修复lightop_per_token_quant_fp8调用前tensor准备. | `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/mem_cache/allocator.py` | shared |
| 2026-07-25 | `0acecf398` | luoyao | Merge branch 'v0.5.12_dev_lightop_ly' into v0.5.12_dev | 无直接文件变更/merge | unclassified |
| 2026-07-27 | `38c750157` | luoyao | fix：修复接口改动. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 21 个文件 | deepseek-v3-r1, deepseek-v32, deepseek-v4, hunyuan3-preview, mimo-v2-flash, minimax, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-27 | `afac89e0e` | yht183 | feat(hcu): add KME W8A8 hipBLASLt path via METHODS=3 | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | shared |
| 2026-07-27 | `87e383180` | luoyao | fix: 移除旧的lmslim导入方式. | `python/sglang/srt/layers/quantization/fp8_utils.py` | shared |
| 2026-07-27 | `163a92c14` | luoyao | fix(hcu):修改lightop的算子接口. | `python/sglang/srt/layers/activation.py`, `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-07-27 | `93c56ce71` | Lvjiajia | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-27 | `49764eb37` | Lvjiajia | Merge pull request #131 from HYGON-AI/lvjia-repoguy-patch-1 | 无直接文件变更/merge | unclassified |
| 2026-07-27 | `0710e82a0` | Lvjiajia | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-28 | `f3f52d4ca` | lizhigong | Merge pull request #129 from HYGON-AI/v0.5.12_dev_lightop | 无直接文件变更/merge | unclassified |
| 2026-07-28 | `42908ff67` | lizhigong | Merge pull request #130 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | 无直接文件变更/merge | unclassified |
| 2026-07-28 | `0e2459739` | JaneEyreliu | fix: pass quant_config to Qwen3Moe gate router, fix qwen3-coder accuracy issue | `python/sglang/srt/models/qwen3_moe.py` | qwen3-coder, qwen3-core |
| 2026-07-28 | `b5a1e8729` | lizhigong | Merge pull request #133 from HYGON-AI/v0.5.12_dev_qwen3_coder | 无直接文件变更/merge | qwen3-coder, qwen3-core |
| 2026-07-28 | `8f848be4e` | LvJIA-RG | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-07-28 | `77939d9a5` | LvJIA-RG | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-07-28 | `997e64560` | LvJIA-RG | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-07-28 | `864b3413b` | chaoyujiang | support dpsk-v4-int8 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 4 个文件 | deepseek-v4 |
| 2026-07-28 | `9a4f82911` | chaoyujiang | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-07-28 | `0305c5a3b` | chaoyujiang | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-07-28 | `4b90fd644` | LvJIA-RG | ci(hcu): add MiniMax-M2.7 two-node PD smoke | `.github/workflows/hcu-pd-1p1d.yml`, `python/sglang/test/hcu_pd_utils.py`, `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh` 等 10 个文件 | minimax |
| 2026-07-28 | `cd4802bba` | chaoyujiang | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` | shared |
| 2026-07-28 | `4aa6d4552` | lizhigong | Merge pull request #134 from HYGON-AI/dpsk-v4-int8-new-2 | 无直接文件变更/merge | unclassified |
| 2026-07-28 | `fc0bc51c7` | LvJIA-RG | chore(compliance): normalize Hygon source headers | `python/sglang/test/hcu_pd_utils.py`, `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`, `scripts/ci/hcu/hcu_ci_pd.py` 等 8 个文件 | minimax |
| 2026-07-28 | `d0c472989` | tianlinyang77 | ci: add HCU PD disaggregation smoke tests | `test/registered/hcu/disaggregation/pd_hcu_utils.py`, `test/registered/hcu/disaggregation/test_pd_basic_hcu.py`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py` 等 6 个文件 | shared |
| 2026-07-28 | `7b89bf661` | chaoyujiang | fix: propagate return_hidden_states_before_norm flag for mHC target-verify | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` | shared |
| 2026-07-28 | `fc59c96c5` | chaoyujiang | fix lint: format line breaks and remove trailing whitespace | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` | shared |
| 2026-07-28 | `1bd7b4664` | lizhigong | Merge pull request #138 from HYGON-AI/dpsk-int8-mtp | 无直接文件变更/merge | unclassified |
| 2026-07-28 | `0e4cd0bd8` | maxiaobetter | fix(pp): propagate NSA topk indices across stages | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py` 等 5 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-28 | `035ca766f` | maxiaobetter | fix(cache): forward Mamba indices in NSA offload | `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-07-29 | `bfa4011ad` | LvJIA-RG | ci(hcu): share wheel staging across runners | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 | shared |
| 2026-07-29 | `92e95e3f5` | liucong | perf(mamba): flatten fused state scatter launch grid | `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py` | shared |
| 2026-07-29 | `ac04c9cb4` | dddddddxl | Merge pull request #139 from HYGON-AI/0729-hcu-wheel-shared-staging | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `24201e257` | yht183 | fix(hy3): apply router_scaling_factor when not fused into topk | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-29 | `ba31df0c0` | RyeYuan | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` 等 1924 个文件 | unclassified |
| 2026-07-29 | `049f5e15e` | whlwhlwhl | [bugfix] 透传apply_routed_scaling_factor_on_output，防止moe_sum多乘routed_scaling_factor | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-07-29 | `6e7a53e86` | maxiaobetter | fix(hcu): select hipblaslt w8a8 layout by gfx arch | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | shared |
| 2026-07-29 | `47ebe8038` | maxiaobetter | fix(hcu): adapt NSA MQA calls to LightOp API | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-07-29 | `4e5a95fcb` | maxiaobetter | fix(pd): transfer MTP NSA topk seed metadata over Mooncake | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py` 等 9 个文件 | shared |
| 2026-07-29 | `573ad577c` | maxiaobetter | fix(nsa): share allocator-independent MTP topk indices | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py` 等 15 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-29 | `d39d628ef` | maxiaobetter | fix(hcu): enable NSA draft-extend cuda graph | `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-07-29 | `58d475775` | maxiaobetter | fix(hcu): allow single-node context parallel tp16 | `python/sglang/srt/server_args.py` | shared |
| 2026-07-29 | `0b6f8212c` | maxiaobetter | fix(ci): satisfy HCU lint checks | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 22 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-29 | `d42b0a3bf` | RyeYuan | merge(hcu): forward-port v0.5.12_dev daily 20260729 | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `3b4327cd7` | RyeYuan | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` | shared |
| 2026-07-29 | `e18e6b94b` | RyeYuan | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-29 | `277d9c6f5` | lizhigong | Merge pull request #140 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `7723b0d62` | maxiaobetter | fix(nsa): localize PD MTP logical topk indices | `python/sglang/srt/layers/attention/nsa/transform_index.py`, `python/sglang/srt/layers/attention/nsa_backend.py` | deepseek-v3-r1, deepseek-v32 |
| 2026-07-29 | `25ffedc22` | RyeYuan | fix(hcu): repair forward-port compatibility gaps | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` 等 15 个文件 | deepseek-v4, qwen3-core |
| 2026-07-29 | `6a031254f` | LvJIA-RG | ci(hcu): isolate nightly services and shared results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-07-29 | `be81ab419` | yht183 | fix(dp): demote DP Decode StepInfo log to debug | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` | shared |
| 2026-07-29 | `b2f0b830c` | LvJIA-RG | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 39 个文件 | shared |
| 2026-07-29 | `111fea82f` | LvJIA-RG | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 36 个文件 | shared |
| 2026-07-29 | `3bd903cb2` | dddddddxl | Merge pull request #147 from HYGON-AI/ci/align-workflows-main-0729 | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `cce4bdd61` | dddddddxl | Merge pull request #148 from HYGON-AI/ci/align-workflows-v0515-0729 | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `956b15538` | lizhigong | Merge pull request #145 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-29 | `fde49599a` | lizhigong | Merge pull request #144 from HYGON-AI/moe_fuse_gate_bug_fix | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `ec651411a` | lizhigong | Merge pull request #143 from HYGON-AI/v0.5.12_dev_lc | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `ed331a148` | lizhigong | Merge pull request #141 from HYGON-AI/v0.5.12_dev_maxiao | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `3c4581ece` | dddddddxl | Merge pull request #135 from HYGON-AI/hcu/minimax-m27-pd-ci | 无直接文件变更/merge | minimax |
| 2026-07-29 | `84bfd45c4` | shangxl | 修复hicache+pp并行 stage不一致问题 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py` 等 4 个文件 | shared |
| 2026-07-30 | `b97abbd58` | maxiaobetter | fix(hcu): avoid duplicate GLM4 MoE scaling | `python/sglang/srt/models/glm4_moe.py` | glm45, glm46-glm47 |
| 2026-07-30 | `716cb09f8` | yht183 | fix(hy3): always post-multiply rsf when not fused into topk | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-07-30 | `b8389e5c5` | LvJIA-RG | test(hcu): register PD helper for nightly collection | `test/registered/hcu/disaggregation/pd_hcu_utils.py` | shared |
| 2026-07-30 | `7a7108c96` | lizhigong | Merge pull request #150 from HYGON-AI/v0.5.12_dev_glm47_fix | 无直接文件变更/merge | glm46-glm47 |
| 2026-07-30 | `1a5a9521a` | lizhigong | Merge pull request #151 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | 无直接文件变更/merge | unclassified |
| 2026-07-30 | `6ea38ee52` | LvJIA-RG | style(hcu): format PD helper registration | `test/registered/hcu/disaggregation/pd_hcu_utils.py` | shared |
| 2026-07-30 | `6e096f24a` | yangyinan | 适配minimax-mtp和w4a8-trtion | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 7 个文件 | minimax |
| 2026-07-30 | `57330da70` | yangyinan | Merge branch 'minimax-mtp' into Minimax_mtp | 无直接文件变更/merge | minimax |
| 2026-07-30 | `489170e5c` | yangyinan | [FIX] 修复moe_w8a8重排函数删除问题 | `python/sglang/srt/layers/moe/moe_runner/lightop.py` | shared |
| 2026-07-30 | `17cf690af` | lizhigong | style: fix HCU lint checks | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 4 个文件 | shared |
| 2026-07-30 | `c55d12dc1` | lizhigong | Merge pull request #152 from HYGON-AI/Minimax_mtp | 无直接文件变更/merge | minimax |
| 2026-07-31 | `02968a96d` | RyeYuan | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 | shared |
| 2026-07-31 | `123e9539e` | RyeYuan | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, hunyuan3-preview, mimo-v2-flash, minimax, mixtral-quark-int4fp8-moe, qwen-vlm-omni-asr, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-31 | `39d691220` | RyeYuan | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` | shared |
| 2026-07-31 | `f6603bbe5` | chenyuege | [fix] Fixed accuracy issue caused by aiter‑moe in Qwen3.6‑35B‑A3B‑W8A8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py` | qwen3-coder, qwen3-core, qwen36 |
| 2026-07-31 | `83f43b3f4` | chenyuege | [CI] Fix some CI errors | `python/sglang/srt/layers/moe/moe_runner/aiter.py` | shared |
| 2026-07-31 | `603b95cea` | lizhigong | Merge pull request #137 from HYGON-AI/ci/hcu-pd-smoke-v0.5.12 | 无直接文件变更/merge | unclassified |
| 2026-07-31 | `dc015a0bc` | liucong521 | [PD] When PP is greater than 1, fix the request rollback when the KV cache is exhausted | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 11 个文件 | shared |
| 2026-07-31 | `497c35457` | chaoyujiang | fix(scheduler): abort too-large requests instead of dead-looping | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` | shared |
| 2026-07-31 | `b48994210` | dingxinlong | ci: install PyYAML for slash command handler (#156) | `.github/workflows/slash-command-handler.yml` | shared |
| 2026-07-31 | `e7106de94` | RyeYuan | V0.5.15.post1 dev to support dspark on HCU (#142) | `python/sglang/benchmark/dspark_sps_profiler.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py` 等 8 个文件 | deepseek-v4 |
| 2026-07-31 | `6b778d9ae` | liucong521 | [Router] Add Anthropic Messages thinking support | `sgl-model-gateway/src/middleware.rs`, `sgl-model-gateway/src/routers/anthropic.rs`, `sgl-model-gateway/src/routers/mod.rs` 等 4 个文件 | unclassified |
| 2026-07-31 | `f7161d452` | liucong | Merge branch 'v0.5.12_dev' of https://github.com/HYGON-AI/sglang-das into v0.5.12_dev_kimi27 | 无直接文件变更/merge | kimi |
| 2026-07-31 | `f556d3896` | yangyn | [FIX] 修复lmslim和lightop接口冲突问题 (#154) | `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | shared |
| 2026-07-31 | `0ff7a014f` | LvJIA-RG | ci(hcu): support resending Feishu accuracy results | `.github/workflows/hcu-feishu-notify-preview.yml` | shared |
| 2026-07-31 | `9c69436ee` | LvJIA-RG | fix(hcu): remove resend tool dependencies | `.github/workflows/hcu-feishu-notify-preview.yml` | shared |
| 2026-07-31 | `85dcec947` | LvJIA-RG | fix(hcu): support Python 3.8 in Feishu notifier | `scripts/ci/hcu/hcu_ci_notify_feishu.py` | shared |
| 2026-08-01 | `f4054ca15` | lizhigong | Merge pull request #153 from HYGON-AI/v0.5.12_dev_chenyue_moe_c | 无直接文件变更/merge | unclassified |
| 2026-08-01 | `ca730a059` | lizhigong | Merge pull request #157 from HYGON-AI/v0.5.12_dev_kimi27 | 无直接文件变更/merge | kimi |
| 2026-08-01 | `3eb90b8a6` | lizhigong | Merge pull request #155 from HYGON-AI/longprompt-deadloop-fix | 无直接文件变更/merge | unclassified |
| 2026-08-02 | `c5c5cc227` | lijing | [Opt]Optimize DSV4 C128 state pool with request-scoped allocation | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/dsv4/c128_cleanup.py` 等 20 个文件 | deepseek-v4 |
| 2026-08-03 | `67ecec8dd` | LvJIA-RG | fix(hcu): scope Feishu status to accuracy results | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | shared |
| 2026-08-03 | `ff7f44b8e` | Lvjiajia | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `286612da4` | Lvjiajia | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `d08093cb4` | Lvjiajia | Merge pull request #158 from HYGON-AI/lvj-repox-patch-1 | 无直接文件变更/merge | unclassified |
| 2026-08-03 | `4d3aaf6af` | Lvjiajia | Update quality gate workflow for versioning and concurrency | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `5fafd197c` | dingxinlong | Merge pull request #159 from HYGON-AI/fix/hcu-feishu-accuracy-status | 无直接文件变更/merge | unclassified |
| 2026-08-03 | `3358846e5` | Lvjiajia | Update quality-gate.yml | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `e6c410259` | Lvjiajia | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `de696eab9` | Lvjiajia | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `9a2b01399` | chaoyujiang | fix assert when mtp enable and step >1 | `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | deepseek-v4 |
| 2026-08-03 | `015f6d49a` | RyeYuan | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` | shared |
| 2026-08-03 | `b97d7df6e` | RyeYuan | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` 等 184 个文件 | unclassified |
| 2026-08-03 | `143ee9287` | yht183 | refactor(hcu): route KME W8A8 hipBLASLt through lightop | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | shared |
| 2026-08-04 | `cd60b7433` | xinleishang | 修改hicache+pp并行 stage不一致问题commit提交格式 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` | shared |
| 2026-08-04 | `8bb597e2c` | RyeYuan | Merge commit 'd703c086ff42655c602b85c9f0ac935215f8c4cc' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `2ceaca5ef` | RyeYuan | Merge commit '2d509d387218fb0e71ca4880cba8c56570316ab3' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `050d160da` | RyeYuan | Merge commit 'f0d6741cc1fc14ad8d74a12777345d23ec8ed7fc' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `4315f50a0` | RyeYuan | Merge commit '1f3d470dc5ff3365a87ae317ea12ef341335fffe' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `9c451b2d2` | RyeYuan | Merge commit '9fc04a7a2cebc525a96301d3e8e9515bb0a5b4b6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `7ac99d59b` | RyeYuan | Merge commit 'c43b06722' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `1462076bb` | RyeYuan | Merge commit '1e2fec228' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `de2659dc6` | RyeYuan | Merge commit '358a33714' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `bb91d55c7` | RyeYuan | Merge commit '416bbd9b9' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `515526331` | RyeYuan | Merge commit '81e3561ae' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `0792d89a9` | RyeYuan | Merge commit '811aa027d' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `235a6b991` | RyeYuan | Merge commit '15a656ea6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `b2e118b59` | RyeYuan | Merge commit '9864c8451' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `a822ab35c` | RyeYuan | Merge commit '9b86479ac' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `8bb3f9ecb` | RyeYuan | Merge commit 'ac56ca009' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `d91d2c7d7` | RyeYuan | Merge commit 'bee4b423f68fa27792f5d8ed79eb9ecbb5e0f4e6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `f628e2a98` | RyeYuan | Merge commit '7482123c3' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `128f5f73b` | RyeYuan | Merge commit '0710e82a0' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `fc4bd96f4` | RyeYuan | Merge commit '997e64560' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `19889fe0e` | RyeYuan | Merge commit 'cce4bdd61' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `e1ad3a989` | RyeYuan | Merge commit 'e7106de94' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `9e305f571` | RyeYuan | Merge commit 'd08093cb4' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `74d439192` | RyeYuan | Merge commit 'de696eab9' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `9dda7e375` | RyeYuan | Merge commit 'b97d7df6e' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-04 | `083d1d8b9` | RyeYuan | fix(hcu): restore DeepGEMM PD helper and current cache API | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-08-04 | `e8298ba90` | RyeYuan | fix(hcu): restore DP decode protocol constants | `python/sglang/srt/managers/scheduler_components/dp_attn.py` | shared |
| 2026-08-04 | `a1dd37d22` | chaoyujiang | fix: resolve lint errors (isort, ruff F821, trailing-whitespace, black) | `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | deepseek-v4 |
| 2026-08-04 | `ff6161f88` | chaoyujiang | Abort requests that exceed KV cache pool capacity with detailed 413 error Fix --swa-full-tokens-ratio 0.8 invalid | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py` | deepseek-v4 |
| 2026-08-04 | `618f17ede` | chaoyujiang | fix: resolve lint errors (ruff unused import, black formatting) | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/managers/scheduler.py` | deepseek-v4 |
| 2026-08-04 | `43d8d9ac1` | lizhigong | style(hcu): fix lint for KME W8A8 lightop path | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | shared |
| 2026-08-04 | `8160ebe53` | RyeYuan | fix(hcu): retain PD decode adapter callbacks | `python/sglang/srt/managers/scheduler_components/dp_attn.py` | shared |
| 2026-08-05 | `bba6b88d3` | lizhigong | Merge pull request #160 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `6d85dc772` | lizhigong | Merge pull request #161 from HYGON-AI/v0.5.12_dev_sxl | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `2a342cdf1` | sunjf | fix fp8 bug of triton | `python/sglang/srt/layers/attention/triton_ops/decode_attention.py` | shared |
| 2026-08-05 | `d20f0063d` | lizhigong | Merge pull request #165 from HYGON-AI/v0.5.12_dev_triton_fp8_bug_fix | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `6742d20c8` | lijing | Fix lint for request-scoped C128 state pool | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` 等 11 个文件 | deepseek-v4 |
| 2026-08-05 | `71de6dd93` | LvJIA-RG | fix(ci): align HCU gateway wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-08-05 | `2fb37eaac` | LvJIA-RG | fix(ci): align HCU Python wheel paths | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-08-05 | `44bb481cf` | liucong | fix(eplb): apply expert ID remapping for HCU fused TopK | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-08-05 | `dabae6b13` | LvJIA-RG | fix(ci): use PR files API for HCU wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-08-05 | `54d01422a` | lizhigong | Merge pull request #163 from HYGON-AI/fix-dpsk-mtp-assert | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `f320ce265` | lizhigong | Merge pull request #164 from HYGON-AI/longprompt-deadloop-fix | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `20ba56a96` | lizhigong | Merge pull request #166 from HYGON-AI/v0.5.12_dev_opt_c128_state_pool | 无直接文件变更/merge | unclassified |
| 2026-08-05 | `a0840f493` | RyeYuan | [BugFix] recall hcu changes in pre_mhc changes to fix the accuracy issues | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-08-06 | `799aaa455` | lizhigong | Merge pull request #168 from HYGON-AI/v0.5.12_dev_qwen3.5_eplb | 无直接文件变更/merge | qwen3-coder, qwen3-core, qwen35 |
| 2026-08-06 | `b1b81c18f` | lizhigong | Merge pull request #169 from HYGON-AI/fix/hcu-wheel-gateway-classification | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `1672d9e47` | lizhigong | Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `b91477f29` | RyeYuan | chore(hcu): anchor forward-port base to ac04c9cb (no content change) | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `4da105483` | RyeYuan | merge(hcu): forward-port v0.5.12_dev daily 20260806 (ac04c9cb..b1b81c18f) | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `3d0f94345` | RyeYuan | fix(hcu): fully revert files owned by the skipped source commits | `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py` 等 20 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-08-06 | `f1c6f5631` | RyeYuan | fix(hcu): drop leftover source hunks that renaming and partial takes left behind | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` | shared |
| 2026-08-06 | `725659198` | RyeYuan | Revert "fix assert when mtp enable and step >1" | `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | deepseek-v4 |
| 2026-08-06 | `8e2aba4bf` | RyeYuan | fix lint: apply isort/black to forward-port diff | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 5 个文件 | shared |
| 2026-08-06 | `f17440f19` | RyeYuan | fix(hcu): restore original license headers dropped by the forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py` | shared |
| 2026-08-06 | `e47388196` | RyeYuan | ci: migrate legacy CUDA suite= registrations to stage=/runner_config= | `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py` 等 44 个文件 | gpt-oss, nemotron-super, qwen3-next |
| 2026-08-06 | `b0f2bb3a8` | RyeYuan | fix(hcu): restore network_mode matrix keys dropped by the forward-port | `.github/workflows/nightly-test-hcu.yml` | shared |
| 2026-08-06 | `34b6864a2` | lizhigong | Merge pull request #173 from HYGON-AI/forward-port/v0.5.12-dev-daily-20260806 | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `5d0386fd4` | LvJIA-RG | ci(hcu): expand functional and numerical coverage | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` 等 16 个文件 | qwen36 |
| 2026-08-07 | `4d9f46783` | RyeYuan | [BugFix] fix the lmslim and lightop calling issues regressions | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 6 个文件 | minimax |
| 2026-08-07 | `154a88c7b` | RyeYuan | fix lint: apply isort/black to the lmslim->lightop migration | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` | shared |
| 2026-08-07 | `b59995e42` | RyeYuan | fix(hcu): point PD smoke tests at a declared HCU suite | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` | shared |
| 2026-08-07 | `eda349619` | RyeYuan | chore(hcu): anchor daily sync base to official edc0e5489 (no content change) | 无直接文件变更/merge | unclassified |
| 2026-08-07 | `654ff007e` | YuanYuan | [BugFix] fix the lmslim and lightop calling issues regressions (#176) | 无直接文件变更/merge | unclassified |
| 2026-08-07 | `b7bd14f19` | LvJIA-RG | ci(hcu): normalize HCU suite names | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 199 个文件 | unclassified |
| 2026-08-07 | `92ce544fa` | LvJIA-RG | ci: align v0.5.15 workflow triggers | `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml` 等 7 个文件 | shared |
| 2026-08-07 | `132b630bc` | LvJIA-RG | ci(hcu): harden server lifecycle and model mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` 等 5 个文件 | shared |
| 2026-08-07 | `4c7a264e5` | LvJIA-RG | ci(hcu): align model assets and selected-ref kernel | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` | shared |
| 2026-08-07 | `2b4271498` | LvJIA-RG | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` 等 11 个文件 | deepseek-v32, glm5-glm51, kimi, minimax, qwen35 |
| 2026-08-07 | `1a5ce1750` | LvJIA-RG | ci(hcu): publish reasoning results to shared storage | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`, `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py` | shared |
| 2026-08-07 | `50736ebe7` | LvJIA-RG | ci(hcu): keep migration changes scoped | `README_HCU.md` | shared |
| 2026-08-07 | `dc5cd7089` | LvJIA-RG | ci: finalize v0.5.15 workflow policy | `.github/workflows/ci-auto-bisect.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/slash-command-handler.yml` | shared |
| 2026-08-07 | `ecf4756ce` | LvJIA-RG | test(hcu): isolate server guard unit test | `scripts/ci/hcu/test_hcu_server_guard.py` | shared |
| 2026-08-07 | `76ced479e` | LvJIA-RG | test(hcu): use v0.5.15 FP8 kernel path | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` | shared |
| 2026-08-07 | `3fbc8ae9e` | LvJIA-RG | test(hcu): align numerical references with v0.5.15 | `test/registered/hcu/kernels/test_attention_reference_hcu.py`, `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py` | shared |
| 2026-08-07 | `b86a8dc74` | LvJIA-RG | test(hcu): bound backend smoke test setup | `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` | qwen36 |
| 2026-08-07 | `3de1323a9` | LvJIA-RG | ci(hcu): normalize rebased PD suite names | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` | shared |
| 2026-08-10 | `80e01615e` | RyeYuan | Sync/official main daily 20260807 | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `37b7742e7` | RyeYuan | Sync/official main 20260810 (v0.5.17) | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `d76d3f185` | yuchenyang | Adapt MiniMax-H3 for v0.5.15 | `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py` 等 84 个文件 | minimax |
| 2026-08-10 | `6f86e904d` | lizhigong | Merge pull request #179 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `abe7d784d` | lizhigong | Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt | 无直接文件变更/merge | minimax |
| 2026-08-10 | `e3a9d595c` | RyeYuan | [HCU][DSpark] Fix sampling parameter updates after graph capture | `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` | shared |
| 2026-08-10 | `4a6fbed98` | RyeYuan | [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config | `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-10 | `5fd89c728` | RyeYuan | [BugFix] fix the inference tensor graph replay issues in MTP mode | `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` | shared |
| 2026-08-10 | `b36730b41` | RyeYuan | fix lint: apply pre-commit fixes to the mHC EAGLE changes | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py` | shared |
| 2026-08-10 | `8f7a660e5` | YuanYuan | Merge pull request #183 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge | unclassified |
| 2026-08-11 | `ad1fea5d7` | dingxinlong | Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci | 无直接文件变更/merge | unclassified |
| 2026-08-11 | `ccbb65acb` | RyeYuan | [HCU][DSpark] Fix DP EP MoE fallback routing | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-12 | `5daa79af7` | RyeYuan | merge(hcu): forward-port v0.5.15.post1_dev through 20260811 | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `9b76db90d` | YuanYuan | Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811 | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `2083c069f` | RyeYuan | fix lint: apply pre-commit fixes to the EP MoE fallback change | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-12 | `856b425b8` | YuanYuan | Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `fb7f11956` | LvJIA-RG | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 | shared |
| 2026-08-12 | `74e12e1e8` | lizhigong | Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515 | 无直接文件变更/merge | unclassified |
| 2026-08-13 | `54e3ed50f` | RyeYuan | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` | shared |
| 2026-08-13 | `18e167b73` | RyeYuan | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` | shared |
| 2026-08-13 | `5e2ba659e` | RyeYuan | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` | shared |
| 2026-08-13 | `97a1938e2` | YuanYuan | Merge pull request #192 from HYGON-AI/rye_dspark_bugfix | 无直接文件变更/merge | unclassified |
| 2026-08-14 | `1c349c31f` | RyeYuan | merge(hcu): forward-port v0.5.15.post1_dev through 20260813 | 无直接文件变更/merge | unclassified |
| 2026-08-14 | `fa309a1e1` | RyeYuan | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | shared |
| 2026-08-17 | `d95af36e1` | YuanYuan | Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813 | 无直接文件变更/merge | unclassified |
| 2026-08-17 | `9f4368f10` | RyeYuan | merge(hcu): backport official main through 20260817 (92b1d382c7) | 无直接文件变更/merge | unclassified |
| 2026-08-17 | `9bbf3799d` | RyeYuan | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` | shared |
| 2026-08-17 | `d20a4750f` | YuanYuan | Merge pull request #208 from HYGON-AI/backport/official-main-20260817 | 无直接文件变更/merge | unclassified |
| 2026-08-18 | `b0dc28040` | dingxinlong | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` 等 9 个文件 | shared |
| 2026-08-20 | `62a07586d` | chenyuege | [feat] 适配HCU FA3 | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 5 个文件 | shared |
| 2026-08-20 | `fb7369fec` | chenyuege | [bugfix]删除无关文件 | `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942` | shared |
| 2026-08-20 | `b628d29e1` | zhangyh15 | [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-08-20 | `11d08002b` | chenyuege | [fix]solved CI Test errors | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 4 个文件 | shared |
| 2026-08-20 | `f6b66222a` | zhangyh15 | revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0 | `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-20 | `72d1d2a73` | chenyuege | [fix]solved other CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` | shared |
| 2026-08-20 | `27ce43c71` | chenyuege | [fix]solved CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` | shared |
| 2026-08-20 | `9ca1b25f7` | lizhigong | Merge pull request #210 from HYGON-AI/main_dev_qwen3.8 | 无直接文件变更/merge | qwen3-coder, qwen3-core |
| 2026-08-20 | `12c25ba52` | zhangpc3 | [fix][minimax-h3]: fix HCU QK-Norm fallback and backend resolution | `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` | minimax |
| 2026-08-20 | `56a4faa68` | zhangpc3 | [fix][minimax-h3]: default HCU component attention backends | `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py` | minimax |
| 2026-08-20 | `37c5b30bb` | zhangyh15 | fix: extract full DTK version for three-part versions | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` 等 4 个文件 | shared |
| 2026-08-21 | `a96aed11f` | zhuwenbopro | [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` | shared |
| 2026-08-21 | `2c0d45485` | reverie-hub | Sanitize HCU platform naming and runtime messages | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-daily-20260721-conflict-review.md`, `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md` 等 21 个文件 | mixtral-quark-int4fp8-moe |
| 2026-08-21 | `d42ecf6fe` | reverie-hub | Fix HCU detection and sanitized topology diagnostics | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt` | shared |
| 2026-08-24 | `0d49fbb93` | lizhigong | Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev | 无直接文件变更/merge | minimax |
| 2026-08-24 | `4a540f118` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `2e8f1408b` | lizhigong | Merge pull request #214 from Crowder13/main | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `7676961ba` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `261b8627f` | RyeYuan | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` | shared |
| 2026-08-24 | `fd4157047` | reverie-hub | Refine HCU platform diagnostics and CLI help | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py` | shared |
| 2026-08-25 | `16d7caa10` | RyeYuan | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 1857 个文件 | unclassified |
| 2026-08-25 | `dd41b1f06` | YuanYuan | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `c40703e6b` | RyeYuan | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` 等 5 个文件 | shared |
| 2026-08-25 | `7b3548f97` | RyeYuan | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` 等 48 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, qwen-vlm-omni-asr, qwen35 |
| 2026-08-25 | `d1adf7b50` | zhangyh15 | [feature] manual compile ci | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-25 | `59213c7e4` | RyeYuan | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` | shared |
| 2026-08-25 | `94e9fa4b1` | zhangyh15 | ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload) | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-25 | `69c73a178` | dddddddxl | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `97aa7a298` | Lvjiajia | Merge pull request #224 from dddddddxl/hcu/fork-pr-target | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `f2fc4e166` | Lvjiajia | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-25 | `4eacd3c36` | Lvjiajia | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `3e6aaf09d` | dddddddxl | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `8ba0c9376` | Lvjiajia | Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `7481b1f54` | Lvjiajia | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `a3cfa2a97` | Lvjiajia | Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `d445b357f` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `6a4a61efb` | dddddddxl | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `688659c15` | Lvjiajia | Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `990a1a798` | dddddddxl | ci: disable scheduled gateway nightly release | `.github/workflows/nightly-release-gateway.yml` | shared |
| 2026-08-26 | `8dd5daf2f` | reverie-hub | Refine HCU and AMD CLI help text | `python/sglang/srt/server_args.py`, `test/run_suite.py` | shared |
| 2026-08-26 | `c94c3ca2c` | zhangyh15 | fix: gateway wheel is at workspace root target/wheels | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-26 | `f6d701c52` | reverie-hub | Fix stale HCU Stage B test paths | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-08-26 | `a2de3b8cf` | dddddddxl | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `ed9037191` | Lvjiajia | Merge pull request #238 from dddddddxl/hcu/fix-bash-shell-main | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `c832752c7` | dddddddxl | Merge remote-tracking branch 'origin/main' into review/pr-230 | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `26c6e0fb3` | lizhigong | Merge pull request #230 from reverie-hub/hcu/sanitize-runtime | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `2866df994` | dddddddxl | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-27 | `a15b56677` | Crowder13 | Merge branch 'HYGON-AI:main' into main | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `fd402a780` | Lvjiajia | Merge pull request #246 from dddddddxl/hcu/fix-safe-directory-main | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `dc7b624e9` | Crowder13 | Merge branch 'HYGON-AI:main' into main | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `7609d9af6` | zhangyh15 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` | shared |
| 2026-08-27 | `6b468d012` | zhangyh15 | [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 | shared |
| 2026-08-28 | `68dcd498a` | zhangyh15 | [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-08-28 | `bc990ebd5` | zhangyh15 | [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复) | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-28 | `13c60ec0d` | lizhigong | Merge pull request #254 from Crowder13/main | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `5cf052bd0` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `20ee2b297` | lizhigong | Merge pull request #216 from Zhuwenbopro/feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `3ca61517d` | dddddddxl | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` | shared |
| 2026-08-31 | `cc6b7c948` | Lvjiajia | Merge pull request #269 from dddddddxl/hcu/remove-amd-pr-state-main | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `e864c3028` | dingxinlong | ci: enable HCU PR tests for release branches (#272) | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-09-01 | `50bacb028` | YuanYuan | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` 等 1435 个文件 | unclassified |
| 2026-09-01 | `8fa7122b3` | Crowder13 | [FEATURE]构建镜像之后触发模型测试 (#277) | `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml` | shared |
| 2026-09-02 | `9d261478d` | dingxinlong | [CI] Update HCU model asset paths on main (#285) | `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh` 等 10 个文件 | shared |
| 2026-09-02 | `6fe7ce909` | dingxinlong | ci(hcu): restore run suite file filters (#290) | `test/run_suite.py` | shared |
| 2026-09-03 | `2828bde71` | dingxinlong | ci(hcu): align llguidance and model asset paths (#299) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` | shared |
| 2026-09-03 | `d150cf2ac` | Crowder13 | [BUGFIX]torchaudio使用hcu的版本 (#298) | `docker/hcu.Dockerfile` | unclassified |
| 2026-09-04 | `0457572a1` | Crowder13 | [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308) | `.github/workflows/nightly-test-image-hcu.yml` | shared |
| 2026-09-07 | `df05aa9f9` | Crowder13 | [FEATURE] daily镜像里面加装ai-dynamo (#313) | `docker/hcu.Dockerfile` | unclassified |
| 2026-09-08 | `0af71f61b` | tianly | fix(ci): update HCU evaluation dependencies and asset paths (#325) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh` | shared |
| 2026-09-08 | `ee0f2375e` | YuanYuan | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` 等 3600 个文件 | unclassified |
| 2026-09-14 | `b5108cc7f` | dingxinlong | ci(hcu): use v0.5.18 image and restore eval dependencies (#347) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` 等 4 个文件 | shared |
| 2026-09-14 | `516261baf` | dingxinlong | ci(hcu): register sampling test and adjust MMLU threshold (#359) | `test/registered/sampling/test_pytorch_sampling_backend.py` | shared |
| 2026-09-14 | `575cf4797` | dingxinlong | ci(hcu): restore source mode for test-only PRs (#364) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` | shared |
| 2026-09-14 | `ca25bc427` | YuanYuan | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` 等 1792 个文件 | unclassified |
| 2026-09-15 | `7c8272a3a` | Crowder13 | [BUGFIX]更新AICC安装方式 (#367) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-09-15 | `ae14a99e5` | tianly | fix(ci): fix HCU wheel build target routing (#372) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-09-15 | `5c03a8e22` | Crowder13 | [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-09-16 | `adc1d69b2` | dingxinlong | ci(hcu): align main wheel builds with 0.5.18 runtime (#379) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 6 个文件 | shared |
| 2026-09-20 | `16229e94d` | YuanYuan | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` 等 1583 个文件 | unclassified |
| 2026-09-21 | `ae5c33991` | Lvjiajia | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` | shared |
| 2026-09-21 | `cb932f5fb` | 463975089 | feat(ci) compaity sgl-kernal main to v0.5.12 (#421) | `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-09-21 | `a981685e7` | 463975089 | fix release-pr-hcu.yml build sglang (#423) | `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-09-22 | `b5ca753bc` | dingxinlong | ci(hcu): run nightly against v0.5.18 and report its results (#432) | `.github/workflows/nightly-test-hcu.yml` | shared |
| 2026-09-23 | `2871c8fdd` | Crowder13 | ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-09-23 | `7be1324cf` | guochenyang | ci: report sglang nightly packages to DashHub (#424) | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-09-23 | `9cd15042a` | Crowder13 | feat(citest): 更新镜像测试用例, 适配 0.5.18 (Qwen3.8 / DeepSeek-V4) (#433) | `docker/image-citest-conf-hcu.yaml` | deepseek-v4, qwen3-coder, qwen3-core |
| 2026-09-23 | `f2d49c2c0` | JackPeng | FIX(DSV4): 补全 system/reminder 结尾对话的 assistant 生成前缀并解析 markdown 伪工具调用 (#435) | `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`, `python/sglang/srt/function_call/deepseekv4_detector.py`, `test/registered/unit/function_call/test_deepseekv4_detector.py` | deepseek-v4 |
| 2026-09-23 | `2f9a696ab` | Crowder13 | [FEATURE] 基础镜像内置 shca 驱动 (#440) | `docker/hcu.Dockerfile` | unclassified |
| 2026-09-23 | `88b0efdfe` | 463975089 | adapt ci to feat/20260920_deepseek-v4.1 (#442) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | deepseek-v4 |
| 2026-09-24 | `665b27d1f` | 463975089 | feat(ci) fix main build whl failed (#449) | `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-09-28 | `5e8269d55` | Crowder13 | [BUGFIX]镜像DTK版本号不对 (#447) | `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-09-28 | `6049c219e` | leon.wang | Glm5.3 flash (#427) | `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc` 等 196 个文件 | unclassified |
| 2026-09-29 | `ab43824b0` | YuanYuan | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` 等 2902 个文件 | unclassified |
| 2026-09-30 | `e05f146be` | dingxinlong | ci(hcu): migrate main workflows to organization runners (#463) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` 等 12 个文件 | shared |
| 2026-09-30 | `756ae5b4f` | YuanYuan | Sync/20260929 rye rel 2 main (#470) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 313 个文件 | unclassified |
| 2026-10-08 | `5cf6ed7f7` | Crowder13 | [BUGFIX]镜像增加安装megamoe (#479) | `docker/hcu.Dockerfile` | unclassified |
| 2026-10-09 | `fb46d17ad` | Lee156 | add optest process (#481) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-10-09 | `f0ee2a505` | JackPeng | FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473) | `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py` | shared |
| 2026-10-10 | `4205397cb` | Lee156 | add password-free download code (#499) | `.github/workflows/nightly-test-operator-hcu.yml` | shared |
| 2026-10-10 | `3b0e4a073` | 王启宇 | [Fix] Bound crash diagnostics and fatal shutdown on main (#498) | `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` 等 6 个文件 | shared |
| 2026-10-12 | `50b0d0051` | guochenyang | Delegate HCU model deployment smoke CI to external controller (#503) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-10-12 | `36b93840b` | YuanYuan | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` 等 3300 个文件 | unclassified |
| 2026-10-12 | `f9b972b37` | guochenyang | Use a clean checkout directory for the model smoke controller (#510) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-12 | `b6dd37e66` | gcy | Run cookbook smoke tests for all cases by default | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-12 | `e295faff5` | Lee156 | update ci name&&add optest log (#515) | `.github/workflows/nightly-test-operator-hcu.yml` | shared |
| 2026-10-14 | `78c700ee0` | guochenyang | Add image input to cookbook deployment smoke workflow (#530) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-15 | `cc3758967` | guochenyang | Pass DashHub credential to deployment smoke controller (#534) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-15 | `fc095e059` | chaoyujiang | fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533) | `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` 等 4 个文件 | shared |
| 2026-10-16 | `87b9d5c85` | guochenyang | Run cookbook deployment checks after HCU image publishing (#548) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-10-19 | `f89209aa8` | guochenyang | ci: pass package server to Cookbook model tests (#556) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-20 | `4975d6490` | YuanYuan | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` 等 3006 个文件 | unclassified |
| 2026-10-20 | `a8543c813` | guochenyang | [CI] cookbook: Add BW1000 deployment smoke tests (#570) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-21 | `5f67ce01c` | YuanYuan | Sync/rel 2 main 20261021 dsv4 validated (#576) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore` 等 321 个文件 | unclassified |
| 2026-10-26 | `15c7204b7` | YuanYuan | [Feat] [HCU] dsv4.1: Sync feature branch updates into main (#594) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `python/sglang/kernels/aot/benchmark/bench_rope_fp4.py` 等 139 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-10-28 | `6dac3481c` | guochenyang | [Fix] ci: Preserve model cases in DashHub operator reporting (#604) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-10-28 | `098f31d69` | 463975089 | fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-10-28 | `029b6e641` | guochenyang | [CI] model-ci: Pass history token for daily comparison report (#607) | `.github/workflows/cookbook-deployment-smoke.yml` | shared |
| 2026-10-28 | `fd98647ed` | guochenyang | [Fix] ci: Restore previous DashHub operator reporting (#614) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` | shared |
| 2026-10-29 | `25aa13e98` | 463975089 | fix(ci) rebase pr-test-hcu.yml (#617) | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-10-29 | `db479b030` | guochenyang | [CI] optest: Report outcome to DashHub (#619) | `.github/workflows/nightly-test-operator-hcu.yml` | shared |
| 2026-10-29 | `9fb319cc3` | guochenyang | [CI] optest: Require every enabled operator result (#622) | `.github/workflows/nightly-test-operator-hcu.yml` | shared |
| 2026-11-02 | `471ab8254` | guochenyang | Add one-time DashHub recovery for run 41338132822 (#633) | `.github/workflows/dashhub-recover-41338132822.yml` | shared |
| 2026-11-02 | `594e1ae94` | guochenyang | [Chore] ci: Remove completed DashHub recovery workflow (#634) | `.github/workflows/dashhub-recover-41338132822.yml` | shared |
| 2026-11-03 | `5343b311c` | YuanYuan | Feat/20261102 Sync latest deepseek-v4.1 optimizations to main (#640) | `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope_hcu.py` 等 93 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
