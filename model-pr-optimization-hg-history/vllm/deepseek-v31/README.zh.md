# vllm DeepSeek V3.1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `examples/online_serving/elastic_ep/serve_deepseek_v2.sh` | `41b6f9200` |
| `examples/tool_chat_template_deepseekv31.jinja` | 无直接提交 |
| `tests/tool_parsers/test_deepseekv31_tool_parser.py` | `ed586e772` |
| `vllm/model_executor/models/deepseek_mtp.py` | `aef3c4873`, `2888b4e5a`, `3bff7958e`, `6395b73e8`, `2ce72b9c2`, `96abd293f`, `df7041633`, `5fe035497`, `be6931ee2`, `dcd80206b`, `600aaab8d`, `482914849`, ... (21 total) |
| `vllm/model_executor/models/deepseek_v2.py` | `aef3c4873`, `a05d749ea`, `2888b4e5a`, `eb933fe15`, `0639678c5`, `168ceef7c`, `2350c778f`, `83c871fbe`, `58a365086`, `cb1a27d25`, `d71496bf0`, `afe3ea1ec`, ... (55 total) |
| `vllm/tool_parsers/deepseekv31_tool_parser.py` | `fefce4980`, `2a1776b7a` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 80
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-22 | `aef3c4873` | 性能/后端优化 | [Feature]添加PCP功能，只支持mla架构，CPLB待验证 | `vllm/config/parallel.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py` |
| 2026-04-08 | `a05d749ea` | 性能/后端优化 | [BUGFIX] rms_quant融合功能适配DSA | `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-03-28 | `2888b4e5a` | 性能/后端优化 | 优化VLLM_DISABLE_DSA的设置，加入envs中，默认关，开启可强制关闭dsa | `vllm/envs.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-03-19 | `eb933fe15` | 性能/后端优化 | feat(moe): 修复 shared_output 透传被覆盖并兼容 torch.compile 启动路径 移除 forward 中对 experts.use_overlapped/_shared_experts 的状态改写，避免 torch.compile 启动期 shared/non-shared 路径不一致 FusedMoE.forward_impl 仅在 shared_output 为空时计算 shared experts，防止透传值被本地重算覆盖 | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-03-18 | `0639678c5` | 性能/后端优化 | feat(moe): 增加 LightOP moe_sum+mul+add 融合并打通参数透传 新增环境变量 VLLM_USE_LIGHTOP_MOE_SUM_MUL_ADD 用于控制 fused sum+mul+add 开关。 在 DeepseekV2MoE 中增加 fused 路径，预计算 shared_output，并下传 iqis 与 routed_scaling_factor。 扩展 FusedMoE/SharedFusedMoE 及相关 custom op 接口，统一透传 i_q/i_s/shared_output/routed_scaling_factor。 同步适配 Triton、Marlin W16A16、SlimQuant W4A8、CompressedTensors W8A8 等实现，支持在内核侧完成 sum+mul+add。 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-03-18 | `3bff7958e` | 性能/后端优化 | x接入mla_cat算子仅在nmz和kvcache-fp8情况下生效，默认关闭，开启需要export VLLM_USE_CAT_MLA=1 | `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-03-17 | `6395b73e8` | 性能/后端优化 | feat:接入VLLM_USE_FUSED_FILL_RMS_CAT优化 | `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-03-16 | `2ce72b9c2` | 模型支持/运行时入口 | [feat]deepseek mtp支持pp模式 | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-12 | `168ceef7c` | 性能/后端优化 | perf: DS V2模型MOE部分增加rmsQuant | `vllm/attention/layer.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` |
| 2026-03-12 | `2350c778f` | 性能/后端优化 | perf: DS V2模型MLA中增加rmsQuant | `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-03-11 | `96abd293f` | 性能/后端优化 | dpsk_v32的mtp层的dense加载适配 | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/attention/ops/flashmla.py` |
| 2026-03-07 | `83c871fbe` | 性能/后端优化 | feat: support shared expert fusion. | `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py` |
| 2026-03-06 | `58a365086` | 性能/后端优化 | perf:Deepseek v2模型增加rmsQuant和siluMulQuant融合 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py` |
| 2026-03-05 | `cb1a27d25` | 缺陷修复 | 修复dsa的workspace的bug，以及添加环境变量关闭DSAVLLM_DISABLE_DSA=1 | `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-03-03 | `d71496bf0` | 性能/后端优化 | support dsa | `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-02 | `afe3ea1ec` | 性能/后端优化 | [Model] GLM adaptation | `benchmarks/kernels/benchmark_moe.py`, `tests/models/registry.py`, `tests/models/test_initialization.py` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-06 | `d7db129ab` | 性能/后端优化 | 修复awq/w4a16的triton支持，以及fuse_moe的接口对齐，以及awq_moe_marlin推理的相关bug，并解决awq/w4a16的精度问题 | `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/fused_marlin_moe_w4a16.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-02-04 | `5fe035497` | 性能/后端优化 | [perf] add VLLM_USE_FUSED_FILL_RMS_CAT to use lightop for dpsk mtp fill + rms*2 + cat | `vllm/envs.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-02-03 | `b31c72519` | 缺陷修复 | fix run error | `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-26 | `be6931ee2` | 性能/后端优化 | [ROCm][Bugfix] Fix ptpc scale load issue for fused shared expert path in deepseek mtp (#33018) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-21 | `6c20e89c0` | 性能/后端优化 | [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp (#29287) | `vllm/_aiter_ops.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-01-20 | `c4e5bdf61` | 缺陷修复 | [Bugfix] Fix the fp8_mqa_logits dim mismatch (#32652) | `vllm/model_executor/models/deepseek_v2.py`, `vllm/utils/deep_gemm.py` |
| 2026-01-16 | `5de6dd066` | 缺陷修复 | [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding (#32175) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-14 | `2c9b4cf5b` | 性能/后端优化 | [BugFix] Fix DeepSeek-V3.1 + DeepGEMM incompatible scale shapes (#32361) | `vllm/model_executor/layers/quantization/utils/quant_utils.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-07 | `8cfec41a0` | 性能/后端优化 | remove USE_FUSED_RMS_QUANT | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-07 | `60b37c6b9` | 性能/后端优化 | remove USE_FUSED_RMS_QUANT and USE_FUSED_SILU_MUL_QUANT | `vllm/envs.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py` |
| 2026-01-07 | `c964b9ad2` | 调度/缓存/PD | skip indexer_k_cache | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-06 | `4ec647327` | 性能/后端优化 | add indexer_k_cache_kernel | `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp` |
| 2026-01-06 | `25ec6a347` | 调度/缓存/PD | update mqa_logits and paged_mqa_logits | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-24 | `b41aeb346` | 性能/后端优化 | [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-23 | `76e6a9519` | 缺陷修复 | [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2 (#31160) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-19 | `4cf942989` | 缺陷修复 | [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2 (#31046) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-19 | `22c6c645c` | 性能/后端优化 | fix moe params and run error | `vllm/attention/ops/flashmla.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2025-12-18 | `41b6f9200` | 性能/后端优化 | Remove all2all backend envvar (#30363) | `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml` |
| 2025-12-18 | `d2fe5111f` | 性能/后端优化 | fix optional and profling | `vllm/compilation/decorators.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-18 | `b166ef20e` | 缺陷修复 | [refactor] Add prefix support to embed_tokens in DeepSeek MTP (#30788) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-17 | `84896fda2` | 缺陷修复 | [Bugfix] deepseek-V3.2 self.weights_proj has no bias (#30841) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-17 | `b66c8e4b2` | 性能/后端优化 | Synchronize the modifications from the 12th to the 17th: 修复CompressedTensorsLinearMethod中的w4a16的冲突问题 feat(moe): add Marlin W16A16 fused MoE behind VLLM_USE_MARLIN_W16A16_MOE replace the fp8_mqa_logits and fp8_paged_mqa_logits interfaces in deepgemm with mqa_logits and paged_mqa_logits from lightop | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`, `vllm/model_executor/layers/fused_moe/marlin_quant.py` |
| 2025-12-16 | `10ee1c64c` | 性能/后端优化 | [CI] Generalize gsm8k test args and add Qwen3-Next MTP B200 test (#30723) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-12 | `3e41992fe` | 性能/后端优化 | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 (#27532) | `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-10 | `b4054c8ab` | 模型支持/运行时入口 | Revert "[CI] Add Async Eplb nightly CI tests (#29385)" (#30431) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-12-08 | `184076c3f` | 性能/后端优化 | [DeepSeek v3.2] Make top-k work for any logit values. (#27568) | `csrc/ops.h`, `csrc/sampler.cu`, `csrc/torch_bindings.cpp` |
| 2025-12-03 | `7fe9c1a22` | 模型支持/运行时入口 | [CI] Add Async Eplb nightly CI tests (#29385) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-12-02 | `9057fc2f1` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `5e5646e20` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `339e84ce8` | 缺陷修复 | [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-02 | `51c57b51d` | 缺陷修复 | [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-02 | `d8c6210ee` | 性能/后端优化 | Add Mistral Large 3 and Ministral 3 (#29757) | `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-11-30 | `14dc2b305` | 性能/后端优化 | [fix]解决deepseek模型cudagraph模式下精度异常问题 | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-24 | `8005e606b` | 性能/后端优化 | [Bugfix][Rocm] Fix shared expert weight loading failure in DeepSeek-MTP (#27563) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-21 | `9a3101b2b` | 性能/后端优化 | [Rocm][CI] Fix DeekSeek V2-Lite Accuracy CI (#29135) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh` |
| 2025-11-20 | `06c20c990` | 性能/后端优化 | [ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA (#26670) | `csrc/cache_kernels.cu`, `vllm/attention/ops/rocm_aiter_mla_sparse.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-20 | `7218f8399` | 性能/后端优化 | [ROCm][BugFix] Fix shared expert loading error when disable `VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS` (#28633) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-19 | `0075bfffd` | 缺陷修复 | [CI] Fix precommit `rope_theta` issue (#29040) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-19 | `88f5b19f0` | 缺陷修复 | [DeepSeek] Fix DeepSeek V3.2 Rope Embedding (#28968) | `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-15 | `e439c784f` | 调度/缓存/PD | Add support for Eagle with separate lm-head and embed_tokens layers (#28549) | `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/models/deepseek_eagle.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-13 | `f687d53c8` | 性能/后端优化 | [fix]解决moe_fused_gate编译错误，去掉mla中mtp部分的修改 | `CMakeLists.txt`, `csrc/moe/moe_fused_gate.cu`, `csrc/moe/moe_ops.h` |
| 2025-11-13 | `81eaff625` | 模型支持/运行时入口 | restore v32 support | `vllm/model_executor/models/config.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-10 | `f080a8351` | 性能/后端优化 | [RFC][ROCm][AITER] Keep all AITER kernels in `_aiter_ops` class like `_custom_ops` and `_ipex_ops` (#24490) | `docs/design/moe_kernel_features.md`, `tests/kernels/moe/test_moe.py`, `tests/model_executor/test_enabled_custom_ops.py` |
| 2025-11-08 | `934a9c3b7` | 性能/后端优化 | [Model] Consolidate Deepseek-MoE implementation with DeepSeek-v2 (#28101) | `tests/models/registry.py`, `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_ocr.py` |
| 2025-11-06 | `43ecd0a90` | 模型支持/运行时入口 | [Chore] Clean up deepseek v2/v3 config copy (#28055) | `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/kimi_vl.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-10-31 | `1851782dd` | 模型支持/运行时入口 | 删除DPSK_FP16_QUICK | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-10-30 | `2bf0bcc1f` | 模型支持/运行时入口 | [CI Test] Add Scheduled Integration Test (#27765) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh`, `.buildkite/test-pipeline.yaml` |
| 2025-10-31 | `100420579` | 模型支持/运行时入口 | [MTP] Refactor mtp predictor to avoid d2h operation (#27643) | `vllm/model_executor/models/deepseek_mtp.py` |

## 逐 Commit 审计卡

### Commit `aef3c4873` - [Feature]添加PCP功能，只支持mla架构，CPLB待验证

- 完整 hash: `aef3c487310cb5103519e25d25098e93f163b2d0`
- 时间/作者: 2026-04-22 / wangmin6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/config/parallel.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py`, `vllm/envs.py`, `vllm/forward_context.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_mtp.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/parallel.py`; `vllm/config/vllm.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/layers/sparse_attn_indexer.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/v1/worker/block_table.py`; `vllm/v1/worker/gpu_model_runner.py`
  - runtime-perf: `vllm/v1/attention/backend.py`; `vllm/v1/attention/backends/mla/flashmla_sparse.py`; `vllm/v1/attention/backends/mla/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a05d749ea` - [BUGFIX] rms_quant融合功能适配DSA

- 完整 hash: `a05d749eab4d1ecac1e7cba6e31051b2679da76f`
- 时间/作者: 2026-04-08 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/linear.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2888b4e5a` - 优化VLLM_DISABLE_DSA的设置，加入envs中，默认关，开启可强制关闭dsa

- 完整 hash: `2888b4e5a7ec26b78bbbb6704277fc2cf58e9f6c`
- 时间/作者: 2026-03-28 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/config.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `eb933fe15` - feat(moe): 修复 shared_output 透传被覆盖并兼容 torch.compile 启动路径 移除 forward 中对 experts.use_overlapped/_shared_experts 的状态改写，避免 torch.compile 启动期 shared/non-shared 路径不一致 FusedMoE.forward_impl 仅在 shared_output 为空时计算 shared experts，防止透传值被本地重算覆盖

- 完整 hash: `eb933fe15ff67ecf908dd40e0009a27981532c22`
- 时间/作者: 2026-03-19 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0639678c5` - feat(moe): 增加 LightOP moe_sum+mul+add 融合并打通参数透传   新增环境变量 VLLM_USE_LIGHTOP_MOE_SUM_MUL_ADD 用于控制   fused sum+mul+add 开关。   在 DeepseekV2MoE 中增加 fused 路径，预计算 shared_output，并下传 iqis 与 routed_scaling_factor。   扩展 FusedMoE/SharedFusedMoE 及相关 custom op 接口，统一透传 i_q/i_s/shared_output/routed_scaling_factor。   同步适配 Triton、Marlin W16A16、SlimQuant W4A8、CompressedTensors W8A8 等实现，支持在内核侧完成 sum+mul+add。

- 完整 hash: `0639678c5a42354614c6bf696ee25867c80ddcac`
- 时间/作者: 2026-03-18 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3bff7958e` - x接入mla_cat算子仅在nmz和kvcache-fp8情况下生效，默认关闭，开启需要export VLLM_USE_CAT_MLA=1

- 完整 hash: `3bff7958eb6d717cfbdcf69d01317800083e729a`
- 时间/作者: 2026-03-18 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/attention/backends/mla/flashmla.py`, `vllm/v1/attention/ops/flashmla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`; `vllm/v1/attention/backends/mla/flashmla.py`; `vllm/v1/attention/ops/flashmla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6395b73e8` - feat:接入VLLM_USE_FUSED_FILL_RMS_CAT优化

- 完整 hash: `6395b73e83ee5c86f65ee459a5ccebcca2aabe48`
- 时间/作者: 2026-03-17 / liuchy5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2ce72b9c2` - [feat]deepseek mtp支持pp模式

- 完整 hash: `2ce72b9c22e92492cf4407b1d5ea8e01411c6040`
- 时间/作者: 2026-03-16 / 王敏
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `168ceef7c` - perf: DS V2模型MOE部分增加rmsQuant

- 完整 hash: `168ceef7c3b0bee93529dbc87246b6f73b0fc67e`
- 时间/作者: 2026-03-12 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2350c778f` - perf: DS V2模型MLA中增加rmsQuant

- 完整 hash: `2350c778fb9b05a676189dbcf681c5e63452f412`
- 时间/作者: 2026-03-12 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `96abd293f` - dpsk_v32的mtp层的dense加载适配

- 完整 hash: `96abd293fe98416ed385a9f9455c3473830a4a61`
- 时间/作者: 2026-03-11 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/attention/ops/flashmla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
  - runtime-perf: `vllm/v1/attention/ops/flashmla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `83c871fbe` - feat: support shared expert fusion.

- 完整 hash: `83c871fbe206c4bba382ce7780c114d9fb2ce2d5`
- 时间/作者: 2026-03-07 / wanglong3
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_aiter_ops.py`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `58a365086` - perf:Deepseek v2模型增加rmsQuant和siluMulQuant融合

- 完整 hash: `58a365086c6076cd7dcabf92cf9df9decd1c7908`
- 时间/作者: 2026-03-06 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/linear.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cb1a27d25` - 修复dsa的workspace的bug，以及添加环境变量关闭DSAVLLM_DISABLE_DSA=1

- 完整 hash: `cb1a27d259e25e739f7e5141bdcf7ecd0975b2ab`
- 时间/作者: 2026-03-05 / yangql
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d71496bf0` - support dsa

- 完整 hash: `d71496bf0dccee23e47f1c2aed21c3fbe2d9440b`
- 时间/作者: 2026-03-03 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/ops/flashmla.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/v1/worker/gpu_model_runner.py`
  - runtime-perf: `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backends/mla/indexer.py`; `vllm/v1/attention/ops/flashmla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `afe3ea1ec` - [Model] GLM adaptation

- 完整 hash: `afe3ea1eccb04c872c5daa4580941ad1b42b2079`
- 时间/作者: 2026-03-02 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/kernels/benchmark_moe.py`, `tests/models/registry.py`, `tests/models/test_initialization.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/model_arch_config_convertor.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/kernels/benchmark_moe.py`
  - runtime-model: `vllm/config/speculative.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/registry.py`; `tests/models/test_initialization.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `df7041633` - sync v0.15.1 (models)

- 完整 hash: `df7041633878cacfcd677cef5efc907705de6c98`
- 时间/作者: 2026-02-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/bagel.py` 等 169 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 147 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d7db129ab` - 修复awq/w4a16的triton支持，以及fuse_moe的接口对齐，以及awq_moe_marlin推理的相关bug，并解决awq/w4a16的精度问题

- 完整 hash: `d7db129ab909dfcf4d4b4eb0201174d07b5b0680`
- 时间/作者: 2026-02-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/fused_marlin_moe_w4a16.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/awq_triton.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_marlin_moe_w4a16.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/awq_triton.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/moe_wna16.py`; `vllm/model_executor/layers/quantization/utils/marlin_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5fe035497` - [perf] add VLLM_USE_FUSED_FILL_RMS_CAT to use lightop for dpsk mtp fill + rms*2 + cat

- 完整 hash: `5fe035497763d3e6a6cc8729c2c69dd8b43c8dcc`
- 时间/作者: 2026-02-04 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b31c72519` - fix run error

- 完整 hash: `b31c72519f3b38835468c679f39fb99131147a87`
- 时间/作者: 2026-02-03 / zhuwenwen
- 自动分类: 缺陷修复
- 主要文件: `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/config/model.py`; `vllm/config/speculative.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `be6931ee2` - [ROCm][Bugfix] Fix ptpc scale load issue for fused shared expert path in deepseek mtp (#33018)

- 完整 hash: `be6931ee275b477dbd5e7cb1b7f99dcd37a6807a`
- 时间/作者: 2026-01-26 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dcd80206b` - [Chore] Update type annotation of `input_ids` in model forward (#33063)

- 完整 hash: `dcd80206b7a9143c81f7f2808e84914f8e38ce95`
- 时间/作者: 2026-01-26 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 140 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
  - tests: `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6c20e89c0` - [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp (#29287)

- 完整 hash: `6c20e89c0209284c1f6c99ecd59c786a78f81b7d`
- 时间/作者: 2026-01-21 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_aiter_ops.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_aiter_ops.py`
  - runtime-model: `vllm/config/compilation.py`; `vllm/model_executor/layers/sparse_attn_indexer.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/platforms/rocm.py`; `vllm/v1/attention/backends/mla/indexer.py`; `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`; `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c4e5bdf61` - [Bugfix] Fix the  fp8_mqa_logits dim mismatch (#32652)

- 完整 hash: `c4e5bdf61b00882749f9a4184c0576b4aa4ed512`
- 时间/作者: 2026-01-20 / Chauncey
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`, `vllm/utils/deep_gemm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/utils/deep_gemm.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5de6dd066` - [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding (#32175)

- 完整 hash: `5de6dd0662da663aa57127e82499d2c2d604c3d0`
- 时间/作者: 2026-01-16 / Kebe
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2c9b4cf5b` - [BugFix] Fix DeepSeek-V3.1 + DeepGEMM incompatible scale shapes (#32361)

- 完整 hash: `2c9b4cf5bf844de0471f77e6579e16c7bc3ee0d0`
- 时间/作者: 2026-01-14 / Lucas Wilkinson
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/utils/quant_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/quant_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fefce4980` - [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240)

- 完整 hash: `fefce49807a52fc94678e336fc5d1f3b7ebe2daf`
- 时间/作者: 2026-01-13 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_completion_error.py`, `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_protocol.py` 等 128 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py`; `vllm/reasoning/holo2_reasoning_parser.py` 等 45 个文件
  - runtime-model: `vllm/entrypoints/anthropic/serving_messages.py`; `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/__init__.py`; `vllm/entrypoints/openai/chat_completion/api_router.py`; `vllm/entrypoints/openai/chat_completion/protocol.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/chat_completion/stream_harmony.py` 等 43 个文件
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/responses/test_errors.py`; `tests/entrypoints/openai/responses/test_function_call_parsing.py`; `tests/entrypoints/openai/test_chat_error.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_completion_error.py`; `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_protocol.py` 等 39 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `600aaab8d` - [Model] Remove incorrect `SupportsPP` from MTP models (#32150)

- 完整 hash: `600aaab8d626301f4dbfcd812ccf47b3e8d81ac9`
- 时间/作者: 2026-01-12 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`, `vllm/model_executor/models/longcat_flash_mtp.py`, `vllm/model_executor/models/openpangu_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/ernie_mtp.py`; `vllm/model_executor/models/openpangu_mtp.py`; `vllm/model_executor/models/qwen3_next_mtp.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/longcat_flash_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2612ba928` - [1/N][Attention] Restructure attention: move files (#31916)

- 完整 hash: `2612ba9285d828f3179801334b6d2db0046b9b6c`
- 时间/作者: 2026-01-09 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `.github/mergify.yml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `docs/contributing/model/basic.md`, `docs/design/custom_op.md` 等 195 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/kernels.yaml`; `.github/CODEOWNERS`; `.github/mergify.yml`
  - docs-bench: `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`; `docs/contributing/model/basic.md`; `docs/design/custom_op.md`; `docs/design/plugin_system.md`; `examples/offline_inference/basic/embed.py`; `examples/offline_inference/basic/score.py`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/cpu.py` 等 10 个文件
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/batch_invariant.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py` 等 66 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/__init__.py`; `vllm/config/attention.py`; `vllm/distributed/kv_transfer/kv_connector/utils.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py` 等 73 个文件
  - tests: `tests/compile/fullgraph/test_full_cudagraph.py`; `tests/compile/fullgraph/test_full_graph.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/config/test_multimodal_config.py`; `tests/engine/test_arg_utils.py`; `tests/kernels/attention/test_aiter_flash_attn.py`; `tests/kernels/attention/test_attention.py` 等 35 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8cfec41a0` - remove USE_FUSED_RMS_QUANT

- 完整 hash: `8cfec41a08c1cfba5bce3b6613cb351c0ed2882c`
- 时间/作者: 2026-01-07 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/linear.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `482914849` - [BugFix] LoRA: Support loading base_layer of experts (#31104)

- 完整 hash: `482914849cf9ce61d3e0dffaa35096bb34de58f5`
- 时间/作者: 2026-01-07 / ℍ𝕠𝕝𝕝𝕠𝕨 𝕄𝕒𝕟
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/dots1.py`, `vllm/model_executor/models/ernie45_moe.py` 等 35 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/dots1.py`; `vllm/model_executor/models/gpt_oss.py`; `vllm/model_executor/models/grok1.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py` 等 19 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `60b37c6b9` - remove USE_FUSED_RMS_QUANT and USE_FUSED_SILU_MUL_QUANT

- 完整 hash: `60b37c6b9e29bcb5419185eb9851ed0ff03dc619`
- 时间/作者: 2026-01-07 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/linear.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c964b9ad2` - skip indexer_k_cache

- 完整 hash: `c964b9ad223c3df4a7e95c7533a3a83cf433a823`
- 时间/作者: 2026-01-07 / zhuwenwen
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `4ec647327` - add indexer_k_cache_kernel

- 完整 hash: `4ec6473275d826ab6768827d1563cd38e5795261`
- 时间/作者: 2026-01-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp`, `vllm/_custom_ops.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `csrc/torch_bindings.cpp`; `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `csrc/cache.h`; `csrc/cache_kernels.cu`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `25ec6a347` - update mqa_logits and paged_mqa_logits

- 完整 hash: `25ec6a34741abc478fd9395338b316f245f516bd`
- 时间/作者: 2026-01-06 / zhuwenwen
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b41aeb346` - [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261)

- 完整 hash: `b41aeb3468fecb33b7934fc7ca5406bdba84dace`
- 时间/作者: 2025-12-24 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `76e6a9519` - [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2 (#31160)

- 完整 hash: `76e6a951925bf37c49f88ad155dc9fcec01a3faf`
- 时间/作者: 2025-12-23 / Wentao Ye
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `4cf942989` - [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2 (#31046)

- 完整 hash: `4cf9429897c1a6c720a0f099a7a46e9d51af9342`
- 时间/作者: 2025-12-19 / Wentao Ye
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `22c6c645c` - fix moe params and run error

- 完整 hash: `22c6c645ce3a7fccdd0d374976b71f3add1864fd`
- 时间/作者: 2025-12-19 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/ops/flashmla.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/attention/ops/flashmla.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `41b6f9200` - Remove all2all backend envvar (#30363)

- 完整 hash: `41b6f9200fef27cd43b3299408a6f0e50654931f`
- 时间/作者: 2025-12-18 / Elizabeth Thomas
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/distributed.yaml`, `docs/design/moe_kernel_features.md`, `examples/online_serving/elastic_ep/serve_deepseek_v2.sh`, `tests/v1/cudagraph/test_cudagraph_dispatch.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/distributed.yaml`
  - docs-bench: `docs/design/moe_kernel_features.md`; `examples/online_serving/elastic_ep/serve_deepseek_v2.sh`
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/parallel.py`
  - tests: `tests/v1/cudagraph/test_cudagraph_dispatch.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d2fe5111f` - fix optional and profling

- 完整 hash: `d2fe5111f75544ee384d359d2aad567417cfdb97`
- 时间/作者: 2025-12-18 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/compilation/decorators.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/compilation/decorators.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b166ef20e` - [refactor] Add prefix support to embed_tokens in DeepSeek MTP (#30788)

- 完整 hash: `b166ef20e1e5256913b34456507d89850a8dba38`
- 时间/作者: 2025-12-18 / zzhxxx
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `84896fda2` - [Bugfix] deepseek-V3.2 self.weights_proj has no bias (#30841)

- 完整 hash: `84896fda22d3de74398a88b5769c98eef14258f1`
- 时间/作者: 2025-12-17 / baoqian426
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b66c8e4b2` - Synchronize the modifications from the 12th to the 17th: 修复CompressedTensorsLinearMethod中的w4a16的冲突问题 feat(moe): add Marlin W16A16 fused MoE behind VLLM_USE_MARLIN_W16A16_MOE replace the fp8_mqa_logits and fp8_paged_mqa_logits interfaces in deepgemm with mqa_logits and paged_mqa_logits from lightop

- 完整 hash: `b66c8e4b22302c944d6b68732792ecaee81a3768`
- 时间/作者: 2025-12-17 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`, `vllm/model_executor/layers/fused_moe/marlin_quant.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/qwen3_moe.py`, `vllm/v1/attention/backends/mla/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`; `vllm/model_executor/layers/fused_moe/marlin_quant.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/v1/attention/backends/mla/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `10ee1c64c` - [CI] Generalize gsm8k test args and add Qwen3-Next MTP B200 test (#30723)

- 完整 hash: `10ee1c64cfa7c0b7f68e9ee793435c9cafbf821a`
- 时间/作者: 2025-12-16 / Michael Goin
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml`, `tests/evals/gsm8k/configs/Llama-3-8B-Instruct-nonuniform-CT.yaml`, `tests/evals/gsm8k/configs/Llama-3.2-1B-Instruct-INT8-CT.yaml`, `tests/evals/gsm8k/configs/Qwen1.5-MoE-W4A16-CT.yaml`, `tests/evals/gsm8k/configs/Qwen2.5-VL-3B-Instruct-FP8-dynamic.yaml`, `tests/evals/gsm8k/configs/Qwen3-0.6B-FP8.yaml` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
  - tests: `tests/evals/gsm8k/README.md`; `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml`; `tests/evals/gsm8k/configs/Llama-3-8B-Instruct-nonuniform-CT.yaml`; `tests/evals/gsm8k/configs/Llama-3.2-1B-Instruct-INT8-CT.yaml`; `tests/evals/gsm8k/configs/Qwen1.5-MoE-W4A16-CT.yaml`; `tests/evals/gsm8k/configs/Qwen2.5-VL-3B-Instruct-FP8-dynamic.yaml`; `tests/evals/gsm8k/configs/Qwen3-0.6B-FP8.yaml`; `tests/evals/gsm8k/configs/Qwen3-30B-A3B-NVFP4.yaml` 等 12 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ed586e772` - [Refactor] [3/N] Move tool parser tests and run on CPU (#30693)

- 完整 hash: `ed586e7724fdf91b391abcf6f3e473be641ff5d6`
- 时间/作者: 2025-12-15 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/tool_use.yaml`, `tests/tool_parsers/__init__.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_ernie45_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/misc.yaml`; `.buildkite/test_areas/tool_use.yaml`
  - tests: `tests/tool_parsers/__init__.py`; `tests/tool_parsers/test_deepseekv31_tool_parser.py`; `tests/tool_parsers/test_ernie45_moe_tool_parser.py`; `tests/tool_parsers/test_glm4_moe_tool_parser.py`; `tests/tool_parsers/test_jamba_tool_parser.py`; `tests/tool_parsers/test_kimi_k2_tool_parser.py`; `tests/tool_parsers/test_minimax_tool_parser.py`; `tests/tool_parsers/test_mistral_tool_parser.py` 等 12 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `2a1776b7a` - [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675)

- 完整 hash: `2a1776b7ac4fae7c50c694edeafc1b14270e4350`
- 时间/作者: 2025-12-15 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py` 等 61 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`
  - other: `vllm/tool_parsers/__init__.py`; `vllm/tool_parsers/abstract_tool_parser.py`; `vllm/tool_parsers/deepseekv31_tool_parser.py`; `vllm/tool_parsers/deepseekv32_tool_parser.py`; `vllm/tool_parsers/deepseekv3_tool_parser.py`; `vllm/tool_parsers/ernie45_tool_parser.py`; `vllm/tool_parsers/gigachat3_tool_parser.py`; `vllm/tool_parsers/granite_20b_fc_tool_parser.py` 等 30 个文件
  - runtime-model: `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/parser/responses_parser.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py` 等 22 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3e41992fe` - [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 (#27532)

- 完整 hash: `3e41992fecdc31ee60715bb350f18fec18ed6680`
- 时间/作者: 2025-12-12 / Lucas Wilkinson
- 自动分类: 性能/后端优化
- 主要文件: `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp`, `tests/conftest.py`, `tests/kernels/moe/test_batched_deepgemm.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_cutlass_moe.py` 等 30 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `csrc/torch_bindings.cpp`; `vllm/_custom_ops.py`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/gpu_worker.py`; `vllm/v1/worker/workspace.py`
  - runtime-perf: `csrc/cache.h`; `csrc/cache_kernels.cu`; `vllm/model_executor/layers/fused_moe/modular_kernel.py`; `vllm/v1/attention/backends/mla/flashmla_sparse.py`; `vllm/v1/attention/backends/mla/indexer.py`; `vllm/v1/attention/backends/utils.py`
  - tests: `tests/conftest.py`; `tests/kernels/moe/test_batched_deepgemm.py`; `tests/kernels/moe/test_batched_moe.py`; `tests/kernels/moe/test_block_fp8.py`; `tests/kernels/moe/test_cutlass_moe.py`; `tests/kernels/moe/test_deepep_deepgemm_moe.py`; `tests/kernels/moe/test_deepep_moe.py`; `tests/kernels/moe/test_deepgemm.py` 等 17 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cf3eacfe5` - Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389)

- 完整 hash: `cf3eacfe58fa9e745c2854782ada884a9f992cf7`
- 时间/作者: 2025-12-11 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `vllm/config/utils.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/afmoe.py` 等 83 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `benchmarks/kernels/benchmark_rope.py`
  - runtime-model: `vllm/config/utils.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/olmoe.py` 等 12 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b4054c8ab` - Revert "[CI] Add Async Eplb nightly CI tests (#29385)" (#30431)

- 完整 hash: `b4054c8ab469a9c3c3c77a1c2f22f54a69b87145`
- 时间/作者: 2025-12-10 / Sage Moore
- 自动分类: 模型支持/运行时入口
- 主要文件: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-pipeline.yaml`, `vllm/distributed/eplb/rebalance_execute.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/eplb/rebalance_execute.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `184076c3f` - [DeepSeek v3.2] Make top-k work for any logit values. (#27568)

- 完整 hash: `184076c3fecf8c322648f36f69a4de836d7f519b`
- 时间/作者: 2025-12-08 / Daniel Cámpora
- 自动分类: 性能/后端优化
- 主要文件: `csrc/ops.h`, `csrc/sampler.cu`, `csrc/torch_bindings.cpp`, `tests/kernels/test_top_k_per_row.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `csrc/ops.h`; `csrc/torch_bindings.cpp`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `csrc/sampler.cu`
  - tests: `tests/kernels/test_top_k_per_row.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7fe9c1a22` - [CI] Add Async Eplb nightly CI tests (#29385)

- 完整 hash: `7fe9c1a2232275ee4cc7d65af3bc5b648543f367`
- 时间/作者: 2025-12-03 / WeiQing Chen
- 自动分类: 模型支持/运行时入口
- 主要文件: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-pipeline.yaml`, `vllm/distributed/eplb/rebalance_execute.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/eplb/rebalance_execute.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9057fc2f1` - [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908)

- 完整 hash: `9057fc2f1b2701c2f33223c1b4b4d4036f2dc998`
- 时间/作者: 2025-12-02 / Julien Denize
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5e5646e20` - [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908)

- 完整 hash: `5e5646e2064f925f97ff533aa688a43834e9ff96`
- 时间/作者: 2025-12-02 / Julien Denize
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `339e84ce8` - [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545)

- 完整 hash: `339e84ce86ee0cb50d1709dae1232ce4cda56398`
- 时间/作者: 2025-12-02 / Matthew Bonanni
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `51c57b51d` - [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545)

- 完整 hash: `51c57b51dd51d87715367850faae1da7a9cabaef`
- 时间/作者: 2025-12-02 / Matthew Bonanni
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d8c6210ee` - Add Mistral Large 3 and Ministral 3 (#29757)

- 完整 hash: `d8c6210eeaa7f3b474e50cf74926f77a8dc79adf`
- 时间/作者: 2025-12-02 / Julien Denize
- 自动分类: 性能/后端优化
- 主要文件: `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py`, `vllm/config/speculative.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8.json`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/tokenizers/mistral.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/speculative.py`; `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/mistral_large_3.py`; `vllm/model_executor/models/mistral_large_3_eagle.py`; `vllm/model_executor/models/registry.py` 等 10 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8.json`
  - tests: `tests/models/registry.py`; `tests/tokenizers_/test_mistral.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `653591d5e` - [Chore] Move tokenizer initialization methods (#29793)

- 完整 hash: `653591d5e73b34ffd9186c61e964474bcc4b7c80`
- 时间/作者: 2025-12-02 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_return_token_ids.py`, `tests/entrypoints/openai/test_return_tokens_as_ids.py`, `tests/entrypoints/openai/test_serving_chat.py` 等 51 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/benchmark_prefix_caching.py`; `benchmarks/benchmark_serving_structured_output.py`
  - other: `vllm/benchmarks/serve.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/__init__.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/async_llm.py`; `vllm/v1/engine/llm_engine.py`; `vllm/v1/structured_output/__init__.py`
  - runtime-model: `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py`; `vllm/model_executor/models/granite_speech.py`; `vllm/model_executor/models/gritlm.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/pixtral.py`; `vllm/model_executor/models/voxtral.py` 等 9 个文件
  - tests: `tests/compile/test_dynamic_shapes_compilation.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_return_token_ids.py`; `tests/entrypoints/openai/test_return_tokens_as_ids.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_token_in_token_out.py`; `tests/entrypoints/openai/test_tokenization.py` 等 32 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `14dc2b305` - [fix]解决deepseek模型cudagraph模式下精度异常问题

- 完整 hash: `14dc2b3058a75111bd0a72adb3d205c5651ff410`
- 时间/作者: 2025-11-30 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `34a984274` - [Misc] Refactor tokenizer interface (#29693)

- 完整 hash: `34a984274eae2f8fb9d1d6413abd08d7fcde741c`
- 时间/作者: 2025-11-29 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py`, `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/openai/tool_parsers/conftest.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py` 等 119 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/backend_request_func.py`; `docs/features/reasoning_outputs.md`; `docs/features/tool_calling.md`
  - other: `tools/pre_commit/check_pickle_imports.py`; `tools/pre_commit/mypy.py`; `vllm/benchmarks/datasets.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/logits_process.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py` 等 32 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_classification.py`; `vllm/entrypoints/openai/serving_completion.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/serving_responses.py`; `vllm/entrypoints/openai/serving_score.py` 等 44 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/openai/tool_parsers/conftest.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/utils.py` 等 37 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `430dd4d9e` - [Attention] Remove imports from `vllm/attention/__init__.py` (#29342)

- 完整 hash: `430dd4d9eb7e342e28012351df06d93892f86741`
- 时间/作者: 2025-11-26 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/kernels/utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_utils.py`, `vllm/attention/__init__.py`, `vllm/attention/backends/abstract.py` 等 96 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`
  - other: `vllm/compilation/fusion_attn.py`; `vllm/compilation/qk_norm_rope_fusion.py`; `vllm/v1/kv_offload/cpu.py`; `vllm/v1/kv_offload/spec.py`
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bloom.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/attention/__init__.py`; `vllm/attention/backends/abstract.py`; `vllm/attention/layer.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py` 等 20 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/kernels/utils.py`; `tests/v1/worker/test_gpu_model_runner.py`; `tests/v1/worker/test_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8005e606b` - [Bugfix][Rocm] Fix shared expert weight loading failure in DeepSeek-MTP (#27563)

- 完整 hash: `8005e606bf280b7b6002f57e95ae3210ddc6f041`
- 时间/作者: 2025-11-24 / 杰兮
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9a3101b2b` - [Rocm][CI] Fix DeekSeek V2-Lite Accuracy CI (#29135)

- 完整 hash: `9a3101b2ba6821488f4b7a9b93124e479edc4d3e`
- 时间/作者: 2025-11-21 / Charlie Fu
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `06c20c990` - [ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA (#26670)

- 完整 hash: `06c20c9904644d8f65523bb747756b2eae706b8e`
- 时间/作者: 2025-11-20 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `csrc/cache_kernels.cu`, `vllm/attention/ops/rocm_aiter_mla_sparse.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/platforms/rocm.py`, `vllm/utils/deep_gemm.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/utils/deep_gemm.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `csrc/cache_kernels.cu`; `vllm/attention/ops/rocm_aiter_mla_sparse.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backends/mla/flashmla_sparse.py`; `vllm/v1/attention/backends/mla/indexer.py`; `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7218f8399` - [ROCm][BugFix] Fix shared expert loading error when disable `VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS` (#28633)

- 完整 hash: `7218f83992c7d61fc3845ea24407a1f3b909713e`
- 时间/作者: 2025-11-20 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0075bfffd` - [CI] Fix precommit `rope_theta` issue (#29040)

- 完整 hash: `0075bfffd4201d1377f0d048848f82911e917639`
- 时间/作者: 2025-11-19 / Wentao Ye
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `88f5b19f0` - [DeepSeek] Fix DeepSeek V3.2 Rope Embedding (#28968)

- 完整 hash: `88f5b19f0bc681c016eaaa17502d3bb4e2b59b51`
- 时间/作者: 2025-11-19 / Yongye Zhu
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/mla.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `a8b70304d` - Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542)

- 完整 hash: `a8b70304d68497ac1c432a2ff343e9bfb516c227`
- 时间/作者: 2025-11-19 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/language/pooling/test_nomic_max_model_len.py` 等 104 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `examples/offline_inference/context_extension.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py` 等 78 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 17 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/models/language/pooling/test_nomic_max_model_len.py`; `tests/test_config.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e439c784f` - Add support for Eagle with separate lm-head and embed_tokens layers (#28549)

- 完整 hash: `e439c784fa318dbc23c04b0730bee0fccf46481d`
- 时间/作者: 2025-11-15 / Eldar Kurtić
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/llama4_eagle.py`, `vllm/model_executor/models/llama_eagle.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/llama4_eagle.py`; `vllm/model_executor/models/llama_eagle.py`; `vllm/model_executor/models/llama_eagle3.py`; `vllm/model_executor/models/minicpm_eagle.py` 等 9 个文件
  - tests: `tests/v1/spec_decode/test_eagle.py`; `tests/v1/spec_decode/test_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `97d1c9930` - Rename clashing method names for vLLM model protocol (#27583)

- 完整 hash: `97d1c99302df6f7eadc0d0b32ec174db69cb4421`
- 时间/作者: 2025-11-13 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/baichuan.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`; `docs/contributing/model/multimodal.md`
  - other: `vllm/multimodal/processing.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/bert.py` 等 144 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f687d53c8` - [fix]解决moe_fused_gate编译错误，去掉mla中mtp部分的修改

- 完整 hash: `f687d53c8127df0bbdb7ab6490696d58d1425f09`
- 时间/作者: 2025-11-13 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `CMakeLists.txt`, `csrc/moe/moe_fused_gate.cu`, `csrc/moe/moe_ops.h`, `csrc/moe/torch_bindings.cpp`, `vllm/_custom_ops.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/v1/attention/backends/mla/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `CMakeLists.txt`; `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
  - runtime-perf: `csrc/moe/moe_fused_gate.cu`; `csrc/moe/moe_ops.h`; `csrc/moe/torch_bindings.cpp`; `vllm/v1/attention/backends/mla/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `81eaff625` - restore v32 support

- 完整 hash: `81eaff625c0e832cd6b72f9ddd90feabd2277b1c`
- 时间/作者: 2025-11-13 / zhuwenwen
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/config.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/config.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f080a8351` - [RFC][ROCm][AITER] Keep all AITER kernels in `_aiter_ops` class like `_custom_ops` and `_ipex_ops` (#24490)

- 完整 hash: `f080a83511511a9c0a222451a752a1623aec095d`
- 时间/作者: 2025-11-10 / vllmellm
- 自动分类: 性能/后端优化
- 主要文件: `docs/design/moe_kernel_features.md`, `tests/kernels/moe/test_moe.py`, `tests/model_executor/test_enabled_custom_ops.py`, `vllm/_aiter_ops.py`, `vllm/attention/ops/rocm_aiter_mla.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/design/moe_kernel_features.md`
  - other: `vllm/_aiter_ops.py`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/attention/ops/rocm_aiter_mla.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py` 等 16 个文件
  - tests: `tests/kernels/moe/test_moe.py`; `tests/model_executor/test_enabled_custom_ops.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `934a9c3b7` - [Model] Consolidate Deepseek-MoE implementation with DeepSeek-v2 (#28101)

- 完整 hash: `934a9c3b79e6cb860a8d23b7f317a5f63adf0fae`
- 时间/作者: 2025-11-08 / Isotr0py
- 自动分类: 性能/后端优化
- 主要文件: `tests/models/registry.py`, `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_vl2.py`, `vllm/model_executor/models/registry.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/deepseek_vl2.py`; `vllm/model_executor/models/registry.py`
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `43ecd0a90` - [Chore] Clean up deepseek v2/v3 config copy (#28055)

- 完整 hash: `43ecd0a900e45e0c594bb428f18b8f2b14434391`
- 时间/作者: 2025-11-06 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/deepseek_v3.py`, `vllm/transformers_utils/configs/deepseek_vl2.py`, `vllm/transformers_utils/configs/eagle.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/kimi_vl.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/deepseek_v3.py`; `vllm/transformers_utils/configs/deepseek_vl2.py`; `vllm/transformers_utils/configs/eagle.py` 等 9 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e50c45467` - [BugFix] Support EP/DP + EPLB with MTP (#25311)

- 完整 hash: `e50c45467215f96068d95736b08d8a25f624e67d`
- 时间/作者: 2025-11-05 / Ilya Markov
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/ernie45_moe.py` 等 27 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/v1/spec_decode/medusa.py`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama4.py`; `vllm/model_executor/models/llama4_eagle.py` 等 17 个文件
  - runtime-perf: `vllm/distributed/eplb/eplb_state.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/model_executor/models/transformers/moe.py`
  - tests: `tests/distributed/test_eplb_spec_decode.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c02fccdbd` - [Refactor] Lazy import tool_parser (#27974)

- 完整 hash: `c02fccdbd2794fe016ebd738e3a8b8c8d78eb78c`
- 时间/作者: 2025-11-04 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py`, `tests/tool_use/test_glm4_moe_tool_parser.py`, `tests/tool_use/test_jamba_tool_parser.py`, `tests/tool_use/test_kimi_k2_tool_parser.py`, `tests/tool_use/test_minimax_tool_parser.py`, `tests/tool_use/test_openai_tool_parser.py` 等 40 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`
  - runtime-model: `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`; `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv3_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/ernie45_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/granite_20b_fc_tool_parser.py` 等 29 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/tool_use/test_deepseekv31_tool_parser.py`; `tests/tool_use/test_ernie45_moe_tool_parser.py`; `tests/tool_use/test_glm4_moe_tool_parser.py`; `tests/tool_use/test_jamba_tool_parser.py`; `tests/tool_use/test_kimi_k2_tool_parser.py`; `tests/tool_use/test_minimax_tool_parser.py`; `tests/tool_use/test_openai_tool_parser.py`; `tests/tool_use/test_seed_oss_tool_parser.py` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1851782dd` - 删除DPSK_FP16_QUICK

- 完整 hash: `1851782dd5d991344df66b247af58b51a988a0ed`
- 时间/作者: 2025-10-31 / zhuwenwen
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2bf0bcc1f` - [CI Test] Add Scheduled Integration Test (#27765)

- 完整 hash: `2bf0bcc1fca422222b78a3b1f39845ecd037aecc`
- 时间/作者: 2025-10-30 / Wentao Ye
- 自动分类: 模型支持/运行时入口
- 主要文件: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh`, `.buildkite/test-pipeline.yaml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep.sh`; `.buildkite/test-pipeline.yaml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `100420579` - [MTP] Refactor mtp predictor to avoid d2h operation (#27643)

- 完整 hash: `10042057953cd1528701234925de3d7b109e26de`
- 时间/作者: 2025-10-31 / Mengqing Cao
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
