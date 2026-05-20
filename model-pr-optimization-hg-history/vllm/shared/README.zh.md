# vllm Shared Framework Commits 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `.clang-format` | 无直接提交 |
| `.coveragerc` | 无直接提交 |
| `.dockerignore` | 无直接提交 |
| `.git-blame-ignore-revs` | 无直接提交 |
| `.github/.bc-linter.yml` | 无直接提交 |
| `.github/CODEOWNERS` | 无直接提交 |
| `.github/FUNDING.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/100-documentation.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/200-installation.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/300-usage.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/400-bug-report.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/450-ci-failure.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/500-feature-request.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/600-new-model.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/700-performance-discussion.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/750-RFC.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/config.yml` | 无直接提交 |
| `.github/PULL_REQUEST_TEMPLATE.md` | 无直接提交 |
| `.github/dependabot.yml` | 无直接提交 |
| `.github/mergify.yml` | 无直接提交 |
| `.github/scale-config.yml` | 无直接提交 |
| `.github/scripts/cleanup_pr_body.sh` | 无直接提交 |
| `.github/workflows/add_label_automerge.yml` | 无直接提交 |
| `.github/workflows/bc-lint.yml` | 无直接提交 |
| `.github/workflows/cleanup_pr_body.yml` | 无直接提交 |
| `.github/workflows/issue_autolabel.yml` | 无直接提交 |
| `.github/workflows/macos-smoke-test.yml` | 无直接提交 |
| `.github/workflows/matchers/actionlint.json` | 无直接提交 |
| `.github/workflows/matchers/markdownlint.json` | 无直接提交 |
| `.github/workflows/matchers/mypy.json` | 无直接提交 |
| `.github/workflows/pre-commit.yml` | 无直接提交 |
| `.github/workflows/reminder_comment.yml` | 无直接提交 |
| `.github/workflows/scripts/build.sh` | 无直接提交 |
| `.github/workflows/scripts/create_release.js` | 无直接提交 |
| `.github/workflows/scripts/cuda-install.sh` | 无直接提交 |
| `.github/workflows/scripts/env.sh` | 无直接提交 |
| `.github/workflows/scripts/pytorch-install.sh` | 无直接提交 |
| `.github/workflows/stale.yml` | 无直接提交 |
| `.gitignore` | 无直接提交 |
| `.markdownlint.yaml` | 无直接提交 |
| `.pre-commit-config.yaml` | 无直接提交 |
| `.readthedocs.yaml` | 无直接提交 |
| `.shellcheckrc` | 无直接提交 |
| `.yapfignore` | 无直接提交 |
| `CMakeLists.txt` | 无直接提交 |
| `CODE_OF_CONDUCT.md` | 无直接提交 |
| `CONTRIBUTING.md` | 无直接提交 |
| `DCO` | 无直接提交 |
| `LICENSE` | 无直接提交 |
| `MANIFEST.in` | 无直接提交 |
| `README.md` | `9d6664d2a` |
| `README_ORIGIN.md` | 无直接提交 |
| `RELEASE.md` | 无直接提交 |
| `SECURITY.md` | 无直接提交 |
| `benchmarks/README.md` | 无直接提交 |
| `benchmarks/auto_tune/README.md` | 无直接提交 |
| `benchmarks/auto_tune/auto_tune.sh` | 无直接提交 |
| `benchmarks/auto_tune/batch_auto_tune.sh` | 无直接提交 |
| `benchmarks/backend_request_func.py` | 无直接提交 |
| `benchmarks/benchmark_batch_invariance.py` | 无直接提交 |
| `benchmarks/benchmark_block_pool.py` | 无直接提交 |
| `benchmarks/benchmark_hash.py` | 无直接提交 |
| `benchmarks/benchmark_latency.py` | 无直接提交 |
| `benchmarks/benchmark_long_document_qa_throughput.py` | 无直接提交 |
| `benchmarks/benchmark_ngram_proposer.py` | 无直接提交 |
| `benchmarks/benchmark_prefix_block_hash.py` | 无直接提交 |
| `benchmarks/benchmark_prefix_caching.py` | 无直接提交 |
| `benchmarks/benchmark_prioritization.py` | 无直接提交 |
| `benchmarks/benchmark_serving.py` | 无直接提交 |
| `benchmarks/benchmark_serving_structured_output.py` | 无直接提交 |
| `benchmarks/benchmark_throughput.py` | 无直接提交 |
| `benchmarks/benchmark_utils.py` | 无直接提交 |
| `benchmarks/cutlass_benchmarks/sparse_benchmarks.py` | 无直接提交 |
| `benchmarks/cutlass_benchmarks/utils.py` | 无直接提交 |
| `benchmarks/cutlass_benchmarks/w8a8_benchmarks.py` | 无直接提交 |
| `benchmarks/cutlass_benchmarks/weight_shapes.py` | 无直接提交 |
| `benchmarks/disagg_benchmarks/disagg_overhead_benchmark.sh` | 无直接提交 |
| `benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh` | 无直接提交 |
| `benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py` | 无直接提交 |
| `benchmarks/disagg_benchmarks/rate_limiter.py` | 无直接提交 |
| ... | 3387 more files omitted from table; all were used for git tracing. |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 80
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-15 | `dc35ab65a` | 缺陷修复 | [PD][Bugfix] 修复scheduler修改影响其他connector | `vllm/v1/core/sched/scheduler.py` |
| 2026-05-14 | `b64d13e19` | 性能/后端优化 | [BUGFIX] 修复w4a8模型权重加载函数没有返回值 | `vllm/model_executor/layers/quantization/utils/w4a8_utils.py` |
| 2026-05-13 | `d04600507` | 缺陷修复 | [BUGFIX] Deepseek r1 修复启动服务有问题 | `vllm/_custom_ops.py` |
| 2026-05-13 | `c9393c10a` | 缺陷修复 | Revert "修复fp8起服务报错" | `vllm/_custom_ops.py` |
| 2026-05-13 | `834bcbe77` | 缺陷修复 | 修复fp8起服务报错 | `vllm/_custom_ops.py` |
| 2026-05-13 | `d7c548be8` | 缺陷修复 | [BUGFIX] Qwen2.5-VL-72B-Instruct修复 fp8 KV cache 模式下 torch.compile 编译崩溃 | `vllm/attention/layer.py` |
| 2026-05-09 | `9d6664d2a` | 通用实现调整 | [ FEATURE ] Merge tencent commit to improve build process | `README.md`, `requirements/hygon.txt`, `setup.py` |
| 2026-05-08 | `72d4617dc` | 性能/后端优化 | [BugFix] Import the aiter package directly by default. | `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-05-08 | `ce26d09cd` | 性能/后端优化 | [BugFix] Add a check to handle the case where num_dispatchers is NULL | `vllm/model_executor/layers/fused_moe/modular_kernel.py` |
| 2026-05-06 | `bad9931de` | 性能/后端优化 | [Feature]w8a8量化模型默认不开启aiter | `vllm/envs.py` |
| 2026-05-03 | `dc4cab3e8` | 性能/后端优化 | [FEATURE] 更新deepgem包并更新权重重排函数 | `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py` |
| 2026-04-24 | `ca9ce18d9` | 性能/后端优化 | [FEATURE]:support w4a16 aiter moe | `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` |
| 2026-04-24 | `e7dee10f5` | 性能/后端优化 | [Feature]: 新增w4a8的moe-aiter算子的支持，采用VLLM_ROCM_USE_AITER_MOE环境变量控制，默认关闭，打开后会走到aiter的w4a8 moe的算子。 | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-04-23 | `d49bafc5d` | 性能/后端优化 | [FEATURE] 接入Aiter MoE W8A8-Int8 量化模型支持 | `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-04-23 | `753b29c08` | 性能/后端优化 | [bugfix][fp8]Enable torch.compile for quant_fp8. | `vllm/_custom_ops.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py` |
| 2026-04-23 | `2444e959a` | 性能/后端优化 | [FEATRUE] 接入Aiter MoE W8A8-FP8 量化模型支持 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-04-22 | `c18194543` | 性能/后端优化 | [feature] support online fp8 quant by ptpc_fp8. | `csrc/ops.h`, `csrc/torch_bindings.cpp`, `vllm/_custom_ops.py` |
| 2026-04-18 | `e375aa36f` | 调度/缓存/PD | [DOCs] add vllm v0.15.1 dcu use readme.md file including introduction, supported models, installation, PD, and EP usage | `docs/README_VLLM_DCU.md` |
| 2026-04-18 | `f90d9d076` | 调度/缓存/PD | [DOC] add vllm v0.15.1 dcu use readme.md file including introduction, supported models, installation, PD, and EP usage | `docs/README_VLLM_DCU.md` |
| 2026-04-18 | `4fca01b87` | 性能/后端优化 | [Perf]优化EP低延迟模式下调度，消除调度空泡 | `vllm/forward_context.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize.py` |
| 2026-04-17 | `8c96d505a` | 性能/后端优化 | [Perf]支持DSA架构模型开启MTP后运行full graph模式 | `vllm/v1/attention/backends/mla/indexer.py` |
| 2026-04-15 | `fbfe20c62` | 缺陷修复 | [DSA][BUGFIX]: 解决mqa_logits导致的oom问题 | `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-04-11 | `3842b3169` | 性能/后端优化 | [FEATURE] 接入 LightOP 的 silu_and_mul 自定义算子并统一 OPT 路径 | `vllm/_custom_ops.py`, `vllm/model_executor/layers/activation.py` |
| 2026-04-10 | `61ba33d58` | 调度/缓存/PD | [PD][Feat]支持pd分离dp并行 | `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_dp.py`, `vllm/distributed/kv_transfer/kv_connector/factory.py`, `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector_dp.py` |
| 2026-04-03 | `ce47a56ea` | 模型支持/运行时入口 | 更新 vllm/model_executor/layers/layernorm.py, vllm/_custom_ops.py | `vllm/_custom_ops.py`, `vllm/model_executor/layers/layernorm.py` |
| 2026-04-02 | `15883da4d` | 性能/后端优化 | fused_add_rms_norm use lightop | `vllm/model_executor/layers/layernorm.py` |
| 2026-04-03 | `456e8c109` | 性能/后端优化 | [BUGFIX] mrope 二维表示情况下，在dcu上kernel无法提前下发 | `vllm/v1/worker/gpu_model_runner.py` |
| 2026-04-03 | `b233584aa` | 性能/后端优化 | [BUGFIX] 回退 ROCm FlashAttention unified KV layout 改动并修正 unified kernel 选择逻辑 | `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/platforms/rocm.py` |
| 2026-04-02 | `9eff7ac1a` | 缺陷修复 | [PD][BugFix]修复PD中的spec decoding的kv传输问题 | `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_mult_mac.py`, `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_engine.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-04-01 | `b281794ed` | 性能/后端优化 | [BUGFIX] 修复 fused MoE modular kernel 路径中 shared_output 和 routed_scaling_factor 透传不完整的问题 | `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` |
| 2026-04-01 | `676545b9f` | 性能/后端优化 | [Perf]消除indexer build时隐式同步导致的调度空泡 | `vllm/v1/attention/backends/mla/indexer.py` |
| 2026-03-27 | `ca158ae99` | 性能/后端优化 | fix get config assert error | `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-03-27 | `6adf9d12c` | 性能/后端优化 | use tunning w4a16 moe | `vllm/model_executor/layers/fused_moe/fused_moe.py` |
| 2026-03-26 | `ee989f6dd` | 性能/后端优化 | refactor(rocm): 提取 unified flash 的 block_size 判定逻辑 | `vllm/platforms/rocm.py` |
| 2026-03-23 | `ea9b8584b` | 性能/后端优化 | feat(v1 attention): 为 ROCm FlashAttention 接入 unified kv layout，并打通 mm_prefix、qq_bias 与 use_alibi_sqrt 透传 在 ROCm FlashAttention 后端增加 unified KV layout 选择逻辑 接入 unified varlen kernel 调用路径 在 FlashAttention metadata 中补充 mm_prefix_range 与 qq_bias 透传 | `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/platforms/rocm.py` |
| 2026-03-26 | `712760431` | 性能/后端优化 | convert_req_index_to_global_index opt | `vllm/v1/attention/backends/mla/flashmla_sparse.py` |
| 2026-03-26 | `a0ac95b09` | 性能/后端优化 | per_token_group_quant_fp8 opt | `vllm/model_executor/layers/quantization/utils/fp8_utils.py` |
| 2026-03-26 | `cb68935ca` | 性能/后端优化 | topk opt | `vllm/envs.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-26 | `707b48918` | 通用实现调整 | The gfx928 architecture force to set VLLM_W8A8_BACKEND == 1 | `vllm/envs.py` |
| 2026-03-24 | `442abc674` | 调度/缓存/PD | 支持kvacache fp8_e4m3/fp8_e5m2 支持kvacache fp8_e4m3/fp8_e5m2的RMS_ROPE_CONCAT | `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-03-24 | `c07d92530` | 模型支持/运行时入口 | 补充1d_mrope | `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-24 | `6ef5d3226` | 性能/后端优化 | fix(moe): 补齐非Marlin量化路径 shared_output/routed_scaling_factor 透传 | `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/fp8.py` |
| 2026-03-24 | `beae085a7` | 性能/后端优化 | 处理VLLM_USE_LIGHTOP_MOE_SUM_MUL_ADD导致的awq推理bug问题 | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/moe_wna16.py` |
| 2026-03-24 | `2d940766a` | 调度/缓存/PD | VLLM_ENCODER_CACHE_SIZE控制encoder_cache_size大小 | `vllm/envs.py`, `vllm/v1/core/encoder_cache_manager.py` |
| 2026-03-24 | `0e5a20b3b` | 调度/缓存/PD | 支持kvacache fp8_e4m3/fp8_e5m2 支持kvacache fp8_e4m3/fp8_e5m2的RMS_ROPE_CONCAT | `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/mla.py` |
| 2026-03-23 | `2799cc7ad` | 模型支持/运行时入口 | 删除1d_mrope | `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-21 | `53889c8ba` | 缺陷修复 | 修复get_gcn_arch_name的导入bug | `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-21 | `7c8db5e76` | 缺陷修复 | 修复get_gcn_arch_name的导入bug | `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-21 | `c6a45c08e` | 性能/后端优化 | 关闭sparse_mla的num_head到64/128的pad，以及添加控制fp8_use_mixed_batch模式的环境变量控制，FP8_USE_MIXED_BATCH，默认为false，为分离模式 | `vllm/envs.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py` |
| 2026-03-21 | `256749c92` | 性能/后端优化 | feat:flash_mla，q去掉pad | `vllm/v1/attention/backends/mla/flashmla_sparse.py` |
| 2026-03-21 | `656944ac0` | 性能/后端优化 | 增加triton的indexer的kcahche读写操作 | `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py` |
| 2026-03-21 | `7eb2446c8` | 性能/后端优化 | [perf]DSA架构模型支持mtp>1 | `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/spec_decode/eagle.py` |
| 2026-03-20 | `839dc88e8` | 性能/后端优化 | fix(moe): 仅在 fused moe_sum+mul+add 开启时透传 shared_output | `vllm/model_executor/layers/fused_moe/layer.py` |
| 2026-03-19 | `44d4976da` | 缺陷修复 | [fix]修复GLM mtp精度问题 | `vllm/v1/spec_decode/eagle.py` |
| 2026-03-18 | `c1cd53346` | 通用实现调整 | _custom_op文件有个if没删除 | `vllm/_custom_ops.py` |
| 2026-03-18 | `b5323d90e` | 模型支持/运行时入口 | feat:支持mqa的fp8实现 | `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-17 | `81077e8dd` | 性能/后端优化 | [perf]默认使用full graph | `vllm/envs.py` |
| 2026-03-17 | `46ab154b7` | 性能/后端优化 | [perf]消除sparse mla build时的拷贝调度空泡 | `vllm/v1/attention/backends/mla/flashmla_sparse.py` |
| 2026-03-17 | `3c900b767` | 模型支持/运行时入口 | add fa unified attn 导入判断 | `vllm/v1/attention/ops/triton_unified_attention.py` |
| 2026-03-16 | `f9a04c974` | 性能/后端优化 | fix: resolve block_shape conflicts between DeepEP MoE and non-DeepEP quantization | `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-16 | `be81eaf61` | 调度/缓存/PD | [PD]添加VLLM_PP_LAYER_PARTITION_D控制d层切分 | `vllm/envs.py` |
| 2026-03-16 | `0c5e5f884` | 缺陷修复 | [PD][Bugfix]修复0151pd分离d卡住问题 | `vllm/envs.py`, `vllm/v1/engine/input_processor.py` |
| 2026-03-16 | `2ce7c0964` | 缺陷修复 | [PD][Fixbug]修复CachedRequestData结构体升级找不到resumed_req_ids变量 | `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py` |
| 2026-03-16 | `55c719cb0` | 模型支持/运行时入口 | [feat]支持ray分布式异步调度，VLLM_ENABLE_RAY_ASYNC_SCHEDULING环境变量控制 | `vllm/config/vllm.py`, `vllm/envs.py`, `vllm/v1/executor/ray_executor.py` |
| 2026-03-13 | `9404668aa` | 性能/后端优化 | rms_norm_opt精度问题解决 | `vllm/_custom_ops.py`, `vllm/model_executor/layers/layernorm.py` |
| 2026-03-13 | `8e726b3f9` | 性能/后端优化 | fix: 修复MOE量化tensor对于其他模型的影响 | `vllm/model_executor/layers/fused_moe/layer.py` |
| 2026-03-13 | `7cec75a7e` | 性能/后端优化 | 修改sparse_attn hip后端 | `vllm/model_executor/custom_op.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-12 | `25a9d4b33` | 性能/后端优化 | [fix]添加VLLM_USE_LIGHTOP_FUSED_TOPP_TOPK控制lightop topp_topk融合算子开关 | `vllm/envs.py` |
| 2026-03-12 | `55a9f930b` | 缺陷修复 | [fix]添加VLLM_USE_LIGHTOP控制lightop topp_topk融合算子开关 | `vllm/v1/sample/ops/topk_topp_sampler.py` |
| 2026-03-12 | `3946292af` | 缺陷修复 | [fix]添加VLLM_USE_LIGHTOP控制lightop topp_topk融合算子开关 | `vllm/v1/sample/ops/topk_topp_sampler.py` |
| 2026-03-12 | `9aabf7e76` | 性能/后端优化 | feat(deepseek-mla):: 精简 fused RMS-RoPE concat 可用性判断 | `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-03-10 | `cae53e46b` | 性能/后端优化 | feat(deepseek-mla): 接入 VLLM_USE_LIGHTOP_RMS_ROPE_CONCAT 融合链路 新增环境变量与 MLA 融合接线（wrapper -> attention -> impl） 接入 lightop fused_rms_norm_rope_contiguous，保留回退路径 | `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-03-09 | `706c031cf` | 性能/后端优化 | moe: 补齐 fill+moe_align 融合开关语义 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`, `vllm/model_executor/model_loader/utils.py` |
| 2026-03-12 | `1b71f5221` | 性能/后端优化 | 增加max_cudagraph_capture_size | `vllm/config/vllm.py`, `vllm/envs.py` |
| 2026-03-12 | `8bf99b0b8` | 缺陷修复 | fix: fix bug http://hpczentao.sugon.com/bug-view-118388.html | `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-03-12 | `6ca1362bd` | 性能/后端优化 | perf: DS v2增加DTBMM融合,默认关闭 | `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-03-12 | `6b03cfdbd` | 模型支持/运行时入口 | 补充mrope创建部分 | `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-12 | `fb445ddee` | 模型支持/运行时入口 | 误删函数恢复 | `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-12 | `ef7e12146` | 模型支持/运行时入口 | mrope_1d修改 | `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-03-07 | `ee355d86e` | 性能/后端优化 | mla: 恢复 opt-cat 在 prefill 和 decode 的拼接路由 | `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/flashmla.py` |

