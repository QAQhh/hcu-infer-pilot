# sglang Llama 4 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/basic_usage/llama4.md` | `3aa11ca72` |
| `examples/chat_template/tool_chat_template_llama4_pythonic.jinja` | 无直接提交 |
| `python/sglang/srt/models/llama4.py` | `d1e95af28`, `bc9190435`, `22df62d58`, `fb683be6e` |
| `python/sglang/srt/models/mllama4.py` | `d1e95af28` |
| `python/sglang/srt/multimodal/processors/mllama4.py` | 无直接提交 |
| `test/manual/lora/test_lora_llama4.py` | 无直接提交 |
| `test/manual/models/test_llama4_models.py` | 无直接提交 |
| `test/registered/8-gpu-models/test_llama4.py` | `912349143`, `655d2c7c2`, `aa2b4f766`, `2ff872311` |
| `test/registered/ascend/llm_models/test_npu_llama4_scount_17b_16e.py` | `895e56097` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 12
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-02-27 | `bc9190435` | 模型支持/运行时入口 | llama4 npu adapt (#17123) | `python/sglang/srt/models/llama4.py`, `python/sglang/srt/server_args.py`, `test/registered/ascend/llm_models/test_ascend_llama4_scount_17b_16e.py` |
| 2026-01-29 | `22df62d58` | 模型支持/运行时入口 | add weightless qk norm to RMSNorm interface for Llama 4 (#12813) | `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/llama4.py` |
| 2026-01-28 | `0998de088` | 性能/后端优化 | [Perf] Tune Llama-4-Scout-17B-16E-Instruct fused moe kernel (#17891) | `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=16,N=2048,device_name=NVIDIA_B200.json` |
| 2026-01-26 | `6756cf18c` | 缺陷修复 | remove multimodal as this is completely dead code (#17750) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/multimodal/error.rs` |
| 2026-01-25 | `912349143` | 调度/缓存/PD | A few updates to the night tests (#17694) | `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-15 | `655d2c7c2` | 缺陷修复 | fix: adding matrix partitioning for h200 and b200 nightly tests (#17091) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-14 | `aa2b4f766` | 缺陷修复 | fix: renaming test file and job names + skip blocking llama4 nightly (#16971) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-07 | `2ff872311` | 模型支持/运行时入口 | ci: adding llama4 placeholder test to nightly (#16599) | `test/registered/8-gpu-models/test_llama4.py` |
| 2026-01-06 | `3aa11ca72` | 调度/缓存/PD | Remove hybrid_kvcache_ratio in server args (#16399) | `docs/basic_usage/llama4.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/tp_worker.py` |

## 逐 Commit 审计卡

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

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- 完整 hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- 时间/作者: 2026-03-16 / Sugar920
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `bc9190435` - llama4 npu adapt (#17123)

- 完整 hash: `bc9190435b3fabd3b3c578e6675071f9387efe66`
- 时间/作者: 2026-02-27 / KnightLTC
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/llama4.py`, `python/sglang/srt/server_args.py`, `test/registered/ascend/llm_models/test_ascend_llama4_scount_17b_16e.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/llama4.py`; `python/sglang/srt/server_args.py`
  - tests: `test/registered/ascend/llm_models/test_ascend_llama4_scount_17b_16e.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `22df62d58` - add weightless qk norm to RMSNorm interface for Llama 4 (#12813)

- 完整 hash: `22df62d5862bed333b0f3f1092ef968d32c174a2`
- 时间/作者: 2026-01-29 / b8zhong
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/llama4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/llama4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0998de088` - [Perf] Tune Llama-4-Scout-17B-16E-Instruct fused moe kernel (#17891)

- 完整 hash: `0998de088b206004db6ab830bd3deba5ce27642f`
- 时间/作者: 2026-01-28 / jackey hua
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=16,N=2048,device_name=NVIDIA_B200.json`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=16,N=2048,device_name=NVIDIA_B200.json`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6756cf18c` - remove multimodal as this is completely dead code (#17750)

- 完整 hash: `6756cf18c61dde7eb855ccecd002ba5cde1ab610`
- 时间/作者: 2026-01-26 / Simo Lin
- 自动分类: 缺陷修复
- 主要文件: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/multimodal/error.rs`, `sgl-model-gateway/src/multimodal/media.rs`, `sgl-model-gateway/src/multimodal/mod.rs`, `sgl-model-gateway/src/multimodal/registry.rs`, `sgl-model-gateway/src/multimodal/tracker.rs`, `sgl-model-gateway/src/multimodal/types.rs` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/src/lib.rs`; `sgl-model-gateway/src/multimodal/error.rs`; `sgl-model-gateway/src/multimodal/media.rs`; `sgl-model-gateway/src/multimodal/mod.rs`; `sgl-model-gateway/src/multimodal/registry.rs`; `sgl-model-gateway/src/multimodal/tracker.rs`; `sgl-model-gateway/src/multimodal/types.rs` 等 20 个文件
  - runtime-model: `sgl-model-gateway/src/multimodal/vision/preprocessor_config.rs`
  - tests: `sgl-model-gateway/tests/multimodal/mod.rs`; `sgl-model-gateway/tests/multimodal/multimodal_tracker_test.rs`; `sgl-model-gateway/tests/multimodal/vision_golden_tests.rs`; `sgl-model-gateway/tests/multimodal_tests.rs`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `912349143` - A few updates to the night tests (#17694)

- 完整 hash: `9123491430c9cc38b6796cbf3ad3ef07e948e8c9`
- 时间/作者: 2026-01-25 / Kangyan-Zhou
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `fb683be6e` - Use attn tp group in embedding for more models (#17570)

- 完整 hash: `fb683be6eb7c6960f3d37ea91ca836c1b8e4120c`
- 时间/作者: 2026-01-24 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/gpt_oss.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/falcon_h1.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/llama4.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/bailing_moe_nextn.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`; `python/sglang/srt/models/glm4_moe_nextn.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 10 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `655d2c7c2` - fix: adding matrix partitioning for h200 and b200 nightly tests (#17091)

- 完整 hash: `655d2c7c2aa42d7b097498a2c0d48cd697aeda61`
- 时间/作者: 2026-01-15 / Douglas Yang
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `aa2b4f766` - fix: renaming test file and job names + skip blocking llama4 nightly (#16971)

- 完整 hash: `aa2b4f76617929469acb3a7bbd6052e718d00ab3`
- 时间/作者: 2026-01-14 / Douglas Yang
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py`, `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py`; `test/registered/8-gpu-models/test_mistral_large3.py` 等 9 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `2ff872311` - ci: adding llama4 placeholder test to nightly (#16599)

- 完整 hash: `2ff872311b4d3e8e5c0416e948dabbe6ff5adf87`
- 时间/作者: 2026-01-07 / Douglas Yang
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/8-gpu-models/test_llama4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/8-gpu-models/test_llama4.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3aa11ca72` - Remove hybrid_kvcache_ratio in server args (#16399)

- 完整 hash: `3aa11ca722ce25d6d1f291636b3bcdd7b3f43dd9`
- 时间/作者: 2026-01-06 / Ke Bao
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/basic_usage/llama4.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/basic_usage/llama4.md`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
