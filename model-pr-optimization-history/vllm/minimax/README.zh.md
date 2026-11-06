# vllm MiniMax M2 Series 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/distributed/test_minimax_m3_indexer_cp_tp.py` | [#57832](https://github.com/vllm-project/vllm/pull/57832) |
| `tests/kernels/attention/minimax_m3_nvfp4_ref.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/attention/test_minimax_m3.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#45720](https://github.com/vllm-project/vllm/pull/45720), [#45892](https://github.com/vllm-project/vllm/pull/45892), [#47287](https://github.com/vllm-project/vllm/pull/47287), [#47502](https://github.com/vllm-project/vllm/pull/47502), [#47984](https://github.com/vllm-project/vllm/pull/47984), [#52664](https://github.com/vllm-project/vllm/pull/52664), [#54535](https://github.com/vllm-project/vllm/pull/54535), [#54597](https://github.com/vllm-project/vllm/pull/54597), [#54682](https://github.com/vllm-project/vllm/pull/54682), [#55235](https://github.com/vllm-project/vllm/pull/55235), [#56151](https://github.com/vllm-project/vllm/pull/56151), ... (21 total) |
| `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` | [#59081](https://github.com/vllm-project/vllm/pull/59081), [#59481](https://github.com/vllm-project/vllm/pull/59481), [#62270](https://github.com/vllm-project/vllm/pull/62270) |
| `tests/kernels/attention/test_minimax_m3_index_topk_decode.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#65087](https://github.com/vllm-project/vllm/pull/65087) |
| `tests/kernels/attention/test_minimax_m3_indexer_cp.py` | [#57832](https://github.com/vllm-project/vllm/pull/57832), [#57909](https://github.com/vllm-project/vllm/pull/57909) |
| `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` | [#50032](https://github.com/vllm-project/vllm/pull/50032), [#51203](https://github.com/vllm-project/vllm/pull/51203), [#55838](https://github.com/vllm-project/vllm/pull/55838), [#59300](https://github.com/vllm-project/vllm/pull/59300), [#60684](https://github.com/vllm-project/vllm/pull/60684), [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64856](https://github.com/vllm-project/vllm/pull/64856) |
| `tests/kernels/attention/test_minimax_m3_norm_rope_nvfp4_insert.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64448](https://github.com/vllm-project/vllm/pull/64448), [#65432](https://github.com/vllm-project/vllm/pull/65432) |
| `tests/kernels/attention/test_minimax_m3_nvfp4_indexer_decode_cp.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/attention/test_minimax_m3_nvfp4_prefill_flydsl.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/attention/test_minimax_m3_nvfp4_sparse_decode.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/core/test_minimax_reduce_rms.py` | [#37045](https://github.com/vllm-project/vllm/pull/37045), [#43410](https://github.com/vllm-project/vllm/pull/43410), [#45935](https://github.com/vllm-project/vllm/pull/45935), [#55057](https://github.com/vllm-project/vllm/pull/55057) |
| `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#45892](https://github.com/vllm-project/vllm/pull/45892), [#47287](https://github.com/vllm-project/vllm/pull/47287), [#50032](https://github.com/vllm-project/vllm/pull/50032), [#59300](https://github.com/vllm-project/vllm/pull/59300), [#62270](https://github.com/vllm-project/vllm/pull/62270), [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64475](https://github.com/vllm-project/vllm/pull/64475) |
| `tests/kernels/test_minimax_m3_amd_ops.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#46117](https://github.com/vllm-project/vllm/pull/46117), [#47158](https://github.com/vllm-project/vllm/pull/47158), [#53674](https://github.com/vllm-project/vllm/pull/53674), [#56849](https://github.com/vllm-project/vllm/pull/56849), [#63637](https://github.com/vllm-project/vllm/pull/63637), [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/test_minimax_m3_dspark_draft.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py` | [#47287](https://github.com/vllm-project/vllm/pull/47287), [#57420](https://github.com/vllm-project/vllm/pull/57420) |
| `tests/models/minimax_m3/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/minimax_m3/amd_specialized_decode/_xcd_stress.py` | [#62712](https://github.com/vllm-project/vllm/pull/62712) |
| `tests/models/minimax_m3/amd_specialized_decode/test_model.py` | [#62712](https://github.com/vllm-project/vllm/pull/62712), [#62994](https://github.com/vllm-project/vllm/pull/62994) |
| `tests/models/minimax_m3/amd_specialized_decode/test_ops.py` | [#62712](https://github.com/vllm-project/vllm/pull/62712) |
| `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` | [#62712](https://github.com/vllm-project/vllm/pull/62712), [#62994](https://github.com/vllm-project/vllm/pull/62994) |
| `tests/models/minimax_m3/test_dense_gemm1_mxfp8.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/minimax_m3/test_dspark_draft_compile.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/minimax_m3/test_index_cache_overrides.py` | [#63082](https://github.com/vllm-project/vllm/pull/63082) |
| `tests/models/minimax_m3/test_mono_host.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/minimax_m3/test_norm_mxfp8.py` | [#64852](https://github.com/vllm-project/vllm/pull/64852) |
| `tests/models/minimax_m3/test_qkv_index_fused_epilogue.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/multimodal/processing/test_minimax_m3.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/models/test_minimax_m3_mega_moe.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/parser/engine/test_minimax_m2.py` | [#45701](https://github.com/vllm-project/vllm/pull/45701), [#62035](https://github.com/vllm-project/vllm/pull/62035) |
| `tests/parser/engine/test_minimax_m3.py` | [#59743](https://github.com/vllm-project/vllm/pull/59743) |
| `tests/reasoning/test_minimax_m2_append_reasoning_parser.py` | [#29882](https://github.com/vllm-project/vllm/pull/29882) |
| `tests/reasoning/test_minimax_m2_reasoning_parser.py` | [#29882](https://github.com/vllm-project/vllm/pull/29882), [#45701](https://github.com/vllm-project/vllm/pull/45701) |
| `tests/reasoning/test_minimax_m3_reasoning_parser.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#45718](https://github.com/vllm-project/vllm/pull/45718), [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `tests/tool_parsers/test_minimax_m2_tool_parser.py` | [#35895](https://github.com/vllm-project/vllm/pull/35895), [#39599](https://github.com/vllm-project/vllm/pull/39599), [#45701](https://github.com/vllm-project/vllm/pull/45701), [#48846](https://github.com/vllm-project/vllm/pull/48846) |
| `tests/tool_parsers/test_minimax_m3_tool_parser.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#48523](https://github.com/vllm-project/vllm/pull/48523), [#59743](https://github.com/vllm-project/vllm/pull/59743) |
| `vllm/model_executor/layers/mamba/linear/minimax_linear_attn.py` | 无直接 PR 号提交 |
| `vllm/model_executor/layers/minimax_rms_norm/__init__.py` | [#43410](https://github.com/vllm-project/vllm/pull/43410) |
| `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` | [#43410](https://github.com/vllm-project/vllm/pull/43410), [#60917](https://github.com/vllm-project/vllm/pull/60917) |
| `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` | [#43410](https://github.com/vllm-project/vllm/pull/43410), [#44849](https://github.com/vllm-project/vllm/pull/44849), [#44983](https://github.com/vllm-project/vllm/pull/44983), [#45935](https://github.com/vllm-project/vllm/pull/45935) |
| `vllm/model_executor/models/minimax_m2.py` | [#27535](https://github.com/vllm-project/vllm/pull/27535), [#27537](https://github.com/vllm-project/vllm/pull/27537), [#27627](https://github.com/vllm-project/vllm/pull/27627), [#30384](https://github.com/vllm-project/vllm/pull/30384), [#31493](https://github.com/vllm-project/vllm/pull/31493), [#32736](https://github.com/vllm-project/vllm/pull/32736), [#32763](https://github.com/vllm-project/vllm/pull/32763), [#36965](https://github.com/vllm-project/vllm/pull/36965), [#37045](https://github.com/vllm-project/vllm/pull/37045), [#37214](https://github.com/vllm-project/vllm/pull/37214), [#37512](https://github.com/vllm-project/vllm/pull/37512), [#38191](https://github.com/vllm-project/vllm/pull/38191), ... (14 total) |
| `vllm/model_executor/warmup/minimax_m3_msa_warmup.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/__init__.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381) |
| `vllm/models/minimax_m3/amd/__init__.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381) |
| `vllm/models/minimax_m3/amd/indexer_context_parallel.py` | [#57832](https://github.com/vllm-project/vllm/pull/57832) |
| `vllm/models/minimax_m3/amd/indexer_cp.py` | [#57909](https://github.com/vllm-project/vllm/pull/57909) |
| `vllm/models/minimax_m3/amd/indexer_msa.py` | [#57909](https://github.com/vllm-project/vllm/pull/57909), [#64448](https://github.com/vllm-project/vllm/pull/64448) |
| `vllm/models/minimax_m3/amd/indexer_nvfp4.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64448](https://github.com/vllm-project/vllm/pull/64448), [#65432](https://github.com/vllm-project/vllm/pull/65432) |
| `vllm/models/minimax_m3/amd/model.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#45810](https://github.com/vllm-project/vllm/pull/45810), [#45892](https://github.com/vllm-project/vllm/pull/45892), [#45896](https://github.com/vllm-project/vllm/pull/45896), [#46419](https://github.com/vllm-project/vllm/pull/46419), [#46474](https://github.com/vllm-project/vllm/pull/46474), [#46545](https://github.com/vllm-project/vllm/pull/46545), [#47269](https://github.com/vllm-project/vllm/pull/47269), [#47287](https://github.com/vllm-project/vllm/pull/47287), [#52664](https://github.com/vllm-project/vllm/pull/52664), [#52849](https://github.com/vllm-project/vllm/pull/52849), [#54535](https://github.com/vllm-project/vllm/pull/54535), ... (22 total) |
| `vllm/models/minimax_m3/amd/model_state.py` | [#62712](https://github.com/vllm-project/vllm/pull/62712) |
| `vllm/models/minimax_m3/amd/mono/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/check.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/config.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/dispatch.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/envs.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/kernels/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/kernels/common.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/kernels/index_score.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64474](https://github.com/vllm-project/vllm/pull/64474) |
| `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/layout.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/peer_buffer.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mono/runner.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64474](https://github.com/vllm-project/vllm/pull/64474) |
| `vllm/models/minimax_m3/amd/mono/weights.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/mtp.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#57909](https://github.com/vllm-project/vllm/pull/57909), [#58648](https://github.com/vllm-project/vllm/pull/58648), [#62270](https://github.com/vllm-project/vllm/pull/62270) |
| `vllm/models/minimax_m3/amd/ops/__init__.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#63637](https://github.com/vllm-project/vllm/pull/63637) |
| `vllm/models/minimax_m3/amd/ops/flydsl_utils.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py` | [#45381](https://github.com/vllm-project/vllm/pull/45381), [#63637](https://github.com/vllm-project/vllm/pull/63637) |
| `vllm/models/minimax_m3/amd/ops/index_cp/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/ops/index_cp/host.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#64448](https://github.com/vllm-project/vllm/pull/64448) |
| `vllm/models/minimax_m3/amd/ops/index_topk.py` | [#46546](https://github.com/vllm-project/vllm/pull/46546), [#54682](https://github.com/vllm-project/vllm/pull/54682), [#55235](https://github.com/vllm-project/vllm/pull/55235), [#59285](https://github.com/vllm-project/vllm/pull/59285) |
| `vllm/models/minimax_m3/amd/ops/index_topk_decode/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#65087](https://github.com/vllm-project/vllm/pull/65087) |
| `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111), [#65087](https://github.com/vllm-project/vllm/pull/65087) |
| `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py` | [#57832](https://github.com/vllm-project/vllm/pull/57832) |
| `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py` | [#57832](https://github.com/vllm-project/vllm/pull/57832) |
| `vllm/models/minimax_m3/amd/ops/norm_rope_nvfp4_insert/__init__.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/ops/norm_rope_nvfp4_insert/host.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| `vllm/models/minimax_m3/amd/ops/norm_rope_nvfp4_insert/kernel.py` | [#64111](https://github.com/vllm-project/vllm/pull/64111) |
| ... | 71 more files omitted from table; all were used for git tracing. |

## PR 覆盖总览

- git 追溯 PR 数: 104
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 104

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-05 | [#64856](https://github.com/vllm-project/vllm/pull/64856) | merged | [Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace | `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` |
| 2026-11-05 | [#65763](https://github.com/vllm-project/vllm/pull/65763) | merged | [CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic | `tests/kernels/attention/test_minimax_m3.py` |
| 2026-11-04 | [#65537](https://github.com/vllm-project/vllm/pull/65537) | merged | [MiniMax-M3] Support sequence parallelism with pipeline parallelism | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-04 | [#65432](https://github.com/vllm-project/vllm/pull/65432) | merged | [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP | `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` |
| 2026-11-04 | [#65087](https://github.com/vllm-project/vllm/pull/65087) | merged | [ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer | `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py` |
| 2026-11-03 | [#65496](https://github.com/vllm-project/vllm/pull/65496) | merged | [Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-03 | [#65226](https://github.com/vllm-project/vllm/pull/65226) | merged | [Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences | `vllm/models/minimax_m3/common/encoder_cudagraph.py` |
| 2026-11-02 | [#64475](https://github.com/vllm-project/vllm/pull/64475) | merged | [MiniMax-M3.1][P/D] NIXL KV-head re-sharding for per-head-contiguous NVFP4 pages | `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` |
| 2026-11-02 | [#62270](https://github.com/vllm-project/vllm/pull/62270) | merged | [ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942 | `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py` |
| 2026-11-02 | [#64448](https://github.com/vllm-project/vllm/pull/64448) | merged | [ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7 | `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `vllm/models/minimax_m3/amd/ops/index_cp/host.py`, `vllm/models/minimax_m3/amd/indexer_msa.py` |
| 2026-11-02 | [#64852](https://github.com/vllm-project/vllm/pull/64852) | merged | [Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8 | `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-02 | [#64659](https://github.com/vllm-project/vllm/pull/64659) | merged | [Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-10-29 | [#64474](https://github.com/vllm-project/vllm/pull/64474) | merged | [Doc] Fix MiniMax-M3 docstring cross-references | `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py` |
| 2026-10-29 | [#64111](https://github.com/vllm-project/vllm/pull/64111) | merged | [New Model] Add MiniMax-M3.1-Flash Model and Kernels | `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py`, `vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py`, `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py` |
| 2026-10-29 | [#64037](https://github.com/vllm-project/vllm/pull/64037) | merged | [Kernel][MiniMax-M3] Enable SM90 split-K in the Triton indexer | `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-10-28 | [#63637](https://github.com/vllm-project/vllm/pull/63637) | merged | [ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj | `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/__init__.py` |
| 2026-10-27 | [#57420](https://github.com/vllm-project/vllm/pull/57420) | merged | [Kernel][MiniMax-M3] Add Triton query-tiled sparse prefill tuned on Hopper | `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py` |
| 2026-10-27 | [#62141](https://github.com/vllm-project/vllm/pull/62141) | merged | [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355 | `tests/kernels/attention/test_minimax_m3.py` |
| 2026-10-24 | [#57909](https://github.com/vllm-project/vllm/pull/57909) | merged | [ROCm][PERF] Enable MiniMax-M3 Indexer CP | `vllm/models/minimax_m3/amd/indexer_msa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/mtp.py` |
| 2026-10-23 | [#63082](https://github.com/vllm-project/vllm/pull/63082) | merged | [Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config | `tests/models/minimax_m3/test_index_cache_overrides.py`, `vllm/models/minimax_m3/amd/model.py` |
| 2026-10-22 | [#62994](https://github.com/vllm-project/vllm/pull/62994) | merged | [ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps | `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py` |
| 2026-10-21 | [#57832](https://github.com/vllm-project/vllm/pull/57832) | merged | [ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in) | `vllm/models/minimax_m3/amd/indexer_context_parallel.py`, `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py`, `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py` |
| 2026-10-21 | [#62712](https://github.com/vllm-project/vllm/pull/62712) | merged | [ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X | `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py`, `tests/models/minimax_m3/amd_specialized_decode/test_ops.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py` |
| 2026-10-16 | [#62035](https://github.com/vllm-project/vllm/pull/62035) | merged | [Perf][Parser] Stream MiniMax M2 tool argument values incrementally (16 KB call: 5.9 s to 26 ms) | `tests/parser/engine/test_minimax_m2.py`, `vllm/parser/minimax_m2.py` |
| 2026-10-14 | [#60990](https://github.com/vllm-project/vllm/pull/60990) | merged | [Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer | `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-10-13 | [#55838](https://github.com/vllm-project/vllm/pull/55838) | merged | [Perf][Attention][MiniMax-M3] Select CUTLASS MSA by EAGLE3 decode shape | `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` |
| 2026-10-12 | [#60917](https://github.com/vllm-project/vllm/pull/60917) | merged | [Fix] MiniMax: fix CUDA IPC handle exchange on cuda-bindings >= 13.4 | `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` |
| 2026-10-11 | [#60684](https://github.com/vllm-project/vllm/pull/60684) | merged | [Perf][MiniMax-M3] MSA prefill attends with the E4M3 query; bump fmha_sm100 to 968061a | `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` |
| 2026-10-08 | [#54597](https://github.com/vllm-project/vllm/pull/54597) | merged | [Bugfix][MiniMax-M3] Guard sparse decode sentinel indices | `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-10-07 | [#59285](https://github.com/vllm-project/vllm/pull/59285) | merged | [ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors | `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py` |
| 2026-10-07 | [#60194](https://github.com/vllm-project/vllm/pull/60194) | merged | [Bugfix][MiniMax-M3] Fence decode indexer shared-memory stage reuse | `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-10-06 | [#59743](https://github.com/vllm-project/vllm/pull/59743) | merged | [Frontend] Port the MiniMax M3 tool parser to the parser engine | `tests/tool_parsers/test_minimax_m3_tool_parser.py`, `vllm/tool_parsers/minimax_m3_tool_parser.py`, `vllm/parser/minimax_m3.py` |
| 2026-10-02 | [#59481](https://github.com/vllm-project/vllm/pull/59481) | merged | [Minimax-M3] Keep the native FP8 MMA in the Triton indexer scorers | `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` |
| 2026-10-02 | [#59613](https://github.com/vllm-project/vllm/pull/59613) | merged | [Bugfix] Fix minimax-m3 multimodal processor compatability with Transformers v5.18 | `vllm/transformers_utils/processors/minimax_m3.py` |
| 2026-10-01 | [#59300](https://github.com/vllm-project/vllm/pull/59300) | merged | [Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path | `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/common/sparse_attention.py` |
| 2026-09-30 | [#57197](https://github.com/vllm-project/vllm/pull/57197) | merged | [Bugfix][PP][Spec Decode] MiniMax-M3 EAGLE3 aux-state relay at PP > 1 and per-stage FlashInfer autotune | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-09-30 | [#56151](https://github.com/vllm-project/vllm/pull/56151) | merged | [Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K | `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-09-30 | [#58648](https://github.com/vllm-project/vllm/pull/58648) | merged | [Bugfix][MiniMax M3] Share target embeddings with MTP under PP | `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/nvidia/mtp.py`, `vllm/models/minimax_m3/amd/model.py` |
| 2026-09-28 | [#59081](https://github.com/vllm-project/vllm/pull/59081) | merged | [Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures. | `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/indexer.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` |
| 2026-09-28 | [#58673](https://github.com/vllm-project/vllm/pull/58673) | merged | [Minimax-M3] Add Encoder CUDA graph support | `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py`, `vllm/models/minimax_m3/amd/model.py` |
| 2026-09-25 | [#58526](https://github.com/vllm-project/vllm/pull/58526) | merged | [Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope | `vllm/models/minimax_m3/common/vision_tower.py` |
| 2026-09-24 | [#58460](https://github.com/vllm-project/vllm/pull/58460) | merged | [Multimodal] Reuse the supplied tokenizer in the MiniMax-M3 VL processor | `vllm/transformers_utils/processors/minimax_m3.py` |
| 2026-09-24 | [#58512](https://github.com/vllm-project/vllm/pull/58512) | merged | [Minimax-M3][Perf] Use Conv3dLayer for M3 patch embedding | `vllm/models/minimax_m3/common/vision_tower.py` |
| 2026-09-23 | [#58089](https://github.com/vllm-project/vllm/pull/58089) | merged | [ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite | `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` |
| 2026-09-21 | [#54535](https://github.com/vllm-project/vllm/pull/54535) | merged | [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm | `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-09-17 | [#56849](https://github.com/vllm-project/vllm/pull/56849) | merged | [ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy | `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/test_minimax_m3_amd_ops.py` |
| 2026-09-16 | [#53674](https://github.com/vllm-project/vllm/pull/53674) | merged | [Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale | `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`, `tests/kernels/test_minimax_m3_amd_ops.py` |
| 2026-09-14 | [#55235](https://github.com/vllm-project/vllm/pull/55235) | merged | [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts | `vllm/models/minimax_m3/amd/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-09-13 | [#56170](https://github.com/vllm-project/vllm/pull/56170) | merged | [ROCm][Performance] Avoid blocking MiniMax M3 scalar upload | `vllm/models/minimax_m3/common/sparse_attention.py` |
| 2026-09-09 | [#52664](https://github.com/vllm-project/vllm/pull/52664) | merged | [Performance][ROCm] Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path | `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py` |
| 2026-09-03 | [#54682](https://github.com/vllm-project/vllm/pull/54682) | merged | [ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k | `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/indexer.py` |
| 2026-09-03 | [#55057](https://github.com/vllm-project/vllm/pull/55057) | merged | [ROCm][CI] Add MiniMax reduce RMS kernel coverage | `tests/kernels/core/test_minimax_reduce_rms.py` |
| 2026-08-28 | [#52849](https://github.com/vllm-project/vllm/pull/52849) | merged | [ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers | `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/amd/model.py` |
| 2026-08-20 | [#51203](https://github.com/vllm-project/vllm/pull/51203) | merged | [Bugfix][MiniMax-M3] Keep FP8 query allocation stable across CUDA graph replay | `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` |
| 2026-08-02 | [#50032](https://github.com/vllm-project/vllm/pull/50032) | merged | [Attention][MiniMax-M3] Add MSA speculative decode verification | `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py` |
| 2026-07-31 | [#50305](https://github.com/vllm-project/vllm/pull/50305) | merged | [Bugfix] Re-land MiniMax M3 default video processor | `vllm/models/minimax_m3/common/mm_preprocess.py` |
| 2026-07-29 | [#50313](https://github.com/vllm-project/vllm/pull/50313) | merged | Revert "[Misc][Minimax-M3]add default video_processor (#50092)" | `vllm/models/minimax_m3/common/mm_preprocess.py` |
| 2026-07-29 | [#50092](https://github.com/vllm-project/vllm/pull/50092) | merged | [Misc][Minimax-M3]add default video_processor | `vllm/models/minimax_m3/common/mm_preprocess.py` |
| 2026-07-25 | [#49149](https://github.com/vllm-project/vllm/pull/49149) | merged | [Bugfix][MiniMax-M3] Fix token-major top-k buffer handling in Triton … | `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/indexer.py` |
| 2026-07-17 | [#48846](https://github.com/vllm-project/vllm/pull/48846) | merged | [Bugfix][Tool Parser] Preserve whitespace in parameter values (MiniMax M2, Qwen3, MiniCPM5 XML) | `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/parser/minimax_m2.py` |
| 2026-07-14 | [#48523](https://github.com/vllm-project/vllm/pull/48523) | merged | [Bugfix] Skip minimax_m3 tool parser tests when Rust extension is absent | `tests/tool_parsers/test_minimax_m3_tool_parser.py` |
| 2026-07-14 | [#47984](https://github.com/vllm-project/vllm/pull/47984) | merged | [ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA | `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-07-14 | [#44849](https://github.com/vllm-project/vllm/pull/44849) | merged | [ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER | `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` |
| 2026-07-13 | [#47287](https://github.com/vllm-project/vllm/pull/47287) | merged | [ROCm][MiniMax-M3] Add AITER sparse paged attention | `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py` |
| 2026-07-08 | [#47158](https://github.com/vllm-project/vllm/pull/47158) | merged | [ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8 | `tests/kernels/test_minimax_m3_amd_ops.py` |
| 2026-07-08 | [#47631](https://github.com/vllm-project/vllm/pull/47631) | merged | [Perf] Minimax M3 - Support cross-layer allreduce-norm fusion | `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/deepseek_v32/nvidia/model.py` |
| 2026-07-08 | [#46117](https://github.com/vllm-project/vllm/pull/46117) | merged | [ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3 | `tests/kernels/test_minimax_m3_amd_ops.py` |
| 2026-07-08 | [#47502](https://github.com/vllm-project/vllm/pull/47502) | merged | [Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels | `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py` |
| 2026-07-01 | [#47269](https://github.com/vllm-project/vllm/pull/47269) | merged | [ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing | `vllm/models/minimax_m3/amd/model.py` |
| 2026-06-27 | [#46474](https://github.com/vllm-project/vllm/pull/46474) | merged | [ROCm][Perf] Fused shared expert for Minimax M3 | `vllm/models/minimax_m3/amd/model.py` |
| 2026-06-26 | [#46545](https://github.com/vllm-project/vllm/pull/46545) | merged | [ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model | `vllm/models/minimax_m3/amd/model.py` |
| 2026-06-26 | [#46419](https://github.com/vllm-project/vllm/pull/46419) | merged | [ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4 | `vllm/models/minimax_m3/amd/model.py` |
| 2026-06-25 | [#46546](https://github.com/vllm-project/vllm/pull/46546) | merged | [ROCm][ [Perf] sparse attention optimization on minimax-m3 | `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py` |
| 2026-06-24 | [#45810](https://github.com/vllm-project/vllm/pull/45810) | merged | [Model][MiniMax-M3] Add pipeline parallelism support | `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-06-23 | [#45718](https://github.com/vllm-project/vllm/pull/45718) | merged | [Bugfix] Parse MiniMax M3 streaming reasoning by text markers | `vllm/reasoning/minimax_m3_reasoning_parser.py`, `tests/reasoning/test_minimax_m3_reasoning_parser.py` |
| 2026-06-23 | [#45892](https://github.com/vllm-project/vllm/pull/45892) | merged | [Minimax-M3] BF16/FP8 Indexer using MSA | `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-06-21 | [#45935](https://github.com/vllm-project/vllm/pull/45935) | merged | [Model]Fix MiniMaxM2ForCausalLM perf regression | `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `tests/kernels/core/test_minimax_reduce_rms.py` |
| 2026-06-17 | [#45896](https://github.com/vllm-project/vllm/pull/45896) | merged | [feature] MiniMax-M3-MXFP4 support added | `vllm/models/minimax_m3/amd/model.py` |
| 2026-06-17 | [#45720](https://github.com/vllm-project/vllm/pull/45720) | merged | [Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype | `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py` |
| 2026-06-16 | [#45701](https://github.com/vllm-project/vllm/pull/45701) | merged | [Frontend] Add Streaming Parser Engine and new MinimaxM2 Parser | `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py` |
| 2026-06-15 | [#45381](https://github.com/vllm-project/vllm/pull/45381) | merged | [Model] Add MiniMax M3 support | `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/common/ops/index_topk.py` |
| 2026-06-09 | [#44983](https://github.com/vllm-project/vllm/pull/44983) | merged | [Bugfix] Fix minimax_qk_norm_fusion | `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` |
| 2026-05-30 | [#38445](https://github.com/vllm-project/vllm/pull/38445) | merged | [PERF]MiniMax-M2 gate kernel | `vllm/model_executor/models/minimax_m2.py` |
| 2026-05-26 | [#43410](https://github.com/vllm-project/vllm/pull/43410) | merged | [Kernel] Porting fuse_minimax_qk_norm to manual fusion | `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `vllm/model_executor/layers/minimax_rms_norm/__init__.py`, `vllm/model_executor/models/minimax_m2.py` |
| 2026-05-19 | [#43025](https://github.com/vllm-project/vllm/pull/43025) | merged | [Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser | `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2026-05-18 | [#43006](https://github.com/vllm-project/vllm/pull/43006) | merged | [Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser | `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2026-05-14 | [#39599](https://github.com/vllm-project/vllm/pull/39599) | merged | fix(tool-parser): preserve "none"/"nil" strings as valid enum values in minimax_m2 | `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2026-04-27 | [#38191](https://github.com/vllm-project/vllm/pull/38191) | merged | [Bugfix] Fix k_norm weight sharding in MiniMaxM2Attention when total_num_kv_heads < tp_size | `vllm/model_executor/models/minimax_m2.py` |
| 2026-04-10 | [#37045](https://github.com/vllm-project/vllm/pull/37045) | merged | [Kernel] Porting the TRTLLM minimax_allreduce_rms kernels | `vllm/model_executor/models/minimax_m2.py`, `tests/kernels/core/test_minimax_reduce_rms.py` |
| 2026-04-06 | [#37512](https://github.com/vllm-project/vllm/pull/37512) | merged | MiniMax-M2: add Eagle3 speculative decoding support | `vllm/model_executor/models/minimax_m2.py` |
| 2026-03-30 | [#36965](https://github.com/vllm-project/vllm/pull/36965) | merged | [Model][Quantization] Add GGUF support for MiniMax-M2.1 | `vllm/model_executor/models/minimax_m2.py` |
| 2026-03-26 | [#37214](https://github.com/vllm-project/vllm/pull/37214) | merged | Fix minimax m2.5 nvfp4 kv scales weight loading | `vllm/model_executor/models/minimax_m2.py` |
| 2026-03-12 | [#35895](https://github.com/vllm-project/vllm/pull/35895) | merged | [Bugfix] Fix minimax_m2 tool parser when stream interval > 1 | `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_use/test_minimax_m2_tool_parser.py` |
| 2026-02-26 | [#35352](https://github.com/vllm-project/vllm/pull/35352) | merged | [Bug] Fix missing tag after tool call in MiniMax 2.1 | `vllm/reasoning/minimax_m2_reasoning_parser.py` |
| 2026-01-24 | [#32763](https://github.com/vllm-project/vllm/pull/32763) | merged | feat: Complete LoRA support for MiniMaxM2 Fixes #32736 | `vllm/model_executor/models/minimax_m2.py` |
| 2026-01-15 | [#32342](https://github.com/vllm-project/vllm/pull/32342) | merged | Fix optional parameter parsing in MiniMax M2 tool parser #32278 | `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-12-29 | [#31493](https://github.com/vllm-project/vllm/pull/31493) | merged | Optimize QKNorm for MiniMax-M2/M2.1 | `vllm/model_executor/models/minimax_m2.py` |
| 2025-12-22 | [#31083](https://github.com/vllm-project/vllm/pull/31083) | merged | Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs | `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-12-17 | [#30555](https://github.com/vllm-project/vllm/pull/30555) | merged | [Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction | `tests/tool_use/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-12-11 | [#29882](https://github.com/vllm-project/vllm/pull/29882) | merged | [bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content. | `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py` |
| 2025-12-10 | [#30384](https://github.com/vllm-project/vllm/pull/30384) | merged | [BugFix] Fix minimax m2 model rotary_dim | `vllm/model_executor/models/minimax_m2.py` |
| 2025-10-29 | [#27627](https://github.com/vllm-project/vllm/pull/27627) | merged | Fix MiniMax-M2 rmsnorm precision and remove useless code | `vllm/model_executor/models/minimax_m2.py` |
| 2025-10-27 | [#27537](https://github.com/vllm-project/vllm/pull/27537) | merged | Fix MiniMax-M2 copyright | `vllm/model_executor/models/minimax_m2.py` |
| 2025-10-26 | [#27535](https://github.com/vllm-project/vllm/pull/27535) | merged | [Model][MiniMax-M2] Support MiniMax-M2 Model | `vllm/model_executor/models/minimax_m2.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py` |

## 逐 PR diff 审计卡

### PR #64856 - [Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace

- 链接: https://github.com/vllm-project/vllm/pull/64856
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`；关联提交 `6a6f8047968a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+72/-142，可读 patch 308 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace」；主要实现面是 `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +47/-34 (81 lines); hunks: -14,14 +14,17; -40,7 +43,6; symbols: MiniMaxM3SparseMSADecodeMetadata, MiniMaxM3SparseMSAPrefillMetadata, _shared_prefill_workspace, MiniMaxM3SparseMSAMetadataBuilder，涉及 `MiniMaxM3SparseMSADecodeMetadata, MiniMaxM3SparseMSAPrefillMetadata, _shared_prefill_workspace`；`tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +25/-108 (133 lines); hunks: -4,7 +4,6; -45,7 +44,6; symbols: test_msa_metadata_builder_prepares_cutlass_for_regular_decode, test_msa_metadata_builder_reserves_prefill_workspace_only_on_sm107, test_msa_nvfp4_impls_share_one_reserved_prefill_workspace, test_msa_cutlass_plan_cache_keys_query_len，涉及 `test_msa_metadata_builder_prepares_cutlass_for_regular_decode, test_msa_metadata_builder_reserves_prefill_workspace_only_on_sm107, test_msa_nvfp4_impls_share_one_reserved_prefill_workspace`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +47/-34 (81 lines); hunks: -14,14 +14,17; -40,7 +43,6; symbols: MiniMaxM3SparseMSADecodeMetadata, MiniMaxM3SparseMSAPrefillMetadata, _shared_prefill_workspace, MiniMaxM3SparseMSAMetadataBuilder
  - `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +25/-108 (133 lines); hunks: -4,7 +4,6; -45,7 +44,6; symbols: test_msa_metadata_builder_prepares_cutlass_for_regular_decode, test_msa_metadata_builder_reserves_prefill_workspace_only_on_sm107, test_msa_nvfp4_impls_share_one_reserved_prefill_workspace, test_msa_cutlass_plan_cache_keys_query_len
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -14,14 +14,17 @@
-from dataclasses import dataclass, fields, replace
+import weakref
+from contextlib import nullcontext
+from dataclasses import dataclass, replace
-from vllm.config import VllmConfig
+from vllm.config import VllmConfig, get_current_vllm_config
diff -- tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py
@@ -4,7 +4,6 @@
-from dataclasses import fields, replace
@@ -45,7 +44,6 @@
-    MiniMaxM3SparseMSAPrefillMetadata,
@@ -343,38 +341,35 @@ def test_msa_metadata_builder_prepares_cutlass_for_regular_decode(
-@pytest.mark.parametrize("is_sm107", [True, False])
-def test_msa_metadata_builder_reserves_prefill_workspace_only_on_sm107(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +47/-34
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +25/-108
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65763 - [CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic

- 链接: https://github.com/vllm-project/vllm/pull/65763
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`；关联提交 `4ab4404e2444`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+21/-4，可读 patch 43 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic」；主要实现面是 `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/attention/test_minimax_m3.py` modified +21/-4 (25 lines); hunks: -1594,6 +1594,9 @@ def test_decode_index_topk_correctness(; -1615,14 +1618,28 @@ def test_decode_index_topk_correctness(; symbols: test_decode_index_topk_correctness，涉及 `test_decode_index_topk_correctness`。
- 代码 diff 细节:
  - `tests/kernels/attention/test_minimax_m3.py` modified +21/-4 (25 lines); hunks: -1594,6 +1594,9 @@ def test_decode_index_topk_correctness(; -1615,14 +1618,28 @@ def test_decode_index_topk_correctness(; symbols: test_decode_index_topk_correctness
- 关键代码摘录:

```diff
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -1594,6 +1594,9 @@ def test_decode_index_topk_correctness(
+    # A local generator, so the inputs don't depend on the RNG state that
+    # earlier tests in the shard leave behind.
+    gen = torch.Generator(device="cuda").manual_seed(0)
@@ -1615,14 +1618,28 @@ def test_decode_index_topk_correctness(
-        num_pages, device="cuda", dtype=torch.int32
+        num_pages, device="cuda", dtype=torch.int32, generator=gen
```

- 已读文件:
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +21/-4
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65537 - [MiniMax-M3] Support sequence parallelism with pipeline parallelism

- 链接: https://github.com/vllm-project/vllm/pull/65537
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `213e64562ba6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+13/-3，可读 patch 44 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MiniMax-M3] Support sequence parallelism with pipeline parallelism」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[MiniMax-M3] Support sequence parallelism with pipeline parallelism」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +13/-3 (16 lines); hunks: -241,8 +241,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -449,7 +448,8 @@ def __init__(; symbols: _use_sequence_parallel, __init__, forward，涉及 `_use_sequence_parallel, __init__, forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +13/-3 (16 lines); hunks: -241,8 +241,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -449,7 +448,8 @@ def __init__(; symbols: _use_sequence_parallel, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -241,8 +241,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:
-        parallel_config.pipeline_parallel_size == 1
-        and parallel_config.enable_expert_parallel
+        parallel_config.enable_expert_parallel
@@ -449,7 +448,8 @@ def __init__(
-            reduce_results=reduce_results,
+            # Under SP the forward reduce-scatters the output itself.
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +13/-3
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #65432 - [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP

- 链接: https://github.com/vllm-project/vllm/pull/65432
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/models/minimax_m3/amd/indexer_nvfp4.py`；关联提交 `ca8bd4c05506`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+28/-0，可读 patch 53 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP」；主要实现面是 `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +5/-0 (5 lines); hunks: -36,6 +36,10; -149,6 +153,7 @@ def _decode_cp(self, num_decodes: int, query_len: int):; symbols: _cp_requests, _decode_cp，涉及 `_cp_requests, _decode_cp`；`tests/kernels/attention/test_minimax_m3_nvfp4_index.py` modified +23/-0 (23 lines); hunks: -18,6 +18,7; -502,3 +503,25 @@ def run(shared, mq):; symbols: run, test_decode_cp_gate，涉及 `run, test_decode_cp_gate`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +5/-0 (5 lines); hunks: -36,6 +36,10; -149,6 +153,7 @@ def _decode_cp(self, num_decodes: int, query_len: int):; symbols: _cp_requests, _decode_cp
  - `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` modified +23/-0 (23 lines); hunks: -18,6 +18,7; -502,3 +503,25 @@ def run(shared, mq):; symbols: run, test_decode_cp_gate
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/indexer_nvfp4.py
@@ -36,6 +36,10 @@
+# DSpark 7 steps with fewer requests than this score locally: CP's cross-rank
+# hops cost a fixed ~13 us a layer, more than the single-head scorer below it.
+# The batch's context is unknown at CUDA graph capture, so the gate is by count.
+CP_MIN_REQS = 3
@@ -149,6 +153,7 @@ def _decode_cp(self, num_decodes: int, query_len: int):
+            or (query_len == 2 * CP_QUERY_LEN and num_decodes < CP_MIN_REQS)
diff -- tests/kernels/attention/test_minimax_m3_nvfp4_index.py
@@ -18,6 +18,7 @@
+from vllm.models.minimax_m3.amd import indexer_nvfp4  # noqa: E402
@@ -502,3 +503,25 @@ def run(shared, mq):
+@pytest.mark.parametrize(
+    ("num_decodes", "query_len", "scores_with_cp"),
+    [
+        (indexer_nvfp4.CP_MIN_REQS - 1, 8, False),  # DSpark 7 below the gate
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +5/-0
  - tests: `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` modified +23/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65087 - [ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer

- 链接: https://github.com/vllm-project/vllm/pull/65087
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`；关联提交 `c0c8373c2319`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+130/-37，可读 patch 292 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer」；主要实现面是 `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py` modified +126/-36 (162 lines); hunks: -4,6 +4,10; -72,8 +76,10 @@ def _comp(k, i):; symbols: _comp, compile_topk_prefill, Shared, kernel，涉及 `_comp, compile_topk_prefill, Shared`；`vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py` modified +1/-1 (2 lines); hunks: -27,7 +27,7 @@ def _get_prefill_kernel(strips: int):; symbols: _get_prefill_kernel, _get_decode_kernel, supports_index_topk，涉及 `_get_prefill_kernel, _get_decode_kernel, supports_index_topk`；`tests/kernels/attention/test_minimax_m3_index_topk_decode.py` modified +3/-0 (3 lines); hunks: -111,6 +111,9 @@ def _aiter_topk(score, bt, seq, msl, nkv, pad, **kw):; symbols: _aiter_topk，涉及 `_aiter_topk`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py` modified +126/-36 (162 lines); hunks: -4,6 +4,10; -72,8 +76,10 @@ def _comp(k, i):; symbols: _comp, compile_topk_prefill, Shared, kernel
  - `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py` modified +1/-1 (2 lines); hunks: -27,7 +27,7 @@ def _get_prefill_kernel(strips: int):; symbols: _get_prefill_kernel, _get_decode_kernel, supports_index_topk
  - `tests/kernels/attention/test_minimax_m3_index_topk_decode.py` modified +3/-0 (3 lines); hunks: -111,6 +111,9 @@ def _aiter_topk(score, bt, seq, msl, nkv, pad, **kw):; symbols: _aiter_topk
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py
@@ -4,6 +4,10 @@
+Decode gives each row four waves: wave w walks windows w, w + 4, ... with its
+own candidates and running top 16, then the four lists merge by an exact rank
+over the (key, index) order.
@@ -72,8 +76,10 @@ def _comp(k, i):
-    assert strips == 26 if decode else strips in PREFILL_STRIPS
+    assert strips == 16 if decode else strips in PREFILL_STRIPS
diff -- vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py
@@ -27,7 +27,7 @@ def _get_prefill_kernel(strips: int):
-    return _kernel.compile_topk_prefill(26, decode=True)
+    return _kernel.compile_topk_prefill(16, decode=True)
diff -- tests/kernels/attention/test_minimax_m3_index_topk_decode.py
@@ -111,6 +111,9 @@ def _aiter_topk(score, bt, seq, msl, nkv, pad, **kw):
+    (100, 4, 1 << 20, (1, 1 << 20), 1, 1),  # 100 requests, every window count
+    (16, 1, 1 << 20, (1020 * BLOCK, 1030 * BLOCK), 1, 1),  # waves 0 and 1 meet
+    (16, 1, 1 << 20, (4090 * BLOCK, 4100 * BLOCK), 1, 1),  # second trip of the waves
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py` modified +126/-36; `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py` modified +1/-1
  - tests: `tests/kernels/attention/test_minimax_m3_index_topk_decode.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65496 - [Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism

- 链接: https://github.com/vllm-project/vllm/pull/65496
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `cc329910bd2e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-2，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +5/-2 (7 lines); hunks: -1395,8 +1395,11 @@ def forward_input_norm(; symbols: forward_input_norm，涉及 `forward_input_norm`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +5/-2 (7 lines); hunks: -1395,8 +1395,11 @@ def forward_input_norm(; symbols: forward_input_norm
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -1395,8 +1395,11 @@ def forward_input_norm(
-            # wrappers installed after construction change the key).
-            mxfp8 = _consumes_mxfp8_128x4(self.self_attn.qkv_proj)
+            # wrappers installed after construction change the key), but not
+            # under sequence parallelism, which all-gathers the norm output.
+            mxfp8 = not self.use_sequence_parallel and _consumes_mxfp8_128x4(
+                self.self_attn.qkv_proj
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #65226 - [Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences

- 链接: https://github.com/vllm-project/vllm/pull/65226
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/encoder_cudagraph.py`；关联提交 `9a519c0585b6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-19，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/encoder_cudagraph.py`；技术摘要: 覆盖「[Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences」；主要实现面是 `vllm/models/minimax_m3/common/encoder_cudagraph.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/encoder_cudagraph.py` modified +7/-19 (26 lines); hunks: -32,7 +32,6 @@ class MiniMaxM3EncoderCudaGraphMixin(SupportsEncoderCudaGraph):; -73,20 +72,12 @@ def get_encoder_cudagraph_config(self) -> "EncoderCudaGraphC...; symbols: MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens, pad_rope_planes，涉及 `MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/encoder_cudagraph.py` modified +7/-19 (26 lines); hunks: -32,7 +32,6 @@ class MiniMaxM3EncoderCudaGraphMixin(SupportsEncoderCudaGraph):; -73,20 +72,12 @@ def get_encoder_cudagraph_config(self) -> "EncoderCudaGraphC...; symbols: MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens, pad_rope_planes
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/encoder_cudagraph.py
@@ -32,7 +32,6 @@ class MiniMaxM3EncoderCudaGraphMixin(SupportsEncoderCudaGraph):
-    _encoder_cg_pad_totals: dict[int, int] = {}
@@ -73,20 +72,12 @@ def get_encoder_cudagraph_config(self) -> "EncoderCudaGraphConfig":
-        pad_totals = self._encoder_cg_pad_totals
-            # Varlen attention requires cu_seqlens[-1] to equal the number of
-            # rows actually passed in. The captured buffers are sized for the
-            # full token budget, so a smaller real batch has to be completed
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/encoder_cudagraph.py` modified +7/-19
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/common/encoder_cudagraph.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #64475 - [MiniMax-M3.1][P/D] NIXL KV-head re-sharding for per-head-contiguous NVFP4 pages

- 链接: https://github.com/vllm-project/vllm/pull/64475
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`；关联提交 `ca66f0906ffa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+188/-14，可读 patch 332 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MiniMax-M3.1][P/D] NIXL KV-head re-sharding for per-head-contiguous NVFP4 pages」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`；技术摘要: 覆盖「[MiniMax-M3.1][P/D] NIXL KV-head re-sharding for per-head-contiguous NVFP4 pages」；主要实现面是 `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +1/-0 (1 lines); hunks: -119,6 +119,7 @@ def customize_spec(cls, spec: AttentionSpec) -> AttentionSpec:; symbols: customize_spec，涉及 `customize_spec`；`tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +125/-0 (125 lines); hunks: -826,6 +826,131 @@ def test_sparse_full_nvfp4(num_tokens, num_kv_heads, block...; symbols: test_sparse_full_nvfp4, test_nvfp4_kv_head_major_slots_match_insert, insert，涉及 `test_sparse_full_nvfp4, test_nvfp4_kv_head_major_slots_match_insert, insert`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +1/-0 (1 lines); hunks: -119,6 +119,7 @@ def customize_spec(cls, spec: AttentionSpec) -> AttentionSpec:; symbols: customize_spec
  - `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +125/-0 (125 lines); hunks: -826,6 +826,131 @@ def test_sparse_full_nvfp4(num_tokens, num_kv_heads, block...; symbols: test_sparse_full_nvfp4, test_nvfp4_kv_head_major_slots_match_insert, insert
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -119,6 +119,7 @@ def customize_spec(cls, spec: AttentionSpec) -> AttentionSpec:
+            kv_head_major_slots=True,
diff -- tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py
@@ -826,6 +826,131 @@ def test_sparse_full_nvfp4(num_tokens, num_kv_heads, block_size, kv_scales):
+@pytest.mark.skipif(
+    not torch.cuda.is_available() or torch.cuda.get_device_capability()[0] != 10,
+    reason="NVFP4 KV caches need SM100",
+)
+@pytest.mark.parametrize("num_tokens", [7, 513])
+@pytest.mark.parametrize("block_size", [16, 128])
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +1/-0
  - tests: `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +125/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62270 - [ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942

- 链接: https://github.com/vllm-project/vllm/pull/62270
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py` 等 6 个文件；关联提交 `901f26dfcd7a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+266/-74，可读 patch 628 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942」；主要实现面是 `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/indexer.py` modified +17/-6 (23 lines); hunks: -118,7 +118,7 @@ def __init__(; -519,7 +519,9 @@ def select_indexer_impl_cls(; symbols: __init__, select_indexer_impl_cls，涉及 `__init__, select_indexer_impl_cls`；`vllm/models/minimax_m3/amd/mtp.py` modified +11/-8 (19 lines); hunks: -219,14 +219,17 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`；`vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +8/-0 (8 lines); hunks: -10,6 +10,7; -296,6 +297,7 @@ def _insert_index_cache_kernel(; symbols: _insert_index_cache_kernel, minimax_m3_insert_index_cache，涉及 `_insert_index_cache_kernel, minimax_m3_insert_index_cache`；`tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +94/-12 (106 lines); hunks: -16,6 +16,7; -279,7 +280,7 @@ def test_sparse_full(num_tokens, block_size, kv_cache_dtype):; symbols: test_sparse_full, test_sparse_skip_index_branch, _has_native_fp8, test_sparse_full_fp8_index，涉及 `test_sparse_full, test_sparse_skip_index_branch, _has_native_fp8`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/indexer.py` modified +17/-6 (23 lines); hunks: -118,7 +118,7 @@ def __init__(; -519,7 +519,9 @@ def select_indexer_impl_cls(; symbols: __init__, select_indexer_impl_cls
  - `vllm/models/minimax_m3/amd/mtp.py` modified +11/-8 (19 lines); hunks: -219,14 +219,17 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +8/-0 (8 lines); hunks: -10,6 +10,7; -296,6 +297,7 @@ def _insert_index_cache_kernel(; symbols: _insert_index_cache_kernel, minimax_m3_insert_index_cache
  - `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +94/-12 (106 lines); hunks: -16,6 +16,7; -279,7 +280,7 @@ def test_sparse_full(num_tokens, block_size, kv_cache_dtype):; symbols: test_sparse_full, test_sparse_skip_index_branch, _has_native_fp8, test_sparse_full_fp8_index
  - `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` modified +57/-14 (71 lines); hunks: -7,21 +7,35; -51,7 +65,7 @@ def _check_selection(top_bf16: set[int], top_fp8: set[int]) ->...; symbols: _check_selection, test_fp8_index_query_and_cache_decode_topk_matches_bf16, select, test_fp8_index_query_and_cache_prefill_topk_matches_bf16
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/indexer.py
@@ -118,7 +118,7 @@ def __init__(
-            cache_dtype = query_dtype = torch.float8_e4m3fn
+            cache_dtype = query_dtype = current_platform.fp8_dtype()
@@ -519,7 +519,9 @@ def select_indexer_impl_cls(
-    support.
+    support and to ROCm gfx942 (MI300-series, CDNA3). gfx950 (MI350-series)
+    takes the fp8 path through the AITER indexer instead, so this fallback
diff -- vllm/models/minimax_m3/amd/mtp.py
@@ -219,14 +219,17 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                raise NotImplementedError(
-                    f"MiniMax M3 MTP could not select the MSA indexer, leaving "
-                    f"its draft layers on the bf16 indexer, so "
-                    f"indexer_kv_dtype={indexer_kv_dtype!r} has nowhere to go. "
-                    f"See the preceding 'MSA unavailable' log line for why. Drop "
-                    f"indexer_kv_dtype from --attention-config, or speculate "
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -10,6 +10,7 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/indexer.py` modified +17/-6; `vllm/models/minimax_m3/amd/mtp.py` modified +11/-8; `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +8/-0
  - tests: `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +94/-12; `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` modified +57/-14; `tests/kernels/attention/test_minimax_m3.py` modified +32/-9
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64448 - [ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7

- 链接: https://github.com/vllm-project/vllm/pull/64448
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/models/minimax_m3/amd/indexer_msa.py`, `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `vllm/models/minimax_m3/amd/ops/index_cp/host.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_decode/kernel_cp_push.py`；关联提交 `eff37e8e2420`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+113/-16，可读 patch 212 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `vllm/models/minimax_m3/amd/ops/index_cp/host.py`, `vllm/models/minimax_m3/amd/indexer_msa.py`；技术摘要: 覆盖「[ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7」；主要实现面是 `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `vllm/models/minimax_m3/amd/ops/index_cp/host.py`, `vllm/models/minimax_m3/amd/indexer_msa.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +27/-9 (36 lines); hunks: -4,8 +4,9; -22,17 +23,32; symbols: _cp_requests, rocm_nvfp4_indexer_unsupported_reason, _decode_cp, forward，涉及 `_cp_requests, rocm_nvfp4_indexer_unsupported_reason, _decode_cp`；`vllm/models/minimax_m3/amd/ops/index_cp/host.py` modified +1/-7 (8 lines); hunks: -107,17 +107,11 @@ def init(device: torch.device, max_width: int) -> None:; symbols: init，涉及 `init`；`vllm/models/minimax_m3/amd/indexer_msa.py` modified +3/-0 (3 lines); hunks: -147,6 +147,9 @@ class MiniMaxM3IndexerMSAMetadata(MiniMaxM3IndexerMetadata):; symbols: MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder，涉及 `MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder`；`vllm/models/minimax_m3/amd/ops/nvfp4_index_decode/kernel_cp_push.py` modified +2/-0 (2 lines); hunks: -609,3 +609,5 @@ def launch(; symbols: launch，涉及 `launch`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +27/-9 (36 lines); hunks: -4,8 +4,9; -22,17 +23,32; symbols: _cp_requests, rocm_nvfp4_indexer_unsupported_reason, _decode_cp, forward
  - `vllm/models/minimax_m3/amd/ops/index_cp/host.py` modified +1/-7 (8 lines); hunks: -107,17 +107,11 @@ def init(device: torch.device, max_width: int) -> None:; symbols: init
  - `vllm/models/minimax_m3/amd/indexer_msa.py` modified +3/-0 (3 lines); hunks: -147,6 +147,9 @@ class MiniMaxM3IndexerMSAMetadata(MiniMaxM3IndexerMetadata):; symbols: MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder
  - `vllm/models/minimax_m3/amd/ops/nvfp4_index_decode/kernel_cp_push.py` modified +2/-0 (2 lines); hunks: -609,3 +609,5 @@ def launch(; symbols: launch
  - `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` modified +75/-0 (75 lines); hunks: -308,6 +308,81 @@ def test_index_decode_cp_push_all_padding(grid):; symbols: test_index_decode_cp_push_all_padding, test_index_decode_cp_push_split_requests, _prefill_case
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/indexer_nvfp4.py
@@ -4,8 +4,9 @@
-table. With ``indexer_decode_cp`` at TP4, decode steps of 4 rows per request
-and at most 256 requests score context-parallel (``ops/index_cp``).
+table. With ``indexer_decode_cp`` at TP4, decode steps 4/8 rows
+per request (DSpark 3/7) and at most 256 4-row requests score
+context-parallel (``ops/index_cp``).
@@ -22,17 +23,32 @@
diff -- vllm/models/minimax_m3/amd/ops/index_cp/host.py
@@ -107,17 +107,11 @@ def init(device: torch.device, max_width: int) -> None:
-    from vllm.config import get_current_vllm_config
-    # One set of buffers and flags: microbatches would share them.
-    if (
-        tp.world_size != WORLD
-        or not on_gfx950()
-        or get_current_vllm_config().parallel_config.use_ubatching
diff -- vllm/models/minimax_m3/amd/indexer_msa.py
@@ -147,6 +147,9 @@ class MiniMaxM3IndexerMSAMetadata(MiniMaxM3IndexerMetadata):
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/indexer_nvfp4.py` modified +27/-9; `vllm/models/minimax_m3/amd/ops/index_cp/host.py` modified +1/-7; `vllm/models/minimax_m3/amd/indexer_msa.py` modified +3/-0; `vllm/models/minimax_m3/amd/ops/nvfp4_index_decode/kernel_cp_push.py` modified +2/-0
  - tests: `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` modified +75/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64852 - [Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8

- 链接: https://github.com/vllm-project/vllm/pull/64852
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`；关联提交 `318c4db661d9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+336/-3，可读 patch 367 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8」；主要实现面是 `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py` added +164/-0 (164 lines); hunks: -0,0 +1,164; symbols: _gemma_rmsnorm_mxfp8_kernel, gemma_rmsnorm_mxfp8，涉及 `_gemma_rmsnorm_mxfp8_kernel, gemma_rmsnorm_mxfp8`；`tests/models/minimax_m3/test_norm_mxfp8.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _rows, _code_steps, test_input_norm_matches_reference, test_norm_module_accepts_3d_per_head，涉及 `_rows, _code_steps, test_input_norm_matches_reference`；`vllm/models/minimax_m3/nvidia/model.py` modified +57/-3 (60 lines); hunks: -264,8 +264,31 @@ def _mega_moe_expert_weight(; -284,7 +307,33 @@ def forward(; symbols: _mega_moe_expert_weight, _consumes_mxfp8_128x4, MiniMAXGemmaRMSNorm, forward，涉及 `_mega_moe_expert_weight, _consumes_mxfp8_128x4, MiniMAXGemmaRMSNorm`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py` added +164/-0 (164 lines); hunks: -0,0 +1,164; symbols: _gemma_rmsnorm_mxfp8_kernel, gemma_rmsnorm_mxfp8
  - `tests/models/minimax_m3/test_norm_mxfp8.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _rows, _code_steps, test_input_norm_matches_reference, test_norm_module_accepts_3d_per_head
  - `vllm/models/minimax_m3/nvidia/model.py` modified +57/-3 (60 lines); hunks: -264,8 +264,31 @@ def _mega_moe_expert_weight(; -284,7 +307,33 @@ def forward(; symbols: _mega_moe_expert_weight, _consumes_mxfp8_128x4, MiniMAXGemmaRMSNorm, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py
@@ -0,0 +1,164 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Gemma RMSNorm (optionally fused with the residual add) in one Triton pass.
+With an ``sf`` scale buffer the output is E4M3 data plus UE8M0 scales in the
+128x4 swizzled layout, replacing the BF16 norm followed by a separate MXFP8
+quantize (which re-reads the full normed activation). Without it, the output
diff -- tests/models/minimax_m3/test_norm_mxfp8.py
@@ -0,0 +1,115 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The MiniMax-M3 Triton input norm against the FlashInfer norm (plus the
+reference MXFP8 quantize for MXFP8 output): residual and UE8M0 scales bitwise,
+E4M3 codes within one quantization step, BF16 output within one BF16 ulp."""
+import pytest
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -264,8 +264,31 @@ def _mega_moe_expert_weight(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py` added +164/-0; `vllm/models/minimax_m3/nvidia/model.py` modified +57/-3
  - tests: `tests/models/minimax_m3/test_norm_mxfp8.py` added +115/-0
- 验证与风险: diff 自带测试面 `tests/models/minimax_m3/test_norm_mxfp8.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64659 - [Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE

- 链接: https://github.com/vllm-project/vllm/pull/64659
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `37e16689fa4c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+229/-20，可读 patch 559 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14 (190 lines); hunks: -13,6 +13,7; -111,6 +112,7; symbols: _supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel, _maybe_init_gemm_rs，涉及 `_supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14 (190 lines); hunks: -13,6 +13,7; -111,6 +112,7; symbols: _supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel, _maybe_init_gemm_rs
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -13,6 +13,7 @@
+from typing import TYPE_CHECKING
@@ -111,6 +112,7 @@
+    sp_reduce_scatter,
@@ -139,6 +141,9 @@
+if TYPE_CHECKING:
+    from vllm.model_executor.kernels.linear.cute_dsl.gemm_rs_ar import GemmRsAr
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14
- 验证与风险: diff 自带测试面 `tests/kernels/test_gemm_rs_ar.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64474 - [Doc] Fix MiniMax-M3 docstring cross-references

- 链接: https://github.com/vllm-project/vllm/pull/64474
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py`；关联提交 `ee1056b3179a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+4/-4，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] Fix MiniMax-M3 docstring cross-references」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py`；技术摘要: 覆盖「[Doc] Fix MiniMax-M3 docstring cross-references」；主要实现面是 `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/mono/kernels/index_score.py` modified +2/-2 (4 lines); hunks: -373,8 +373,8 @@ def score_task(tk, b, page):; symbols: score_task, q_frag_from, q_frag_head，涉及 `score_task, q_frag_from, q_frag_head`；`vllm/models/minimax_m3/amd/mono/runner.py` modified +1/-1 (2 lines); hunks: -235,7 +235,7 @@ def run_sparse_layer(; symbols: run_sparse_layer，涉及 `run_sparse_layer`；`vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py` modified +1/-1 (2 lines); hunks: -79,7 +79,7 @@ def _fp8_pair(w, sv):; symbols: _fp8_pair, _mfma_fp8_32x32x64，涉及 `_fp8_pair, _mfma_fp8_32x32x64`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/mono/kernels/index_score.py` modified +2/-2 (4 lines); hunks: -373,8 +373,8 @@ def score_task(tk, b, page):; symbols: score_task, q_frag_from, q_frag_head
  - `vllm/models/minimax_m3/amd/mono/runner.py` modified +1/-1 (2 lines); hunks: -235,7 +235,7 @@ def run_sparse_layer(; symbols: run_sparse_layer
  - `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py` modified +1/-1 (2 lines); hunks: -79,7 +79,7 @@ def _fp8_pair(w, sv):; symbols: _fp8_pair, _mfma_fp8_32x32x64
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/mono/kernels/index_score.py
@@ -373,8 +373,8 @@ def score_task(tk, b, page):
-    """(``q_frag``, ``q_frag_head``) reading index q from memory: [token][head]
-    [HEAD_DIM] bf16, ``heads.count`` heads a token."""
+    """(`q_frag`, `q_frag_head`) reading index q from memory:
+    `[token][head][HEAD_DIM]` bf16, `heads.count` heads a token."""
diff -- vllm/models/minimax_m3/amd/mono/runner.py
@@ -235,7 +235,7 @@ def run_sparse_layer(
-        """Sparse layer ``i``: (ars[i % 2][:n], res) -> (ars[(i + 1) % 2][:n], the
+        """Sparse layer `i`: (`ars[i % 2][:n]`, res) -> (`ars[(i + 1) % 2][:n]`, the
diff -- vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py
@@ -79,7 +79,7 @@ def _fp8_pair(w, sv):
-    D[8 (i // 4) + 4 h + i % 4][r]."""
+    `D[8 (i // 4) + 4 h + i % 4][r]`."""
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/mono/kernels/index_score.py` modified +2/-2; `vllm/models/minimax_m3/amd/mono/runner.py` modified +1/-1; `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #64111 - [New Model] Add MiniMax-M3.1-Flash Model and Kernels

- 链接: https://github.com/vllm-project/vllm/pull/64111
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/minimax_m3_nvfp4_ref.py`, `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `tests/kernels/attention/test_minimax_m3_norm_rope_nvfp4_insert.py` 等 79 个文件；关联提交 `dbd49af22235`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 141 个文件，+27012/-1941，可读 patch 28862 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[New Model] Add MiniMax-M3.1-Flash Model and Kernels」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py`, `vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py`, `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py`；技术摘要: 覆盖「[New Model] Add MiniMax-M3.1-Flash Model and Kernels」；主要实现面是 `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py`, `vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py`, `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py` added +2963/-0 (2963 lines)；`vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py` added +1101/-0 (1101 lines); hunks: -0,0 +1,1101; symbols: _rms_norm, _rope64, _nvfp4_cache_views, _nvfp4_quant32，涉及 `_rms_norm, _rope64, _nvfp4_cache_views`；`vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py` added +902/-0 (902 lines); hunks: -0,0 +1,902; symbols: page16_of, _ld_bf16x4, ld_raw8, bf16x8_f32，涉及 `page16_of, _ld_bf16x4, ld_raw8`；`vllm/models/minimax_m3/nvidia/ops/finalize_allreduce_norm.py` added +781/-0 (781 lines); hunks: -0,0 +1,781; symbols: _ue8m0_ceil, _ue8m0_inverse, _f32x4_to_e4m3x4, _store_global_u32x2，涉及 `_ue8m0_ceil, _ue8m0_inverse, _f32x4_to_e4m3x4`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py` added +2963/-0 (2963 lines)
  - `vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py` added +1101/-0 (1101 lines); hunks: -0,0 +1,1101; symbols: _rms_norm, _rope64, _nvfp4_cache_views, _nvfp4_quant32
  - `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py` added +902/-0 (902 lines); hunks: -0,0 +1,902; symbols: page16_of, _ld_bf16x4, ld_raw8, bf16x8_f32
  - `vllm/models/minimax_m3/nvidia/ops/finalize_allreduce_norm.py` added +781/-0 (781 lines); hunks: -0,0 +1,781; symbols: _ue8m0_ceil, _ue8m0_inverse, _f32x4_to_e4m3x4, _store_global_u32x2
  - `vllm/models/minimax_m3/nvidia/model.py` modified +624/-85 (709 lines); hunks: -18,11 +18,18; -35,6 +42,28; symbols: _supports_qkv_fused_epilogue, _sparse_attention_layer_ids, _is_moe_layer, _use_mega_moe
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py
@@ -0,0 +1,1101 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MXFP8 QKV+indexer GEMM with a fused QK-norm/RoPE + KV-insert epilogue.
+Replaces mm_mxfp8 + fused_minimax_m3_qknorm_rope_kv_insert for the MiniMax-M3
+qkv_proj with one persistent SM100 kernel. Per 128-col head tile, the
+epilogue applies Gemma RMSNorm + partial NeoX RoPE to the f32 accumulator
diff -- vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py
@@ -0,0 +1,902 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# SPDX-License-Identifier: MIT
+# Copyright (C) 2026, Advanced Micro Devices, Inc. All rights reserved.
+"""K1 ``mono_pre``: one MiniMax-M3 sparse layer, input norm through cache insert.
+One launch per layer and rank, ``BLOCKS`` CTAs x ``THREADS`` threads, for S =
diff -- vllm/models/minimax_m3/nvidia/ops/finalize_allreduce_norm.py
@@ -0,0 +1,781 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/mono/kernels/post_attn.py` added +2963/-0; `vllm/models/minimax_m3/nvidia/ops/qkv_index_fused_epilogue.py` added +1101/-0; `vllm/models/minimax_m3/amd/mono/kernels/pre_attn.py` added +902/-0; `vllm/models/minimax_m3/nvidia/ops/finalize_allreduce_norm.py` added +781/-0; `vllm/models/minimax_m3/nvidia/model.py` modified +624/-85; `vllm/models/minimax_m3/nvidia/ops/dense_gemm1_mxfp8.py` added +664/-0
- 验证与风险: diff 自带测试面 `tests/config/test_speculative_draft_hf_overrides.py`, `tests/distributed/test_custom_all_reduce.py`, `tests/kernels/attention/minimax_m3_nvfp4_ref.py`, `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64037 - [Kernel][MiniMax-M3] Enable SM90 split-K in the Triton indexer

- 链接: https://github.com/vllm-project/vllm/pull/64037
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`；关联提交 `a94b768d964e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+22/-13，可读 patch 52 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel][MiniMax-M3] Enable SM90 split-K in the Triton indexer」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Kernel][MiniMax-M3] Enable SM90 split-K in the Triton indexer」；主要实现面是 `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +10/-6 (16 lines); hunks: -703,15 +703,19 @@ def minimax_m3_index_score(; symbols: minimax_m3_index_score，涉及 `minimax_m3_index_score`；`tests/kernels/attention/test_minimax_m3.py` modified +12/-7 (19 lines); hunks: -627,13 +627,18 @@ def _reference_decode_index_score(; symbols: _reference_decode_index_score, test_prefill_index_topk_correctness，涉及 `_reference_decode_index_score, test_prefill_index_topk_correctness`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +10/-6 (16 lines); hunks: -703,15 +703,19 @@ def minimax_m3_index_score(; symbols: minimax_m3_index_score
  - `tests/kernels/attention/test_minimax_m3.py` modified +12/-7 (19 lines); hunks: -627,13 +627,18 @@ def _reference_decode_index_score(; symbols: _reference_decode_index_score, test_prefill_index_topk_correctness
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -703,15 +703,19 @@ def minimax_m3_index_score(
-    SCORE_TARGET_GRID = 48
+    # Splits write disjoint score columns, preserving the unsplit result.
+    if current_platform.is_cuda() and current_platform.is_device_capability((12, 0)):
+        score_target_grid = 48
+    elif current_platform.is_cuda() and current_platform.is_device_capability_family(
+        90
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -627,13 +627,18 @@ def _reference_decode_index_score(
-@pytest.mark.parametrize("force_split_k", [False, True])
-def test_prefill_index_topk_correctness(monkeypatch, prefix_len, force_split_k):
-    if force_split_k:
-        # Take the SM12.0-only split-K launch on any CUDA GPU.
-        monkeypatch.setattr(
-            current_platform, "is_device_capability", lambda cap, *_: cap == (12, 0)
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +10/-6
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +12/-7
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63637 - [ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj

- 链接: https://github.com/vllm-project/vllm/pull/63637
- 状态/时间: merged / 2026-10-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/__init__.py`, `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py`；关联提交 `1cb31be70284`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+371/-28，可读 patch 659 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/__init__.py`；技术摘要: 覆盖「[ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj」；主要实现面是 `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py` modified +94/-8 (102 lines); hunks: -8,9 +8,13; -21,6 +25,11; symbols: _gemma_fused_add_rmsnorm_kernel, _num_warps, gemma_fused_add_rmsnorm, gemma_fused_add_rmsnorm_mxfp8，涉及 `_gemma_fused_add_rmsnorm_kernel, _num_warps, gemma_fused_add_rmsnorm`；`vllm/models/minimax_m3/amd/model.py` modified +46/-5 (51 lines); hunks: -36,6 +36,9; -50,6 +53,10; symbols: __init__, forward, _insert_aiter_sparse_pa_kv, _run_attention，涉及 `__init__, forward, _insert_aiter_sparse_pa_kv`；`vllm/models/minimax_m3/amd/ops/__init__.py` modified +2/-0 (2 lines); hunks: -9,6 +9,7; -19,6 +20,7；`tests/kernels/test_minimax_m3_amd_ops.py` modified +156/-1 (157 lines); hunks: -6,9 +6,13; -39,10 +43,15; symbols: test_num_warps_monotonic, _mxfp8_edge_case_inputs, test_gemma_fused_add_rmsnorm_mxfp8_bitwise_eq_unfused, _spy，涉及 `test_num_warps_monotonic, _mxfp8_edge_case_inputs, test_gemma_fused_add_rmsnorm_mxfp8_bitwise_eq_unfused`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py` modified +94/-8 (102 lines); hunks: -8,9 +8,13; -21,6 +25,11; symbols: _gemma_fused_add_rmsnorm_kernel, _num_warps, gemma_fused_add_rmsnorm, gemma_fused_add_rmsnorm_mxfp8
  - `vllm/models/minimax_m3/amd/model.py` modified +46/-5 (51 lines); hunks: -36,6 +36,9; -50,6 +53,10; symbols: __init__, forward, _insert_aiter_sparse_pa_kv, _run_attention
  - `vllm/models/minimax_m3/amd/ops/__init__.py` modified +2/-0 (2 lines); hunks: -9,6 +9,7; -19,6 +20,7
  - `tests/kernels/test_minimax_m3_amd_ops.py` modified +156/-1 (157 lines); hunks: -6,9 +6,13; -39,10 +43,15; symbols: test_num_warps_monotonic, _mxfp8_edge_case_inputs, test_gemma_fused_add_rmsnorm_mxfp8_bitwise_eq_unfused, _spy
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py
@@ -8,9 +8,13 @@
-Two entry points:
+Entry points:
+  * ``gemma_fused_add_rmsnorm_mxfp8(x, res, w, eps)``
+        -> (MXFP8 values, E8M0 scales, x + res): the fused add + norm with the
+           per-32-block MXFP8 activation quant as an epilogue, so a following
+           MXFP8 linear need not quantize its input again.
diff -- vllm/models/minimax_m3/amd/model.py
@@ -36,6 +36,9 @@
+from vllm.model_executor.kernels.linear.mxfp8.rocm_native import (
+    RocmDotScaledMxfp8LinearKernel,
+)
@@ -50,6 +53,10 @@
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
diff -- vllm/models/minimax_m3/amd/ops/__init__.py
@@ -9,6 +9,7 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/gemma_rmsnorm.py` modified +94/-8; `vllm/models/minimax_m3/amd/model.py` modified +46/-5; `vllm/models/minimax_m3/amd/ops/__init__.py` modified +2/-0
  - tests: `tests/kernels/test_minimax_m3_amd_ops.py` modified +156/-1
- 验证与风险: diff 自带测试面 `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/test_minimax_m3_amd_ops.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57420 - [Kernel][MiniMax-M3] Add Triton query-tiled sparse prefill tuned on Hopper

- 链接: https://github.com/vllm-project/vllm/pull/57420
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py`；关联提交 `8e26dec5f5ef`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+334/-8，可读 patch 434 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel][MiniMax-M3] Add Triton query-tiled sparse prefill tuned on Hopper」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`；技术摘要: 覆盖「[Kernel][MiniMax-M3] Add Triton query-tiled sparse prefill tuned on Hopper」；主要实现面是 `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py` added +279/-0 (279 lines); hunks: -0,0 +1,279; symbols: _gqa_sparse_fwd_tiled_kernel, minimax_m3_sparse_attn，涉及 `_gqa_sparse_fwd_tiled_kernel, minimax_m3_sparse_attn`；`vllm/models/minimax_m3/common/sparse_attention.py` modified +12/-3 (15 lines); hunks: -5,8 +5,9; -28,13 +29,21；`tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py` modified +14/-4 (18 lines); hunks: -26,6 +26,15; -68,8 +77,9 @@ def _make_kv_cache(num_blocks: int, seed: int):; symbols: _make_kv_cache, test_minimax_m3_sparse_prefill_fp8_kv_scales，涉及 `_make_kv_cache, test_minimax_m3_sparse_prefill_fp8_kv_scales`；`tests/kernels/attention/test_minimax_m3.py` modified +12/-1 (13 lines); hunks: -43,6 +43,15; -1587,6 +1596,7 @@ def _reference_sparse_attn(; symbols: kv_layout, _reference_sparse_attn, test_prefill_sparse_attention_correctness，涉及 `kv_layout, _reference_sparse_attn, test_prefill_sparse_attention_correctness`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py` added +279/-0 (279 lines); hunks: -0,0 +1,279; symbols: _gqa_sparse_fwd_tiled_kernel, minimax_m3_sparse_attn
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +12/-3 (15 lines); hunks: -5,8 +5,9; -28,13 +29,21
  - `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py` modified +14/-4 (18 lines); hunks: -26,6 +26,15; -68,8 +77,9 @@ def _make_kv_cache(num_blocks: int, seed: int):; symbols: _make_kv_cache, test_minimax_m3_sparse_prefill_fp8_kv_scales
  - `tests/kernels/attention/test_minimax_m3.py` modified +12/-1 (13 lines); hunks: -43,6 +43,15; -1587,6 +1596,7 @@ def _reference_sparse_attn(; symbols: kv_layout, _reference_sparse_attn, test_prefill_sparse_attention_correctness
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py
@@ -0,0 +1,279 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Hopper query-tiled sparse prefill attention for MiniMax M3."""
+import torch
+from vllm.models.minimax_m3.common.ops.sparse_attn import (
+    _FP8_DTYPES,
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -5,8 +5,9 @@
-builder, and the impl that reads the indexer's top-k from that buffer. The Triton
-attend kernel lives here; the SM100 (MSA)
+builder, and the impl that reads the indexer's top-k from that buffer. The generic
+Triton attend kernel lives in ``common/ops``; Hopper uses the query-tiled prefill
+kernel in ``nvidia/ops``. The SM100 (MSA)
@@ -28,13 +29,21 @@
diff -- tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py
@@ -26,6 +26,15 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/ops/sparse_prefill.py` added +279/-0; `vllm/models/minimax_m3/common/sparse_attention.py` modified +12/-3
  - tests: `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py` modified +14/-4; `tests/kernels/attention/test_minimax_m3.py` modified +12/-1
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62141 - [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355

- 链接: https://github.com/vllm-project/vllm/pull/62141
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`；关联提交 `6fe3d447ac64`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+267/-8，可读 patch 374 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355」；主要实现面是 `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/attention/test_minimax_m3.py` modified +209/-0 (209 lines); hunks: -956,6 +956,215 @@ def test_msa_indexer_impl_matches_triton(topk, index_dtype...; symbols: test_msa_indexer_impl_matches_triton, _reference_aiter_sparse_table, test_aiter_indexer_impl_matches_reference，涉及 `test_msa_indexer_impl_matches_triton, _reference_aiter_sparse_table, test_aiter_indexer_impl_matches_reference`。
- 代码 diff 细节:
  - `tests/kernels/attention/test_minimax_m3.py` modified +209/-0 (209 lines); hunks: -956,6 +956,215 @@ def test_msa_indexer_impl_matches_triton(topk, index_dtype...; symbols: test_msa_indexer_impl_matches_triton, _reference_aiter_sparse_table, test_aiter_indexer_impl_matches_reference
- 关键代码摘录:

```diff
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -956,6 +956,215 @@ def test_msa_indexer_impl_matches_triton(topk, index_dtype, monkeypatch):
+def _reference_aiter_sparse_table(
+    topk: torch.Tensor,
+    page16_block_table: torch.Tensor,
+    row_req_id: list[int],
+    row_pos: list[int],
+    num_kv_heads: int,
```

- 已读文件:
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +209/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/models/kimi_k3/test_prefix_cache.py`, `tests/v1/e2e/test_replayssm_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57909 - [ROCm][PERF] Enable MiniMax-M3 Indexer CP

- 链接: https://github.com/vllm-project/vllm/pull/57909
- 状态/时间: merged / 2026-10-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`, `vllm/models/minimax_m3/amd/indexer_cp.py`, `vllm/models/minimax_m3/amd/indexer_msa.py`, `vllm/models/minimax_m3/amd/model.py` 等 6 个文件；关联提交 `cba669d45d12`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+1719/-785，可读 patch 2745 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][PERF] Enable MiniMax-M3 Indexer CP」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/indexer_msa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/mtp.py`；技术摘要: 覆盖「[ROCm][PERF] Enable MiniMax-M3 Indexer CP」；主要实现面是 `vllm/models/minimax_m3/amd/indexer_msa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/indexer_msa.py` added +931/-0 (931 lines); hunks: -0,0 +1,931; symbols: _score_width, _score_buffer, _cp_score_buffer, MiniMaxM3IndexerMSABackend，涉及 `_score_width, _score_buffer, _cp_score_buffer`；`vllm/models/minimax_m3/amd/model.py` modified +103/-65 (168 lines); hunks: -89,9 +89,11; -642,7 +644,10 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/minimax_m3/amd/mtp.py` modified +106/-3 (109 lines); hunks: -18,13 +18,15; -46,6 +48,15; symbols: _SparseIndexerContext, _build_sparse_indexer_context, MiniMaxM3MultiTokenPredictorLayer, __init__，涉及 `_SparseIndexerContext, _build_sparse_indexer_context, MiniMaxM3MultiTokenPredictorLayer`；`vllm/models/minimax_m3/amd/indexer_cp.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: get_indexer_cp_group, _ipc_alloc, IndexerCpPeers, get_indexer_cp_peers，涉及 `get_indexer_cp_group, _ipc_alloc, IndexerCpPeers`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/indexer_msa.py` added +931/-0 (931 lines); hunks: -0,0 +1,931; symbols: _score_width, _score_buffer, _cp_score_buffer, MiniMaxM3IndexerMSABackend
  - `vllm/models/minimax_m3/amd/model.py` modified +103/-65 (168 lines); hunks: -89,9 +89,11; -642,7 +644,10 @@ def __init__(; symbols: __init__
  - `vllm/models/minimax_m3/amd/mtp.py` modified +106/-3 (109 lines); hunks: -18,13 +18,15; -46,6 +48,15; symbols: _SparseIndexerContext, _build_sparse_indexer_context, MiniMaxM3MultiTokenPredictorLayer, __init__
  - `vllm/models/minimax_m3/amd/indexer_cp.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: get_indexer_cp_group, _ipc_alloc, IndexerCpPeers, get_indexer_cp_peers
  - `tests/kernels/attention/test_indexer_msa.py` added +424/-0 (424 lines); hunks: -0,0 +1,424; symbols: aiter_msa_indexer_gate, probe, test_msa_indexer_gate_rejects_unshardable_configs, test_msa_slot_cap_matches_what_aiter_compiled
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/indexer_msa.py
@@ -0,0 +1,931 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MSA (gfx950/CDNA4) indexer impl for MiniMax M3.
+Scores index blocks and selects the top-k with AITER's fp8 MFMA kernels. Prefill
+and decode differ only in the scorer -- ragged rows against uniform ones -- and
+share one ``pa_sparse_block_topk``, which also emits the attend's page table in
diff -- vllm/models/minimax_m3/amd/model.py
@@ -89,9 +89,11 @@
-from vllm.models.minimax_m3.amd.indexer_aiter import (
-    MiniMaxM3AiterIndexer,
-    select_aiter_indexer_impl_cls,
+from vllm.models.minimax_m3.amd.indexer_msa import (
+    MiniMaxM3IndexerMSAImpl,
+    MiniMaxM3MSAIndexer,
diff -- vllm/models/minimax_m3/amd/mtp.py
@@ -18,13 +18,15 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/indexer_msa.py` added +931/-0; `vllm/models/minimax_m3/amd/model.py` modified +103/-65; `vllm/models/minimax_m3/amd/mtp.py` modified +106/-3; `vllm/models/minimax_m3/amd/indexer_cp.py` added +87/-0
  - tests: `tests/kernels/attention/test_indexer_msa.py` added +424/-0; `tests/kernels/attention/test_minimax_m3.py` modified +15/-47; `tests/kernels/attention/test_minimax_m3_indexer_cp.py` modified +15/-3
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_indexer_msa.py`, `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63082 - [Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config

- 链接: https://github.com/vllm-project/vllm/pull/63082
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/minimax_m3/test_index_cache_overrides.py`, `vllm/models/minimax_m3/amd/model.py`；关联提交 `f120f1dbf2f0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+104/-4，可读 patch 155 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/models/minimax_m3/test_index_cache_overrides.py`, `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config」；主要实现面是 `tests/models/minimax_m3/test_index_cache_overrides.py`, `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/minimax_m3/test_index_cache_overrides.py` added +67/-0 (67 lines); hunks: -0,0 +1,67; symbols: checkpoint, test_top_level_overrides_are_rejected, test_text_config_overrides_take_effect，涉及 `checkpoint, test_top_level_overrides_are_rejected, test_text_config_overrides_take_effect`；`vllm/models/minimax_m3/amd/model.py` modified +5/-4 (9 lines); hunks: -170,10 +170,11 @@ def _should_skip_index_topk(config: PreTrainedConfig, laye...; symbols: _should_skip_index_topk，涉及 `_should_skip_index_topk`。
- 代码 diff 细节:
  - `tests/models/minimax_m3/test_index_cache_overrides.py` added +67/-0 (67 lines); hunks: -0,0 +1,67; symbols: checkpoint, test_top_level_overrides_are_rejected, test_text_config_overrides_take_effect
  - `vllm/models/minimax_m3/amd/model.py` modified +5/-4 (9 lines); hunks: -170,10 +170,11 @@ def _should_skip_index_topk(config: PreTrainedConfig, laye...; symbols: _should_skip_index_topk
- 关键代码摘录:

```diff
diff -- tests/models/minimax_m3/test_index_cache_overrides.py
@@ -0,0 +1,67 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiniMax-M3 rejects IndexCache keys passed as top-level --hf-overrides."""
+import pytest
+import regex as re
+from vllm.config import ModelConfig
diff -- vllm/models/minimax_m3/amd/model.py
@@ -170,10 +170,11 @@ def _should_skip_index_topk(config: PreTrainedConfig, layer_id: int) -> bool:
-    same forward pass. This cuts the indexer score + top-k cost ~``freq``x with
-    negligible accuracy impact (adjacent sparse layers pick nearly the same
-    blocks; ATOM validated GSM8K with freq=4). Gated by ``use_index_cache``;
-    enable via ``--hf-overrides '{"use_index_cache": true, "index_topk_freq": 4}'``.
+    same forward pass. This cuts the indexer score + top-k cost ~``freq``x but
+    approximates the per-layer selection, so validate accuracy on long-context
```

- 已读文件:
  - tests: `tests/models/minimax_m3/test_index_cache_overrides.py` added +67/-0
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +5/-4
- 验证与风险: diff 自带测试面 `tests/models/minimax_m3/test_index_cache_overrides.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62994 - [ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps

- 链接: https://github.com/vllm-project/vllm/pull/62994
- 状态/时间: merged / 2026-10-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/specialized_decode/runtime/routing.py` 等 7 个文件；关联提交 `05406ba47018`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+177/-32，可读 patch 311 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps」；主要实现面是 `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/minimax_m3/amd_specialized_decode/test_model.py` modified +132/-11 (143 lines); hunks: -23,6 +23,7; -188,20 +189,16 @@ def generator(name, sharded=True):; symbols: generator, _requests, _decode, test_late_rank_fault_returns_no_tokens_from_full_graphs，涉及 `generator, _requests, _decode`；`tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` modified +27/-5 (32 lines); hunks: -38,19 +38,22; -74,7 +77,15 @@ def _metadata(rows, *, decode_tokens=None, prefills=0, query_...; symbols: _metadata, test_step_routing, test_config_refusals_report_every_reason, test_only_eagle3_speculation_is_accepted，涉及 `_metadata, test_step_routing, test_config_refusals_report_every_reason`；`vllm/models/minimax_m3/amd/model.py` modified +7/-6 (13 lines); hunks: -1502,26 +1502,27 @@ def forward(; symbols: forward，涉及 `forward`；`vllm/models/minimax_m3/amd/specialized_decode/runtime/routing.py` modified +2/-4 (6 lines); hunks: -39,12 +39,10 @@ def decide_step(; symbols: decide_step，涉及 `decide_step`。
- 代码 diff 细节:
  - `tests/models/minimax_m3/amd_specialized_decode/test_model.py` modified +132/-11 (143 lines); hunks: -23,6 +23,7; -188,20 +189,16 @@ def generator(name, sharded=True):; symbols: generator, _requests, _decode, test_late_rank_fault_returns_no_tokens_from_full_graphs
  - `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` modified +27/-5 (32 lines); hunks: -38,19 +38,22; -74,7 +77,15 @@ def _metadata(rows, *, decode_tokens=None, prefills=0, query_...; symbols: _metadata, test_step_routing, test_config_refusals_report_every_reason, test_only_eagle3_speculation_is_accepted
  - `vllm/models/minimax_m3/amd/model.py` modified +7/-6 (13 lines); hunks: -1502,26 +1502,27 @@ def forward(; symbols: forward
  - `vllm/models/minimax_m3/amd/specialized_decode/runtime/routing.py` modified +2/-4 (6 lines); hunks: -39,12 +39,10 @@ def decide_step(; symbols: decide_step
  - `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +3/-2 (5 lines); hunks: -65,8 +65,9 @@ def _sparse_attn_prefill_kwargs() -> dict:; symbols: _sparse_attn_prefill_kwargs
- 关键代码摘录:

```diff
diff -- tests/models/minimax_m3/amd_specialized_decode/test_model.py
@@ -23,6 +23,7 @@
+from vllm.utils.torch_utils import set_random_seed
@@ -188,20 +189,16 @@ def generator(name, sharded=True):
-    g = torch.Generator().manual_seed(SEED)
+    set_random_seed(SEED)
+    requests = []
-            {
diff -- tests/models/minimax_m3/amd_specialized_decode/test_runtime.py
@@ -38,19 +38,22 @@
+    """A decode-first step: ``decode_tokens`` rows of requests ``query_len``
+    rows each (an EAGLE3 verify step: 1 + num_speculative_tokens)."""
+    requests = decode_tokens // query_len
-        seq_lens=torch.ones(rows, dtype=torch.int32),
+        seq_lens=torch.ones(requests, dtype=torch.int32),
-        num_decodes=decode_tokens,
diff -- vllm/models/minimax_m3/amd/model.py
@@ -1502,26 +1502,27 @@ def forward(
```

- 已读文件:
  - tests: `tests/models/minimax_m3/amd_specialized_decode/test_model.py` modified +132/-11; `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` modified +27/-5
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +7/-6; `vllm/models/minimax_m3/amd/specialized_decode/runtime/routing.py` modified +2/-4; `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +3/-2; `vllm/models/minimax_m3/amd/specialized_decode/runtime/spec.py` modified +3/-2; `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57832 - [ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in)

- 链接: https://github.com/vllm-project/vllm/pull/57832
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/distributed/test_minimax_m3_indexer_cp_tp.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`, `vllm/models/minimax_m3/amd/indexer_context_parallel.py`, `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py`, `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py` 等 6 个文件；关联提交 `153b76b304ee`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+1511/-0，可读 patch 1544 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in)」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/indexer_context_parallel.py`, `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py`, `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py`；技术摘要: 覆盖「[ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in)」；主要实现面是 `vllm/models/minimax_m3/amd/indexer_context_parallel.py`, `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py`, `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/indexer_context_parallel.py` added +363/-0 (363 lines); hunks: -0,0 +1,363; symbols: _packed, IndexerCPDecode, __init__, buf，涉及 `_packed, IndexerCPDecode, __init__`；`vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: _pack_score_key, _force, _local_topk_keys, _merge_topk_keys，涉及 `_pack_score_key, _force, _local_topk_keys`；`vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: _decode_score_chunks, _context_score, check_context_score_inputs, indexer_context_scores，涉及 `_decode_score_chunks, _context_score, check_context_score_inputs`；`vllm/models/minimax_m3/common/indexer.py` modified +25/-0 (25 lines); hunks: -505,6 +505,31 @@ def select_indexer_impl_cls(; symbols: select_indexer_impl_cls，涉及 `select_indexer_impl_cls`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/indexer_context_parallel.py` added +363/-0 (363 lines); hunks: -0,0 +1,363; symbols: _packed, IndexerCPDecode, __init__, buf
  - `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: _pack_score_key, _force, _local_topk_keys, _merge_topk_keys
  - `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: _decode_score_chunks, _context_score, check_context_score_inputs, indexer_context_scores
  - `vllm/models/minimax_m3/common/indexer.py` modified +25/-0 (25 lines); hunks: -505,6 +505,31 @@ def select_indexer_impl_cls(; symbols: select_indexer_impl_cls
  - `tests/kernels/attention/test_minimax_m3_indexer_cp.py` added +327/-0 (327 lines); hunks: -0,0 +1,327; symbols: _reference_shard, test_indexer_context_scores_matches_reference, test_indexer_context_scores_independent_of_shape_bound, score
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/indexer_context_parallel.py
@@ -0,0 +1,363 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiniMax-M3 context-parallel Triton indexer for ROCm.
+M3's index heads shard like its KV heads, so at TP=4 each rank owns one of
+the four index heads. Partitioning the *blocks* across ranks therefore needs
+every rank to score every head:
diff -- vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py
@@ -0,0 +1,331 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Candidate exchange for MiniMax-M3 Triton indexer CP (graph-safe).
+Each rank keeps, per index head, its own top-k over a 1/P block shard,
+all-gathers the packed keys (payload independent of context length), then
+merges per head. The merge is exact only when every shard
diff -- vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py
@@ -0,0 +1,248 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/indexer_context_parallel.py` added +363/-0; `vllm/models/minimax_m3/amd/ops/indexer_cp_exchange.py` added +331/-0; `vllm/models/minimax_m3/amd/ops/indexer_context_parallel.py` added +248/-0; `vllm/models/minimax_m3/common/indexer.py` modified +25/-0
  - tests: `tests/kernels/attention/test_minimax_m3_indexer_cp.py` added +327/-0; `tests/distributed/test_minimax_m3_indexer_cp_tp.py` added +200/-0
- 验证与风险: diff 自带测试面 `tests/distributed/test_minimax_m3_indexer_cp_tp.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62712 - [ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X

- 链接: https://github.com/vllm-project/vllm/pull/62712
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/minimax_m3/amd_specialized_decode/_xcd_stress.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_ops.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py` 等 24 个文件；关联提交 `385d1dab3ba4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 27 个文件，+4903/-7，可读 patch 5024 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py`, `tests/models/minimax_m3/amd_specialized_decode/test_ops.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X」；主要实现面是 `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py`, `tests/models/minimax_m3/amd_specialized_decode/test_ops.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py` added +1080/-0 (1080 lines); hunks: -0,0 +1,1080; symbols: Experts, FfnBuild, slots, peer_half_bytes，涉及 `Experts, FfnBuild, slots`；`tests/models/minimax_m3/amd_specialized_decode/test_ops.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: _metrics, weights, codes, scales，涉及 `_metrics, weights, codes`；`tests/models/minimax_m3/amd_specialized_decode/test_model.py` added +454/-0 (454 lines); hunks: -0,0 +1,454; symbols: _supported, model_dir, _randomize, generator，涉及 `_supported, model_dir, _randomize`；`tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` added +432/-0 (432 lines); hunks: -0,0 +1,432; symbols: _metadata, test_step_routing, _vllm_config, test_config_refusals_report_every_reason，涉及 `_metadata, test_step_routing, _vllm_config`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py` added +1080/-0 (1080 lines); hunks: -0,0 +1,1080; symbols: Experts, FfnBuild, slots, peer_half_bytes
  - `tests/models/minimax_m3/amd_specialized_decode/test_ops.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: _metrics, weights, codes, scales
  - `tests/models/minimax_m3/amd_specialized_decode/test_model.py` added +454/-0 (454 lines); hunks: -0,0 +1,454; symbols: _supported, model_dir, _randomize, generator
  - `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` added +432/-0 (432 lines); hunks: -0,0 +1,432; symbols: _metadata, test_step_routing, _vllm_config, test_config_refusals_report_every_reason
  - `vllm/models/minimax_m3/amd/specialized_decode/mono/sync.py` added +333/-0 (333 lines); hunks: -0,0 +1,333; symbols: _ptr, store64, load64, store32
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py
@@ -0,0 +1,1080 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiniMax-M3 FFN launch: one persistent kernel from the unreduced ``o_proj``
+partial to the reduced MoE output (``MiniMaxM3DecoderLayer.forward`` after its
+attention).
+``BLOCKS`` x ``THREADS``, S rows, one launch per sparse layer and rank:
diff -- tests/models/minimax_m3/amd_specialized_decode/test_ops.py
@@ -0,0 +1,722 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Op-level tests of the fused FFN launch (TP=1 builds unless noted) against
+vLLM's and AITER's native ops, with MXFP4 weights from vLLM's real post-load
+path: stage parity, routing ties, padding, residency, graph replay, fail-stop
+sites, epoch reset, the gfx950 hand-off ISA, and the hand-off stresses (one-GPU
diff -- tests/models/minimax_m3/amd_specialized_decode/test_model.py
@@ -0,0 +1,454 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/specialized_decode/mono/ffn.py` added +1080/-0; `vllm/models/minimax_m3/amd/specialized_decode/mono/sync.py` added +333/-0; `vllm/models/minimax_m3/amd/specialized_decode/runtime/weights.py` added +273/-0; `vllm/models/minimax_m3/amd/specialized_decode/runtime/executor.py` added +218/-0
  - tests: `tests/models/minimax_m3/amd_specialized_decode/test_ops.py` added +722/-0; `tests/models/minimax_m3/amd_specialized_decode/test_model.py` added +454/-0; `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py` added +432/-0; `tests/models/minimax_m3/amd_specialized_decode/_xcd_stress.py` added +251/-0
- 验证与风险: diff 自带测试面 `tests/models/minimax_m3/amd_specialized_decode/_xcd_stress.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_ops.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62035 - [Perf][Parser] Stream MiniMax M2 tool argument values incrementally (16 KB call: 5.9 s to 26 ms)

- 链接: https://github.com/vllm-project/vllm/pull/62035
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_minimax_m2.py`, `vllm/parser/minimax_m2.py`；关联提交 `b088eba94431`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+185/-14，可读 patch 263 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Parser] Stream MiniMax M2 tool argument values incrementally (16 KB call: 5.9 s to 26 ms)」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `tests/parser/engine/test_minimax_m2.py`, `vllm/parser/minimax_m2.py`；技术摘要: 覆盖「[Perf][Parser] Stream MiniMax M2 tool argument values incrementally (16 KB call: 5.9 s to 26 ms)」；主要实现面是 `tests/parser/engine/test_minimax_m2.py`, `vllm/parser/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/parser/engine/test_minimax_m2.py` modified +121/-0 (121 lines); hunks: -1,6 +1,7; -15,11 +16,14; symbols: test_streaming_invalid_tool_name_is_rejected, TestArgValueExtender, write_tool, test_long_call_streams_non_streaming_arguments，涉及 `test_streaming_invalid_tool_name_is_rejected, TestArgValueExtender, write_tool`；`vllm/parser/minimax_m2.py` modified +64/-14 (78 lines); hunks: -22,6 +22,7; -57,37 +58,85; symbols: _minimax_m2_arg_converter, _param_name, _minimax_m2_parse_args, _value_end_window，涉及 `_minimax_m2_arg_converter, _param_name, _minimax_m2_parse_args`。
- 代码 diff 细节:
  - `tests/parser/engine/test_minimax_m2.py` modified +121/-0 (121 lines); hunks: -1,6 +1,7; -15,11 +16,14; symbols: test_streaming_invalid_tool_name_is_rejected, TestArgValueExtender, write_tool, test_long_call_streams_non_streaming_arguments
  - `vllm/parser/minimax_m2.py` modified +64/-14 (78 lines); hunks: -22,6 +22,7; -57,37 +58,85; symbols: _minimax_m2_arg_converter, _param_name, _minimax_m2_parse_args, _value_end_window
- 关键代码摘录:

```diff
diff -- tests/parser/engine/test_minimax_m2.py
@@ -1,6 +1,7 @@
+import dataclasses
@@ -15,11 +16,14 @@
+from vllm.parser.engine.parser_engine import ParserEngine
+    _minimax_m2_arg_value_extender,
+    minimax_m2_config,
@@ -238,6 +242,123 @@ def test_streaming_invalid_tool_name_is_rejected(
diff -- vllm/parser/minimax_m2.py
@@ -22,6 +22,7 @@
+    ArgValueExtender,
@@ -57,37 +58,85 @@
-def _minimax_m2_arg_converter(raw_args: str, partial: bool) -> str:
+# What ends an open value in ``_PARAM_RE``: a closing tag or the next opener.
+_PARAM_VALUE_END_RE = re.compile(r"<\s*/\s*parameter\s*>|<\s*parameter\s+name\s*=")
+def _param_name(match: re.Match) -> str:
```

- 已读文件:
  - tests: `tests/parser/engine/test_minimax_m2.py` modified +121/-0
  - runtime: `vllm/parser/minimax_m2.py` modified +64/-14
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_minimax_m2.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60990 - [Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer

- 链接: https://github.com/vllm-project/vllm/pull/60990
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `e96c822660df`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+39/-3，可读 patch 70 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer」；主要实现面是 `vllm/models/minimax_m3/common/sparse_attention.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/sparse_attention.py` modified +3/-1 (4 lines); hunks: -125,7 +125,9 @@ def minimax_m3_use_aiter_sparse_pa(; symbols: minimax_m3_use_aiter_sparse_pa，涉及 `minimax_m3_use_aiter_sparse_pa`；`tests/kernels/attention/test_minimax_m3.py` modified +29/-0 (29 lines); hunks: -1833,6 +1833,35 @@ def unsupported_reason() -> str | None:; symbols: unsupported_reason, test_aiter_indexer_rejects_unbuilt_index_heads, test_aiter_consolidated_qknorm_enabled，涉及 `unsupported_reason, test_aiter_indexer_rejects_unbuilt_index_heads, test_aiter_consolidated_qknorm_enabled`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +3/-1 (4 lines); hunks: -125,7 +125,9 @@ def minimax_m3_use_aiter_sparse_pa(; symbols: minimax_m3_use_aiter_sparse_pa
  - `tests/kernels/attention/test_minimax_m3.py` modified +29/-0 (29 lines); hunks: -1833,6 +1833,35 @@ def unsupported_reason() -> str | None:; symbols: unsupported_reason, test_aiter_indexer_rejects_unbuilt_index_heads, test_aiter_consolidated_qknorm_enabled
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -125,7 +125,9 @@ def minimax_m3_use_aiter_sparse_pa(
-            "unless the indexer emits the attend's page table."
+            "unless the AITER indexer emits the attend's page table. It is not "
+            "in use here; the 'MiniMax M3 indexer: AITER unavailable' log line "
+            "says why."
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -1833,6 +1833,35 @@ def unsupported_reason() -> str | None:
+def test_aiter_indexer_rejects_unbuilt_index_heads(monkeypatch):
+    """AITER builds the MSA score kernels for 1 or 2 index heads only.
+    MiniMax-M3 has 4, so at attention TP=1 the indexer has to fall back at load
+    time rather than fail at the first forward.
+    """
+    import vllm.models.minimax_m3.amd.indexer_aiter as indexer_aiter_mod
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/sparse_attention.py` modified +3/-1
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +29/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55838 - [Perf][Attention][MiniMax-M3] Select CUTLASS MSA by EAGLE3 decode shape

- 链接: https://github.com/vllm-project/vllm/pull/55838
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`；关联提交 `3f550129e8a3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+62/-17，可读 patch 170 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Attention][MiniMax-M3] Select CUTLASS MSA by EAGLE3 decode shape」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；技术摘要: 覆盖「[Perf][Attention][MiniMax-M3] Select CUTLASS MSA by EAGLE3 decode shape」；主要实现面是 `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +26/-4 (30 lines); hunks: -23,9 +23,10; -235,6 +236,22 @@ def _supported_head_geometry(num_q_heads: int, num_kv_heads...; symbols: is_nvfp4_kv_cache, _supported_head_geometry, _min_cutlass_batch_size, supports_cutlass_sparse_decode，涉及 `is_nvfp4_kv_cache, _supported_head_geometry, _min_cutlass_batch_size`；`vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-0 (8 lines); hunks: -8,6 +8,7; -49,6 +50,11; symbols: _get_msa_cutlass_min_batch_size, _dequantize_query, __init__, build，涉及 `_get_msa_cutlass_min_batch_size, _dequantize_query, __init__`；`tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +28/-13 (41 lines); hunks: -65,30 +65,40; -291,6 +301,7 @@ def test_msa_metadata_builder_prepares_cutlass_for_regular_d...; symbols: test_msa_cutlass_decode_static_dispatch, test_msa_metadata_builder_prepares_cutlass_for_regular_decode, _make_topk, test_msa_cutlass_decode_matches_triton_with_interleaved_cache，涉及 `test_msa_cutlass_decode_static_dispatch, test_msa_metadata_builder_prepares_cutlass_for_regular_decode, _make_topk`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +26/-4 (30 lines); hunks: -23,9 +23,10; -235,6 +236,22 @@ def _supported_head_geometry(num_q_heads: int, num_kv_heads...; symbols: is_nvfp4_kv_cache, _supported_head_geometry, _min_cutlass_batch_size, supports_cutlass_sparse_decode
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-0 (8 lines); hunks: -8,6 +8,7; -49,6 +50,11; symbols: _get_msa_cutlass_min_batch_size, _dequantize_query, __init__, build
  - `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +28/-13 (41 lines); hunks: -65,30 +65,40; -291,6 +301,7 @@ def test_msa_metadata_builder_prepares_cutlass_for_regular_d...; symbols: test_msa_cutlass_decode_static_dispatch, test_msa_metadata_builder_prepares_cutlass_for_regular_decode, _make_topk, test_msa_cutlass_decode_matches_triton_with_interleaved_cache
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py
@@ -23,9 +23,10 @@
-# Kernel benchmarks put the CUTLASS crossover at 16 requests for TP1 and TP4.
-# NVFP4 has no Triton fallback, so it takes CUTLASS at every batch size.
-_MIN_CUTLASS_BATCH_SIZE = 16
+_DEFAULT_MIN_CUTLASS_BATCH_SIZE = 16
+_B300_EAGLE3_QUERY_HEAD_ROWS = 1024
+_B300_EAGLE3_MAX_QUERY_LEN = 8
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -8,6 +8,7 @@
+import os
@@ -49,6 +50,11 @@
+def _get_msa_cutlass_min_batch_size() -> int | None:
+    value = os.getenv("VLLM_MINIMAX_M3_MSA_CUTLASS_MIN_BATCH")
+    return int(value) if value is not None else None
@@ -133,6 +139,7 @@ def __init__(
diff -- tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py
@@ -65,30 +65,40 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +26/-4; `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-0
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +28/-13
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60917 - [Fix] MiniMax: fix CUDA IPC handle exchange on cuda-bindings >= 13.4

- 链接: https://github.com/vllm-project/vllm/pull/60917
- 状态/时间: merged / 2026-10-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`；关联提交 `cc9b0f097d49`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+20/-3，可读 patch 57 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] MiniMax: fix CUDA IPC handle exchange on cuda-bindings >= 13.4」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`；技术摘要: 覆盖「[Fix] MiniMax: fix CUDA IPC handle exchange on cuda-bindings >= 13.4」；主要实现面是 `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` modified +20/-3 (23 lines); hunks: -4,6 +4,7; -16,6 +17,7; symbols: _check, _ipc_handle_to_bytes, _ipc_handle_from_bytes, _cuda_malloc，涉及 `_check, _ipc_handle_to_bytes, _ipc_handle_from_bytes`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` modified +20/-3 (23 lines); hunks: -4,6 +4,7; -16,6 +17,7; symbols: _check, _ipc_handle_to_bytes, _ipc_handle_from_bytes, _cuda_malloc
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py
@@ -4,6 +4,7 @@
+import ctypes
@@ -16,6 +17,7 @@
+_IPC_HANDLE_SIZE = 64  # sizeof(cudaIpcMemHandle_t)
@@ -30,6 +32,20 @@ def _check(error):
+# cuda-bindings >= 13.4 no longer exposes cudaIpcMemHandle_t.reserved, so
+# copy the raw handle bytes through getPtr() instead. This is safe because the
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` modified +20/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #60684 - [Perf][MiniMax-M3] MSA prefill attends with the E4M3 query; bump fmha_sm100 to 968061a

- 链接: https://github.com/vllm-project/vllm/pull/60684
- 状态/时间: merged / 2026-10-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`；关联提交 `2eb491e18b1c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+176/-32，可读 patch 323 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] MSA prefill attends with the E4M3 query; bump fmha_sm100 to 968061a」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] MSA prefill attends with the E4M3 query; bump fmha_sm100 to 968061a」；主要实现面是 `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-8 (16 lines); hunks: -266,7 +266,7 @@ def forward(; -339,11 +339,11 @@ def forward(; symbols: forward，涉及 `forward`；`vllm/models/minimax_m3/nvidia/model.py` modified +1/-1 (2 lines); hunks: -614,7 +614,7 @@ def forward(; symbols: forward，涉及 `forward`；`tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +157/-22 (179 lines); hunks: -782,6 +782,46 @@ def _make_nvfp4_kv_cache(; -898,27 +938,14 @@ def run() -> None:; symbols: _make_nvfp4_kv_cache, _e4m3_staged_kv_reference, _assert_close_fp8_prefill, _record_query_dtypes，涉及 `_make_nvfp4_kv_cache, _e4m3_staged_kv_reference, _assert_close_fp8_prefill`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-8 (16 lines); hunks: -266,7 +266,7 @@ def forward(; -339,11 +339,11 @@ def forward(; symbols: forward
  - `vllm/models/minimax_m3/nvidia/model.py` modified +1/-1 (2 lines); hunks: -614,7 +614,7 @@ def forward(; symbols: forward
  - `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +157/-22 (179 lines); hunks: -782,6 +782,46 @@ def _make_nvfp4_kv_cache(; -898,27 +938,14 @@ def run() -> None:; symbols: _make_nvfp4_kv_cache, _e4m3_staged_kv_reference, _assert_close_fp8_prefill, _record_query_dtypes
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -266,7 +266,7 @@ def forward(
-        # decode reads it directly, and the bf16-query kernels read it
+        # decode and prefill read it directly, and Triton decode reads it
@@ -339,11 +339,11 @@ def forward(
-            qp = (
-                q[nd:]
-                if q_fp8 is None
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -614,7 +614,7 @@ def forward(
-        # into ``q`` for the tokens that run on bf16-query kernels.
+        # into ``q`` for the tokens that run on Triton decode.
diff -- tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py
@@ -782,6 +782,46 @@ def _make_nvfp4_kv_cache(
+def _e4m3_staged_kv_reference(
+    kv_reference: torch.Tensor, k_scale: torch.Tensor, v_scale: torch.Tensor
+) -> torch.Tensor:
+    """The dequantized NVFP4 cache as an E4M3-query kernel reads it: each
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +8/-8; `vllm/models/minimax_m3/nvidia/model.py` modified +1/-1
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +157/-22
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54597 - [Bugfix][MiniMax-M3] Guard sparse decode sentinel indices

- 链接: https://github.com/vllm-project/vllm/pull/54597
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；关联提交 `1664c4f44416`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+128/-10，可读 patch 196 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Guard sparse decode sentinel indices」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Guard sparse decode sentinel indices」；主要实现面是 `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +16/-8 (24 lines); hunks: -304,7 +304,7 @@ def _gqa_sparse_decode_kernel(; -334,10 +334,15 @@ def _gqa_sparse_decode_kernel(; symbols: _gqa_sparse_decode_kernel，涉及 `_gqa_sparse_decode_kernel`；`tests/kernels/attention/test_minimax_m3.py` modified +97/-0 (97 lines); hunks: -2612,6 +2612,103 @@ def test_decode_sparse_attention_correctness(; symbols: test_decode_sparse_attention_correctness, test_decode_sparse_attention_ignores_invalid_topk, run_decode, test_decode_wrong_layout_breaks_parity，涉及 `test_decode_sparse_attention_correctness, test_decode_sparse_attention_ignores_invalid_topk, run_decode`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +16/-8 (24 lines); hunks: -304,7 +304,7 @@ def _gqa_sparse_decode_kernel(; -334,10 +334,15 @@ def _gqa_sparse_decode_kernel(; symbols: _gqa_sparse_decode_kernel
  - `tests/kernels/attention/test_minimax_m3.py` modified +97/-0 (97 lines); hunks: -2612,6 +2612,103 @@ def test_decode_sparse_attention_correctness(; symbols: test_decode_sparse_attention_correctness, test_decode_sparse_attention_ignores_invalid_topk, run_decode, test_decode_wrong_layout_breaks_parity
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -304,7 +304,7 @@ def _gqa_sparse_decode_kernel(
-    # Valid block count from seq_len (no sentinel): min(topk, cdiv(kv_len, blk)).
+    # Upper bound on top-k entries from causal length; entries may be sentinels.
@@ -334,10 +334,15 @@ def _gqa_sparse_decode_kernel(
-        c = blk * BLOCK_SIZE_K
-        page = tl.load(bt_row + blk).to(tl.int64)
+        # topk_idx uses -1 for unused entries. Select a safe logical block
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -2612,6 +2612,103 @@ def test_decode_sparse_attention_correctness(
+@pytest.mark.parametrize("kv_layout", ["NHD", "HND"], indirect=True)
+@pytest.mark.parametrize("capture_graph", [False, True])
+@pytest.mark.parametrize("num_reqs", [2, 17], ids=["split-k", "single-chunk"])
+@pytest.mark.parametrize(
+    "invalid_block", [-1, 1_000_000], ids=["sentinel", "out-of-range"]
+)
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +16/-8
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +97/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59285 - [ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors

- 链接: https://github.com/vllm-project/vllm/pull/59285
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；关联提交 `d64a18832bcb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+80/-70，可读 patch 240 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`；技术摘要: 覆盖「[ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors」；主要实现面是 `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +56/-49 (105 lines); hunks: -110,23 +110,30 @@ def _gqa_sparse_fwd_kernel(; -203,15 +210,14 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel, _merge_topk_attn_out_kernel，涉及 `_gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel, _merge_topk_attn_out_kernel`；`vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +16/-14 (30 lines); hunks: -139,15 +139,15 @@ def _gqa_sparse_fwd_kernel(; -228,15 +228,17 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel，涉及 `_gqa_sparse_fwd_kernel`；`vllm/models/minimax_m3/amd/ops/index_topk.py` modified +8/-7 (15 lines); hunks: -229,15 +229,16 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel，涉及 `_index_block_score_kernel`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +56/-49 (105 lines); hunks: -110,23 +110,30 @@ def _gqa_sparse_fwd_kernel(; -203,15 +210,14 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel, _merge_topk_attn_out_kernel
  - `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +16/-14 (30 lines); hunks: -139,15 +139,15 @@ def _gqa_sparse_fwd_kernel(; -228,15 +228,17 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel
  - `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +8/-7 (15 lines); hunks: -229,15 +229,16 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -110,23 +110,30 @@ def _gqa_sparse_fwd_kernel(
+    off_h = tl.arange(0, BLOCK_SIZE_H)
+    h_mask = off_h < gqa_group_size
-        q_ptrs = tl.make_block_ptr(
-            base=q_ptr + q_start * stride_qn + pid_h * stride_qh,
-            shape=(q_len, gqa_group_size, head_dim),
-            strides=(stride_qn, stride_qh, stride_qd),
diff -- vllm/models/minimax_m3/amd/ops/sparse_attn.py
@@ -139,15 +139,15 @@ def _gqa_sparse_fwd_kernel(
-        q_ptrs = tl.make_block_ptr(
+        q_desc = tl.make_tensor_descriptor(
-            shape=(q_len, gqa_group_size, head_dim),
-            strides=(stride_qn, stride_qh, stride_qd),
-            offsets=(pid_q_j * BLOCK_SIZE_Q, 0, 0),
-            block_shape=(BLOCK_SIZE_Q, BLOCK_SIZE_H, BLOCK_SIZE_D),
diff -- vllm/models/minimax_m3/amd/ops/index_topk.py
@@ -229,15 +229,16 @@ def _index_block_score_kernel(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +56/-49; `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +16/-14; `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +8/-7
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #60194 - [Bugfix][MiniMax-M3] Fence decode indexer shared-memory stage reuse

- 链接: https://github.com/vllm-project/vllm/pull/60194
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py`；关联提交 `fe51194e2d79`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+35/-8，可读 patch 106 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Fence decode indexer shared-memory stage reuse」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Fence decode indexer shared-memory stage reuse」；主要实现面是 `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py` modified +3/-0 (3 lines); hunks: -287,6 +287,8 @@ def kernel(; -342,6 +344,7 @@ def kernel(; symbols: kernel，涉及 `kernel`；`tests/kernels/attention/test_minimax_m3.py` modified +32/-8 (40 lines); hunks: -2,6 +2,8; -1444,19 +1446,21 @@ def test_decode_index_topk_fp8(num_idx_heads: int):; symbols: test_decode_index_topk_fp8, test_decode_index_score_cutedsl_correctness，涉及 `test_decode_index_topk_fp8, test_decode_index_score_cutedsl_correctness`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py` modified +3/-0 (3 lines); hunks: -287,6 +287,8 @@ def kernel(; -342,6 +344,7 @@ def kernel(; symbols: kernel
  - `tests/kernels/attention/test_minimax_m3.py` modified +32/-8 (40 lines); hunks: -2,6 +2,8; -1444,19 +1446,21 @@ def test_decode_index_topk_fp8(num_idx_heads: int):; symbols: test_decode_index_topk_fp8, test_decode_index_score_cutedsl_correctness
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/ops/index_decode_score.py
@@ -287,6 +287,8 @@ def kernel(
+                # Order ldmatrix reads before the producer refills this stage with TMA.
+                cute.arch.fence_proxy("async.shared", space="cta")
@@ -342,6 +344,7 @@ def kernel(
+                    cute.arch.fence_proxy("async.shared", space="cta")
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -2,6 +2,8 @@
+from functools import partial
@@ -1444,19 +1446,21 @@ def test_decode_index_topk_fp8(num_idx_heads: int):
-    ("dtype", "decode_query_len", "max_decode_query_len"),
+    ("dtype", "decode_query_len", "max_decode_query_len", "concurrent_writes"),
-        (torch.bfloat16, 1, 1),
-        (torch.bfloat16, 3, 8),
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py` modified +3/-0
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +32/-8
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59743 - [Frontend] Port the MiniMax M3 tool parser to the parser engine

- 链接: https://github.com/vllm-project/vllm/pull/59743
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_minimax_m3.py`, `tests/tool_parsers/test_minimax_m3_tool_parser.py`, `vllm/parser/minimax_m3.py`, `vllm/tool_parsers/minimax_m3_tool_parser.py`；关联提交 `5145e35e50ca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+658/-41，可读 patch 788 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Port the MiniMax M3 tool parser to the parser engine」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `tests/tool_parsers/test_minimax_m3_tool_parser.py`, `vllm/tool_parsers/minimax_m3_tool_parser.py`, `vllm/parser/minimax_m3.py`；技术摘要: 覆盖「[Frontend] Port the MiniMax M3 tool parser to the parser engine」；主要实现面是 `tests/tool_parsers/test_minimax_m3_tool_parser.py`, `vllm/tool_parsers/minimax_m3_tool_parser.py`, `vllm/parser/minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +34/-23 (57 lines); hunks: -8,16 +8,13; -108,6 +105,23 @@ def build_order_call() -> str:; symbols: build_order_call, build_order_invocation, test_minimax_m3_parser_registered, test_required_tool_choice_keeps_native_syntax，涉及 `build_order_call, build_order_invocation, test_minimax_m3_parser_registered`；`vllm/tool_parsers/minimax_m3_tool_parser.py` modified +5/-14 (19 lines); hunks: -1,19 +1,10; symbols: MinimaxM3ToolParser, only，涉及 `MinimaxM3ToolParser, only`；`vllm/parser/minimax_m3.py` added +293/-0 (293 lines); hunks: -0,0 +1,293; symbols: _parse_element, _parse_invoke_params, _container_schema, _convert_element，涉及 `_parse_element, _parse_invoke_params, _container_schema`；`tests/parser/engine/test_minimax_m3.py` added +253/-0 (253 lines); hunks: -0,0 +1,253; symbols: parser, element, tool_block, parse_arguments，涉及 `parser, element, tool_block`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +34/-23 (57 lines); hunks: -8,16 +8,13; -108,6 +105,23 @@ def build_order_call() -> str:; symbols: build_order_call, build_order_invocation, test_minimax_m3_parser_registered, test_required_tool_choice_keeps_native_syntax
  - `vllm/tool_parsers/minimax_m3_tool_parser.py` modified +5/-14 (19 lines); hunks: -1,19 +1,10; symbols: MinimaxM3ToolParser, only
  - `vllm/parser/minimax_m3.py` added +293/-0 (293 lines); hunks: -0,0 +1,293; symbols: _parse_element, _parse_invoke_params, _container_schema, _convert_element
  - `tests/parser/engine/test_minimax_m3.py` added +253/-0 (253 lines); hunks: -0,0 +1,253; symbols: parser, element, tool_block, parse_arguments
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_minimax_m3_tool_parser.py
@@ -8,16 +8,13 @@
+    ChatCompletionRequest,
-# MinimaxM3ToolParser extends RustToolParser; skip when the PyO3 extension
-# is absent (mirrors the guard in test_rust_tool_parser.py).
-pytest.importorskip("vllm._rust_tool_parser")
@@ -108,6 +105,23 @@ def build_order_call() -> str:
+ORDER_ARGUMENTS = {
diff -- vllm/tool_parsers/minimax_m3_tool_parser.py
@@ -1,19 +1,10 @@
-from vllm.tool_parsers.rust_tool_parser import RustToolParser
+from vllm.parser.engine.registered_adapters import MinimaxM3ParserToolAdapter
-class MinimaxM3ToolParser(RustToolParser):
-    """Adapter from the Rust MiniMax M3 parser to vLLM ToolParser.
-    The real M3 grammar lives in the Rust tool-parser crate. This class only
-    configures the generic Rust bridge with the MiniMax M3 parser name.
diff -- vllm/parser/minimax_m3.py
@@ -0,0 +1,293 @@
```

- 已读文件:
  - tests: `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +34/-23; `tests/parser/engine/test_minimax_m3.py` added +253/-0
  - runtime: `vllm/tool_parsers/minimax_m3_tool_parser.py` modified +5/-14; `vllm/parser/minimax_m3.py` added +293/-0
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_minimax_m3.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py`, `tests/tool_parsers/test_minimax_m3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59481 - [Minimax-M3] Keep the native FP8 MMA in the Triton indexer scorers

- 链接: https://github.com/vllm-project/vllm/pull/59481
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`；关联提交 `e42d35d4f3b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+45/-9，可读 patch 86 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3] Keep the native FP8 MMA in the Triton indexer scorers」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`；技术摘要: 覆盖「[Minimax-M3] Keep the native FP8 MMA in the Triton indexer scorers」；主要实现面是 `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +11/-9 (20 lines); hunks: -124,9 +124,11 @@ def _index_block_score_kernel(; -162,7 +164,7 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, _decode_index_score_kernel，涉及 `_index_block_score_kernel, _decode_index_score_kernel`；`tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` modified +34/-0 (34 lines); hunks: -107,3 +107,37 @@ def select(cache: torch.Tensor) -> set[int]:; symbols: select, test_bf16_query_against_fp8_cache_decode_topk_matches_bf16，涉及 `select, test_bf16_query_against_fp8_cache_decode_topk_matches_bf16`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +11/-9 (20 lines); hunks: -124,9 +124,11 @@ def _index_block_score_kernel(; -162,7 +164,7 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, _decode_index_score_kernel
  - `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` modified +34/-0 (34 lines); hunks: -107,3 +107,37 @@ def select(cache: torch.Tensor) -> set[int]:; symbols: select, test_bf16_query_against_fp8_cache_decode_topk_matches_bf16
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -124,9 +124,11 @@ def _index_block_score_kernel(
-    # FP8 has no mixed-dtype dot with bf16/fp32. Leave bf16 and fp32 loads
-    # in their stored dtype so fp32 pipeline tests keep full precision.
-    if q.dtype.is_fp8():
+    # A matched fp8 pair (e.g. e4m3 x e4m3) lowers to a native FP8 MMA, so
+    # upcast only when the operands differ: there is no mixed-dtype fp8 MMA,
+    # including across fp8 flavours (fp8e4nv vs fp8e4b8). bf16 and fp32 loads
diff -- tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py
@@ -107,3 +107,37 @@ def select(cache: torch.Tensor) -> set[int]:
+@pytest.mark.skipif(not FP8_CUDA_SUPPORTED, reason="CUDA FP8 support required")
+@torch.inference_mode()
+def test_bf16_query_against_fp8_cache_decode_topk_matches_bf16() -> None:
+    """A mixed pair must upcast rather than emit a mixed-dtype fp8 dot.
+    Production allocates index_q with the index-K cache dtype, so the scorers
+    normally see a matched pair and keep the native FP8 MMA. This pins the
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +11/-9
  - tests: `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` modified +34/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59613 - [Bugfix] Fix minimax-m3 multimodal processor compatability with Transformers v5.18

- 链接: https://github.com/vllm-project/vllm/pull/59613
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/processors/minimax_m3.py`；关联提交 `b558f160a2c0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix minimax-m3 multimodal processor compatability with Transformers v5.18」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/transformers_utils/processors/minimax_m3.py`；技术摘要: 覆盖「[Bugfix] Fix minimax-m3 multimodal processor compatability with Transformers v5.18」；主要实现面是 `vllm/transformers_utils/processors/minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/processors/minimax_m3.py` modified +0/-1 (1 lines); hunks: -375,7 +375,6 @@ def __init__(self, **kwargs: Unpack[MiniMaxM3VLVideoProcesso...; symbols: __init__, _preprocess，涉及 `__init__, _preprocess`。
- 代码 diff 细节:
  - `vllm/transformers_utils/processors/minimax_m3.py` modified +0/-1 (1 lines); hunks: -375,7 +375,6 @@ def __init__(self, **kwargs: Unpack[MiniMaxM3VLVideoProcesso...; symbols: __init__, _preprocess
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/processors/minimax_m3.py
@@ -375,7 +375,6 @@ def __init__(self, **kwargs: Unpack[MiniMaxM3VLVideoProcessorKwargs]):
-        do_convert_rgb: bool,
```

- 已读文件:
  - runtime: `vllm/transformers_utils/processors/minimax_m3.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `vllm/transformers_utils/processors/minimax_m3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #59300 - [Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path

- 链接: https://github.com/vllm-project/vllm/pull/59300
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` 等 6 个文件；关联提交 `7566d83bd35c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+1293/-69，可读 patch 1860 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；技术摘要: 覆盖「[Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path」；主要实现面是 `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/common/sparse_attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +108/-11 (119 lines); hunks: -4,15 +4,18; -29,20 +32,33; symbols: _dequantize_query, MiniMaxM3SparseMSABackend, get_builder_cls, MiniMaxM3SparseMSANvfp4Backend，涉及 `_dequantize_query, MiniMaxM3SparseMSABackend, get_builder_cls`；`vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +52/-7 (59 lines); hunks: -12,6 +12,7; -23,9 +24,36; symbols: is_nvfp4_kv_cache, nvfp4_kv_cache_views, nvfp4_kv_cache_slots, MSACutlassDecodeMetadata，涉及 `is_nvfp4_kv_cache, nvfp4_kv_cache_views, nvfp4_kv_cache_slots`；`vllm/models/minimax_m3/common/sparse_attention.py` modified +19/-3 (22 lines); hunks: -56,6 +56,7; -531,10 +532,10 @@ def select_main_backend_and_impl_cls(; symbols: select_main_backend_and_impl_cls，涉及 `select_main_backend_and_impl_cls`；`vllm/models/minimax_m3/nvidia/model.py` modified +7/-1 (8 lines); hunks: -500,6 +500,8 @@ def __init__(; -611,6 +613,8 @@ def forward(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +108/-11 (119 lines); hunks: -4,15 +4,18; -29,20 +32,33; symbols: _dequantize_query, MiniMaxM3SparseMSABackend, get_builder_cls, MiniMaxM3SparseMSANvfp4Backend
  - `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +52/-7 (59 lines); hunks: -12,6 +12,7; -23,9 +24,36; symbols: is_nvfp4_kv_cache, nvfp4_kv_cache_views, nvfp4_kv_cache_slots, MSACutlassDecodeMetadata
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +19/-3 (22 lines); hunks: -56,6 +56,7; -531,10 +532,10 @@ def select_main_backend_and_impl_cls(; symbols: select_main_backend_and_impl_cls
  - `vllm/models/minimax_m3/nvidia/model.py` modified +7/-1 (8 lines); hunks: -500,6 +500,8 @@ def __init__(; -611,6 +613,8 @@ def forward(; symbols: __init__, forward
  - `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +441/-1 (442 lines); hunks: -1,13 +1,15; -18,6 +20,7; symbols: test_msa_cutlass_decode_static_dispatch_requires_sm100, test_msa_cutlass_decode_static_dispatch_nvfp4_has_no_fallback, test_nvfp4_selects_msa_nvfp4_backend_and_requires_sm100, test_msa_cutlass_decode_matches_triton_with_interleaved_cache
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -4,15 +4,18 @@
-path for regular decode and speculative verification.
+path for regular decode and speculative verification. NVFP4 KV caches read the
+vLLM packed pages directly in both prefill and CUTLASS decode.
-from dataclasses import dataclass
+from dataclasses import dataclass, replace
+from typing import ClassVar
diff -- vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py
@@ -12,6 +12,7 @@
+from vllm.v1.kv_cache_interface import get_kv_quant_mode
@@ -23,9 +24,36 @@
+# NVFP4 has no Triton fallback, so it takes CUTLASS at every batch size.
+def is_nvfp4_kv_cache(kv_cache_dtype: str) -> bool:
+    return get_kv_quant_mode(kv_cache_dtype).is_nvfp4
+def nvfp4_kv_cache_views(
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -56,6 +56,7 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +108/-11; `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` modified +52/-7; `vllm/models/minimax_m3/common/sparse_attention.py` modified +19/-3; `vllm/models/minimax_m3/nvidia/model.py` modified +7/-1
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +441/-1; `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +226/-4
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57197 - [Bugfix][PP][Spec Decode] MiniMax-M3 EAGLE3 aux-state relay at PP > 1 and per-stage FlashInfer autotune

- 链接: https://github.com/vllm-project/vllm/pull/57197
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `42f0c17ea755`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+382/-15，可读 patch 502 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][PP][Spec Decode] MiniMax-M3 EAGLE3 aux-state relay at PP > 1 and per-stage FlashInfer autotune」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix][PP][Spec Decode] MiniMax-M3 EAGLE3 aux-state relay at PP > 1 and per-stage FlashInfer autotune」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +19/-4 (23 lines); hunks: -793,6 +793,7 @@ def ffn_all_reduce_deferred(self) -> bool:; -883,17 +884,30 @@ def forward(; symbols: ffn_all_reduce_deferred, MiniMaxM3Model, __init__, forward，涉及 `ffn_all_reduce_deferred, MiniMaxM3Model, __init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +19/-4 (23 lines); hunks: -793,6 +793,7 @@ def ffn_all_reduce_deferred(self) -> bool:; -883,17 +884,30 @@ def forward(; symbols: ffn_all_reduce_deferred, MiniMaxM3Model, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -793,6 +793,7 @@ def ffn_all_reduce_deferred(self) -> bool:
+    supports_aux_hidden_states_over_pp = True
@@ -883,17 +884,30 @@ def forward(
-        # EAGLE3 is not yet compatible with pipeline parallel
-        aux_hidden_states = self._maybe_add_hidden_state([], 0, hidden_states, residual)
-        for idx, layer in enumerate(self.layers[self.start_layer : self.end_layer]):
+        remote_aux = self.collect_remote_aux_hidden_states(intermediate_tensors)
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +19/-4
- 验证与风险: diff 自带测试面 `tests/model_executor/test_flashinfer_autotune_warmup.py`, `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56151 - [Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K

- 链接: https://github.com/vllm-project/vllm/pull/56151
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`；关联提交 `84f738f1878f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+38/-7，可读 patch 100 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K」；主要实现面是 `vllm/models/minimax_m3/common/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +28/-5 (33 lines); hunks: -101,6 +101,7 @@ def _index_block_score_kernel(; -136,8 +137,19 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, minimax_m3_index_score, minimax_m3_index_decode_score，涉及 `_index_block_score_kernel, minimax_m3_index_score, minimax_m3_index_decode_score`；`tests/kernels/attention/test_minimax_m3.py` modified +10/-2 (12 lines); hunks: -614,14 +614,22 @@ def _reference_decode_index_score(; symbols: _reference_decode_index_score, test_prefill_index_topk_correctness，涉及 `_reference_decode_index_score, test_prefill_index_topk_correctness`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +28/-5 (33 lines); hunks: -101,6 +101,7 @@ def _index_block_score_kernel(; -136,8 +137,19 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, minimax_m3_index_score, minimax_m3_index_decode_score
  - `tests/kernels/attention/test_minimax_m3.py` modified +10/-2 (12 lines); hunks: -614,14 +614,22 @@ def _reference_decode_index_score(; symbols: _reference_decode_index_score, test_prefill_index_topk_correctness
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -101,6 +101,7 @@ def _index_block_score_kernel(
+    USE_SPLIT_K: tl.constexpr,
@@ -136,8 +137,19 @@ def _index_block_score_kernel(
-    for i in tl.range(0, hi, BLOCK_SIZE_K):
-        blk = i // BLOCK_SIZE_K
+    num_blocks = tl.cdiv(hi, BLOCK_SIZE_K)
+    if USE_SPLIT_K:
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -614,14 +614,22 @@ def _reference_decode_index_score(
-def test_prefill_index_topk_correctness():
+# 3600: 29 blocks over 12 splits of 3, so the last busy split has 2 blocks.
+@pytest.mark.parametrize("prefix_len", [1024, 3600])
+@pytest.mark.parametrize("force_split_k", [False, True])
+def test_prefill_index_topk_correctness(monkeypatch, prefix_len, force_split_k):
+    if force_split_k:
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +28/-5
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +10/-2
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58648 - [Bugfix][MiniMax M3] Share target embeddings with MTP under PP

- 链接: https://github.com/vllm-project/vllm/pull/58648
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/mtp.py`；关联提交 `a8e069f81b48`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+229/-6，可读 patch 335 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax M3] Share target embeddings with MTP under PP」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/nvidia/mtp.py`, `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[Bugfix][MiniMax M3] Share target embeddings with MTP under PP」；主要实现面是 `vllm/models/minimax_m3/amd/mtp.py`, `vllm/models/minimax_m3/nvidia/mtp.py`, `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/mtp.py` modified +11/-0 (11 lines); hunks: -24,6 +24,7; -164,6 +165,10 @@ class MiniMaxM3MTP(nn.Module):; symbols: MiniMaxM3MTP, __init__, load_weights，涉及 `MiniMaxM3MTP, __init__, load_weights`；`vllm/models/minimax_m3/nvidia/mtp.py` modified +11/-0 (11 lines); hunks: -8,6 +8,7; -146,6 +147,10 @@ class MiniMaxM3MTP(nn.Module):; symbols: MiniMaxM3MTP, __init__, load_weights，涉及 `MiniMaxM3MTP, __init__, load_weights`；`vllm/models/minimax_m3/amd/model.py` modified +4/-1 (5 lines); hunks: -85,6 +85,7; -1370,7 +1371,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`；`vllm/models/minimax_m3/nvidia/model.py` modified +4/-1 (5 lines); hunks: -68,6 +68,7; -803,7 +804,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/mtp.py` modified +11/-0 (11 lines); hunks: -24,6 +24,7; -164,6 +165,10 @@ class MiniMaxM3MTP(nn.Module):; symbols: MiniMaxM3MTP, __init__, load_weights
  - `vllm/models/minimax_m3/nvidia/mtp.py` modified +11/-0 (11 lines); hunks: -8,6 +8,7; -146,6 +147,10 @@ class MiniMaxM3MTP(nn.Module):; symbols: MiniMaxM3MTP, __init__, load_weights
  - `vllm/models/minimax_m3/amd/model.py` modified +4/-1 (5 lines); hunks: -85,6 +85,7; -1370,7 +1371,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `vllm/models/minimax_m3/nvidia/model.py` modified +4/-1 (5 lines); hunks: -68,6 +68,7; -803,7 +804,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/mtp.py
@@ -24,6 +24,7 @@
+from vllm.distributed import get_pp_group
@@ -164,6 +165,10 @@ class MiniMaxM3MTP(nn.Module):
+        if vllm_config.use_v2_model_runner and get_pp_group().world_size > 1:
+            # Preserve embeddings from loaders that bypass load_weights.
+            self.has_own_embed_tokens = vllm_config.load_config.load_format != "dummy"
@@ -333,4 +338,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
diff -- vllm/models/minimax_m3/nvidia/mtp.py
@@ -8,6 +8,7 @@
+from vllm.distributed import get_pp_group
@@ -146,6 +147,10 @@ class MiniMaxM3MTP(nn.Module):
+        if vllm_config.use_v2_model_runner and get_pp_group().world_size > 1:
+            # Preserve embeddings from loaders that bypass load_weights.
+            self.has_own_embed_tokens = vllm_config.load_config.load_format != "dummy"
@@ -315,4 +320,10 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
diff -- vllm/models/minimax_m3/amd/model.py
@@ -85,6 +85,7 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/mtp.py` modified +11/-0; `vllm/models/minimax_m3/nvidia/mtp.py` modified +11/-0; `vllm/models/minimax_m3/amd/model.py` modified +4/-1; `vllm/models/minimax_m3/nvidia/model.py` modified +4/-1
- 验证与风险: diff 自带测试面 `tests/v1/worker/test_spec_decode_embed_sharing_pp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59081 - [Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures.

- 链接: https://github.com/vllm-project/vllm/pull/59081
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`；关联提交 `e03875f4d283`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+133/-9，可读 patch 191 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures.」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/indexer.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`；技术摘要: 覆盖「[Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures.」；主要实现面是 `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/indexer.py`, `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +14/-4 (18 lines); hunks: -123,6 +123,10 @@ def _index_block_score_kernel(; -146,7 +150,9 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, _decode_index_score_kernel，涉及 `_index_block_score_kernel, _decode_index_score_kernel`；`vllm/models/minimax_m3/common/indexer.py` modified +10/-5 (15 lines); hunks: -502,16 +502,21 @@ def select_indexer_impl_cls(; -530,7 +535,7 @@ def select_indexer_impl_cls(; symbols: select_indexer_impl_cls，涉及 `select_indexer_impl_cls`；`tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _make_inputs, _check_selection, test_fp8_index_query_and_cache_decode_topk_matches_bf16, select，涉及 `_make_inputs, _check_selection, test_fp8_index_query_and_cache_decode_topk_matches_bf16`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +14/-4 (18 lines); hunks: -123,6 +123,10 @@ def _index_block_score_kernel(; -146,7 +150,9 @@ def _index_block_score_kernel(; symbols: _index_block_score_kernel, _decode_index_score_kernel
  - `vllm/models/minimax_m3/common/indexer.py` modified +10/-5 (15 lines); hunks: -502,16 +502,21 @@ def select_indexer_impl_cls(; -530,7 +535,7 @@ def select_indexer_impl_cls(; symbols: select_indexer_impl_cls
  - `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _make_inputs, _check_selection, test_fp8_index_query_and_cache_decode_topk_matches_bf16, select
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -123,6 +123,10 @@ def _index_block_score_kernel(
+    # FP8 has no mixed-dtype dot with bf16/fp32. Leave bf16 and fp32 loads
+    # in their stored dtype so fp32 pipeline tests keep full precision.
+    if q.dtype.is_fp8():
+        q = q.to(tl.bfloat16)
@@ -146,7 +150,9 @@ def _index_block_score_kernel(
-        qk = tl.dot(q, k)
diff -- vllm/models/minimax_m3/common/indexer.py
@@ -502,16 +502,21 @@ def select_indexer_impl_cls(
-    Triton indexer (bf16 only).
+    Triton indexer, with fp8 restricted to CUDA platforms that advertise fp8
+    support.
-    is_sm100 = (
-        current_platform.is_cuda() and current_platform.is_device_capability_family(100)
-    )
diff -- tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py
@@ -0,0 +1,109 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/ops/index_topk.py` modified +14/-4; `vllm/models/minimax_m3/common/indexer.py` modified +10/-5
  - tests: `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py` added +109/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58673 - [Minimax-M3] Add Encoder CUDA graph support

- 链接: https://github.com/vllm-project/vllm/pull/58673
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py`, `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `55de40a2fc1a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+397/-17，可读 patch 496 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3] Add Encoder CUDA graph support」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py`, `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[Minimax-M3] Add Encoder CUDA graph support」；主要实现面是 `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py`, `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/encoder_cudagraph.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens, pad_rope_planes，涉及 `MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens`；`vllm/models/minimax_m3/common/vision_tower.py` modified +82/-15 (97 lines); hunks: -392,43 +392,65 @@ def _apply_max_frames_limit(self, grid_thw: list[list[int]...; -442,6 +464,45 @@ def forward(; symbols: _apply_max_frames_limit, forward, prepare_encoder_metadata，涉及 `_apply_max_frames_limit, forward, prepare_encoder_metadata`；`vllm/models/minimax_m3/amd/model.py` modified +8/-1 (9 lines); hunks: -106,6 +106,9; -1685,7 +1688,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, MiniMaxM3SparseForConditionalGeneration，涉及 `load_weights, MiniMaxM3SparseForConditionalGeneration`；`vllm/models/minimax_m3/nvidia/model.py` modified +8/-1 (9 lines); hunks: -70,6 +70,9; -1076,7 +1079,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, MiniMaxM3SparseForConditionalGeneration，涉及 `load_weights, MiniMaxM3SparseForConditionalGeneration`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/encoder_cudagraph.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: MiniMaxM3EncoderCudaGraphMixin, get_encoder_cudagraph_config, pad_cu_seqlens, pad_rope_planes
  - `vllm/models/minimax_m3/common/vision_tower.py` modified +82/-15 (97 lines); hunks: -392,43 +392,65 @@ def _apply_max_frames_limit(self, grid_thw: list[list[int]...; -442,6 +464,45 @@ def forward(; symbols: _apply_max_frames_limit, forward, prepare_encoder_metadata
  - `vllm/models/minimax_m3/amd/model.py` modified +8/-1 (9 lines); hunks: -106,6 +106,9; -1685,7 +1688,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, MiniMaxM3SparseForConditionalGeneration
  - `vllm/models/minimax_m3/nvidia/model.py` modified +8/-1 (9 lines); hunks: -70,6 +70,9; -1076,7 +1079,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, MiniMaxM3SparseForConditionalGeneration
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/encoder_cudagraph.py
@@ -0,0 +1,281 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Encoder CUDA graph support for the MiniMax M3 vision tower.
+Mixin implementing the SupportsEncoderCudaGraph protocol for any host class
+that holds the vision tower as ``self.vision_tower`` (a
+``MiniMaxVLVisionModel``). The manager routes image items through this mixin;
diff -- vllm/models/minimax_m3/common/vision_tower.py
@@ -392,43 +392,65 @@ def _apply_max_frames_limit(self, grid_thw: list[list[int]]) -> list[list[int]]:
-    # ── Forward ──────────────────────────────────────────────────────────
+    # ── Encoder metadata (shared by eager forward and CUDA graph replay) ──
-    def forward(
+    def prepare_encoder_metadata(
-        pixel_values: torch.Tensor,
-    ) -> torch.Tensor:
diff -- vllm/models/minimax_m3/amd/model.py
@@ -106,6 +106,9 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/encoder_cudagraph.py` added +281/-0; `vllm/models/minimax_m3/common/vision_tower.py` modified +82/-15; `vllm/models/minimax_m3/amd/model.py` modified +8/-1; `vllm/models/minimax_m3/nvidia/model.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation/test_vit_cudagraph.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58526 - [Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope

- 链接: https://github.com/vllm-project/vllm/pull/58526
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/vision_tower.py`；关联提交 `16070ed7e9b0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+280/-179，可读 patch 595 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/vision_tower.py`；技术摘要: 覆盖「[Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope」；主要实现面是 `vllm/models/minimax_m3/common/vision_tower.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/vision_tower.py` modified +42/-171 (213 lines); hunks: -21,20 +21,16; -125,56 +121,13 @@ def __init__(; symbols: MiniMaxVLPatchEmbed, __init__, _apply_rotary_emb, forward，涉及 `MiniMaxVLPatchEmbed, __init__, _apply_rotary_emb`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/vision_tower.py` modified +42/-171 (213 lines); hunks: -21,20 +21,16; -125,56 +121,13 @@ def __init__(; symbols: MiniMaxVLPatchEmbed, __init__, _apply_rotary_emb, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/vision_tower.py
@@ -21,20 +21,16 @@
-from vllm.model_executor.layers.rotary_embedding.common import ApplyRotaryEmb
+from vllm.model_executor.layers.rotary_embedding.mrope import triton_mrope
+from vllm.model_executor.layers.rotary_embedding.mrope_vit_setup import (
+    vit_mrope_setup,
+)
-from vllm.platforms import current_platform
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/vision_tower.py` modified +42/-171
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_mrope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58460 - [Multimodal] Reuse the supplied tokenizer in the MiniMax-M3 VL processor

- 链接: https://github.com/vllm-project/vllm/pull/58460
- 状态/时间: merged / 2026-09-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/processors/minimax_m3.py`；关联提交 `f5a78f2ad73d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-3，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Multimodal] Reuse the supplied tokenizer in the MiniMax-M3 VL processor」；模型线: MiniMax M2 Series；类别: 模型实现调整；主要 diff: `vllm/transformers_utils/processors/minimax_m3.py`；技术摘要: 覆盖「[Multimodal] Reuse the supplied tokenizer in the MiniMax-M3 VL processor」；主要实现面是 `vllm/transformers_utils/processors/minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/processors/minimax_m3.py` modified +8/-3 (11 lines); hunks: -522,9 +522,14 @@ def from_pretrained(cls, pretrained_model_name_or_path, **k...; symbols: from_pretrained，涉及 `from_pretrained`。
- 代码 diff 细节:
  - `vllm/transformers_utils/processors/minimax_m3.py` modified +8/-3 (11 lines); hunks: -522,9 +522,14 @@ def from_pretrained(cls, pretrained_model_name_or_path, **k...; symbols: from_pretrained
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/processors/minimax_m3.py
@@ -522,9 +522,14 @@ def from_pretrained(cls, pretrained_model_name_or_path, **kwargs):
-        tokenizer = AutoTokenizer.from_pretrained(
-            pretrained_model_name_or_path, **kwargs
-        )
+        #
+        # Reuse the tokenizer passed by vLLM instead of loading another one,
+        # and keep it out of the kwargs forwarded to the sub-processor loaders.
```

- 已读文件:
  - runtime: `vllm/transformers_utils/processors/minimax_m3.py` modified +8/-3
- 验证与风险: runtime 路径改动集中在 `vllm/transformers_utils/processors/minimax_m3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58512 - [Minimax-M3][Perf] Use Conv3dLayer for M3 patch embedding

- 链接: https://github.com/vllm-project/vllm/pull/58512
- 状态/时间: merged / 2026-09-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/vision_tower.py`；关联提交 `00b7847c8036`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+45/-1，可读 patch 61 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3][Perf] Use Conv3dLayer for M3 patch embedding」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/vision_tower.py`；技术摘要: 覆盖「[Minimax-M3][Perf] Use Conv3dLayer for M3 patch embedding」；主要实现面是 `vllm/models/minimax_m3/common/vision_tower.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/vision_tower.py` modified +2/-1 (3 lines); hunks: -14,6 +14,7; -55,7 +56,7 @@ def __init__(self, config: PretrainedConfig) -> None:; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/vision_tower.py` modified +2/-1 (3 lines); hunks: -14,6 +14,7; -55,7 +56,7 @@ def __init__(self, config: PretrainedConfig) -> None:; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/vision_tower.py
@@ -14,6 +14,7 @@
+from vllm.model_executor.layers.conv import Conv3dLayer
@@ -55,7 +56,7 @@ def __init__(self, config: PretrainedConfig) -> None:
-        self.patch_embedding = nn.Conv3d(
+        self.patch_embedding = Conv3dLayer(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/vision_tower.py` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_conv.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58089 - [ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite

- 链接: https://github.com/vllm-project/vllm/pull/58089
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`；关联提交 `56b3acb55bb2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-2，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`；技术摘要: 覆盖「[ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite」；主要实现面是 `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +4/-2 (6 lines); hunks: -113,8 +113,10 @@ def _swiglu_oai_quant_kernel(; symbols: _swiglu_oai_quant_kernel，涉及 `_swiglu_oai_quant_kernel`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +4/-2 (6 lines); hunks: -113,8 +113,10 @@ def _swiglu_oai_quant_kernel(; symbols: _swiglu_oai_quant_kernel
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/swiglu_oai.py
@@ -113,8 +113,10 @@ def _swiglu_oai_quant_kernel(
-    descale = tl.exp2(sb - 127.0)
-    aq = (act / descale[:, None]).to(aq_ptr.dtype.element_ty)
+    # Computing the E8M0 byte-0 divisor (2^-127) can flush to zero on CDNA.
+    # Use its finite reciprocal so all-zero blocks do not produce 0/0.
+    rescale = tl.exp2(127.0 - sb)
+    aq = (act * rescale[:, None]).to(aq_ptr.dtype.element_ty)
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +4/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54535 - [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm

- 链接: https://github.com/vllm-project/vllm/pull/54535
- 状态/时间: merged / 2026-09-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/model.py`；关联提交 `b8cf2753825d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+636/-91，可读 patch 826 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +163/-81 (244 lines); hunks: -890,13 +890,39 @@ def get_aiter_sparse_pa_kv_cache(self) -> tuple[torch.Tens...; -906,22 +932,6 @@ def _insert_aiter_sparse_pa_kv(; symbols: get_aiter_sparse_pa_kv_cache, _get_aiter_sparse_pa_slot_mapping, _insert_aiter_sparse_pa_kv, forward，涉及 `get_aiter_sparse_pa_kv_cache, _get_aiter_sparse_pa_slot_mapping, _insert_aiter_sparse_pa_kv`；`tests/kernels/attention/test_minimax_m3.py` modified +361/-10 (371 lines); hunks: -19,7 +19,10; -28,6 +31,7; symbols: test_main_cache_layout_contract, test_aiter_sparse_pa_layout_contract, test_aiter_sparse_pa_rejects_multiple_kv_heads，涉及 `test_main_cache_layout_contract, test_aiter_sparse_pa_layout_contract, test_aiter_sparse_pa_rejects_multiple_kv_heads`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +163/-81 (244 lines); hunks: -890,13 +890,39 @@ def get_aiter_sparse_pa_kv_cache(self) -> tuple[torch.Tens...; -906,22 +932,6 @@ def _insert_aiter_sparse_pa_kv(; symbols: get_aiter_sparse_pa_kv_cache, _get_aiter_sparse_pa_slot_mapping, _insert_aiter_sparse_pa_kv, forward
  - `tests/kernels/attention/test_minimax_m3.py` modified +361/-10 (371 lines); hunks: -19,7 +19,10; -28,6 +31,7; symbols: test_main_cache_layout_contract, test_aiter_sparse_pa_layout_contract, test_aiter_sparse_pa_rejects_multiple_kv_heads
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -890,13 +890,39 @@ def get_aiter_sparse_pa_kv_cache(self) -> tuple[torch.Tensor, torch.Tensor]:
+    def _get_aiter_sparse_pa_slot_mapping(
+        self,
+        slot_mapping: torch.Tensor,
+        key_cache: torch.Tensor,
+        value_cache: torch.Tensor,
+    ) -> torch.Tensor:
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -19,7 +19,10 @@
-from vllm.models.minimax_m3.common.sparse_attention import MiniMaxM3SparseTritonImpl
+from vllm.models.minimax_m3.common.sparse_attention import (
+    MiniMaxM3SparseTritonImpl,
+    minimax_m3_rebase_slots_to_page16,
+)
@@ -28,6 +31,7 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +163/-81
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +361/-10
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56849 - [ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy

- 链接: https://github.com/vllm-project/vllm/pull/56849
- 状态/时间: merged / 2026-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/models/minimax_m3/amd/model.py`；关联提交 `438434b5b5f8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+104/-2，可读 patch 138 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/test_minimax_m3_amd_ops.py`；技术摘要: 覆盖「[ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`, `tests/kernels/test_minimax_m3_amd_ops.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +28/-2 (30 lines); hunks: -579,6 +579,32 @@ def forward(; -902,8 +928,8 @@ def _insert_aiter_sparse_pa_kv(; symbols: forward, _kv_insert_operand, MiniMaxM3SparseAttention, _insert_aiter_sparse_pa_kv，涉及 `forward, _kv_insert_operand, MiniMaxM3SparseAttention`；`tests/kernels/test_minimax_m3_amd_ops.py` modified +76/-0 (76 lines); hunks: -10,6 +10,7; -39,6 +40,7; symbols: resolve, _fused_qkv_kv_slices, _asm_kv_cache, test_kv_insert_operand_matches_contiguous，涉及 `resolve, _fused_qkv_kv_slices, _asm_kv_cache`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +28/-2 (30 lines); hunks: -579,6 +579,32 @@ def forward(; -902,8 +928,8 @@ def _insert_aiter_sparse_pa_kv(; symbols: forward, _kv_insert_operand, MiniMaxM3SparseAttention, _insert_aiter_sparse_pa_kv
  - `tests/kernels/test_minimax_m3_amd_ops.py` modified +76/-0 (76 lines); hunks: -10,6 +10,7; -39,6 +40,7; symbols: resolve, _fused_qkv_kv_slices, _asm_kv_cache, test_kv_insert_operand_matches_contiguous
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -579,6 +579,32 @@ def forward(
+# Widest row pitch aiter's reshape_and_cache can carry in its `int` stride args.
+_MAX_KV_INSERT_ROW_STRIDE = 2**31 - 1
+def _kv_insert_operand(t: torch.Tensor) -> torch.Tensor:
+    """K or V operand for ``aiter.reshape_and_cache``, without a needless copy.
+    The AITER sparse-PA insert takes K and V as column slices of the fused
+    ``[q | k | v | index_q | index_k]`` projection, so they are row-strided
diff -- tests/kernels/test_minimax_m3_amd_ops.py
@@ -10,6 +10,7 @@
+  * Strided K/V sparse-PA cache insert           -> contiguous-copy insert
@@ -39,6 +40,7 @@
+from vllm.models.minimax_m3.amd.model import _kv_insert_operand  # noqa: E402
@@ -588,3 +590,77 @@ def resolve(consumes_mask, *, has_moe_kernel=True):
+# --------------------------------------------------------------------------- #
+# Strided K/V operand for the AITER sparse-PA cache insert
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +28/-2
  - tests: `tests/kernels/test_minimax_m3_amd_ops.py` modified +76/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_minimax_m3_amd_ops.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53674 - [Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale

- 链接: https://github.com/vllm-project/vllm/pull/53674
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`；关联提交 `22bb158c21fc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+28/-4，可读 patch 74 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`, `tests/kernels/test_minimax_m3_amd_ops.py`；技术摘要: 覆盖「[Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale」；主要实现面是 `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`, `tests/kernels/test_minimax_m3_amd_ops.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +6/-2 (8 lines); hunks: -83,6 +83,8 @@ def _swiglu_oai_quant_kernel(; -109,8 +111,8 @@ def _swiglu_oai_quant_kernel(; symbols: _swiglu_oai_quant_kernel, swiglu_oai_quantize_mxfp8，涉及 `_swiglu_oai_quant_kernel, swiglu_oai_quantize_mxfp8`；`tests/kernels/test_minimax_m3_amd_ops.py` modified +22/-2 (24 lines); hunks: -42,6 +42,7; -167,6 +168,25 @@ def test_swiglu_oai_split(m, inter, limit, dtype):; symbols: test_swiglu_oai_split, test_swiglu_oai_quantize_mxfp8_uses_e4m3_range_for_scale, test_mxfp8_quant_triton_matches_torch，涉及 `test_swiglu_oai_split, test_swiglu_oai_quantize_mxfp8_uses_e4m3_range_for_scale, test_mxfp8_quant_triton_matches_torch`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +6/-2 (8 lines); hunks: -83,6 +83,8 @@ def _swiglu_oai_quant_kernel(; -109,8 +111,8 @@ def _swiglu_oai_quant_kernel(; symbols: _swiglu_oai_quant_kernel, swiglu_oai_quantize_mxfp8
  - `tests/kernels/test_minimax_m3_amd_ops.py` modified +22/-2 (24 lines); hunks: -42,6 +42,7; -167,6 +168,25 @@ def test_swiglu_oai_split(m, inter, limit, dtype):; symbols: test_swiglu_oai_split, test_swiglu_oai_quantize_mxfp8_uses_e4m3_range_for_scale, test_mxfp8_quant_triton_matches_torch
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/swiglu_oai.py
@@ -83,6 +83,8 @@ def _swiglu_oai_quant_kernel(
+    FP8_MAX: tl.constexpr,
+    TINY: tl.constexpr,
@@ -109,8 +111,8 @@ def _swiglu_oai_quant_kernel(
-    amax = tl.maximum(tl.max(tl.abs(act), axis=1), 1e-30)  # [BLOCK_M]
-    sb = tl.minimum(tl.maximum(tl.floor(tl.log2(amax)) + 127.0, 0.0), 254.0)
+    amax = tl.maximum(tl.max(tl.abs(act), axis=1), TINY)  # [BLOCK_M]
diff -- tests/kernels/test_minimax_m3_amd_ops.py
@@ -42,6 +42,7 @@
+    swiglu_oai_quantize_mxfp8,
@@ -167,6 +168,25 @@ def test_swiglu_oai_split(m, inter, limit, dtype):
+@torch.inference_mode()
+def test_swiglu_oai_quantize_mxfp8_uses_e4m3_range_for_scale():
+    # Keep a small value in two MX blocks next to their maxima. The scale must
+    # use E4M3's finite range (448), otherwise that value underflows to zero.
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py` modified +6/-2
  - tests: `tests/kernels/test_minimax_m3_amd_ops.py` modified +22/-2
- 验证与风险: diff 自带测试面 `tests/kernels/test_minimax_m3_amd_ops.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55235 - [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts

- 链接: https://github.com/vllm-project/vllm/pull/55235
- 状态/时间: merged / 2026-09-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`；关联提交 `dfa1984e58dc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+90/-48，可读 patch 268 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts」；主要实现面是 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +27/-7 (34 lines); hunks: -37,6 +37,7; -103,14 +104,23 @@ def _decode_topk_launch_policy(; symbols: _decode_topk_launch_policy, minimax_m3_index_decode，涉及 `_decode_topk_launch_policy, minimax_m3_index_decode`；`tests/kernels/attention/test_minimax_m3.py` modified +63/-41 (104 lines); hunks: -1025,17 +1025,20 @@ def test_decode_index_topk_correctness(; -1044,9 +1047,9 @@ def test_amd_decode_topk_launch_policy(; symbols: test_decode_index_topk_correctness, test_amd_decode_topk_launch_policy, test_amd_decode_fused_topk_total_order_and_replay，涉及 `test_decode_index_topk_correctness, test_amd_decode_topk_launch_policy, test_amd_decode_fused_topk_total_order_and_replay`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +27/-7 (34 lines); hunks: -37,6 +37,7; -103,14 +104,23 @@ def _decode_topk_launch_policy(; symbols: _decode_topk_launch_policy, minimax_m3_index_decode
  - `tests/kernels/attention/test_minimax_m3.py` modified +63/-41 (104 lines); hunks: -1025,17 +1025,20 @@ def test_decode_index_topk_correctness(; -1044,9 +1047,9 @@ def test_amd_decode_topk_launch_policy(; symbols: test_decode_index_topk_correctness, test_amd_decode_topk_launch_policy, test_amd_decode_fused_topk_total_order_and_replay
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/index_topk.py
@@ -37,6 +37,7 @@
+DECODE_TOPK_SHORT_BLOCKS_PER_CHUNK = 128
@@ -103,14 +104,23 @@ def _decode_topk_launch_policy(
-) -> tuple[int, bool, bool]:
-    """Choose the graph grid and bounded-context selector specialization."""
+) -> tuple[int, int, int, int, bool, bool]:
+    """Choose the selector grid and compile-time launch configuration."""
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -1025,17 +1025,20 @@ def test_decode_index_topk_correctness(
-        (0, 24, 1, 16, True, (2, False, False)),
-        (1, 1, 1, 16, True, (16, True, True)),
-        (512, 4, 1, 16, True, (16, True, True)),
-        (513, 24, 4, 16, True, (16, True, True)),
-        (2760, 5, 2, 16, True, (16, True, True)),
-        (8192, 64, 4, 16, True, (16, True, True)),
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +27/-7
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +63/-41
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56170 - [ROCm][Performance] Avoid blocking MiniMax M3 scalar upload

- 链接: https://github.com/vllm-project/vllm/pull/56170
- 状态/时间: merged / 2026-09-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `f09c52a587f2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-1，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Performance] Avoid blocking MiniMax M3 scalar upload」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/common/sparse_attention.py`；技术摘要: 覆盖「[ROCm][Performance] Avoid blocking MiniMax M3 scalar upload」；主要实现面是 `vllm/models/minimax_m3/common/sparse_attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/sparse_attention.py` modified +4/-1 (5 lines); hunks: -314,7 +314,10 @@ def build(; symbols: build，涉及 `build`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +4/-1 (5 lines); hunks: -314,7 +314,10 @@ def build(; symbols: build
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -314,7 +314,10 @@ def build(
-            prefill_cu_seqlens_k[0] = 0
+            if current_platform.is_rocm():
+                prefill_cu_seqlens_k[:1].zero_()
+            else:
+                prefill_cu_seqlens_k[0] = 0
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/sparse_attention.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/common/sparse_attention.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #52664 - [Performance][ROCm] Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path

- 链接: https://github.com/vllm-project/vllm/pull/52664
- 状态/时间: merged / 2026-09-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `83252ea899c6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+1077/-58，可读 patch 1393 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Performance][ROCm] Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`；技术摘要: 覆盖「[Performance][ROCm] Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +158/-36 (194 lines); hunks: -87,17 +87,24; -111,7 +118,7; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +152/-5 (157 lines); hunks: -2,16 +2,118; -28,8 +130,11 @@ def forward(; symbols: MiniMaxM3SparseAiterPABackend, get_builder_cls, MiniMaxM3SparseAiterPAPrefillMetadata, MiniMaxM3SparseAiterPADecodeMetadata，涉及 `MiniMaxM3SparseAiterPABackend, get_builder_cls, MiniMaxM3SparseAiterPAPrefillMetadata`；`vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +45/-8 (53 lines); hunks: -312,7 +312,9 @@ def _insert_index_cache_kernel(; -368,6 +370,32 @@ def minimax_m3_sparse_block_page_stride(; symbols: _insert_index_cache_kernel, minimax_m3_sparse_block_page_stride, minimax_m3_rebase_block_table_to_page16, _gluon_scale_arg，涉及 `_insert_index_cache_kernel, minimax_m3_sparse_block_page_stride, minimax_m3_rebase_block_table_to_page16`；`vllm/models/minimax_m3/common/sparse_attention.py` modified +24/-9 (33 lines); hunks: -109,13 +109,22 @@ def minimax_m3_query_token_positions(; -252,9 +261,9 @@ def __init__(; symbols: minimax_m3_query_token_positions, minimax_m3_use_aiter_sparse_pa, __init__, select_main_backend_and_impl_cls，涉及 `minimax_m3_query_token_positions, minimax_m3_use_aiter_sparse_pa, __init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +158/-36 (194 lines); hunks: -87,17 +87,24; -111,7 +118,7; symbols: __init__, forward
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +152/-5 (157 lines); hunks: -2,16 +2,118; -28,8 +130,11 @@ def forward(; symbols: MiniMaxM3SparseAiterPABackend, get_builder_cls, MiniMaxM3SparseAiterPAPrefillMetadata, MiniMaxM3SparseAiterPADecodeMetadata
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +45/-8 (53 lines); hunks: -312,7 +312,9 @@ def _insert_index_cache_kernel(; -368,6 +370,32 @@ def minimax_m3_sparse_block_page_stride(; symbols: _insert_index_cache_kernel, minimax_m3_sparse_block_page_stride, minimax_m3_rebase_block_table_to_page16, _gluon_scale_arg
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +24/-9 (33 lines); hunks: -109,13 +109,22 @@ def minimax_m3_query_token_positions(; -252,9 +261,9 @@ def __init__(; symbols: minimax_m3_query_token_positions, minimax_m3_use_aiter_sparse_pa, __init__, select_main_backend_and_impl_cls
  - `tests/kernels/attention/test_minimax_m3.py` modified +52/-0 (52 lines); hunks: -1694,6 +1694,58 @@ def test_aiter_sparse_pa_rejects_multiple_kv_heads(monkey...; symbols: test_aiter_sparse_pa_rejects_multiple_kv_heads, test_aiter_indexer_requires_the_aiter_attend, test_indexer_cache_squeezes_to_contiguous_3d
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -87,17 +87,24 @@
+from vllm.models.minimax_m3.amd.indexer_aiter import (
+    MiniMaxM3AiterIndexer,
+    select_aiter_indexer_impl_cls,
+)
+    ASM_PAGE_SIZE,
+    MiniMaxM3SparseAiterPADecodeMetadata,
diff -- vllm/models/minimax_m3/amd/sparse_attention_msa.py
@@ -2,16 +2,118 @@
+from dataclasses import dataclass
+from vllm.config import VllmConfig
+    MiniMaxM3SparseBackend,
+    MiniMaxM3SparseDecodeMetadata,
+    MiniMaxM3SparseMetadataBuilder,
+    MiniMaxM3SparsePrefillMetadata,
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -312,7 +312,9 @@ def _insert_index_cache_kernel(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +158/-36; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +152/-5; `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +45/-8; `vllm/models/minimax_m3/common/sparse_attention.py` modified +24/-9
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +52/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54682 - [ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k

- 链接: https://github.com/vllm-project/vllm/pull/54682
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py` 等 6 个文件；关联提交 `cee0f92c0211`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+2010/-327，可读 patch 2644 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/indexer.py`；技术摘要: 覆盖「[ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k」；主要实现面是 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +986/-306 (1292 lines); hunks: -7,21 +7,119; -397,255 +495,670 @@ def _decode_index_score_kernel(; symbols: _decode_score_program_budget, _decode_score_split_launch_policy, _decode_topk_launch_policy, _decode_index_score_kernel，涉及 `_decode_score_program_budget, _decode_score_split_launch_policy, _decode_topk_launch_policy`；`vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +60/-19 (79 lines); hunks: -32,14 +32,13 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:; -56,8 +55,7 @@ def _write_sparse_block_table_row(; symbols: _is_fp8_kv_cache_tensor, _write_sparse_block_table_row, _write_sparse_block_table_row_from_values，涉及 `_is_fp8_kv_cache_tensor, _write_sparse_block_table_row, _write_sparse_block_table_row_from_values`；`vllm/models/minimax_m3/common/indexer.py` modified +71/-1 (72 lines); hunks: -369,6 +369,18 @@ def __init__(; -392,6 +404,11 @@ class MiniMaxM3IndexerTritonImpl(MiniMaxM3IndexerImpl):; symbols: __init__, MiniMaxM3IndexerTritonImpl, forward，涉及 `__init__, MiniMaxM3IndexerTritonImpl, forward`；`vllm/models/minimax_m3/amd/model.py` modified +46/-1 (47 lines); hunks: -92,6 +92,13; -701,6 +708,7 @@ def __init__(; symbols: __init__, _ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache, _run_attention，涉及 `__init__, _ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +986/-306 (1292 lines); hunks: -7,21 +7,119; -397,255 +495,670 @@ def _decode_index_score_kernel(; symbols: _decode_score_program_budget, _decode_score_split_launch_policy, _decode_topk_launch_policy, _decode_index_score_kernel
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +60/-19 (79 lines); hunks: -32,14 +32,13 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:; -56,8 +55,7 @@ def _write_sparse_block_table_row(; symbols: _is_fp8_kv_cache_tensor, _write_sparse_block_table_row, _write_sparse_block_table_row_from_values
  - `vllm/models/minimax_m3/common/indexer.py` modified +71/-1 (72 lines); hunks: -369,6 +369,18 @@ def __init__(; -392,6 +404,11 @@ class MiniMaxM3IndexerTritonImpl(MiniMaxM3IndexerImpl):; symbols: __init__, MiniMaxM3IndexerTritonImpl, forward
  - `vllm/models/minimax_m3/amd/model.py` modified +46/-1 (47 lines); hunks: -92,6 +92,13; -701,6 +708,7 @@ def __init__(; symbols: __init__, _ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache, _run_attention
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +7/-0 (7 lines); hunks: -25,6 +25,7 @@ def forward(; -70,6 +71,12 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/index_topk.py
@@ -7,21 +7,119 @@
-Index-K cache layout (vLLM): ``(num_blocks, 128, idx_head_dim)`` (single head).
+Index-K cache layout (vLLM): ``(num_blocks, 128, idx_head_dim)`` (one shared
+key vector per token).
-disabled (score-only indexer), single shared index head. The selected block ids
-feed the block-sparse attention kernels in ``sparse_attn``.
+disabled (score-only indexer), and shared index keys. Each local index-query
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -32,14 +32,13 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:
-def _write_sparse_block_table_row(
-    topk_row,  # [topk] int32, selected logical block ids for this query
+def _write_sparse_block_table_row_from_values(
+    blk,  # [BLOCK_SIZE_T] int32 selected logical block ids for this query
-    stride_topk_k,
@@ -56,8 +55,7 @@ def _write_sparse_block_table_row(
diff -- vllm/models/minimax_m3/common/indexer.py
@@ -369,6 +369,18 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/index_topk.py` modified +986/-306; `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +60/-19; `vllm/models/minimax_m3/common/indexer.py` modified +71/-1; `vllm/models/minimax_m3/amd/model.py` modified +46/-1; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +7/-0
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +840/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55057 - [ROCm][CI] Add MiniMax reduce RMS kernel coverage

- 链接: https://github.com/vllm-project/vllm/pull/55057
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/core/test_minimax_reduce_rms.py`；关联提交 `096d8e8ce61f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+173/-5，可读 patch 222 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Add MiniMax reduce RMS kernel coverage」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `tests/kernels/core/test_minimax_reduce_rms.py`；技术摘要: 覆盖「[ROCm][CI] Add MiniMax reduce RMS kernel coverage」；主要实现面是 `tests/kernels/core/test_minimax_reduce_rms.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/core/test_minimax_reduce_rms.py` modified +114/-1 (115 lines); hunks: -1,6 +1,8; -9,6 +11,7; symbols: _worker_forward_qk, _worker_forward_qk_rocm_aiter, test_minimax_reduce_rms_qk_rocm_aiter，涉及 `_worker_forward_qk, _worker_forward_qk_rocm_aiter, test_minimax_reduce_rms_qk_rocm_aiter`。
- 代码 diff 细节:
  - `tests/kernels/core/test_minimax_reduce_rms.py` modified +114/-1 (115 lines); hunks: -1,6 +1,8; -9,6 +11,7; symbols: _worker_forward_qk, _worker_forward_qk_rocm_aiter, test_minimax_reduce_rms_qk_rocm_aiter
- 关键代码摘录:

```diff
diff -- tests/kernels/core/test_minimax_reduce_rms.py
@@ -1,6 +1,8 @@
-"""Tests for MiniMax QK RMS-norm: NCCL reference vs Lamport fused kernel."""
+"""Tests for MiniMax QK RMS-norm fused all-reduce kernels and fallbacks."""
+from unittest.mock import patch
@@ -9,6 +11,7 @@
+from vllm._aiter_ops import is_aiter_found_and_supported, rocm_aiter_ops
@@ -124,6 +127,116 @@ def _worker_forward_qk(
```

- 已读文件:
  - tests: `tests/kernels/core/test_minimax_reduce_rms.py` modified +114/-1
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_minimax_reduce_rms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52849 - [ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers

- 链接: https://github.com/vllm-project/vllm/pull/52849
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `ae5b8e4a8d77`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+574/-201，可读 patch 1143 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers」；主要实现面是 `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +155/-118 (273 lines); hunks: -32,43 +32,42 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:; -83,42 +82,54 @@ def _build_sparse_block_table_kernel(; symbols: _is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, _write_sparse_block_table_row, minimax_m3_build_sparse_block_table，涉及 `_is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, _write_sparse_block_table_row`；`vllm/models/minimax_m3/common/sparse_attention.py` modified +97/-7 (104 lines); hunks: -66,6 +66,49 @@ def _minimax_m3_aiter_sparse_pa_requested() -> bool:; -117,10 +160,14 @@ def is_sparse(cls) -> bool:; symbols: _minimax_m3_aiter_sparse_pa_requested, minimax_m3_rebase_slots_to_page16, minimax_m3_query_token_positions, minimax_m3_use_aiter_sparse_pa，涉及 `_minimax_m3_aiter_sparse_pa_requested, minimax_m3_rebase_slots_to_page16, minimax_m3_query_token_positions`；`vllm/models/minimax_m3/amd/model.py` modified +39/-12 (51 lines); hunks: -101,6 +101,8; -755,35 +757,45 @@ def _ensure_aiter_sparse_pa_kv_cache(self) -> None:; symbols: _ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache, _insert_aiter_sparse_pa_kv，涉及 `_ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache, _insert_aiter_sparse_pa_kv`；`vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +3/-2 (5 lines); hunks: -75,14 +75,15 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +155/-118 (273 lines); hunks: -32,43 +32,42 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:; -83,42 +82,54 @@ def _build_sparse_block_table_kernel(; symbols: _is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, _write_sparse_block_table_row, minimax_m3_build_sparse_block_table
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +97/-7 (104 lines); hunks: -66,6 +66,49 @@ def _minimax_m3_aiter_sparse_pa_requested() -> bool:; -117,10 +160,14 @@ def is_sparse(cls) -> bool:; symbols: _minimax_m3_aiter_sparse_pa_requested, minimax_m3_rebase_slots_to_page16, minimax_m3_query_token_positions, minimax_m3_use_aiter_sparse_pa
  - `vllm/models/minimax_m3/amd/model.py` modified +39/-12 (51 lines); hunks: -101,6 +101,8; -755,35 +757,45 @@ def _ensure_aiter_sparse_pa_kv_cache(self) -> None:; symbols: _ensure_aiter_sparse_pa_kv_cache, get_aiter_sparse_pa_kv_cache, _insert_aiter_sparse_pa_kv
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +3/-2 (5 lines); hunks: -75,14 +75,15 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -32,43 +32,42 @@ def _is_fp8_kv_cache_tensor(kv_cache: torch.Tensor) -> bool:
-def _build_sparse_block_table_kernel(
-    topk_ptr,  # [1, batch, topk] int32, selected logical 128-block ids
-    block_table_ptr,  # [batch, max_blocks] int32, logical 128-page table
-    seq_lens_ptr,  # [batch] int32
-    sparse_bt_ptr,  # [batch, topk * 8] int32, physical 16-page table
-    sparse_ctx_ptr,  # [batch] int32
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -66,6 +66,49 @@ def _minimax_m3_aiter_sparse_pa_requested() -> bool:
+def minimax_m3_rebase_slots_to_page16(
+    slot_mapping: torch.Tensor,
+    block_size: int,
+    out: torch.Tensor | None = None,
+) -> torch.Tensor:
+    """Rebase a token slot mapping onto AITER's page-16 page numbering.
diff -- vllm/models/minimax_m3/amd/model.py
@@ -101,6 +101,8 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +155/-118; `vllm/models/minimax_m3/common/sparse_attention.py` modified +97/-7; `vllm/models/minimax_m3/amd/model.py` modified +39/-12; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51203 - [Bugfix][MiniMax-M3] Keep FP8 query allocation stable across CUDA graph replay

- 链接: https://github.com/vllm-project/vllm/pull/51203
- 状态/时间: merged / 2026-08-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `7c8b68b9ce30`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+91/-11，可读 patch 142 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Keep FP8 query allocation stable across CUDA graph replay」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Keep FP8 query allocation stable across CUDA graph replay」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +10/-10 (20 lines); hunks: -564,6 +564,15 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; -598,16 +607,7 @@ def forward(; symbols: get_kv_cache_spec, _allocate_query_fp8, forward，涉及 `get_kv_cache_spec, _allocate_query_fp8, forward`；`tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +81/-1 (82 lines); hunks: -9,19 +9,22; -316,6 +319,83 @@ def fake_build_plan(**kwargs):; symbols: fake_build_plan, test_query_fp8_stays_valid_when_cutlass_plan_appears_on_replay, run_attention, _make_topk，涉及 `fake_build_plan, test_query_fp8_stays_valid_when_cutlass_plan_appears_on_replay, run_attention`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +10/-10 (20 lines); hunks: -564,6 +564,15 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; -598,16 +607,7 @@ def forward(; symbols: get_kv_cache_spec, _allocate_query_fp8, forward
  - `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +81/-1 (82 lines); hunks: -9,19 +9,22; -316,6 +319,83 @@ def fake_build_plan(**kwargs):; symbols: fake_build_plan, test_query_fp8_stays_valid_when_cutlass_plan_appears_on_replay, run_attention, _make_topk
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -564,6 +564,15 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
+    def _allocate_query_fp8(self, qkv: torch.Tensor) -> torch.Tensor | None:
+        if not getattr(self.impl, "use_cutlass_decode", False):
+            return None
+        return torch.empty(
+            (qkv.shape[0], self.q_size),
+            dtype=torch.float8_e4m3fn,
diff -- tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py
@@ -9,19 +9,22 @@
-from vllm.config import AttentionConfig
+from vllm.config import AttentionConfig, CUDAGraphMode
+from vllm.forward_context import ForwardContext, override_forward_context
+    MiniMaxM3SparseMetadata,
+from vllm.models.minimax_m3.nvidia.model import MiniMaxM3SparseAttention
@@ -316,6 +319,83 @@ def fake_build_plan(**kwargs):
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +10/-10
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` modified +81/-1
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50032 - [Attention][MiniMax-M3] Add MSA speculative decode verification

- 链接: https://github.com/vllm-project/vllm/pull/50032
- 状态/时间: merged / 2026-08-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/nvidia/model.py` 等 7 个文件；关联提交 `0055b8bfa3a2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1275/-59，可读 patch 1678 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention][MiniMax-M3] Add MSA speculative decode verification」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；技术摘要: 覆盖「[Attention][MiniMax-M3] Add MSA speculative decode verification」；主要实现面是 `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` added +316/-0 (316 lines); hunks: -0,0 +1,316; symbols: MSACutlassDecodeMetadata, _update_runtime_metadata_kernel, MSACutlassDecodePlanCache, _build_plan，涉及 `MSACutlassDecodeMetadata, _update_runtime_metadata_kernel, MSACutlassDecodePlanCache`；`vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +210/-19 (229 lines); hunks: -1,35 +1,207; -52,23 +224,42 @@ def forward(; symbols: MiniMaxM3SparseMSABackend, get_builder_cls, MiniMaxM3SparseCutlassBackend, get_name，涉及 `MiniMaxM3SparseMSABackend, get_builder_cls, MiniMaxM3SparseCutlassBackend`；`vllm/models/minimax_m3/common/sparse_attention.py` modified +30/-7 (37 lines); hunks: -330,6 +330,7 @@ def __init__(; -355,6 +356,8 @@ def forward(; symbols: __init__, forward, should_use_msa_decode, MiniMaxM3SparseTritonImpl，涉及 `__init__, forward, should_use_msa_decode`；`vllm/models/minimax_m3/nvidia/model.py` modified +28/-6 (34 lines); hunks: -79,7 +79,7; -505,22 +505,25 @@ def __init__(; symbols: __init__, forward, _run_attention, MiniMaxM3DecoderLayer，涉及 `__init__, forward, _run_attention`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` added +316/-0 (316 lines); hunks: -0,0 +1,316; symbols: MSACutlassDecodeMetadata, _update_runtime_metadata_kernel, MSACutlassDecodePlanCache, _build_plan
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +210/-19 (229 lines); hunks: -1,35 +1,207; -52,23 +224,42 @@ def forward(; symbols: MiniMaxM3SparseMSABackend, get_builder_cls, MiniMaxM3SparseCutlassBackend, get_name
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +30/-7 (37 lines); hunks: -330,6 +330,7 @@ def __init__(; -355,6 +356,8 @@ def forward(; symbols: __init__, forward, should_use_msa_decode, MiniMaxM3SparseTritonImpl
  - `vllm/models/minimax_m3/nvidia/model.py` modified +28/-6 (34 lines); hunks: -79,7 +79,7; -505,22 +505,25 @@ def __init__(; symbols: __init__, forward, _run_attention, MiniMaxM3DecoderLayer
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +2/-0 (2 lines); hunks: -23,6 +23,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py
@@ -0,0 +1,316 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiniMax CUTLASS sparse decode using per-query-token page indices."""
+from __future__ import annotations
+from dataclasses import dataclass, field
+from typing import Any
diff -- vllm/models/minimax_m3/nvidia/sparse_attention_msa.py
@@ -1,35 +1,207 @@
-"""MSA (SM100/Blackwell) block-sparse attend for MiniMax M3.
+"""MSA (SM100/Blackwell) block-sparse attention for MiniMax M3.
-Prefill attends with ``fmha_sm100`` (``build_k2q_csr`` + ``sparse_atten_func``);
-decode falls back to the Triton split-K kernel (no MSA decode yet). ``fmha_sm100``
-imports are function-local, so this module is import-safe on AMD/non-SM100.
+Prefill attends with ``fmha_sm100`` (``build_k2q_csr`` + ``sparse_atten_func``).
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -330,6 +330,7 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py` added +316/-0; `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +210/-19; `vllm/models/minimax_m3/common/sparse_attention.py` modified +30/-7; `vllm/models/minimax_m3/nvidia/model.py` modified +28/-6; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +2/-0
  - tests: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` added +561/-0; `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` modified +15/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50305 - [Bugfix] Re-land MiniMax M3 default video processor

- 链接: https://github.com/vllm-project/vllm/pull/50305
- 状态/时间: merged / 2026-07-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/mm_preprocess.py`；关联提交 `f727951d3f0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+42/-12，可读 patch 105 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Re-land MiniMax M3 default video processor」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/mm_preprocess.py`；技术摘要: 覆盖「[Bugfix] Re-land MiniMax M3 default video processor」；主要实现面是 `vllm/models/minimax_m3/common/mm_preprocess.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +34/-11 (45 lines); hunks: -3,8 +3,9; -469,10 +470,39 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample，涉及 `get_video_replacement, MiniMaxM3VideoBackend, load_bytes`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/mm_preprocess.py` modified +34/-11 (45 lines); hunks: -3,8 +3,9; -469,10 +470,39 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/mm_preprocess.py
@@ -3,8 +3,9 @@
-from typing import cast
+from typing import Any, Literal, cast
+import numpy.typing as npt
@@ -469,10 +470,39 @@ def get_video_replacement(item_idx: int):
-# TODO(Isotr0py): Tie with MinimaxVideoProcessor
-# after https://github.com/vllm-project/vllm/pull/44126
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +34/-11
- 验证与风险: diff 自带测试面 `tests/multimodal/test_video.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50313 - Revert "[Misc][Minimax-M3]add default video_processor (#50092)"

- 链接: https://github.com/vllm-project/vllm/pull/50313
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/mm_preprocess.py`；关联提交 `2ecd8645d87e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-44，可读 patch 95 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[Misc][Minimax-M3]add default video_processor (#50092)"」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/common/mm_preprocess.py`；技术摘要: 覆盖「Revert "[Misc][Minimax-M3]add default video_processor (#50092)"」；主要实现面是 `vllm/models/minimax_m3/common/mm_preprocess.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +7/-37 (44 lines); hunks: -3,9 +3,8; -470,39 +469,10 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample，涉及 `get_video_replacement, MiniMaxM3VideoBackend, load_bytes`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/mm_preprocess.py` modified +7/-37 (44 lines); hunks: -3,9 +3,8; -470,39 +469,10 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/mm_preprocess.py
@@ -3,9 +3,8 @@
-from typing import Any, Literal, cast
+from typing import cast
-import numpy.typing as npt
@@ -470,39 +469,10 @@ def get_video_replacement(item_idx: int):
-@VIDEO_LOADER_REGISTRY.register(
-    name="minimax_m3_vl",
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +7/-37
- 验证与风险: diff 自带测试面 `tests/multimodal/test_video.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50092 - [Misc][Minimax-M3]add default video_processor

- 链接: https://github.com/vllm-project/vllm/pull/50092
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/mm_preprocess.py`；关联提交 `2ecd8645d87e`, `df2735ea2e14`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+44/-7，可读 patch 95 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc][Minimax-M3]add default video_processor」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/common/mm_preprocess.py`；技术摘要: 覆盖「[Misc][Minimax-M3]add default video_processor」；主要实现面是 `vllm/models/minimax_m3/common/mm_preprocess.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +37/-7 (44 lines); hunks: -3,8 +3,9; -469,10 +470,39 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample，涉及 `get_video_replacement, MiniMaxM3VideoBackend, load_bytes`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/mm_preprocess.py` modified +37/-7 (44 lines); hunks: -3,8 +3,9; -469,10 +470,39 @@ def get_video_replacement(item_idx: int):; symbols: get_video_replacement, MiniMaxM3VideoBackend, load_bytes, compute_frames_index_to_sample
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/mm_preprocess.py
@@ -3,8 +3,9 @@
-from typing import cast
+from typing import Any, Literal, cast
+import numpy.typing as npt
@@ -469,10 +470,39 @@ def get_video_replacement(item_idx: int):
-# TODO(Isotr0py): Tie with MinimaxVideoProcessor
-# after https://github.com/vllm-project/vllm/pull/44126
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/mm_preprocess.py` modified +37/-7
- 验证与风险: diff 自带测试面 `tests/multimodal/test_video.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #49149 - [Bugfix][MiniMax-M3] Fix token-major top-k buffer handling in Triton …

- 链接: https://github.com/vllm-project/vllm/pull/49149
- 状态/时间: merged / 2026-07-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `d1a8ba63d9d2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+13/-3，可读 patch 44 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Fix token-major top-k buffer handling in Triton …」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/indexer.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Fix token-major top-k buffer handling in Triton …」；主要实现面是 `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/indexer.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-1 (9 lines); hunks: -384,7 +384,14 @@ def forward(; symbols: forward，涉及 `forward`；`vllm/models/minimax_m3/common/indexer.py` modified +5/-2 (7 lines); hunks: -424,6 +424,9 @@ def forward(; -441,7 +444,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-1 (9 lines); hunks: -384,7 +384,14 @@ def forward(; symbols: forward
  - `vllm/models/minimax_m3/common/indexer.py` modified +5/-2 (7 lines); hunks: -424,6 +424,9 @@ def forward(; -441,7 +444,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -384,7 +384,14 @@ def forward(
-        topk = layer.topk_indices_buffer  # type: ignore[attr-defined]
+        topk_buffer = layer.topk_indices_buffer  # type: ignore[attr-defined]
+        assert topk_buffer is not None
+        topk = (
+            topk_buffer
+            if current_platform.is_rocm()
diff -- vllm/models/minimax_m3/common/indexer.py
@@ -424,6 +424,9 @@ def forward(
+        buf_htk = (
+            buf if buf is None or current_platform.is_rocm() else buf.transpose(0, 1)
+        )
@@ -441,7 +444,7 @@ def forward(
-                out=buf,
+                out=buf_htk,
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-1; `vllm/models/minimax_m3/common/indexer.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #48846 - [Bugfix][Tool Parser] Preserve whitespace in parameter values (MiniMax M2, Qwen3, MiniCPM5 XML)

- 链接: https://github.com/vllm-project/vllm/pull/48846
- 状态/时间: merged / 2026-07-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/parser/minimax_m2.py`；关联提交 `11d291511a35`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+164/-9，可读 patch 249 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Tool Parser] Preserve whitespace in parameter values (MiniMax M2, Qwen3, MiniCPM5 XML)」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/parser/minimax_m2.py`；技术摘要: 覆盖「[Bugfix][Tool Parser] Preserve whitespace in parameter values (MiniMax M2, Qwen3, MiniCPM5 XML)」；主要实现面是 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/parser/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +34/-0 (34 lines); hunks: -567,3 +567,37 @@ def test_nil_string_preserved(self):; symbols: test_nil_string_preserved, TestParameterWhitespace, test_whitespace_preserved, test_whitespace_preserved_across_chunks，涉及 `test_nil_string_preserved, TestParameterWhitespace, test_whitespace_preserved`；`vllm/parser/minimax_m2.py` modified +5/-2 (7 lines); hunks: -69,7 +69,9 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) ->...; -82,7 +84,8 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) ->...; symbols: _minimax_m2_arg_converter，涉及 `_minimax_m2_arg_converter`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +34/-0 (34 lines); hunks: -567,3 +567,37 @@ def test_nil_string_preserved(self):; symbols: test_nil_string_preserved, TestParameterWhitespace, test_whitespace_preserved, test_whitespace_preserved_across_chunks
  - `vllm/parser/minimax_m2.py` modified +5/-2 (7 lines); hunks: -69,7 +69,9 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) ->...; -82,7 +84,8 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) ->...; symbols: _minimax_m2_arg_converter
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_minimax_m2_tool_parser.py
@@ -567,3 +567,37 @@ def test_nil_string_preserved(self):
+class TestParameterWhitespace:
+    """Parameter values must preserve surrounding whitespace."""
+    def test_whitespace_preserved(self, parser):
+        results = _feed(
+            parser,
+            [
diff -- vllm/parser/minimax_m2.py
@@ -69,7 +69,9 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) -> str:
-        params[name] = match.group("value").strip()
+        # Keep the value verbatim (like the glm47 converter): it is inline
+        # between `>` and `</parameter>`, so surrounding whitespace is data.
+        params[name] = match.group("value")
@@ -82,7 +84,8 @@ def _minimax_m2_arg_converter(raw_args: str, partial: bool) -> str:
-                params[name] = match.group("value").strip()
```

- 已读文件:
  - tests: `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +34/-0
  - runtime: `vllm/parser/minimax_m2.py` modified +5/-2
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_qwen3.py`, `tests/tool_parsers/test_minicpm5xml_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_parsers/test_qwen3coder_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48523 - [Bugfix] Skip minimax_m3 tool parser tests when Rust extension is absent

- 链接: https://github.com/vllm-project/vllm/pull/48523
- 状态/时间: merged / 2026-07-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_minimax_m3_tool_parser.py`；关联提交 `af1f036a70e0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-0，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Skip minimax_m3 tool parser tests when Rust extension is absent」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_minimax_m3_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Skip minimax_m3 tool parser tests when Rust extension is absent」；主要实现面是 `tests/tool_parsers/test_minimax_m3_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +4/-0 (4 lines); hunks: -14,6 +14,10。
- 代码 diff 细节:
  - `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +4/-0 (4 lines); hunks: -14,6 +14,10
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_minimax_m3_tool_parser.py
@@ -14,6 +14,10 @@
+# MinimaxM3ToolParser extends RustToolParser; skip when the PyO3 extension
+# is absent (mirrors the guard in test_rust_tool_parser.py).
+pytest.importorskip("vllm._rust_tool_parser")
```

- 已读文件:
  - tests: `tests/tool_parsers/test_minimax_m3_tool_parser.py` modified +4/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_minimax_m3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47984 - [ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA

- 链接: https://github.com/vllm-project/vllm/pull/47984
- 状态/时间: merged / 2026-07-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`；关联提交 `95aab66e9585`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+182/-15，可读 patch 276 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA」；主要实现面是 `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +41/-10 (51 lines); hunks: -49,15 +49,16 @@ def _build_sparse_block_table_kernel(; -82,7 +83,7 @@ def _build_sparse_block_table_kernel(; symbols: _build_sparse_block_table_kernel, _build_sparse_block_table_prefill_kernel, minimax_m3_build_sparse_block_table_prefill，涉及 `_build_sparse_block_table_kernel, _build_sparse_block_table_prefill_kernel, minimax_m3_build_sparse_block_table_prefill`；`vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +1/-5 (6 lines); hunks: -55,11 +55,6 @@ def forward(; -72,6 +67,7 @@ def forward(; symbols: forward，涉及 `forward`；`tests/kernels/attention/test_minimax_m3.py` modified +140/-0 (140 lines); hunks: -1010,6 +1010,146 @@ def _build_decode_inputs(; symbols: _build_decode_inputs, test_aiter_sparse_block_table_handles_padded_decode_rows, test_aiter_decode_sparse_block_table_supports_spec_decode，涉及 `_build_decode_inputs, test_aiter_sparse_block_table_handles_padded_decode_rows, test_aiter_decode_sparse_block_table_supports_spec_decode`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +41/-10 (51 lines); hunks: -49,15 +49,16 @@ def _build_sparse_block_table_kernel(; -82,7 +83,7 @@ def _build_sparse_block_table_kernel(; symbols: _build_sparse_block_table_kernel, _build_sparse_block_table_prefill_kernel, minimax_m3_build_sparse_block_table_prefill
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +1/-5 (6 lines); hunks: -55,11 +55,6 @@ def forward(; -72,6 +67,7 @@ def forward(; symbols: forward
  - `tests/kernels/attention/test_minimax_m3.py` modified +140/-0 (140 lines); hunks: -1010,6 +1010,146 @@ def _build_decode_inputs(; symbols: _build_decode_inputs, test_aiter_sparse_block_table_handles_padded_decode_rows, test_aiter_decode_sparse_block_table_supports_spec_decode
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -49,15 +49,16 @@ def _build_sparse_block_table_kernel(
-    last_blk = (seq_len - 1) // SPARSE_BLOCK_SIZE_C
+    has_tokens = seq_len > 0
+    last_blk = tl.maximum((seq_len - 1) // SPARSE_BLOCK_SIZE_C, 0)
-    valid = blk >= 0
+    valid = has_tokens & (blk >= 0)
@@ -82,7 +83,7 @@ def _build_sparse_block_table_kernel(
diff -- vllm/models/minimax_m3/amd/sparse_attention_msa.py
@@ -55,11 +55,6 @@ def forward(
-            if d.decode_query_len != 1:
-                raise NotImplementedError(
-                    "MiniMax-M3 AITER sparse PA does not support speculative "
-                    f"decode_query_len={d.decode_query_len}"
-                )
@@ -72,6 +67,7 @@ def forward(
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -1010,6 +1010,146 @@ def _build_decode_inputs(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` modified +41/-10; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` modified +1/-5
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +140/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44849 - [ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER

- 链接: https://github.com/vllm-project/vllm/pull/44849
- 状态/时间: merged / 2026-07-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；关联提交 `b50ef9c6ed97`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-0，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；技术摘要: 覆盖「[ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER」；主要实现面是 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +12/-0 (12 lines); hunks: -6,6 +6,7; -235,6 +236,17 @@ def _minimax_qk_norm_fusion(; symbols: _minimax_qk_norm_fusion，涉及 `_minimax_qk_norm_fusion`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +12/-0 (12 lines); hunks: -6,6 +6,7; -235,6 +236,17 @@ def _minimax_qk_norm_fusion(; symbols: _minimax_qk_norm_fusion
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py
@@ -6,6 +6,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -235,6 +236,17 @@ def _minimax_qk_norm_fusion(
+    # ROCm AITER fused QK-norm + AllReduce; skips unaligned shapes.
+    if tp_world > 1 and num_tokens <= MINIMAX_QK_NORM_MAX_TOKEN_NUM:
+        pack_size = 16 // qkv.element_size()
+        warp_work_size = 32 * pack_size
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +12/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #47287 - [ROCm][MiniMax-M3] Add AITER sparse paged attention

- 链接: https://github.com/vllm-project/vllm/pull/47287
- 状态/时间: merged / 2026-07-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py` 等 11 个文件；关联提交 `ee5a89f4d7b8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1553/-127，可读 patch 2389 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M3] Add AITER sparse paged attention」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；技术摘要: 覆盖「[ROCm][MiniMax-M3] Add AITER sparse paged attention」；主要实现面是 `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` added +466/-0 (466 lines); hunks: -0,0 +1,466; symbols: _is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, minimax_m3_build_sparse_block_table, _build_sparse_block_table_prefill_kernel，涉及 `_is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, minimax_m3_build_sparse_block_table`；`vllm/models/minimax_m3/amd/model.py` modified +214/-25 (239 lines); hunks: -35,6 +35,7; -93,6 +94,7; symbols: __init__, get_kv_cache_spec, _ensure_aiter_sparse_pa_kv_cache，涉及 `__init__, get_kv_cache_spec, _ensure_aiter_sparse_pa_kv_cache`；`vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +160/-0 (160 lines); hunks: -52,6 +52,8; -72,6 +74,10 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel，涉及 `_gqa_sparse_fwd_kernel`；`vllm/models/minimax_m3/amd/sparse_attention_msa.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: MiniMaxM3SparseAiterPAImpl, forward，涉及 `MiniMaxM3SparseAiterPAImpl, forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/sparse_pa.py` added +466/-0 (466 lines); hunks: -0,0 +1,466; symbols: _is_fp8_kv_cache_tensor, _build_sparse_block_table_kernel, minimax_m3_build_sparse_block_table, _build_sparse_block_table_prefill_kernel
  - `vllm/models/minimax_m3/amd/model.py` modified +214/-25 (239 lines); hunks: -35,6 +35,7; -93,6 +94,7; symbols: __init__, get_kv_cache_spec, _ensure_aiter_sparse_pa_kv_cache
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +160/-0 (160 lines); hunks: -52,6 +52,8; -72,6 +74,10 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel
  - `vllm/models/minimax_m3/amd/sparse_attention_msa.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: MiniMaxM3SparseAiterPAImpl, forward
  - `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +65/-8 (73 lines); hunks: -12,7 +12,9; -70,7 +72,9 @@ def _sparse_attn_prefill_kwargs() -> dict:; symbols: _sparse_attn_prefill_kwargs, _gqa_sparse_fwd_kernel
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/sparse_pa.py
@@ -0,0 +1,466 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""AITER page-16 sparse paged-attention helpers for MiniMax-M3 on ROCm."""
+import torch
+try:
+    from vllm.triton_utils import tl, triton
diff -- vllm/models/minimax_m3/amd/model.py
@@ -35,6 +35,7 @@
+from vllm.model_executor.layers.attention.attention import set_default_quant_scales
@@ -93,6 +94,7 @@
+    minimax_m3_use_aiter_sparse_pa,
@@ -103,6 +105,7 @@
+    is_quantized_kv_cache,
@@ -636,6 +639,11 @@ def __init__(
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -52,6 +52,8 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/sparse_pa.py` added +466/-0; `vllm/models/minimax_m3/amd/model.py` modified +214/-25; `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +160/-0; `vllm/models/minimax_m3/amd/sparse_attention_msa.py` added +94/-0; `vllm/models/minimax_m3/amd/ops/sparse_attn.py` modified +65/-8; `vllm/models/minimax_m3/common/sparse_attention.py` modified +48/-4
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47158 - [ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8

- 链接: https://github.com/vllm-project/vllm/pull/47158
- 状态/时间: merged / 2026-07-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_minimax_m3_amd_ops.py`；关联提交 `2c64b4c1cc18`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+107/-12，可读 patch 139 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/kernels/test_minimax_m3_amd_ops.py`；技术摘要: 覆盖「[ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8」；主要实现面是 `tests/kernels/test_minimax_m3_amd_ops.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/test_minimax_m3_amd_ops.py` modified +94/-0 (94 lines); hunks: -335,3 +335,97 @@ def test_mxfp8_linear_emulation_bf16_at_load(; symbols: test_mxfp8_linear_emulation_bf16_at_load, _capture_expert_mask, _fake_fused_moe, test_aiter_mxfp8_ep_expert_mask_both_master_modes，涉及 `test_mxfp8_linear_emulation_bf16_at_load, _capture_expert_mask, _fake_fused_moe`。
- 代码 diff 细节:
  - `tests/kernels/test_minimax_m3_amd_ops.py` modified +94/-0 (94 lines); hunks: -335,3 +335,97 @@ def test_mxfp8_linear_emulation_bf16_at_load(; symbols: test_mxfp8_linear_emulation_bf16_at_load, _capture_expert_mask, _fake_fused_moe, test_aiter_mxfp8_ep_expert_mask_both_master_modes
- 关键代码摘录:

```diff
diff -- tests/kernels/test_minimax_m3_amd_ops.py
@@ -335,3 +335,97 @@ def test_mxfp8_linear_emulation_bf16_at_load(
+# ── EP expert_mask handling for the FlyDSL (AITER_MXFP8) MoE ────────────────
+# Regression for the EP + aiter-master-switch interaction: under expert
+# parallelism ``RoutedExperts.expert_map`` hands the experts either the 0/1
+# ``expert_mask`` (aiter master ON, ``rocm_aiter_fmoe_enabled``) or vLLM's -1
+# index map (master OFF). ``AiterMxfp8Experts.apply`` must forward the right 0/1
+# mask to aiter in BOTH cases. The old code always rebuilt the mask via
```

- 已读文件:
  - tests: `tests/kernels/test_minimax_m3_amd_ops.py` modified +94/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_minimax_m3_amd_ops.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47631 - [Perf] Minimax M3 - Support cross-layer allreduce-norm fusion

- 链接: https://github.com/vllm-project/vllm/pull/47631
- 状态/时间: merged / 2026-07-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `2afa3f7e9502`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+65/-17，可读 patch 228 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Minimax M3 - Support cross-layer allreduce-norm fusion」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/deepseek_v32/nvidia/model.py`；技术摘要: 覆盖「[Perf] Minimax M3 - Support cross-layer allreduce-norm fusion」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/deepseek_v32/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +37/-10 (47 lines); hunks: -196,6 +196,7 @@ def __init__(; -261,6 +262,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/deepseek_v32/nvidia/model.py` modified +4/-4 (8 lines); hunks: -72,17 +72,17 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +37/-10 (47 lines); hunks: -196,6 +196,7 @@ def __init__(; -261,6 +262,7 @@ def __init__(; symbols: __init__
  - `vllm/models/deepseek_v32/nvidia/model.py` modified +4/-4 (8 lines); hunks: -72,17 +72,17 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -196,6 +196,7 @@ def __init__(
+        reduce_results: bool = True,
@@ -261,6 +262,7 @@ def __init__(
+            reduce_results=reduce_results,
@@ -658,14 +660,10 @@ def __init__(
-        # Complete the preceding dense MLP's deferred all-reduce
-        # (reduce_results=False), fused into this layer's input_layernorm.
diff -- vllm/models/deepseek_v32/nvidia/model.py
@@ -72,17 +72,17 @@ def __init__(
+            # Defer the MoE cross-rank all-reduce; it is fused into the next
+            # layer's input_layernorm (or the final norm) via
+            # fused_allreduce_rms_norm.
+                reduce_results=False,
-            # Defer the MoE cross-rank all-reduce; it is fused into the next
-            # layer's input_layernorm (or the final norm) via
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +37/-10; `vllm/models/deepseek_v32/nvidia/model.py` modified +4/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46117 - [ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3

- 链接: https://github.com/vllm-project/vllm/pull/46117
- 状态/时间: merged / 2026-07-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/test_minimax_m3_amd_ops.py`；关联提交 `d9e57ea82e3e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+226/-42，可读 patch 372 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `tests/kernels/test_minimax_m3_amd_ops.py`；技术摘要: 覆盖「[ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3」；主要实现面是 `tests/kernels/test_minimax_m3_amd_ops.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/test_minimax_m3_amd_ops.py` modified +87/-0 (87 lines); hunks: -284,6 +284,93 @@ def test_mxfp8_native_moe(T, H, inter, E, top_k):; symbols: test_mxfp8_native_moe, _ref_grouped_gemm, test_mxfp8_grouped_gemm_native，涉及 `test_mxfp8_native_moe, _ref_grouped_gemm, test_mxfp8_grouped_gemm_native`。
- 代码 diff 细节:
  - `tests/kernels/test_minimax_m3_amd_ops.py` modified +87/-0 (87 lines); hunks: -284,6 +284,93 @@ def test_mxfp8_native_moe(T, H, inter, E, top_k):; symbols: test_mxfp8_native_moe, _ref_grouped_gemm, test_mxfp8_grouped_gemm_native
- 关键代码摘录:

```diff
diff -- tests/kernels/test_minimax_m3_amd_ops.py
@@ -284,6 +284,93 @@ def test_mxfp8_native_moe(T, H, inter, E, top_k):
+# --------------------------------------------------------------------------- #
+# Native MXFP8 grouped GEMM (dot_scaled) vs pure-PyTorch grouped matmul
+# --------------------------------------------------------------------------- #
+def _ref_grouped_gemm(a_deq, w_deq, topk_ids, a_div, num_valid, mul_weight=None):
+    """Pure-PyTorch reference for ``_grouped_gemm_mxfp8``.
+    For each routed (expanded) token ``tid in [0, num_valid)`` the kernel writes
```

- 已读文件:
  - tests: `tests/kernels/test_minimax_m3_amd_ops.py` modified +87/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_minimax_m3_amd_ops.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47502 - [Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels

- 链接: https://github.com/vllm-project/vllm/pull/47502
- 状态/时间: merged / 2026-07-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/__init__.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py` 等 8 个文件；关联提交 `902158949803`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+233/-72，可读 patch 577 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；技术摘要: 覆盖「[Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels」；主要实现面是 `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/indexer_msa.py` modified +135/-35 (170 lines); hunks: -2,16 +2,21; -22,6 +27,7; symbols: MiniMaxM3IndexerMSABackend, MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder, __init__，涉及 `MiniMaxM3IndexerMSABackend, MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder`；`vllm/models/minimax_m3/common/ops/index_topk.py` modified +67/-15 (82 lines); hunks: -757,33 +757,33 @@ def minimax_m3_index_topk(; -800,13 +800,16 @@ def minimax_m3_index_decode(; symbols: minimax_m3_index_topk, minimax_m3_index_decode, minimax_m3_index_decode_score，涉及 `minimax_m3_index_topk, minimax_m3_index_decode, minimax_m3_index_decode_score`；`vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +7/-11 (18 lines); hunks: -43,7 +43,6; -84,7 +83,6 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel，涉及 `_gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel`；`vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +6/-3 (9 lines); hunks: -39,7 +39,8 @@ def forward(; -56,7 +57,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/indexer_msa.py` modified +135/-35 (170 lines); hunks: -2,16 +2,21; -22,6 +27,7; symbols: MiniMaxM3IndexerMSABackend, MiniMaxM3IndexerMSAMetadata, MiniMaxM3IndexerMSAMetadataBuilder, __init__
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +67/-15 (82 lines); hunks: -757,33 +757,33 @@ def minimax_m3_index_topk(; -800,13 +800,16 @@ def minimax_m3_index_decode(; symbols: minimax_m3_index_topk, minimax_m3_index_decode, minimax_m3_index_decode_score
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +7/-11 (18 lines); hunks: -43,7 +43,6; -84,7 +83,6 @@ def _gqa_sparse_fwd_kernel(; symbols: _gqa_sparse_fwd_kernel, _gqa_sparse_decode_kernel
  - `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +6/-3 (9 lines); hunks: -39,7 +39,8 @@ def forward(; -56,7 +57,7 @@ def forward(; symbols: forward
  - `vllm/models/minimax_m3/common/indexer.py` modified +7/-0 (7 lines); hunks: -256,6 +256,13 @@ def __init__(; symbols: __init__, MiniMaxM3IndexerTritonMetadataBuilder
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/indexer_msa.py
@@ -2,16 +2,21 @@
-Prefill scores with ``fmha_sm100``'s score-only (``OnlyScore``) path then selects
-top-k blocks with the Triton ``minimax_m3_index_topk`` kernel -- fmha is much
-faster than Triton for the wide prefill score (benchmarked ~3-5x).
-Decode uses the Triton fused ``minimax_m3_index_decode`` (the same kernel the
-Triton indexer impl uses): for q_len==1 it is a purpose-built vector x matrix
-score (no wasted tensor-core tiles) with a 256-way split-K and a fused split-K
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -757,33 +757,33 @@ def minimax_m3_index_topk(
-def minimax_m3_index_decode(
+def minimax_m3_index_decode_score(
-    topk: int,
-    out: torch.Tensor | None = None,
+    score_out: torch.Tensor | None = None,
-    """Decode index block-score + top-k, both split-K (cudagraph-safe).
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -43,7 +43,6 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/indexer_msa.py` modified +135/-35; `vllm/models/minimax_m3/common/ops/index_topk.py` modified +67/-15; `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +7/-11; `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py` modified +6/-3; `vllm/models/minimax_m3/common/indexer.py` modified +7/-0; `vllm/models/minimax_m3/nvidia/model.py` modified +4/-3
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +4/-4
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47269 - [ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing

- 链接: https://github.com/vllm-project/vllm/pull/47269
- 状态/时间: merged / 2026-07-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`；关联提交 `4e5ca89cfe98`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+41/-1，可读 patch 63 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing」；模型线: MiniMax M2 Series；类别: 模型实现调整；主要 diff: `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +41/-1 (42 lines); hunks: -135,6 +135,37 @@ def _sparse_attention_layer_ids(config: PretrainedConfig) -...; -541,6 +572,12 @@ def __init__(; symbols: _sparse_attention_layer_ids, _sparse_attention_layer_ordinals, _should_skip_index_topk, _is_moe_layer，涉及 `_sparse_attention_layer_ids, _sparse_attention_layer_ordinals, _should_skip_index_topk`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +41/-1 (42 lines); hunks: -135,6 +135,37 @@ def _sparse_attention_layer_ids(config: PretrainedConfig) -...; -541,6 +572,12 @@ def __init__(; symbols: _sparse_attention_layer_ids, _sparse_attention_layer_ordinals, _should_skip_index_topk, _is_moe_layer
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -135,6 +135,37 @@ def _sparse_attention_layer_ids(config: PretrainedConfig) -> set[int]:
+def _sparse_attention_layer_ordinals(config: PretrainedConfig) -> dict[int, int]:
+    """Map each sparse-attention layer id to its ordinal among sparse layers."""
+    return {
+        lid: ordinal
+        for ordinal, lid in enumerate(sorted(_sparse_attention_layer_ids(config)))
+    }
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +41/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46474 - [ROCm][Perf] Fused shared expert for Minimax M3

- 链接: https://github.com/vllm-project/vllm/pull/46474
- 状态/时间: merged / 2026-06-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`；关联提交 `51a99565c398`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+46/-13，可读 patch 127 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Fused shared expert for Minimax M3」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm][Perf] Fused shared expert for Minimax M3」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +46/-13 (59 lines); hunks: -23,8 +23,9; -96,7 +97,6; symbols: _fuse_shared_experts_enabled, forward, _aiter_moe_fused_shared_experts_enabled, MiniMaxM3MoE，涉及 `_fuse_shared_experts_enabled, forward, _aiter_moe_fused_shared_experts_enabled`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +46/-13 (59 lines); hunks: -23,8 +23,9; -96,7 +97,6; symbols: _fuse_shared_experts_enabled, forward, _aiter_moe_fused_shared_experts_enabled, MiniMaxM3MoE
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -23,8 +23,9 @@
-import vllm.envs as envs
+from vllm import envs
+from vllm._aiter_ops import rocm_aiter_ops
@@ -96,7 +97,6 @@
-from vllm.platforms import current_platform
@@ -107,14 +107,15 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +46/-13
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46545 - [ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model

- 链接: https://github.com/vllm-project/vllm/pull/46545
- 状态/时间: merged / 2026-06-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`；关联提交 `c2507fb2937a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+110/-20，可读 patch 266 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +47/-3 (50 lines); hunks: -23,6 +23,7; -95,6 +96,7; symbols: _fuse_shared_experts_enabled, _sparse_attention_layer_ids, __init__, forward，涉及 `_fuse_shared_experts_enabled, _sparse_attention_layer_ids, __init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +47/-3 (50 lines); hunks: -23,6 +23,7; -95,6 +96,7; symbols: _fuse_shared_experts_enabled, _sparse_attention_layer_ids, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -23,6 +23,7 @@
+import vllm.envs as envs
@@ -95,6 +96,7 @@
+from vllm.platforms import current_platform
@@ -104,6 +106,23 @@
+def _fuse_shared_experts_enabled(config: PretrainedConfig) -> bool:
+    """Whether to fuse the shared expert into the routed grouped MoE.
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +47/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46419 - [ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4

- 链接: https://github.com/vllm-project/vllm/pull/46419
- 状态/时间: merged / 2026-06-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`；关联提交 `8e394244a59a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+27/-8，可读 patch 100 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +1/-0 (1 lines); hunks: -309,6 +309,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +1/-0 (1 lines); hunks: -309,6 +309,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -309,6 +309,7 @@ def __init__(
+            intermediate_pad=0,
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46546 - [ROCm][ [Perf] sparse attention optimization on minimax-m3

- 链接: https://github.com/vllm-project/vllm/pull/46546
- 状态/时间: merged / 2026-06-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `c63cd4906c2a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+1238/-36，可读 patch 1313 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][ [Perf] sparse attention optimization on minimax-m3」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`；技术摘要: 覆盖「[ROCm][ [Perf] sparse attention optimization on minimax-m3」；主要实现面是 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/ops/index_topk.py` added +939/-0 (939 lines); hunks: -0,0 +1,939; symbols: _compare_and_swap, _bitonic_merge, _index_block_score_kernel, _topk_index_kernel，涉及 `_compare_and_swap, _bitonic_merge, _index_block_score_kernel`；`vllm/models/minimax_m3/amd/ops/sparse_attn.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: _sparse_attn_prefill_kwargs, _gqa_sparse_fwd_kernel, minimax_m3_sparse_attn，涉及 `_sparse_attn_prefill_kwargs, _gqa_sparse_fwd_kernel, minimax_m3_sparse_attn`；`vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +0/-26 (26 lines); hunks: -31,30 +31,6; -498,7 +474,6 @@ def minimax_m3_sparse_attn(; symbols: _sparse_attn_num_stages_kwarg, minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode，涉及 `_sparse_attn_num_stages_kwarg, minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode`；`vllm/models/minimax_m3/common/indexer.py` modified +14/-5 (19 lines); hunks: -27,12 +27,21。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/ops/index_topk.py` added +939/-0 (939 lines); hunks: -0,0 +1,939; symbols: _compare_and_swap, _bitonic_merge, _index_block_score_kernel, _topk_index_kernel
  - `vllm/models/minimax_m3/amd/ops/sparse_attn.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: _sparse_attn_prefill_kwargs, _gqa_sparse_fwd_kernel, minimax_m3_sparse_attn
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +0/-26 (26 lines); hunks: -31,30 +31,6; -498,7 +474,6 @@ def minimax_m3_sparse_attn(; symbols: _sparse_attn_num_stages_kwarg, minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode
  - `vllm/models/minimax_m3/common/indexer.py` modified +14/-5 (19 lines); hunks: -27,12 +27,21
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +14/-5 (19 lines); hunks: -24,12 +24,21
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/ops/index_topk.py
@@ -0,0 +1,939 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Triton kernels for MiniMax M3 lightning-indexer block scoring + top-k.
+Index queries score each 128-token block of index keys (max over the block),
+then the top-k blocks (plus forced init/local blocks) are selected per query
+token. Adapted to vLLM's paged KV cache: the KV page size is forced to equal the
diff -- vllm/models/minimax_m3/amd/ops/sparse_attn.py
@@ -0,0 +1,271 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm gfx942/gfx950 block-sparse GQA prefill kernel for MiniMax-M3.
+Only the prefill path is specialized on CDNA: each 128-token KV block is split
+into SUB_K-token sub-tiles to right-size the per-block QK/PV MFMAs. Everything
+else -- the decode split-K kernels, the FP8 dtype set, the sparse block size --
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -31,30 +31,6 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/ops/index_topk.py` added +939/-0; `vllm/models/minimax_m3/amd/ops/sparse_attn.py` added +271/-0; `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +0/-26; `vllm/models/minimax_m3/common/indexer.py` modified +14/-5; `vllm/models/minimax_m3/common/sparse_attention.py` modified +14/-5
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45810 - [Model][MiniMax-M3] Add pipeline parallelism support

- 链接: https://github.com/vllm-project/vllm/pull/45810
- 状态/时间: merged / 2026-06-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `d7c1821b5a31`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+124/-49，可读 patch 397 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][MiniMax-M3] Add pipeline parallelism support」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Model][MiniMax-M3] Add pipeline parallelism support」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +61/-24 (85 lines); hunks: -30,7 +30,7; -64,12 +64,15; symbols: __init__, embed_input_ids, forward，涉及 `__init__, embed_input_ids, forward`；`vllm/models/minimax_m3/nvidia/model.py` modified +61/-24 (85 lines); hunks: -21,7 +21,7; -56,12 +56,15; symbols: __init__, embed_input_ids, forward，涉及 `__init__, embed_input_ids, forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +61/-24 (85 lines); hunks: -30,7 +30,7; -64,12 +64,15; symbols: __init__, embed_input_ids, forward
  - `vllm/models/minimax_m3/nvidia/model.py` modified +61/-24 (85 lines); hunks: -21,7 +21,7; -56,12 +56,15; symbols: __init__, embed_input_ids, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -30,7 +30,7 @@
-from vllm.distributed import get_tensor_model_parallel_world_size
+from vllm.distributed import get_pp_group, get_tensor_model_parallel_world_size
@@ -64,12 +64,15 @@
+    SupportsPP,
+    PPMissingLayer,
+    make_empty_intermediate_tensors_factory,
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -21,7 +21,7 @@
-from vllm.distributed import get_tensor_model_parallel_world_size
+from vllm.distributed import get_pp_group, get_tensor_model_parallel_world_size
@@ -56,12 +56,15 @@
+    SupportsPP,
+    PPMissingLayer,
+    make_empty_intermediate_tensors_factory,
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +61/-24; `vllm/models/minimax_m3/nvidia/model.py` modified +61/-24
- 验证与风险: runtime 路径改动集中在 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45718 - [Bugfix] Parse MiniMax M3 streaming reasoning by text markers

- 链接: https://github.com/vllm-project/vllm/pull/45718
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_minimax_m3_reasoning_parser.py`, `vllm/reasoning/minimax_m3_reasoning_parser.py`；关联提交 `d8e422ccda9b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+357/-67，可读 patch 496 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Parse MiniMax M3 streaming reasoning by text markers」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/reasoning/minimax_m3_reasoning_parser.py`, `tests/reasoning/test_minimax_m3_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] Parse MiniMax M3 streaming reasoning by text markers」；主要实现面是 `vllm/reasoning/minimax_m3_reasoning_parser.py`, `tests/reasoning/test_minimax_m3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/minimax_m3_reasoning_parser.py` modified +215/-66 (281 lines); hunks: -19,10 +19,12 @@ class MiniMaxM3ReasoningParser(BaseThinkingReasoningParser):; -35,9 +37,135 @@ def end_token(self) -> str:; symbols: MiniMaxM3ReasoningParser, end_token, __init__, _encode_text，涉及 `MiniMaxM3ReasoningParser, end_token, __init__`；`tests/reasoning/test_minimax_m3_reasoning_parser.py` modified +142/-1 (143 lines); hunks: -83,6 +83,20 @@ def convert_tokens_to_string(self, tokens: list[str]) -> str:; -105,7 +119,8 @@ def run_streaming(; symbols: convert_tokens_to_string, SplitMiniMaxM3Tokenizer, tokenize, RuntimeSplitMiniMaxM3Tokenizer，涉及 `convert_tokens_to_string, SplitMiniMaxM3Tokenizer, tokenize`。
- 代码 diff 细节:
  - `vllm/reasoning/minimax_m3_reasoning_parser.py` modified +215/-66 (281 lines); hunks: -19,10 +19,12 @@ class MiniMaxM3ReasoningParser(BaseThinkingReasoningParser):; -35,9 +37,135 @@ def end_token(self) -> str:; symbols: MiniMaxM3ReasoningParser, end_token, __init__, _encode_text
  - `tests/reasoning/test_minimax_m3_reasoning_parser.py` modified +142/-1 (143 lines); hunks: -83,6 +83,20 @@ def convert_tokens_to_string(self, tokens: list[str]) -> str:; -105,7 +119,8 @@ def run_streaming(; symbols: convert_tokens_to_string, SplitMiniMaxM3Tokenizer, tokenize, RuntimeSplitMiniMaxM3Tokenizer
- 关键代码摘录:

```diff
diff -- vllm/reasoning/minimax_m3_reasoning_parser.py
@@ -19,10 +19,12 @@ class MiniMaxM3ReasoningParser(BaseThinkingReasoningParser):
-    The M3 tokenizer exposes both markers as complete vocabulary tokens. The
-    chat template may also prefill the start marker when
-    ``thinking_mode="enabled"``, so generated text can begin directly inside a
-    reasoning block without emitting ``<mm:think>`` again.
+    The M3 tokenizer exposes both markers as complete vocabulary entries, but
+    generated marker text may be tokenized into smaller pieces. The streaming
diff -- tests/reasoning/test_minimax_m3_reasoning_parser.py
@@ -83,6 +83,20 @@ def convert_tokens_to_string(self, tokens: list[str]) -> str:
+class SplitMiniMaxM3Tokenizer(MiniMaxM3Tokenizer):
+    """Tokenizer that exposes marker vocab entries but encodes them as text."""
+    def tokenize(self, text: str) -> list[str]:
+        return list(text)
+class RuntimeSplitMiniMaxM3Tokenizer(MiniMaxM3Tokenizer):
+    """Tokenizer whose runtime output splits markers despite atomic encodes."""
```

- 已读文件:
  - runtime: `vllm/reasoning/minimax_m3_reasoning_parser.py` modified +215/-66
  - tests: `tests/reasoning/test_minimax_m3_reasoning_parser.py` modified +142/-1
- 验证与风险: diff 自带测试面 `tests/reasoning/test_minimax_m3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45892 - [Minimax-M3] BF16/FP8 Indexer using MSA

- 链接: https://github.com/vllm-project/vllm/pull/45892
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py` 等 9 个文件；关联提交 `6691f087a65b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+1048/-104，可读 patch 1712 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Minimax-M3] BF16/FP8 Indexer using MSA」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Minimax-M3] BF16/FP8 Indexer using MSA」；主要实现面是 `vllm/models/minimax_m3/nvidia/indexer_msa.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/indexer_msa.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: MiniMaxM3IndexerMSABackend, get_builder_cls, MiniMaxM3IndexerMSAPrefillMetadata, MiniMaxM3IndexerMSAMetadata，涉及 `MiniMaxM3IndexerMSABackend, get_builder_cls, MiniMaxM3IndexerMSAPrefillMetadata`；`vllm/models/minimax_m3/common/indexer.py` modified +60/-8 (68 lines); hunks: -25,12 +25,14; -46,6 +48,8; symbols: MiniMaxM3IndexerBackend, __init__, forward，涉及 `MiniMaxM3IndexerBackend, __init__, forward`；`vllm/models/minimax_m3/nvidia/model.py` modified +40/-4 (44 lines); hunks: -402,6 +402,7 @@ def __init__(; -489,6 +490,10 @@ def __init__(; symbols: __init__, forward, _run_attention，涉及 `__init__, forward, _run_attention`；`vllm/models/minimax_m3/common/ops/index_topk.py` modified +30/-12 (42 lines); hunks: -373,7 +373,10 @@ def _decode_index_score_kernel(; -709,16 +712,25 @@ def minimax_m3_index_topk(; symbols: _decode_index_score_kernel, minimax_m3_index_topk, minimax_m3_index_decode，涉及 `_decode_index_score_kernel, minimax_m3_index_topk, minimax_m3_index_decode`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/indexer_msa.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: MiniMaxM3IndexerMSABackend, get_builder_cls, MiniMaxM3IndexerMSAPrefillMetadata, MiniMaxM3IndexerMSAMetadata
  - `vllm/models/minimax_m3/common/indexer.py` modified +60/-8 (68 lines); hunks: -25,12 +25,14; -46,6 +48,8; symbols: MiniMaxM3IndexerBackend, __init__, forward
  - `vllm/models/minimax_m3/nvidia/model.py` modified +40/-4 (44 lines); hunks: -402,6 +402,7 @@ def __init__(; -489,6 +490,10 @@ def __init__(; symbols: __init__, forward, _run_attention
  - `vllm/models/minimax_m3/common/ops/index_topk.py` modified +30/-12 (42 lines); hunks: -373,7 +373,10 @@ def _decode_index_score_kernel(; -709,16 +712,25 @@ def minimax_m3_index_topk(; symbols: _decode_index_score_kernel, minimax_m3_index_topk, minimax_m3_index_decode
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +22/-15 (37 lines); hunks: -2,10 +2,11; -272,9 +273,10 @@ class MiniMaxM3SparseImpl(AttentionImplBase[MiniMaxM3Sparse...; symbols: MiniMaxM3SparseImpl, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/nvidia/indexer_msa.py
@@ -0,0 +1,251 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MSA (SM100/Blackwell) indexer impl for MiniMax M3.
+Prefill scores with ``fmha_sm100``'s score-only (``OnlyScore``) path then selects
+top-k blocks with the Triton ``minimax_m3_index_topk`` kernel -- fmha is much
+faster than Triton for the wide prefill score (benchmarked ~3-5x).
diff -- vllm/models/minimax_m3/common/indexer.py
@@ -25,12 +25,14 @@
+from vllm.logger import init_logger
+from vllm.platforms import current_platform
@@ -46,6 +48,8 @@
+logger = init_logger(__name__)
@@ -120,16 +124,20 @@ def __init__(
-        if indexer_kv_dtype != "bf16":
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -402,6 +402,7 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/indexer_msa.py` added +251/-0; `vllm/models/minimax_m3/common/indexer.py` modified +60/-8; `vllm/models/minimax_m3/nvidia/model.py` modified +40/-4; `vllm/models/minimax_m3/common/ops/index_topk.py` modified +30/-12; `vllm/models/minimax_m3/common/sparse_attention.py` modified +22/-15; `vllm/models/minimax_m3/amd/model.py` modified +28/-3
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +325/-1
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45935 - [Model]Fix MiniMaxM2ForCausalLM perf regression

- 链接: https://github.com/vllm-project/vllm/pull/45935
- 状态/时间: merged / 2026-06-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/core/test_minimax_reduce_rms.py`, `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；关联提交 `745bba5ea8fa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+215/-16，可读 patch 305 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model]Fix MiniMaxM2ForCausalLM perf regression」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `tests/kernels/core/test_minimax_reduce_rms.py`；技术摘要: 覆盖「[Model]Fix MiniMaxM2ForCausalLM perf regression」；主要实现面是 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `tests/kernels/core/test_minimax_reduce_rms.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +156/-13 (169 lines); hunks: -14,7 +14,7; -40,32 +40,171 @@ def _all_reduce_variance(var: torch.Tensor) -> torch.Tensor:; symbols: _all_reduce_variance, _minimax_qk_norm_fallback, _minimax_qk_var_kernel, _minimax_rms_apply_kernel，涉及 `_all_reduce_variance, _minimax_qk_norm_fallback, _minimax_qk_var_kernel`；`tests/kernels/core/test_minimax_reduce_rms.py` modified +59/-3 (62 lines); hunks: -10,8 +10,12; -54,8 +58,19 @@ def _worker_forward_qk(; symbols: _worker_forward_qk, test_minimax_reduce_rms_qk, test_minimax_qk_norm_triton_fallback，涉及 `_worker_forward_qk, test_minimax_reduce_rms_qk, test_minimax_qk_norm_triton_fallback`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +156/-13 (169 lines); hunks: -14,7 +14,7; -40,32 +40,171 @@ def _all_reduce_variance(var: torch.Tensor) -> torch.Tensor:; symbols: _all_reduce_variance, _minimax_qk_norm_fallback, _minimax_qk_var_kernel, _minimax_rms_apply_kernel
  - `tests/kernels/core/test_minimax_reduce_rms.py` modified +59/-3 (62 lines); hunks: -10,8 +10,12; -54,8 +58,19 @@ def _worker_forward_qk(; symbols: _worker_forward_qk, test_minimax_reduce_rms_qk, test_minimax_qk_norm_triton_fallback
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py
@@ -14,7 +14,7 @@
-from vllm.platforms import current_platform
+from vllm.triton_utils import HAS_TRITON, tl, triton
@@ -40,32 +40,171 @@ def _all_reduce_variance(var: torch.Tensor) -> torch.Tensor:
-@torch.compile(backend=current_platform.simple_compile_backend, dynamic=True)
-def _minimax_qk_norm_fallback(
+@triton.jit
diff -- tests/kernels/core/test_minimax_reduce_rms.py
@@ -10,8 +10,12 @@
-from vllm.model_executor.layers.minimax_rms_norm import MiniMaxText01RMSNormTP
+from vllm.model_executor.layers.minimax_rms_norm import (
+    MiniMaxText01RMSNormTP,
+    rms_norm_tp,
+)
+from vllm.triton_utils import HAS_TRITON
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +156/-13
  - tests: `tests/kernels/core/test_minimax_reduce_rms.py` modified +59/-3
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_minimax_reduce_rms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45896 - [feature] MiniMax-M3-MXFP4 support added

- 链接: https://github.com/vllm-project/vllm/pull/45896
- 状态/时间: merged / 2026-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/amd/model.py`；关联提交 `d112eb1ac78e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+44/-3，可读 patch 102 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[feature] MiniMax-M3-MXFP4 support added」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/model.py`；技术摘要: 覆盖「[feature] MiniMax-M3-MXFP4 support added」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` modified +12/-2 (14 lines); hunks: -924,6 +924,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; -987,14 +992,19 @@ class MiniMaxM3SparseForConditionalGeneration(; symbols: load_weights, MiniMaxM3SparseForCausalLM, __init__, MiniMaxM3SparseForConditionalGeneration，涉及 `load_weights, MiniMaxM3SparseForCausalLM, __init__`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` modified +12/-2 (14 lines); hunks: -924,6 +924,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; -987,14 +992,19 @@ class MiniMaxM3SparseForConditionalGeneration(; symbols: load_weights, MiniMaxM3SparseForCausalLM, __init__, MiniMaxM3SparseForConditionalGeneration
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -924,6 +924,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+    packed_modules_mapping = {
+        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
+        "gate_up_proj": ["gate_proj", "up_proj"],
+    }
@@ -987,14 +992,19 @@ class MiniMaxM3SparseForConditionalGeneration(
+    packed_modules_mapping = {
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` modified +12/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45720 - [Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype

- 链接: https://github.com/vllm-project/vllm/pull/45720
- 状态/时间: merged / 2026-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/sparse_attention.py`；关联提交 `efd15e192a1a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+60/-5，可读 patch 112 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype」；主要实现面是 `vllm/models/minimax_m3/common/sparse_attention.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-3 (11 lines); hunks: -291,9 +291,14 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +8/-2 (10 lines); hunks: -24,6 +24,12; -456,7 +462,7 @@ def minimax_m3_sparse_attn(; symbols: minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode，涉及 `minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode`；`tests/kernels/attention/test_minimax_m3.py` modified +44/-0 (44 lines); hunks: -15,11 +15,13; -79,6 +81,48 @@ def _allocate_main_kv_via_contract(; symbols: _allocate_main_kv_via_contract, test_sparse_impl_uses_platform_fp8_dtype, test_sparse_kernels_recognize_fp8_dtypes, _reference_index_topk，涉及 `_allocate_main_kv_via_contract, test_sparse_impl_uses_platform_fp8_dtype, test_sparse_kernels_recognize_fp8_dtypes`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-3 (11 lines); hunks: -291,9 +291,14 @@ def __init__(; symbols: __init__
  - `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +8/-2 (10 lines); hunks: -24,6 +24,12; -456,7 +462,7 @@ def minimax_m3_sparse_attn(; symbols: minimax_m3_sparse_attn, minimax_m3_sparse_attn_decode
  - `tests/kernels/attention/test_minimax_m3.py` modified +44/-0 (44 lines); hunks: -15,11 +15,13; -79,6 +81,48 @@ def _allocate_main_kv_via_contract(; symbols: _allocate_main_kv_via_contract, test_sparse_impl_uses_platform_fp8_dtype, test_sparse_kernels_recognize_fp8_dtypes, _reference_index_topk
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/common/sparse_attention.py
@@ -291,9 +291,14 @@ def __init__(
-        self.kv_cache_fp8_dtype = (
-            torch.float8_e5m2 if "e5m2" in kv_cache_dtype else torch.float8_e4m3fn
-        )
+        if "e5m2" in kv_cache_dtype:
+            self.kv_cache_fp8_dtype = (
+                torch.float8_e5m2fnuz
diff -- vllm/models/minimax_m3/common/ops/sparse_attn.py
@@ -24,6 +24,12 @@
+_FP8_DTYPES = (
+    torch.float8_e4m3fn,
+    torch.float8_e4m3fnuz,
+    torch.float8_e5m2,
+    torch.float8_e5m2fnuz,
+)
diff -- tests/kernels/attention/test_minimax_m3.py
@@ -15,11 +15,13 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/common/sparse_attention.py` modified +8/-3; `vllm/models/minimax_m3/common/ops/sparse_attn.py` modified +8/-2
  - tests: `tests/kernels/attention/test_minimax_m3.py` modified +44/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45701 - [Frontend] Add Streaming Parser Engine and new MinimaxM2 Parser

- 链接: https://github.com/vllm-project/vllm/pull/45701
- 状态/时间: merged / 2026-06-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_minimax_m2.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/parser/minimax_m2.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py` 等 6 个文件；关联提交 `f00e163f3562`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+588/-481，可读 patch 1318 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Add Streaming Parser Engine and new MinimaxM2 Parser」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`；技术摘要: 覆盖「[Frontend] Add Streaming Parser Engine and new MinimaxM2 Parser」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-278 (280 lines); hunks: -1,284 +1,8; symbols: MinimaxM2ToolParser, __init__, _generate_tool_call_id, _extract_name，涉及 `MinimaxM2ToolParser, __init__, _generate_tool_call_id`；`tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +6/-117 (123 lines); hunks: -18,7 +18,6; -34,6 +33,10 @@ def __init__(self):; symbols: FakeTokenizer, __init__, get_vocab, decode，涉及 `FakeTokenizer, __init__, get_vocab`；`vllm/reasoning/minimax_m2_reasoning_parser.py` modified +2/-51 (53 lines); hunks: -8,8 +8,8; -19,7 +19,7; symbols: MiniMaxM2ReasoningParser, start_token, end_token，涉及 `MiniMaxM2ReasoningParser, start_token, end_token`；`tests/reasoning/test_minimax_m2_reasoning_parser.py` modified +0/-26 (26 lines); hunks: -59,14 +59,6 @@ def minimax_m2_tokenizer():; -75,14 +67,6 @@ def minimax_m2_tokenizer():; symbols: minimax_m2_tokenizer，涉及 `minimax_m2_tokenizer`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-278 (280 lines); hunks: -1,284 +1,8; symbols: MinimaxM2ToolParser, __init__, _generate_tool_call_id, _extract_name
  - `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +6/-117 (123 lines); hunks: -18,7 +18,6; -34,6 +33,10 @@ def __init__(self):; symbols: FakeTokenizer, __init__, get_vocab, decode
  - `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +2/-51 (53 lines); hunks: -8,8 +8,8; -19,7 +19,7; symbols: MiniMaxM2ReasoningParser, start_token, end_token
  - `tests/reasoning/test_minimax_m2_reasoning_parser.py` modified +0/-26 (26 lines); hunks: -59,14 +59,6 @@ def minimax_m2_tokenizer():; -75,14 +67,6 @@ def minimax_m2_tokenizer():; symbols: minimax_m2_tokenizer
  - `tests/parser/engine/test_minimax_m2.py` added +264/-0 (264 lines); hunks: -0,0 +1,264; symbols: mock_tokenizer, parser, make_tools, TestNonStreaming
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -1,284 +1,8 @@
-import json
-import uuid
-from collections.abc import Sequence
+from vllm.parser.engine.registered_adapters import MinimaxM2ParserToolAdapter
-import regex as re
-from vllm.entrypoints.openai.chat_completion.protocol import (
diff -- tests/tool_parsers/test_minimax_m2_tool_parser.py
@@ -18,7 +18,6 @@
-EOS_ID = 99
@@ -34,6 +33,10 @@ def __init__(self):
+    def decode(self, token_ids):
+        id_to_token = {v: k for k, v in self.vocab.items()}
+        return "".join(id_to_token.get(token_id, "") for token_id in token_ids)
@@ -121,7 +124,6 @@ def test_plain_content(self, parser):
diff -- vllm/reasoning/minimax_m2_reasoning_parser.py
@@ -8,8 +8,8 @@
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-278; `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +2/-51; `vllm/parser/minimax_m2.py` added +180/-0
  - tests: `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +6/-117; `tests/reasoning/test_minimax_m2_reasoning_parser.py` modified +0/-26; `tests/parser/engine/test_minimax_m2.py` added +264/-0
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_minimax_m2.py`, `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45381 - [Model] Add MiniMax M3 support

- 链接: https://github.com/vllm-project/vllm/pull/45381
- 状态/时间: merged / 2026-06-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `tests/kernels/test_minimax_m3_amd_ops.py`, `tests/models/multimodal/processing/test_minimax_m3.py`, `tests/reasoning/test_minimax_m3_reasoning_parser.py` 等 30 个文件；关联提交 `0a1c5034f5e4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 108 个文件，+14746/-323，可读 patch 16807 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add MiniMax M3 support」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`；技术摘要: 覆盖「[Model] Add MiniMax M3 support」；主要实现面是 `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/amd/model.py` added +1216/-0 (1216 lines); hunks: -0,0 +1,1216; symbols: _sparse_attention_layer_ids, _is_moe_layer, _build_rotary_emb, MiniMAXGemmaRMSNorm，涉及 `_sparse_attention_layer_ids, _is_moe_layer, _build_rotary_emb`；`vllm/models/minimax_m3/nvidia/model.py` added +1177/-0 (1177 lines); hunks: -0,0 +1,1177; symbols: _sparse_attention_layer_ids, _is_moe_layer, MiniMAXGemmaRMSNorm, __init__，涉及 `_sparse_attention_layer_ids, _is_moe_layer, MiniMAXGemmaRMSNorm`；`vllm/models/minimax_m3/common/ops/index_topk.py` added +898/-0 (898 lines); hunks: -0,0 +1,898; symbols: _compare_and_swap, _bitonic_merge, _index_block_score_kernel, _topk_index_kernel，涉及 `_compare_and_swap, _bitonic_merge, _index_block_score_kernel`；`vllm/models/minimax_m3/common/vision_tower.py` added +765/-0 (765 lines); hunks: -0,0 +1,765; symbols: MiniMaxVLPatchEmbed, __init__, forward, MiniMaxVLAttention，涉及 `MiniMaxVLPatchEmbed, __init__, forward`。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/amd/model.py` added +1216/-0 (1216 lines); hunks: -0,0 +1,1216; symbols: _sparse_attention_layer_ids, _is_moe_layer, _build_rotary_emb, MiniMAXGemmaRMSNorm
  - `vllm/models/minimax_m3/nvidia/model.py` added +1177/-0 (1177 lines); hunks: -0,0 +1,1177; symbols: _sparse_attention_layer_ids, _is_moe_layer, MiniMAXGemmaRMSNorm, __init__
  - `vllm/models/minimax_m3/common/ops/index_topk.py` added +898/-0 (898 lines); hunks: -0,0 +1,898; symbols: _compare_and_swap, _bitonic_merge, _index_block_score_kernel, _topk_index_kernel
  - `vllm/models/minimax_m3/common/vision_tower.py` added +765/-0 (765 lines); hunks: -0,0 +1,765; symbols: MiniMaxVLPatchEmbed, __init__, forward, MiniMaxVLAttention
  - `vllm/transformers_utils/processors/minimax_m3.py` added +736/-0 (736 lines); hunks: -0,0 +1,736; symbols: round_by_factor, ceil_by_factor, floor_by_factor, _smart_resize_by_long_side
- 关键代码摘录:

```diff
diff -- vllm/models/minimax_m3/amd/model.py
@@ -0,0 +1,1216 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only MiniMax M3 (text backbone) model — AMD ROCm implementation.
+Self-contained per-platform impl (mirrors ``deepseek_v4/amd``). It is identical
+to ``../nvidia/model.py`` except for RMS normalization: FlashInfer's Gemma
+RMSNorm kernels are CUDA-only, so ``MiniMAXGemmaRMSNorm`` here uses a native
diff -- vllm/models/minimax_m3/nvidia/model.py
@@ -0,0 +1,1177 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only MiniMax M3 (text backbone) model.
+The MiniMax-M3-preview config selects a single set of branches:
+    * qk_norm_type == "per_head"
+    * hidden_act == "swigluoai"
diff -- vllm/models/minimax_m3/common/ops/index_topk.py
@@ -0,0 +1,898 @@
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/amd/model.py` added +1216/-0; `vllm/models/minimax_m3/nvidia/model.py` added +1177/-0; `vllm/models/minimax_m3/common/ops/index_topk.py` added +898/-0; `vllm/models/minimax_m3/common/vision_tower.py` added +765/-0; `vllm/transformers_utils/processors/minimax_m3.py` added +736/-0; `vllm/models/minimax_m3/common/ops/sparse_attn.py` added +593/-0
- 验证与风险: diff 自带测试面 `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt`, `tests/kernels/attention/test_minimax_m3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44983 - [Bugfix] Fix minimax_qk_norm_fusion

- 链接: https://github.com/vllm-project/vllm/pull/44983
- 状态/时间: merged / 2026-06-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；关联提交 `dc10e467a985`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+41/-9，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix minimax_qk_norm_fusion」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；技术摘要: 覆盖「[Bugfix] Fix minimax_qk_norm_fusion」；主要实现面是 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +41/-9 (50 lines); hunks: -12,17 +12,34; -42,7 +59,7 @@ def _minimax_qk_norm_fallback(; symbols: _all_reduce_variance, _minimax_qk_norm_fallback, __init__, weight_loader，涉及 `_all_reduce_variance, _minimax_qk_norm_fallback, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +41/-9 (50 lines); hunks: -12,17 +12,34; -42,7 +59,7 @@ def _minimax_qk_norm_fallback(; symbols: _all_reduce_variance, _minimax_qk_norm_fallback, __init__, weight_loader
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py
@@ -12,17 +12,34 @@
+from vllm.logger import init_logger
+logger = init_logger(__name__)
+def _all_reduce_variance(var: torch.Tensor) -> torch.Tensor:
+    """All-reduce a per-token variance tensor across the TP group.
+    Variance is accumulated in fp32 for numerical stability. The FlashInfer
+    fused all-reduce caches a single global workspace keyed to the model's
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` modified +41/-9
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38445 - [PERF]MiniMax-M2 gate kernel

- 链接: https://github.com/vllm-project/vllm/pull/38445
- 状态/时间: merged / 2026-05-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `559d6710bf45`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+716/-23，可读 patch 871 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PERF]MiniMax-M2 gate kernel」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「[PERF]MiniMax-M2 gate kernel」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +4/-4 (8 lines); hunks: -43,10 +43,10; -113,12 +113,12 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +4/-4 (8 lines); hunks: -43,10 +43,10; -113,12 +113,12 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -43,10 +43,10 @@
+from vllm.model_executor.layers.fused_moe.router.gate_linear import GateLinear
-    ReplicatedLinear,
@@ -113,12 +113,12 @@ def __init__(
-        self.gate = ReplicatedLinear(
+        self.gate = GateLinear(
-            quant_config=None,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +4/-4
- 验证与风险: diff 自带测试面 `tests/kernels/test_fp32_router_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43410 - [Kernel] Porting fuse_minimax_qk_norm to manual fusion

- 链接: https://github.com/vllm-project/vllm/pull/43410
- 状态/时间: merged / 2026-05-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/core/test_minimax_reduce_rms.py`, `vllm/model_executor/layers/minimax_rms_norm/__init__.py`, `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`, `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `vllm/model_executor/models/minimax_m2.py`；关联提交 `6e503868caa4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+262/-490，可读 patch 893 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Porting fuse_minimax_qk_norm to manual fusion」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `vllm/model_executor/layers/minimax_rms_norm/__init__.py`, `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「[Kernel] Porting fuse_minimax_qk_norm to manual fusion」；主要实现面是 `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`, `vllm/model_executor/layers/minimax_rms_norm/__init__.py`, `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: _minimax_qk_norm_fallback, _minimax_qk_norm_fusion, _minimax_qk_norm_fusion_fake, MiniMaxText01RMSNormTP，涉及 `_minimax_qk_norm_fallback, _minimax_qk_norm_fusion, _minimax_qk_norm_fusion_fake`；`vllm/model_executor/layers/minimax_rms_norm/__init__.py` added +10/-0 (10 lines); hunks: -0,0 +1,10；`vllm/model_executor/models/minimax_m2.py` modified +4/-3 (7 lines); hunks: -50,7 +50,7; -243,8 +243,9 @@ def forward(; symbols: forward，涉及 `forward`；`vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` renamed +0/-0 (0 lines)。
- 代码 diff 细节:
  - `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: _minimax_qk_norm_fallback, _minimax_qk_norm_fusion, _minimax_qk_norm_fusion_fake, MiniMaxText01RMSNormTP
  - `vllm/model_executor/layers/minimax_rms_norm/__init__.py` added +10/-0 (10 lines); hunks: -0,0 +1,10
  - `vllm/model_executor/models/minimax_m2.py` modified +4/-3 (7 lines); hunks: -50,7 +50,7; -243,8 +243,9 @@ def forward(; symbols: forward
  - `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` renamed +0/-0 (0 lines)
  - `tests/kernels/core/test_minimax_reduce_rms.py` modified +2/-2 (4 lines); hunks: -10,7 +10,7; -59,7 +59,7 @@ def _worker_forward_qk(; symbols: _worker_forward_qk
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py
@@ -0,0 +1,234 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from functools import partial
+import torch
+from torch import nn
+from vllm.distributed.communication_op import tensor_model_parallel_all_reduce
diff -- vllm/model_executor/layers/minimax_rms_norm/__init__.py
@@ -0,0 +1,10 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp import (
+    MiniMaxText01RMSNormTP,
+)
+__all__ = [
diff -- vllm/model_executor/models/minimax_m2.py
@@ -50,7 +50,7 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py` added +234/-0; `vllm/model_executor/layers/minimax_rms_norm/__init__.py` added +10/-0; `vllm/model_executor/models/minimax_m2.py` modified +4/-3; `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py` renamed +0/-0
  - tests: `tests/kernels/core/test_minimax_reduce_rms.py` modified +2/-2
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_minimax_reduce_rms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43025 - [Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser

- 链接: https://github.com/vllm-project/vllm/pull/43025
- 状态/时间: merged / 2026-05-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `42b4f1fdf726`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+123/-106，可读 patch 282 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser」；模型线: MiniMax M2 Series；类别: 模型实现调整；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「[Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +10/-105 (115 lines); hunks: -4,7 +4,6; -25,7 +24,11; symbols: _extract_name, _extract_types_from_schema, _get_param_types_from_config, _parse_single_invoke，涉及 `_extract_name, _extract_types_from_schema, _get_param_types_from_config`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +10/-105 (115 lines); hunks: -4,7 +4,6; -25,7 +24,11; symbols: _extract_name, _extract_types_from_schema, _get_param_types_from_config, _parse_single_invoke
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -4,7 +4,6 @@
-from typing import Any
@@ -25,7 +24,11 @@
-from vllm.tool_parsers.utils import coerce_to_schema_type
+from vllm.tool_parsers.utils import (
+    coerce_to_schema_type,
+    extract_types_from_schema,
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +10/-105
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43006 - [Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser

- 链接: https://github.com/vllm-project/vllm/pull/43006
- 状态/时间: merged / 2026-05-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `57fef4e0bf0b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+247/-77，可读 patch 353 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser」；模型线: MiniMax M2 Series；类别: 模型实现调整；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「[Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-77 (79 lines); hunks: -25,6 +25,7; -146,80 +147,6 @@ def _extract_types_from_schema(self, schema: Any) -> list[s...; symbols: _extract_types_from_schema, _convert_param_value_with_types, _get_param_types_from_config, _parse_single_invoke，涉及 `_extract_types_from_schema, _convert_param_value_with_types, _get_param_types_from_config`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-77 (79 lines); hunks: -25,6 +25,7; -146,80 +147,6 @@ def _extract_types_from_schema(self, schema: Any) -> list[s...; symbols: _extract_types_from_schema, _convert_param_value_with_types, _get_param_types_from_config, _parse_single_invoke
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -25,6 +25,7 @@
+from vllm.tool_parsers.utils import coerce_to_schema_type
@@ -146,80 +147,6 @@ def _extract_types_from_schema(self, schema: Any) -> list[str]:
-    def _convert_param_value_with_types(
-        self, value: str, param_types: list[str]
-    ) -> Any:
-        """
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-77
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39599 - fix(tool-parser): preserve "none"/"nil" strings as valid enum values in minimax_m2

- 链接: https://github.com/vllm-project/vllm/pull/39599
- 状态/时间: merged / 2026-05-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `63cc8a55a97f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+137/-6，可读 patch 166 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(tool-parser): preserve "none"/"nil" strings as valid enum values in minimax_m2」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「fix(tool-parser): preserve "none"/"nil" strings as valid enum values in minimax_m2」；主要实现面是 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +130/-0 (130 lines); hunks: -548,3 +548,133 @@ def test_anyof_nullable_param_object_value(self):; symbols: test_anyof_nullable_param_object_value, TestNoneStringPreservation, test_none_string_preserved_in_enum, test_none_string_preserved_plain_string，涉及 `test_anyof_nullable_param_object_value, TestNoneStringPreservation, test_none_string_preserved_in_enum`；`vllm/tool_parsers/minimax_m2_tool_parser.py` modified +7/-6 (13 lines); hunks: -160,16 +160,13 @@ def _convert_param_value_with_types(; -187,7 +184,11 @@ def _convert_param_value_with_types(; symbols: _convert_param_value_with_types，涉及 `_convert_param_value_with_types`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +130/-0 (130 lines); hunks: -548,3 +548,133 @@ def test_anyof_nullable_param_object_value(self):; symbols: test_anyof_nullable_param_object_value, TestNoneStringPreservation, test_none_string_preserved_in_enum, test_none_string_preserved_plain_string
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +7/-6 (13 lines); hunks: -160,16 +160,13 @@ def _convert_param_value_with_types(; -187,7 +184,11 @@ def _convert_param_value_with_types(; symbols: _convert_param_value_with_types
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_minimax_m2_tool_parser.py
@@ -548,3 +548,133 @@ def test_anyof_nullable_param_object_value(self):
+class TestNoneStringPreservation:
+    """Regression tests for #39567: 'none' as a string must not become None."""
+    def test_none_string_preserved_in_enum(self):
+        """'none' in an enum must stay as the string 'none', not Python None."""
+        tools = [
+            ChatCompletionToolsParam(
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -160,16 +160,13 @@ def _convert_param_value_with_types(
-        # Check if the VALUE itself indicates null (not just if null is allowed)
-        if value.lower() in ("null", "none", "nil"):
-            return None
-        # Priority: integer > number > boolean > object > array > string
+        # Priority: null > integer > number > boolean > object > array > string
+            "null",
```

- 已读文件:
  - tests: `tests/tool_parsers/test_minimax_m2_tool_parser.py` modified +130/-0
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +7/-6
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_minimax_m2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38191 - [Bugfix] Fix k_norm weight sharding in MiniMaxM2Attention when total_num_kv_heads < tp_size

- 链接: https://github.com/vllm-project/vllm/pull/38191
- 状态/时间: merged / 2026-04-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `f8ac0c7cf0e3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+44/-12，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix k_norm weight sharding in MiniMaxM2Attention when total_num_kv_heads < tp_size」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「[Bugfix] Fix k_norm weight sharding in MiniMaxM2Attention when total_num_kv_heads < tp_size」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +16/-3 (19 lines); hunks: -35,6 +35,7; -220,9 +221,21 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +16/-3 (19 lines); hunks: -35,6 +35,7; -220,9 +221,21 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -35,6 +35,7 @@
+    get_tensor_model_parallel_rank,
@@ -220,9 +221,21 @@ def __init__(
-        self.k_norm = MiniMaxText01RMSNormTP(
-            self.head_dim * self.total_num_kv_heads, eps=rms_norm_eps
-        )
+        if self.total_num_kv_heads >= tp_size:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +16/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37045 - [Kernel] Porting the TRTLLM minimax_allreduce_rms kernels

- 链接: https://github.com/vllm-project/vllm/pull/37045
- 状态/时间: merged / 2026-04-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/core/test_minimax_reduce_rms.py`, `vllm/model_executor/models/minimax_m2.py`；关联提交 `ecd1ea13634e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1861/-4，可读 patch 1936 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Porting the TRTLLM minimax_allreduce_rms kernels」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/minimax_m2.py`, `tests/kernels/core/test_minimax_reduce_rms.py`；技术摘要: 覆盖「[Kernel] Porting the TRTLLM minimax_allreduce_rms kernels」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`, `tests/kernels/core/test_minimax_reduce_rms.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +1/-3 (4 lines); hunks: -233,9 +233,7 @@ def forward(; symbols: forward，涉及 `forward`；`tests/kernels/core/test_minimax_reduce_rms.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _worker_forward_qk, test_minimax_reduce_rms_qk，涉及 `_worker_forward_qk, test_minimax_reduce_rms_qk`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +1/-3 (4 lines); hunks: -233,9 +233,7 @@ def forward(; symbols: forward
  - `tests/kernels/core/test_minimax_reduce_rms.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _worker_forward_qk, test_minimax_reduce_rms_qk
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -233,9 +233,7 @@ def forward(
-        q, k = MiniMaxText01RMSNormTP.forward_qk(
-            self.q_norm, self.k_norm, q.contiguous(), k.contiguous()
-        )
+        q, k = MiniMaxText01RMSNormTP.forward_qk(self.q_norm, self.k_norm, q, k)
diff -- tests/kernels/core/test_minimax_reduce_rms.py
@@ -0,0 +1,152 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Tests for MiniMax QK RMS-norm: NCCL reference vs Lamport fused kernel."""
+import pytest
+import torch
+import torch.nn as nn
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +1/-3
  - tests: `tests/kernels/core/test_minimax_reduce_rms.py` added +152/-0
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_minimax_reduce_rms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37512 - MiniMax-M2: add Eagle3 speculative decoding support

- 链接: https://github.com/vllm-project/vllm/pull/37512
- 状态/时间: merged / 2026-04-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `f6983f01de2b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+24/-5，可读 patch 99 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「MiniMax-M2: add Eagle3 speculative decoding support」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「MiniMax-M2: add Eagle3 speculative decoding support」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +16/-5 (21 lines); hunks: -24,6 +24,7; -59,7 +60,7; symbols: forward, MiniMaxM2Model, __init__，涉及 `forward, MiniMaxM2Model, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +16/-5 (21 lines); hunks: -24,6 +24,7; -59,7 +60,7; symbols: forward, MiniMaxM2Model, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -24,6 +24,7 @@
+from itertools import islice
@@ -59,7 +60,7 @@
-from .interfaces import SupportsLoRA, SupportsPP
+from .interfaces import EagleModelMixin, SupportsEagle3, SupportsLoRA, SupportsPP
@@ -313,7 +314,7 @@ def forward(
-class MiniMaxM2Model(nn.Module):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +16/-5
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36965 - [Model][Quantization] Add GGUF support for MiniMax-M2.1

- 链接: https://github.com/vllm-project/vllm/pull/36965
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `63babd17f1b1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+137/-10，可读 patch 238 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][Quantization] Add GGUF support for MiniMax-M2.1」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「[Model][Quantization] Add GGUF support for MiniMax-M2.1」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +5/-2 (7 lines); hunks: -331,7 +331,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; -518,7 +518,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +5/-2 (7 lines); hunks: -331,7 +331,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; -518,7 +518,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -331,7 +331,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                quant_config=None,
+                quant_config=quant_config,
@@ -518,7 +518,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                config.vocab_size, config.hidden_size, quant_config=None
+                config.vocab_size,
+                config.hidden_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `vllm/config/model.py`, `vllm/model_executor/layers/quantization/gguf.py`, `vllm/model_executor/model_loader/gguf_loader.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37214 - Fix minimax m2.5 nvfp4 kv scales weight loading

- 链接: https://github.com/vllm-project/vllm/pull/37214
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `74056039b776`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-0，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix minimax m2.5 nvfp4 kv scales weight loading」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「Fix minimax m2.5 nvfp4 kv scales weight loading」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +11/-0 (11 lines); hunks: -439,6 +439,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +11/-0 (11 lines); hunks: -439,6 +439,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -439,6 +439,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                # Remap qkv_proj.[kv]_scale to attn.[kv]_scale
+                if name.endswith((".k_scale", ".v_scale")):
+                    remapped_name = maybe_remap_kv_scale_name(name, params_dict)
+                    if remapped_name is not None and remapped_name in params_dict:
+                        param = params_dict[remapped_name]
+                        weight_loader = getattr(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +11/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35895 - [Bugfix] Fix minimax_m2 tool parser when stream interval > 1

- 链接: https://github.com/vllm-project/vllm/pull/35895
- 状态/时间: merged / 2026-03-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `8647c6cf510b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+534/-532，可读 patch 1119 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix minimax_m2 tool parser when stream interval > 1」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_use/test_minimax_m2_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Fix minimax_m2 tool parser when stream interval > 1」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_use/test_minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +90/-413 (503 lines); hunks: -37,37 +37,10 @@ def __init__(self, tokenizer: TokenizerLike):; -103,46 +76,15 @@ def _generate_tool_call_id(self) -> str:; symbols: __init__, type, _generate_tool_call_id, _reset_streaming_state，涉及 `__init__, type, _generate_tool_call_id`；`tests/tool_parsers/test_minimax_m2_tool_parser.py` added +444/-0 (444 lines); hunks: -0,0 +1,444; symbols: FakeTokenizer, __init__, get_vocab, parser，涉及 `FakeTokenizer, __init__, get_vocab`；`tests/tool_use/test_minimax_m2_tool_parser.py` removed +0/-119 (119 lines); hunks: -1,119 +0,0; symbols: FakeTokenizer, __init__, get_vocab, minimax_m2_tool_parser，涉及 `FakeTokenizer, __init__, get_vocab`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +90/-413 (503 lines); hunks: -37,37 +37,10 @@ def __init__(self, tokenizer: TokenizerLike):; -103,46 +76,15 @@ def _generate_tool_call_id(self) -> str:; symbols: __init__, type, _generate_tool_call_id, _reset_streaming_state
  - `tests/tool_parsers/test_minimax_m2_tool_parser.py` added +444/-0 (444 lines); hunks: -0,0 +1,444; symbols: FakeTokenizer, __init__, get_vocab, parser
  - `tests/tool_use/test_minimax_m2_tool_parser.py` removed +0/-119 (119 lines); hunks: -1,119 +0,0; symbols: FakeTokenizer, __init__, get_vocab, minimax_m2_tool_parser
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -37,37 +37,10 @@ def __init__(self, tokenizer: TokenizerLike):
-        self.invoke_start_prefix: str = "<invoke name="
-        self.invoke_end_token: str = "</invoke>"
-        self.parameter_prefix: str = "<parameter name="
-        self.parameter_end_token: str = "</parameter>"
-        # Streaming state variables
-        self.current_tool_name_sent: bool = False
diff -- tests/tool_parsers/test_minimax_m2_tool_parser.py
@@ -0,0 +1,444 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import json
+import pytest
+from vllm.tool_parsers.minimax_m2_tool_parser import (
+    MinimaxM2ToolParser,
diff -- tests/tool_use/test_minimax_m2_tool_parser.py
@@ -1,119 +0,0 @@
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +90/-413
  - tests: `tests/tool_parsers/test_minimax_m2_tool_parser.py` added +444/-0; `tests/tool_use/test_minimax_m2_tool_parser.py` removed +0/-119
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_use/test_minimax_m2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35352 - [Bug] Fix missing tag after tool call in MiniMax 2.1

- 链接: https://github.com/vllm-project/vllm/pull/35352
- 状态/时间: merged / 2026-02-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/reasoning/minimax_m2_reasoning_parser.py`；关联提交 `7fea7250a46c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-1，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] Fix missing tag after tool call in MiniMax 2.1」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/reasoning/minimax_m2_reasoning_parser.py`；技术摘要: 覆盖「[Bug] Fix missing tag after tool call in MiniMax 2.1」；主要实现面是 `vllm/reasoning/minimax_m2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +6/-1 (7 lines); hunks: -87,10 +87,15 @@ class MiniMaxM2AppendThinkReasoningParser(ReasoningParser):; symbols: MiniMaxM2AppendThinkReasoningParser, __init__, is_reasoning_end, extract_content_ids，涉及 `MiniMaxM2AppendThinkReasoningParser, __init__, is_reasoning_end`。
- 代码 diff 细节:
  - `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +6/-1 (7 lines); hunks: -87,10 +87,15 @@ class MiniMaxM2AppendThinkReasoningParser(ReasoningParser):; symbols: MiniMaxM2AppendThinkReasoningParser, __init__, is_reasoning_end, extract_content_ids
- 关键代码摘录:

```diff
diff -- vllm/reasoning/minimax_m2_reasoning_parser.py
@@ -87,10 +87,15 @@ class MiniMaxM2AppendThinkReasoningParser(ReasoningParser):
+        self.start_token_id = self.vocab.get("<think>")
-        return any(input_id == end_token_id for input_id in reversed(input_ids))
+        start_token_id = self.start_token_id
+        for input_id in reversed(input_ids):
+            if input_id in (end_token_id, start_token_id):
+                return input_id == end_token_id
```

- 已读文件:
  - runtime: `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `vllm/reasoning/minimax_m2_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #32763 - feat: Complete LoRA support for MiniMaxM2 Fixes #32736

- 链接: https://github.com/vllm-project/vllm/pull/32763
- 状态/时间: merged / 2026-01-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `bc0d291bfebf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-3，可读 patch 35 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: Complete LoRA support for MiniMaxM2 Fixes #32736」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「feat: Complete LoRA support for MiniMaxM2 Fixes #32736」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +10/-2 (12 lines); hunks: -59,7 +59,7; -487,7 +487,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiniMaxM2ForCausalLM, __init__，涉及 `load_weights, MiniMaxM2ForCausalLM, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +10/-2 (12 lines); hunks: -59,7 +59,7; -487,7 +487,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiniMaxM2ForCausalLM, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -59,7 +59,7 @@
-from .interfaces import SupportsPP
+from .interfaces import SupportsLoRA, SupportsPP
@@ -487,7 +487,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-class MiniMaxM2ForCausalLM(nn.Module, SupportsPP):
+class MiniMaxM2ForCausalLM(nn.Module, SupportsLoRA, SupportsPP):
+    packed_modules_mapping = {
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #32342 - Fix optional parameter parsing in MiniMax M2 tool parser #32278

- 链接: https://github.com/vllm-project/vllm/pull/32342
- 状态/时间: merged / 2026-01-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `19b251fe3d26`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-5，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix optional parameter parsing in MiniMax M2 tool parser #32278」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「Fix optional parameter parsing in MiniMax M2 tool parser #32278」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-5 (7 lines); hunks: -217,16 +217,13 @@ def _convert_param_value_with_types(; symbols: _convert_param_value_with_types，涉及 `_convert_param_value_with_types`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-5 (7 lines); hunks: -217,16 +217,13 @@ def _convert_param_value_with_types(; symbols: _convert_param_value_with_types
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -217,16 +217,13 @@ def _convert_param_value_with_types(
-        if value.lower() == "null":
+        # Check if the VALUE itself indicates null (not just if null is allowed)
+        if value.lower() in ("null", "none", "nil"):
-        # Try null first if it's in the list
-        if "null" in normalized_types or value.lower() in ("null", "none", "nil"):
-            return None
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +2/-5
- 验证与风险: runtime 路径改动集中在 `vllm/tool_parsers/minimax_m2_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31493 - Optimize QKNorm for MiniMax-M2/M2.1

- 链接: https://github.com/vllm-project/vllm/pull/31493
- 状态/时间: merged / 2025-12-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `5bc664110f12`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+25/-2，可读 patch 41 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Optimize QKNorm for MiniMax-M2/M2.1」；模型线: MiniMax M2 Series；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「Optimize QKNorm for MiniMax-M2/M2.1」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +3/-2 (5 lines); hunks: -234,8 +234,9 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +3/-2 (5 lines); hunks: -234,8 +234,9 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -234,8 +234,9 @@ def forward(
-        q = self.q_norm(q)
-        k = self.k_norm(k)
+        q, k = MiniMaxText01RMSNormTP.forward_qk(
+            self.q_norm, self.k_norm, q.contiguous(), k.contiguous()
+        )
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31083 - Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs

- 链接: https://github.com/vllm-project/vllm/pull/31083
- 状态/时间: merged / 2025-12-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `c02a2705f9ce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+167/-48，可读 patch 257 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs」；模型线: MiniMax M2 Series；类别: 文档/测试/CI；主要 diff: `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs」；主要实现面是 `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +166/-47 (213 lines); hunks: -138,37 +138,167 @@ def _extract_name(self, name_str: str) -> str:; -207,17 +337,11 @@ def _parse_single_invoke(; symbols: _extract_name, _convert_param_value, _extract_types_from_schema, _convert_param_value_with_types，涉及 `_extract_name, _convert_param_value, _extract_types_from_schema`。
- 代码 diff 细节:
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +166/-47 (213 lines); hunks: -138,37 +138,167 @@ def _extract_name(self, name_str: str) -> str:; -207,17 +337,11 @@ def _parse_single_invoke(; symbols: _extract_name, _convert_param_value, _extract_types_from_schema, _convert_param_value_with_types
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -138,37 +138,167 @@ def _extract_name(self, name_str: str) -> str:
-        """Convert parameter value to the correct type."""
+        """Convert parameter value to the correct type (legacy single-type version)."""
+        return self._convert_param_value_with_types(value, [param_type])
+    def _extract_types_from_schema(self, schema: Any) -> list[str]:
+        """
+        Extract all possible types from a JSON schema definition.
```

- 已读文件:
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +166/-47
- 验证与风险: runtime 路径改动集中在 `vllm/tool_parsers/minimax_m2_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30555 - [Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction

- 链接: https://github.com/vllm-project/vllm/pull/30555
- 状态/时间: merged / 2025-12-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/minimax_m2_tool_parser.py`；关联提交 `20fda431515d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+137/-4，可读 patch 186 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/tool_use/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`；技术摘要: 覆盖「[Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction」；主要实现面是 `tests/tool_use/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_use/test_minimax_m2_tool_parser.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: FakeTokenizer, __init__, get_vocab, minimax_m2_tool_parser，涉及 `FakeTokenizer, __init__, get_vocab`；`vllm/tool_parsers/minimax_m2_tool_parser.py` modified +18/-4 (22 lines); hunks: -122,6 +122,8 @@ def _reset_streaming_state(self):; -421,9 +423,12 @@ def extract_tool_calls_streaming(; symbols: _reset_streaming_state, _extract_name, extract_tool_calls_streaming，涉及 `_reset_streaming_state, _extract_name, extract_tool_calls_streaming`。
- 代码 diff 细节:
  - `tests/tool_use/test_minimax_m2_tool_parser.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: FakeTokenizer, __init__, get_vocab, minimax_m2_tool_parser
  - `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +18/-4 (22 lines); hunks: -122,6 +122,8 @@ def _reset_streaming_state(self):; -421,9 +423,12 @@ def extract_tool_calls_streaming(; symbols: _reset_streaming_state, _extract_name, extract_tool_calls_streaming
- 关键代码摘录:

```diff
diff -- tests/tool_use/test_minimax_m2_tool_parser.py
@@ -0,0 +1,119 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import json
+import pytest
+from vllm.tool_parsers.minimax_m2_tool_parser import (
+    MinimaxM2ToolParser,
diff -- vllm/tool_parsers/minimax_m2_tool_parser.py
@@ -122,6 +122,8 @@ def _reset_streaming_state(self):
+        # Reset streamed args tracking
+        self.streamed_args_for_tool.clear()
@@ -421,9 +423,12 @@ def extract_tool_calls_streaming(
-                                "arguments": "{}",  # Placeholder, will be updated later
+                                "arguments": {},  # Placeholder, will be updated later
+                        # Initialize streamed_args_for_tool for this tool call
```

- 已读文件:
  - tests: `tests/tool_use/test_minimax_m2_tool_parser.py` added +119/-0
  - runtime: `vllm/tool_parsers/minimax_m2_tool_parser.py` modified +18/-4
- 验证与风险: diff 自带测试面 `tests/tool_use/test_minimax_m2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29882 - [bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content.

- 链接: https://github.com/vllm-project/vllm/pull/29882
- 状态/时间: merged / 2025-12-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`；关联提交 `6299628d326f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+468/-0，可读 patch 484 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content.」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`；技术摘要: 覆盖「[bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content.」；主要实现面是 `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_minimax_m2_reasoning_parser.py` added +230/-0 (230 lines); hunks: -0,0 +1,230; symbols: minimax_m2_tokenizer, test_reasoning，涉及 `minimax_m2_tokenizer, test_reasoning`；`tests/reasoning/test_minimax_m2_append_reasoning_parser.py` added +195/-0 (195 lines); hunks: -0,0 +1,195; symbols: minimax_m2_tokenizer, test_reasoning，涉及 `minimax_m2_tokenizer, test_reasoning`；`vllm/reasoning/minimax_m2_reasoning_parser.py` modified +43/-0 (43 lines); hunks: -19,6 +19,10; -31,6 +35,45 @@ def end_token(self) -> str:; symbols: MiniMaxM2ReasoningParser, end_token, extract_reasoning_streaming, MiniMaxM2AppendThinkReasoningParser，涉及 `MiniMaxM2ReasoningParser, end_token, extract_reasoning_streaming`。
- 代码 diff 细节:
  - `tests/reasoning/test_minimax_m2_reasoning_parser.py` added +230/-0 (230 lines); hunks: -0,0 +1,230; symbols: minimax_m2_tokenizer, test_reasoning
  - `tests/reasoning/test_minimax_m2_append_reasoning_parser.py` added +195/-0 (195 lines); hunks: -0,0 +1,195; symbols: minimax_m2_tokenizer, test_reasoning
  - `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +43/-0 (43 lines); hunks: -19,6 +19,10; -31,6 +35,45 @@ def end_token(self) -> str:; symbols: MiniMaxM2ReasoningParser, end_token, extract_reasoning_streaming, MiniMaxM2AppendThinkReasoningParser
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_minimax_m2_reasoning_parser.py
@@ -0,0 +1,230 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from tests.reasoning.utils import run_reasoning_extraction
+from vllm.reasoning import ReasoningParser, ReasoningParserManager
diff -- tests/reasoning/test_minimax_m2_append_reasoning_parser.py
@@ -0,0 +1,195 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from tests.reasoning.utils import run_reasoning_extraction
+from vllm.reasoning import ReasoningParser, ReasoningParserManager
diff -- vllm/reasoning/minimax_m2_reasoning_parser.py
@@ -19,6 +19,10 @@
```

- 已读文件:
  - tests: `tests/reasoning/test_minimax_m2_reasoning_parser.py` added +230/-0; `tests/reasoning/test_minimax_m2_append_reasoning_parser.py` added +195/-0
  - runtime: `vllm/reasoning/minimax_m2_reasoning_parser.py` modified +43/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30384 - [BugFix] Fix minimax m2 model rotary_dim

- 链接: https://github.com/vllm-project/vllm/pull/30384
- 状态/时间: merged / 2025-12-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `d017bceb08ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Fix minimax m2 model rotary_dim」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「[BugFix] Fix minimax m2 model rotary_dim」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +1/-1 (2 lines); hunks: -201,7 +201,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +1/-1 (2 lines); hunks: -201,7 +201,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -201,7 +201,7 @@ def __init__(
-            rotary_dim=rotary_dim,
+            rotary_dim=self.head_dim,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27627 - Fix MiniMax-M2 rmsnorm precision and remove useless code

- 链接: https://github.com/vllm-project/vllm/pull/27627
- 状态/时间: merged / 2025-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `d6704dd099b7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+1/-19，可读 patch 41 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix MiniMax-M2 rmsnorm precision and remove useless code」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「Fix MiniMax-M2 rmsnorm precision and remove useless code」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +0/-18 (18 lines); hunks: -263,23 +263,6 @@ def __init__(; -288,7 +271,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +0/-18 (18 lines); hunks: -263,23 +263,6 @@ def __init__(; -288,7 +271,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -263,23 +263,6 @@ def __init__(
-        # TODO: support MTP
-        attn_window_size = getattr(config, "attn_window_size", None)
-        if attn_window_size is not None:
-            if isinstance(attn_window_size, list):
-                attn_window_size = attn_window_size[layer_idx]
-            elif isinstance(attn_window_size, int):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +0/-18
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27537 - Fix MiniMax-M2 copyright

- 链接: https://github.com/vllm-project/vllm/pull/27537
- 状态/时间: merged / 2025-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`；关联提交 `5980604c44d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-3，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix MiniMax-M2 copyright」；模型线: MiniMax M2 Series；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/minimax_m2.py`；技术摘要: 覆盖「Fix MiniMax-M2 copyright」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` modified +2/-3 (5 lines); hunks: -1,10 +1,9。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` modified +2/-3 (5 lines); hunks: -1,10 +1,9
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -1,10 +1,9 @@
-# Adapted from
-# https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/models/llama/modeling_llama.py
+# Copyright 2025 The MiniMax AI team.
-# Copyright 2023 DeepSeek-AI and the HuggingFace Inc. team. All rights reserved.
+# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` modified +2/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/minimax_m2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27535 - [Model][MiniMax-M2] Support MiniMax-M2 Model

- 链接: https://github.com/vllm-project/vllm/pull/27535
- 状态/时间: merged / 2025-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/minimax_m2.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`；关联提交 `720af6ab7911`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+1306/-0，可读 patch 1347 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][MiniMax-M2] Support MiniMax-M2 Model」；模型线: MiniMax M2 Series；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/minimax_m2.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`；技术摘要: 覆盖「[Model][MiniMax-M2] Support MiniMax-M2 Model」；主要实现面是 `vllm/model_executor/models/minimax_m2.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/minimax_m2.py` added +585/-0 (585 lines); hunks: -0,0 +1,585; symbols: MiniMaxM2MoE, __init__, ebias_weight_loader, forward，涉及 `MiniMaxM2MoE, __init__, ebias_weight_loader`；`vllm/reasoning/minimax_m2_reasoning_parser.py` added +69/-0 (69 lines); hunks: -0,0 +1,69; symbols: MiniMaxM2ReasoningParser, start_token, end_token, MiniMaxM2AppendThinkReasoningParser，涉及 `MiniMaxM2ReasoningParser, start_token, end_token`。
- 代码 diff 细节:
  - `vllm/model_executor/models/minimax_m2.py` added +585/-0 (585 lines); hunks: -0,0 +1,585; symbols: MiniMaxM2MoE, __init__, ebias_weight_loader, forward
  - `vllm/reasoning/minimax_m2_reasoning_parser.py` added +69/-0 (69 lines); hunks: -0,0 +1,69; symbols: MiniMaxM2ReasoningParser, start_token, end_token, MiniMaxM2AppendThinkReasoningParser
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/minimax_m2.py
@@ -0,0 +1,585 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from
+# https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/models/llama/modeling_llama.py
+# Copyright 2023 The vLLM team.
+# Copyright 2023 DeepSeek-AI and the HuggingFace Inc. team. All rights reserved.
diff -- vllm/reasoning/minimax_m2_reasoning_parser.py
@@ -0,0 +1,69 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Sequence
+from vllm.entrypoints.openai.protocol import (
+    ChatCompletionRequest,
+    DeltaMessage,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/minimax_m2.py` added +585/-0; `vllm/reasoning/minimax_m2_reasoning_parser.py` added +69/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