## 逐 Commit 审计卡

### Commit `dc35ab65a` - [PD][Bugfix] 修复scheduler修改影响其他connector

- 完整 hash: `dc35ab65ae36b0b60d68500958c72ac89f84a95a`
- 时间/作者: 2026-05-15 / xuxz
- 自动分类: 缺陷修复
- 主要文件: `vllm/v1/core/sched/scheduler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/core/sched/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b64d13e19` - [BUGFIX] 修复w4a8模型权重加载函数没有返回值

- 完整 hash: `b64d13e1978e38a55e7392bf5b234df6891967b7`
- 时间/作者: 2026-05-14 / chenhw5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/utils/w4a8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/w4a8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d04600507` - [BUGFIX] Deepseek r1 修复启动服务有问题

- 完整 hash: `d04600507907146c0520c2631a5ad0b50c6df2f3`
- 时间/作者: 2026-05-13 / zhangzbb
- 自动分类: 缺陷修复
- 主要文件: `vllm/_custom_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c9393c10a` - Revert "修复fp8起服务报错"

- 完整 hash: `c9393c10a37694d3eb8f90fdbb8407af5290cad6`
- 时间/作者: 2026-05-13 / zhangzbb
- 自动分类: 缺陷修复
- 主要文件: `vllm/_custom_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `834bcbe77` - 修复fp8起服务报错

