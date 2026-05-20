# vllm DeepSeek V3.2 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `examples/online_serving/elastic_ep/serve_deepseek_v2.sh` | `41b6f9200` |
| `vllm/entrypoints/encoding_dsv32.py` | `ba7bcccdd` |
| `vllm/model_executor/models/deepseek_mtp.py` | `aef3c4873`, `2888b4e5a`, `3bff7958e`, `6395b73e8`, `2ce72b9c2`, `96abd293f`, `df7041633`, `5fe035497`, `be6931ee2`, `dcd80206b`, `600aaab8d`, `482914849`, ... (15 total) |
| `vllm/model_executor/models/deepseek_v2.py` | `aef3c4873`, `a05d749ea`, `2888b4e5a`, `eb933fe15`, `0639678c5`, `168ceef7c`, `2350c778f`, `83c871fbe`, `58a365086`, `cb1a27d25`, `d71496bf0`, `afe3ea1ec`, ... (41 total) |
| `vllm/renderers/deepseek_v32.py` | `d117a4d1a` |
| `vllm/tokenizers/deepseek_v32.py` | `644482487`, `b7b6a60ac`, `a524d1ba0` |
| `vllm/tokenizers/deepseek_v32_encoding.py` | `f61c9da71`, `346e56455`, `82a64b3d8`, `ac1886588`, `b78772c43` |
| `vllm/tool_parsers/deepseekv32_tool_parser.py` | `fefce4980`, `2a1776b7a` |

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
| 2026-02-12 | `838b45097` | 调度/缓存/PD | update chat template of dsv32 | `vllm/renderers/hf.py` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-06 | `d7db129ab` | 性能/后端优化 | 修复awq/w4a16的triton支持，以及fuse_moe的接口对齐，以及awq_moe_marlin推理的相关bug，并解决awq/w4a16的精度问题 | `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/fused_marlin_moe_w4a16.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-02-04 | `5fe035497` | 性能/后端优化 | [perf] add VLLM_USE_FUSED_FILL_RMS_CAT to use lightop for dpsk mtp fill + rms*2 + cat | `vllm/envs.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-02-03 | `b31c72519` | 缺陷修复 | fix run error | `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-27 | `0d8ce320a` | 缺陷修复 | [Bugfix] Fix DeepseekV32 `AssertionError: num_kv_heads == 1` (#33090) | `vllm/distributed/kv_transfer/kv_connector/utils.py` |
| 2026-01-26 | `be6931ee2` | 性能/后端优化 | [ROCm][Bugfix] Fix ptpc scale load issue for fused shared expert path in deepseek mtp (#33018) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-01-26 | `9ef3b718d` | 缺陷修复 | [Bugfix] Fix Can't instantiate abstract class DeepseekV32IndexerBackend (#33052) | `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-22 | `f61c9da71` | 缺陷修复 | [BugFix] deepseek_v32_encoding: Replace asserts with proper exceptions (#32884) | `vllm/tokenizers/deepseek_v32_encoding.py` |
| 2026-01-22 | `d117a4d1a` | 模型支持/运行时入口 | [Frontend] Introduce Renderer for processing chat messages (using `ModelConfig`) (#30200) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2026-01-21 | `6c20e89c0` | 性能/后端优化 | [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp (#29287) | `vllm/_aiter_ops.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-01-20 | `c4e5bdf61` | 缺陷修复 | [Bugfix] Fix the fp8_mqa_logits dim mismatch (#32652) | `vllm/model_executor/models/deepseek_v2.py`, `vllm/utils/deep_gemm.py` |
| 2026-01-16 | `5de6dd066` | 缺陷修复 | [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding (#32175) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-07 | `8cfec41a0` | 性能/后端优化 | remove USE_FUSED_RMS_QUANT | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-07 | `60b37c6b9` | 性能/后端优化 | remove USE_FUSED_RMS_QUANT and USE_FUSED_SILU_MUL_QUANT | `vllm/envs.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py` |
| 2026-01-07 | `c964b9ad2` | 调度/缓存/PD | skip indexer_k_cache | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-06 | `644482487` | 模型支持/运行时入口 | [Misc] Implement `TokenizerLike.convert_tokens_to_ids` (#31796) | `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py` |
| 2026-01-06 | `4ec647327` | 性能/后端优化 | add indexer_k_cache_kernel | `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp` |
| 2026-01-06 | `25ec6a347` | 调度/缓存/PD | update mqa_logits and paged_mqa_logits | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-05 | `346e56455` | 缺陷修复 | Add chat prefix completion feature to DeepSeek v3.2 (#31147) | `vllm/tokenizers/deepseek_v32_encoding.py` |
| 2025-12-24 | `b41aeb346` | 性能/后端优化 | [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-24 | `369f47aa0` | 性能/后端优化 | [DeepSeek v3.2] Remove unnecessary syncwarps (#31047) | `csrc/cache_kernels.cu` |
| 2025-12-23 | `76e6a9519` | 缺陷修复 | [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2 (#31160) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-19 | `4cf942989` | 缺陷修复 | [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2 (#31046) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-19 | `22c6c645c` | 性能/后端优化 | fix moe params and run error | `vllm/attention/ops/flashmla.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2025-12-18 | `41b6f9200` | 性能/后端优化 | Remove all2all backend envvar (#30363) | `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml` |
| 2025-12-18 | `d2fe5111f` | 性能/后端优化 | fix optional and profling | `vllm/compilation/decorators.py`, `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-18 | `b166ef20e` | 缺陷修复 | [refactor] Add prefix support to embed_tokens in DeepSeek MTP (#30788) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-17 | `b7b6a60ac` | 模型支持/运行时入口 | Adapt the old parameter enable_thinking in chat_template_kwargs (#30852) | `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/tokenizers/deepseek_v32.py` |
| 2025-12-17 | `84896fda2` | 缺陷修复 | [Bugfix] deepseek-V3.2 self.weights_proj has no bias (#30841) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-17 | `b66c8e4b2` | 性能/后端优化 | Synchronize the modifications from the 12th to the 17th: 修复CompressedTensorsLinearMethod中的w4a16的冲突问题 feat(moe): add Marlin W16A16 fused MoE behind VLLM_USE_MARLIN_W16A16_MOE replace the fp8_mqa_logits and fp8_paged_mqa_logits interfaces in deepgemm with mqa_logits and paged_mqa_logits from lightop | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fuse_moe_w16a16_marlin.py`, `vllm/model_executor/layers/fused_moe/marlin_quant.py` |
| 2025-12-16 | `eaa82a709` | 缺陷修复 | [Bugfix][DSV32] Fix overflow in topk. (#30754) | `csrc/sampler.cu` |
| 2025-12-16 | `10ee1c64c` | 性能/后端优化 | [CI] Generalize gsm8k test args and add Qwen3-Next MTP B200 test (#30723) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml` |
| 2025-12-15 | `855b101d7` | 模型支持/运行时入口 | [Frontend] add tools for dsv32 developer role (#30040) | `vllm/entrypoints/chat_utils.py` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-15 | `a524d1ba0` | 缺陷修复 | [Bugfix] Fix deepseek_v32 tokenizer_mode (#30658) | `vllm/entrypoints/openai/serving_engine.py`, `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/registry.py` |
| 2025-12-13 | `39cefbdf1` | 调度/缓存/PD | [Refactor] `TokenizerRegistry` only uses lazy imports (#30609) | `tests/test_inputs.py`, `tests/tokenizers_/test_basic.py`, `tests/tokenizers_/test_registry.py` |
| 2025-12-12 | `3e34adcdf` | 调度/缓存/PD | [DeepSeek V3.2] Proper drop_thinking logic (#30490) | `vllm/tokenizers/deepseekv32.py` |
| 2025-12-12 | `3e41992fe` | 性能/后端优化 | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 (#27532) | `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-10 | `b4054c8ab` | 模型支持/运行时入口 | Revert "[CI] Add Async Eplb nightly CI tests (#29385)" (#30431) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-12-10 | `9db78f34d` | 缺陷修复 | [Bugfix] Fix the issue where DeepSeek v3.2 cannot use structured_output (#30371) | `vllm/v1/structured_output/backend_xgrammar.py` |
| 2025-12-10 | `d007387aa` | 缺陷修复 | [Bugfix] Cache added_vocab to avoid per-token overhead (#30351) | `vllm/tokenizers/deepseekv32.py` |
| 2025-12-08 | `184076c3f` | 性能/后端优化 | [DeepSeek v3.2] Make top-k work for any logit values. (#27568) | `csrc/ops.h`, `csrc/sampler.cu`, `csrc/torch_bindings.cpp` |
| 2025-12-07 | `0044c4038` | 性能/后端优化 | [BugFix][DeepSeek-V3.2] Fix backend selection logic for Blackwell (#30195) | `vllm/platforms/cuda.py` |
| 2025-12-05 | `40a046cd8` | 缺陷修复 | [Bugfix]: Fix `TokenizerLike` interface (#30009) | `vllm/benchmarks/datasets.py`, `vllm/benchmarks/serve.py`, `vllm/benchmarks/throughput.py` |
| 2025-12-04 | `ffdd18111` | 调度/缓存/PD | Add DeepSeek-V3.2 tool parser. (#29848) | `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv32_tool_parser.py` |
| 2025-12-04 | `82a64b3d8` | 缺陷修复 | [Bugfix] fixed deepseekv32 tool calling error (#30025) | `vllm/tokenizers/deepseek_v32_encoding.py`, `vllm/tokenizers/deepseekv32.py` |
| 2025-12-03 | `ac1886588` | 缺陷修复 | [CI] Fix re import error (#29973) | `.buildkite/scripts/generate-nightly-index.py`, `vllm/entrypoints/serve/instrumentator/metrics.py`, `vllm/tokenizers/deepseek_v32_encoding.py` |
| 2025-12-03 | `b78772c43` | 调度/缓存/PD | [Frontend] supports deepseekv32 chat template (#29837) | `vllm/config/model.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/tokenizers/__init__.py` |
| 2025-12-03 | `7fe9c1a22` | 模型支持/运行时入口 | [CI] Add Async Eplb nightly CI tests (#29385) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-12-02 | `9057fc2f1` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `5e5646e20` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `339e84ce8` | 缺陷修复 | [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-02 | `51c57b51d` | 缺陷修复 | [Bugfix] Fix DeepSeek R1 MTP weight loading (#29545) | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-12-02 | `d8c6210ee` | 性能/后端优化 | Add Mistral Large 3 and Ministral 3 (#29757) | `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py` |
| 2025-12-02 | `ba7bcccdd` | 模型支持/运行时入口 | add VLLM_USE_V32_ENCODE to use encoding_dsv32.py | `vllm/entrypoints/chat_utils.py`, `vllm/entrypoints/encoding_dsv32.py`, `vllm/envs.py` |
| 2025-11-30 | `14dc2b305` | 性能/后端优化 | [fix]解决deepseek模型cudagraph模式下精度异常问题 | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |

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

### Commit `838b45097` - update chat template of dsv32

- 完整 hash: `838b450973fcf3293552daa0f46ca53f8bb6c6b8`
- 时间/作者: 2026-02-12 / zhuwenwen
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/renderers/hf.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/renderers/hf.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `0d8ce320a` - [Bugfix] Fix DeepseekV32 `AssertionError: num_kv_heads == 1` (#33090)

- 完整 hash: `0d8ce320a2e5eaf9fc025c6744a8a89419f59c38`
- 时间/作者: 2026-01-27 / Nicolò Lucchesi
- 自动分类: 缺陷修复
- 主要文件: `vllm/distributed/kv_transfer/kv_connector/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `be6931ee2` - [ROCm][Bugfix] Fix ptpc scale load issue for fused shared expert path in deepseek mtp (#33018)

- 完整 hash: `be6931ee275b477dbd5e7cb1b7f99dcd37a6807a`
- 时间/作者: 2026-01-26 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9ef3b718d` - [Bugfix] Fix Can't instantiate abstract class DeepseekV32IndexerBackend (#33052)

- 完整 hash: `9ef3b718d98ada5c02ebe67c2a545d3005a6b10d`
- 时间/作者: 2026-01-26 / Chauncey
- 自动分类: 缺陷修复
- 主要文件: `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `f61c9da71` - [BugFix] deepseek_v32_encoding: Replace asserts with proper exceptions (#32884)

- 完整 hash: `f61c9da711d846220cb59738d10c0a937ffb80e2`
- 时间/作者: 2026-01-22 / Rishabh Saini
- 自动分类: 缺陷修复
- 主要文件: `vllm/tokenizers/deepseek_v32_encoding.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseek_v32_encoding.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d117a4d1a` - [Frontend] Introduce Renderer for processing chat messages (using `ModelConfig`) (#30200)

- 完整 hash: `d117a4d1a915c7acf124563f9b337de5c0aa2c2f`
- 时间/作者: 2026-01-22 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml`, `docs/features/reasoning_outputs.md`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/openai/test_serving_models.py` 等 48 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/misc.yaml`
  - docs-bench: `docs/features/reasoning_outputs.md`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/renderers/__init__.py`; `vllm/renderers/deepseek_v32.py`; `vllm/renderers/grok2.py`; `vllm/renderers/hf.py`; `vllm/renderers/mistral.py` 等 14 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/completion/serving.py`; `vllm/entrypoints/openai/engine/serving.py`; `vllm/entrypoints/openai/models/serving.py`; `vllm/entrypoints/openai/responses/context.py` 等 17 个文件
  - tests: `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/openai/test_serving_models.py`; `tests/entrypoints/openai/test_serving_responses.py`; `tests/entrypoints/pooling/score/test_utils.py`; `tests/entrypoints/test_chat_utils.py`; `tests/renderers/__init__.py` 等 13 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `644482487` - [Misc] Implement `TokenizerLike.convert_tokens_to_ids` (#31796)

- 完整 hash: `6444824873711eeeb68ded97cad79394bd051ed1`
- 时间/作者: 2026-01-06 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseek_v32.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `346e56455` - Add chat prefix completion feature to DeepSeek v3.2 (#31147)

- 完整 hash: `346e56455a3b10787c7d6e951861317953723185`
- 时间/作者: 2026-01-05 / CHENYUE
- 自动分类: 缺陷修复
- 主要文件: `vllm/tokenizers/deepseek_v32_encoding.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseek_v32_encoding.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b41aeb346` - [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261)

- 完整 hash: `b41aeb3468fecb33b7934fc7ca5406bdba84dace`
- 时间/作者: 2025-12-24 / Pleaplusone
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `369f47aa0` - [DeepSeek v3.2] Remove unnecessary syncwarps (#31047)

- 完整 hash: `369f47aa0f1c8ab8e24a13c1dde7d1626f3b940e`
- 时间/作者: 2025-12-24 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `csrc/cache_kernels.cu`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `csrc/cache_kernels.cu`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `b7b6a60ac` - Adapt the old parameter enable_thinking in chat_template_kwargs (#30852)

- 完整 hash: `b7b6a60aca0405b2d6b2ed6fd13853635f000b5d`
- 时间/作者: 2025-12-17 / 高鑫崧
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/tokenizers/deepseek_v32.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/tokenizers/deepseek_v32.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `eaa82a709` - [Bugfix][DSV32] Fix overflow in topk. (#30754)

- 完整 hash: `eaa82a709a963ab744647a701fe267223ed7b02b`
- 时间/作者: 2025-12-16 / Daniel Cámpora
- 自动分类: 缺陷修复
- 主要文件: `csrc/sampler.cu`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `csrc/sampler.cu`
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

### Commit `855b101d7` - [Frontend] add tools for dsv32 developer role (#30040)

- 完整 hash: `855b101d75d2fc1fa02a47a6fcfa4053e8541cf0`
- 时间/作者: 2025-12-15 / yjc9696
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/entrypoints/chat_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/chat_utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `a524d1ba0` - [Bugfix] Fix  deepseek_v32 tokenizer_mode  (#30658)

- 完整 hash: `a524d1ba0af49998820d81429872869c62f8585f`
- 时间/作者: 2025-12-15 / Jee Jee Li
- 自动分类: 缺陷修复
- 主要文件: `vllm/entrypoints/openai/serving_engine.py`, `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/registry.py`, `vllm/v1/structured_output/backend_xgrammar.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseek_v32.py`; `vllm/tokenizers/registry.py`; `vllm/v1/structured_output/backend_xgrammar.py`
  - runtime-model: `vllm/entrypoints/openai/serving_engine.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `39cefbdf1` - [Refactor] `TokenizerRegistry` only uses lazy imports (#30609)

- 完整 hash: `39cefbdf17e2e906e0eae3e82bd601f66137deb4`
- 时间/作者: 2025-12-13 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/test_inputs.py`, `tests/tokenizers_/test_basic.py`, `tests/tokenizers_/test_registry.py`, `vllm/entrypoints/chat_utils.py`, `vllm/tokenizers/__init__.py`, `vllm/tokenizers/deepseekv32.py`, `vllm/tokenizers/hf.py`, `vllm/tokenizers/mistral.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/__init__.py`; `vllm/tokenizers/deepseekv32.py`; `vllm/tokenizers/hf.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/async_llm.py` 等 10 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`
  - tests: `tests/test_inputs.py`; `tests/tokenizers_/test_basic.py`; `tests/tokenizers_/test_registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3e34adcdf` - [DeepSeek V3.2] Proper drop_thinking logic (#30490)

- 完整 hash: `3e34adcdfb1e3845e2fc4d0cd192d314eab516f0`
- 时间/作者: 2025-12-12 / Vladislav Nosivskoy
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/tokenizers/deepseekv32.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseekv32.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `9db78f34d` - [Bugfix] Fix the issue where DeepSeek v3.2 cannot use structured_output (#30371)

- 完整 hash: `9db78f34dce03d149f3571d45a2d2f259bdc7d15`
- 时间/作者: 2025-12-10 / Chauncey
- 自动分类: 缺陷修复
- 主要文件: `vllm/v1/structured_output/backend_xgrammar.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/structured_output/backend_xgrammar.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d007387aa` - [Bugfix] Cache added_vocab to avoid per-token overhead (#30351)

- 完整 hash: `d007387aa742c25f60d9b35bc103cbaf753114c8`
- 时间/作者: 2025-12-10 / Mingliang Li
- 自动分类: 缺陷修复
- 主要文件: `vllm/tokenizers/deepseekv32.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseekv32.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `0044c4038` - [BugFix][DeepSeek-V3.2] Fix backend selection logic for Blackwell (#30195)

- 完整 hash: `0044c4038c571e7fb38acb008256f925dfe515f1`
- 时间/作者: 2025-12-07 / Lucas Wilkinson
- 自动分类: 性能/后端优化
- 主要文件: `vllm/platforms/cuda.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/platforms/cuda.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `40a046cd8` - [Bugfix]: Fix `TokenizerLike` interface (#30009)

- 完整 hash: `40a046cd82af87e65d3be9db8bd27a4be65f1b00`
- 时间/作者: 2025-12-05 / Rohan Potdar
- 自动分类: 缺陷修复
- 主要文件: `vllm/benchmarks/datasets.py`, `vllm/benchmarks/serve.py`, `vllm/benchmarks/throughput.py`, `vllm/config/model.py`, `vllm/tokenizers/deepseekv32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py`, `vllm/tokenizers/registry.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/benchmarks/datasets.py`; `vllm/benchmarks/serve.py`; `vllm/benchmarks/throughput.py`; `vllm/tokenizers/deepseekv32.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`; `vllm/tokenizers/registry.py`
  - runtime-model: `vllm/config/model.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ffdd18111` - Add DeepSeek-V3.2 tool parser. (#29848)

- 完整 hash: `ffdd18111b767d271786b982378d51b51ce151fe`
- 时间/作者: 2025-12-04 / Xu Wenqing
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv32_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/__init__.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv32_tool_parser.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `82a64b3d8` - [Bugfix] fixed deepseekv32 tool calling error (#30025)

- 完整 hash: `82a64b3d8f93521d39569078d4ac56992a50a640`
- 时间/作者: 2025-12-04 / Chauncey
- 自动分类: 缺陷修复
- 主要文件: `vllm/tokenizers/deepseek_v32_encoding.py`, `vllm/tokenizers/deepseekv32.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/deepseek_v32_encoding.py`; `vllm/tokenizers/deepseekv32.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ac1886588` - [CI] Fix re import error (#29973)

- 完整 hash: `ac1886588fd8799ff874b860b6c266a84d5a2b2b`
- 时间/作者: 2025-12-03 / Wentao Ye
- 自动分类: 缺陷修复
- 主要文件: `.buildkite/scripts/generate-nightly-index.py`, `vllm/entrypoints/serve/instrumentator/metrics.py`, `vllm/tokenizers/deepseek_v32_encoding.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/scripts/generate-nightly-index.py`
  - other: `vllm/tokenizers/deepseek_v32_encoding.py`
  - runtime-model: `vllm/entrypoints/serve/instrumentator/metrics.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b78772c43` - [Frontend] supports deepseekv32 chat template (#29837)

- 完整 hash: `b78772c433515a22bfeeaea41f3524002609e264`
- 时间/作者: 2025-12-03 / Chauncey
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/config/model.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/tokenizers/__init__.py`, `vllm/tokenizers/deepseek_v32_encoding.py`, `vllm/tokenizers/deepseekv32.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tokenizers/__init__.py`; `vllm/tokenizers/deepseek_v32_encoding.py`; `vllm/tokenizers/deepseekv32.py`
  - runtime-model: `vllm/config/model.py`; `vllm/entrypoints/openai/serving_engine.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `ba7bcccdd` - add VLLM_USE_V32_ENCODE to use encoding_dsv32.py

- 完整 hash: `ba7bcccddd7de2568adb73769df0091d8a27bb1d`
- 时间/作者: 2025-12-02 / zhuwenwen
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/entrypoints/chat_utils.py`, `vllm/entrypoints/encoding_dsv32.py`, `vllm/envs.py`, `vllm/model_executor/model_loader/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/encoding_dsv32.py`; `vllm/model_executor/model_loader/utils.py`
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
