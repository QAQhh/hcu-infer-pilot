# sglang Qwen3.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/basic_usage/qwen3_5.md` | `6b8e62f94` |
| `docs/platforms/ascend_npu_qwen3_5_examples.md` | `210d0fbae`, `56891e46b`, `d85884ca5`, `f2d72866e` |
| `python/sglang/srt/configs/qwen3_5.py` | `944a9f6fc`, `27c447653` |
| `python/sglang/srt/models/qwen3_5.py` | `94a624b83`, `5bdc07d97`, `852e112eb`, `d1e95af28`, `0acc1d3c9`, `97d5386a2`, `9b55a98a6`, `cabe171b6`, `7da590d4d`, `bdc1e46e5`, `b3202fe6d`, `d38c0e537`, ... (17 total) |
| `python/sglang/srt/models/qwen3_5_mtp.py` | `cabe171b6`, `9457c049e`, `bba2fc49a`, `fa5698d79`, `07a24f1a3`, `4ed254842`, `27c447653` |
| `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml` | `6b8e62f94` |
| `test/registered/4-gpu-models/test_qwen35_hicache.py` | `f5c225eeb` |
| `test/registered/4-gpu-models/test_qwen35_models.py` | `f5c225eeb`, `0986bed8e`, `3f883ebf2`, `4cc19862e`, `7142a594f`, `9457c049e` |
| `test/registered/8-gpu-models/test_qwen35.py` | `ac453b253` |
| `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` | `6b8e62f94` |
| `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py` | `6b8e62f94` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 47
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-07 | `9f67deca2` | 性能/后端优化 | 支持qwen3.5-awq模型 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py` |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `94a624b83` | 性能/后端优化 | 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-03-25 | `f5c225eeb` | 缺陷修复 | [CI] Fix TestQwen35WithHiCache (#21371) | `test/registered/4-gpu-models/test_qwen35_hicache.py`, `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-25 | `6b0f1e3b4` | 调度/缓存/PD | Update skip condition for TestQwen35PPAccuracy (#21370) | `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-24 | `0986bed8e` | 缺陷修复 | [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController (#20457) | `benchmark/hicache/bench_multiturn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py` |
| 2026-03-24 | `b4d3fb001` | 性能/后端优化 | [AMD] Add fused GemmaRMSNorm forward_hip to use aiter/vllm kernels for qwen3.5 (#21188) | `python/sglang/srt/layers/layernorm.py` |
| 2026-03-23 | `5bdc07d97` | 性能/后端优化 | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019) | `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-21 | `852e112eb` | 缺陷修复 | [Qwen3.5] Fix broken pipeline parallelism layer splitting (#21070) | `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-21 | `3f883ebf2` | 缺陷修复 | Fix test_qwen35_models (#21081) | `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-18 | `0acc1d3c9` | 缺陷修复 | fix: change qwen 3.5 linear attention a_log to fp32 (#19961) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-18 | `97d5386a2` | 性能/后端优化 | Use TRTLLM allreduce fusion for Qwen 3.5 (#19889) | `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-17 | `4cc19862e` | 性能/后端优化 | [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 (#19150) | `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py` |
| 2026-03-17 | `cfead25bb` | 缺陷修复 | [Qwen3.5] mamba slice fix (Prefill TP != Decode TP & decode TP size>1) (#20655) | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-03-17 | `210d0fbae` | 调度/缓存/PD | Update ascend docs (#20674) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md` |
| 2026-03-15 | `7142a594f` | 模型支持/运行时入口 | [CI]: Add CI For HiMambaRadixTree and qwen3.5 (#20540) | `.github/workflows/pr-test.yml`, `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-13 | `9c8777c80` | 性能/后端优化 | [AMD][Qwen3.5] aiter a8w8 gemm configuration (#19826) | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-03-11 | `9b55a98a6` | 性能/后端优化 | perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… (#20386) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-10 | `9884957c0` | 缺陷修复 | [NPU] Bugfix for qwen35 on NPU (#19756) | `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-03-09 | `cabe171b6` | 性能/后端优化 | Fix qwen3.5 mtp eplb related issues (#19767) | `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-03-07 | `7da590d4d` | 模型支持/运行时入口 | [Qwen3.5] Support Qwen3.5 Pipeline Parallelism (#19670) | `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-06 | `ac453b253` | 模型支持/运行时入口 | Add Qwen3.5-397B-A17B nightly test (8-GPU) (#19906) | `test/registered/8-gpu-models/test_qwen35.py` |
| 2026-03-06 | `f7de9375a` | 性能/后端优化 | [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775) | `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-03-04 | `9457c049e` | 调度/缓存/PD | [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-03-02 | `6b8e62f94` | 性能/后端优化 | [AMD] [Qwen 3.5 Day 0] Add Qwen 3.5 nightly accuracy tests (#19479) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/popular_model_usage.rst` |
| 2026-03-03 | `3f9fc8b84` | 性能/后端优化 | [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-02 | `468e3dc56` | 通用实现调整 | [Qwen3.5] Set full attn_backend to trtllm_mha on SM100 by default when possible (#19030) | `python/sglang/srt/server_args.py` |
| 2026-02-26 | `bdc1e46e5` | 缺陷修复 | [Qwen3.5] Qwen3.5-27B inference repeat bug fix (#19411) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-25 | `b3202fe6d` | 性能/后端优化 | [PCG] fix piecewise cuda graph for Qwen3.5 (#19220) | `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-25 | `56891e46b` | 模型支持/运行时入口 | [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-25 | `d38c0e537` | 缺陷修复 | fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 (#19070) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-25 | `f75abb452` | 缺陷修复 | [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads (#19086) | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-02-24 | `73fe389dd` | 调度/缓存/PD | [Qwen3.5] Raise Exception when radix_cache and extra_buffer are enabled at the same time (#19169) | `python/sglang/srt/server_args.py` |
| 2026-02-19 | `8541b1118` | 缺陷修复 | [Fix][Qwen3.5] Pass max_mamba_cache_size to mamba pool in disaggregation decode path (#19002) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-02-18 | `bba2fc49a` | 模型支持/运行时入口 | [Qwen3.5] Enable nvfp4 checkpoint (#18937) | `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-18 | `fa5698d79` | 性能/后端优化 | feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation (#18926) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-16 | `d85884ca5` | 调度/缓存/PD | Update ascend_npu_qwen3_5_examples.md (#18888) | `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-16 | `f2d72866e` | 测试/文档/基准 | Create ascend_npu_qwen3_5_examples.md (#18864) | `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-14 | `944a9f6fc` | 缺陷修复 | Fix/qwen3 5 amd rope cutedsl fallback (#18753) | `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` |
| 2026-02-12 | `1edc69be0` | 性能/后端优化 | [Ascend]Support qwen3.5 (#18544) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-12 | `4ed254842` | 模型支持/运行时入口 | [Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation (#18538) | `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-10 | `27c447653` | 性能/后端优化 | model: support Qwen3.5 (#18489) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py` |

## 逐 Commit 审计卡

### Commit `9f67deca2` - 支持qwen3.5-awq模型

- 完整 hash: `9f67deca24b100410fe69d142a4ebca4fe26cc34`
- 时间/作者: 2026-05-07 / maxiao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/moe_wna16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- 完整 hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- 时间/作者: 2026-04-29 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- 完整 hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `94a624b83` - 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子

- 完整 hash: `94a624b8364de497a4a7ee4a6f9def06e18d90c9`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b8cd509f4` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- 完整 hash: `b8cd509f45f9a51adee404eb9104358653e869d1`
- 时间/作者: 2026-04-09 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `28dec61dd` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- 完整 hash: `28dec61dd674f482fe34b5251ff0cd050ca2184c`
- 时间/作者: 2026-04-02 / liucong
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f5c225eeb` - [CI] Fix TestQwen35WithHiCache (#21371)

- 完整 hash: `f5c225eeba3c6f027e5e7691784249d6a667026f`
- 时间/作者: 2026-03-25 / Baizhou Zhang
- 自动分类: 缺陷修复
- 主要文件: `test/registered/4-gpu-models/test_qwen35_hicache.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen35_hicache.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `6b0f1e3b4` - Update skip condition for TestQwen35PPAccuracy (#21370)

- 完整 hash: `6b0f1e3b437dc6aabf933deab07c3a0daa137f7b`
- 时间/作者: 2026-03-25 / Shangming Cai
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0986bed8e` - [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController (#20457)

- 完整 hash: `0986bed8e279ce67659e4e473300fc3c5c717d6a`
- 时间/作者: 2026-03-24 / hzh0425
- 自动分类: 缺陷修复
- 主要文件: `benchmark/hicache/bench_multiturn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hicache_storage.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/hicache/bench_multiturn.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`; `python/sglang/srt/mem_cache/mamba_radix_cache.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b4d3fb001` - [AMD] Add fused GemmaRMSNorm forward_hip to use aiter/vllm kernels for qwen3.5 (#21188)

- 完整 hash: `b4d3fb001d435a9792a1a3896f2384ea9061b67b`
- 时间/作者: 2026-03-24 / jacky.cheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `5bdc07d97` - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019)

- 完整 hash: `5bdc07d974f6cf236fa765a685453ea5e587a838`
- 时间/作者: 2026-03-23 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `852e112eb` - [Qwen3.5] Fix broken pipeline parallelism layer splitting (#21070)

- 完整 hash: `852e112ebf0054b317e9f02aec97fcf533259cac`
- 时间/作者: 2026-03-21 / Alison Shao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3f883ebf2` - Fix test_qwen35_models (#21081)

- 完整 hash: `3f883ebf2e11fd1c56224bc9111deea1b8860a50`
- 时间/作者: 2026-03-21 / Qiaolin Yu
- 自动分类: 缺陷修复
- 主要文件: `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- 完整 hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- 时间/作者: 2026-03-18 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0acc1d3c9` - fix: change qwen 3.5 linear attention a_log to fp32 (#19961)

- 完整 hash: `0acc1d3c9ad7e912d2ecfe245bc29c6486ada405`
- 时间/作者: 2026-03-18 / shiyu7
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `97d5386a2` - Use TRTLLM allreduce fusion for Qwen 3.5 (#19889)

- 完整 hash: `97d5386a211c83a21d2c977540fd453928f5e417`
- 时间/作者: 2026-03-18 / Brayden Zhong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4cc19862e` - [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 (#19150)

- 完整 hash: `4cc19862efded3a4aff44aafa8dcd87be8cff5c2`
- 时间/作者: 2026-03-17 / Kaixi Hou
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/accuracy_test_runner.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cfead25bb` - [Qwen3.5] mamba slice fix (Prefill TP != Decode TP & decode TP size>1) (#20655)

- 完整 hash: `cfead25bbf695b577fcb8ef6d5cb4ab63e2901f6`
- 时间/作者: 2026-03-17 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `210d0fbae` - Update ascend docs (#20674)

- 完整 hash: `210d0fbaef41bb18a83320e1fbe8f50c9d0c9ead`
- 时间/作者: 2026-03-17 / amote-i
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`; `docs/platforms/ascend_npu_support_features.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `7142a594f` - [CI]: Add CI For HiMambaRadixTree and qwen3.5 (#20540)

- 完整 hash: `7142a594f950053646793b590ac6f9aafe58416c`
- 时间/作者: 2026-03-15 / hzh0425
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test.yml`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `9c8777c80` - [AMD][Qwen3.5] aiter a8w8 gemm configuration (#19826)

- 完整 hash: `9c8777c80f685fba2179a5341492bfdcf6077ad8`
- 时间/作者: 2026-03-13 / seungrokj
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9b55a98a6` - perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… (#20386)

- 完整 hash: `9b55a98a67059b30a2997f244221be1b0b4042c3`
- 时间/作者: 2026-03-11 / Vedant V Jhaveri
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9884957c0` - [NPU] Bugfix  for qwen35 on NPU (#19756)

- 完整 hash: `9884957c07ce0a98fad34ea0055803594c459cb1`
- 时间/作者: 2026-03-10 / Hexq0210
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cabe171b6` - Fix qwen3.5 mtp eplb related issues (#19767)

- 完整 hash: `cabe171b6ce3b0d4fb25ff9c88d5743430efaca6`
- 时间/作者: 2026-03-09 / luoyuyan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_next_mtp.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7da590d4d` - [Qwen3.5] Support Qwen3.5 Pipeline Parallelism (#19670)

- 完整 hash: `7da590d4d069273644e2eed5fd67c597ba97b220`
- 时间/作者: 2026-03-07 / Yuan Luo
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ac453b253` - Add Qwen3.5-397B-A17B nightly test (8-GPU) (#19906)

- 完整 hash: `ac453b253f586b3d85d5eac2a3a38ee77826cbf1`
- 时间/作者: 2026-03-06 / Alison Shao
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/8-gpu-models/test_qwen35.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/8-gpu-models/test_qwen35.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f7de9375a` - [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775)

- 完整 hash: `f7de9375ace71f46882d095bb3fc23f706bad660`
- 时间/作者: 2026-03-06 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`; `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
  - tests: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9457c049e` - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391)

- 完整 hash: `9457c049e19e1cfa75833ef4351ac5aa26941c2c`
- 时间/作者: 2026-03-04 / hlu1
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6b8e62f94` - [AMD] [Qwen 3.5 Day 0] Add Qwen 3.5 nightly accuracy tests (#19479)

- 完整 hash: `6b8e62f94fec4703048869ca3efbaf40e2928817`
- 时间/作者: 2026-03-02 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/popular_model_usage.rst`, `docs/basic_usage/qwen3_5.md`, `docs/supported_models/text_generation/generative_models.md`, `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - docs-bench: `docs/basic_usage/popular_model_usage.rst`; `docs/basic_usage/qwen3_5.md`; `docs/supported_models/text_generation/generative_models.md`
  - tests: `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`; `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3f9fc8b84` - [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291)

- 完整 hash: `3f9fc8b848365a5797a44856854e3e6f00a60dd0`
- 时间/作者: 2026-03-03 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `468e3dc56` - [Qwen3.5] Set full attn_backend to trtllm_mha on SM100 by default when possible (#19030)

- 完整 hash: `468e3dc56beef6cf2d15284851f77a6390d7e97f`
- 时间/作者: 2026-03-02 / hlu1
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `bdc1e46e5` - [Qwen3.5] Qwen3.5-27B inference repeat bug fix (#19411)

- 完整 hash: `bdc1e46e5ac93dd7ee2d53e5d8c2d3de7dc03f69`
- 时间/作者: 2026-02-26 / AlfredYong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b3202fe6d` - [PCG] fix piecewise cuda graph for Qwen3.5 (#19220)

- 完整 hash: `b3202fe6d072c6afdfd8a567977d84de17c1d50d`
- 时间/作者: 2026-02-25 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `56891e46b` - [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339)

- 完整 hash: `56891e46bc1ac4f75e8e541b61810f777cda8209`
- 时间/作者: 2026-02-25 / Hexq0210
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d38c0e537` - fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 (#19070)

- 完整 hash: `d38c0e537d95bfb78486c1185f68c90046ce0cc9`
- 时间/作者: 2026-02-25 / Zheng Li
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f75abb452` - [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads (#19086)

- 完整 hash: `f75abb4521cfa5a58a9876b3d71c5788302f751d`
- 时间/作者: 2026-02-25 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `73fe389dd` - [Qwen3.5] Raise Exception when radix_cache and extra_buffer are enabled at the same time (#19169)

- 完整 hash: `73fe389dd11472fcd41f401382c0763d4d1db664`
- 时间/作者: 2026-02-24 / YAMY
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `8541b1118` - [Fix][Qwen3.5] Pass max_mamba_cache_size to mamba pool in disaggregation decode path (#19002)

- 完整 hash: `8541b1118d6cb396fe9c8f580ea597996635f8fb`
- 时间/作者: 2026-02-19 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-perf: `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bba2fc49a` - [Qwen3.5] Enable nvfp4 checkpoint (#18937)

- 完整 hash: `bba2fc49a1700d82ac9f4f79bf6e05b120d424e7`
- 时间/作者: 2026-02-18 / hlu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fa5698d79` - feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation (#18926)

- 完整 hash: `fa5698d7916497288af8fe5a5b57bc4ee7e6fb37`
- 时间/作者: 2026-02-18 / Zheng Li
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d85884ca5` - Update ascend_npu_qwen3_5_examples.md (#18888)

- 完整 hash: `d85884ca5759feebe7164b4d6884746776582218`
- 时间/作者: 2026-02-16 / RAY
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `f2d72866e` - Create ascend_npu_qwen3_5_examples.md  (#18864)

- 完整 hash: `f2d72866e9e9e56413c41807d63a20e88cb72af1`
- 时间/作者: 2026-02-16 / chenxu214
- 自动分类: 测试/文档/基准
- 主要文件: `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `07a24f1a3` - update pre-commit config (#18860)

- 完整 hash: `07a24f1a3846c4186e82ffc2bc43990ba6c0babc`
- 时间/作者: 2026-02-16 / SoluMilken
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py`, `benchmark/fla/benchmark_layernorm_gated.py`, `benchmark/tip_suggestion/bench_other.py`, `benchmark/tip_suggestion/bench_sglang.py`, `benchmark/tip_suggestion/lmql_funcs.py`, `examples/runtime/engine/save_remote_state.py` 等 100 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint.yml`
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`; `benchmark/tip_suggestion/bench_other.py`; `benchmark/tip_suggestion/bench_sglang.py`; `benchmark/tip_suggestion/lmql_funcs.py`; `examples/runtime/engine/save_remote_state.py`; `examples/runtime/engine/save_sharded_state.py`
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/function_call/base_format_detector.py`; `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/metrics/collector.py`; `python/sglang/srt/metrics/utils.py` 等 25 个文件
  - runtime-model: `.pre-commit-config.yaml`; `python/sglang/srt/checkpoint_engine/checkpoint_engine_worker.py`; `python/sglang/srt/configs/exaone.py`; `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/entrypoints/openai/serving_responses.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 34 个文件
  - runtime-perf: `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `python/sglang/jit_kernel/include/sgl_kernel/type.cuh`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/linear/seg_la.py`; `python/sglang/srt/layers/attention/wave_ops/prefill_attention.py`; `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` 等 27 个文件
  - tests: `sgl-kernel/tests/test_per_token_group_quant_8bit.py`; `test/manual/test_vlm_accuracy.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/layers/test_fla_layernorm_guard.py`; `test/registered/quant/test_awq_dequant.py`; `test/srt/cpu/test_norm.py`; `test/srt/cpu/test_qwen3.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `944a9f6fc` - Fix/qwen3 5 amd rope cutedsl fallback (#18753)

- 完整 hash: `944a9f6fcfe6a56f682da9e0644abf569cb4ca2c`
- 时间/作者: 2026-02-14 / andyluo7
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1edc69be0` - [Ascend]Support qwen3.5 (#18544)

- 完整 hash: `1edc69be085473f27314f885e43ab7e70ef09a23`
- 时间/作者: 2026-02-12 / chenxu214
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4ed254842` - [Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation (#18538)

- 完整 hash: `4ed2548427a0f01a969d6e518088bcb62a568f5d`
- 时间/作者: 2026-02-12 / Zheng Li
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `27c447653` - model: support Qwen3.5 (#18489)

- 完整 hash: `27c447653d9cf0f63aea1c190b931be4875cbf86`
- 时间/作者: 2026-02-10 / Zheng Li
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/managers/mm_utils.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`; `python/sglang/srt/utils/common.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py` 等 10 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