- 完整 hash: `834bcbe774118a25ac383835fc3f1e938b8bd249`
- 时间/作者: 2026-05-13 / jujil
- 自动分类: 缺陷修复
- 主要文件: `vllm/_custom_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d7c548be8` - [BUGFIX] Qwen2.5-VL-72B-Instruct修复 fp8 KV cache 模式下 torch.compile 编译崩溃

- 完整 hash: `d7c548be8ee969af13c0ee05073361497119cf67`
- 时间/作者: 2026-05-13 / laibao
- 自动分类: 缺陷修复
- 主要文件: `vllm/attention/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/attention/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9d6664d2a` - [ FEATURE ] Merge tencent commit to improve build process

- 完整 hash: `9d6664d2aa617ce7ecfad76838c663a7d5432930`
- 时间/作者: 2026-05-09 / zhangyh15
- 自动分类: 通用实现调整
- 主要文件: `README.md`, `requirements/hygon.txt`, `setup.py`, `vllm/entrypoints/logger.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/completion/serving.py`, `vllm/entrypoints/openai/engine/serving.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README.md`; `requirements/hygon.txt`; `setup.py`
  - runtime-model: `vllm/entrypoints/logger.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/completion/serving.py`; `vllm/entrypoints/openai/engine/serving.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `72d4617dc` - [BugFix] Import the aiter package directly by default.

- 完整 hash: `72d4617dcd84d171ab546557d8e63d37b57d5ab2`
- 时间/作者: 2026-05-08 / zhenggf
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ce26d09cd` - [BugFix] Add a check to handle the case where num_dispatchers is NULL

- 完整 hash: `ce26d09cd1c072ebd4f25e10574ed4030256f727`
- 时间/作者: 2026-05-08 / zhenggf
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/modular_kernel.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/modular_kernel.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bad9931de` - [Feature]w8a8量化模型默认不开启aiter

- 完整 hash: `bad9931de5f175567a4d12566e567b5c7a9fabdb`
- 时间/作者: 2026-05-06 / fanth
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `dc4cab3e8` - [FEATURE] 更新deepgem包并更新权重重排函数

- 完整 hash: `dc4cab3e80ed8fbf5f5aa5bd74c1470eff442cb2`
- 时间/作者: 2026-05-03 / chenhw5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ca9ce18d9` - [FEATURE]:support w4a16 aiter moe

- 完整 hash: `ca9ce18d97b71227d7f52ba6c7f23d580cf18282`
- 时间/作者: 2026-04-24 / wangaq
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e7dee10f5` - [Feature]: 新增w4a8的moe-aiter算子的支持，采用VLLM_ROCM_USE_AITER_MOE环境变量控制，默认关闭，打开后会走到aiter的w4a8 moe的算子。

- 完整 hash: `e7dee10f5b460a8fde06297e19d008ce9c8bc3a1`
- 时间/作者: 2026-04-24 / yangql1
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/slimquant_w4a8.py`; `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d49bafc5d` - [FEATURE] 接入Aiter MoE W8A8-Int8 量化模型支持

- 完整 hash: `d49bafc5d90fa537e0a68e9acc8f63c33adb5ffe`
- 时间/作者: 2026-04-23 / lixh6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `753b29c08` - [bugfix][fp8]Enable torch.compile for quant_fp8.

- 完整 hash: `753b29c08c6e7874f81b93703b256968b3f43a0c`
- 时间/作者: 2026-04-23 / Song Zhao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_custom_ops.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/input_quant_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2444e959a` - [FEATRUE] 接入Aiter MoE W8A8-FP8 量化模型支持

- 完整 hash: `2444e959ae1b95e1bf7a98e5d9e17dfe9ded4583`
- 时间/作者: 2026-04-23 / lixh6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c18194543` - [feature] support online fp8 quant by ptpc_fp8.

- 完整 hash: `c181945433a6b794e70dfdc0c528c1f6dc2ce8f2`
- 时间/作者: 2026-04-22 / zhaosong
- 自动分类: 性能/后端优化
- 主要文件: `csrc/ops.h`, `csrc/torch_bindings.cpp`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/quantization/__init__.py`, `vllm/model_executor/layers/quantization/ptpc_fp8.py`, `vllm/version.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `csrc/ops.h`; `csrc/torch_bindings.cpp`; `vllm/_custom_ops.py`; `vllm/version.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/__init__.py`; `vllm/model_executor/layers/quantization/ptpc_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e375aa36f` - [DOCs] add vllm v0.15.1 dcu use readme.md file including  introduction, supported models, installation, PD, and EP usage

- 完整 hash: `e375aa36fcaecb228e7027a0c9e1d4f9edc9458d`
- 时间/作者: 2026-04-18 / bin zhang
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/README_VLLM_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/README_VLLM_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `f90d9d076` - [DOC] add vllm v0.15.1 dcu use readme.md file including  introduction, supported models, installation, PD, and EP usage

- 完整 hash: `f90d9d07636a81040f19655f7e725964dd0b3c14`
- 时间/作者: 2026-04-18 / bin zhang
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/README_VLLM_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/README_VLLM_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `4fca01b87` - [Perf]优化EP低延迟模式下调度，消除调度空泡

- 完整 hash: `4fca01b87427ccac1fc572be45d1c3753c6380f7`
- 时间/作者: 2026-04-18 / wangmin6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/forward_context.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py`, `vllm/v1/worker/dp_utils.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/forward_context.py`
  - runtime-model: `vllm/v1/worker/dp_utils.py`; `vllm/v1/worker/gpu_model_runner.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/modular_kernel.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8c96d505a` - [Perf]支持DSA架构模型开启MTP后运行full graph模式

- 完整 hash: `8c96d505ae9a354c7c889bc8ab711a186ae1a4e0`
- 时间/作者: 2026-04-17 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/attention/backends/mla/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/backends/mla/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fbfe20c62` - [DSA][BUGFIX]: 解决mqa_logits导致的oom问题

- 完整 hash: `fbfe20c62ce5efe1f26a96cbd2cf28ed49b6282e`
- 时间/作者: 2026-04-15 / wanghl6
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3842b3169` - [FEATURE] 接入 LightOP 的 silu_and_mul 自定义算子并统一 OPT 路径

- 完整 hash: `3842b316979a3ca0c56ceecb7d0faf7262653950`
- 时间/作者: 2026-04-11 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_custom_ops.py`, `vllm/model_executor/layers/activation.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/layers/activation.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `61ba33d58` - [PD][Feat]支持pd分离dp并行

- 完整 hash: `61ba33d5802363c09f0acab9e14b7f73abb414c4`
- 时间/作者: 2026-04-10 / xuxz
- 自动分类: 调度/缓存/PD
- 主要文件: `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_dp.py`, `vllm/distributed/kv_transfer/kv_connector/factory.py`, `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector_dp.py`, `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_engine_dp.py`, `vllm/envs.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/core.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_dp.py`
  - other: `vllm/envs.py`; `vllm/v1/engine/core.py`
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/factory.py`; `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector_dp.py`; `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_engine_dp.py`; `vllm/v1/core/sched/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ce47a56ea` - 更新 vllm/model_executor/layers/layernorm.py, vllm/_custom_ops.py

- 完整 hash: `ce47a56ea58791ee23e4abaa8e305c3c0ab0fdc5`
- 时间/作者: 2026-04-03 / yangyn1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/_custom_ops.py`, `vllm/model_executor/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `15883da4d` - fused_add_rms_norm use lightop

- 完整 hash: `15883da4d4d3eab250f9061a535e7d8f7142f560`
- 时间/作者: 2026-04-02 / fanwl
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `456e8c109` - [BUGFIX] mrope 二维表示情况下，在dcu上kernel无法提前下发

- 完整 hash: `456e8c1090b264565a32e4ea6e5d5fdaa0ca0dc7`
- 时间/作者: 2026-04-03 / guanyu1
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b233584aa` - [BUGFIX] 回退 ROCm FlashAttention unified KV layout 改动并修正 unified kernel 选择逻辑

- 完整 hash: `b233584aaf2c4a950afae0360f6a2e969cdcd496`
- 时间/作者: 2026-04-03 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`, `vllm/v1/attention/selector.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backend.py`; `vllm/v1/attention/backends/flash_attn.py`; `vllm/v1/attention/ops/triton_unified_attention.py`; `vllm/v1/attention/selector.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9eff7ac1a` - [PD][BugFix]修复PD中的spec decoding的kv传输问题

- 完整 hash: `9eff7ac1aa9f0927e6471416f3aaaaa0fdc4c1f7`
- 时间/作者: 2026-04-02 / xuxz
- 自动分类: 缺陷修复
- 主要文件: `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_mult_mac.py`, `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_engine.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/kv_connector_model_runner_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd_mult_mac.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/kv_connector_model_runner_mixin.py`
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_engine.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b281794ed` - [BUGFIX] 修复 fused MoE modular kernel 路径中 shared_output 和 routed_scaling_factor 透传不完整的问题

- 完整 hash: `b281794ede3858848aabfcfa4f1184cee349bf33`
- 时间/作者: 2026-04-01 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/modular_kernel.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `676545b9f` - [Perf]消除indexer build时隐式同步导致的调度空泡

- 完整 hash: `676545b9f3abe8f570866665a617f3649263596e`
- 时间/作者: 2026-04-01 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/attention/backends/mla/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/backends/mla/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ca158ae99` - fix get config assert error

- 完整 hash: `ca158ae997345ed545103836fada67a3c3cde0e1`
- 时间/作者: 2026-03-27 / wangaq
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6adf9d12c` - use tunning w4a16 moe

- 完整 hash: `6adf9d12cd5bd58fa456892f9caa4a8a081bcb2d`
- 时间/作者: 2026-03-27 / wangaq
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ee989f6dd` - refactor(rocm): 提取 unified flash 的 block_size 判定逻辑

- 完整 hash: `ee989f6dd0932c3aa781f977cc20e6c8cb0ddecc`
- 时间/作者: 2026-03-26 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/platforms/rocm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/platforms/rocm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ea9b8584b` - feat(v1 attention): 为 ROCm FlashAttention 接入 unified kv layout，并打通 mm_prefix、qq_bias 与 use_alibi_sqrt 透传 在 ROCm FlashAttention 后端增加 unified KV layout 选择逻辑 接入 unified varlen kernel 调用路径 在 FlashAttention metadata 中补充 mm_prefix_range 与 qq_bias 透传

- 完整 hash: `ea9b8584bcd925f1fc7fc9dc2f480b0f5febfdb7`
- 时间/作者: 2026-03-23 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`, `vllm/v1/attention/selector.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backend.py`; `vllm/v1/attention/backends/flash_attn.py`; `vllm/v1/attention/ops/triton_unified_attention.py`; `vllm/v1/attention/selector.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `712760431` - convert_req_index_to_global_index opt

- 完整 hash: `712760431d9a20dbdd430dcebbf45f96116411a0`
- 时间/作者: 2026-03-26 / wanghl6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a0ac95b09` - per_token_group_quant_fp8 opt

- 完整 hash: `a0ac95b09256ac760969bc408d6c98b165918f12`
- 时间/作者: 2026-03-26 / wanghl6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cb68935ca` - topk opt

- 完整 hash: `cb68935ca4295d1c266ef805717ae7db1653c1a4`
- 时间/作者: 2026-03-26 / wanghl6
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `707b48918` - The gfx928 architecture force to set VLLM_W8A8_BACKEND == 1

- 完整 hash: `707b48918790d92edc15ba8518c525d33cd84915`
- 时间/作者: 2026-03-26 / wanglong3
- 自动分类: 通用实现调整
- 主要文件: `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `442abc674` - 支持kvacache fp8_e4m3/fp8_e5m2 支持kvacache fp8_e4m3/fp8_e5m2的RMS_ROPE_CONCAT

- 完整 hash: `442abc674a24df3054d425ace17a11ba77dab823`
- 时间/作者: 2026-03-24 / xiabo
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c07d92530` - 补充1d_mrope

- 完整 hash: `c07d92530a7c5212261099de4970e8defef94e32`
- 时间/作者: 2026-03-24 / guanyu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `6ef5d3226` - fix(moe): 补齐非Marlin量化路径 shared_output/routed_scaling_factor 透传

- 完整 hash: `6ef5d3226b8b25973298b52ad765c8a668c87ee4`
- 时间/作者: 2026-03-24 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `beae085a7` - 处理VLLM_USE_LIGHTOP_MOE_SUM_MUL_ADD导致的awq推理bug问题

- 完整 hash: `beae085a7b8281d828f1cfb6cfeb4506a9d0cc91`
- 时间/作者: 2026-03-24 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/moe_wna16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2d940766a` - VLLM_ENCODER_CACHE_SIZE控制encoder_cache_size大小

- 完整 hash: `2d940766aedf46428de8d3d2268d1f56ad75cfcc`
- 时间/作者: 2026-03-24 / guanyu1
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/envs.py`, `vllm/v1/core/encoder_cache_manager.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/v1/core/encoder_cache_manager.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0e5a20b3b` - 支持kvacache fp8_e4m3/fp8_e5m2 支持kvacache fp8_e4m3/fp8_e5m2的RMS_ROPE_CONCAT

- 完整 hash: `0e5a20b3b82938b6d4007c7704795d812741e951`
- 时间/作者: 2026-03-24 / xiabo
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/mla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/mla.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2799cc7ad` - 删除1d_mrope

- 完整 hash: `2799cc7adbcee9801834a5166527b0cc0627a399`
- 时间/作者: 2026-03-23 / guanyu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `53889c8ba` - 修复get_gcn_arch_name的导入bug

- 完整 hash: `53889c8baec8c64b40d92bf98c2718e132628885`
- 时间/作者: 2026-03-21 / yangql
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `7c8db5e76` - 修复get_gcn_arch_name的导入bug

- 完整 hash: `7c8db5e7695e6b9bb5c5d6f41d115b9202fc7fe9`
- 时间/作者: 2026-03-21 / yangql
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c6a45c08e` - 关闭sparse_mla的num_head到64/128的pad，以及添加控制fp8_use_mixed_batch模式的环境变量控制，FP8_USE_MIXED_BATCH，默认为false，为分离模式

- 完整 hash: `c6a45c08e34a8aa53c31d842ee7baf7e0fa2635a`
- 时间/作者: 2026-03-21 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `256749c92` - feat:flash_mla，q去掉pad

- 完整 hash: `256749c923b605346918f514c802cb3e096e143b`
- 时间/作者: 2026-03-21 / liuchy5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `656944ac0` - 增加triton的indexer的kcahche读写操作

- 完整 hash: `656944ac0f95baf8b45978c3a68ed8ebfd49a920`
- 时间/作者: 2026-03-21 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
  - runtime-perf: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7eb2446c8` - [perf]DSA架构模型支持mtp>1

- 完整 hash: `7eb2446c83014eb20b282ca8c3b1e11364946d4d`
- 时间/作者: 2026-03-21 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/spec_decode/eagle.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
  - runtime-perf: `vllm/v1/attention/backends/mla/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `839dc88e8` - fix(moe): 仅在 fused moe_sum+mul+add 开启时透传 shared_output

- 完整 hash: `839dc88e826aa9b62615077fe1f2b2fb75235cdb`
- 时间/作者: 2026-03-20 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `44d4976da` - [fix]修复GLM mtp精度问题

- 完整 hash: `44d4976daee3cba0f30a1e04b9a5100b5c7c4e52`
- 时间/作者: 2026-03-19 / 王敏
- 自动分类: 缺陷修复
- 主要文件: `vllm/v1/spec_decode/eagle.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/spec_decode/eagle.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c1cd53346` - _custom_op文件有个if没删除

- 完整 hash: `c1cd53346d71ae33c2bc6fbbce7d4c6fb50fe691`
- 时间/作者: 2026-03-18 / guanyu1
- 自动分类: 通用实现调整
- 主要文件: `vllm/_custom_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b5323d90e` - feat:支持mqa的fp8实现

- 完整 hash: `b5323d90e281757f30309816f319408685dc42b5`
- 时间/作者: 2026-03-18 / lixh6
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `81077e8dd` - [perf]默认使用full graph

- 完整 hash: `81077e8ddc30a46f9ab43d2448dec6629726561f`
- 时间/作者: 2026-03-17 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `46ab154b7` - [perf]消除sparse mla build时的拷贝调度空泡

- 完整 hash: `46ab154b76f8d1cd71760b1c81f51011244877c7`
- 时间/作者: 2026-03-17 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/backends/mla/flashmla_sparse.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3c900b767` - add fa unified attn 导入判断

- 完整 hash: `3c900b767b50958602c71f29fbe50c235e36f6d0`
- 时间/作者: 2026-03-17 / fanwl
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/v1/attention/ops/triton_unified_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/attention/ops/triton_unified_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f9a04c974` - fix: resolve block_shape conflicts between DeepEP MoE and non-DeepEP quantization

- 完整 hash: `f9a04c97429bf3a2f1cacb51142beb525875cc5a`
- 时间/作者: 2026-03-16 / chenhw5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `be81eaf61` - [PD]添加VLLM_PP_LAYER_PARTITION_D控制d层切分

- 完整 hash: `be81eaf617aa8ec2018daacef98ebf04aba59c93`
- 时间/作者: 2026-03-16 / xuxz
- 自动分类: 调度/缓存/PD
- 主要文件: `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0c5e5f884` - [PD][Bugfix]修复0151pd分离d卡住问题

- 完整 hash: `0c5e5f884861d1b5b11edfde570c1ff394667f48`
- 时间/作者: 2026-03-16 / xuxz
- 自动分类: 缺陷修复
- 主要文件: `vllm/envs.py`, `vllm/v1/engine/input_processor.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`; `vllm/v1/engine/input_processor.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `2ce7c0964` - [PD][Fixbug]修复CachedRequestData结构体升级找不到resumed_req_ids变量

- 完整 hash: `2ce7c096430d6c597c0e82e6ba00f01e984b57ec`
- 时间/作者: 2026-03-16 / xuxz
- 自动分类: 缺陷修复
- 主要文件: `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `55c719cb0` - [feat]支持ray分布式异步调度，VLLM_ENABLE_RAY_ASYNC_SCHEDULING环境变量控制

- 完整 hash: `55c719cb0eb51258408ceb625181bb01d336425b`
- 时间/作者: 2026-03-16 / 王敏
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/config/vllm.py`, `vllm/envs.py`, `vllm/v1/executor/ray_executor.py`, `vllm/v1/executor/ray_utils.py`, `vllm/v1/outputs.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/worker_base.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`; `vllm/v1/executor/ray_executor.py`; `vllm/v1/executor/ray_utils.py`; `vllm/v1/outputs.py`
  - runtime-model: `vllm/config/vllm.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/worker_base.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9404668aa` - rms_norm_opt精度问题解决

- 完整 hash: `9404668aab7a2caca68420df40ad83351d41a2c1`
- 时间/作者: 2026-03-13 / guanyu1
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_custom_ops.py`, `vllm/model_executor/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `8e726b3f9` - fix: 修复MOE量化tensor对于其他模型的影响

- 完整 hash: `8e726b3f929dffb0670d89aa3b4abbff838cea45`
- 时间/作者: 2026-03-13 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7cec75a7e` - 修改sparse_attn hip后端

- 完整 hash: `7cec75a7eafecc665439c438ed2f59e875fa9406`
- 时间/作者: 2026-03-13 / liuchy5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/custom_op.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/custom_op.py`; `vllm/model_executor/layers/sparse_attn_indexer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `25a9d4b33` - [fix]添加VLLM_USE_LIGHTOP_FUSED_TOPP_TOPK控制lightop topp_topk融合算子开关

- 完整 hash: `25a9d4b33f6915bdfc9f8369ad3d1a6d44c3820f`
- 时间/作者: 2026-03-12 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `55a9f930b` - [fix]添加VLLM_USE_LIGHTOP控制lightop topp_topk融合算子开关

- 完整 hash: `55a9f930b6fcc319b245321d754a484559cd519d`
- 时间/作者: 2026-03-12 / 王敏
- 自动分类: 缺陷修复
- 主要文件: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3946292af` - [fix]添加VLLM_USE_LIGHTOP控制lightop topp_topk融合算子开关

- 完整 hash: `3946292af5d48f99c4aa90042df6386ff4207bab`
- 时间/作者: 2026-03-12 / 王敏
- 自动分类: 缺陷修复
- 主要文件: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9aabf7e76` - feat(deepseek-mla):: 精简 fused RMS-RoPE concat 可用性判断

- 完整 hash: `9aabf7e7691d71658116ac8e122d360b1bd2fd4e`
- 时间/作者: 2026-03-12 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cae53e46b` - feat(deepseek-mla): 接入 VLLM_USE_LIGHTOP_RMS_ROPE_CONCAT 融合链路 新增环境变量与 MLA 融合接线（wrapper -> attention -> impl） 接入 lightop fused_rms_norm_rope_contiguous，保留回退路径

- 完整 hash: `cae53e46bbe5af2d7d40976365a00270cc9a25b2`
- 时间/作者: 2026-03-10 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/mla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/mla.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `706c031cf` - moe: 补齐 fill+moe_align 融合开关语义

- 完整 hash: `706c031cf25d292e2aedaff629a64b7ad42c8ffb`
- 时间/作者: 2026-03-09 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`, `vllm/model_executor/model_loader/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1b71f5221` - 增加max_cudagraph_capture_size

- 完整 hash: `1b71f5221b39b22ba97ab0d665bacebb885801c1`
- 时间/作者: 2026-03-12 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/config/vllm.py`, `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/config/vllm.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `8bf99b0b8` - fix: fix bug http://hpczentao.sugon.com/bug-view-118388.html

- 完整 hash: `8bf99b0b87ea99195d651710c1d71fb2e97962f7`
- 时间/作者: 2026-03-12 / wanglong3
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6ca1362bd` - perf: DS v2增加DTBMM融合,默认关闭

- 完整 hash: `6ca1362bded6d66d3ffba5ca4fd57a61a2940c50`
- 时间/作者: 2026-03-12 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6b03cfdbd` - 补充mrope创建部分

- 完整 hash: `6b03cfdbd4acd5c7765d8cc2468b733105370f28`
- 时间/作者: 2026-03-12 / guanyu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fb445ddee` - 误删函数恢复

- 完整 hash: `fb445ddeece11b32b345b9bf34f61dc24fe081c6`
- 时间/作者: 2026-03-12 / guanyu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ef7e12146` - mrope_1d修改

- 完整 hash: `ef7e12146f5806fcb4ca836743e3e29a0f26fa34`
- 时间/作者: 2026-03-12 / guanyu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/envs.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ee355d86e` - mla: 恢复 opt-cat 在 prefill 和 decode 的拼接路由

- 完整 hash: `ee355d86ef68016148ee8321b4cb540aa36c37b7`
- 时间/作者: 2026-03-07 / laibao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/flashmla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`; `vllm/v1/attention/backends/mla/flashmla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
