# vllm Kimi K2/K2.5/Linear/VL 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `benchmarks/kernels/benchmark_kimi_k3_amd_fp8_fusions.py` | [#59069](https://github.com/vllm-project/vllm/pull/59069) |
| `benchmarks/kernels/benchmark_kimi_k3_attn_res.py` | [#54261](https://github.com/vllm-project/vllm/pull/54261) |
| `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` | [#50654](https://github.com/vllm-project/vllm/pull/50654), [#53396](https://github.com/vllm-project/vllm/pull/53396) |
| `benchmarks/kernels/benchmark_kimi_k3_kda_projection.py` | [#54697](https://github.com/vllm-project/vllm/pull/54697) |
| `benchmarks/kernels/benchmark_kimi_k3_latent_moe_tail.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089) |
| `benchmarks/kernels/benchmark_kimi_k3_sp_collectives.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089) |
| `tests/distributed/test_kimi_linear_context_parallel.py` | [#50484](https://github.com/vllm-project/vllm/pull/50484), [#50493](https://github.com/vllm-project/vllm/pull/50493) |
| `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-AITER-TP4.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml` | [#54817](https://github.com/vllm-project/vllm/pull/54817) |
| `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#51772](https://github.com/vllm-project/vllm/pull/51772), [#54896](https://github.com/vllm-project/vllm/pull/54896), [#61527](https://github.com/vllm-project/vllm/pull/61527) |
| `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py` | [#50484](https://github.com/vllm-project/vllm/pull/50484) |
| `tests/models/kimi_k3/__init__.py` | [#51253](https://github.com/vllm-project/vllm/pull/51253) |
| `tests/models/kimi_k3/amd_specialized_decode/__init__.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683) |
| `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683), [#64029](https://github.com/vllm-project/vllm/pull/64029) |
| `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683), [#64029](https://github.com/vllm-project/vllm/pull/64029) |
| `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683), [#61435](https://github.com/vllm-project/vllm/pull/61435), [#63031](https://github.com/vllm-project/vllm/pull/63031), [#64029](https://github.com/vllm-project/vllm/pull/64029) |
| `tests/models/kimi_k3/test_amd_attn_res.py` | [#50090](https://github.com/vllm-project/vllm/pull/50090), [#50593](https://github.com/vllm-project/vllm/pull/50593), [#59069](https://github.com/vllm-project/vllm/pull/59069), [#60717](https://github.com/vllm-project/vllm/pull/60717) |
| `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py` | [#59824](https://github.com/vllm-project/vllm/pull/59824) |
| `tests/models/kimi_k3/test_amd_kda_checkpoint.py` | [#58344](https://github.com/vllm-project/vllm/pull/58344), [#59552](https://github.com/vllm-project/vllm/pull/59552), [#63297](https://github.com/vllm-project/vllm/pull/63297), [#64619](https://github.com/vllm-project/vllm/pull/64619) |
| `tests/models/kimi_k3/test_amd_kda_chunk.py` | [#52606](https://github.com/vllm-project/vllm/pull/52606), [#53294](https://github.com/vllm-project/vllm/pull/53294), [#54038](https://github.com/vllm-project/vllm/pull/54038), [#58344](https://github.com/vllm-project/vllm/pull/58344), [#58743](https://github.com/vllm-project/vllm/pull/58743), [#59552](https://github.com/vllm-project/vllm/pull/59552), [#63297](https://github.com/vllm-project/vllm/pull/63297) |
| `tests/models/kimi_k3/test_amd_kda_decode.py` | [#50654](https://github.com/vllm-project/vllm/pull/50654), [#57392](https://github.com/vllm-project/vllm/pull/57392), [#58743](https://github.com/vllm-project/vllm/pull/58743), [#61207](https://github.com/vllm-project/vllm/pull/61207), [#64886](https://github.com/vllm-project/vllm/pull/64886) |
| `tests/models/kimi_k3/test_amd_kda_direct_return.py` | [#50592](https://github.com/vllm-project/vllm/pull/50592) |
| `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py` | [#63342](https://github.com/vllm-project/vllm/pull/63342) |
| `tests/models/kimi_k3/test_amd_latent_moe_runner.py` | [#51253](https://github.com/vllm-project/vllm/pull/51253), [#54956](https://github.com/vllm-project/vllm/pull/54956), [#59591](https://github.com/vllm-project/vllm/pull/59591) |
| `tests/models/kimi_k3/test_amd_mla_direct_return.py` | [#50592](https://github.com/vllm-project/vllm/pull/50592), [#59069](https://github.com/vllm-project/vllm/pull/59069), [#59634](https://github.com/vllm-project/vllm/pull/59634), [#60110](https://github.com/vllm-project/vllm/pull/60110), [#63409](https://github.com/vllm-project/vllm/pull/63409) |
| `tests/models/kimi_k3/test_amd_qb_uk_fold.py` | [#60110](https://github.com/vllm-project/vllm/pull/60110), [#64158](https://github.com/vllm-project/vllm/pull/64158) |
| `tests/models/kimi_k3/test_attn_res.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50090](https://github.com/vllm-project/vllm/pull/50090), [#54261](https://github.com/vllm-project/vllm/pull/54261), [#58012](https://github.com/vllm-project/vllm/pull/58012) |
| `tests/models/kimi_k3/test_aux_attn_res_stream.py` | [#50487](https://github.com/vllm-project/vllm/pull/50487) |
| `tests/models/kimi_k3/test_eagle3.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50487](https://github.com/vllm-project/vllm/pull/50487), [#52171](https://github.com/vllm-project/vllm/pull/52171), [#54482](https://github.com/vllm-project/vllm/pull/54482) |
| `tests/models/kimi_k3/test_gfx942_int4.py` | [#51274](https://github.com/vllm-project/vllm/pull/51274) |
| `tests/models/kimi_k3/test_kda.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#51682](https://github.com/vllm-project/vllm/pull/51682), [#51809](https://github.com/vllm-project/vllm/pull/51809), [#53396](https://github.com/vllm-project/vllm/pull/53396), [#53581](https://github.com/vllm-project/vllm/pull/53581), [#54255](https://github.com/vllm-project/vllm/pull/54255), [#54859](https://github.com/vllm-project/vllm/pull/54859), [#56159](https://github.com/vllm-project/vllm/pull/56159), [#58045](https://github.com/vllm-project/vllm/pull/58045), [#63045](https://github.com/vllm-project/vllm/pull/63045) |
| `tests/models/kimi_k3/test_kda_metadata.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#51483](https://github.com/vllm-project/vllm/pull/51483), [#53614](https://github.com/vllm-project/vllm/pull/53614), [#53766](https://github.com/vllm-project/vllm/pull/53766), [#54781](https://github.com/vllm-project/vllm/pull/54781), [#56159](https://github.com/vllm-project/vllm/pull/56159), [#58045](https://github.com/vllm-project/vllm/pull/58045), [#63045](https://github.com/vllm-project/vllm/pull/63045) |
| `tests/models/kimi_k3/test_kv_balanced_mla.py` | [#63638](https://github.com/vllm-project/vllm/pull/63638) |
| `tests/models/kimi_k3/test_latent_moe_tail.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#53327](https://github.com/vllm-project/vllm/pull/53327), [#54168](https://github.com/vllm-project/vllm/pull/54168), [#62980](https://github.com/vllm-project/vllm/pull/62980), [#64583](https://github.com/vllm-project/vllm/pull/64583) |
| `tests/models/kimi_k3/test_mla_prefill_context.py` | [#51772](https://github.com/vllm-project/vllm/pull/51772), [#56881](https://github.com/vllm-project/vllm/pull/56881) |
| `tests/models/kimi_k3/test_nvidia_kda_direct_return.py` | [#50592](https://github.com/vllm-project/vllm/pull/50592) |
| `tests/models/kimi_k3/test_prefix_cache.py` | [#59229](https://github.com/vllm-project/vllm/pull/59229), [#62141](https://github.com/vllm-project/vllm/pull/62141), [#63449](https://github.com/vllm-project/vllm/pull/63449) |
| `tests/models/kimi_k3/test_recoverssm_kernels.py` | [#63045](https://github.com/vllm-project/vllm/pull/63045) |
| `tests/models/kimi_k3/test_sequence_parallel.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50656](https://github.com/vllm-project/vllm/pull/50656), [#50912](https://github.com/vllm-project/vllm/pull/50912), [#52079](https://github.com/vllm-project/vllm/pull/52079), [#56875](https://github.com/vllm-project/vllm/pull/56875) |
| `tests/models/multimodal/processing/test_kimi_k3.py` | [#59278](https://github.com/vllm-project/vllm/pull/59278) |
| `tests/reasoning/test_kimi_k2_reasoning_parser.py` | [#37438](https://github.com/vllm-project/vllm/pull/37438), [#41068](https://github.com/vllm-project/vllm/pull/41068), [#46610](https://github.com/vllm-project/vllm/pull/46610) |
| `tests/reasoning/test_kimi_k3_reasoning_parser.py` | [#50093](https://github.com/vllm-project/vllm/pull/50093), [#50886](https://github.com/vllm-project/vllm/pull/50886), [#58372](https://github.com/vllm-project/vllm/pull/58372), [#62507](https://github.com/vllm-project/vllm/pull/62507) |
| `tests/renderers/test_kimi_k3.py` | [#50093](https://github.com/vllm-project/vllm/pull/50093) |
| `tests/tool_parsers/test_kimi_k2_tool_parser.py` | [#31207](https://github.com/vllm-project/vllm/pull/31207), [#38579](https://github.com/vllm-project/vllm/pull/38579) |
| `tests/tool_parsers/test_kimi_k3_named_tool_choice.py` | [#50093](https://github.com/vllm-project/vllm/pull/50093) |
| `tests/tool_use/test_kimi_k3_tool_parser.py` | [#50093](https://github.com/vllm-project/vllm/pull/50093), [#50420](https://github.com/vllm-project/vllm/pull/50420), [#62203](https://github.com/vllm-project/vllm/pull/62203), [#62507](https://github.com/vllm-project/vllm/pull/62507) |
| `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` | [#50000](https://github.com/vllm-project/vllm/pull/50000), [#50592](https://github.com/vllm-project/vllm/pull/50592), [#51862](https://github.com/vllm-project/vllm/pull/51862) |
| `vllm/model_executor/models/kimi_audio.py` | [#36127](https://github.com/vllm-project/vllm/pull/36127), [#36903](https://github.com/vllm-project/vllm/pull/36903) |
| `vllm/model_executor/models/kimi_k25.py` | [#33131](https://github.com/vllm-project/vllm/pull/33131), [#33320](https://github.com/vllm-project/vllm/pull/33320), [#33346](https://github.com/vllm-project/vllm/pull/33346), [#33562](https://github.com/vllm-project/vllm/pull/33562), [#33876](https://github.com/vllm-project/vllm/pull/33876), [#34427](https://github.com/vllm-project/vllm/pull/34427), [#34501](https://github.com/vllm-project/vllm/pull/34501), [#36192](https://github.com/vllm-project/vllm/pull/36192), [#36361](https://github.com/vllm-project/vllm/pull/36361), [#37693](https://github.com/vllm-project/vllm/pull/37693), [#39344](https://github.com/vllm-project/vllm/pull/39344), [#42869](https://github.com/vllm-project/vllm/pull/42869), ... (16 total) |
| `vllm/model_executor/models/kimi_k25_vit.py` | [#33131](https://github.com/vllm-project/vllm/pull/33131), [#33346](https://github.com/vllm-project/vllm/pull/33346), [#34501](https://github.com/vllm-project/vllm/pull/34501), [#42081](https://github.com/vllm-project/vllm/pull/42081), [#44493](https://github.com/vllm-project/vllm/pull/44493), [#50000](https://github.com/vllm-project/vllm/pull/50000), [#50400](https://github.com/vllm-project/vllm/pull/50400), [#51196](https://github.com/vllm-project/vllm/pull/51196), [#53011](https://github.com/vllm-project/vllm/pull/53011), [#58527](https://github.com/vllm-project/vllm/pull/58527), [#58651](https://github.com/vllm-project/vllm/pull/58651), [#59278](https://github.com/vllm-project/vllm/pull/59278) |
| `vllm/model_executor/models/kimi_vl.py` | [#16387](https://github.com/vllm-project/vllm/pull/16387), [#16833](https://github.com/vllm-project/vllm/pull/16833), [#17156](https://github.com/vllm-project/vllm/pull/17156), [#21769](https://github.com/vllm-project/vllm/pull/21769), [#23114](https://github.com/vllm-project/vllm/pull/23114), [#23817](https://github.com/vllm-project/vllm/pull/23817), [#31738](https://github.com/vllm-project/vllm/pull/31738), [#41992](https://github.com/vllm-project/vllm/pull/41992) |
| `vllm/model_executor/models/moonvit.py` | [#16387](https://github.com/vllm-project/vllm/pull/16387), [#23817](https://github.com/vllm-project/vllm/pull/23817), [#29309](https://github.com/vllm-project/vllm/pull/29309), [#31738](https://github.com/vllm-project/vllm/pull/31738), [#41992](https://github.com/vllm-project/vllm/pull/41992) |
| `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` | [#50000](https://github.com/vllm-project/vllm/pull/50000), [#59257](https://github.com/vllm-project/vllm/pull/59257), [#59552](https://github.com/vllm-project/vllm/pull/59552) |
| `vllm/models/kimi_k3/__init__.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50131](https://github.com/vllm-project/vllm/pull/50131), [#51529](https://github.com/vllm-project/vllm/pull/51529), [#63531](https://github.com/vllm-project/vllm/pull/63531) |
| `vllm/models/kimi_k3/amd/__init__.py` | [#50090](https://github.com/vllm-project/vllm/pull/50090) |
| `vllm/models/kimi_k3/amd/kda.py` | [#50592](https://github.com/vllm-project/vllm/pull/50592), [#50649](https://github.com/vllm-project/vllm/pull/50649), [#50654](https://github.com/vllm-project/vllm/pull/50654), [#51862](https://github.com/vllm-project/vllm/pull/51862), [#52606](https://github.com/vllm-project/vllm/pull/52606), [#53294](https://github.com/vllm-project/vllm/pull/53294), [#53581](https://github.com/vllm-project/vllm/pull/53581), [#54038](https://github.com/vllm-project/vllm/pull/54038), [#57392](https://github.com/vllm-project/vllm/pull/57392), [#58045](https://github.com/vllm-project/vllm/pull/58045), [#58344](https://github.com/vllm-project/vllm/pull/58344), [#58743](https://github.com/vllm-project/vllm/pull/58743), ... (19 total) |
| `vllm/models/kimi_k3/amd/kda_metadata.py` | [#51862](https://github.com/vllm-project/vllm/pull/51862), [#58344](https://github.com/vllm-project/vllm/pull/58344), [#59824](https://github.com/vllm-project/vllm/pull/59824), [#63342](https://github.com/vllm-project/vllm/pull/63342) |
| `vllm/models/kimi_k3/amd/latent_moe_runner.py` | [#51253](https://github.com/vllm-project/vllm/pull/51253), [#54956](https://github.com/vllm-project/vllm/pull/54956), [#59591](https://github.com/vllm-project/vllm/pull/59591) |
| `vllm/models/kimi_k3/amd/linear.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50592](https://github.com/vllm-project/vllm/pull/50592), [#50593](https://github.com/vllm-project/vllm/pull/50593), [#50649](https://github.com/vllm-project/vllm/pull/50649), [#50761](https://github.com/vllm-project/vllm/pull/50761), [#51253](https://github.com/vllm-project/vllm/pull/51253), [#52494](https://github.com/vllm-project/vllm/pull/52494), [#58743](https://github.com/vllm-project/vllm/pull/58743), [#59069](https://github.com/vllm-project/vllm/pull/59069), [#59591](https://github.com/vllm-project/vllm/pull/59591), [#59634](https://github.com/vllm-project/vllm/pull/59634), [#60110](https://github.com/vllm-project/vllm/pull/60110), ... (14 total) |
| `vllm/models/kimi_k3/amd/mla.py` | [#52494](https://github.com/vllm-project/vllm/pull/52494), [#57640](https://github.com/vllm-project/vllm/pull/57640), [#59069](https://github.com/vllm-project/vllm/pull/59069), [#59634](https://github.com/vllm-project/vllm/pull/59634), [#60110](https://github.com/vllm-project/vllm/pull/60110), [#60683](https://github.com/vllm-project/vllm/pull/60683), [#61654](https://github.com/vllm-project/vllm/pull/61654), [#63409](https://github.com/vllm-project/vllm/pull/63409), [#64886](https://github.com/vllm-project/vllm/pull/64886) |
| `vllm/models/kimi_k3/amd/model.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#59278](https://github.com/vllm-project/vllm/pull/59278), [#60683](https://github.com/vllm-project/vllm/pull/60683), [#64158](https://github.com/vllm-project/vllm/pull/64158) |
| `vllm/models/kimi_k3/amd/mtp.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#59634](https://github.com/vllm-project/vllm/pull/59634) |
| `vllm/models/kimi_k3/amd/ops/__init__.py` | [#50090](https://github.com/vllm-project/vllm/pull/50090), [#50131](https://github.com/vllm-project/vllm/pull/50131) |
| `vllm/models/kimi_k3/amd/ops/attn_res.py` | [#50090](https://github.com/vllm-project/vllm/pull/50090), [#50593](https://github.com/vllm-project/vllm/pull/50593), [#59069](https://github.com/vllm-project/vllm/pull/59069), [#60717](https://github.com/vllm-project/vllm/pull/60717) |
| `vllm/models/kimi_k3/amd/ops/kda_checkpoint.py` | [#58344](https://github.com/vllm-project/vllm/pull/58344) |
| `vllm/models/kimi_k3/amd/ops/kda_chunk.py` | [#52606](https://github.com/vllm-project/vllm/pull/52606), [#53294](https://github.com/vllm-project/vllm/pull/53294), [#54038](https://github.com/vllm-project/vllm/pull/54038), [#56526](https://github.com/vllm-project/vllm/pull/56526), [#58344](https://github.com/vllm-project/vllm/pull/58344), [#58743](https://github.com/vllm-project/vllm/pull/58743) |
| `vllm/models/kimi_k3/amd/ops/kda_decode.py` | [#50654](https://github.com/vllm-project/vllm/pull/50654), [#58743](https://github.com/vllm-project/vllm/pull/58743), [#61207](https://github.com/vllm-project/vllm/pull/61207) |
| `vllm/models/kimi_k3/amd/ops/kda_prefill.py` | [#52606](https://github.com/vllm-project/vllm/pull/52606), [#53294](https://github.com/vllm-project/vllm/pull/53294), [#54038](https://github.com/vllm-project/vllm/pull/54038), [#58344](https://github.com/vllm-project/vllm/pull/58344), [#58743](https://github.com/vllm-project/vllm/pull/58743), [#59552](https://github.com/vllm-project/vllm/pull/59552) |
| `vllm/models/kimi_k3/amd/ops/third_party/__init__.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089) |
| `vllm/models/kimi_k3/amd/ops/third_party/kda/__init__.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#58045](https://github.com/vllm-project/vllm/pull/58045) |
| `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#50649](https://github.com/vllm-project/vllm/pull/50649), [#51862](https://github.com/vllm-project/vllm/pull/51862), [#58769](https://github.com/vllm-project/vllm/pull/58769) |
| `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#58769](https://github.com/vllm-project/vllm/pull/58769), [#60446](https://github.com/vllm-project/vllm/pull/60446) |
| `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#58769](https://github.com/vllm-project/vllm/pull/58769) |
| `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` | [#50089](https://github.com/vllm-project/vllm/pull/50089), [#51682](https://github.com/vllm-project/vllm/pull/51682), [#58045](https://github.com/vllm-project/vllm/pull/58045) |
| `vllm/models/kimi_k3/amd/specialized_decode/README.md` | [#60683](https://github.com/vllm-project/vllm/pull/60683), [#61435](https://github.com/vllm-project/vllm/pull/61435), [#63031](https://github.com/vllm-project/vllm/pull/63031), [#64029](https://github.com/vllm-project/vllm/pull/64029) |
| `vllm/models/kimi_k3/amd/specialized_decode/__init__.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683), [#64029](https://github.com/vllm-project/vllm/pull/64029) |
| `vllm/models/kimi_k3/amd/specialized_decode/hooks.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683) |
| `vllm/models/kimi_k3/amd/specialized_decode/model_state.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683) |
| `vllm/models/kimi_k3/amd/specialized_decode/mono/__init__.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683) |
| `vllm/models/kimi_k3/amd/specialized_decode/mono/abi.py` | [#60683](https://github.com/vllm-project/vllm/pull/60683) |
| ... | 134 more files omitted from table; all were used for git tracing. |

## PR 覆盖总览

- git 追溯 PR 数: 160
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 160

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-05 | [#63730](https://github.com/vllm-project/vllm/pull/63730) | merged | [ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels | `vllm/models/kimi_k3/amd/linear.py` |
| 2026-11-05 | [#64886](https://github.com/vllm-project/vllm/pull/64886) | merged | [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes | `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/mla.py` |
| 2026-11-04 | [#64583](https://github.com/vllm-project/vllm/pull/64583) | merged | [Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode | `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` |
| 2026-11-04 | [#62203](https://github.com/vllm-project/vllm/pull/62203) | merged | [Perf][ToolParser] Scan Kimi K3 streaming tool calls incrementally | `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py` |
| 2026-11-03 | [#65174](https://github.com/vllm-project/vllm/pull/65174) | merged | [Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig | `vllm/transformers_utils/configs/kimi_vl.py` |
| 2026-11-03 | [#61435](https://github.com/vllm-project/vllm/pull/61435) | merged | [ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8) | `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md` |
| 2026-11-02 | [#64029](https://github.com/vllm-project/vllm/pull/64029) | merged | [ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows | `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` |
| 2026-11-02 | [#61950](https://github.com/vllm-project/vllm/pull/61950) | merged | [Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections | `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-31 | [#63297](https://github.com/vllm-project/vllm/pull/63297) | merged | [ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend | `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-30 | [#64619](https://github.com/vllm-project/vllm/pull/64619) | merged | [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub | `tests/models/kimi_k3/test_amd_kda_checkpoint.py` |
| 2026-10-29 | [#53011](https://github.com/vllm-project/vllm/pull/53011) | merged | [Bugfix] Avoid eager torch.compile in Kimi K2.5 vision helper | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-10-28 | [#64158](https://github.com/vllm-project/vllm/pull/64158) | merged | [ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model | `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/model.py` |
| 2026-10-27 | [#63989](https://github.com/vllm-project/vllm/pull/63989) | merged | [Bugfix][Kimi-K3] Reserve KDA prefill workspace before profiling | `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-10-27 | [#63409](https://github.com/vllm-project/vllm/pull/63409) | merged | [ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel | `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/mla.py` |
| 2026-10-27 | [#60110](https://github.com/vllm-project/vllm/pull/60110) | merged | [ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query | `vllm/models/kimi_k3/amd/mla.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/linear.py` |
| 2026-10-27 | [#63342](https://github.com/vllm-project/vllm/pull/63342) | merged | [ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d | `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-27 | [#62141](https://github.com/vllm-project/vllm/pull/62141) | merged | [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355 | `tests/models/kimi_k3/test_prefix_cache.py` |
| 2026-10-26 | [#63638](https://github.com/vllm-project/vllm/pull/63638) | merged | [Perf][Kimi K3] Opt-in KV-balanced FP8 MLA decode for agentic workloads | `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py`, `tests/models/kimi_k3/test_kv_balanced_mla.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py` |
| 2026-10-26 | [#61527](https://github.com/vllm-project/vllm/pull/61527) | merged | [Kimi-K3] Route the fp8 chunked-context K/V pack through FlashInfer where it has a fused kernel | `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` |
| 2026-10-26 | [#63531](https://github.com/vllm-project/vllm/pull/63531) | merged | [XPU] Fix Kimi-Linear model dispatch | `vllm/models/kimi_k3/__init__.py` |
| 2026-10-24 | [#63449](https://github.com/vllm-project/vllm/pull/63449) | merged | [CI][Kimi-K3] Expect no trailing-block drop in DSpark resend tests | `tests/models/kimi_k3/test_prefix_cache.py` |
| 2026-10-24 | [#63045](https://github.com/vllm-project/vllm/pull/63045) | merged | [Kimi K3] KDA RecoverSSM: CuTe verify and commit kernels, records outside the KV cache | `tests/models/kimi_k3/test_recoverssm_kernels.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py` |
| 2026-10-23 | [#63031](https://github.com/vllm-project/vllm/pull/63031) | merged | [ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode | `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md` |
| 2026-10-23 | [#58743](https://github.com/vllm-project/vllm/pull/58743) | merged | [ROCm][Kimi-K3] Support BF16 KDA recurrent state | `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-22 | [#62507](https://github.com/vllm-project/vllm/pull/62507) | merged | [Bugfix][Frontend][Kimi K3] Fix Kimi K3 XTML marker leakage in responses API | `tests/tool_use/test_kimi_k3_tool_parser.py`, `tests/reasoning/test_kimi_k3_reasoning_parser.py` |
| 2026-10-22 | [#62980](https://github.com/vllm-project/vllm/pull/62980) | merged | [Bugfix] Support online quantization of Kimi K3 NVIDIA projections | `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` |
| 2026-10-21 | [#60683](https://github.com/vllm-project/vllm/pull/60683) | merged | [ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X | `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` |
| 2026-10-20 | [#59634](https://github.com/vllm-project/vllm/pull/59634) | merged | [ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep | `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mtp.py` |
| 2026-10-16 | [#59552](https://github.com/vllm-project/vllm/pull/59552) | merged | [ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill | `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py` |
| 2026-10-16 | [#59824](https://github.com/vllm-project/vllm/pull/59824) | merged | [ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X | `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `vllm/models/kimi_k3/amd/kda_metadata.py` |
| 2026-10-16 | [#61867](https://github.com/vllm-project/vllm/pull/61867) | merged | [Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x) | `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py` |
| 2026-10-15 | [#57392](https://github.com/vllm-project/vllm/pull/57392) | merged | [ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode | `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-14 | [#61654](https://github.com/vllm-project/vllm/pull/61654) | merged | [ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper | `vllm/models/kimi_k3/amd/mla.py` |
| 2026-10-13 | [#61207](https://github.com/vllm-project/vllm/pull/61207) | merged | [Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading | `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-09 | [#60446](https://github.com/vllm-project/vllm/pull/60446) | merged | [Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys | `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py` |
| 2026-10-09 | [#60717](https://github.com/vllm-project/vllm/pull/60717) | merged | [ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization | `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py` |
| 2026-10-08 | [#56875](https://github.com/vllm-project/vllm/pull/56875) | merged | [Perf] Enable Kimi K3 shared expert sharding with DeepEP v2 | `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_sequence_parallel.py` |
| 2026-10-08 | [#59591](https://github.com/vllm-project/vllm/pull/59591) | merged | [ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj | `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py` |
| 2026-10-08 | [#59069](https://github.com/vllm-project/vllm/pull/59069) | merged | [ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization | `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py` |
| 2026-10-08 | [#59733](https://github.com/vllm-project/vllm/pull/59733) | merged | [Bugfix][Kimi-K3] Declare max_tp_shards on the DSpark MLA KV cache spec | `tests/models/test_dspark_mla.py`, `vllm/models/kimi_k3/nvidia/mla.py` |
| 2026-10-06 | [#56881](https://github.com/vllm-project/vllm/pull/56881) | merged | [Kimi-K3] Use the fused K/V pack kernel on the decode-context-parallel prefill path | `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py` |
| 2026-10-05 | [#59278](https://github.com/vllm-project/vllm/pull/59278) | merged | [Model] Extend device-side mm normalization to Kimi K2.5 / K3 | `tests/models/multimodal/processing/test_kimi_k3.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-10-03 | [#51274](https://github.com/vllm-project/vllm/pull/51274) | merged | [ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion | `tests/models/kimi_k3/test_gfx942_int4.py` |
| 2026-10-02 | [#59229](https://github.com/vllm-project/vllm/pull/59229) | merged | [CI][Kimi-K3] Test prefix cache reuse with KV offload, P/D and DCP | `tests/models/kimi_k3/test_prefix_cache.py` |
| 2026-10-02 | [#58344](https://github.com/vllm-project/vllm/pull/58344) | merged | [ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm | `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-10-01 | [#58769](https://github.com/vllm-project/vllm/pull/58769) | merged | [ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor … | `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py` |
| 2026-10-01 | [#59257](https://github.com/vllm-project/vllm/pull/59257) | merged | [Bugfix] Gate Kimi-K3 KDA warmup on sys.modules to skip Kimi import for non-Kimi models | `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` |
| 2026-10-01 | [#54255](https://github.com/vllm-project/vllm/pull/54255) | merged | [Kimi-K3] Add FlashInfer speculative KDA backend | `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-09-30 | [#57640](https://github.com/vllm-project/vllm/pull/57640) | merged | [ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER | `vllm/models/kimi_k3/amd/mla.py` |
| 2026-09-28 | [#58814](https://github.com/vllm-project/vllm/pull/58814) | merged | [Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound | `vllm/models/kimi_k3/nvidia/dspark_mla.py` |
| 2026-09-28 | [#54956](https://github.com/vllm-project/vllm/pull/54956) | merged | [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP | `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py` |
| 2026-09-28 | [#58651](https://github.com/vllm-project/vllm/pull/58651) | merged | [KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-09-25 | [#58372](https://github.com/vllm-project/vllm/pull/58372) | merged | [Bugfix][Reasoning] Count Kimi K3 reasoning tokens | `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py` |
| 2026-09-25 | [#58045](https://github.com/vllm-project/vllm/pull/58045) | merged | [ROCm][Kimi-K3] Optimize low-concurrency speculative KDA | `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`, `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py` |
| 2026-09-25 | [#58527](https://github.com/vllm-project/vllm/pull/58527) | merged | [Kimi-K3][Perf] Dispatch GEMM for vision patch embedder | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-09-23 | [#58012](https://github.com/vllm-project/vllm/pull/58012) | merged | [CI][ROCm] Add an MI355 Kimi-K3 unit test group | `tests/models/kimi_k3/test_attn_res.py` |
| 2026-09-23 | [#52988](https://github.com/vllm-project/vllm/pull/52988) | merged | [Spec decode] Support variable-length decode for Kimi-K3 adaptive ver | `vllm/models/kimi_k3/nvidia/dspark_mla.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py` |
| 2026-09-21 | [#50592](https://github.com/vllm-project/vllm/pull/50592) | merged | [Kimi-K3][AMD] Return KDA and MLA projection outputs directly | `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py` |
| 2026-09-18 | [#57430](https://github.com/vllm-project/vllm/pull/57430) | merged | [Quantization] Support kimi-k3 routed expert quant | `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-09-17 | [#57098](https://github.com/vllm-project/vllm/pull/57098) | merged | [Kimi K3 Bug] Fix kimi k3 reasoning parser | `vllm/reasoning/kimi_k3_reasoning_parser.py` |
| 2026-09-16 | [#51483](https://github.com/vllm-project/vllm/pull/51483) | merged | [Bugfix][Kimi-K3] Do not classify a stateless first chunk as a decode | `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py` |
| 2026-09-12 | [#56526](https://github.com/vllm-project/vllm/pull/56526) | merged | [ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill | `vllm/models/kimi_k3/amd/ops/kda_chunk.py` |
| 2026-09-11 | [#55426](https://github.com/vllm-project/vllm/pull/55426) | merged | [Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper | `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-09-11 | [#55356](https://github.com/vllm-project/vllm/pull/55356) | merged | [Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch | `vllm/models/kimi_k3/nvidia/dspark_mla.py` |
| 2026-09-10 | [#56159](https://github.com/vllm-project/vllm/pull/56159) | merged | [Kimi K3 Perf] Avoid KDA mixed-batch gather/scatter, 5.2%~7.7% E2E Throughput Improvement | `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `tests/models/kimi_k3/test_kda.py` |
| 2026-09-10 | [#54038](https://github.com/vllm-project/vllm/pull/54038) | merged | [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland | `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py` |
| 2026-09-08 | [#55924](https://github.com/vllm-project/vllm/pull/55924) | merged | [Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered` | `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-09-08 | [#53379](https://github.com/vllm-project/vllm/pull/53379) | merged | [Bugfix] Fix Kimi K3 loading with interleaved weight streams | `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-09-06 | [#53614](https://github.com/vllm-project/vllm/pull/53614) | merged | [Kimi K3] Support internal prefix checkpoints with partial prefix caching and spec-decoding | `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-09-05 | [#55242](https://github.com/vllm-project/vllm/pull/55242) | merged | [Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy | `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-09-04 | [#52494](https://github.com/vllm-project/vllm/pull/52494) | merged | [AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper | `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py` |
| 2026-09-03 | [#54896](https://github.com/vllm-project/vllm/pull/54896) | merged | [Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency | `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` |
| 2026-09-03 | [#54606](https://github.com/vllm-project/vllm/pull/54606) | merged | [Kernel] Enable Kimi-K3 SiTU on the CuteDSL MoE backend and the SM107 low-latency GEMM plan | `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-09-02 | [#54817](https://github.com/vllm-project/vllm/pull/54817) | merged | [CI] Add Kimi-K3-pruned75-DSpark-TP4 gsm8k eval | `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml` |
| 2026-09-02 | [#54859](https://github.com/vllm-project/vllm/pull/54859) | merged | [Kimi-K3] Bump FlashKDA to fix unstable inverse | `tests/models/kimi_k3/test_kda.py` |
| 2026-09-02 | [#54697](https://github.com/vllm-project/vllm/pull/54697) | merged | [Kimi-K3] Overlap low-M TP8 KDA projections | `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-09-01 | [#54781](https://github.com/vllm-project/vllm/pull/54781) | merged | [Kimi Bug] Fix `cannot access local variable 'active_non_spec_mask_cpu'` | `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py` |
| 2026-08-31 | [#54261](https://github.com/vllm-project/vllm/pull/54261) | merged | [Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default | `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `benchmarks/kernels/benchmark_kimi_k3_attn_res.py` |
| 2026-08-31 | [#54482](https://github.com/vllm-project/vllm/pull/54482) | merged | [CI/Build] Fix Kimi K3 Eagle3 test fixture | `tests/models/kimi_k3/test_eagle3.py` |
| 2026-08-28 | [#54168](https://github.com/vllm-project/vllm/pull/54168) | merged | [Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail | `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py`, `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py` |
| 2026-08-28 | [#54167](https://github.com/vllm-project/vllm/pull/54167) | merged | [Kimi-K3][Bugfix] Fix low-latency GEMM fallback initialization | `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-08-28 | [#54015](https://github.com/vllm-project/vllm/pull/54015) | merged | [Kimi-K3] Merge MLA gate into QKV-A projection | `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mtp.py` |
| 2026-08-27 | [#54088](https://github.com/vllm-project/vllm/pull/54088) | merged | [Kimi Perf] Tune hopper low latency gemm kernel, 4%~97% performance improvement | `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-08-27 | [#53396](https://github.com/vllm-project/vllm/pull/53396) | merged | [Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel | `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` |
| 2026-08-26 | [#53942](https://github.com/vllm-project/vllm/pull/53942) | merged | [Kimi K3 Perf] Optimize `eh_proj` linear calculation, 12.9 ~ 25.2% kernel performance improvement | `vllm/models/kimi_k3/nvidia/mtp.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-08-25 | [#53534](https://github.com/vllm-project/vllm/pull/53534) | merged | [Kimi K3][Kernel] Enable low-latency decode GEMM dispatch on SM100 | `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` |
| 2026-08-25 | [#53766](https://github.com/vllm-project/vllm/pull/53766) | merged | [CI Bug] Fix kimi test `AssertionError: Aligned Mamba state indices must be precomputed` | `tests/models/kimi_k3/test_kda_metadata.py` |
| 2026-08-24 | [#53581](https://github.com/vllm-project/vllm/pull/53581) | merged | [Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling | `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-08-22 | [#53327](https://github.com/vllm-project/vllm/pull/53327) | merged | [Bugfix][Kimi K3] Enable deferred MoE finalization before weight loading | `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` |
| 2026-08-21 | [#53294](https://github.com/vllm-project/vllm/pull/53294) | merged | Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill" | `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py` |
| 2026-08-21 | [#52606](https://github.com/vllm-project/vllm/pull/52606) | merged | [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill | `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py` |
| 2026-08-21 | [#53132](https://github.com/vllm-project/vllm/pull/53132) | merged | Support kimi k3 nvfp4 checkpoint | `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-08-21 | [#53053](https://github.com/vllm-project/vllm/pull/53053) | merged | [Kimi-K3] Extend GEMM-RS to GEMM-AR | `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py` |
| 2026-08-20 | [#50400](https://github.com/vllm-project/vllm/pull/50400) | merged | [Kernel][Kimi] fused vision q/k roper kernel | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-08-18 | [#50493](https://github.com/vllm-project/vllm/pull/50493) | merged | [Kimi-K3] support DCP partial prefix cache hit | `tests/distributed/test_kimi_linear_context_parallel.py` |
| 2026-08-17 | [#52188](https://github.com/vllm-project/vllm/pull/52188) | merged | [Spec decode] Support Kimi-K3 DCP with DSpark | `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py` |
| 2026-08-17 | [#51809](https://github.com/vllm-project/vllm/pull/51809) | merged | [XPU] Enable Kimi K3 KDA kernel tests on XPU | `tests/models/kimi_k3/test_kda.py` |
| 2026-08-15 | [#52445](https://github.com/vllm-project/vllm/pull/52445) | merged | [Bugfix][Model] Kimi-K3 MegaMoE: pass situ_beta/situ_linear_beta to fp8_fp4_mega_moe | `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-08-14 | [#50487](https://github.com/vllm-project/vllm/pull/50487) | merged | [Model][Spec Decode] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state | `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_eagle3.py` |
| 2026-08-13 | [#52171](https://github.com/vllm-project/vllm/pull/52171) | merged | [Bugfix] Declare SupportsEagle3 on KimiLinearForCausalLM | `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-08-13 | [#52079](https://github.com/vllm-project/vllm/pull/52079) | merged | [Kimi-K3] Add GEMM-RS for sequence parallelism | `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-08-13 | [#51862](https://github.com/vllm-project/vllm/pull/51862) | merged | [ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA | `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` |
| 2026-08-13 | [#51772](https://github.com/vllm-project/vllm/pull/51772) | merged | [Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing | `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` |
| 2026-08-12 | [#50654](https://github.com/vllm-project/vllm/pull/50654) | merged | [ROCm][Perf] Kimi-K3 Fused kernel for KDA decode | `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-08-10 | [#50484](https://github.com/vllm-project/vllm/pull/50484) | merged | [Kimi-K3] DCP support | `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py`, `tests/distributed/test_kimi_linear_context_parallel.py` |
| 2026-08-10 | [#51682](https://github.com/vllm-project/vllm/pull/51682) | merged | [Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride | `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` |
| 2026-08-09 | [#51529](https://github.com/vllm-project/vllm/pull/51529) | merged | [K3] Allow tpu to import kimi_k3.common | `vllm/models/kimi_k3/__init__.py` |
| 2026-08-08 | [#51196](https://github.com/vllm-project/vllm/pull/51196) | merged | [Kimi][MM] disable kimi_vit's dynamic torch.compile for TPU | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-08-07 | [#51253](https://github.com/vllm-project/vllm/pull/51253) | merged | [ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path | `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `tests/models/kimi_k3/__init__.py` |
| 2026-08-06 | [#51249](https://github.com/vllm-project/vllm/pull/51249) | merged | [Bugfix][Model] Add missing fused_qkv_a_proj to Kimi-Linear packed_modules_mapping | `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-08-05 | [#50649](https://github.com/vllm-project/vllm/pull/50649) | merged | [ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config | `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` |
| 2026-08-05 | [#50404](https://github.com/vllm-project/vllm/pull/50404) | merged | [Model] Fix Kimi-K3 MLA with disabled context parallelism | `vllm/models/kimi_k3/nvidia/mla.py` |
| 2026-08-04 | [#50912](https://github.com/vllm-project/vllm/pull/50912) | merged | [Kimi K3 Perf] option to shard the shared expert for non mega case, 16.98 GiB memory/GPU saved | `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-08-04 | [#50929](https://github.com/vllm-project/vllm/pull/50929) | merged | [MM][CG] Support ViT full CUDA graph for Kimi-K2.5 | `vllm/model_executor/models/kimi_k25.py` |
| 2026-08-04 | [#50593](https://github.com/vllm-project/vllm/pull/50593) | merged | [Kimi-K3][AMD] Fuse AttnRes state updates and norms | `vllm/models/kimi_k3/amd/ops/attn_res.py`, `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/linear.py` |
| 2026-08-04 | [#50886](https://github.com/vllm-project/vllm/pull/50886) | merged | [Bugfix][Reasoning] kimi_k3: O(delta) reasoning-end check on the decode path | `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py` |
| 2026-08-04 | [#50567](https://github.com/vllm-project/vllm/pull/50567) | merged | [Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch | `vllm/models/kimi_k3/nvidia/ops/attn_res.py` |
| 2026-08-03 | [#50656](https://github.com/vllm-project/vllm/pull/50656) | merged | [Kimi-K3] Add option to shard the shared expert instead of replicating | `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-08-02 | [#50761](https://github.com/vllm-project/vllm/pull/50761) | merged | [ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32 | `vllm/models/kimi_k3/amd/linear.py` |
| 2026-07-31 | [#50500](https://github.com/vllm-project/vllm/pull/50500) | merged | [Compressed-Tensors] Support Kimi-K3 quantized models | `vllm/models/kimi_k3/nvidia/model.py` |
| 2026-07-31 | [#50420](https://github.com/vllm-project/vllm/pull/50420) | merged | [Frontend][Bugfix] Use default tool call IDs for Kimi K3 for conversation-level uniqueness | `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py` |
| 2026-07-30 | [#50000](https://github.com/vllm-project/vllm/pull/50000) | merged | [New model] Kimi K3 | `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/model_executor/models/kimi_linear.py`, `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-07-29 | [#50262](https://github.com/vllm-project/vllm/pull/50262) | merged | [ROCm][CI] Fix Kimi K3 KDA on ROCm | `vllm/models/kimi_k3/nvidia/kda.py` |
| 2026-07-29 | [#50093](https://github.com/vllm-project/vllm/pull/50093) | merged | [Model] Add Kimi K3 support: Python frontend [2/2] | `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py` |
| 2026-07-29 | [#50089](https://github.com/vllm-project/vllm/pull/50089) | merged | [Model] Add Kimi K3 support: model files and kernels [1/N] | `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py`, `vllm/models/kimi_k3/amd/linear.py` |
| 2026-07-28 | [#50131](https://github.com/vllm-project/vllm/pull/50131) | merged | [Bugfix] Add missing `vllm/models/kimi_k3/__init__.py` | `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py` |
| 2026-07-28 | [#50090](https://github.com/vllm-project/vllm/pull/50090) | merged | [Kimi-K3] Add AttnRes kernels | `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py` |
| 2026-07-06 | [#47416](https://github.com/vllm-project/vllm/pull/47416) | merged | [perf]Add fused Kimi image preprocessing | `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`, `vllm/model_executor/models/kimi_k25.py` |
| 2026-06-30 | [#46610](https://github.com/vllm-project/vllm/pull/46610) | merged | [Frontend] Add Streaming Parser Engine and new Kimi k2.5/k2.6/k2.7 Parser | `vllm/tool_parsers/kimi_k2_tool_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`, `tests/reasoning/test_kimi_k2_reasoning_parser.py` |
| 2026-06-17 | [#41992](https://github.com/vllm-project/vllm/pull/41992) | merged | [MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL | `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py` |
| 2026-06-04 | [#44493](https://github.com/vllm-project/vllm/pull/44493) | merged | [Bugfix]Fix Kimi-K2.5 FlashInfer ViT metadata | `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py` |
| 2026-05-18 | [#42869](https://github.com/vllm-project/vllm/pull/42869) | merged | [BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization | `vllm/model_executor/models/kimi_k25.py` |
| 2026-05-11 | [#42081](https://github.com/vllm-project/vllm/pull/42081) | merged | [Bug] Fix kimi dtype issue with `mm_projector_forward` | `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-05-04 | [#41068](https://github.com/vllm-project/vllm/pull/41068) | merged | [Bugfix] KimiK2ReasoningParser: guard against buffered end-token in streaming | `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py` |
| 2026-04-19 | [#38579](https://github.com/vllm-project/vllm/pull/38579) | merged | [Bugfix] Kimi-K2 tool parser streaming - fix token leakage, argument truncation, and content dropping | `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py` |
| 2026-04-12 | [#39344](https://github.com/vllm-project/vllm/pull/39344) | merged | fix(kimi_k25): resolve media_placeholder_token_id from tokenizer | `vllm/model_executor/models/kimi_k25.py` |
| 2026-03-20 | [#37693](https://github.com/vllm-project/vllm/pull/37693) | merged | [Model] Update Kimi-K25 and Isaac processors to fit HF-style | `vllm/transformers_utils/processors/kimi_k25.py`, `vllm/model_executor/models/kimi_k25.py` |
| 2026-03-19 | [#37438](https://github.com/vllm-project/vllm/pull/37438) | merged | [Bugfix] Add Kimi-K2.5 reasoning/tool parser aliases and tool_call_id support | `tests/reasoning/test_kimi_k2_reasoning_parser.py` |
| 2026-03-14 | [#36903](https://github.com/vllm-project/vllm/pull/36903) | merged | [Misc] Clean up Kimi-audio whisper encoder loading | `vllm/model_executor/models/kimi_audio.py` |
| 2026-03-11 | [#36361](https://github.com/vllm-project/vllm/pull/36361) | merged | Kimi k2.5 MLA based eagle3 | `vllm/model_executor/models/kimi_k25.py` |
| 2026-03-11 | [#36127](https://github.com/vllm-project/vllm/pull/36127) | merged | [Model] Add support for moonshotai/Kimi-Audio-7B-Instruct | `vllm/model_executor/models/kimi_audio.py`, `vllm/tokenizers/kimi_audio.py`, `vllm/transformers_utils/processors/kimi_audio.py` |
| 2026-03-06 | [#36192](https://github.com/vllm-project/vllm/pull/36192) | merged | [Security] Respect user trust_remote_code setting in NemotronVL and KimiK25 | `vllm/model_executor/models/kimi_k25.py` |
| 2026-02-27 | [#33646](https://github.com/vllm-project/vllm/pull/33646) | merged | [Bugfix] Handle case when kimi ends reasoning with a tool call | `vllm/reasoning/kimi_k2_reasoning_parser.py` |
| 2026-02-13 | [#34501](https://github.com/vllm-project/vllm/pull/34501) | merged | [Bugfix] Add quant_config in ViT of Kimi-K2.5 | `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py` |
| 2026-02-13 | [#34427](https://github.com/vllm-project/vllm/pull/34427) | merged | [Bugfix] Delete unused redundant code in Kimi-K2.5 | `vllm/model_executor/models/kimi_k25.py` |
| 2026-02-05 | [#33876](https://github.com/vllm-project/vllm/pull/33876) | merged | [Bugfix] Fix Kimi-K2.5 NVFP4 checkpoints weight loading | `vllm/model_executor/models/kimi_k25.py` |
| 2026-02-02 | [#33562](https://github.com/vllm-project/vllm/pull/33562) | merged | [Bugfix] Enable Kimi k25 processor test | `vllm/model_executor/models/kimi_k25.py` |
| 2026-01-30 | [#33346](https://github.com/vllm-project/vllm/pull/33346) | merged | [Models] Refactor Kimi-K2.5 weight loading | `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py` |
| 2026-01-29 | [#33320](https://github.com/vllm-project/vllm/pull/33320) | merged | [Backport] [Kimi-K2.5] Replace torch.cuda with current_platform for d… | `vllm/model_executor/models/kimi_k25.py` |
| 2026-01-27 | [#33131](https://github.com/vllm-project/vllm/pull/33131) | merged | [Models] Kimi-K2.5 | `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/configs/kimi_k25.py` |
| 2026-01-06 | [#31738](https://github.com/vllm-project/vllm/pull/31738) | merged | [Models]: Use `MMEncoderAttention` for MoonViT | `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py` |
| 2025-12-30 | [#31207](https://github.com/vllm-project/vllm/pull/31207) | merged | fix: update kimi k2 tool parser logic | `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py` |
| 2025-11-24 | [#29309](https://github.com/vllm-project/vllm/pull/29309) | merged | [XPU]fix Kimi-VL-A3B-thinking on xpu | `vllm/model_executor/models/moonvit.py` |
| 2025-10-30 | [#27809](https://github.com/vllm-project/vllm/pull/27809) | merged | [Model] Introduce Kimi Linear to vLLM | `vllm/model_executor/models/kimi_linear.py`, `vllm/transformers_utils/configs/kimi_linear.py` |
| 2025-09-01 | [#23817](https://github.com/vllm-project/vllm/pull/23817) | merged | [Model] Support DP for ViT on Kimi-VL-A3B-Thinking-2506 | `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py` |
| 2025-08-19 | [#23114](https://github.com/vllm-project/vllm/pull/23114) | merged | [Model] Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506 | `vllm/model_executor/models/kimi_vl.py` |
| 2025-08-05 | [#21769](https://github.com/vllm-project/vllm/pull/21769) | merged | Migrate KimiVLImagePixelInputs to TensorSchema | `vllm/model_executor/models/kimi_vl.py` |
| 2025-04-25 | [#17156](https://github.com/vllm-project/vllm/pull/17156) | merged | fix float16 support for kimi-vl | `vllm/model_executor/models/kimi_vl.py` |
| 2025-04-18 | [#16833](https://github.com/vllm-project/vllm/pull/16833) | merged | [Misc] Clean up Kimi-VL | `vllm/model_executor/models/kimi_vl.py` |
| 2025-04-14 | [#16387](https://github.com/vllm-project/vllm/pull/16387) | merged | [Model][VLM] Add Kimi-VL model support | `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/transformers_utils/configs/kimi_vl.py` |

## 逐 PR diff 审计卡

### PR #63730 - [ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels

- 链接: https://github.com/vllm-project/vllm/pull/63730
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/linear.py`；关联提交 `ae96354d8bf3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+176/-1，可读 patch 224 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels」；主要实现面是 `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/linear.py` modified +6/-1 (7 lines); hunks: -275,11 +275,16 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/linear.py` modified +6/-1 (7 lines); hunks: -275,11 +275,16 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -275,11 +275,16 @@ def __init__(
+            # The checkpoint stores this layer in BF16 even when its quant config
+            # targets every Linear, so only online quantization may apply.
+            down_quant_config = quant_config
+            if quant_config is not None and quant_config.get_name() != "online":
+                down_quant_config = quant_config.online_quantization_config
-                quant_config=None,
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/linear.py` modified +6/-1
- 验证与风险: diff 自带测试面 `tests/model_executor/model_loader/test_reload.py`, `tests/model_executor/test_rocm_aiter_gemm_warmup.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64886 - [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes

- 链接: https://github.com/vllm-project/vllm/pull/64886
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/mla.py`；关联提交 `e5d0ef3527c9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+57/-16，可读 patch 140 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/mla.py`；技术摘要: 覆盖「[Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13 (45 lines); hunks: -346,12 +346,15 @@ def test_decode_weights_staged_after_loading(; -412,20 +415,36 @@ def test_decode_weights_staged_after_loading(; symbols: test_decode_weights_staged_after_loading, check_staged，涉及 `test_decode_weights_staged_after_loading, check_staged`；`vllm/models/kimi_k3/amd/kda.py` modified +5/-3 (8 lines); hunks: -344,10 +344,12 @@ def __init__(; symbols: __init__, process_weights_after_loading, refresh_derived_weights，涉及 `__init__, process_weights_after_loading, refresh_derived_weights`；`vllm/models/kimi_k3/amd/mla.py` modified +3/-0 (3 lines); hunks: -185,6 +185,9 @@ def _build_w_fold(self) -> None:; symbols: _build_w_fold, process_weights_after_loading, refresh_derived_weights，涉及 `_build_w_fold, process_weights_after_loading, refresh_derived_weights`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13 (45 lines); hunks: -346,12 +346,15 @@ def test_decode_weights_staged_after_loading(; -412,20 +415,36 @@ def test_decode_weights_staged_after_loading(; symbols: test_decode_weights_staged_after_loading, check_staged
  - `vllm/models/kimi_k3/amd/kda.py` modified +5/-3 (8 lines); hunks: -344,10 +344,12 @@ def __init__(; symbols: __init__, process_weights_after_loading, refresh_derived_weights
  - `vllm/models/kimi_k3/amd/mla.py` modified +3/-0 (3 lines); hunks: -185,6 +185,9 @@ def _build_w_fold(self) -> None:; symbols: _build_w_fold, process_weights_after_loading, refresh_derived_weights
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_decode.py
@@ -346,12 +346,15 @@ def test_decode_weights_staged_after_loading(
-    on, so the copies must also stay out of autograd.
+    on, so the copies must also stay out of autograd. A kernel-format reload
+    overwrites the weights in place without the post-load hook, so the copies
+    must be re-staged at the addresses captured graphs read.
+    from vllm.model_executor.model_loader.reload.inplace import reload_weights
@@ -412,20 +415,36 @@ def test_decode_weights_staged_after_loading(
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -344,10 +344,12 @@ def __init__(
-    @torch.no_grad()
-        if is_weights_pre_processed():
-            return
+        if not is_weights_pre_processed():
+            self.refresh_derived_weights()
+    @torch.no_grad()
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -185,6 +185,9 @@ def _build_w_fold(self) -> None:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +5/-3; `vllm/models/kimi_k3/amd/mla.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64583 - [Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode

- 链接: https://github.com/vllm-project/vllm/pull/64583
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；关联提交 `75f67614971a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+48/-23，可读 patch 110 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode」；主要实现面是 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +37/-19 (56 lines); hunks: -33,24 +33,26; -94,19 +96,35 @@ def fake_tail_initialize(**kwargs):; symbols: test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, build_runner, fake_tail_initialize，涉及 `test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, build_runner`；`vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-4 (15 lines); hunks: -92,16 +92,23 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_latent_moe_tail.py` modified +37/-19 (56 lines); hunks: -33,24 +33,26; -94,19 +96,35 @@ def fake_tail_initialize(**kwargs):; symbols: test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, build_runner, fake_tail_initialize
  - `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-4 (15 lines); hunks: -92,16 +92,23 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_latent_moe_tail.py
@@ -33,24 +33,26 @@
-def test_deferred_finalize_enabled_before_moe_kernel_setup(
+class FakeMoEConfig:
+    tp_size = 8
+    dp_size = 1
+    ep_size = 1
+    pcp_size = 1
diff -- vllm/models/kimi_k3/nvidia/latent_moe_runner.py
@@ -92,16 +92,23 @@ def __init__(
+        if (
+            self.enable_k3_latent_moe_tail_fusion
+            and use_fused_path
+            and get_current_vllm_config().model_config.enable_sleep_mode
+        ):
+            logger.warning_once(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +37/-19
  - runtime: `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-4
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_latent_moe_tail.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62203 - [Perf][ToolParser] Scan Kimi K3 streaming tool calls incrementally

- 链接: https://github.com/vllm-project/vllm/pull/62203
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`；关联提交 `441d9782064e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+124/-14，可读 patch 175 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][ToolParser] Scan Kimi K3 streaming tool calls incrementally」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`；技术摘要: 覆盖「[Perf][ToolParser] Scan Kimi K3 streaming tool calls incrementally」；主要实现面是 `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +99/-0 (99 lines); hunks: -373,6 +373,105 @@ def test_streaming_split_markers_do_not_leak():; symbols: test_streaming_split_markers_do_not_leak, test_streaming_call_boundaries, test_streaming_does_not_redecode_completed_calls, counted_decode_call，涉及 `test_streaming_split_markers_do_not_leak, test_streaming_call_boundaries, test_streaming_does_not_redecode_completed_calls`；`vllm/tool_parsers/kimi_k3_tool_parser.py` modified +25/-14 (39 lines); hunks: -133,10 +133,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[T...; -365,24 +368,32 @@ def extract_tool_calls_streaming(; symbols: __init__, extract_tool_calls_streaming，涉及 `__init__, extract_tool_calls_streaming`。
- 代码 diff 细节:
  - `tests/tool_use/test_kimi_k3_tool_parser.py` modified +99/-0 (99 lines); hunks: -373,6 +373,105 @@ def test_streaming_split_markers_do_not_leak():; symbols: test_streaming_split_markers_do_not_leak, test_streaming_call_boundaries, test_streaming_does_not_redecode_completed_calls, counted_decode_call
  - `vllm/tool_parsers/kimi_k3_tool_parser.py` modified +25/-14 (39 lines); hunks: -133,10 +133,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[T...; -365,24 +368,32 @@ def extract_tool_calls_streaming(; symbols: __init__, extract_tool_calls_streaming
- 关键代码摘录:

```diff
diff -- tests/tool_use/test_kimi_k3_tool_parser.py
@@ -373,6 +373,105 @@ def test_streaming_split_markers_do_not_leak():
+@pytest.mark.parametrize("chunk_size", [1, 3, 7, 16, 31, 128, 4096])
+@pytest.mark.parametrize(
+    "output",
+    [
+        _response("answer"),
+        "answer" + RESPONSE_CLOSE,
diff -- vllm/tool_parsers/kimi_k3_tool_parser.py
@@ -133,10 +133,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None):
+        self._call_close_re = re.compile(_C + r"\s*call\s*" + _S)
+        self._stream_call_close_idx = 0
+        self._stream_call_parse_idx = 0
@@ -365,24 +368,32 @@ def extract_tool_calls_streaming(
-        # Conservative streaming: stream unwrapped response-channel text, then
-        # buffer tool calls and emit each call once its block closes.
```

- 已读文件:
  - tests: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +99/-0
  - runtime: `vllm/tool_parsers/kimi_k3_tool_parser.py` modified +25/-14
- 验证与风险: diff 自带测试面 `tests/tool_use/test_kimi_k3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65174 - [Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig

- 链接: https://github.com/vllm-project/vllm/pull/65174
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/configs/kimi_vl.py`；关联提交 `2173d7121fc6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/transformers_utils/configs/kimi_vl.py`；技术摘要: 覆盖「[Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig」；主要实现面是 `vllm/transformers_utils/configs/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/configs/kimi_vl.py` modified +2/-1 (3 lines); hunks: -34,5 +34,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/transformers_utils/configs/kimi_vl.py` modified +2/-1 (3 lines); hunks: -34,5 +34,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/configs/kimi_vl.py
@@ -34,5 +34,6 @@ def __init__(
+        self.pad_token_id = pad_token_id
-        super().__init__(pad_token_id=pad_token_id, **kwargs)
+        super().__init__(**kwargs)
```

- 已读文件:
  - runtime: `vllm/transformers_utils/configs/kimi_vl.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/transformers_utils/configs/kimi_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #61435 - [ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8)

- 链接: https://github.com/vllm-project/vllm/pull/61435
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/decode.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/guards.py` 等 7 个文件；关联提交 `254a2a33908a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+160/-115，可读 patch 520 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8)」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8)」；主要实现面是 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +79/-15 (94 lines); hunks: -35,6 +35,7; -90,6 +91,7 @@ def _vllm_config(**over) -> SimpleNamespace:; symbols: _vllm_config, fp4_bmm, on_mi355x，涉及 `_vllm_config, fp4_bmm, on_mi355x`；`vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py` modified +5/-63 (68 lines); hunks: -1,21 +1,17; -37,44 +33,6 @@ def qkv_gate_weights(wrapper):; symbols: qkv_gate_weights, pre, attend, m1c_inputs，涉及 `qkv_gate_weights, pre, attend`；`vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +29/-22 (51 lines); hunks: -11,12 +11,13 @@ layer loop. The TP all-reduces run in-kernel over peer memory.; -29,7 +30,8 @@ but at 32 and 64 rows they lose to vLLM's decode, so a served...；`vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +31/-8 (39 lines); hunks: -30,6 +30,8; -44,14 +46,17 @@ class DecodeConfig:; symbols: DecodeConfig, widths, decode_backend, specialized_decode_config，涉及 `DecodeConfig, widths, decode_backend`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +79/-15 (94 lines); hunks: -35,6 +35,7; -90,6 +91,7 @@ def _vllm_config(**over) -> SimpleNamespace:; symbols: _vllm_config, fp4_bmm, on_mi355x
  - `vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py` modified +5/-63 (68 lines); hunks: -1,21 +1,17; -37,44 +33,6 @@ def qkv_gate_weights(wrapper):; symbols: qkv_gate_weights, pre, attend, m1c_inputs
  - `vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +29/-22 (51 lines); hunks: -11,12 +11,13 @@ layer loop. The TP all-reduces run in-kernel over peer memory.; -29,7 +30,8 @@ but at 32 and 64 rows they lose to vLLM's decode, so a served...
  - `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +31/-8 (39 lines); hunks: -30,6 +30,8; -44,14 +46,17 @@ class DecodeConfig:; symbols: DecodeConfig, widths, decode_backend, specialized_decode_config
  - `vllm/models/kimi_k3/amd/specialized_decode/runtime/guards.py` modified +8/-4 (12 lines); hunks: -13,6 +13,7; -121,8 +122,8 @@ def mla_weight_reasons(model) -> list[str]:; symbols: mla_weight_reasons, _mla_reasons
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/amd_specialized_decode/test_runtime.py
@@ -35,6 +35,7 @@
+from vllm.v1.attention.backends.registry import AttentionBackendEnum
@@ -90,6 +91,7 @@ def _vllm_config(**over) -> SimpleNamespace:
+        attention_config=SimpleNamespace(backend=None),
@@ -107,7 +109,10 @@ def _vllm_config(**over) -> SimpleNamespace:
+    monkeypatch.setenv("VLLM_ROCM_USE_AITER", "1")
+    monkeypatch.setenv("VLLM_ROCM_USE_AITER_MOE", "1")
diff -- vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py
@@ -1,21 +1,17 @@
-"""An MLA layer's decode, split where the mono kernels split it (vLLM's ops,
-the reference M1a / M1b reproduce):
+"""An MLA layer's decode between the mono kernels' halves (M1a before, M1b in
+K2 after):
-- ``pre``: qkv_a, the q / kv norms, q_b, W_UK (fp4), the query's fp8 quant,
-  this rank's KV-cache rows, the DCP query all-gather (DCP8), the output gate.
diff -- vllm/models/kimi_k3/amd/specialized_decode/README.md
@@ -11,12 +11,13 @@ layer loop. The TP all-reduces run in-kernel over peer memory.
```

- 已读文件:
  - tests: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +79/-15
  - runtime: `vllm/models/kimi_k3/amd/specialized_decode/runtime/mla.py` modified +5/-63; `vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +29/-22; `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +31/-8; `vllm/models/kimi_k3/amd/specialized_decode/runtime/guards.py` modified +8/-4; `vllm/models/kimi_k3/amd/specialized_decode/runtime/decode.py` modified +5/-1; `vllm/models/kimi_k3/amd/specialized_decode/runtime/layers.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64029 - [ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows

- 链接: https://github.com/vllm-project/vllm/pull/64029
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/__init__.py` 等 22 个文件；关联提交 `51c6dfd8c86c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 22 个文件，+7306/-577，可读 patch 9581 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows」；主要实现面是 `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py` added +1424/-0 (1424 lines); hunks: -0,0 +1,1424; symbols: MlaAttnBuild, wspec, stamp, hw_log2，涉及 `MlaAttnBuild, wspec, stamp`；`vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` modified +976/-304 (1280 lines); hunks: -3,7 +3,7; -14,16 +14,18; symbols: max_u, max_tiles, inter_lds, few_rows，涉及 `max_u, max_tiles, inter_lds`；`tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` modified +976/-34 (1010 lines); hunks: -10,6 +10,10; -60,7 +64,7 @@ def _randn(g, *shape, scale=1.0, dtype=bf):; symbols: _randn, _kda_inputs，涉及 `_randn, _kda_inputs`；`vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla.py` added +869/-0 (869 lines); hunks: -0,0 +1,869; symbols: MlaPreBuild, scratch_layout, scratch_bytes, q_heads，涉及 `MlaPreBuild, scratch_layout, scratch_bytes`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py` added +1424/-0 (1424 lines); hunks: -0,0 +1,1424; symbols: MlaAttnBuild, wspec, stamp, hw_log2
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` modified +976/-304 (1280 lines); hunks: -3,7 +3,7; -14,16 +14,18; symbols: max_u, max_tiles, inter_lds, few_rows
  - `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` modified +976/-34 (1010 lines); hunks: -10,6 +10,10; -60,7 +64,7 @@ def _randn(g, *shape, scale=1.0, dtype=bf):; symbols: _randn, _kda_inputs
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla.py` added +869/-0 (869 lines); hunks: -0,0 +1,869; symbols: MlaPreBuild, scratch_layout, scratch_bytes, q_heads
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_back.py` added +760/-0 (760 lines); hunks: -0,0 +1,760; symbols: MlaPostBuild, peer_pairs, peer_bytes, cmb_pair
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py
@@ -0,0 +1,1424 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""M1c ``mla_attn``: Kimi-K3's MLA decode attention at TP8 + DCP1, the bf16
+query (M1a ``qbf16``) against the fp8 latent cache, split over the KV: one pass
+a split, every split's partial (bf16 o, f32 LSE) for a combine (M1b's).
+One launch, ``BLOCKS`` CTAs x ``THREADS`` threads. A CTA a (head group, split):
diff -- vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py
@@ -3,7 +3,7 @@
-One launch a layer and rank, ``BLOCKS`` x ``THREADS``, S <= 8 rows (a
+One launch a layer and rank, ``BLOCKS`` x ``THREADS``, S <= 64 rows (a
@@ -14,16 +14,18 @@
-            sigmoids renormalized (IEEE 1 / sum) -> ROUTE (every rank alike)
+            sigmoids renormalized (IEEE 1 / sum) -> ROUTE (every rank alike);
+            every CTA then lays out U and its pick tiles in LDS (``load_route``)
diff -- tests/models/kimi_k3/amd_specialized_decode/test_numerics.py
@@ -10,6 +10,10 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_attn.py` added +1424/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` modified +976/-304; `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla.py` added +869/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/mla_back.py` added +760/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py` modified +610/-49; `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/back.py` modified +302/-22
  - tests: `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` modified +976/-34
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #61950 - [Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections

- 链接: https://github.com/vllm-project/vllm/pull/61950
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/kda.py`；关联提交 `de53c2deed03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+31/-3，可读 patch 56 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections」；主要实现面是 `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/kda.py` modified +31/-3 (34 lines); hunks: -73,6 +73,35; -159,17 +188,16 @@ def __init__(; symbols: _PaddedKimiGDNMergedColumnParallelLinear, __init__, weight_loader, weight_loader_v2，涉及 `_PaddedKimiGDNMergedColumnParallelLinear, __init__, weight_loader`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/kda.py` modified +31/-3 (34 lines); hunks: -73,6 +73,35; -159,17 +188,16 @@ def __init__(; symbols: _PaddedKimiGDNMergedColumnParallelLinear, __init__, weight_loader, weight_loader_v2
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -73,6 +73,35 @@
+class _PaddedKimiGDNMergedColumnParallelLinear(_KimiGDNMergedColumnParallelLinear):
+    """Merged projection with ``padding_size`` zero rows appended per rank."""
+    def __init__(self, *args, padding_size: int = 0, **kwargs) -> None:
+        super().__init__(*args, **kwargs)
+        self.padding_size = padding_size
+        if padding_size:
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +31/-3
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/kda.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #63297 - [ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend

- 链接: https://github.com/vllm-project/vllm/pull/63297
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`；关联提交 `e3eec51570d7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+75/-4，可读 patch 116 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +40/-0 (40 lines); hunks: -537,6 +537,46 @@ def test_checkpoint_leaves_the_output_and_final_state_alone...; symbols: test_checkpoint_leaves_the_output_and_final_state_alone, _slice_inputs, test_gluon_hands_checkpoint_steps_to_fused, test_unusable_checkpoint_offsets_write_nothing，涉及 `test_checkpoint_leaves_the_output_and_final_state_alone, _slice_inputs, test_gluon_hands_checkpoint_steps_to_fused`；`tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +19/-1 (20 lines); hunks: -511,7 +511,6 @@ def test_opt_in_publishes_chunk_walk_alignment(monkeypatch)...; -522,6 +521,25 @@ def test_paths_that_cannot_export_stay_opted_out(monkeypatc...; symbols: test_opt_in_publishes_chunk_walk_alignment, test_paths_that_cannot_export_stay_opted_out, test_gluon_backend_keeps_the_checkpoint, test_gluon_backend_opts_out_without_the_fused_kernel，涉及 `test_opt_in_publishes_chunk_walk_alignment, test_paths_that_cannot_export_stay_opted_out, test_gluon_backend_keeps_the_checkpoint`；`vllm/models/kimi_k3/amd/kda.py` modified +16/-3 (19 lines); hunks: -98,10 +98,18 @@ def get_state_shape(self) -> tuple[tuple[int, ...], tuple[in...; -732,7 +740,12 @@ def _prefill_conv(; symbols: get_state_shape, get_kv_cache_spec, _prefill_conv，涉及 `get_state_shape, get_kv_cache_spec, _prefill_conv`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +40/-0 (40 lines); hunks: -537,6 +537,46 @@ def test_checkpoint_leaves_the_output_and_final_state_alone...; symbols: test_checkpoint_leaves_the_output_and_final_state_alone, _slice_inputs, test_gluon_hands_checkpoint_steps_to_fused, test_unusable_checkpoint_offsets_write_nothing
  - `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +19/-1 (20 lines); hunks: -511,7 +511,6 @@ def test_opt_in_publishes_chunk_walk_alignment(monkeypatch)...; -522,6 +521,25 @@ def test_paths_that_cannot_export_stay_opted_out(monkeypatc...; symbols: test_opt_in_publishes_chunk_walk_alignment, test_paths_that_cannot_export_stay_opted_out, test_gluon_backend_keeps_the_checkpoint, test_gluon_backend_opts_out_without_the_fused_kernel
  - `vllm/models/kimi_k3/amd/kda.py` modified +16/-3 (19 lines); hunks: -98,10 +98,18 @@ def get_state_shape(self) -> tuple[tuple[int, ...], tuple[in...; -732,7 +740,12 @@ def _prefill_conv(; symbols: get_state_shape, get_kv_cache_spec, _prefill_conv
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -537,6 +537,46 @@ def test_checkpoint_leaves_the_output_and_final_state_alone() -> None:
+def _slice_inputs(inp: dict, start: int, end: int, h0: torch.Tensor) -> dict:
+    """Tokens ``[start, end)`` of a one-sequence fixture, resumed from ``h0``."""
+    part = dict(inp)
+    for key in ("q", "k", "v", "raw_g", "raw_beta"):
+        part[key] = inp[key][:, start:end].contiguous()
+    part["h0"] = h0
diff -- tests/models/kimi_k3/test_amd_kda_checkpoint.py
@@ -511,7 +511,6 @@ def test_opt_in_publishes_chunk_walk_alignment(monkeypatch) -> None:
-        ("kda_prefill_backend", "gluon"),
@@ -522,6 +521,25 @@ def test_paths_that_cannot_export_stay_opted_out(monkeypatch, attr, value) -> No
+def test_gluon_backend_keeps_the_checkpoint(monkeypatch) -> None:
+    # AITER's chunk_kda cannot export the snapshot, but the steps that carry
+    # one run on the fused kernel, which this module already requires.
+    spec = _spec_for(monkeypatch, kda_prefill_backend="gluon")
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -98,10 +98,18 @@ def get_state_shape(self) -> tuple[tuple[int, ...], tuple[int, ...]]:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +40/-0; `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +19/-1
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +16/-3
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64619 - [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub

- 链接: https://github.com/vllm-project/vllm/pull/64619
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`；关联提交 `daccf69eb222`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`；技术摘要: 覆盖「[CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +1/-0 (1 lines); hunks: -53,6 +53,7; symbols: _StubSpeculativeConfig, __init__，涉及 `_StubSpeculativeConfig, __init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +1/-0 (1 lines); hunks: -53,6 +53,7; symbols: _StubSpeculativeConfig, __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_checkpoint.py
@@ -53,6 +53,7 @@
+    enable_adaptive_verification = False
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53011 - [Bugfix] Avoid eager torch.compile in Kimi K2.5 vision helper

- 链接: https://github.com/vllm-project/vllm/pull/53011
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `604b961640ee`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-20，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Avoid eager torch.compile in Kimi K2.5 vision helper」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Bugfix] Avoid eager torch.compile in Kimi K2.5 vision helper」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +0/-20 (20 lines); hunks: -40,7 +40,6; -63,25 +62,6 @@ def _apply_rope_input_validation(x, freqs_cis):; symbols: _apply_rope_input_validation, get_rope_shape_decorate, wrapper, get_rope_shape，涉及 `_apply_rope_input_validation, get_rope_shape_decorate, wrapper`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +0/-20 (20 lines); hunks: -40,7 +40,6; -63,25 +62,6 @@ def _apply_rope_input_validation(x, freqs_cis):; symbols: _apply_rope_input_validation, get_rope_shape_decorate, wrapper, get_rope_shape
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -40,7 +40,6 @@
-from vllm.platforms import current_platform
@@ -63,25 +62,6 @@ def _apply_rope_input_validation(x, freqs_cis):
-def get_rope_shape_decorate(func):
-    _get_rope_shape_first_call_flag = set()
-    def wrapper(org, interpolation_mode, shape):
-        key = (org.requires_grad, torch.is_grad_enabled(), interpolation_mode)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +0/-20
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #64158 - [ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model

- 链接: https://github.com/vllm-project/vllm/pull/64158
- 状态/时间: merged / 2026-10-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/model.py`；关联提交 `b71c1d5f14e5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+18/-0，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/model.py`；技术摘要: 覆盖「[ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model」；主要实现面是 `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_qb_uk_fold.py` modified +13/-0 (13 lines); hunks: -93,3 +93,16 @@ def test_fold_through_aiter_gemm(num_tokens: int) -> None:; symbols: test_fold_through_aiter_gemm, test_root_model_builds_the_fold，涉及 `test_fold_through_aiter_gemm, test_root_model_builds_the_fold`；`vllm/models/kimi_k3/amd/model.py` modified +5/-0 (5 lines); hunks: -252,3 +252,8 @@ def get_mamba_state_copy_func(cls):; symbols: get_mamba_state_copy_func, load_weights, process_weights_after_loading，涉及 `get_mamba_state_copy_func, load_weights, process_weights_after_loading`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_qb_uk_fold.py` modified +13/-0 (13 lines); hunks: -93,3 +93,16 @@ def test_fold_through_aiter_gemm(num_tokens: int) -> None:; symbols: test_fold_through_aiter_gemm, test_root_model_builds_the_fold
  - `vllm/models/kimi_k3/amd/model.py` modified +5/-0 (5 lines); hunks: -252,3 +252,8 @@ def get_mamba_state_copy_func(cls):; symbols: get_mamba_state_copy_func, load_weights, process_weights_after_loading
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_qb_uk_fold.py
@@ -93,3 +93,16 @@ def test_fold_through_aiter_gemm(num_tokens: int) -> None:
+def test_root_model_builds_the_fold() -> None:
+    """The loader calls only the root model's post-load hook, so
+    KimiK3ForConditionalGeneration must forward it to the text model, whose hook
+    builds each MLA wrapper's W_fold (else _fused_decode asserts at DCP1)."""
+    from unittest.mock import MagicMock
+    from vllm.models.kimi_k3.amd.model import KimiK3ForConditionalGeneration
diff -- vllm/models/kimi_k3/amd/model.py
@@ -252,3 +252,8 @@ def get_mamba_state_copy_func(cls):
+    def process_weights_after_loading(self) -> None:
+        # The loader calls only the root model's hook; forward it so the text
+        # model's MLA layers build their folded q_b_proj / W_UK weight.
+        self.language_model.process_weights_after_loading()
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_qb_uk_fold.py` modified +13/-0
  - runtime: `vllm/models/kimi_k3/amd/model.py` modified +5/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_qb_uk_fold.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63989 - [Bugfix][Kimi-K3] Reserve KDA prefill workspace before profiling

- 链接: https://github.com/vllm-project/vllm/pull/63989
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `e96b490b1204`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+16/-1，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Reserve KDA prefill workspace before profiling」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Reserve KDA prefill workspace before profiling」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +16/-1 (17 lines); hunks: -73,7 +73,10; -857,6 +860,18 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +16/-1 (17 lines); hunks: -73,7 +73,10; -857,6 +860,18 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -73,7 +73,10 @@
-from vllm.v1.worker.workspace import current_workspace_manager
+from vllm.v1.worker.workspace import (
+    current_workspace_manager,
+    is_workspace_manager_initialized,
+)
@@ -857,6 +860,18 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +16/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/kda.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #63409 - [ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel

- 链接: https://github.com/vllm-project/vllm/pull/63409
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/mla.py`；关联提交 `bb7ea479c6e1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+94/-11，可读 patch 174 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/mla.py`；技术摘要: 覆盖「[ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel」；主要实现面是 `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +67/-4 (71 lines); hunks: -1,7 +1,8; -91,9 +92,7 @@ def attention_output(path, output_shape):; symbols: attention_output, test_fused_decode_feeds_zero_positions_to_kernel，涉及 `attention_output, test_fused_decode_feeds_zero_positions_to_kernel`；`vllm/models/kimi_k3/amd/mla.py` modified +27/-7 (34 lines); hunks: -7,6 +7,7; -46,6 +47,18 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_decode, forward，涉及 `__init__, _fused_decode, forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +67/-4 (71 lines); hunks: -1,7 +1,8; -91,9 +92,7 @@ def attention_output(path, output_shape):; symbols: attention_output, test_fused_decode_feeds_zero_positions_to_kernel
  - `vllm/models/kimi_k3/amd/mla.py` modified +27/-7 (34 lines); hunks: -7,6 +7,7; -46,6 +47,18 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_decode, forward
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_mla_direct_return.py
@@ -1,7 +1,8 @@
-from types import SimpleNamespace
+import sys
+from types import ModuleType, SimpleNamespace
@@ -91,9 +92,7 @@ def attention_output(path, output_shape):
-        _fused_decode=lambda q, kv, pe, pos, shape, *args: attention_output(
-            "fused", shape
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -7,6 +7,7 @@
+from vllm.config import get_current_vllm_config
@@ -46,6 +47,18 @@ def __init__(self, *args, **kwargs) -> None:
+        # Positions fed to the fused kernel's identity RoPE; see _fused_decode.
+        # Allocated once here so every captured CUDA graph shares one zeroed
+        # buffer instead of capturing a memset per layer.
+        zero_positions = None
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +67/-4
  - runtime: `vllm/models/kimi_k3/amd/mla.py` modified +27/-7
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_mla_direct_return.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60110 - [ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query

- 链接: https://github.com/vllm-project/vllm/pull/60110
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`；关联提交 `6aa70c4beca4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+228/-52，可读 patch 361 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/mla.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query」；主要实现面是 `vllm/models/kimi_k3/amd/mla.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/mla.py` modified +127/-52 (179 lines); hunks: -8,12 +8,16; -42,6 +46,17 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_qk_prep_supported, _normalize_q_kv, _compute_w_fold，涉及 `__init__, _fused_qk_prep_supported, _normalize_q_kv`；`tests/models/kimi_k3/test_amd_qb_uk_fold.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: _weights, _reference, _split_fold_output, test_fold_row_layout，涉及 `_weights, _reference, _split_fold_output`；`vllm/models/kimi_k3/amd/linear.py` modified +5/-0 (5 lines); hunks: -1171,6 +1171,11 @@ def get_mamba_state_copy_func(; symbols: get_mamba_state_copy_func, process_weights_after_loading, compute_logits，涉及 `get_mamba_state_copy_func, process_weights_after_loading, compute_logits`；`tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0 (1 lines); hunks: -90,6 +90,7 @@ def attention_output(path, output_shape):; symbols: attention_output，涉及 `attention_output`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/mla.py` modified +127/-52 (179 lines); hunks: -8,12 +8,16; -42,6 +46,17 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_qk_prep_supported, _normalize_q_kv, _compute_w_fold
  - `tests/models/kimi_k3/test_amd_qb_uk_fold.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: _weights, _reference, _split_fold_output, test_fold_row_layout
  - `vllm/models/kimi_k3/amd/linear.py` modified +5/-0 (5 lines); hunks: -1171,6 +1171,11 @@ def get_mamba_state_copy_func(; symbols: get_mamba_state_copy_func, process_weights_after_loading, compute_logits
  - `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0 (1 lines); hunks: -90,6 +90,7 @@ def attention_output(path, output_shape):; symbols: attention_output
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -8,12 +8,16 @@
+from vllm.model_executor.layers.attention.mla_attention import split_kv_b_proj
-from vllm.model_executor.layers.linear import KimiK3MergedQKVGateLinear
+from vllm.model_executor.layers.linear import (
+    KimiK3MergedQKVGateLinear,
+    UnquantizedLinearMethod,
+)
diff -- tests/models/kimi_k3/test_amd_qb_uk_fold.py
@@ -0,0 +1,95 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The folded q_b_proj + W_UK decode-query weight of the AMD Kimi-K3 MLA wrapper."""
+import pytest
+import torch
+from vllm.models.kimi_k3.amd.mla import KimiK3MultiHeadLatentAttentionWrapper
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -1171,6 +1171,11 @@ def get_mamba_state_copy_func(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/mla.py` modified +127/-52; `vllm/models/kimi_k3/amd/linear.py` modified +5/-0
  - tests: `tests/models/kimi_k3/test_amd_qb_uk_fold.py` added +95/-0; `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63342 - [ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d

- 链接: https://github.com/vllm-project/vllm/pull/63342
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`；关联提交 `f8f7634cb43a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+124/-3，可读 patch 180 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py` modified +72/-1 (73 lines); hunks: -7,7 +7,10; -161,3 +164,71 @@ def test_fused_split_qkv_conv1d_matches_reference(seqlens,...; symbols: test_fused_split_qkv_conv1d_matches_reference, test_prebuilt_block_m_128_schedule, run，涉及 `test_fused_split_qkv_conv1d_matches_reference, test_prebuilt_block_m_128_schedule, run`；`vllm/models/kimi_k3/amd/kda_metadata.py` modified +47/-0 (47 lines); hunks: -19,6 +19,7; -33,6 +34,9; symbols: _chunk_metadata_kernel, prepare_chunk_metadata_device, _to_device, build_conv1d_chunk_schedule，涉及 `_chunk_metadata_kernel, prepare_chunk_metadata_device, _to_device`；`vllm/models/kimi_k3/amd/kda.py` modified +5/-2 (7 lines); hunks: -45,7 +45,10; -611,7 +614,7 @@ def _forward(; symbols: _forward，涉及 `_forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py` modified +72/-1 (73 lines); hunks: -7,7 +7,10; -161,3 +164,71 @@ def test_fused_split_qkv_conv1d_matches_reference(seqlens,...; symbols: test_fused_split_qkv_conv1d_matches_reference, test_prebuilt_block_m_128_schedule, run
  - `vllm/models/kimi_k3/amd/kda_metadata.py` modified +47/-0 (47 lines); hunks: -19,6 +19,7; -33,6 +34,9; symbols: _chunk_metadata_kernel, prepare_chunk_metadata_device, _to_device, build_conv1d_chunk_schedule
  - `vllm/models/kimi_k3/amd/kda.py` modified +5/-2 (7 lines); hunks: -45,7 +45,10; -611,7 +614,7 @@ def _forward(; symbols: _forward
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_fused_conv1d.py
@@ -7,7 +7,10 @@
-from vllm.v1.attention.backends.utils import NULL_BLOCK_ID
+from vllm.v1.attention.backends.utils import (
+    NULL_BLOCK_ID,
+    compute_causal_conv1d_metadata,
+)
@@ -161,3 +164,71 @@ def test_fused_split_qkv_conv1d_matches_reference(seqlens, has_initial_state, bl
diff -- vllm/models/kimi_k3/amd/kda_metadata.py
@@ -19,6 +19,7 @@
+from vllm.utils.torch_utils import PIN_MEMORY
@@ -33,6 +34,9 @@
+# block_m of the fused prefill conv1d in kda.py; shared GDN builder prebuilds only 8
+PREFILL_CONV_BLOCK_M = 128
@@ -95,6 +99,33 @@ def prepare_chunk_metadata_device(
+def _to_device(t: torch.Tensor, device: torch.device) -> torch.Tensor:
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -45,7 +45,10 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py` modified +72/-1
  - runtime: `vllm/models/kimi_k3/amd/kda_metadata.py` modified +47/-0; `vllm/models/kimi_k3/amd/kda.py` modified +5/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62141 - [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355

- 链接: https://github.com/vllm-project/vllm/pull/62141
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_prefix_cache.py`；关联提交 `6fe3d447ac64`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+267/-8，可读 patch 374 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_prefix_cache.py`；技术摘要: 覆盖「[CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355」；主要实现面是 `tests/models/kimi_k3/test_prefix_cache.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_prefix_cache.py` modified +8/-4 (12 lines); hunks: -52,8 +52,12; -173,7 +177,7 @@ def num_gpus(self) -> int:; symbols: num_gpus, _known_failure, mooncake_store，涉及 `num_gpus, _known_failure, mooncake_store`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_prefix_cache.py` modified +8/-4 (12 lines); hunks: -52,8 +52,12; -173,7 +177,7 @@ def num_gpus(self) -> int:; symbols: num_gpus, _known_failure, mooncake_store
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_prefix_cache.py
@@ -52,8 +52,12 @@
-    not current_platform.is_device_capability_family(100),
-    reason="Kimi-K3 NVIDIA kernels require the SM100 family",
+    not (
+        current_platform.supports_mx()
+        if current_platform.is_rocm()
+        else current_platform.is_device_capability_family(100)
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_prefix_cache.py` modified +8/-4
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_minimax_m3.py`, `tests/models/kimi_k3/test_prefix_cache.py`, `tests/v1/e2e/test_replayssm_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63638 - [Perf][Kimi K3] Opt-in KV-balanced FP8 MLA decode for agentic workloads

- 链接: https://github.com/vllm-project/vllm/pull/63638
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kv_balanced_mla.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/__init__.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/backend.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/decode.py` 等 7 个文件；关联提交 `6597ceafbc50`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+6553/-0，可读 patch 1684 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Kimi K3] Opt-in KV-balanced FP8 MLA decode for agentic workloads」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py`, `tests/models/kimi_k3/test_kv_balanced_mla.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py`；技术摘要: 覆盖「[Perf][Kimi K3] Opt-in KV-balanced FP8 MLA decode for agentic workloads」；主要实现面是 `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py`, `tests/models/kimi_k3/test_kv_balanced_mla.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py` added +4882/-0 (4882 lines)；`tests/models/kimi_k3/test_kv_balanced_mla.py` added +446/-0 (446 lines); hunks: -0,0 +1,446; symbols: test_kv_balanced_backend_is_registered_and_opt_in, test_kv_balanced_backend_rejects_unsupported, reasons, test_kv_balanced_impl_runs_the_kernel，涉及 `test_kv_balanced_backend_is_registered_and_opt_in, test_kv_balanced_backend_rejects_unsupported, reasons`；`vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py` added +423/-0 (423 lines); hunks: -0,0 +1,423; symbols: get_mla_decode_arch, select_mla_decode_tilers, compute_q_tile_layout, get_mla_decode_fold_sq_factor，涉及 `get_mla_decode_arch, select_mla_decode_tilers, compute_q_tile_layout`；`vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py` added +377/-0 (377 lines); hunks: -0,0 +1,377; symbols: query_tiles, max_planned_requests, workspace_bytes, work_list_len，涉及 `query_tiles, max_planned_requests, workspace_bytes`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py` added +4882/-0 (4882 lines)
  - `tests/models/kimi_k3/test_kv_balanced_mla.py` added +446/-0 (446 lines); hunks: -0,0 +1,446; symbols: test_kv_balanced_backend_is_registered_and_opt_in, test_kv_balanced_backend_rejects_unsupported, reasons, test_kv_balanced_impl_runs_the_kernel
  - `vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py` added +423/-0 (423 lines); hunks: -0,0 +1,423; symbols: get_mla_decode_arch, select_mla_decode_tilers, compute_q_tile_layout, get_mla_decode_fold_sq_factor
  - `vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py` added +377/-0 (377 lines); hunks: -0,0 +1,377; symbols: query_tiles, max_planned_requests, workspace_bytes, work_list_len
  - `vllm/models/kimi_k3/nvidia/kv_balanced_mla/decode.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: KvBalancedDecode, __init__, _buffers, _core
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kv_balanced_mla.py
@@ -0,0 +1,446 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The Kimi K3 KV-balanced MLA decode against an FP32 reference."""
+import math
+from types import SimpleNamespace
+import pytest
diff -- vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py
@@ -0,0 +1,423 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# ruff: noqa
+# Vendored from TokenSpeed MLA 2.0.3 (tokenspeed_mla/mla_helpers.py, MIT, see below)
+# for the Kimi K3 KV-balanced MLA decode; adds MLAWorkListTileScheduler.
+#
diff -- vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py
@@ -0,0 +1,377 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kv_balanced_mla/kernel.py` added +4882/-0; `vllm/models/kimi_k3/nvidia/kv_balanced_mla/helpers.py` added +423/-0; `vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py` added +377/-0; `vllm/models/kimi_k3/nvidia/kv_balanced_mla/decode.py` added +228/-0; `vllm/models/kimi_k3/nvidia/kv_balanced_mla/backend.py` added +189/-0; `vllm/models/kimi_k3/nvidia/kv_balanced_mla/__init__.py` added +5/-0
  - tests: `tests/models/kimi_k3/test_kv_balanced_mla.py` added +446/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kv_balanced_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #61527 - [Kimi-K3] Route the fp8 chunked-context K/V pack through FlashInfer where it has a fused kernel

- 链接: https://github.com/vllm-project/vllm/pull/61527
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`；关联提交 `4eb5df80389a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+72/-6，可读 patch 152 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Route the fp8 chunked-context K/V pack through FlashInfer where it has a fused kernel」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`；技术摘要: 覆盖「[Kimi-K3] Route the fp8 chunked-context K/V pack through FlashInfer where it has a fused kernel」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +26/-0 (26 lines); hunks: -24,6 +24,9; -212,6 +215,29 @@ def fused_mla_kv_concat_quant_fp8(; symbols: fused_mla_key_concat_kv_cache_insert, fused_mla_kv_concat_quant_fp8, fused_mla_kv_pack_quant_fp8, fused_mla_decode_q_concat_kv_cache_insert，涉及 `fused_mla_key_concat_kv_cache_insert, fused_mla_kv_concat_quant_fp8, fused_mla_kv_pack_quant_fp8`；`vllm/models/kimi_k3/nvidia/mla.py` modified +12/-6 (18 lines); hunks: -83,7 +83,7; -797,9 +797,11 @@ def _fused_mla_kv_concat(; symbols: _fused_mla_kv_concat, _compute_prefill_context, run_chunk，涉及 `_fused_mla_kv_concat, _compute_prefill_context, run_chunk`；`tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +24/-0 (24 lines); hunks: -11,9 +11,11; -308,3 +310,25 @@ def test_decode_epilogue_row_split_boundary(num_tokens: int...; symbols: test_decode_epilogue_row_split_boundary, test_context_kv_pack_flashinfer_route_is_byte_exact，涉及 `test_decode_epilogue_row_split_boundary, test_context_kv_pack_flashinfer_route_is_byte_exact`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +26/-0 (26 lines); hunks: -24,6 +24,9; -212,6 +215,29 @@ def fused_mla_kv_concat_quant_fp8(; symbols: fused_mla_key_concat_kv_cache_insert, fused_mla_kv_concat_quant_fp8, fused_mla_kv_pack_quant_fp8, fused_mla_decode_q_concat_kv_cache_insert
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +12/-6 (18 lines); hunks: -83,7 +83,7; -797,9 +797,11 @@ def _fused_mla_kv_concat(; symbols: _fused_mla_kv_concat, _compute_prefill_context, run_chunk
  - `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +24/-0 (24 lines); hunks: -11,9 +11,11; -308,3 +310,25 @@ def test_decode_epilogue_row_split_boundary(num_tokens: int...; symbols: test_decode_epilogue_row_split_boundary, test_context_kv_pack_flashinfer_route_is_byte_exact
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py
@@ -24,6 +24,9 @@
+from vllm.platforms import current_platform
+from vllm.utils.flashinfer import has_flashinfer_concat_mla_kv_quant_fp8
@@ -212,6 +215,29 @@ def fused_mla_kv_concat_quant_fp8(
+def fused_mla_kv_pack_quant_fp8(
+    kv_nope: torch.Tensor,  # [T, H, nope + v] bf16/fp16, the kv_b_proj output
+    k_pe: torch.Tensor,  # [T, rope] or [T, 1, rope], kv_nope's dtype or fp8
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -83,7 +83,7 @@
-    fused_mla_kv_concat_quant_fp8,
+    fused_mla_kv_pack_quant_fp8,
@@ -797,9 +797,11 @@ def _fused_mla_kv_concat(
-        k_nope, v = kv_nope.split([self.qk_nope_head_dim, self.v_head_dim], dim=-1)
-            return fused_mla_kv_concat_quant_fp8(k_nope, k_pe, v)
+            return fused_mla_kv_pack_quant_fp8(
diff -- tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py
@@ -11,9 +11,11 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +26/-0; `vllm/models/kimi_k3/nvidia/mla.py` modified +12/-6
  - tests: `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +24/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63531 - [XPU] Fix Kimi-Linear model dispatch

- 链接: https://github.com/vllm-project/vllm/pull/63531
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/__init__.py`；关联提交 `2a2717d9b8e4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-1，可读 patch 33 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Fix Kimi-Linear model dispatch」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/__init__.py`；技术摘要: 覆盖「[XPU] Fix Kimi-Linear model dispatch」；主要实现面是 `vllm/models/kimi_k3/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/__init__.py` modified +7/-0 (7 lines); hunks: -5,6 +5,9; -24,6 +27,10。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/__init__.py` modified +7/-0 (7 lines); hunks: -5,6 +5,9; -24,6 +27,10
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/__init__.py
@@ -5,6 +5,9 @@
+On XPU, Kimi-Linear uses the reference KDA/MLA path in ``amd/linear.py``
+instead of the NVIDIA-specific fused attention kernels.
@@ -24,6 +27,10 @@
+elif current_platform.is_xpu():
+    from .amd.linear import KimiLinearForCausalLM  # type: ignore[assignment]
+    from .nvidia.model import KimiK3ForConditionalGeneration
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/__init__.py` modified +7/-0
- 验证与风险: diff 自带测试面 `tests/models/test_registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63449 - [CI][Kimi-K3] Expect no trailing-block drop in DSpark resend tests

- 链接: https://github.com/vllm-project/vllm/pull/63449
- 状态/时间: merged / 2026-10-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_prefix_cache.py`；关联提交 `1bd56eaef38d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-12，可读 patch 51 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kimi-K3] Expect no trailing-block drop in DSpark resend tests」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_prefix_cache.py`；技术摘要: 覆盖「[CI][Kimi-K3] Expect no trailing-block drop in DSpark resend tests」；主要实现面是 `tests/models/kimi_k3/test_prefix_cache.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_prefix_cache.py` modified +10/-12 (22 lines); hunks: -378,7 +378,7 @@ def _format(turns: list[Turn]) -> str:; -391,8 +391,8 @@ def _check_resend_reuses_prompt_checkpoint(; symbols: _format, _check_resend_reuses_prompt_checkpoint, test_dspark_exact_resend_reuses_prompt_checkpoint，涉及 `_format, _check_resend_reuses_prompt_checkpoint, test_dspark_exact_resend_reuses_prompt_checkpoint`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_prefix_cache.py` modified +10/-12 (22 lines); hunks: -378,7 +378,7 @@ def _format(turns: list[Turn]) -> str:; -391,8 +391,8 @@ def _check_resend_reuses_prompt_checkpoint(; symbols: _format, _check_resend_reuses_prompt_checkpoint, test_dspark_exact_resend_reuses_prompt_checkpoint
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_prefix_cache.py
@@ -378,7 +378,7 @@ def _format(turns: list[Turn]) -> str:
-    """Resends reuse the Mamba checkpoint and its companion EAGLE attention proof."""
+    """Resends reuse the last prompt checkpoint before the final token."""
@@ -391,8 +391,8 @@ def _check_resend_reuses_prompt_checkpoint(
-    # EAGLE's dropped hash unit already leaves tokens to recompute on resend.
-    expected = (prompt_len // 128 - 1) * 128
+    # DSpark keeps the trailing hash unit, unlike EAGLE.
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_prefix_cache.py` modified +10/-12
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_prefix_cache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63045 - [Kimi K3] KDA RecoverSSM: CuTe verify and commit kernels, records outside the KV cache

- 链接: https://github.com/vllm-project/vllm/pull/63045
- 状态/时间: merged / 2026-10-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/kimi_k3/test_recoverssm_kernels.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py` 等 13 个文件；关联提交 `ae065918640a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+2957/-212，可读 patch 3514 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3] KDA RecoverSSM: CuTe verify and commit kernels, records outside the KV cache」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_recoverssm_kernels.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py`；技术摘要: 覆盖「[Kimi K3] KDA RecoverSSM: CuTe verify and commit kernels, records outside the KV cache」；主要实现面是 `tests/models/kimi_k3/test_recoverssm_kernels.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py`, `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_recoverssm_kernels.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: _pages, _records, _clone_records, _clone_pages，涉及 `_pages, _records, _clone_records`；`vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: state_sw128_layout, bulk_load, arrive_expect, arrive，涉及 `state_sw128_layout, bulk_load, arrive_expect`；`vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py` added +526/-0 (526 lines); hunks: -0,0 +1,526; symbols: state_smem_layout, tmem_alloc, tmem_relinquish, tmem_dealloc，涉及 `state_smem_layout, tmem_alloc, tmem_relinquish`；`vllm/models/kimi_k3/nvidia/recoverssm/kernels.py` added +374/-0 (374 lines); hunks: -0,0 +1,374; symbols: can_use_cute_recoverssm, _architecture, _ctas, _compile_verify，涉及 `can_use_cute_recoverssm, _architecture, _ctas`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_recoverssm_kernels.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: _pages, _records, _clone_records, _clone_pages
  - `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py` added +722/-0 (722 lines); hunks: -0,0 +1,722; symbols: state_sw128_layout, bulk_load, arrive_expect, arrive
  - `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py` added +526/-0 (526 lines); hunks: -0,0 +1,526; symbols: state_smem_layout, tmem_alloc, tmem_relinquish, tmem_dealloc
  - `vllm/models/kimi_k3/nvidia/recoverssm/kernels.py` added +374/-0 (374 lines); hunks: -0,0 +1,374; symbols: can_use_cute_recoverssm, _architecture, _ctas, _compile_verify
  - `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/commit.py` added +292/-0 (292 lines); hunks: -0,0 +1,292; symbols: store_bulk, bulk_read_done, bulk_done, proxy_fence
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_recoverssm_kernels.py
@@ -0,0 +1,722 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The CuTe KDA RecoverSSM verify and state commit against the Triton reference
+(``causal_conv1d_update`` + ``kda_recoverssm_verify``, and the Triton commit), on
+Mamba page views as vLLM binds them (one padded page per slot holding the conv
+and SSM state) and per-layer verify records indexed by batch row."""
diff -- vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py
@@ -0,0 +1,722 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""KDA RecoverSSM verify with the fused short convolution on the fifth-generation
+tensor cores, warp specialized (the dim-first conv state layout).
+The math and the per-item MMA / solve are those of ``verify.py`` (read its
+docstring first). What differs is how an item's inputs reach the CTA:
diff -- vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py
@@ -0,0 +1,526 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_recoverssm_kernels.py` added +722/-0; `tests/models/kimi_k3/test_kda_metadata.py` modified +48/-3
  - runtime: `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify_ws.py` added +722/-0; `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/verify.py` added +526/-0; `vllm/models/kimi_k3/nvidia/recoverssm/kernels.py` added +374/-0; `vllm/models/kimi_k3/nvidia/recoverssm/cutedsl/commit.py` added +292/-0; `vllm/models/kimi_k3/nvidia/kda.py` modified +193/-66; `vllm/models/kimi_k3/nvidia/ops/recoverssm.py` modified +55/-71
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/kimi_k3/test_recoverssm_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #63031 - [ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode

- 链接: https://github.com/vllm-project/vllm/pull/63031
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`；关联提交 `098eb89ea45c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+111/-7，可读 patch 171 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`；技术摘要: 覆盖「[ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode」；主要实现面是 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +88/-4 (92 lines); hunks: -8,7 +8,15; -137,8 +145,77 @@ def test_an_unknown_backend_is_refused():; symbols: test_an_unknown_backend_is_refused, test_supported_config_is_accepted, supported_vllm_config, test_moriio_consumer_is_supported，涉及 `test_an_unknown_backend_is_refused, test_supported_config_is_accepted, supported_vllm_config`；`vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +11/-1 (12 lines); hunks: -89,6 +89,7 @@ def unsupported(vllm_config) -> list[str]:; -103,7 +104,16 @@ def unsupported(vllm_config) -> list[str]:; symbols: unsupported，涉及 `unsupported`；`vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +6/-2 (8 lines); hunks: -31,12 +31,16 @@ TP8 on MI355X with all 256 CUs, decode context parallel 1 or...。
- 代码 diff 细节:
  - `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +88/-4 (92 lines); hunks: -8,7 +8,15; -137,8 +145,77 @@ def test_an_unknown_backend_is_refused():; symbols: test_an_unknown_backend_is_refused, test_supported_config_is_accepted, supported_vllm_config, test_moriio_consumer_is_supported
  - `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +11/-1 (12 lines); hunks: -89,6 +89,7 @@ def unsupported(vllm_config) -> list[str]:; -103,7 +104,16 @@ def unsupported(vllm_config) -> list[str]:; symbols: unsupported
  - `vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +6/-2 (8 lines); hunks: -31,12 +31,16 @@ TP8 on MI355X with all 256 CUs, decode context parallel 1 or...
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/amd_specialized_decode/test_runtime.py
@@ -8,7 +8,15 @@
-from vllm.config import CompilationMode, CUDAGraphMode
+from vllm.config import (
+    CompilationMode,
+    CUDAGraphMode,
+    KVTransferConfig,
+    ModelConfig,
diff -- vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py
@@ -89,6 +89,7 @@ def unsupported(vllm_config) -> list[str]:
+    kv = vllm_config.kv_transfer_config
@@ -103,7 +104,16 @@ def unsupported(vllm_config) -> list[str]:
-        (vllm_config.kv_transfer_config is not None, "KV transfer connectors"),
+        # MoRIIO consumers finish loads before execution, without per-layer hooks.
+        (
+            kv is not None
diff -- vllm/models/kimi_k3/amd/specialized_decode/README.md
@@ -31,12 +31,16 @@ TP8 on MI355X with all 256 CUs, decode context parallel 1 or 8, speculative
```

- 已读文件:
  - tests: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` modified +88/-4
  - runtime: `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py` modified +11/-1; `vllm/models/kimi_k3/amd/specialized_decode/README.md` modified +6/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58743 - [ROCm][Kimi-K3] Support BF16 KDA recurrent state

- 链接: https://github.com/vllm-project/vllm/pull/58743
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py` 等 7 个文件；关联提交 `dc05b1455636`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+304/-91，可读 patch 853 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Support BF16 KDA recurrent state」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Support BF16 KDA recurrent state」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +147/-37 (184 lines); hunks: -447,13 +447,13 @@ def test_accepts_chunk_metadata_from_the_attention_builder(; -470,9 +470,13 @@ def _prefix_inputs(inp: dict, seq: int, num_tokens: int) ->...; symbols: test_accepts_chunk_metadata_from_the_attention_builder, _checkpoint_buffer, _prefix_inputs, _run_with_checkpoints，涉及 `test_accepts_chunk_metadata_from_the_attention_builder, _checkpoint_buffer, _prefix_inputs`；`tests/models/kimi_k3/test_amd_kda_decode.py` modified +58/-1 (59 lines); hunks: -14,6 +14,8; -335,7 +337,11 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:; symbols: test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading，涉及 `test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading`；`vllm/models/kimi_k3/amd/kda.py` modified +14/-4 (18 lines); hunks: -78,7 +78,9 @@ def get_state_dtype(self) -> tuple[torch.dtype, torch.dtype]:; -192,15 +194,19 @@ def __init__(; symbols: get_state_dtype, get_state_shape, __init__，涉及 `get_state_dtype, get_state_shape, __init__`；`vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +5/-4 (9 lines); hunks: -86,9 +86,9 @@ def chunk_kda_prefill(; -231,6 +231,7 @@ def chunk_kda_prefill(; symbols: chunk_kda_prefill，涉及 `chunk_kda_prefill`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +147/-37 (184 lines); hunks: -447,13 +447,13 @@ def test_accepts_chunk_metadata_from_the_attention_builder(; -470,9 +470,13 @@ def _prefix_inputs(inp: dict, seq: int, num_tokens: int) ->...; symbols: test_accepts_chunk_metadata_from_the_attention_builder, _checkpoint_buffer, _prefix_inputs, _run_with_checkpoints
  - `tests/models/kimi_k3/test_amd_kda_decode.py` modified +58/-1 (59 lines); hunks: -14,6 +14,8; -335,7 +337,11 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:; symbols: test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading
  - `vllm/models/kimi_k3/amd/kda.py` modified +14/-4 (18 lines); hunks: -78,7 +78,9 @@ def get_state_dtype(self) -> tuple[torch.dtype, torch.dtype]:; -192,15 +194,19 @@ def __init__(; symbols: get_state_dtype, get_state_shape, __init__
  - `vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +5/-4 (9 lines); hunks: -86,9 +86,9 @@ def chunk_kda_prefill(; -231,6 +231,7 @@ def chunk_kda_prefill(; symbols: chunk_kda_prefill
  - `vllm/models/kimi_k3/amd/linear.py` modified +3/-1 (4 lines); hunks: -1140,7 +1140,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -447,13 +447,13 @@ def test_accepts_chunk_metadata_from_the_attention_builder(
-def _checkpoint_buffer(rows: int) -> torch.Tensor:
+def _checkpoint_buffer(rows: int, dtype: torch.dtype = torch.float32) -> torch.Tensor:
-        dtype=torch.float32,
+        dtype=dtype,
@@ -470,9 +470,13 @@ def _prefix_inputs(inp: dict, seq: int, num_tokens: int) -> dict:
-    inp: dict, offsets: list[int], rows: int | None = None, **kw
diff -- tests/models/kimi_k3/test_amd_kda_decode.py
@@ -14,6 +14,8 @@
+from functools import partial
@@ -335,7 +337,11 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:
-def test_decode_weights_staged_after_loading(dist_init) -> None:
+@pytest.mark.parametrize("state_dtype", ["float32", "bfloat16"])
+@pytest.mark.parametrize("aiter_available", [False, True])
+def test_decode_weights_staged_after_loading(
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -78,7 +78,9 @@ def get_state_dtype(self) -> tuple[torch.dtype, torch.dtype]:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +147/-37; `tests/models/kimi_k3/test_amd_kda_decode.py` modified +58/-1
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +14/-4; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +5/-4; `vllm/models/kimi_k3/amd/linear.py` modified +3/-1; `vllm/models/kimi_k3/amd/ops/kda_chunk.py` modified +2/-2; `vllm/models/kimi_k3/amd/ops/kda_decode.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62507 - [Bugfix][Frontend][Kimi K3] Fix Kimi K3 XTML marker leakage in responses API

- 链接: https://github.com/vllm-project/vllm/pull/62507
- 状态/时间: merged / 2026-10-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/tool_use/test_kimi_k3_tool_parser.py`；关联提交 `2de0531d8152`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+26/-12，可读 patch 102 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Frontend][Kimi K3] Fix Kimi K3 XTML marker leakage in responses API」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/tool_use/test_kimi_k3_tool_parser.py`, `tests/reasoning/test_kimi_k3_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix][Frontend][Kimi K3] Fix Kimi K3 XTML marker leakage in responses API」；主要实现面是 `tests/tool_use/test_kimi_k3_tool_parser.py`, `tests/reasoning/test_kimi_k3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +11/-7 (18 lines); hunks: -449,15 +449,20 @@ def test_delegating_parser_tool_choice_none_strips_xtml_an...; -469,8 +474,7 @@ def test_adjust_request_required_uses_xtml_parser_not_json_g...; symbols: test_delegating_parser_tool_choice_none_strips_xtml_and_suppresses_calls, test_adjust_request_keeps_xtml_markers_contiguous, test_adjust_request_required_uses_xtml_parser_not_json_guidance，涉及 `test_delegating_parser_tool_choice_none_strips_xtml_and_suppresses_calls, test_adjust_request_keeps_xtml_markers_contiguous, test_adjust_request_required_uses_xtml_parser_not_json_guidance`；`tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +11/-5 (16 lines); hunks: -9,6 +9,7; -301,15 +302,20 @@ def test_delegating_parser_thinking_false_streams_response...; symbols: test_delegating_parser_thinking_false_streams_response_content, test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end，涉及 `test_delegating_parser_thinking_false_streams_response_content, test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end`。
- 代码 diff 细节:
  - `tests/tool_use/test_kimi_k3_tool_parser.py` modified +11/-7 (18 lines); hunks: -449,15 +449,20 @@ def test_delegating_parser_tool_choice_none_strips_xtml_an...; -469,8 +474,7 @@ def test_adjust_request_required_uses_xtml_parser_not_json_g...; symbols: test_delegating_parser_tool_choice_none_strips_xtml_and_suppresses_calls, test_adjust_request_keeps_xtml_markers_contiguous, test_adjust_request_required_uses_xtml_parser_not_json_guidance
  - `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +11/-5 (16 lines); hunks: -9,6 +9,7; -301,15 +302,20 @@ def test_delegating_parser_thinking_false_streams_response...; symbols: test_delegating_parser_thinking_false_streams_response_content, test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end
- 关键代码摘录:

```diff
diff -- tests/tool_use/test_kimi_k3_tool_parser.py
@@ -449,15 +449,20 @@ def test_delegating_parser_tool_choice_none_strips_xtml_and_suppresses_calls():
-def test_adjust_request_keeps_xtml_markers_contiguous():
+@pytest.mark.parametrize(
+    "req",
+    [
+        _request(),
+        _responses_request(),
diff -- tests/reasoning/test_kimi_k3_reasoning_parser.py
@@ -9,6 +9,7 @@
+from vllm.entrypoints.openai.responses.protocol import ResponsesRequest
@@ -301,15 +302,20 @@ def test_delegating_parser_thinking_false_streams_response_content():
-def test_adjust_request_keeps_xtml_markers_contiguous():
+@pytest.mark.parametrize(
+    "req",
+    [
```

- 已读文件:
  - tests: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +11/-7; `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +11/-5
- 验证与风险: diff 自带测试面 `tests/entrypoints/openai/responses/test_sampling_params.py`, `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/tool_use/test_kimi_k3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62980 - [Bugfix] Support online quantization of Kimi K3 NVIDIA projections

- 链接: https://github.com/vllm-project/vllm/pull/62980
- 状态/时间: merged / 2026-10-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `9c66703eef17`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+32/-6，可读 patch 124 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Support online quantization of Kimi K3 NVIDIA projections」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；技术摘要: 覆盖「[Bugfix] Support online quantization of Kimi K3 NVIDIA projections」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-2 (16 lines); hunks: -104,12 +104,21 @@ def __init__(; -129,6 +138,8 @@ def weight_loader(; symbols: __init__, weight_loader, weight_loader_v2，涉及 `__init__, weight_loader, weight_loader_v2`；`vllm/models/kimi_k3/nvidia/model.py` modified +8/-3 (11 lines); hunks: -38,6 +38,7; -323,15 +324,19 @@ def forward(; symbols: forward，涉及 `forward`；`vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +7/-0 (7 lines); hunks: -15,6 +15,7; -179,6 +180,12 @@ def _use_fused_path(self) -> bool:; symbols: _use_fused_path, _select_tail_tier，涉及 `_use_fused_path, _select_tail_tier`；`tests/models/kimi_k3/test_latent_moe_tail.py` modified +3/-1 (4 lines); hunks: -21,6 +21,7; -59,7 +60,8 @@ class FakeMoEConfig:; symbols: FakeMoEConfig，涉及 `FakeMoEConfig`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-2 (16 lines); hunks: -104,12 +104,21 @@ def __init__(; -129,6 +138,8 @@ def weight_loader(; symbols: __init__, weight_loader, weight_loader_v2
  - `vllm/models/kimi_k3/nvidia/model.py` modified +8/-3 (11 lines); hunks: -38,6 +38,7; -323,15 +324,19 @@ def forward(; symbols: forward
  - `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +7/-0 (7 lines); hunks: -15,6 +15,7; -179,6 +180,12 @@ def _use_fused_path(self) -> bool:; symbols: _use_fused_path, _select_tail_tier
  - `tests/models/kimi_k3/test_latent_moe_tail.py` modified +3/-1 (4 lines); hunks: -21,6 +21,7; -59,7 +60,8 @@ class FakeMoEConfig:; symbols: FakeMoEConfig
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -104,12 +104,21 @@ def __init__(
+        padding_size: int = 0,
+        self.padding_size = padding_size
+        if padding_size:
+            # Exclude padding rows from the load-completion count.
+            set_weight_attrs(
+                self.weight,
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -38,6 +38,7 @@
+    UnquantizedLinearMethod,
@@ -323,15 +324,19 @@ def forward(
-                accumulate into. It is consumed in the GEMM's beta-add
-                epilogue, so adding it costs no extra kernel.
+                accumulate into. Unquantized projections fuse the addition
+                into the GEMM epilogue.
diff -- vllm/models/kimi_k3/nvidia/latent_moe_runner.py
@@ -15,6 +15,7 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-2; `vllm/models/kimi_k3/nvidia/model.py` modified +8/-3; `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +7/-0
  - tests: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_latent_moe_tail.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60683 - [ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X

- 链接: https://github.com/vllm-project/vllm/pull/60683
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/amd_specialized_decode/__init__.py`, `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/linear.py` 等 33 个文件；关联提交 `a9bf45ed8a85`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 34 个文件，+6318/-7，可读 patch 6424 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X」；主要实现面是 `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` added +1025/-0 (1025 lines); hunks: -0,0 +1,1025; symbols: peer_pairs, scratch_layout, f32_of, tanh_libm，涉及 `peer_pairs, scratch_layout, f32_of`；`vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py` added +1021/-0 (1021 lines); hunks: -0,0 +1,1021; symbols: KdaPreBuild, scratch_layout, scratch_bytes, step_tag，涉及 `KdaPreBuild, scratch_layout, scratch_bytes`；`tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` added +575/-0 (575 lines); hunks: -0,0 +1,575; symbols: _on_gfx950, _cos, _rel_l2, _randn，涉及 `_on_gfx950, _cos, _rel_l2`；`vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py` added +573/-0 (573 lines); hunks: -0,0 +1,573; symbols: K2Build, peer_layout, peer_bytes, scratch_layout，涉及 `K2Build, peer_layout, peer_bytes`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` added +1025/-0 (1025 lines); hunks: -0,0 +1,1025; symbols: peer_pairs, scratch_layout, f32_of, tanh_libm
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py` added +1021/-0 (1021 lines); hunks: -0,0 +1,1021; symbols: KdaPreBuild, scratch_layout, scratch_bytes, step_tag
  - `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` added +575/-0 (575 lines); hunks: -0,0 +1,575; symbols: _on_gfx950, _cos, _rel_l2, _randn
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py` added +573/-0 (573 lines); hunks: -0,0 +1,573; symbols: K2Build, peer_layout, peer_bytes, scratch_layout
  - `vllm/models/kimi_k3/amd/specialized_decode/mono/common/ops.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: kernel_symbol, rsrc, permlane_swap, lane_gather
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py
@@ -0,0 +1,1025 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""K2b ``moe``: one Kimi-K3 latent-MoE layer, from the MoE input row x to the
+layer's output, every TP reduction inside the kernel.
+One launch a layer and rank, ``BLOCKS`` x ``THREADS``, S <= 8 rows (a
+spec-verify step). The original path (vLLM ROCm, see MOE_SPEC.md) replicates the
diff -- vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py
@@ -0,0 +1,1021 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""K1 ``kda_pre``: one Kimi-K3 KDA layer from the AttnRes seam to the gated core
+output, for a spec-verify step (R requests x L tokens, S = R L rows).
+One launch a layer, ``BLOCKS`` CTAs x ``THREADS`` threads, in three roles so that
+no CTA that polls a mailbox has weight loads in flight (a poll's load retires
diff -- tests/models/kimi_k3/amd_specialized_decode/test_numerics.py
@@ -0,0 +1,575 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` added +1025/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py` added +1021/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py` added +573/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/common/ops.py` added +435/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/common/sync.py` added +255/-0; `vllm/models/kimi_k3/amd/specialized_decode/mono/common/plan.py` added +237/-0
  - tests: `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` added +575/-0; `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py` added +318/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/amd_specialized_decode/__init__.py`, `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59634 - [ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep

- 链接: https://github.com/vllm-project/vllm/pull/59634
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/mtp.py`；关联提交 `09fd02721764`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+103/-7，可读 patch 239 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mtp.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep」；主要实现面是 `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/mla.py` modified +24/-2 (26 lines); hunks: -13,6 +13,7; -31,6 +32,16 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_qk_prep_supported, _fused_decode, forward，涉及 `__init__, _fused_qk_prep_supported, _fused_decode`；`vllm/models/kimi_k3/amd/linear.py` modified +18/-3 (21 lines); hunks: -27,6 +27,7; -398,7 +399,20 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`；`vllm/models/kimi_k3/amd/mtp.py` modified +2/-0 (2 lines); hunks: -239,6 +239,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`；`tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0 (1 lines); hunks: -89,6 +89,7 @@ def attention_output(path, output_shape):; symbols: attention_output，涉及 `attention_output`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/mla.py` modified +24/-2 (26 lines); hunks: -13,6 +13,7; -31,6 +32,16 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _fused_qk_prep_supported, _fused_decode, forward
  - `vllm/models/kimi_k3/amd/linear.py` modified +18/-3 (21 lines); hunks: -27,6 +27,7; -398,7 +399,20 @@ def __init__(; symbols: __init__, load_weights
  - `vllm/models/kimi_k3/amd/mtp.py` modified +2/-0 (2 lines); hunks: -239,6 +239,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
  - `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0 (1 lines); hunks: -89,6 +89,7 @@ def attention_output(path, output_shape):; symbols: attention_output
  - `vllm/v1/attention/backends/mla/rocm_aiter_mla.py` modified +58/-2 (60 lines); hunks: -147,6 +147,29 @@ def _fp8_mla_prefill_supported() -> bool:; -2076,8 +2099,12 @@ def get_mla_padded_q(; symbols: _fp8_mla_prefill_supported, _fused_mla_prefill_qkv_supported, _aiter_mla_native_h24_reducer_supported, get_mla_padded_q
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -13,6 +13,7 @@
+from vllm.model_executor.layers.linear import KimiK3MergedQKVGateLinear
@@ -31,6 +32,16 @@ def __init__(self, *args, **kwargs) -> None:
+        self._qkv_gate_fused = isinstance(
+            self.fused_qkv_a_proj, KimiK3MergedQKVGateLinear
+        )
+        self._fused_q_heads = self.num_heads
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -27,6 +27,7 @@
+    KimiK3MergedQKVGateLinear,
@@ -398,7 +399,20 @@ def __init__(
-        if self.q_lora_rank is not None:
+        self.use_output_gate = config.mla_use_output_gate
+        if self.q_lora_rank is not None and self.use_output_gate:
+            self.fused_qkv_a_proj = KimiK3MergedQKVGateLinear(
diff -- vllm/models/kimi_k3/amd/mtp.py
@@ -239,6 +239,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/mla.py` modified +24/-2; `vllm/models/kimi_k3/amd/linear.py` modified +18/-3; `vllm/models/kimi_k3/amd/mtp.py` modified +2/-0; `vllm/v1/attention/backends/mla/rocm_aiter_mla.py` modified +58/-2
  - tests: `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_mla_direct_return.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59552 - [ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill

- 链接: https://github.com/vllm-project/vllm/pull/59552
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；关联提交 `28e92eeff25f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+197/-20，可读 patch 354 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill」；主要实现面是 `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +54/-2 (56 lines); hunks: -19,9 +19,11; -172,9 +174,59 @@ def _warm_recurrent_kda(; symbols: _get_kda_layer, _warm_recurrent_kda, _warm_gluon_chunk_kda, kimi_k3_triton_warmup，涉及 `_get_kda_layer, _warm_recurrent_kda, _warm_gluon_chunk_kda`；`vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +39/-5 (44 lines); hunks: -9,6 +9,7; -24,6 +25,11; symbols: get_gluon_chunk_kda_warmup_profiles, chunk_kda_prefill，涉及 `get_gluon_chunk_kda_warmup_profiles, chunk_kda_prefill`；`tests/models/kimi_k3/test_amd_kda_chunk.py` modified +23/-2 (25 lines); hunks: -77,7 +77,7 @@ def _run(inp: dict, use_fused: bool, out: torch.Tensor | None...; -112,6 +112,27 @@ def test_fused_chunk_matches_triton(seqlens: list[int]) ->...; symbols: _run, test_fused_chunk_matches_triton, test_gluon_chunk_matches_triton, test_out_argument_receives_the_result，涉及 `_run, test_fused_chunk_matches_triton, test_gluon_chunk_matches_triton`；`vllm/models/kimi_k3/amd/kda.py` modified +13/-9 (22 lines); hunks: -95,7 +95,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> MambaS...; -242,13 +244,15 @@ def __init__(; symbols: get_kv_cache_spec, __init__, _prefill_conv，涉及 `get_kv_cache_spec, __init__, _prefill_conv`。
- 代码 diff 细节:
  - `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +54/-2 (56 lines); hunks: -19,9 +19,11; -172,9 +174,59 @@ def _warm_recurrent_kda(; symbols: _get_kda_layer, _warm_recurrent_kda, _warm_gluon_chunk_kda, kimi_k3_triton_warmup
  - `vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +39/-5 (44 lines); hunks: -9,6 +9,7; -24,6 +25,11; symbols: get_gluon_chunk_kda_warmup_profiles, chunk_kda_prefill
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +23/-2 (25 lines); hunks: -77,7 +77,7 @@ def _run(inp: dict, use_fused: bool, out: torch.Tensor | None...; -112,6 +112,27 @@ def test_fused_chunk_matches_triton(seqlens: list[int]) ->...; symbols: _run, test_fused_chunk_matches_triton, test_gluon_chunk_matches_triton, test_out_argument_receives_the_result
  - `vllm/models/kimi_k3/amd/kda.py` modified +13/-9 (22 lines); hunks: -95,7 +95,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> MambaS...; -242,13 +244,15 @@ def __init__(; symbols: get_kv_cache_spec, __init__, _prefill_conv
  - `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +3/-2 (5 lines); hunks: -482,7 +482,7 @@ def _spec_for(monkeypatch, **attrs) -> MambaSpec:; -506,7 +506,8 @@ def test_opt_in_publishes_chunk_walk_alignment(monkeypatch)...; symbols: _spec_for, test_opt_in_publishes_chunk_walk_alignment
- 关键代码摘录:

```diff
diff -- vllm/model_executor/warmup/kimi_k3_triton_warmup.py
@@ -19,9 +19,11 @@
-def _get_kda_layer(worker: Worker) -> KimiK3DeltaAttention | None:
+def _get_kda_layer(
+    worker: Worker, module: str = "vllm.models.kimi_k3.nvidia.kda"
+) -> KimiK3DeltaAttention | None:
-    kda = sys.modules.get("vllm.models.kimi_k3.nvidia.kda")
+    kda = sys.modules.get(module)
diff -- vllm/models/kimi_k3/amd/ops/kda_prefill.py
@@ -9,6 +9,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -24,6 +25,11 @@
+# Consumed by kimi_k3_triton_warmup.py during kernel_warmup().
+def get_gluon_chunk_kda_warmup_profiles() -> tuple[tuple[int, int], ...]:
+    return ((1, 64), (2, 64), (4, 64), (8, 64), (16, 64), (1, 4096), (2, 2048))
@@ -40,7 +46,7 @@ def chunk_kda_prefill(
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -77,7 +77,7 @@ def _run(inp: dict, use_fused: bool, out: torch.Tensor | None = None, **kw):
```

- 已读文件:
  - runtime: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +54/-2; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +39/-5; `vllm/models/kimi_k3/amd/kda.py` modified +13/-9
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +23/-2; `tests/models/kimi_k3/test_amd_kda_checkpoint.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59824 - [ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X

- 链接: https://github.com/vllm-project/vllm/pull/59824
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`；关联提交 `5bf3d9f6653e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+383/-13，可读 patch 686 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py` added +93/-0 (93 lines); hunks: -0,0 +1,93; symbols: _config, _spec, _builder, _trimmed_verify_batch，涉及 `_config, _spec, _builder`；`vllm/models/kimi_k3/amd/kda_metadata.py` modified +29/-0 (29 lines); hunks: -11,19 +11,22; -92,7 +95,24 @@ def prepare_chunk_metadata_device(; symbols: prepare_chunk_metadata_device, _adaptive_verification_enabled, KimiK3ROCmKDAMetadataBuilder, get_varlen_cudagraph_max_query_len，涉及 `prepare_chunk_metadata_device, _adaptive_verification_enabled, KimiK3ROCmKDAMetadataBuilder`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py` added +93/-0 (93 lines); hunks: -0,0 +1,93; symbols: _config, _spec, _builder, _trimmed_verify_batch
  - `vllm/models/kimi_k3/amd/kda_metadata.py` modified +29/-0 (29 lines); hunks: -11,19 +11,22; -92,7 +95,24 @@ def prepare_chunk_metadata_device(; symbols: prepare_chunk_metadata_device, _adaptive_verification_enabled, KimiK3ROCmKDAMetadataBuilder, get_varlen_cudagraph_max_query_len
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_adaptive_verification.py
@@ -0,0 +1,93 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm Kimi-K3 KDA metadata under adaptive verification.
+Adaptive verification splits the draft budget evenly on the host, then trims
+each verify request on device. The KDA spec path must therefore plan from the
+device offsets, never from host lengths that merely look uniform.
diff -- vllm/models/kimi_k3/amd/kda_metadata.py
@@ -11,19 +11,22 @@
+from vllm.config import VllmConfig
+from vllm.v1.attention.backend import max_decode_query_len
+from vllm.v1.kv_cache_interface import KVCacheSpec
@@ -92,7 +95,24 @@ def prepare_chunk_metadata_device(
+def _adaptive_verification_enabled(vllm_config: VllmConfig) -> bool:
+    speculative_config = vllm_config.speculative_config
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py` added +93/-0
  - runtime: `vllm/models/kimi_k3/amd/kda_metadata.py` modified +29/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `tests/v1/attention/test_expand_page_indices.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #61867 - [Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x)

- 链接: https://github.com/vllm-project/vllm/pull/61867
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/model_state.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/__init__.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/__init__.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/attn_res/__init__.py` 等 50 个文件；关联提交 `642c18d64c4c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 50 个文件，+12805/-3，可读 patch 12903 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x)」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py`；技术摘要: 覆盖「[Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x)」；主要实现面是 `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py` added +1579/-0 (1579 lines); hunks: -0,0 +1,1579; symbols: ExpertsGeometry, __init__, image, swizzled，涉及 `ExpertsGeometry, __init__, image`；`vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py` added +1031/-0 (1031 lines); hunks: -0,0 +1,1031; symbols: scatter_sums, gather_sums, spread, MoeTail，涉及 `scatter_sums, gather_sums, spread`；`vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py` added +928/-0 (928 lines); hunks: -0,0 +1,928; symbols: ptx, asm, wrap, op，涉及 `ptx, asm, wrap`；`vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/kda/kernel.py` added +715/-0 (715 lines); hunks: -0,0 +1,715; symbols: reciprocal_guess, reciprocal_rn, sigmoids, advance，涉及 `reciprocal_guess, reciprocal_rn, sigmoids`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py` added +1579/-0 (1579 lines); hunks: -0,0 +1,1579; symbols: ExpertsGeometry, __init__, image, swizzled
  - `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py` added +1031/-0 (1031 lines); hunks: -0,0 +1,1031; symbols: scatter_sums, gather_sums, spread, MoeTail
  - `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py` added +928/-0 (928 lines); hunks: -0,0 +1,928; symbols: ptx, asm, wrap, op
  - `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/kda/kernel.py` added +715/-0 (715 lines); hunks: -0,0 +1,715; symbols: reciprocal_guess, reciprocal_rn, sigmoids, advance
  - `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/shared.py` added +684/-0 (684 lines); hunks: -0,0 +1,684; symbols: situ, prefetch_tma2, release_count, acquire_count
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py
@@ -0,0 +1,1579 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Persistent routed experts: TMA producer, MXFP8 activations, FP4 x MXFP8 FC1/FC2 MMAs,
+SiTU hidden exchange and output epilogue. Capacity <= 8 keeps the batch's activations in
+SMEM; capacity > 8 (grouped) runs (expert, <= 8 tokens) units whose FC1 stages gather
+8-row slices of the grid-quantized batch."""
diff -- vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py
@@ -0,0 +1,1031 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Clustered MoE tail (TP8 B1..4, TP16 B1..8): routed finalization/publication,
+all-reduce, RMS tree, K-split up projection, shared reduce-scatter and output multicast.
+TMA weight loads overlap the mailbox wait. The caller owns the three rotating mailboxes
+and must use different parities on successive calls. TP8 B5+ and TP16 B9+ run the
diff -- vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py
@@ -0,0 +1,928 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/experts.py` added +1579/-0; `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/tail.py` added +1031/-0; `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/common/primitives.py` added +928/-0; `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/kda/kernel.py` added +715/-0; `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/shared.py` added +684/-0; `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/moe/small_batch/front_tp16.py` added +580/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/model_state.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #57392 - [ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode

- 链接: https://github.com/vllm-project/vllm/pull/57392
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`；关联提交 `3f1e57225abe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+503/-17，可读 patch 674 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +325/-13 (338 lines); hunks: -1,11 +1,17; -14,18 +20,34; symbols: _on_supported_arch, _hip_kernel_arch, _aiter_gluon_kda_available, _requires_kernel，涉及 `_on_supported_arch, _hip_kernel_arch, _aiter_gluon_kda_available`；`vllm/models/kimi_k3/amd/kda.py` modified +68/-4 (72 lines); hunks: -8,6 +8,7; -182,16 +183,19 @@ def __init__(; symbols: __init__, _forward，涉及 `__init__, _forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_decode.py` modified +325/-13 (338 lines); hunks: -1,11 +1,17; -14,18 +20,34; symbols: _on_supported_arch, _hip_kernel_arch, _aiter_gluon_kda_available, _requires_kernel
  - `vllm/models/kimi_k3/amd/kda.py` modified +68/-4 (72 lines); hunks: -8,6 +8,7; -182,16 +183,19 @@ def __init__(; symbols: __init__, _forward
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_decode.py
@@ -1,11 +1,17 @@
-"""The ROCm fused KDA decode kernel must match the Triton chain it replaces.
+"""The ROCm fused KDA decode kernels must match the Triton chain they replace.
-The fused kernel folds the packed causal conv1d update, the gated delta-rule
-recurrence and the gated output RMSNorm into one launch, and updates both the
-conv state and the recurrent state in place. Every one of those outputs is
-compared against the three-kernel path the AMD layer falls back to.
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -8,6 +8,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -182,16 +183,19 @@ def __init__(
-        decode_conv1d_weight = None
-        if is_fused_kda_decode_supported(
+        self.use_aiter_decode = bool(rocm_aiter_ops.is_kda_gluon_decode_available())
+        use_hip_decode = not self.use_aiter_decode and is_fused_kda_decode_supported(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +325/-13
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +68/-4
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #61654 - [ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper

- 链接: https://github.com/vllm-project/vllm/pull/61654
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/mla.py`；关联提交 `9a648b4649de`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-2，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/models/kimi_k3/amd/mla.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper」；主要实现面是 `vllm/models/kimi_k3/amd/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/mla.py` modified +3/-2 (5 lines); hunks: -50,8 +50,9 @@ def _fused_qk_prep_supported(self) -> bool:; symbols: _fused_qk_prep_supported, get_input_quant_key，涉及 `_fused_qk_prep_supported, get_input_quant_key`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/mla.py` modified +3/-2 (5 lines); hunks: -50,8 +50,9 @@ def _fused_qk_prep_supported(self) -> bool:; symbols: _fused_qk_prep_supported, get_input_quant_key
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -50,8 +50,9 @@ def _fused_qk_prep_supported(self) -> bool:
-        return attn.is_aiter_triton_fp4_bmm_enabled or (
-            not attn.is_aiter_triton_fp8_bmm_enabled and attn.W_UK_T is not None
+        return (
+            attn.is_aiter_triton_fp4_bmm_enabled
+            or not attn.is_aiter_triton_fp8_bmm_enabled
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/mla.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #61207 - [Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading

- 链接: https://github.com/vllm-project/vllm/pull/61207
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`；关联提交 `67516b6c42ba`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+77/-74，可读 patch 207 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +56/-0 (56 lines); hunks: -289,3 +289,59 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:; symbols: test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading，涉及 `test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading`；`vllm/models/kimi_k3/amd/ops/kda_decode.py` modified +2/-52 (54 lines); hunks: -7,17 +7,14; -51,50 +48,3 @@ def is_fused_kda_decode_supported(; symbols: is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader, make_decode_norm_weight_loader，涉及 `is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader`；`vllm/models/kimi_k3/amd/kda.py` modified +19/-22 (41 lines); hunks: -43,7 +43,7; -54,8 +54,6; symbols: __init__, process_weights_after_loading, rearrange_mixed_qkv，涉及 `__init__, process_weights_after_loading, rearrange_mixed_qkv`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_decode.py` modified +56/-0 (56 lines); hunks: -289,3 +289,59 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:; symbols: test_fused_kda_decode_skips_null_block_padding, test_decode_weights_staged_after_loading
  - `vllm/models/kimi_k3/amd/ops/kda_decode.py` modified +2/-52 (54 lines); hunks: -7,17 +7,14; -51,50 +48,3 @@ def is_fused_kda_decode_supported(; symbols: is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader, make_decode_norm_weight_loader
  - `vllm/models/kimi_k3/amd/kda.py` modified +19/-22 (41 lines); hunks: -43,7 +43,7; -54,8 +54,6; symbols: __init__, process_weights_after_loading, rearrange_mixed_qkv
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_decode.py
@@ -289,3 +289,59 @@ def test_fused_kda_decode_skips_null_block_padding() -> None:
+def test_decode_weights_staged_after_loading(dist_init) -> None:
+    """The fused-decode weight copies must not depend on the weight loaders.
+    Loaders that bypass ``weight_loader`` (e.g. ``--load-format dummy``) left
+    them uninitialized, so decode could read NaN. Loading runs with grad mode
+    on, so the copies must also stay out of autograd.
+    """
diff -- vllm/models/kimi_k3/amd/ops/kda_decode.py
@@ -7,17 +7,14 @@
-The kernel wants a width-major conv weight and an fp32 norm weight, so both are
-staged once at load time by the weight loaders below.
+The kernel wants a width-major conv weight and an fp32 norm weight, so the
+layer stages both once in ``process_weights_after_loading``.
-from collections.abc import Callable
-from vllm.model_executor.model_loader.weight_utils import default_weight_loader
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -43,7 +43,7 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +56/-0
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_decode.py` modified +2/-52; `vllm/models/kimi_k3/amd/kda.py` modified +19/-22
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #60446 - [Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys

- 链接: https://github.com/vllm-project/vllm/pull/60446
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py`；关联提交 `fc3931739271`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py`；技术摘要: 覆盖「[Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys」；主要实现面是 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +1/-1 (2 lines); hunks: -349,7 +349,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk，涉及 `chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk`；`vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py` modified +1/-1 (2 lines); hunks: -451,7 +451,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk，涉及 `chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +1/-1 (2 lines); hunks: -349,7 +349,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk
  - `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py` modified +1/-1 (2 lines); hunks: -451,7 +451,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused, chunk_kda_fwd_kernel_intra_sub_chunk
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py
@@ -349,7 +349,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(
-    key=["BK", "NC", "BT", "HV"],
+    key=["BK", "BT", "HV"],
diff -- vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py
@@ -451,7 +451,7 @@ def chunk_kda_fwd_kernel_inter_solve_fused(
-    key=["BK", "NC", "BT", "HV"],
+    key=["BK", "BT", "HV"],
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +1/-1; `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #60717 - [ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization

- 链接: https://github.com/vllm-project/vllm/pull/60717
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`；关联提交 `88a419649e36`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-5，可读 patch 38 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization」；主要实现面是 `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_attn_res.py` modified +8/-4 (12 lines); hunks: -247,12 +247,16 @@ def test_amd_attn_res_fp8_preserves_prefix_and_quantized_o...; symbols: test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, ordinal，涉及 `test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, ordinal`；`vllm/models/kimi_k3/amd/ops/attn_res.py` modified +2/-1 (3 lines); hunks: -10,6 +10,7; -207,7 +208,7 @@ def attn_res(; symbols: attn_res，涉及 `attn_res`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_attn_res.py` modified +8/-4 (12 lines); hunks: -247,12 +247,16 @@ def test_amd_attn_res_fp8_preserves_prefix_and_quantized_o...; symbols: test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, ordinal
  - `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +2/-1 (3 lines); hunks: -10,6 +10,7; -207,7 +208,7 @@ def attn_res(; symbols: attn_res
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_attn_res.py
@@ -247,12 +247,16 @@ def test_amd_attn_res_fp8_preserves_prefix_and_quantized_output(
-        code_delta = (
-            output.view(torch.uint8).to(torch.int16)
-            - ref_output.view(torch.uint8).to(torch.int16)
-        ).abs()
+        # Codes are sign-magnitude, so order them by value to keep a step
+        # across zero adjacent.
diff -- vllm/models/kimi_k3/amd/ops/attn_res.py
@@ -10,6 +10,7 @@
+from vllm.model_executor.layers.quantization.utils.quant_utils import get_fp8_min_max
@@ -207,7 +208,7 @@ def attn_res(
-        QUANT_MAX=0.0 if quant_dtype is None else torch.finfo(quant_dtype).max,
+        QUANT_MAX=0.0 if quant_dtype is None else get_fp8_min_max()[1],
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_attn_res.py` modified +8/-4
  - runtime: `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_attn_res.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56875 - [Perf] Enable Kimi K3 shared expert sharding with DeepEP v2

- 链接: https://github.com/vllm-project/vllm/pull/56875
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `8674a794c788`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+41/-4，可读 patch 66 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Enable Kimi K3 shared expert sharding with DeepEP v2」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_sequence_parallel.py`；技术摘要: 覆盖「[Perf] Enable Kimi K3 shared expert sharding with DeepEP v2」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_sequence_parallel.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +20/-4 (24 lines); hunks: -156,6 +156,20 @@ def shard_sequence_parallel_mlp(; -617,10 +631,12 @@ def __init__(; symbols: shard_sequence_parallel_mlp, can_shard_sequence_parallel_shared_expert, maybe_init_gemm_rs_ar, __init__，涉及 `shard_sequence_parallel_mlp, can_shard_sequence_parallel_shared_expert, maybe_init_gemm_rs_ar`；`tests/models/kimi_k3/test_sequence_parallel.py` modified +21/-0 (21 lines); hunks: -301,6 +301,27 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_shard_sequence_parallel_mlp_gating, test_shared_expert_sharding_backend_gate, test_sharded_sequence_parallel_mlp_matches_replicated，涉及 `test_shard_sequence_parallel_mlp_gating, test_shared_expert_sharding_backend_gate, test_sharded_sequence_parallel_mlp_matches_replicated`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +20/-4 (24 lines); hunks: -156,6 +156,20 @@ def shard_sequence_parallel_mlp(; -617,10 +631,12 @@ def __init__(; symbols: shard_sequence_parallel_mlp, can_shard_sequence_parallel_shared_expert, maybe_init_gemm_rs_ar, __init__
  - `tests/models/kimi_k3/test_sequence_parallel.py` modified +21/-0 (21 lines); hunks: -301,6 +301,27 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_shard_sequence_parallel_mlp_gating, test_shared_expert_sharding_backend_gate, test_sharded_sequence_parallel_mlp_matches_replicated
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -156,6 +156,20 @@ def shard_sequence_parallel_mlp(
+def can_shard_sequence_parallel_shared_expert(vllm_config: VllmConfig) -> bool:
+    """Whether the active MoE backend preserves the SP shared-expert contract.
+    MegaMoE invokes the shared expert directly. DeepEP v2 invokes it through
+    ``MoERunner``, but its EP combine returns the routed output in the local
+    sequence-sharded layout, so the shared expert can use the same
+    all-gather/partial-GEMM/reduce-scatter implementation.
diff -- tests/models/kimi_k3/test_sequence_parallel.py
@@ -301,6 +301,27 @@ def test_shard_sequence_parallel_mlp_gating(
+@pytest.mark.parametrize(
+    ("moe_backend", "all2all_backend", "expected"),
+    [
+        ("deep_gemm_mega_moe", "naive", True),
+        ("auto", "deepep_v2", True),
+        ("auto", "deepep_low_latency", False),
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +20/-4
  - tests: `tests/models/kimi_k3/test_sequence_parallel.py` modified +21/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_sequence_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59591 - [ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj

- 链接: https://github.com/vllm-project/vllm/pull/59591
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`；关联提交 `d80ddaac7321`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+125/-28，可读 patch 277 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj」；主要实现面是 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +80/-16 (96 lines); hunks: -22,7 +22,7; -40,20 +40,42; symbols: _build_transform, _tail_runner, _rank_partials，涉及 `_build_transform, _tail_runner, _rank_partials`；`vllm/models/kimi_k3/amd/linear.py` modified +32/-9 (41 lines); hunks: -125,11 +125,13 @@ class KimiRoutedOutputTransform(nn.Module):; -240,7 +242,7 @@ def __init__(; symbols: KimiRoutedOutputTransform, __init__, forward，涉及 `KimiRoutedOutputTransform, __init__, forward`；`vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +13/-3 (16 lines); hunks: -36,18 +36,23 @@ def __init__(; -80,7 +85,12 @@ def _shard_up_proj_tail(; symbols: __init__, _shard_up_proj_tail，涉及 `__init__, _shard_up_proj_tail`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +80/-16 (96 lines); hunks: -22,7 +22,7; -40,20 +40,42; symbols: _build_transform, _tail_runner, _rank_partials
  - `vllm/models/kimi_k3/amd/linear.py` modified +32/-9 (41 lines); hunks: -125,11 +125,13 @@ class KimiRoutedOutputTransform(nn.Module):; -240,7 +242,7 @@ def __init__(; symbols: KimiRoutedOutputTransform, __init__, forward
  - `vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +13/-3 (16 lines); hunks: -36,18 +36,23 @@ def __init__(; -80,7 +85,12 @@ def _shard_up_proj_tail(; symbols: __init__, _shard_up_proj_tail
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_latent_moe_runner.py
@@ -22,7 +22,7 @@
-from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.layers.linear import ColumnParallelLinear, ReplicatedLinear
@@ -40,20 +40,42 @@
-def _build_transform(device: torch.device) -> KimiRoutedOutputTransform:
+def _build_transform(
+    device: torch.device, *, row_sharded: bool = False
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -125,11 +125,13 @@ class KimiRoutedOutputTransform(nn.Module):
-        up_proj: ReplicatedLinear,
+        up_proj: ReplicatedLinear | ColumnParallelLinear,
+        row_sharded: bool = False,
+        self.row_sharded = row_sharded
@@ -240,7 +242,7 @@ def __init__(
-        self.routed_expert_up_proj: ReplicatedLinear | None
diff -- vllm/models/kimi_k3/amd/latent_moe_runner.py
@@ -36,18 +36,23 @@ def __init__(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +80/-16
  - runtime: `vllm/models/kimi_k3/amd/linear.py` modified +32/-9; `vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +13/-3
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59069 - [ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization

- 链接: https://github.com/vllm-project/vllm/pull/59069
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_amd_fp8_fusions.py`, `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py` 等 7 个文件；关联提交 `458ba2edf85b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+455/-15，可读 patch 689 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization」；主要实现面是 `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_attn_res.py` modified +99/-0 (99 lines); hunks: -191,3 +191,102 @@ def test_amd_attn_res_fused_contract(; symbols: test_amd_attn_res_fused_contract, test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, test_mla_input_quant_requires_all_consumers，涉及 `test_amd_attn_res_fused_contract, test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, test_mla_input_quant_requires_all_consumers`；`tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +81/-0 (81 lines); hunks: -1,6 +1,9; -36,3 +39,81 @@ def test_mla_self_attention_returns_projection_storage_direct...; symbols: test_mla_self_attention_returns_projection_storage_directly, test_mla_forward_preserves_output_shape_with_fp8_input, input_projection, attention_output，涉及 `test_mla_self_attention_returns_projection_storage_directly, test_mla_forward_preserves_output_shape_with_fp8_input, input_projection`；`vllm/models/kimi_k3/amd/linear.py` modified +44/-5 (49 lines); hunks: -2,11 +2,12; -19,6 +20,10; symbols: __init__, get_input_quant_key, forward, _apply_attn_res，涉及 `__init__, get_input_quant_key, forward`；`vllm/models/kimi_k3/amd/ops/attn_res.py` modified +27/-4 (31 lines); hunks: -22,6 +22,7 @@ def _attn_res_kernel(; -35,6 +36,7 @@ def _attn_res_kernel(; symbols: _attn_res_kernel, attn_res，涉及 `_attn_res_kernel, attn_res`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_attn_res.py` modified +99/-0 (99 lines); hunks: -191,3 +191,102 @@ def test_amd_attn_res_fused_contract(; symbols: test_amd_attn_res_fused_contract, test_amd_attn_res_fp8_preserves_prefix_and_quantized_output, test_mla_input_quant_requires_all_consumers
  - `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +81/-0 (81 lines); hunks: -1,6 +1,9; -36,3 +39,81 @@ def test_mla_self_attention_returns_projection_storage_direct...; symbols: test_mla_self_attention_returns_projection_storage_directly, test_mla_forward_preserves_output_shape_with_fp8_input, input_projection, attention_output
  - `vllm/models/kimi_k3/amd/linear.py` modified +44/-5 (49 lines); hunks: -2,11 +2,12; -19,6 +20,10; symbols: __init__, get_input_quant_key, forward, _apply_attn_res
  - `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +27/-4 (31 lines); hunks: -22,6 +22,7 @@ def _attn_res_kernel(; -35,6 +36,7 @@ def _attn_res_kernel(; symbols: _attn_res_kernel, attn_res
  - `vllm/models/kimi_k3/amd/mla.py` modified +27/-2 (29 lines); hunks: -8,8 +8,13; -49,6 +54,21 @@ def _fused_qk_prep_supported(self) -> bool:; symbols: _fused_qk_prep_supported, get_input_quant_key, _normalize_q_kv, _fused_decode
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_attn_res.py
@@ -191,3 +191,102 @@ def test_amd_attn_res_fused_contract(
+@pytest.mark.parametrize(
+    "num_tokens,num_blocks,has_delta,write_block",
+    [
+        (0, 0, False, False),
+        (1, 0, True, True),
+        (17, 4, True, True),
diff -- tests/models/kimi_k3/test_amd_mla_direct_return.py
@@ -1,6 +1,9 @@
+from types import SimpleNamespace
+import pytest
@@ -36,3 +39,81 @@ def test_mla_self_attention_returns_projection_storage_directly() -> None:
+@pytest.mark.parametrize("quantized", [False, True])
+@pytest.mark.parametrize("fused_decode", [False, True])
+def test_mla_forward_preserves_output_shape_with_fp8_input(
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -2,11 +2,12 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_attn_res.py` modified +99/-0; `tests/models/kimi_k3/test_amd_mla_direct_return.py` modified +81/-0
  - runtime: `vllm/models/kimi_k3/amd/linear.py` modified +44/-5; `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +27/-4; `vllm/models/kimi_k3/amd/mla.py` modified +27/-2; `vllm/models/kimi_k3/amd/kda.py` modified +12/-4
  - other: `benchmarks/kernels/benchmark_kimi_k3_amd_fp8_fusions.py` added +165/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59733 - [Bugfix][Kimi-K3] Declare max_tp_shards on the DSpark MLA KV cache spec

- 链接: https://github.com/vllm-project/vllm/pull/59733
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/mla.py`；关联提交 `1fbbfa165709`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+34/-0，可读 patch 45 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Declare max_tp_shards on the DSpark MLA KV cache spec」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/test_dspark_mla.py`, `vllm/models/kimi_k3/nvidia/mla.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Declare max_tp_shards on the DSpark MLA KV cache spec」；主要实现面是 `tests/models/test_dspark_mla.py`, `vllm/models/kimi_k3/nvidia/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/test_dspark_mla.py` modified +33/-0 (33 lines); hunks: -336,3 +336,36 @@ def __call__(self, main_x):; symbols: __call__, test_k3_dspark_mla_kv_cache_spec_groups_with_target_mla，涉及 `__call__, test_k3_dspark_mla_kv_cache_spec_groups_with_target_mla`；`vllm/models/kimi_k3/nvidia/mla.py` modified +1/-0 (1 lines); hunks: -422,6 +422,7 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCa...; symbols: get_kv_cache_spec，涉及 `get_kv_cache_spec`。
- 代码 diff 细节:
  - `tests/models/test_dspark_mla.py` modified +33/-0 (33 lines); hunks: -336,3 +336,36 @@ def __call__(self, main_x):; symbols: __call__, test_k3_dspark_mla_kv_cache_spec_groups_with_target_mla
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +1/-0 (1 lines); hunks: -422,6 +422,7 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCa...; symbols: get_kv_cache_spec
- 关键代码摘录:

```diff
diff -- tests/models/test_dspark_mla.py
@@ -336,3 +336,36 @@ def __call__(self, main_x):
+@pytest.mark.cpu_test
+def test_k3_dspark_mla_kv_cache_spec_groups_with_target_mla():
+    """The draft's MLA layers must share a KV cache group with the target's."""
+    from vllm.model_executor.layers.attention.mla_attention import MLAAttention
+    from vllm.models.kimi_k3.nvidia.mla import MultiHeadLatentAttention
+    from vllm.v1.core.kv_cache_utils import _get_kv_cache_groups_uniform_page_size
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -422,6 +422,7 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
+            max_tp_shards=1,
```

- 已读文件:
  - tests: `tests/models/test_dspark_mla.py` modified +33/-0
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/test_dspark_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56881 - [Kimi-K3] Use the fused K/V pack kernel on the decode-context-parallel prefill path

- 链接: https://github.com/vllm-project/vllm/pull/56881
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`；关联提交 `b2863c0de953`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+142/-7，可读 patch 198 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Use the fused K/V pack kernel on the decode-context-parallel prefill path」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`；技术摘要: 覆盖「[Kimi-K3] Use the fused K/V pack kernel on the decode-context-parallel prefill path」；主要实现面是 `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_mla_prefill_context.py` modified +114/-0 (114 lines); hunks: -13,8 +13,10; -317,3 +319,115 @@ def test_fused_context_rejects_an_unquantized_query() -> N...; symbols: test_fused_context_rejects_an_unquantized_query, _run_dcp_context_loop, test_dcp_context_fused_pack_matches_generic_tail，涉及 `test_fused_context_rejects_an_unquantized_query, _run_dcp_context_loop, test_dcp_context_fused_pack_matches_generic_tail`；`vllm/models/kimi_k3/nvidia/mla.py` modified +12/-2 (14 lines); hunks: -785,6 +785,15 @@ def _decode_concat_cache(; -814,8 +823,8 @@ def _compute_prefill_context(; symbols: _decode_concat_cache, _fused_mla_kv_concat, _compute_prefill_context, _forward_prefill_fused，涉及 `_decode_concat_cache, _fused_mla_kv_concat, _compute_prefill_context`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_mla_prefill_context.py` modified +114/-0 (114 lines); hunks: -13,8 +13,10; -317,3 +319,115 @@ def test_fused_context_rejects_an_unquantized_query() -> N...; symbols: test_fused_context_rejects_an_unquantized_query, _run_dcp_context_loop, test_dcp_context_fused_pack_matches_generic_tail
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +12/-2 (14 lines); hunks: -785,6 +785,15 @@ def _decode_concat_cache(; -814,8 +823,8 @@ def _compute_prefill_context(; symbols: _decode_concat_cache, _fused_mla_kv_concat, _compute_prefill_context, _forward_prefill_fused
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_mla_prefill_context.py
@@ -13,8 +13,10 @@
+import vllm.model_executor.layers.attention.mla_attention as mla_attention
+    MLACommonImpl,
@@ -317,3 +319,115 @@ def test_fused_context_rejects_an_unquantized_query() -> None:
+# --------------------------------------------------------------------------
+# Decode context parallelism: the generic impl keeps its loop (allgather +
+# reorg) and only the per-chunk K/V pack is handed to the layer's fused kernel.
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -785,6 +785,15 @@ def _decode_concat_cache(
+    def _fused_mla_kv_concat(
+        self, kv_nope: torch.Tensor, k_pe: torch.Tensor, use_fp8_prefill: bool
+    ) -> tuple[torch.Tensor, torch.Tensor]:
+        """Pack one DCP context chunk's ``(k, v)`` with the fused kernels."""
+        k_nope, v = kv_nope.split([self.qk_nope_head_dim, self.v_head_dim], dim=-1)
+        if use_fp8_prefill:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_mla_prefill_context.py` modified +114/-0
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +12/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_mla_prefill_context.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59278 - [Model] Extend device-side mm normalization to Kimi K2.5 / K3

- 链接: https://github.com/vllm-project/vllm/pull/59278
- 状态/时间: merged / 2026-10-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_kimi_k3.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/models/kimi_k3/amd/model.py`, `vllm/models/kimi_k3/common/mm_preprocess.py` 等 9 个文件；关联提交 `0e468adb43d6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+130/-15，可读 patch 384 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Extend device-side mm normalization to Kimi K2.5 / K3」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/multimodal/processing/test_kimi_k3.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Model] Extend device-side mm normalization to Kimi K2.5 / K3」；主要实现面是 `tests/models/multimodal/processing/test_kimi_k3.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_kimi_k3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: image_processors, _noise_image, test_fused_image_processor_matches_hf, test_mm_device_do_normalize，涉及 `image_processors, _noise_image, test_fused_image_processor_matches_hf`；`vllm/model_executor/models/kimi_k25.py` modified +9/-4 (13 lines); hunks: -17,6 +17,7; -306,6 +307,7 @@ class KimiK25ForConditionalGeneration(; symbols: KimiK25ForConditionalGeneration, __init__, _parse_and_validate_media_input, prepare_encoder_cudagraph_capture_inputs，涉及 `KimiK25ForConditionalGeneration, __init__, _parse_and_validate_media_input`；`vllm/models/kimi_k3/nvidia/model.py` modified +6/-7 (13 lines); hunks: -30,6 +30,7; -1736,6 +1737,7 @@ class KimiK3ForConditionalGeneration(; symbols: KimiK3ForConditionalGeneration, __init__, prepare_encoder_cudagraph_capture_inputs, encoder_eager_forward，涉及 `KimiK3ForConditionalGeneration, __init__, prepare_encoder_cudagraph_capture_inputs`；`vllm/transformers_utils/processors/kimi_k25_vision_fused.py` modified +10/-2 (12 lines); hunks: -17,6 +17,8; -238,7 +240,12 @@ def preprocess(; symbols: preprocess，涉及 `preprocess`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_kimi_k3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: image_processors, _noise_image, test_fused_image_processor_matches_hf, test_mm_device_do_normalize
  - `vllm/model_executor/models/kimi_k25.py` modified +9/-4 (13 lines); hunks: -17,6 +17,7; -306,6 +307,7 @@ class KimiK25ForConditionalGeneration(; symbols: KimiK25ForConditionalGeneration, __init__, _parse_and_validate_media_input, prepare_encoder_cudagraph_capture_inputs
  - `vllm/models/kimi_k3/nvidia/model.py` modified +6/-7 (13 lines); hunks: -30,6 +30,7; -1736,6 +1737,7 @@ class KimiK3ForConditionalGeneration(; symbols: KimiK3ForConditionalGeneration, __init__, prepare_encoder_cudagraph_capture_inputs, encoder_eager_forward
  - `vllm/transformers_utils/processors/kimi_k25_vision_fused.py` modified +10/-2 (12 lines); hunks: -17,6 +17,8; -238,7 +240,12 @@ def preprocess(; symbols: preprocess
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +6/-0 (6 lines); hunks: -22,6 +22,7; -187,6 +188,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/processing/test_kimi_k3.py
@@ -0,0 +1,81 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import numpy as np
+import pytest
+import torch
+from PIL import Image
diff -- vllm/model_executor/models/kimi_k25.py
@@ -17,6 +17,7 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
@@ -306,6 +307,7 @@ class KimiK25ForConditionalGeneration(
+    supports_mm_device_do_normalize = True
@@ -350,6 +352,7 @@ def __init__(
+                input_norm=build_mm_input_norm(vllm_config.model_config),
@@ -404,9 +407,6 @@ def _parse_and_validate_media_input(
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -30,6 +30,7 @@
```

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_kimi_k3.py` added +81/-0
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +9/-4; `vllm/models/kimi_k3/nvidia/model.py` modified +6/-7; `vllm/transformers_utils/processors/kimi_k25_vision_fused.py` modified +10/-2; `vllm/model_executor/models/kimi_k25_vit.py` modified +6/-0; `vllm/models/kimi_k3/amd/model.py` modified +3/-2; `vllm/models/kimi_k3/common/mm_preprocess.py` modified +4/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_kimi_k3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51274 - [ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion

- 链接: https://github.com/vllm-project/vllm/pull/51274
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_gfx942_int4.py`；关联提交 `b0e21b308352`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+346/-2，可读 patch 434 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_gfx942_int4.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion」；主要实现面是 `tests/models/kimi_k3/test_gfx942_int4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_gfx942_int4.py` added +108/-0 (108 lines); hunks: -0,0 +1,108; symbols: _FakeRocmModule, _FakeAiterOpsModule, _vllm_config, test_moe_weight_override_is_int4，涉及 `_FakeRocmModule, _FakeAiterOpsModule, _vllm_config`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_gfx942_int4.py` added +108/-0 (108 lines); hunks: -0,0 +1,108; symbols: _FakeRocmModule, _FakeAiterOpsModule, _vllm_config, test_moe_weight_override_is_int4
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_gfx942_int4.py
@@ -0,0 +1,108 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import sys
+from collections.abc import Callable
+from types import ModuleType, SimpleNamespace
+from unittest.mock import Mock, patch
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_gfx942_int4.py` added +108/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_gfx942_int4.py`, `tests/quantization/test_quantization_config_args.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59229 - [CI][Kimi-K3] Test prefix cache reuse with KV offload, P/D and DCP

- 链接: https://github.com/vllm-project/vllm/pull/59229
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_prefix_cache.py`；关联提交 `d648847fe451`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+396/-1，可读 patch 412 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kimi-K3] Test prefix cache reuse with KV offload, P/D and DCP」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_prefix_cache.py`；技术摘要: 覆盖「[CI][Kimi-K3] Test prefix cache reuse with KV offload, P/D and DCP」；主要实现面是 `tests/models/kimi_k3/test_prefix_cache.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_prefix_cache.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: Mode, name, Instance, num_gpus，涉及 `Mode, name, Instance`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_prefix_cache.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: Mode, name, Instance, num_gpus
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_prefix_cache.py
@@ -0,0 +1,375 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Kimi-K3 multi-turn prefix cache reuse with KV offload, P/D and DCP."""
+import contextlib
+import json
+import random
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_prefix_cache.py` added +375/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_prefix_cache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58344 - [ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm

- 链接: https://github.com/vllm-project/vllm/pull/58344
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/kda_checkpoint.py` 等 7 个文件；关联提交 `01549796563f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+748/-14，可读 patch 900 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_checkpoint.py` added +521/-0 (521 lines); hunks: -0,0 +1,521; symbols: _StubSpeculativeConfig, __init__, use_eagle_block_drop, _builder，涉及 `_StubSpeculativeConfig, __init__, use_eagle_block_drop`；`tests/models/kimi_k3/test_amd_kda_chunk.py` modified +56/-6 (62 lines); hunks: -13,17 +13,17; -701,6 +701,56 @@ def test_cold_rows_start_from_zero_not_from_cache_junk(use_...; symbols: _on_gfx950, _fused_chunk_available, test_cold_rows_start_from_zero_not_from_cache_junk, test_state_indices_accept_a_block_table_column，涉及 `_on_gfx950, _fused_chunk_available, test_cold_rows_start_from_zero_not_from_cache_junk`；`vllm/models/kimi_k3/amd/kda.py` modified +56/-6 (62 lines); hunks: -1,6 +1,8; -38,7 +40,11; symbols: get_state_shape, get_kv_cache_spec, __init__, _prefill_conv，涉及 `get_state_shape, get_kv_cache_spec, __init__`；`vllm/models/kimi_k3/amd/kda_metadata.py` modified +56/-0 (56 lines); hunks: -7,16 +7,23; -86,6 +93,55 @@ def prepare_chunk_metadata_device(; symbols: prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder, build, _build_checkpoint_metadata，涉及 `prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder, build`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_checkpoint.py` added +521/-0 (521 lines); hunks: -0,0 +1,521; symbols: _StubSpeculativeConfig, __init__, use_eagle_block_drop, _builder
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +56/-6 (62 lines); hunks: -13,17 +13,17; -701,6 +701,56 @@ def test_cold_rows_start_from_zero_not_from_cache_junk(use_...; symbols: _on_gfx950, _fused_chunk_available, test_cold_rows_start_from_zero_not_from_cache_junk, test_state_indices_accept_a_block_table_column
  - `vllm/models/kimi_k3/amd/kda.py` modified +56/-6 (62 lines); hunks: -1,6 +1,8; -38,7 +40,11; symbols: get_state_shape, get_kv_cache_spec, __init__, _prefill_conv
  - `vllm/models/kimi_k3/amd/kda_metadata.py` modified +56/-0 (56 lines); hunks: -7,16 +7,23; -86,6 +93,55 @@ def prepare_chunk_metadata_device(; symbols: prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder, build, _build_checkpoint_metadata
  - `vllm/models/kimi_k3/amd/ops/kda_checkpoint.py` added +41/-0 (41 lines); hunks: -0,0 +1,41; symbols: KimiK3ROCmKDAPrefillCheckpointExporter, export
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_checkpoint.py
@@ -0,0 +1,521 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The ROCm KDA prefill checkpoint: where it is taken and what it stores.
+Two things have to line up for a checkpoint to be safe: the metadata must name
+a position the chunk kernel will actually write, and the conv window saved
+there must be the one a resumed prefill would have left.
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -13,17 +13,17 @@
-def _on_gfx950() -> bool:
-    if not current_platform.is_rocm():
+def _fused_chunk_available() -> bool:
+    if not (current_platform.is_rocm() and torch.cuda.is_available()):
-    from vllm.platforms.rocm import on_gfx950
+    from vllm.models.kimi_k3.amd.ops.kda_chunk import is_fused_kda_chunk_supported
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -1,6 +1,8 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_checkpoint.py` added +521/-0; `tests/models/kimi_k3/test_amd_kda_chunk.py` modified +56/-6
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +56/-6; `vllm/models/kimi_k3/amd/kda_metadata.py` modified +56/-0; `vllm/models/kimi_k3/amd/ops/kda_checkpoint.py` added +41/-0; `vllm/models/kimi_k3/amd/ops/kda_chunk.py` modified +11/-1; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` modified +7/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58769 - [ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor …

- 链接: https://github.com/vllm-project/vllm/pull/58769
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py`；关联提交 `d848c4ed3d0c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+112/-351，可读 patch 655 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor …」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py`；技术摘要: 覆盖「[ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor …」；主要实现面是 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +59/-165 (224 lines); hunks: -12,7 +12,11; -125,33 +129,21 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused，涉及 `chunk_kda_fwd_kernel_inter_solve_fused`；`vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +47/-175 (222 lines); hunks: -17,7 +17,11; -90,86 +94,35 @@ def recompute_w_u_fwd_kernel(; symbols: recompute_w_u_fwd_kernel, recompute_w_u_fwd, chunk_gla_fwd_kernel_o, chunk_gla_fwd_o_gk，涉及 `recompute_w_u_fwd_kernel, recompute_w_u_fwd, chunk_gla_fwd_kernel_o`；`vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py` modified +6/-11 (17 lines); hunks: -12,7 +12,7; -108,20 +108,15 @@ def chunk_kda_fwd_kernel_intra_token_parallel(; symbols: chunk_kda_fwd_kernel_intra_token_parallel，涉及 `chunk_kda_fwd_kernel_intra_token_parallel`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +59/-165 (224 lines); hunks: -12,7 +12,11; -125,33 +129,21 @@ def chunk_kda_fwd_kernel_inter_solve_fused(; symbols: chunk_kda_fwd_kernel_inter_solve_fused
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +47/-175 (222 lines); hunks: -17,7 +17,11; -90,86 +94,35 @@ def recompute_w_u_fwd_kernel(; symbols: recompute_w_u_fwd_kernel, recompute_w_u_fwd, chunk_gla_fwd_kernel_o, chunk_gla_fwd_o_gk
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py` modified +6/-11 (17 lines); hunks: -12,7 +12,7; -108,20 +108,15 @@ def chunk_kda_fwd_kernel_intra_token_parallel(; symbols: chunk_kda_fwd_kernel_intra_token_parallel
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py
@@ -12,7 +12,11 @@
-from vllm.third_party.flash_linear_attention.ops.op import exp2, gather
+from vllm.third_party.flash_linear_attention.ops.op import (
+    exp2,
+    gather,
+    make_tensor_descriptor,
+)
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py
@@ -17,7 +17,11 @@
-from vllm.third_party.flash_linear_attention.ops.op import exp2, log
+from vllm.third_party.flash_linear_attention.ops.op import (
+    exp2,
+    log,
+    make_tensor_descriptor,
+)
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py
@@ -12,7 +12,7 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py` modified +59/-165; `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +47/-175; `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py` modified +6/-11
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #59257 - [Bugfix] Gate Kimi-K3 KDA warmup on sys.modules to skip Kimi import for non-Kimi models

- 链接: https://github.com/vllm-project/vllm/pull/59257
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`；关联提交 `08d77cad7be4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-2，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Gate Kimi-K3 KDA warmup on sys.modules to skip Kimi import for non-Kimi models」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`；技术摘要: 覆盖「[Bugfix] Gate Kimi-K3 KDA warmup on sys.modules to skip Kimi import for non-Kimi models」；主要实现面是 `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +6/-2 (8 lines); hunks: -4,6 +4,7; -19,7 +20,10; symbols: _get_kda_layer，涉及 `_get_kda_layer`。
- 代码 diff 细节:
  - `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +6/-2 (8 lines); hunks: -4,6 +4,7; -19,7 +20,10; symbols: _get_kda_layer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/warmup/kimi_k3_triton_warmup.py
@@ -4,6 +4,7 @@
+import sys
@@ -19,7 +20,10 @@
-    from vllm.models.kimi_k3.nvidia.kda import KimiK3DeltaAttention
+    # Kimi model construction already imports kda. Avoid importing it here.
+    kda = sys.modules.get("vllm.models.kimi_k3.nvidia.kda")
+    if kda is None:
```

- 已读文件:
  - runtime: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` modified +6/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54255 - [Kimi-K3] Add FlashInfer speculative KDA backend

- 链接: https://github.com/vllm-project/vllm/pull/54255
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `766b4ae54c49`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+383/-9，可读 patch 479 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Add FlashInfer speculative KDA backend」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Kimi-K3] Add FlashInfer speculative KDA backend」；主要实现面是 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +241/-0 (241 lines); hunks: -30,13 +30,17; -90,6 +94,25 @@ def test_kda_warmup_skips_missing_metadata(monkeypatch):; symbols: test_kda_warmup_skips_missing_metadata, test_resolve_kda_spec_decode_backend, test_kda_recoverssm_config_state_layout, test_fused_kda_decode_correctness，涉及 `test_kda_warmup_skips_missing_metadata, test_resolve_kda_spec_decode_backend, test_kda_recoverssm_config_state_layout`；`vllm/models/kimi_k3/nvidia/kda.py` modified +130/-9 (139 lines); hunks: -55,8 +55,10; -214,6 +216,73 @@ def is_flashinfer_fused_kda_decode_supported(; symbols: is_flashinfer_fused_kda_decode_supported, is_flashinfer_fused_kda_spec_decode_supported, resolve_kda_spec_decode_backend, resolve_kda_decode_backend，涉及 `is_flashinfer_fused_kda_decode_supported, is_flashinfer_fused_kda_spec_decode_supported, resolve_kda_spec_decode_backend`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +241/-0 (241 lines); hunks: -30,13 +30,17; -90,6 +94,25 @@ def test_kda_warmup_skips_missing_metadata(monkeypatch):; symbols: test_kda_warmup_skips_missing_metadata, test_resolve_kda_spec_decode_backend, test_kda_recoverssm_config_state_layout, test_fused_kda_decode_correctness
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +130/-9 (139 lines); hunks: -55,8 +55,10; -214,6 +216,73 @@ def is_flashinfer_fused_kda_decode_supported(; symbols: is_flashinfer_fused_kda_decode_supported, is_flashinfer_fused_kda_spec_decode_supported, resolve_kda_spec_decode_backend, resolve_kda_decode_backend
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -30,13 +30,17 @@
+    KimiK3DeltaAttention,
+    is_flashinfer_fused_kda_spec_decode_supported,
+    resolve_kda_spec_decode_backend,
+from vllm.models.kimi_k3.nvidia.kda_metadata import KimiK3KDAMetadata
@@ -90,6 +94,25 @@ def test_kda_warmup_skips_missing_metadata(monkeypatch):
+def test_resolve_kda_spec_decode_backend(monkeypatch: pytest.MonkeyPatch):
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -55,8 +55,10 @@
+    flashinfer_packed_fused_kda_decode,
+    has_flashinfer_packed_fused_kda_decode,
@@ -214,6 +216,73 @@ def is_flashinfer_fused_kda_decode_supported(
+def is_flashinfer_fused_kda_spec_decode_supported(
+    num_heads: int,
+    head_dim: int,
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +241/-0
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +130/-9
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57640 - [ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER

- 链接: https://github.com/vllm-project/vllm/pull/57640
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/mla.py`；关联提交 `8f24ab30a36d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+170/-8，可读 patch 208 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/mla.py`；技术摘要: 覆盖「[ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER」；主要实现面是 `vllm/models/kimi_k3/amd/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/mla.py` modified +170/-8 (178 lines); hunks: -7,16 +7,47; -38,6 +69,107 @@ def _normalize_q_kv(; symbols: KimiK3MultiHeadLatentAttentionWrapper, __init__, _fused_qk_prep_supported, _normalize_q_kv，涉及 `KimiK3MultiHeadLatentAttentionWrapper, __init__, _fused_qk_prep_supported`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/mla.py` modified +170/-8 (178 lines); hunks: -7,16 +7,47; -38,6 +69,107 @@ def _normalize_q_kv(; symbols: KimiK3MultiHeadLatentAttentionWrapper, __init__, _fused_qk_prep_supported, _normalize_q_kv
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -7,16 +7,47 @@
+from vllm.model_executor.layers.attention.attention import get_attention_context
+from vllm.platforms import current_platform
+_OPT_KV_LORA_RANK = 512
+_OPT_ROT_DIM = 64
+_OPT_MIN_SIZE = 2048
-    """Kimi-K3 MLA wrapper with eager AITER q/kv RMSNorm fusion."""
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/mla.py` modified +170/-8
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58814 - [Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound

- 链接: https://github.com/vllm-project/vllm/pull/58814
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/dspark_mla.py`；关联提交 `94d146292479`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-1，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/dspark_mla.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound」；主要实现面是 `vllm/models/kimi_k3/nvidia/dspark_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +6/-1 (7 lines); hunks: -376,7 +376,12 @@ def _has_uniform_block_layout(; symbols: _has_uniform_block_layout，涉及 `_has_uniform_block_layout`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +6/-1 (7 lines); hunks: -376,7 +376,12 @@ def _has_uniform_block_layout(; symbols: _has_uniform_block_layout
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/dspark_mla.py
@@ -376,7 +376,12 @@ def _has_uniform_block_layout(
-        if not hasattr(self, "_layers_share_kv_block_layout"):
+        key = tuple(cl.kv_cache.data_ptr() for cl in cache_layers)
+        if getattr(self, "_kv_cache_ptrs_key", None) != key:
+            assert not torch.cuda.is_current_stream_capturing()
+            self._kv_cache_ptrs_key = key
+            if hasattr(self, "_context_cache_ptrs"):
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/dspark_mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54956 - [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP

- 链接: https://github.com/vllm-project/vllm/pull/54956
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`；关联提交 `a7ff44355c1c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+97/-16，可读 patch 237 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP」；主要实现面是 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +95/-15 (110 lines); hunks: -23,6 +23,7; -56,21 +57,26 @@ def _build_transform(device: torch.device) -> KimiRoutedOutp...; symbols: _build_transform, _tail_runner, method, _rank_partials，涉及 `_build_transform, _tail_runner, method`；`vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +2/-1 (3 lines); hunks: -6,6 +6,7; -33,7 +34,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +95/-15 (110 lines); hunks: -23,6 +23,7; -56,21 +57,26 @@ def _build_transform(device: torch.device) -> KimiRoutedOutp...; symbols: _build_transform, _tail_runner, method, _rank_partials
  - `vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +2/-1 (3 lines); hunks: -6,6 +6,7; -33,7 +34,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_latent_moe_runner.py
@@ -23,6 +23,7 @@
+from vllm.models.kimi_k3.amd import latent_moe_runner
@@ -56,21 +57,26 @@ def _build_transform(device: torch.device) -> KimiRoutedOutputTransform:
-    transform: KimiRoutedOutputTransform, tp_size: int
+    transform: KimiRoutedOutputTransform, tp_world: int, use_ep: bool = False
+    ``tp_world`` is the size of the TP process group, which is what the hidden
+    dim is split by. Under expert parallelism the MoE config reports
diff -- vllm/models/kimi_k3/amd/latent_moe_runner.py
@@ -6,6 +6,7 @@
+    get_tensor_model_parallel_world_size,
@@ -33,7 +34,7 @@ def __init__(
-        tp_size = self.moe_config.tp_size
+        tp_size = get_tensor_model_parallel_world_size()
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` modified +95/-15
  - runtime: `vllm/models/kimi_k3/amd/latent_moe_runner.py` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58651 - [KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel

- 链接: https://github.com/vllm-project/vllm/pull/58651
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `39d49539de86`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+140/-7，可读 patch 174 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +16/-7 (23 lines); hunks: -30,13 +30,17; -451,14 +455,19 @@ def attention_qkvpacked(; symbols: attention_qkvpacked，涉及 `attention_qkvpacked`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +16/-7 (23 lines); hunks: -30,13 +30,17; -451,14 +455,19 @@ def attention_qkvpacked(; symbols: attention_qkvpacked
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -30,13 +30,17 @@
+from vllm.model_executor.layers.rotary_embedding.packed_qk_rope import (
+    packed_qk_rope_,
+)
+from vllm.triton_utils import HAS_TRITON
@@ -451,14 +455,19 @@ def attention_qkvpacked(
-        xq, xk, xv = torch.unbind(xqkv, dim=-3)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +16/-7
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_apply_rotary_emb.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58372 - [Bugfix][Reasoning] Count Kimi K3 reasoning tokens

- 链接: https://github.com/vllm-project/vllm/pull/58372
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`；关联提交 `9bf44c40134c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+91/-4，可读 patch 130 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Reasoning] Count Kimi K3 reasoning tokens」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix][Reasoning] Count Kimi K3 reasoning tokens」；主要实现面是 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +51/-4 (55 lines); hunks: -19,6 +19,9; -119,6 +122,54 @@ def test_is_reasoning_end_ignores_stale_close_from_prior_tu...; symbols: DummyTokenizer, test_is_reasoning_end_ignores_stale_close_from_prior_turn, test_count_reasoning_tokens_matches_think_channel, test_count_reasoning_tokens_is_zero_when_thinking_disabled，涉及 `DummyTokenizer, test_is_reasoning_end_ignores_stale_close_from_prior_turn, test_count_reasoning_tokens_matches_think_channel`；`vllm/reasoning/kimi_k3_reasoning_parser.py` modified +40/-0 (40 lines); hunks: -134,6 +134,9 @@ def __init__(self, tokenizer: PreTrainedTokenizerBase, *args...; -211,6 +214,43 @@ def extract_content_ids(self, input_ids: list[int]) -> list...; symbols: __init__, extract_content_ids, count_reasoning_tokens, _strip_content_wrapper，涉及 `__init__, extract_content_ids, count_reasoning_tokens`。
- 代码 diff 细节:
  - `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +51/-4 (55 lines); hunks: -19,6 +19,9; -119,6 +122,54 @@ def test_is_reasoning_end_ignores_stale_close_from_prior_tu...; symbols: DummyTokenizer, test_is_reasoning_end_ignores_stale_close_from_prior_turn, test_count_reasoning_tokens_matches_think_channel, test_count_reasoning_tokens_is_zero_when_thinking_disabled
  - `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +40/-0 (40 lines); hunks: -134,6 +134,9 @@ def __init__(self, tokenizer: PreTrainedTokenizerBase, *args...; -211,6 +214,43 @@ def extract_content_ids(self, input_ids: list[int]) -> list...; symbols: __init__, extract_content_ids, count_reasoning_tokens, _strip_content_wrapper
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_kimi_k3_reasoning_parser.py
@@ -19,6 +19,9 @@
+OPEN_IDS = [1, 2, 3]
+CLOSE_IDS = [4, 2, 3]
+RESPONSE_OPEN_IDS = [ord(ch) for ch in RESPONSE_OPEN]
@@ -119,6 +122,54 @@ def test_is_reasoning_end_ignores_stale_close_from_prior_turn():
+@pytest.mark.parametrize(
+    ("token_ids", "expected"),
diff -- vllm/reasoning/kimi_k3_reasoning_parser.py
@@ -134,6 +134,9 @@ def __init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
+        self._response_open_ids = tokenizer.encode(
+            self._response_open, add_special_tokens=False
+        )
@@ -211,6 +214,43 @@ def extract_content_ids(self, input_ids: list[int]) -> list[int]:
+    def count_reasoning_tokens(self, token_ids: Sequence[int]) -> int:
+        if not self._thinking_enabled:
```

- 已读文件:
  - tests: `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +51/-4
  - runtime: `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +40/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_kimi_k3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58045 - [ROCm][Kimi-K3] Optimize low-concurrency speculative KDA

- 链接: https://github.com/vllm-project/vllm/pull/58045
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/__init__.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`；关联提交 `1417022c3dbb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+201/-27，可读 patch 479 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Optimize low-concurrency speculative KDA」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`, `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Optimize low-concurrency speculative KDA」；主要实现面是 `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`, `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +103/-15 (118 lines); hunks: -164,15 +164,24 @@ def fused_recurrent_kda_fwd_kernel(; -208,6 +217,14 @@ def fused_recurrent_kda_fwd_kernel(; symbols: fused_recurrent_kda_fwd_kernel，涉及 `fused_recurrent_kda_fwd_kernel`；`tests/models/kimi_k3/test_kda.py` modified +56/-9 (65 lines); hunks: -22,6 +22,9; -44,10 +47,12; symbols: test_kda_warmup_skips_missing_metadata, test_packed_kda_decode_correctness, test_kda_spec_decode_correctness，涉及 `test_kda_warmup_skips_missing_metadata, test_packed_kda_decode_correctness, test_kda_spec_decode_correctness`；`tests/models/kimi_k3/test_kda_metadata.py` modified +19/-0 (19 lines); hunks: -49,6 +49,7; -409,6 +410,7 @@ def test_internal_checkpoint_metadata_skips_unaligned_offset():; symbols: test_internal_checkpoint_metadata_skips_unaligned_offset，涉及 `test_internal_checkpoint_metadata_skips_unaligned_offset`；`vllm/models/kimi_k3/amd/kda.py` modified +9/-0 (9 lines); hunks: -438,6 +438,14 @@ def _forward(; -457,6 +465,7 @@ def _forward(; symbols: _forward，涉及 `_forward`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +103/-15 (118 lines); hunks: -164,15 +164,24 @@ def fused_recurrent_kda_fwd_kernel(; -208,6 +217,14 @@ def fused_recurrent_kda_fwd_kernel(; symbols: fused_recurrent_kda_fwd_kernel
  - `tests/models/kimi_k3/test_kda.py` modified +56/-9 (65 lines); hunks: -22,6 +22,9; -44,10 +47,12; symbols: test_kda_warmup_skips_missing_metadata, test_packed_kda_decode_correctness, test_kda_spec_decode_correctness
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +19/-0 (19 lines); hunks: -49,6 +49,7; -409,6 +410,7 @@ def test_internal_checkpoint_metadata_skips_unaligned_offset():; symbols: test_internal_checkpoint_metadata_skips_unaligned_offset
  - `vllm/models/kimi_k3/amd/kda.py` modified +9/-0 (9 lines); hunks: -438,6 +438,14 @@ def _forward(; -457,6 +465,7 @@ def _forward(; symbols: _forward
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/__init__.py` modified +4/-3 (7 lines); hunks: -16,9 +16,10
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py
@@ -164,15 +164,24 @@ def fused_recurrent_kda_fwd_kernel(
+    IS_SINGLE_SEQUENCE: tl.constexpr,
+    SEQUENCE_LENGTH: tl.constexpr,
-    i_n, i_h = i_nh // H, i_nh % H
-    bos = tl.load(cu_seqlens + i_n).to(tl.int64)
-    eos = tl.load(cu_seqlens + i_n + 1).to(tl.int64)
-    sequence_length = eos - bos
diff -- tests/models/kimi_k3/test_kda.py
@@ -22,6 +22,9 @@
+from vllm.models.kimi_k3.amd.ops.third_party.kda import (
+    fused_recurrent_kda as fused_recurrent_kda_amd,
+)
@@ -44,10 +47,12 @@
-    fused_recurrent_kda,
+from vllm.models.kimi_k3.nvidia.ops.third_party.kda import (
diff -- tests/models/kimi_k3/test_kda_metadata.py
@@ -49,6 +49,7 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +103/-15; `vllm/models/kimi_k3/amd/kda.py` modified +9/-0; `vllm/models/kimi_k3/amd/ops/third_party/kda/__init__.py` modified +4/-3
  - tests: `tests/models/kimi_k3/test_kda.py` modified +56/-9; `tests/models/kimi_k3/test_kda_metadata.py` modified +19/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58527 - [Kimi-K3][Perf] Dispatch GEMM for vision patch embedder

- 链接: https://github.com/vllm-project/vllm/pull/58527
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `ade1056ee5af`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+30/-17，可读 patch 80 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][Perf] Dispatch GEMM for vision patch embedder」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Kimi-K3][Perf] Dispatch GEMM for vision patch embedder」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +4/-16 (20 lines); hunks: -21,6 +21,7; -194,7 +195,7 @@ def __init__(; symbols: __init__, forward, _proj, Rope2DPosEmbRepeated，涉及 `__init__, forward, _proj`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +4/-16 (20 lines); hunks: -21,6 +21,7; -194,7 +195,7 @@ def __init__(; symbols: __init__, forward, _proj, Rope2DPosEmbRepeated
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -21,6 +21,7 @@
+from vllm.model_executor.layers.conv import Conv2dLayer
@@ -194,7 +195,7 @@ def __init__(
-        self.proj = nn.Conv2d(
+        self.proj = Conv2dLayer(
@@ -220,26 +221,13 @@ def forward(
-        x = self._proj(x).view(x.size(0), -1)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +4/-16
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_conv.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58012 - [CI][ROCm] Add an MI355 Kimi-K3 unit test group

- 链接: https://github.com/vllm-project/vllm/pull/58012
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_attn_res.py`；关联提交 `c4cfd7007bad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+102/-0，可读 patch 158 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][ROCm] Add an MI355 Kimi-K3 unit test group」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_attn_res.py`；技术摘要: 覆盖「[CI][ROCm] Add an MI355 Kimi-K3 unit test group」；主要实现面是 `tests/models/kimi_k3/test_attn_res.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_attn_res.py` modified +23/-0 (23 lines); hunks: -17,6 +17,26; -79,6 +99,7 @@ def test_attn_res(; symbols: _on_rocm_below_10, _skip_on_old_rocm, _randn_with_row_padding, test_attn_res，涉及 `_on_rocm_below_10, _skip_on_old_rocm, _randn_with_row_padding`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_attn_res.py` modified +23/-0 (23 lines); hunks: -17,6 +17,26; -79,6 +99,7 @@ def test_attn_res(; symbols: _on_rocm_below_10, _skip_on_old_rocm, _randn_with_row_padding, test_attn_res
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_attn_res.py
@@ -17,6 +17,26 @@
+def _on_rocm_below_10() -> bool:
+    if not current_platform.is_rocm():
+        return False
+    from vllm.platforms.rocm import get_rocm_version
+    return (get_rocm_version() or (0,)) < (10,)
+# The Triton bundled with ROCm < 10 (3.7.x) crashes in the AMD
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_attn_res.py` modified +23/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_attn_res.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52988 - [Spec decode] Support variable-length decode for Kimi-K3 adaptive ver

- 链接: https://github.com/vllm-project/vllm/pull/52988
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/dspark_mla.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；关联提交 `88aa0d287dd3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+203/-22，可读 patch 510 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec decode] Support variable-length decode for Kimi-K3 adaptive ver」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/dspark_mla.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；技术摘要: 覆盖「[Spec decode] Support variable-length decode for Kimi-K3 adaptive ver」；主要实现面是 `vllm/models/kimi_k3/nvidia/dspark_mla.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +29/-1 (30 lines); hunks: -15,7 +15,10; -188,6 +191,18 @@ def __init__(; symbols: __init__, mapper, markov_embed, markov_bias，涉及 `__init__, mapper, markov_embed`；`vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +17/-1 (18 lines); hunks: -25,7 +25,7; -305,6 +305,10 @@ def commit_recoverssm_state(; symbols: commit_recoverssm_state, KimiK3KDAMetadataBuilder, __init__, build，涉及 `commit_recoverssm_state, KimiK3KDAMetadataBuilder, __init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +29/-1 (30 lines); hunks: -15,7 +15,10; -188,6 +191,18 @@ def __init__(; symbols: __init__, mapper, markov_embed, markov_bias
  - `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +17/-1 (18 lines); hunks: -25,7 +25,7; -305,6 +305,10 @@ def commit_recoverssm_state(; symbols: commit_recoverssm_state, KimiK3KDAMetadataBuilder, __init__, build
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/dspark_mla.py
@@ -15,7 +15,10 @@
-from vllm.model_executor.models.qwen3_dspark import DSparkMarkovHead
+from vllm.model_executor.models.qwen3_dspark import (
+    DSparkConfidenceHead,
+    DSparkMarkovHead,
+)
@@ -188,6 +191,18 @@ def __init__(
diff -- vllm/models/kimi_k3/nvidia/kda_metadata.py
@@ -25,7 +25,7 @@
-from vllm.v1.attention.backend import CommonAttentionMetadata
+from vllm.v1.attention.backend import AttentionCGSupport, CommonAttentionMetadata
@@ -305,6 +305,10 @@ def commit_recoverssm_state(
+    # Overrides GDN's UNIFORM_BATCH: adaptive verification requires ALWAYS from every
+    # builder, and KDA reads per-request offsets off device within a fixed k+1 window,
+    # so one k+1 graph replays any 1..k+1 mix.
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +29/-1; `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +17/-1
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `tests/v1/worker/test_mamba_hybrid_model_state.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50592 - [Kimi-K3][AMD] Return KDA and MLA projection outputs directly

- 链接: https://github.com/vllm-project/vllm/pull/50592
- 状态/时间: merged / 2026-09-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_nvidia_kda_direct_return.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/models/kimi_k3/amd/kda.py` 等 7 个文件；关联提交 `382970ee6ca4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+170/-33，可读 patch 337 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][AMD] Return KDA and MLA projection outputs directly」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`；技术摘要: 覆盖「[Kimi-K3][AMD] Return KDA and MLA projection outputs directly」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_direct_return.py` added +72/-0 (72 lines); hunks: -0,0 +1,72; symbols: _ReturningAttention, __init__, forward, _TupleProjection，涉及 `_ReturningAttention, __init__, forward`；`vllm/models/kimi_k3/amd/linear.py` modified +25/-16 (41 lines); hunks: -456,9 +456,8 @@ def forward(; -582,25 +581,29 @@ def _run_self_attn(; symbols: forward, KimiDecoderLayer, _run_self_attn, forward_attn_residual，涉及 `forward, KimiDecoderLayer, _run_self_attn`；`tests/models/kimi_k3/test_amd_mla_direct_return.py` added +38/-0 (38 lines); hunks: -0,0 +1,38; symbols: _DirectMLA, __init__, forward, _make_layer，涉及 `_DirectMLA, __init__, forward`；`tests/models/kimi_k3/test_nvidia_kda_direct_return.py` added +31/-0 (31 lines); hunks: -0,0 +1,31; symbols: _ReturningSharedKDA, __init__, forward, test_low_rank_kda_caller_returns_projection_storage_directly，涉及 `_ReturningSharedKDA, __init__, forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_direct_return.py` added +72/-0 (72 lines); hunks: -0,0 +1,72; symbols: _ReturningAttention, __init__, forward, _TupleProjection
  - `vllm/models/kimi_k3/amd/linear.py` modified +25/-16 (41 lines); hunks: -456,9 +456,8 @@ def forward(; -582,25 +581,29 @@ def _run_self_attn(; symbols: forward, KimiDecoderLayer, _run_self_attn, forward_attn_residual
  - `tests/models/kimi_k3/test_amd_mla_direct_return.py` added +38/-0 (38 lines); hunks: -0,0 +1,38; symbols: _DirectMLA, __init__, forward, _make_layer
  - `tests/models/kimi_k3/test_nvidia_kda_direct_return.py` added +31/-0 (31 lines); hunks: -0,0 +1,31; symbols: _ReturningSharedKDA, __init__, forward, test_low_rank_kda_caller_returns_projection_storage_directly
  - `vllm/models/kimi_k3/nvidia/model.py` modified +0/-11 (11 lines); hunks: -922,14 +922,12 @@ def __init__(; -959,7 +957,6 @@ def __init__(; symbols: __init__, _run_self_attn
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_direct_return.py
@@ -0,0 +1,72 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import torch
+from torch import nn
+from vllm.models.kimi_k3.amd.kda import KimiK3DeltaAttention
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -456,9 +456,8 @@ def forward(
-        output: torch.Tensor,
-    ) -> None:
-        output[:] = self.mla_attn(positions, hidden_states)
+    ) -> torch.Tensor:
+        return self.mla_attn(positions, hidden_states)
@@ -582,25 +581,29 @@ def _run_self_attn(
diff -- tests/models/kimi_k3/test_amd_mla_direct_return.py
@@ -0,0 +1,38 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_direct_return.py` added +72/-0; `tests/models/kimi_k3/test_amd_mla_direct_return.py` added +38/-0; `tests/models/kimi_k3/test_nvidia_kda_direct_return.py` added +31/-0
  - runtime: `vllm/models/kimi_k3/amd/linear.py` modified +25/-16; `vllm/models/kimi_k3/nvidia/model.py` modified +0/-11; `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +2/-3; `vllm/models/kimi_k3/amd/kda.py` modified +2/-3
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_nvidia_kda_direct_return.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57430 - [Quantization] Support kimi-k3 routed expert quant

- 链接: https://github.com/vllm-project/vllm/pull/57430
- 状态/时间: merged / 2026-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `76d517fd1279`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization] Support kimi-k3 routed expert quant」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Quantization] Support kimi-k3 routed expert quant」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2 (4 lines); hunks: -677,7 +677,7 @@ def __init__(; -694,7 +694,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2 (4 lines); hunks: -677,7 +677,7 @@ def __init__(; -694,7 +694,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -677,7 +677,7 @@ def __init__(
-                quant_config=None,
+                quant_config=quant_config,
@@ -694,7 +694,7 @@ def __init__(
-                quant_config=None,
+                quant_config=quant_config,
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #57098 - [Kimi K3 Bug] Fix kimi k3 reasoning parser

- 链接: https://github.com/vllm-project/vllm/pull/57098
- 状态/时间: merged / 2026-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/reasoning/kimi_k3_reasoning_parser.py`；关联提交 `f3aa88d23095`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-5，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3 Bug] Fix kimi k3 reasoning parser」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/reasoning/kimi_k3_reasoning_parser.py`；技术摘要: 覆盖「[Kimi K3 Bug] Fix kimi k3 reasoning parser」；主要实现面是 `vllm/reasoning/kimi_k3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +10/-5 (15 lines); hunks: -256,11 +256,13 @@ def extract_reasoning(; -270,11 +272,14 @@ def extract_reasoning(; symbols: extract_reasoning，涉及 `extract_reasoning`。
- 代码 diff 细节:
  - `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +10/-5 (15 lines); hunks: -256,11 +256,13 @@ def extract_reasoning(; -270,11 +272,14 @@ def extract_reasoning(; symbols: extract_reasoning
- 关键代码摘录:

```diff
diff -- vllm/reasoning/kimi_k3_reasoning_parser.py
@@ -256,11 +256,13 @@ def extract_reasoning(
-        Handles three shapes:
-          * no think channel at all   -> ``(None, model_output)`` (all content)
+        Handles four shapes:
+          * response opener without think markers -> no think channel; all content
+          * neither marker present     -> truncated reasoning after a consumed
+            generation prefix
```

- 已读文件:
  - runtime: `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +10/-5
- 验证与风险: runtime 路径改动集中在 `vllm/reasoning/kimi_k3_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51483 - [Bugfix][Kimi-K3] Do not classify a stateless first chunk as a decode

- 链接: https://github.com/vllm-project/vllm/pull/51483
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；关联提交 `f8b5c11468f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+113/-2，可读 patch 128 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Do not classify a stateless first chunk as a decode」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Do not classify a stateless first chunk as a decode」；主要实现面是 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda_metadata.py` modified +88/-0 (88 lines); hunks: -934,3 +934,91 @@ def test_aligned_block_table_matches_shared_gdn():; symbols: test_aligned_block_table_matches_shared_gdn, _build_non_spec, test_one_token_first_chunk_excludes_padding, test_one_token_chunk_classification，涉及 `test_aligned_block_table_matches_shared_gdn, _build_non_spec, test_one_token_first_chunk_excludes_padding`；`vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +25/-2 (27 lines); hunks: -427,10 +427,33 @@ def build( # type: ignore[override]; symbols: build，涉及 `build`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +88/-0 (88 lines); hunks: -934,3 +934,91 @@ def test_aligned_block_table_matches_shared_gdn():; symbols: test_aligned_block_table_matches_shared_gdn, _build_non_spec, test_one_token_first_chunk_excludes_padding, test_one_token_chunk_classification
  - `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +25/-2 (27 lines); hunks: -427,10 +427,33 @@ def build( # type: ignore[override]; symbols: build
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda_metadata.py
@@ -934,3 +934,91 @@ def test_aligned_block_table_matches_shared_gdn():
+def _build_non_spec(batch, is_prefilling, full_cuda_graph=False):
+    common_attn_metadata = create_common_attn_metadata(
+        batch, BLOCK_SIZE, DEVICE
+    ).replace(
+        is_prefilling=None
+        if is_prefilling is None
diff -- vllm/models/kimi_k3/nvidia/kda_metadata.py
@@ -427,10 +427,33 @@ def build(  # type: ignore[override]
-            # The runner orders ordinary decodes before prefills.
+            # V2 already excludes prefills from full decode graphs via has_prefill.
+            # Classify first chunks as prefills to mask recycled state;
+            # resumed one-token chunks can still use the decode kernels.
+            assert m.seq_lens_cpu_upper_bound is not None
+            query_lens_cpu = query_start_loc_cpu.diff()
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda_metadata.py` modified +88/-0
  - runtime: `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +25/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda_metadata.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56526 - [ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill

- 链接: https://github.com/vllm-project/vllm/pull/56526
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/ops/kda_chunk.py`；关联提交 `06e57f622cf5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+5/-3，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/amd/ops/kda_chunk.py`；技术摘要: 覆盖「[ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill」；主要实现面是 `vllm/models/kimi_k3/amd/ops/kda_chunk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/ops/kda_chunk.py` modified +2/-2 (4 lines); hunks: -286,9 +286,9 @@ def fused_kda_chunk(; symbols: fused_kda_chunk，涉及 `fused_kda_chunk`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/ops/kda_chunk.py` modified +2/-2 (4 lines); hunks: -286,9 +286,9 @@ def fused_kda_chunk(; symbols: fused_kda_chunk
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/ops/kda_chunk.py
@@ -286,9 +286,9 @@ def fused_kda_chunk(
-        else checkpoint_state_indices.to(torch.int32),
+        else checkpoint_state_indices.to(torch.int32).contiguous(),
-        None if state_indices is None else state_indices.to(torch.int32),
+        None if state_indices is None else state_indices.to(torch.int32).contiguous(),
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_chunk.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #55426 - [Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper

- 链接: https://github.com/vllm-project/vllm/pull/55426
- 状态/时间: merged / 2026-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`；关联提交 `0c1e89ceb92b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+239/-43，可读 patch 406 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` modified +91/-14 (105 lines); hunks: -18,6 +18,8; -91,14 +93,61 @@ def _fma_f32_bf16(; symbols: _fma_f32_bf16, _fma_f32_bf16_portable, _has_mixed_precision_bf16_fma, _KdaSkinnyNGemm，涉及 `_fma_f32_bf16, _fma_f32_bf16_portable, _has_mixed_precision_bf16_fma`；`vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +47/-28 (75 lines); hunks: -65,6 +65,20; -749,14 +763,16 @@ def run_qkvg() -> torch.Tensor:; symbols: _kda_qkvg_flashinfer_backend, ProjectionSpec, run_qkvg, run_fab_fb，涉及 `_kda_qkvg_flashinfer_backend, ProjectionSpec, run_qkvg`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` modified +91/-14 (105 lines); hunks: -18,6 +18,8; -91,14 +93,61 @@ def _fma_f32_bf16(; symbols: _fma_f32_bf16, _fma_f32_bf16_portable, _has_mixed_precision_bf16_fma, _KdaSkinnyNGemm
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +47/-28 (75 lines); hunks: -65,6 +65,20; -749,14 +763,16 @@ def run_qkvg() -> torch.Tensor:; symbols: _kda_qkvg_flashinfer_backend, ProjectionSpec, run_qkvg, run_fab_fb
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py
@@ -18,6 +18,8 @@
+from vllm.platforms import current_platform
@@ -91,14 +93,61 @@ def _fma_f32_bf16(
+@dsl_user_op
+def _fma_f32_bf16_portable(
+    a: BFloat16,
+    b: BFloat16,
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -65,6 +65,20 @@
+def _kda_qkvg_flashinfer_backend() -> Literal["cute-dsl"] | None:
+    """Return the tested FlashInfer backend for the low-M QKVG branch.
+    FlashInfer's ``cute-dsl`` BF16 GEMM supports SM100 and SM103, but rejects
+    SM90 during backend validation. Other capabilities use ``torch.mm`` for
+    QKVG while retaining the concurrent F_A/beta and F_B branch.
+    """
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` modified +91/-14; `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +47/-28
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55356 - [Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch

- 链接: https://github.com/vllm-project/vllm/pull/55356
- 状态/时间: merged / 2026-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/dspark_mla.py`；关联提交 `1e1060f9988f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+216/-39，可读 patch 385 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/dspark_mla.py`；技术摘要: 覆盖「[Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch」；主要实现面是 `vllm/models/kimi_k3/nvidia/dspark_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +21/-5 (26 lines); hunks: -28,6 +28,10; -233,6 +237,13 @@ def _build_fused_context_kv_metadata(self) -> None:; symbols: _duplicate_context_kv_weights, _build_fused_context_kv_metadata, _precompute_fused_context_kv，涉及 `_duplicate_context_kv_weights, _build_fused_context_kv_metadata, _precompute_fused_context_kv`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +21/-5 (26 lines); hunks: -28,6 +28,10; -233,6 +237,13 @@ def _build_fused_context_kv_metadata(self) -> None:; symbols: _duplicate_context_kv_weights, _build_fused_context_kv_metadata, _precompute_fused_context_kv
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/dspark_mla.py
@@ -28,6 +28,10 @@
+_GROUPED_KV_CACHE_DTYPES = frozenset(
+    {"auto", "bfloat16", "fp8", "fp8_e4m3", "fp8_e5m2"}
+)
@@ -233,6 +237,13 @@ def _build_fused_context_kv_metadata(self) -> None:
+        self._context_kv_scales: torch.Tensor | None = None
+        if attn0.kv_cache_dtype in _GROUPED_KV_CACHE_DTYPES and is_quantized_kv_cache(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +21/-5
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_cache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56159 - [Kimi K3 Perf] Avoid KDA mixed-batch gather/scatter, 5.2%~7.7% E2E Throughput Improvement

- 链接: https://github.com/vllm-project/vllm/pull/56159
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` 等 6 个文件；关联提交 `86aca6619161`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+66/-5，可读 patch 261 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3 Perf] Avoid KDA mixed-batch gather/scatter, 5.2%~7.7% E2E Throughput Improvement」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `tests/models/kimi_k3/test_kda.py`；技术摘要: 覆盖「[Kimi K3 Perf] Avoid KDA mixed-batch gather/scatter, 5.2%~7.7% E2E Throughput Improvement」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `tests/models/kimi_k3/test_kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +33/-3 (36 lines); hunks: -903,6 +903,8 @@ def _forward(; -981,6 +983,18 @@ def _forward(; symbols: _forward, _prefill_conv，涉及 `_forward, _prefill_conv`；`vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +13/-0 (13 lines); hunks: -270,6 +270,8 @@ class KDACheckpointMetadata:; -422,6 +424,8 @@ def build( # type: ignore[override]; symbols: KDACheckpointMetadata, KimiK3KDAMetadata, build，涉及 `KDACheckpointMetadata, KimiK3KDAMetadata, build`；`tests/models/kimi_k3/test_kda.py` modified +7/-0 (7 lines); hunks: -330,6 +330,7 @@ def test_chunk_kda_fused_gate_cumsum_matches_unfused(; -343,8 +344,10 @@ def test_chunk_kda_fused_gate_cumsum_matches_unfused(; symbols: test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness，涉及 `test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness`；`vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` modified +6/-1 (7 lines); hunks: -598,6 +598,7 @@ def _chunk_kda_fwd_with_cumulative_g(; -642,7 +643,7 @@ def _chunk_kda_fwd_with_cumulative_g(; symbols: _chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate，涉及 `_chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +33/-3 (36 lines); hunks: -903,6 +903,8 @@ def _forward(; -981,6 +983,18 @@ def _forward(; symbols: _forward, _prefill_conv
  - `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +13/-0 (13 lines); hunks: -270,6 +270,8 @@ class KDACheckpointMetadata:; -422,6 +424,8 @@ def build( # type: ignore[override]; symbols: KDACheckpointMetadata, KimiK3KDAMetadata, build
  - `tests/models/kimi_k3/test_kda.py` modified +7/-0 (7 lines); hunks: -330,6 +330,7 @@ def test_chunk_kda_fused_gate_cumsum_matches_unfused(; -343,8 +344,10 @@ def test_chunk_kda_fused_gate_cumsum_matches_unfused(; symbols: test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness
  - `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` modified +6/-1 (7 lines); hunks: -598,6 +598,7 @@ def _chunk_kda_fwd_with_cumulative_g(; -642,7 +643,7 @@ def _chunk_kda_fwd_with_cumulative_g(; symbols: _chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +4/-0 (4 lines); hunks: -512,6 +512,8 @@ def test_mixed_regular_and_spec_decode_uses_packed_decode_me...; -539,6 +541,8 @@ def test_mixed_regular_and_spec_decode_excludes_request_padd...; symbols: test_mixed_regular_and_spec_decode_uses_packed_decode_metadata, test_mixed_regular_and_spec_decode_excludes_request_padding
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -903,6 +903,8 @@ def _forward(
+        spec_token_start = m.spec_token_start
+        non_spec_token_start = m.non_spec_token_start
@@ -981,6 +983,18 @@ def _forward(
+            elif spec_token_start is not None:
+                assert non_spec_token_start is not None
+                spec_end = spec_token_start + m.num_spec_decode_tokens
diff -- vllm/models/kimi_k3/nvidia/kda_metadata.py
@@ -270,6 +270,8 @@ class KDACheckpointMetadata:
+    spec_token_start: int | None = None
+    non_spec_token_start: int | None = None
@@ -422,6 +424,8 @@ def build(  # type: ignore[override]
+        spec_token_start = None
+        non_spec_token_start = None
@@ -518,6 +522,13 @@ def build(  # type: ignore[override]
diff -- tests/models/kimi_k3/test_kda.py
@@ -330,6 +330,7 @@ def test_chunk_kda_fused_gate_cumsum_matches_unfused(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +33/-3; `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +13/-0; `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` modified +6/-1; `vllm/models/kimi_k3/nvidia/ops/third_party/kda/fused_recurrent.py` modified +3/-1
  - tests: `tests/models/kimi_k3/test_kda.py` modified +7/-0; `tests/models/kimi_k3/test_kda_metadata.py` modified +4/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54038 - [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland

- 链接: https://github.com/vllm-project/vllm/pull/54038
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；关联提交 `9521c60bdc0c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+3818/-33，可读 patch 1639 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_chunk.py` added +859/-0 (859 lines); hunks: -0,0 +1,859; symbols: _on_gfx950, _requires_kernel, _inputs, _run，涉及 `_on_gfx950, _requires_kernel, _inputs`；`vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +294/-0 (294 lines); hunks: -0,0 +1,294; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like，涉及 `is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue`；`vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +179/-0 (179 lines); hunks: -0,0 +1,179; symbols: chunk_kda_prefill，涉及 `chunk_kda_prefill`；`vllm/models/kimi_k3/amd/kda.py` modified +44/-23 (67 lines); hunks: -35,19 +35,19; -210,10 +210,21 @@ def __init__(; symbols: __init__, _prefill_conv，涉及 `__init__, _prefill_conv`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` added +859/-0 (859 lines); hunks: -0,0 +1,859; symbols: _on_gfx950, _requires_kernel, _inputs, _run
  - `vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +294/-0 (294 lines); hunks: -0,0 +1,294; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like
  - `vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +179/-0 (179 lines); hunks: -0,0 +1,179; symbols: chunk_kda_prefill
  - `vllm/models/kimi_k3/amd/kda.py` modified +44/-23 (67 lines); hunks: -35,19 +35,19; -210,10 +210,21 @@ def __init__(; symbols: __init__, _prefill_conv
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -0,0 +1,859 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The fused ROCm KDA chunk kernel must match the Triton chunk path.
+The fused kernel reassociates nothing, but it keeps the chunk states in
+registers and rounds them to bfloat16 only where the Triton path does, so the
+outputs agree to bfloat16 rounding and the final states nearly exactly.
diff -- vllm/models/kimi_k3/amd/ops/kda_chunk.py
@@ -0,0 +1,294 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm entry point for the fused Kimi-K3 KDA chunk kernel.
+The kernel in ``csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu``
+replaces the chunk-state recurrence and the output GEMM of the Triton chunk
+path with a single launch that keeps the per-chunk state in registers, so the
diff -- vllm/models/kimi_k3/amd/ops/kda_prefill.py
@@ -0,0 +1,179 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` added +859/-0
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +294/-0; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +179/-0; `vllm/models/kimi_k3/amd/kda.py` modified +44/-23
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55924 - [Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered`

- 链接: https://github.com/vllm-project/vllm/pull/55924
- 状态/时间: merged / 2026-09-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `bfb443a6b6f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered`」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered`」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +1/-1 (2 lines); hunks: -415,7 +415,7 @@ def _store_cache_checkpoints_kernel(; symbols: _store_cache_checkpoints_kernel，涉及 `_store_cache_checkpoints_kernel`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +1/-1 (2 lines); hunks: -415,7 +415,7 @@ def _store_cache_checkpoints_kernel(; symbols: _store_cache_checkpoints_kernel
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -415,7 +415,7 @@ def _store_cache_checkpoints_kernel(
-    state_idx = tl.load(checkpoint_state_indices_ptr + seq_idx)
+    state_idx = tl.load(checkpoint_state_indices_ptr + seq_idx).to(tl.int64)
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/kda.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #53379 - [Bugfix] Fix Kimi K3 loading with interleaved weight streams

- 链接: https://github.com/vllm-project/vllm/pull/53379
- 状态/时间: merged / 2026-09-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `f998862d46e7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+80/-2，可读 patch 98 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Kimi K3 loading with interleaved weight streams」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix] Fix Kimi K3 loading with interleaved weight streams」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +8/-2 (10 lines); hunks: -1705,12 +1705,15 @@ def compute_logits(; -2155,3 +2158,6 @@ def get_mamba_state_copy_func(cls):; symbols: compute_logits, load_weights, process_weights_after_loading, get_spec_layer_idx_from_weight_name，涉及 `compute_logits, load_weights, process_weights_after_loading`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +8/-2 (10 lines); hunks: -1705,12 +1705,15 @@ def compute_logits(; -2155,3 +2158,6 @@ def get_mamba_state_copy_func(cls):; symbols: compute_logits, load_weights, process_weights_after_loading, get_spec_layer_idx_from_weight_name
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -1705,12 +1705,15 @@ def compute_logits(
-        loaded = loader.load_weights(weights)
+        return loader.load_weights(weights)
+    def process_weights_after_loading(self) -> None:
+        # A parent AutoWeightsLoader may invoke load_weights repeatedly for
+        # non-contiguous streamed prefixes. Finalize only after the full stream.
-        return loaded
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +8/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_weight_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53614 - [Kimi K3] Support internal prefix checkpoints with partial prefix caching and spec-decoding

- 链接: https://github.com/vllm-project/vllm/pull/53614
- 状态/时间: merged / 2026-09-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；关联提交 `144e79c8106d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+481/-106，可读 patch 1033 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3] Support internal prefix checkpoints with partial prefix caching and spec-decoding」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Kimi K3] Support internal prefix checkpoints with partial prefix caching and spec-decoding」；主要实现面是 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda_metadata.py` modified +71/-1 (72 lines); hunks: -92,6 +92,10 @@ def _make_builder(; -102,20 +106,29 @@ def _make_builder(; symbols: _make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary，涉及 `_make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary`；`vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +35/-15 (50 lines); hunks: -20,6 +20,7; -36,17 +37,18; symbols: _metadata_launch_pdl, build，涉及 `_metadata_launch_pdl, build`；`vllm/models/kimi_k3/nvidia/kda.py` modified +3/-0 (3 lines); hunks: -609,6 +609,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> Mamb...; symbols: get_kv_cache_spec, forward，涉及 `get_kv_cache_spec, forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +71/-1 (72 lines); hunks: -92,6 +92,10 @@ def _make_builder(; -102,20 +106,29 @@ def _make_builder(; symbols: _make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary
  - `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +35/-15 (50 lines); hunks: -20,6 +20,7; -36,17 +37,18; symbols: _metadata_launch_pdl, build
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +3/-0 (3 lines); hunks: -609,6 +609,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> Mamb...; symbols: get_kv_cache_spec, forward
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda_metadata.py
@@ -92,6 +92,10 @@ def _make_builder(
+    mamba_block_size: int = BLOCK_SIZE,
+    prefix_match_unit: int | None = None,
+    use_eagle: bool = False,
+    disable_eagle_block_drop: bool = False,
@@ -102,20 +106,29 @@ def _make_builder(
+        if use_eagle:
diff -- vllm/models/kimi_k3/nvidia/kda_metadata.py
@@ -20,6 +20,7 @@
+from vllm.utils.math_utils import cdiv
@@ -36,17 +37,18 @@
-from vllm.v1.kv_cache_interface import MambaSpec
+from vllm.v1.kv_cache_interface import (
+    MambaSpec,
+    get_mamba_prefill_checkpoint_position,
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -609,6 +609,9 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> MambaSpec:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda_metadata.py` modified +71/-1
  - runtime: `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +35/-15; `vllm/models/kimi_k3/nvidia/kda.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_mamba_align_chunk_split.py`, `tests/v1/core/test_prefix_caching.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55242 - [Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy

- 链接: https://github.com/vllm-project/vllm/pull/55242
- 状态/时间: merged / 2026-09-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `16328c7a775f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+53/-21，可读 patch 195 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-8 (22 lines); hunks: -33,6 +33,9; -428,8 +431,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/kimi_k3/nvidia/mla.py` modified +1/-4 (5 lines); hunks: -306,10 +306,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/kimi_k3/nvidia/model.py` modified +1/-4 (5 lines); hunks: -283,10 +283,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-8 (22 lines); hunks: -33,6 +33,9; -428,8 +431,7 @@ def __init__(; symbols: __init__
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +1/-4 (5 lines); hunks: -306,10 +306,7 @@ def __init__(; symbols: __init__
  - `vllm/models/kimi_k3/nvidia/model.py` modified +1/-4 (5 lines); hunks: -283,10 +283,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -33,6 +33,9 @@
+from vllm.model_executor.layers.quantization.modelopt import (
+    ModelOptMixedPrecisionConfig,
+)
@@ -428,8 +431,7 @@ def __init__(
-        # Keep f_a before the narrow beta shard, then pad each TP-local row
-        # to select the aligned BF16 GEMM path.
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -306,10 +306,7 @@ def __init__(
-                logger.warning_once(
-                    "GEMM-RS/AR is disabled for %s due to an incompatible projection.",
-                    prefix,
-                )
+                gemm_rs_ar.warn_incompatible_projection()
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -283,10 +283,7 @@ def __init__(
-                logger.warning_once(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +14/-8; `vllm/models/kimi_k3/nvidia/mla.py` modified +1/-4; `vllm/models/kimi_k3/nvidia/model.py` modified +1/-4
- 验证与风险: diff 自带测试面 `tests/quantization/test_modelopt.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52494 - [AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper

- 链接: https://github.com/vllm-project/vllm/pull/52494
- 状态/时间: merged / 2026-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`；关联提交 `3ff4f02dfe69`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+123/-2，可读 patch 147 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper」；主要实现面是 `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/mla.py` added +120/-0 (120 lines); hunks: -0,0 +1,120; symbols: KimiK3MultiHeadLatentAttentionWrapper, __init__, _normalize_q_kv, forward，涉及 `KimiK3MultiHeadLatentAttentionWrapper, __init__, _normalize_q_kv`；`vllm/models/kimi_k3/amd/linear.py` modified +3/-2 (5 lines); hunks: -36,7 +36,7; -63,6 +63,7; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/mla.py` added +120/-0 (120 lines); hunks: -0,0 +1,120; symbols: KimiK3MultiHeadLatentAttentionWrapper, __init__, _normalize_q_kv, forward
  - `vllm/models/kimi_k3/amd/linear.py` modified +3/-2 (5 lines); hunks: -36,7 +36,7; -63,6 +63,7; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/mla.py
@@ -0,0 +1,120 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""AMD-specific MLA wrapper for Kimi-K3."""
+from typing import cast
+import torch
+from vllm._aiter_ops import rocm_aiter_ops
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -36,7 +36,7 @@
-from vllm.model_executor.layers.mla import MLAModules, MultiHeadLatentAttentionWrapper
+from vllm.model_executor.layers.mla import MLAModules
@@ -63,6 +63,7 @@
+from vllm.models.kimi_k3.amd.mla import KimiK3MultiHeadLatentAttentionWrapper
@@ -438,7 +439,7 @@ def __init__(
-        self.mla_attn = MultiHeadLatentAttentionWrapper(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/mla.py` added +120/-0; `vllm/models/kimi_k3/amd/linear.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54896 - [Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency

- 链接: https://github.com/vllm-project/vllm/pull/54896
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`；关联提交 `9509fc8ae61a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+121/-36，可读 patch 261 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`；技术摘要: 覆盖「[Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency」；主要实现面是 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +23/-0 (23 lines); hunks: -285,3 +285,26 @@ def test_decode_epilogue_preserves_nope_path() -> None:; symbols: test_decode_epilogue_preserves_nope_path, test_decode_epilogue_row_split_boundary，涉及 `test_decode_epilogue_preserves_nope_path, test_decode_epilogue_row_split_boundary`。
- 代码 diff 细节:
  - `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +23/-0 (23 lines); hunks: -285,3 +285,26 @@ def test_decode_epilogue_preserves_nope_path() -> None:; symbols: test_decode_epilogue_preserves_nope_path, test_decode_epilogue_row_split_boundary
- 关键代码摘录:

```diff
diff -- tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py
@@ -285,3 +285,26 @@ def test_decode_epilogue_preserves_nope_path() -> None:
+@torch.inference_mode()
+@pytest.mark.parametrize("num_tokens", [64, 65])
+def test_decode_epilogue_row_split_boundary(num_tokens: int) -> None:
+    """Both sides of the M-based warps-per-row dispatch produce the same rows."""
+    torch.manual_seed(3)
+    num_blocks = (num_tokens + _BLOCK_SIZE - 1) // _BLOCK_SIZE
```

- 已读文件:
  - tests: `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +23/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54606 - [Kernel] Enable Kimi-K3 SiTU on the CuteDSL MoE backend and the SM107 low-latency GEMM plan

- 链接: https://github.com/vllm-project/vllm/pull/54606
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；关联提交 `d410fc12f30b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+30/-4，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Enable Kimi-K3 SiTU on the CuteDSL MoE backend and the SM107 low-latency GEMM plan」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Kernel] Enable Kimi-K3 SiTU on the CuteDSL MoE backend and the SM107 low-latency GEMM plan」；主要实现面是 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +11/-3 (14 lines); hunks: -1,6 +1,6; -12,7 +12,10; symbols: _is_sm103, _is_sm107, _low_latency_table，涉及 `_is_sm103, _is_sm107, _low_latency_table`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +11/-3 (14 lines); hunks: -1,6 +1,6; -12,7 +12,10; symbols: _is_sm103, _is_sm107, _low_latency_table
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -1,6 +1,6 @@
-"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM90/SM100/SM103.
+"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM90/SM100/SM103/SM107.
@@ -12,7 +12,10 @@
-genuinely differ between the parts, so the tables must not be merged.
+genuinely differ between the parts, so the tables must not be merged. SM107
+(Rubin) reuses the SM103 table: the plan was validated end-to-end on SM107
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +11/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54817 - [CI] Add Kimi-K3-pruned75-DSpark-TP4 gsm8k eval

- 链接: https://github.com/vllm-project/vllm/pull/54817
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml`；关联提交 `872084fb773b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+64/-30，可读 patch 124 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Add Kimi-K3-pruned75-DSpark-TP4 gsm8k eval」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml`；技术摘要: 覆盖「[CI] Add Kimi-K3-pruned75-DSpark-TP4 gsm8k eval」；主要实现面是 `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml` added +26/-0 (26 lines); hunks: -0,0 +1,26。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml` added +26/-0 (26 lines); hunks: -0,0 +1,26
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml
@@ -0,0 +1,26 @@
+model_name: "mgoin/Kimi-K3-pruned75"
+accuracy_threshold: 0.33
+min_acceptance_length: 4.8
+num_questions: 1319
+num_fewshot: 5
+startup_max_wait_seconds: 1800
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml` added +26/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TEP4.yaml`, `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54859 - [Kimi-K3] Bump FlashKDA to fix unstable inverse

- 链接: https://github.com/vllm-project/vllm/pull/54859
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`；关联提交 `f4e613614628`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+51/-1，可读 patch 66 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Bump FlashKDA to fix unstable inverse」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda.py`；技术摘要: 覆盖「[Kimi-K3] Bump FlashKDA to fix unstable inverse」；主要实现面是 `tests/models/kimi_k3/test_kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +50/-0 (50 lines); hunks: -1083,6 +1083,56 @@ def test_fused_kda_decode_rejects_speculative_conv_state():; symbols: test_fused_kda_decode_rejects_speculative_conv_state, test_flashkda_near_collinear_keys_remain_finite, test_flashkda_correctness，涉及 `test_fused_kda_decode_rejects_speculative_conv_state, test_flashkda_near_collinear_keys_remain_finite, test_flashkda_correctness`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +50/-0 (50 lines); hunks: -1083,6 +1083,56 @@ def test_fused_kda_decode_rejects_speculative_conv_state():; symbols: test_fused_kda_decode_rejects_speculative_conv_state, test_flashkda_near_collinear_keys_remain_finite, test_flashkda_correctness
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -1083,6 +1083,56 @@ def test_fused_kda_decode_rejects_speculative_conv_state():
+@torch.inference_mode()
+def test_flashkda_near_collinear_keys_remain_finite():
+    """Guard against unstable inversion of near-collinear key blocks."""
+    lower_bound = -5.0
+    if not is_flashkda_supported(128, torch.bfloat16, lower_bound):
+        pytest.skip("FlashKDA is not supported on this platform")
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +50/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54697 - [Kimi-K3] Overlap low-M TP8 KDA projections

- 链接: https://github.com/vllm-project/vllm/pull/54697
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_kda_projection.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`；关联提交 `3ba9907a1db2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+1092/-12，可读 patch 1197 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Overlap low-M TP8 KDA projections」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Kimi-K3] Overlap low-M TP8 KDA projections」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` added +507/-0 (507 lines); hunks: -0,0 +1,507; symbols: _fma_f32_bf16, _KdaSkinnyNGemm, __init__, __call__，涉及 `_fma_f32_bf16, _KdaSkinnyNGemm, __init__`；`vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +195/-0 (195 lines); hunks: -35,12 +35,32; -683,6 +703,137 @@ def _run_plan(; symbols: ProjectionSpec, _run_plan, run_kda_projection_overlap, run_qkvg，涉及 `ProjectionSpec, _run_plan, run_kda_projection_overlap`；`vllm/models/kimi_k3/nvidia/kda.py` modified +43/-12 (55 lines); hunks: -399,6 +399,7 @@ def __init__(; -421,6 +422,11 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/models/kimi_k3/nvidia/model.py` modified +1/-0 (1 lines); hunks: -895,6 +895,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` added +507/-0 (507 lines); hunks: -0,0 +1,507; symbols: _fma_f32_bf16, _KdaSkinnyNGemm, __init__, __call__
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +195/-0 (195 lines); hunks: -35,12 +35,32; -683,6 +703,137 @@ def _run_plan(; symbols: ProjectionSpec, _run_plan, run_kda_projection_overlap, run_qkvg
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +43/-12 (55 lines); hunks: -399,6 +399,7 @@ def __init__(; -421,6 +422,11 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/kimi_k3/nvidia/model.py` modified +1/-0 (1 lines); hunks: -895,6 +895,7 @@ def __init__(; symbols: __init__
  - `benchmarks/kernels/benchmark_kimi_k3_kda_projection.py` added +221/-0 (221 lines); hunks: -0,0 +1,221; symbols: _capture, _benchmark_graph, _validate, _sequential_projection
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py
@@ -0,0 +1,507 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from
+# https://github.com/sgl-project/sglang/blob/main/python/sglang/kernels/jit/csrc/gemm/tiny_gemm.cuh
+"""Kimi-K3 TP8 skinny GEMMs for the KDA F_A/beta and F_B projections."""
+from __future__ import annotations
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -35,12 +35,32 @@
+from vllm.utils.multi_stream_utils import maybe_execute_in_parallel
+# TP8 KDA projection split, measured together under CUDA graph capture on B300.
+# Q/K/V/G stay on the graph's main stream while F_A/beta and F_B run on the
+# model's auxiliary stream.
+KDA_M1_QKVG_CONFIG = SkinnyGemmConfig(1, 64, 4, 2, 8)
+KDA_M1_FAB_CONFIG = SkinnyGemmConfig(1, 224, 1, 2, 8)
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -399,6 +399,7 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py` added +507/-0; `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +195/-0; `vllm/models/kimi_k3/nvidia/kda.py` modified +43/-12; `vllm/models/kimi_k3/nvidia/model.py` modified +1/-0
  - other: `benchmarks/kernels/benchmark_kimi_k3_kda_projection.py` added +221/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54781 - [Kimi Bug] Fix `cannot access local variable 'active_non_spec_mask_cpu'`

- 链接: https://github.com/vllm-project/vllm/pull/54781
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；关联提交 `fc72fc39ace2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+145/-1，可读 patch 186 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi Bug] Fix `cannot access local variable 'active_non_spec_mask_cpu'`」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`；技术摘要: 覆盖「[Kimi Bug] Fix `cannot access local variable 'active_non_spec_mask_cpu'`」；主要实现面是 `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda_metadata.py` modified +143/-1 (144 lines); hunks: -2,7 +2,8; -21,6 +22,7; symbols: _make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary，涉及 `_make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary`；`vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +2/-0 (2 lines); hunks: -409,6 +409,8 @@ def build( # type: ignore[override]; symbols: build，涉及 `build`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +143/-1 (144 lines); hunks: -2,7 +2,8; -21,6 +22,7; symbols: _make_builder, test_kda_recoverssm_startup_metadata_flow_without_model, test_internal_checkpoint_metadata_targets_last_aligned_boundary
  - `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +2/-0 (2 lines); hunks: -409,6 +409,8 @@ def build( # type: ignore[override]; symbols: build
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda_metadata.py
@@ -2,7 +2,8 @@
-from unittest.mock import Mock
+from types import SimpleNamespace
+from unittest.mock import Mock, patch
@@ -21,6 +22,7 @@
+from vllm.models.kimi_k3.nvidia.model import KimiLinearForCausalLM
@@ -30,11 +32,13 @@
diff -- vllm/models/kimi_k3/nvidia/kda_metadata.py
@@ -409,6 +409,8 @@ def build(  # type: ignore[override]
+                if num_spec_decodes == 0:
+                    spec_sequence_masks_cpu = None
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda_metadata.py` modified +143/-1
  - runtime: `vllm/models/kimi_k3/nvidia/kda_metadata.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda_metadata.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54261 - [Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default

- 链接: https://github.com/vllm-project/vllm/pull/54261
- 状态/时间: merged / 2026-08-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/nvidia/ops/attn_res.py`；关联提交 `d6d665854314`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+415/-94，可读 patch 797 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `benchmarks/kernels/benchmark_kimi_k3_attn_res.py`；技术摘要: 覆盖「[Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default」；主要实现面是 `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `benchmarks/kernels/benchmark_kimi_k3_attn_res.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_attn_res.py` modified +53/-0 (53 lines); hunks: -1,6 +1,8; -12,6 +14,7; symbols: _randn_with_row_padding, _reference, test_attn_res_without_output_norm, test_sm100_variants_do_not_fall_back_to_triton，涉及 `_randn_with_row_padding, _reference, test_attn_res_without_output_norm`；`vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +9/-8 (17 lines); hunks: -186,16 +186,16 @@ def attn_res(; -207,6 +207,7 @@ def attn_res(; symbols: attn_res，涉及 `attn_res`；`benchmarks/kernels/benchmark_kimi_k3_attn_res.py` added +235/-0 (235 lines); hunks: -0,0 +1,235; symbols: Inputs, Result, parse_args, make_inputs，涉及 `Inputs, Result, parse_args`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_attn_res.py` modified +53/-0 (53 lines); hunks: -1,6 +1,8; -12,6 +14,7; symbols: _randn_with_row_padding, _reference, test_attn_res_without_output_norm, test_sm100_variants_do_not_fall_back_to_triton
  - `vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +9/-8 (17 lines); hunks: -186,16 +186,16 @@ def attn_res(; -207,6 +207,7 @@ def attn_res(; symbols: attn_res
  - `benchmarks/kernels/benchmark_kimi_k3_attn_res.py` added +235/-0 (235 lines); hunks: -0,0 +1,235; symbols: Inputs, Result, parse_args, make_inputs
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_attn_res.py
@@ -1,6 +1,8 @@
+import importlib
@@ -12,6 +14,7 @@
+attn_res_module = importlib.import_module("vllm.models.kimi_k3.nvidia.ops.attn_res")
@@ -60,6 +63,7 @@ def _reference(
+        pytest.param(1, 4, 0, False, True, "nvidia", id="nvidia-single-token"),
@@ -194,6 +198,55 @@ def test_attn_res_without_output_norm():
diff -- vllm/models/kimi_k3/nvidia/ops/attn_res.py
@@ -186,16 +186,16 @@ def attn_res(
-    # The in-tree NVIDIA kernel covers the common fused-add + output-norm path;
-    # Triton handles block boundaries and final pre-norm output. The native op
-    # is only compiled for SM100 under CUDA >= 13, so a device check alone is
-    # not enough to know it exists.
+    # The native kernel covers every Kimi-K3 AttnRes variant on dense SM100
+    # inputs. The op is only compiled under CUDA >= 13, so a device check alone
diff -- benchmarks/kernels/benchmark_kimi_k3_attn_res.py
@@ -0,0 +1,235 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_attn_res.py` modified +53/-0
  - runtime: `vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +9/-8
  - other: `benchmarks/kernels/benchmark_kimi_k3_attn_res.py` added +235/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_attn_res.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54482 - [CI/Build] Fix Kimi K3 Eagle3 test fixture

- 链接: https://github.com/vllm-project/vllm/pull/54482
- 状态/时间: merged / 2026-08-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_eagle3.py`；关联提交 `648b7468b8e1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI/Build] Fix Kimi K3 Eagle3 test fixture」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_eagle3.py`；技术摘要: 覆盖「[CI/Build] Fix Kimi K3 Eagle3 test fixture」；主要实现面是 `tests/models/kimi_k3/test_eagle3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_eagle3.py` modified +1/-0 (1 lines); hunks: -42,6 +42,7 @@ def test_kimi_k3_uses_shared_eagle3_layer_configuration():; symbols: test_kimi_k3_uses_shared_eagle3_layer_configuration，涉及 `test_kimi_k3_uses_shared_eagle3_layer_configuration`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_eagle3.py` modified +1/-0 (1 lines); hunks: -42,6 +42,7 @@ def test_kimi_k3_uses_shared_eagle3_layer_configuration():; symbols: test_kimi_k3_uses_shared_eagle3_layer_configuration
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_eagle3.py
@@ -42,6 +42,7 @@ def test_kimi_k3_uses_shared_eagle3_layer_configuration():
+        forward=lambda input_ids, positions: None,
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_eagle3.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_eagle3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54168 - [Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail

- 链接: https://github.com/vllm-project/vllm/pull/54168
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy.py`, `vllm/models/kimi_k3/nvidia/ops/latent_moe_tail.py`；关联提交 `d9dabfa351ac`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+653/-194，可读 patch 1203 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py`, `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py`；技术摘要: 覆盖「[Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py`, `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` modified +327/-161 (488 lines); hunks: -23,21 +23,27; -92,7 +98,7 @@ def _select_routed_schedule(; symbols: _mapping, _select_routed_schedule, AllReduceRMSNormWithReduceScatterEarlyExit, __init__，涉及 `_mapping, _select_routed_schedule, AllReduceRMSNormWithReduceScatterEarlyExit`；`tests/models/kimi_k3/test_latent_moe_tail.py` modified +107/-2 (109 lines); hunks: -153,6 +153,57 @@ def _make_deferred_routed_output(; -197,7 +248,8 @@ def _test_latent_moe_tail_worker(; symbols: _make_deferred_routed_output, _make_bf16_top16_deferred_output, _test_latent_moe_tail_worker, _test_deferred_finalize_parity_worker，涉及 `_make_deferred_routed_output, _make_bf16_top16_deferred_output, _test_latent_moe_tail_worker`；`vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py` modified +24/-10 (34 lines); hunks: -19,6 +19,7; -38,6 +39,13 @@ class SkinnyConfig:; symbols: SkinnyConfig, config_for_m, _as_cute, kernel，涉及 `SkinnyConfig, config_for_m, _as_cute`；`vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy.py` modified +11/-20 (31 lines); hunks: -40,8 +40,13 @@ def __call__(; -54,14 +59,15 @@ def kernel(; symbols: __call__, kernel，涉及 `__call__, kernel`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` modified +327/-161 (488 lines); hunks: -23,21 +23,27; -92,7 +98,7 @@ def _select_routed_schedule(; symbols: _mapping, _select_routed_schedule, AllReduceRMSNormWithReduceScatterEarlyExit, __init__
  - `tests/models/kimi_k3/test_latent_moe_tail.py` modified +107/-2 (109 lines); hunks: -153,6 +153,57 @@ def _make_deferred_routed_output(; -197,7 +248,8 @@ def _test_latent_moe_tail_worker(; symbols: _make_deferred_routed_output, _make_bf16_top16_deferred_output, _test_latent_moe_tail_worker, _test_deferred_finalize_parity_worker
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py` modified +24/-10 (34 lines); hunks: -19,6 +19,7; -38,6 +39,13 @@ class SkinnyConfig:; symbols: SkinnyConfig, config_for_m, _as_cute, kernel
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy.py` modified +11/-20 (31 lines); hunks: -40,8 +40,13 @@ def __call__(; -54,14 +59,15 @@ def kernel(; symbols: __call__, kernel
  - `vllm/models/kimi_k3/nvidia/ops/latent_moe_tail.py` modified +1/-1 (2 lines); hunks: -22,7 +22,7
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py
@@ -23,21 +23,27 @@
-    block_sum_specialized,
+    finalize_top16_bf16,
+    load_shared_f32x2,
+    load_shared_f32x4,
+    stmc_bf16x8,
+    warp_sum_specialized,
diff -- tests/models/kimi_k3/test_latent_moe_tail.py
@@ -153,6 +153,57 @@ def _make_deferred_routed_output(
+def _make_bf16_top16_deferred_output(
+    num_tokens: int,
+    device: torch.device,
+    *,
+    drop_last_route: bool = False,
+) -> tuple[UnfinalizedMoEOutput, torch.Tensor]:
diff -- vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py
@@ -19,6 +19,7 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` modified +327/-161; `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py` modified +24/-10; `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy.py` modified +11/-20; `vllm/models/kimi_k3/nvidia/ops/latent_moe_tail.py` modified +1/-1
  - tests: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +107/-2
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_latent_moe_tail.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54167 - [Kimi-K3][Bugfix] Fix low-latency GEMM fallback initialization

- 链接: https://github.com/vllm-project/vllm/pull/54167
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；关联提交 `f956e1c343dc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-13，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][Bugfix] Fix low-latency GEMM fallback initialization」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Kimi-K3][Bugfix] Fix low-latency GEMM fallback initialization」；主要实现面是 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +1/-0 (1 lines); hunks: -725,6 +725,7 @@ class _KimiK3LowLatencyApply:; symbols: _KimiK3LowLatencyApply, __init__, apply，涉及 `_KimiK3LowLatencyApply, __init__, apply`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +1/-0 (1 lines); hunks: -725,6 +725,7 @@ class _KimiK3LowLatencyApply:; symbols: _KimiK3LowLatencyApply, __init__, apply
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -725,6 +725,7 @@ class _KimiK3LowLatencyApply:
+        super().__init__()
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54015 - [Kimi-K3] Merge MLA gate into QKV-A projection

- 链接: https://github.com/vllm-project/vllm/pull/54015
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mtp.py`；关联提交 `6ec92bcbc8ef`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+280/-103，可读 patch 533 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Merge MLA gate into QKV-A projection」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mtp.py`；技术摘要: 覆盖「[Kimi-K3] Merge MLA gate into QKV-A projection」；主要实现面是 `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/mla.py` modified +167/-94 (261 lines); hunks: -5,7 +5,8; -23,7 +24,8; symbols: _gate_sigmoid_mul, __init__，涉及 `_gate_sigmoid_mul, __init__`；`vllm/models/kimi_k3/nvidia/model.py` modified +12/-4 (16 lines); hunks: -1120,6 +1120,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, Supports...; -1460,10 +1461,17 @@ def load_weights(; symbols: KimiLinearModel, __init__, load_weights，涉及 `KimiLinearModel, __init__, load_weights`；`vllm/models/kimi_k3/nvidia/mtp.py` modified +11/-4 (15 lines); hunks: -272,10 +272,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +167/-94 (261 lines); hunks: -5,7 +5,8; -23,7 +24,8; symbols: _gate_sigmoid_mul, __init__
  - `vllm/models/kimi_k3/nvidia/model.py` modified +12/-4 (16 lines); hunks: -1120,6 +1120,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, Supports...; -1460,10 +1461,17 @@ def load_weights(; symbols: KimiLinearModel, __init__, load_weights
  - `vllm/models/kimi_k3/nvidia/mtp.py` modified +11/-4 (15 lines); hunks: -272,10 +272,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -5,7 +5,8 @@
-      -> fused pre-attention ops (fused_qkv_a_proj / norms / q_b_proj)
+      -> fused pre-attention ops (fused_qkv_a_proj / norms / q_b_proj;
+         with an output gate the rows use fused_qkv_a_g_proj instead)
@@ -23,7 +24,8 @@
-layers, enabled for DSpark) and an optional sigmoid output gate (``g_proj``).
+layers, enabled for DSpark) and an optional sigmoid output gate (``g_proj``,
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -1120,6 +1120,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, SupportsQuant):
+        "fused_qkv_a_g_proj": ["q_a_proj", "kv_a_proj_with_mqa", "g_proj"],
@@ -1460,10 +1461,17 @@ def load_weights(
-            stacked_params_mapping += [
-                (".fused_qkv_a_proj", ".q_a_proj", 0),
-                (".fused_qkv_a_proj", ".kv_a_proj_with_mqa", 1),
-            ]
diff -- vllm/models/kimi_k3/nvidia/mtp.py
@@ -272,10 +272,17 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +167/-94; `vllm/models/kimi_k3/nvidia/model.py` modified +12/-4; `vllm/models/kimi_k3/nvidia/mtp.py` modified +11/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #54088 - [Kimi Perf] Tune hopper low latency gemm kernel, 4%~97% performance improvement

- 链接: https://github.com/vllm-project/vllm/pull/54088
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；关联提交 `9818bb3db8fd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+175/-35，可读 patch 337 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi Perf] Tune hopper low latency gemm kernel, 4%~97% performance improvement」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Kimi Perf] Tune hopper low latency gemm kernel, 4%~97% performance improvement」；主要实现面是 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +98/-7 (105 lines); hunks: -1,19 +1,18; -493,6 +492,96 @@ def _cute(; symbols: _cute, _sm90_spec, _backend_for, _low_latency_table，涉及 `_cute, _sm90_spec, _backend_for`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +98/-7 (105 lines); hunks: -1,19 +1,18; -493,6 +492,96 @@ def _cute(; symbols: _cute, _sm90_spec, _backend_for, _low_latency_table
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -1,19 +1,18 @@
-"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM103 and SM100.
+"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM90/SM100/SM103.
-The two supported capabilities carry separate measured tables:
+The supported capabilities carry separate measured tables:
-:data:`KIMI_K3_PROJECTIONS_SM100` on B200 (SM100). The per-(shape, M) winners
-genuinely differ between the two parts (e.g. 3584x7168 favors dsv3 at M2..8 on
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +98/-7
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53396 - [Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel

- 链接: https://github.com/vllm-project/vllm/pull/53396
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`, `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `aa640684cc95`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+213/-106，可读 patch 649 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`；技术摘要: 覆盖「[Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel」；主要实现面是 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +37/-15 (52 lines); hunks: -895,13 +895,18 @@ def test_kda_recoverssm_verify_and_group_commit(; -910,6 +915,7 @@ def test_fused_kda_decode_correctness(; symbols: test_kda_recoverssm_verify_and_group_commit, test_fused_kda_decode_correctness，涉及 `test_kda_recoverssm_verify_and_group_commit, test_fused_kda_decode_correctness`；`vllm/models/kimi_k3/nvidia/kda.py` modified +2/-1 (3 lines); hunks: -153,14 +153,15 @@ def is_fused_kda_decode_supported(; symbols: is_fused_kda_decode_supported，涉及 `is_fused_kda_decode_supported`；`benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` modified +25/-8 (33 lines); hunks: -81,7 +81,7 @@ def _bench_graph(fn, repeats: int = NUM_KDA_LAYERS) -> float:; -98,9 +98,15 @@ def __init__(self, num_tokens: int, num_heads: int) -> None:; symbols: _bench_graph, Inputs, __init__，涉及 `_bench_graph, Inputs, __init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +37/-15 (52 lines); hunks: -895,13 +895,18 @@ def test_kda_recoverssm_verify_and_group_commit(; -910,6 +915,7 @@ def test_fused_kda_decode_correctness(; symbols: test_kda_recoverssm_verify_and_group_commit, test_fused_kda_decode_correctness
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +2/-1 (3 lines); hunks: -153,14 +153,15 @@ def is_fused_kda_decode_supported(; symbols: is_fused_kda_decode_supported
  - `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` modified +25/-8 (33 lines); hunks: -81,7 +81,7 @@ def _bench_graph(fn, repeats: int = NUM_KDA_LAYERS) -> float:; -98,9 +98,15 @@ def __init__(self, num_tokens: int, num_heads: int) -> None:; symbols: _bench_graph, Inputs, __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -895,13 +895,18 @@ def test_kda_recoverssm_verify_and_group_commit(
-    ("num_heads", "num_seqs", "lower_bound", "fuse_output_norm"),
+    ("num_heads", "num_seqs", "lower_bound", "fuse_output_norm", "conv_layout"),
-        (12, 1, -5.0, True),
-        (12, 4, None, False),
-        (24, 4, None, False),
-        (48, 1, -5.0, True),
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -153,14 +153,15 @@ def is_fused_kda_decode_supported(
+    # The fused kernel handles both conv-state cache layouts (SD and DS); the
+    # inner strides are selected from the tensor at launch time.
-        or is_conv_state_dim_first()
diff -- benchmarks/kernels/benchmark_kimi_k3_kda_decode.py
@@ -81,7 +81,7 @@ def _bench_graph(fn, repeats: int = NUM_KDA_LAYERS) -> float:
-    def __init__(self, num_tokens: int, num_heads: int) -> None:
+    def __init__(self, num_tokens: int, num_heads: int, conv_layout: str) -> None:
@@ -98,9 +98,15 @@ def __init__(self, num_tokens: int, num_heads: int) -> None:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +37/-15
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +2/-1
  - other: `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` modified +25/-8
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53942 - [Kimi K3 Perf] Optimize `eh_proj` linear calculation, 12.9 ~ 25.2% kernel performance improvement

- 链接: https://github.com/vllm-project/vllm/pull/53942
- 状态/时间: merged / 2026-08-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/mtp.py`；关联提交 `76cfe1cd88d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+26/-2，可读 patch 70 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3 Perf] Optimize `eh_proj` linear calculation, 12.9 ~ 25.2% kernel performance improvement」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/mtp.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Kimi K3 Perf] Optimize `eh_proj` linear calculation, 12.9 ~ 25.2% kernel performance improvement」；主要实现面是 `vllm/models/kimi_k3/nvidia/mtp.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/mtp.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -80,7 +81,14 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +8/-0 (8 lines); hunks: -194,6 +194,14 @@ def _cute(; symbols: _cute，涉及 `_cute`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/mtp.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -80,7 +81,14 @@ def __init__(; symbols: __init__
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +8/-0 (8 lines); hunks: -194,6 +194,14 @@ def _cute(; symbols: _cute
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/mtp.py
@@ -16,6 +16,7 @@
+from vllm.model_executor.layers.linear import ReplicatedLinear
@@ -80,7 +81,14 @@ def __init__(
-        self.eh_proj = nn.Linear(config.hidden_size * 2, config.hidden_size, bias=False)
+        self.eh_proj = ReplicatedLinear(
+            config.hidden_size * 2,
+            config.hidden_size,
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -194,6 +194,14 @@ def _cute(
+    (7168, 14336): ProjectionSpec(
+        7168,
+        14336,
+        cute_configs=(
+            (1, SkinnyGemmConfig(1, 256, 2, vector_width=4, static_k=14336)),
+            (2, _cute(2, 224, 4, 2)),
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/mtp.py` modified +9/-1; `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +8/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53534 - [Kimi K3][Kernel] Enable low-latency decode GEMM dispatch on SM100

- 链接: https://github.com/vllm-project/vllm/pull/53534
- 状态/时间: merged / 2026-08-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；关联提交 `bc2d63e650f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+323/-7，可读 patch 406 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3][Kernel] Enable low-latency decode GEMM dispatch on SM100」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`；技术摘要: 覆盖「[Kimi K3][Kernel] Enable low-latency decode GEMM dispatch on SM100」；主要实现面是 `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +228/-6 (234 lines); hunks: -1,12 +1,19; -280,6 +287,204 @@ def _cute(; symbols: _cute, _backend_for, _is_sm103, _low_latency_table，涉及 `_cute, _backend_for, _is_sm103`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +228/-6 (234 lines); hunks: -1,12 +1,19; -280,6 +287,204 @@ def _cute(; symbols: _cute, _backend_for, _is_sm103, _low_latency_table
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/low_latency_gemm.py
@@ -1,12 +1,19 @@
-"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM103.
+"""Kimi-K3 decode GEMM selection for unquantized BF16 on SM103 and SM100.
+The two supported capabilities carry separate measured tables:
+:data:`KIMI_K3_PROJECTIONS` was tuned on B300 (SM103),
+:data:`KIMI_K3_PROJECTIONS_SM100` on B200 (SM100). The per-(shape, M) winners
+genuinely differ between the two parts (e.g. 3584x7168 favors dsv3 at M2..8 on
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/low_latency_gemm.py` modified +228/-6
- 验证与风险: diff 自带测试面 `tests/kernels/test_bf16_skinny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53766 - [CI Bug] Fix kimi test `AssertionError: Aligned Mamba state indices must be precomputed`

- 链接: https://github.com/vllm-project/vllm/pull/53766
- 状态/时间: merged / 2026-08-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda_metadata.py`；关联提交 `0e30bd62fedf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+20/-4，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI Bug] Fix kimi test `AssertionError: Aligned Mamba state indices must be precomputed`」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda_metadata.py`；技术摘要: 覆盖「[CI Bug] Fix kimi test `AssertionError: Aligned Mamba state indices must be precomputed`」；主要实现面是 `tests/models/kimi_k3/test_kda_metadata.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda_metadata.py` modified +20/-4 (24 lines); hunks: -130,14 +130,22 @@ def test_internal_checkpoint_metadata_targets_last_aligned...; -159,14 +167,22 @@ def test_internal_checkpoint_metadata_skips_unaligned_offs...; symbols: test_internal_checkpoint_metadata_targets_last_aligned_boundary, test_internal_checkpoint_metadata_skips_unaligned_offset，涉及 `test_internal_checkpoint_metadata_targets_last_aligned_boundary, test_internal_checkpoint_metadata_skips_unaligned_offset`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda_metadata.py` modified +20/-4 (24 lines); hunks: -130,14 +130,22 @@ def test_internal_checkpoint_metadata_targets_last_aligned...; -159,14 +167,22 @@ def test_internal_checkpoint_metadata_skips_unaligned_offs...; symbols: test_internal_checkpoint_metadata_targets_last_aligned_boundary, test_internal_checkpoint_metadata_skips_unaligned_offset
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda_metadata.py
@@ -130,14 +130,22 @@ def test_internal_checkpoint_metadata_targets_last_aligned_boundary():
-    actual = _make_builder(
+    builder = _make_builder(
-    ).build(0, common_attn_metadata)
+    )
+    assert isinstance(builder, KimiK3KDAMetadataBuilder)
+    builder.mamba_aligned_state_indices = mamba_get_block_table_tensor(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda_metadata.py` modified +20/-4
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda_metadata.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53581 - [Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling

- 链接: https://github.com/vllm-project/vllm/pull/53581
- 状态/时间: merged / 2026-08-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `4c56e62c85ce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-2，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling」；主要实现面是 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +14/-0 (14 lines); hunks: -20,6 +20,7; -59,6 +60,19; symbols: test_kda_warmup_skips_missing_metadata, test_kda_recoverssm_config_state_layout，涉及 `test_kda_warmup_skips_missing_metadata, test_kda_recoverssm_config_state_layout`；`vllm/models/kimi_k3/amd/kda.py` modified +3/-1 (4 lines); hunks: -313,7 +313,9 @@ def _forward(; symbols: _forward，涉及 `_forward`；`vllm/models/kimi_k3/nvidia/kda.py` modified +3/-1 (4 lines); hunks: -658,7 +658,9 @@ def _forward(; symbols: _forward，涉及 `_forward`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +14/-0 (14 lines); hunks: -20,6 +20,7; -59,6 +60,19; symbols: test_kda_warmup_skips_missing_metadata, test_kda_recoverssm_config_state_layout
  - `vllm/models/kimi_k3/amd/kda.py` modified +3/-1 (4 lines); hunks: -313,7 +313,9 @@ def _forward(; symbols: _forward
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +3/-1 (4 lines); hunks: -658,7 +658,9 @@ def _forward(; symbols: _forward
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -20,6 +20,7 @@
+from vllm.models.kimi_k3.nvidia import kda as nvidia_kda
@@ -59,6 +60,19 @@
+def test_kda_warmup_skips_missing_metadata(monkeypatch):
+    monkeypatch.setattr(
+        nvidia_kda,
+        "get_forward_context",
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -313,7 +313,9 @@ def _forward(
-        attn_metadata_narrowed = attn_metadata_raw[self.prefix]
+        attn_metadata_narrowed = attn_metadata_raw.get(self.prefix)
+        if attn_metadata_narrowed is None:
+            return
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -658,7 +658,9 @@ def _forward(
-        attn_metadata_narrowed = attn_metadata_raw[self.prefix]
+        attn_metadata_narrowed = attn_metadata_raw.get(self.prefix)
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +14/-0
  - runtime: `vllm/models/kimi_k3/amd/kda.py` modified +3/-1; `vllm/models/kimi_k3/nvidia/kda.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53327 - [Bugfix][Kimi K3] Enable deferred MoE finalization before weight loading

- 链接: https://github.com/vllm-project/vllm/pull/53327
- 状态/时间: merged / 2026-08-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；关联提交 `e9d1398d9edf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+90/-9，可读 patch 137 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi K3] Enable deferred MoE finalization before weight loading」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；技术摘要: 覆盖「[Bugfix][Kimi K3] Enable deferred MoE finalization before weight loading」；主要实现面是 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +79/-0 (79 lines); hunks: -1,6 +1,8; -13,8 +15,13; symbols: test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, use_deferred_moe_finalize, fake_runner_init，涉及 `test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, use_deferred_moe_finalize`；`vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-9 (20 lines); hunks: -113,16 +113,12 @@ def __init__(; -145,6 +141,12 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_latent_moe_tail.py` modified +79/-0 (79 lines); hunks: -1,6 +1,8; -13,8 +15,13; symbols: test_deferred_finalize_enabled_before_moe_kernel_setup, FakeMoEConfig, use_deferred_moe_finalize, fake_runner_init
  - `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-9 (20 lines); hunks: -113,16 +113,12 @@ def __init__(; -145,6 +141,12 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_latent_moe_tail.py
@@ -1,6 +1,8 @@
+from types import SimpleNamespace
@@ -13,8 +15,13 @@
+from vllm.model_executor.layers.fused_moe.experts.trtllm_mxfp4_moe import (
+    TrtLlmMxfp4ExpertsMonolithic,
+)
+from vllm.model_executor.layers.fused_moe.runner.moe_runner import MoERunner
diff -- vllm/models/kimi_k3/nvidia/latent_moe_runner.py
@@ -113,16 +113,12 @@ def __init__(
-            moe_kernel = self._quant_method.moe_kernel
+            # The kernel instance is built after weight loading, while the tail
+            # must register its CuTeDSL warmup units during runner construction.
-                (
-                    experts_cls is TrtLlmMxfp4ExpertsMonolithic
-                    or experts_cls is TrtLlmNvFp4ExpertsMonolithic
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_latent_moe_tail.py` modified +79/-0
  - runtime: `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` modified +11/-9
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_latent_moe_tail.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53294 - Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill"

- 链接: https://github.com/vllm-project/vllm/pull/53294
- 状态/时间: merged / 2026-08-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；关联提交 `592e06f2ae11`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+18/-2716，可读 patch 2868 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill"」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；技术摘要: 覆盖「Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill"」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_chunk.py` removed +0/-426 (426 lines); hunks: -1,426 +0,0; symbols: _on_gfx950, _requires_kernel, _inputs, _run，涉及 `_on_gfx950, _requires_kernel, _inputs`；`vllm/models/kimi_k3/amd/ops/kda_chunk.py` removed +0/-251 (251 lines); hunks: -1,251 +0,0; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like，涉及 `is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue`；`vllm/models/kimi_k3/amd/ops/kda_prefill.py` removed +0/-126 (126 lines); hunks: -1,126 +0,0; symbols: chunk_kda_prefill，涉及 `chunk_kda_prefill`；`vllm/models/kimi_k3/amd/kda.py` modified +10/-38 (48 lines); hunks: -41,16 +41,13; -213,21 +210,10 @@ def __init__(; symbols: __init__, _prefill_conv，涉及 `__init__, _prefill_conv`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` removed +0/-426 (426 lines); hunks: -1,426 +0,0; symbols: _on_gfx950, _requires_kernel, _inputs, _run
  - `vllm/models/kimi_k3/amd/ops/kda_chunk.py` removed +0/-251 (251 lines); hunks: -1,251 +0,0; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like
  - `vllm/models/kimi_k3/amd/ops/kda_prefill.py` removed +0/-126 (126 lines); hunks: -1,126 +0,0; symbols: chunk_kda_prefill
  - `vllm/models/kimi_k3/amd/kda.py` modified +10/-38 (48 lines); hunks: -41,16 +41,13; -213,21 +210,10 @@ def __init__(; symbols: __init__, _prefill_conv
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -1,426 +0,0 @@
-# SPDX-License-Identifier: Apache-2.0
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
-"""The fused ROCm KDA chunk kernel must match the Triton chunk path.
-The fused kernel reassociates nothing, but it keeps the chunk states in
-registers and rounds them to bfloat16 only where the Triton path does, so the
-outputs agree to bfloat16 rounding and the final states nearly exactly.
diff -- vllm/models/kimi_k3/amd/ops/kda_chunk.py
@@ -1,251 +0,0 @@
-# SPDX-License-Identifier: Apache-2.0
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
-"""ROCm entry point for the fused Kimi-K3 KDA chunk kernel.
-The kernel in ``csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu``
-replaces the chunk-state recurrence and the output GEMM of the Triton chunk
-path with a single launch that keeps the per-chunk state in registers, so the
diff -- vllm/models/kimi_k3/amd/ops/kda_prefill.py
@@ -1,126 +0,0 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` removed +0/-426
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_chunk.py` removed +0/-251; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` removed +0/-126; `vllm/models/kimi_k3/amd/kda.py` modified +10/-38
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52606 - [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill

- 链接: https://github.com/vllm-project/vllm/pull/52606
- 状态/时间: merged / 2026-08-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；关联提交 `463aa5e30fe0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+2716/-18，可读 patch 2868 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/models/kimi_k3/amd/ops/kda_prefill.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_chunk.py` added +426/-0 (426 lines); hunks: -0,0 +1,426; symbols: _on_gfx950, _requires_kernel, _inputs, _run，涉及 `_on_gfx950, _requires_kernel, _inputs`；`vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like，涉及 `is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue`；`vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: chunk_kda_prefill，涉及 `chunk_kda_prefill`；`vllm/models/kimi_k3/amd/kda.py` modified +38/-10 (48 lines); hunks: -41,13 +41,16; -210,10 +213,21 @@ def __init__(; symbols: __init__, _prefill_conv，涉及 `__init__, _prefill_conv`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_chunk.py` added +426/-0 (426 lines); hunks: -0,0 +1,426; symbols: _on_gfx950, _requires_kernel, _inputs, _run
  - `vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: is_fused_kda_chunk_supported, can_use_fused_kda_chunk, fused_kda_prologue, _like
  - `vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: chunk_kda_prefill
  - `vllm/models/kimi_k3/amd/kda.py` modified +38/-10 (48 lines); hunks: -41,13 +41,16; -210,10 +213,21 @@ def __init__(; symbols: __init__, _prefill_conv
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_chunk.py
@@ -0,0 +1,426 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The fused ROCm KDA chunk kernel must match the Triton chunk path.
+The fused kernel reassociates nothing, but it keeps the chunk states in
+registers and rounds them to bfloat16 only where the Triton path does, so the
+outputs agree to bfloat16 rounding and the final states nearly exactly.
diff -- vllm/models/kimi_k3/amd/ops/kda_chunk.py
@@ -0,0 +1,251 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm entry point for the fused Kimi-K3 KDA chunk kernel.
+The kernel in ``csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu``
+replaces the chunk-state recurrence and the output GEMM of the Triton chunk
+path with a single launch that keeps the per-chunk state in registers, so the
diff -- vllm/models/kimi_k3/amd/ops/kda_prefill.py
@@ -0,0 +1,126 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_chunk.py` added +426/-0
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_chunk.py` added +251/-0; `vllm/models/kimi_k3/amd/ops/kda_prefill.py` added +126/-0; `vllm/models/kimi_k3/amd/kda.py` modified +38/-10
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_chunk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53132 - Support kimi k3 nvfp4 checkpoint

- 链接: https://github.com/vllm-project/vllm/pull/53132
- 状态/时间: merged / 2026-08-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `f8e060271381`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+151/-35，可读 patch 366 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support kimi k3 nvfp4 checkpoint」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「Support kimi k3 nvfp4 checkpoint」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +11/-3 (14 lines); hunks: -36,7 +36,7; -102,7 +102,11 @@ def weight_loader(; symbols: weight_loader, weight_loader_v2，涉及 `weight_loader, weight_loader_v2`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +11/-3 (14 lines); hunks: -36,7 +36,7; -102,7 +102,11 @@ def weight_loader(; symbols: weight_loader, weight_loader_v2
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -36,7 +36,7 @@
-from vllm.model_executor.parameter import BasevLLMParameter
+from vllm.model_executor.parameter import BasevLLMParameter, BlockQuantScaleParameter
@@ -102,7 +102,11 @@ def weight_loader(
-        if loaded_shard_id == self.replicated_shard_id:
+        replicate_block_scale = (
+            isinstance(param, BlockQuantScaleParameter)
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +11/-3
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `tests/quantization/test_modelopt.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53053 - [Kimi-K3] Extend GEMM-RS to GEMM-AR

- 链接: https://github.com/vllm-project/vllm/pull/53053
- 状态/时间: merged / 2026-08-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `2785c72a1497`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+481/-232，可读 patch 1343 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Extend GEMM-RS to GEMM-AR」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`；技术摘要: 覆盖「[Kimi-K3] Extend GEMM-RS to GEMM-AR」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +60/-36 (96 lines); hunks: -154,15 +154,18 @@ def shard_sequence_parallel_mlp(; -178,17 +181,32 @@ def maybe_init_gemm_rs(vllm_config: VllmConfig, use_sequen...; symbols: shard_sequence_parallel_mlp, maybe_init_gemm_rs, maybe_init_gemm_rs_ar, __init__，涉及 `shard_sequence_parallel_mlp, maybe_init_gemm_rs, maybe_init_gemm_rs_ar`；`vllm/models/kimi_k3/nvidia/kda.py` modified +13/-13 (26 lines); hunks: -319,7 +319,7 @@ def __init__(; -491,14 +491,18 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/models/kimi_k3/nvidia/mla.py` modified +13/-13 (26 lines); hunks: -134,7 +134,7 @@ def __init__(; -271,14 +271,18 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +60/-36 (96 lines); hunks: -154,15 +154,18 @@ def shard_sequence_parallel_mlp(; -178,17 +181,32 @@ def maybe_init_gemm_rs(vllm_config: VllmConfig, use_sequen...; symbols: shard_sequence_parallel_mlp, maybe_init_gemm_rs, maybe_init_gemm_rs_ar, __init__
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +13/-13 (26 lines); hunks: -319,7 +319,7 @@ def __init__(; -491,14 +491,18 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +13/-13 (26 lines); hunks: -134,7 +134,7 @@ def __init__(; -271,14 +271,18 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -154,15 +154,18 @@ def shard_sequence_parallel_mlp(
-def maybe_init_gemm_rs(vllm_config: VllmConfig, use_sequence_parallel: bool) -> bool:
-    if not envs.VLLM_KIMI_K3_GEMM_RS:
+def maybe_init_gemm_rs_ar(vllm_config: VllmConfig, use_sequence_parallel: bool) -> bool:
+    # Both feature flags may be enabled; the worker's static SP topology binds
+    # its singleton to exactly one mode.
+    all_reduce = not use_sequence_parallel
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -319,7 +319,7 @@ def __init__(
-        run_gemm_rs: bool = False,
+        run_gemm_rs_ar: bool = False,
@@ -491,14 +491,18 @@ def __init__(
-        self.run_gemm_rs = run_gemm_rs
-        if self.run_gemm_rs:
-            from vllm.models.kimi_k3.nvidia.ops.cute_dsl.gemm_rs import get_gemm_rs
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -134,7 +134,7 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +60/-36; `vllm/models/kimi_k3/nvidia/kda.py` modified +13/-13; `vllm/models/kimi_k3/nvidia/mla.py` modified +13/-13
- 验证与风险: diff 自带测试面 `tests/kernels/test_kimi_k3_gemm_rs_ar.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50400 - [Kernel][Kimi] fused vision q/k roper kernel

- 链接: https://github.com/vllm-project/vllm/pull/50400
- 状态/时间: merged / 2026-08-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `c8de519917ce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+14/-26，可读 patch 80 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel][Kimi] fused vision q/k roper kernel」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Kernel][Kimi] fused vision q/k roper kernel」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +14/-26 (40 lines); hunks: -29,6 +29,7; -79,29 +80,6 @@ def get_rope_shape(org, interpolation_mode, shape):; symbols: get_rope_shape, apply_rope, get_1d_sincos_pos_embed_from_grid, __init__，涉及 `get_rope_shape, apply_rope, get_1d_sincos_pos_embed_from_grid`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +14/-26 (40 lines); hunks: -29,6 +29,7; -79,29 +80,6 @@ def get_rope_shape(org, interpolation_mode, shape):; symbols: get_rope_shape, apply_rope, get_1d_sincos_pos_embed_from_grid, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -29,6 +29,7 @@
+from vllm.model_executor.layers.rotary_embedding.common import ApplyRotaryEmb
@@ -79,29 +80,6 @@ def get_rope_shape(org, interpolation_mode, shape):
-def apply_rope(
-    xq: torch.Tensor, xk: torch.Tensor, freqs_cis: torch.Tensor
-) -> tuple[torch.Tensor, torch.Tensor]:
-    """
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +14/-26
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50493 - [Kimi-K3] support DCP partial prefix cache hit

- 链接: https://github.com/vllm-project/vllm/pull/50493
- 状态/时间: merged / 2026-08-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/distributed/test_kimi_linear_context_parallel.py`；关联提交 `0db502c8d8a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+523/-37，可读 patch 715 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] support DCP partial prefix cache hit」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/distributed/test_kimi_linear_context_parallel.py`；技术摘要: 覆盖「[Kimi-K3] support DCP partial prefix cache hit」；主要实现面是 `tests/distributed/test_kimi_linear_context_parallel.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/distributed/test_kimi_linear_context_parallel.py` modified +111/-0 (111 lines); hunks: -2,12 +2,15; -126,3 +129,111 @@ def test_kimi_linear_dcp_tiny(; symbols: test_kimi_linear_dcp_tiny, _make_tiny_k3_config, _run_k3_partial_prefix_reuse, test_kimi_k3_dcp_partial_prefix_reuse，涉及 `test_kimi_linear_dcp_tiny, _make_tiny_k3_config, _run_k3_partial_prefix_reuse`。
- 代码 diff 细节:
  - `tests/distributed/test_kimi_linear_context_parallel.py` modified +111/-0 (111 lines); hunks: -2,12 +2,15; -126,3 +129,111 @@ def test_kimi_linear_dcp_tiny(; symbols: test_kimi_linear_dcp_tiny, _make_tiny_k3_config, _run_k3_partial_prefix_reuse, test_kimi_k3_dcp_partial_prefix_reuse
- 关键代码摘录:

```diff
diff -- tests/distributed/test_kimi_linear_context_parallel.py
@@ -2,12 +2,15 @@
+from pathlib import Path
+from vllm.config import CUDAGraphMode
+from vllm.transformers_utils.configs.kimi_k3 import KimiK3Config
@@ -126,3 +129,111 @@ def test_kimi_linear_dcp_tiny(
+def _make_tiny_k3_config(model_dir: Path) -> str:
+    config = KimiK3Config(
```

- 已读文件:
  - tests: `tests/distributed/test_kimi_linear_context_parallel.py` modified +111/-0
- 验证与风险: diff 自带测试面 `tests/distributed/test_kimi_linear_context_parallel.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52188 - [Spec decode] Support Kimi-K3 DCP with DSpark

- 链接: https://github.com/vllm-project/vllm/pull/52188
- 状态/时间: merged / 2026-08-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/mla.py`；关联提交 `d1e3eee6fb8e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+341/-51，可读 patch 710 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec decode] Support Kimi-K3 DCP with DSpark」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py`；技术摘要: 覆盖「[Spec decode] Support Kimi-K3 DCP with DSpark」；主要实现面是 `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/mla.py` modified +0/-5 (5 lines); hunks: -341,11 +341,6 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +115/-7 (122 lines); hunks: -1,7 +1,8; -15,6 +16,7; symbols: _get_multi_ctas_kv_counter_buffer, FlashInferMLAMetadataBuilder, FlashInferMLADecodeMetadata, FlashInferMLAMetadata，涉及 `_get_multi_ctas_kv_counter_buffer, FlashInferMLAMetadataBuilder, FlashInferMLADecodeMetadata`；`vllm/v1/attention/backends/mla/tokenspeed_mla.py` modified +1/-0 (1 lines); hunks: -61,6 +61,7 @@ class TokenspeedMLAMetadataBuilder(MLACommonMetadataBuilder[ML...; symbols: TokenspeedMLAMetadataBuilder, __init__，涉及 `TokenspeedMLAMetadataBuilder, __init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +0/-5 (5 lines); hunks: -341,11 +341,6 @@ def __init__(; symbols: __init__
  - `vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +115/-7 (122 lines); hunks: -1,7 +1,8; -15,6 +16,7; symbols: _get_multi_ctas_kv_counter_buffer, FlashInferMLAMetadataBuilder, FlashInferMLADecodeMetadata, FlashInferMLAMetadata
  - `vllm/v1/attention/backends/mla/tokenspeed_mla.py` modified +1/-0 (1 lines); hunks: -61,6 +61,7 @@ class TokenspeedMLAMetadataBuilder(MLACommonMetadataBuilder[ML...; symbols: TokenspeedMLAMetadataBuilder, __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -341,11 +341,6 @@ def __init__(
-        assert self.dcp_world_size <= 1 or self.rotary_emb is None, (
-            "Kimi-K3 MultiHeadLatentAttention does not support RoPE with decode "
-            "context parallelism because gathered queries require gathered "
-            "positions."
-        )
diff -- vllm/v1/attention/backends/mla/flashinfer_mla.py
@@ -1,7 +1,8 @@
-from typing import ClassVar
+from dataclasses import dataclass
+from typing import TYPE_CHECKING, ClassVar
@@ -15,6 +16,7 @@
+    MLACommonDecodeMetadata,
@@ -30,6 +32,10 @@
diff -- vllm/v1/attention/backends/mla/tokenspeed_mla.py
@@ -61,6 +61,7 @@ class TokenspeedMLAMetadataBuilder(MLACommonMetadataBuilder[MLACommonMetadata]):
+    supports_non_causal_multi_token_dcp: ClassVar[bool] = True
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +0/-5; `vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +115/-7; `vllm/v1/attention/backends/mla/tokenspeed_mla.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/transformers_utils/test_dspark_mla_config.py`, `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51809 - [XPU] Enable Kimi K3 KDA kernel tests on XPU

- 链接: https://github.com/vllm-project/vllm/pull/51809
- 状态/时间: merged / 2026-08-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`；关联提交 `cc7cf71fc819`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+8/-2，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Enable Kimi K3 KDA kernel tests on XPU」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_kda.py`；技术摘要: 覆盖「[XPU] Enable Kimi K3 KDA kernel tests on XPU」；主要实现面是 `tests/models/kimi_k3/test_kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +7/-1 (8 lines); hunks: -30,9 +30,15。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +7/-1 (8 lines); hunks: -30,9 +30,15
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -30,9 +30,15 @@
+from vllm.platforms import current_platform
-DEVICE = "cuda"
+DEVICE = current_platform.device_type
+pytestmark = pytest.mark.skipif(
+    not (current_platform.is_cuda_alike() or current_platform.is_xpu()),
+    reason="The KDA kernels require a CUDA-alike or XPU device.",
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +7/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52445 - [Bugfix][Model] Kimi-K3 MegaMoE: pass situ_beta/situ_linear_beta to fp8_fp4_mega_moe

- 链接: https://github.com/vllm-project/vllm/pull/52445
- 状态/时间: merged / 2026-08-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `ed0f4750f876`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Kimi-K3 MegaMoE: pass situ_beta/situ_linear_beta to fp8_fp4_mega_moe」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix][Model] Kimi-K3 MegaMoE: pass situ_beta/situ_linear_beta to fp8_fp4_mega_moe」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2 (4 lines); hunks: -486,8 +486,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2 (4 lines); hunks: -486,8 +486,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -486,8 +486,8 @@ def forward(
-            activation_beta=self.activation_beta,
-            activation_linear_beta=self.activation_linear_beta,
+            situ_beta=self.activation_beta,
+            situ_linear_beta=self.activation_linear_beta,
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50487 - [Model][Spec Decode] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state

- 链接: https://github.com/vllm-project/vllm/pull/50487
- 状态/时间: merged / 2026-08-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `03a8d0b1ede6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+350/-1，可读 patch 391 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][Spec Decode] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_eagle3.py`；技术摘要: 覆盖「[Model][Spec Decode] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state」；主要实现面是 `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `vllm/models/kimi_k3/nvidia/model.py`, `tests/models/kimi_k3/test_eagle3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_aux_attn_res_stream.py` added +197/-0 (197 lines); hunks: -0,0 +1,197; symbols: _weights, _stub_model, recorder, _fake_attn_res，涉及 `_weights, _stub_model, recorder`；`vllm/models/kimi_k3/nvidia/model.py` modified +83/-1 (84 lines); hunks: -1198,6 +1198,85 @@ def make_empty_intermediate_tensors(; -1265,7 +1344,10 @@ def forward(; symbols: make_empty_intermediate_tensors, _set_aux_hidden_state_layers, _aux_attn_res_stream, _capture_aux_hidden_stream，涉及 `make_empty_intermediate_tensors, _set_aux_hidden_state_layers, _aux_attn_res_stream`；`tests/models/kimi_k3/test_eagle3.py` modified +62/-0 (62 lines); hunks: -19,6 +19,7 @@ def _make_kimi_linear_model() -> KimiLinearModel:; -137,3 +138,64 @@ def test_kimi_linear_forward_extracts_attn_res_aux_hidden_s...; symbols: _make_kimi_linear_model, test_kimi_linear_forward_extracts_attn_res_aux_hidden_states, test_attn_res_stream_capture_receives_the_layer_outputs_in_order，涉及 `_make_kimi_linear_model, test_kimi_linear_forward_extracts_attn_res_aux_hidden_states, test_attn_res_stream_capture_receives_the_layer_outputs_in_order`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_aux_attn_res_stream.py` added +197/-0 (197 lines); hunks: -0,0 +1,197; symbols: _weights, _stub_model, recorder, _fake_attn_res
  - `vllm/models/kimi_k3/nvidia/model.py` modified +83/-1 (84 lines); hunks: -1198,6 +1198,85 @@ def make_empty_intermediate_tensors(; -1265,7 +1344,10 @@ def forward(; symbols: make_empty_intermediate_tensors, _set_aux_hidden_state_layers, _aux_attn_res_stream, _capture_aux_hidden_stream
  - `tests/models/kimi_k3/test_eagle3.py` modified +62/-0 (62 lines); hunks: -19,6 +19,7 @@ def _make_kimi_linear_model() -> KimiLinearModel:; -137,3 +138,64 @@ def test_kimi_linear_forward_extracts_attn_res_aux_hidden_s...; symbols: _make_kimi_linear_model, test_kimi_linear_forward_extracts_attn_res_aux_hidden_states, test_attn_res_stream_capture_receives_the_layer_outputs_in_order
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_aux_attn_res_stream.py
@@ -0,0 +1,197 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Which value the DFlash drafter is fed under AttnRes.
+`_capture_aux_hidden_stream` picks the weights it mixes against from one of
+three places depending on where the tapped layer sits, and returns the plain
+running prefix when the feature is off. The mixture itself is the kernel's
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -1198,6 +1198,85 @@ def make_empty_intermediate_tensors(
+    def _set_aux_hidden_state_layers(self, layers: tuple[int, ...]) -> None:
+        super()._set_aux_hidden_state_layers(layers)
+        if self.use_attn_res:
+            # Emitted once, at configuration time. Which layers are tapped and
+            # which convention is in force are the two things you need to
+            # confirm from a running process, and neither is recoverable from
diff -- tests/models/kimi_k3/test_eagle3.py
@@ -19,6 +19,7 @@ def _make_kimi_linear_model() -> KimiLinearModel:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_aux_attn_res_stream.py` added +197/-0; `tests/models/kimi_k3/test_eagle3.py` modified +62/-0
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +83/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `tests/models/kimi_k3/test_eagle3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52171 - [Bugfix] Declare SupportsEagle3 on KimiLinearForCausalLM

- 链接: https://github.com/vllm-project/vllm/pull/52171
- 状态/时间: merged / 2026-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `83d4c6196ad9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-1，可读 patch 32 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Declare SupportsEagle3 on KimiLinearForCausalLM」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix] Declare SupportsEagle3 on KimiLinearForCausalLM」；主要实现面是 `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_eagle3.py` modified +9/-0 (9 lines); hunks: -10,6 +10,7; -25,6 +26,14 @@ def test_kimi_k3_advertises_eagle3_support():; symbols: test_kimi_k3_advertises_eagle3_support, test_kimi_linear_advertises_eagle3_support, test_kimi_k3_uses_shared_eagle3_layer_configuration，涉及 `test_kimi_k3_advertises_eagle3_support, test_kimi_linear_advertises_eagle3_support, test_kimi_k3_uses_shared_eagle3_layer_configuration`；`vllm/models/kimi_k3/nvidia/model.py` modified +1/-1 (2 lines); hunks: -1397,7 +1397,7 @@ def finalize_mega_moe_weights(self) -> None:; symbols: finalize_mega_moe_weights, KimiLinearForCausalLM, __init__，涉及 `finalize_mega_moe_weights, KimiLinearForCausalLM, __init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_eagle3.py` modified +9/-0 (9 lines); hunks: -10,6 +10,7; -25,6 +26,14 @@ def test_kimi_k3_advertises_eagle3_support():; symbols: test_kimi_k3_advertises_eagle3_support, test_kimi_linear_advertises_eagle3_support, test_kimi_k3_uses_shared_eagle3_layer_configuration
  - `vllm/models/kimi_k3/nvidia/model.py` modified +1/-1 (2 lines); hunks: -1397,7 +1397,7 @@ def finalize_mega_moe_weights(self) -> None:; symbols: finalize_mega_moe_weights, KimiLinearForCausalLM, __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_eagle3.py
@@ -10,6 +10,7 @@
+    KimiLinearForCausalLM,
@@ -25,6 +26,14 @@ def test_kimi_k3_advertises_eagle3_support():
+def test_kimi_linear_advertises_eagle3_support():
+    # The text-only architecture serves the same inner KimiLinearModel, which
+    # already carries the EagleModelMixin tap machinery - only the interface
+    # declaration was missing, so EAGLE3-family speculative decoding (dspark)
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -1397,7 +1397,7 @@ def finalize_mega_moe_weights(self) -> None:
-    nn.Module, HasInnerState, SupportsPP, MixtureOfExperts, IsHybrid
+    nn.Module, HasInnerState, SupportsPP, MixtureOfExperts, IsHybrid, SupportsEagle3
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_eagle3.py` modified +9/-0
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_eagle3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52079 - [Kimi-K3] Add GEMM-RS for sequence parallelism

- 链接: https://github.com/vllm-project/vllm/pull/52079
- 状态/时间: merged / 2026-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `6014f9e67291`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+1591/-13，可读 patch 1827 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Add GEMM-RS for sequence parallelism」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[Kimi-K3] Add GEMM-RS for sequence parallelism」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +82/-2 (84 lines); hunks: -133,21 +133,60 @@ def shard_sequence_parallel_mlp(; -172,6 +211,8 @@ def __init__(; symbols: shard_sequence_parallel_mlp, maybe_init_gemm_rs, KimiMLP, __init__，涉及 `shard_sequence_parallel_mlp, maybe_init_gemm_rs, KimiMLP`；`vllm/models/kimi_k3/nvidia/mla.py` modified +18/-4 (22 lines); hunks: -134,6 +134,7 @@ def __init__(; -270,6 +271,16 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/models/kimi_k3/nvidia/kda.py` modified +17/-1 (18 lines); hunks: -305,6 +305,7 @@ def __init__(; -470,7 +471,16 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`tests/models/kimi_k3/test_sequence_parallel.py` modified +9/-6 (15 lines); hunks: -267,19 +267,21 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkey...; -293,6 +295,7 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating，涉及 `test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +82/-2 (84 lines); hunks: -133,21 +133,60 @@ def shard_sequence_parallel_mlp(; -172,6 +211,8 @@ def __init__(; symbols: shard_sequence_parallel_mlp, maybe_init_gemm_rs, KimiMLP, __init__
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +18/-4 (22 lines); hunks: -134,6 +134,7 @@ def __init__(; -270,6 +271,16 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +17/-1 (18 lines); hunks: -305,6 +305,7 @@ def __init__(; -470,7 +471,16 @@ def __init__(; symbols: __init__, forward
  - `tests/models/kimi_k3/test_sequence_parallel.py` modified +9/-6 (15 lines); hunks: -267,19 +267,21 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkey...; -293,6 +295,7 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -133,21 +133,60 @@ def shard_sequence_parallel_mlp(
+    eligible: bool,
-    if not (use_sequence_parallel and enabled):
+    if not (use_sequence_parallel and eligible and enabled):
+def maybe_init_gemm_rs(vllm_config: VllmConfig, use_sequence_parallel: bool) -> bool:
+    if not envs.VLLM_KIMI_K3_GEMM_RS:
+        return False
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -134,6 +134,7 @@ def __init__(
+        run_gemm_rs: bool = False,
@@ -270,6 +271,16 @@ def __init__(
+        self.run_gemm_rs = run_gemm_rs
+        if self.run_gemm_rs:
+            from vllm.models.kimi_k3.nvidia.ops.cute_dsl.gemm_rs import get_gemm_rs
+            self.run_gemm_rs = get_gemm_rs().can_run(self.o_proj)
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -305,6 +305,7 @@ def __init__(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +82/-2; `vllm/models/kimi_k3/nvidia/mla.py` modified +18/-4; `vllm/models/kimi_k3/nvidia/kda.py` modified +17/-1
  - tests: `tests/models/kimi_k3/test_sequence_parallel.py` modified +9/-6
- 验证与风险: diff 自带测试面 `tests/kernels/test_kimi_k3_gemm_rs.py`, `tests/models/kimi_k3/test_sequence_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51862 - [ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA

- 链接: https://github.com/vllm-project/vllm/pull/51862
- 状态/时间: merged / 2026-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`；关联提交 `f96261637c05`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+188/-43，可读 patch 338 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA」；主要实现面是 `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/kda_metadata.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _chunk_metadata_kernel, prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder, _build_chunk_metadata，涉及 `_chunk_metadata_kernel, prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder`；`vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +14/-5 (19 lines); hunks: -601,6 +601,7 @@ def _chunk_kda_fwd_with_cumulative_g(; -638,6 +639,7 @@ def _chunk_kda_fwd_with_cumulative_g(; symbols: _chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate，涉及 `_chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate`；`vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +11/-2 (13 lines); hunks: -2,6 +2,7; -393,8 +394,16 @@ def _forward(; symbols: _forward，涉及 `_forward`；`vllm/models/kimi_k3/amd/kda.py` modified +7/-0 (7 lines); hunks: -40,6 +40,7; -52,12 +53,16; symbols: KimiK3DeltaAttention, get_attn_backend, get_state_dtype, _prefill_conv，涉及 `KimiK3DeltaAttention, get_attn_backend, get_state_dtype`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/kda_metadata.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _chunk_metadata_kernel, prepare_chunk_metadata_device, KimiK3ROCmKDAMetadataBuilder, _build_chunk_metadata
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +14/-5 (19 lines); hunks: -601,6 +601,7 @@ def _chunk_kda_fwd_with_cumulative_g(; -638,6 +639,7 @@ def _chunk_kda_fwd_with_cumulative_g(; symbols: _chunk_kda_fwd_with_cumulative_g, chunk_kda_with_fused_gate_fwd, chunk_kda_with_fused_gate
  - `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +11/-2 (13 lines); hunks: -2,6 +2,7; -393,8 +394,16 @@ def _forward(; symbols: _forward
  - `vllm/models/kimi_k3/amd/kda.py` modified +7/-0 (7 lines); hunks: -40,6 +40,7; -52,12 +53,16; symbols: KimiK3DeltaAttention, get_attn_backend, get_state_dtype, _prefill_conv
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/kda_metadata.py
@@ -0,0 +1,109 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm Kimi-K3 specialization of GDN attention metadata.
+The request classification and cudagraph staging intentionally mirror
+``GDNAttentionMetadataBuilder``. Only the FLA chunk metadata is built
+differently on device rather than on the host.
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py
@@ -601,6 +601,7 @@ def _chunk_kda_fwd_with_cumulative_g(
+    chunk_offsets: torch.Tensor | None = None,
@@ -638,6 +639,7 @@ def _chunk_kda_fwd_with_cumulative_g(
+        chunk_offsets=chunk_offsets,
@@ -711,13 +713,15 @@ def chunk_kda_with_fused_gate_fwd(
+    chunk_indices: torch.Tensor | None = None,
+    chunk_offsets: torch.Tensor | None = None,
diff -- vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py
@@ -2,6 +2,7 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/kda_metadata.py` added +109/-0; `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +14/-5; `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +11/-2; `vllm/models/kimi_k3/amd/kda.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51772 - [Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing

- 链接: https://github.com/vllm-project/vllm/pull/51772
- 状态/时间: merged / 2026-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`；关联提交 `903d2efe7eb6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+996/-35，可读 patch 1326 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`；技术摘要: 覆盖「[Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing」；主要实现面是 `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_mla_prefill_context.py` added +319/-0 (319 lines); hunks: -0,0 +1,319; symbols: _RecordingPrefillBackend, __init__, get_name, supports_out，涉及 `_RecordingPrefillBackend, __init__, get_name`；`vllm/models/kimi_k3/nvidia/mla.py` modified +192/-6 (198 lines); hunks: -8,8 +8,9; -34,6 +35,7; symbols: _decode_concat_cache, _compute_prefill_context, run_chunk, _gather_context_latent，涉及 `_decode_concat_cache, _compute_prefill_context, run_chunk`；`vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +56/-0 (56 lines); hunks: -12,6 +12,9; -156,6 +159,59 @@ def fused_mla_qkv_quant_kv_cache_fp8_insert(; symbols: fused_mla_qkv_quant_kv_cache_fp8_insert, _empty_full_key, fused_mla_kv_concat, fused_mla_kv_concat_quant_fp8，涉及 `fused_mla_qkv_quant_kv_cache_fp8_insert, _empty_full_key, fused_mla_kv_concat`；`tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +68/-2 (70 lines); hunks: -9,6 +9,8; -25,8 +27,8; symbols: _randn, _rope_cache, _assert_fp8_close, _strided_context_inputs，涉及 `_randn, _rope_cache, _assert_fp8_close`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_mla_prefill_context.py` added +319/-0 (319 lines); hunks: -0,0 +1,319; symbols: _RecordingPrefillBackend, __init__, get_name, supports_out
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +192/-6 (198 lines); hunks: -8,8 +8,9; -34,6 +35,7; symbols: _decode_concat_cache, _compute_prefill_context, run_chunk, _gather_context_latent
  - `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +56/-0 (56 lines); hunks: -12,6 +12,9; -156,6 +159,59 @@ def fused_mla_qkv_quant_kv_cache_fp8_insert(; symbols: fused_mla_qkv_quant_kv_cache_fp8_insert, _empty_full_key, fused_mla_kv_concat, fused_mla_kv_concat_quant_fp8
  - `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +68/-2 (70 lines); hunks: -9,6 +9,8; -25,8 +27,8; symbols: _randn, _rope_cache, _assert_fp8_close, _strided_context_inputs
  - `vllm/v1/attention/backends/mla/prefill/tokenspeed_mla.py` modified +4/-1 (5 lines); hunks: -166,11 +166,13 @@ def run_prefill_context_chunk(; -187,6 +189,7 @@ def run_prefill_context_chunk(; symbols: run_prefill_context_chunk
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_mla_prefill_context.py
@@ -0,0 +1,319 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""K3's fused chunked-context prefill must match the generic MLA impl.
+The layer owns its own context loop so it can fuse the per-chunk K/V pack and
+skip re-quantizing an already-quantized query. That is only safe if it feeds the
+prefill backend exactly what ``MLACommonBaseImpl._compute_prefill_context``
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -8,8 +8,9 @@
-                    (+ chunked-context merge); dispatched by cache dtype
-                    (bf16 / plain fp8 / fp8_ds_mla)
+                    (+ chunked-context merge, whose per-chunk gather -> kv_b_proj
+                    -> fused K/V pack loop this layer owns); dispatched by cache
+                    dtype (bf16 / plain fp8 / fp8_ds_mla)
@@ -34,6 +35,7 @@
diff -- vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py
@@ -12,6 +12,9 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_mla_prefill_context.py` added +319/-0; `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` modified +68/-2
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +192/-6; `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py` modified +56/-0; `vllm/v1/attention/backends/mla/prefill/tokenspeed_mla.py` modified +4/-1
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `tests/models/kimi_k3/test_mla_prefill_context.py`, `tests/v1/attention/test_mla_prefill_registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50654 - [ROCm][Perf] Kimi-K3 Fused kernel for KDA decode

- 链接: https://github.com/vllm-project/vllm/pull/50654
- 状态/时间: merged / 2026-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`；关联提交 `7f9173dfa24d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+1592/-9，可读 patch 1666 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Fused kernel for KDA decode」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Fused kernel for KDA decode」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_decode.py` added +291/-0 (291 lines); hunks: -0,0 +1,291; symbols: _on_gfx950, _requires_kernel, KdaDecodeInputs, __init__，涉及 `_on_gfx950, _requires_kernel, KdaDecodeInputs`；`vllm/models/kimi_k3/amd/ops/kda_decode.py` added +99/-0 (99 lines); hunks: -0,0 +1,99; symbols: is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader, make_decode_norm_weight_loader，涉及 `is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader`；`vllm/models/kimi_k3/amd/kda.py` modified +89/-9 (98 lines); hunks: -5,10 +5,12; -38,6 +40,11; symbols: KimiK3DeltaAttention, get_state_dtype, __init__, _forward，涉及 `KimiK3DeltaAttention, get_state_dtype, __init__`；`benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` added +291/-0 (291 lines); hunks: -0,0 +1,291; symbols: _bench, _bench_graph_layers, _bench_graph, Inputs，涉及 `_bench, _bench_graph_layers, _bench_graph`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_decode.py` added +291/-0 (291 lines); hunks: -0,0 +1,291; symbols: _on_gfx950, _requires_kernel, KdaDecodeInputs, __init__
  - `vllm/models/kimi_k3/amd/ops/kda_decode.py` added +99/-0 (99 lines); hunks: -0,0 +1,99; symbols: is_fused_kda_decode_supported, make_decode_conv1d_weight_loader, weight_loader, make_decode_norm_weight_loader
  - `vllm/models/kimi_k3/amd/kda.py` modified +89/-9 (98 lines); hunks: -5,10 +5,12; -38,6 +40,11; symbols: KimiK3DeltaAttention, get_state_dtype, __init__, _forward
  - `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` added +291/-0 (291 lines); hunks: -0,0 +1,291; symbols: _bench, _bench_graph_layers, _bench_graph, Inputs
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_kda_decode.py
@@ -0,0 +1,291 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The ROCm fused KDA decode kernel must match the Triton chain it replaces.
+The fused kernel folds the packed causal conv1d update, the gated delta-rule
+recurrence and the gated output RMSNorm into one launch, and updates both the
+conv state and the recurrent state in place. Every one of those outputs is
diff -- vllm/models/kimi_k3/amd/ops/kda_decode.py
@@ -0,0 +1,99 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""ROCm entry points for the fused Kimi-K3 KDA decode kernel.
+The kernel in ``csrc/libtorch_stable/kimi_k3/fused_kda_decode_kernel_rocm.cu``
+replaces, for a pure non-speculative decode batch, the three Triton launches
+and two copies the AMD KDA layer otherwise runs per layer: the packed causal
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -5,10 +5,12 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_decode.py` added +291/-0
  - runtime: `vllm/models/kimi_k3/amd/ops/kda_decode.py` added +99/-0; `vllm/models/kimi_k3/amd/kda.py` modified +89/-9
  - other: `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py` added +291/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50484 - [Kimi-K3] DCP support

- 链接: https://github.com/vllm-project/vllm/pull/50484
- 状态/时间: merged / 2026-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/distributed/test_kimi_linear_context_parallel.py`, `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py`, `vllm/models/kimi_k3/nvidia/mla.py`；关联提交 `63ac04a61e62`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 19 个文件，+3529/-82，可读 patch 4066 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] DCP support」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py`, `tests/distributed/test_kimi_linear_context_parallel.py`；技术摘要: 覆盖「[Kimi-K3] DCP support」；主要实现面是 `vllm/models/kimi_k3/nvidia/mla.py`, `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py`, `tests/distributed/test_kimi_linear_context_parallel.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/mla.py` modified +69/-11 (80 lines); hunks: -24,8 +24,8; -35,7 +35,11; symbols: __init__, _attention, _decode_concat_cache, _forward_prefill_fused，涉及 `__init__, _attention, _decode_concat_cache`；`tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py` added +246/-0 (246 lines); hunks: -0,0 +1,246; symbols: _inputs, make, _slot_mapping, _owned，涉及 `_inputs, make, _slot_mapping`；`tests/distributed/test_kimi_linear_context_parallel.py` added +128/-0 (128 lines); hunks: -0,0 +1,128; symbols: _make_tiny_overrides, _run_tiny_model, test_kimi_linear_dcp_tiny，涉及 `_make_tiny_overrides, _run_tiny_model, test_kimi_linear_dcp_tiny`；`vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +4/-2 (6 lines); hunks: -309,9 +309,11 @@ def forward_mqa(; -326,7 +328,7 @@ def forward_mqa(; symbols: forward_mqa，涉及 `forward_mqa`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +69/-11 (80 lines); hunks: -24,8 +24,8; -35,7 +35,11; symbols: __init__, _attention, _decode_concat_cache, _forward_prefill_fused
  - `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py` added +246/-0 (246 lines); hunks: -0,0 +1,246; symbols: _inputs, make, _slot_mapping, _owned
  - `tests/distributed/test_kimi_linear_context_parallel.py` added +128/-0 (128 lines); hunks: -0,0 +1,128; symbols: _make_tiny_overrides, _run_tiny_model, test_kimi_linear_dcp_tiny
  - `vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +4/-2 (6 lines); hunks: -309,9 +309,11 @@ def forward_mqa(; -326,7 +328,7 @@ def forward_mqa(; symbols: forward_mqa
  - `vllm/v1/attention/backends/mla/tokenspeed_mla.py` modified +2/-1 (3 lines); hunks: -289,8 +289,9 @@ def forward_mqa(; symbols: forward_mqa
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -24,8 +24,8 @@
-Out of scope (extension points, not wired here): context parallelism (DCP/PCP),
-sparse/indexer MLA, and the ROCm/aiter fp8/fp4 BMM fast paths.
+Out of scope (extension points, not wired here): prefill context parallelism
+(PCP), sparse/indexer MLA, and the ROCm/aiter fp8/fp4 BMM fast paths.
@@ -35,7 +35,11 @@
-from vllm.config import CacheConfig, VllmConfig, get_current_vllm_config
diff -- tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py
@@ -0,0 +1,246 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+import torch
+import vllm._custom_ops as ops
+from vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache import (
diff -- tests/distributed/test_kimi_linear_context_parallel.py
@@ -0,0 +1,128 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +69/-11; `vllm/v1/attention/backends/mla/flashinfer_mla.py` modified +4/-2; `vllm/v1/attention/backends/mla/tokenspeed_mla.py` modified +2/-1
  - tests: `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py` added +246/-0; `tests/distributed/test_kimi_linear_context_parallel.py` added +128/-0
- 验证与风险: diff 自带测试面 `tests/distributed/test_dcp_a2a.py`, `tests/distributed/test_dcp_direct_a2a_lse_reduce.py`, `tests/distributed/test_kimi_linear_context_parallel.py`, `tests/kernels/attention/test_kimi_k3_mla_key_concat_kv_cache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51682 - [Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride

- 链接: https://github.com/vllm-project/vllm/pull/51682
- 状态/时间: merged / 2026-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`；关联提交 `0e2d78028c47`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+18/-4，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride」；主要实现面是 `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_kda.py` modified +13/-1 (14 lines); hunks: -15,6 +15,9; -31,6 +34,13; symbols: test_gather_initial_states_correctness, test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness，涉及 `test_gather_initial_states_correctness, test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness`；`vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +5/-3 (8 lines); hunks: -459,6 +459,7 @@ def fused_recurrent_kda_packed_decode_kernel(; -476,7 +477,7 @@ def fused_recurrent_kda_packed_decode_kernel(; symbols: fused_recurrent_kda_packed_decode_kernel, fused_recurrent_kda_packed_decode，涉及 `fused_recurrent_kda_packed_decode_kernel, fused_recurrent_kda_packed_decode`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_kda.py` modified +13/-1 (14 lines); hunks: -15,6 +15,9; -31,6 +34,13; symbols: test_gather_initial_states_correctness, test_chunk_kda_fused_gate_cumsum_matches_unfused, test_packed_kda_decode_correctness
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +5/-3 (8 lines); hunks: -459,6 +459,7 @@ def fused_recurrent_kda_packed_decode_kernel(; -476,7 +477,7 @@ def fused_recurrent_kda_packed_decode_kernel(; symbols: fused_recurrent_kda_packed_decode_kernel, fused_recurrent_kda_packed_decode
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_kda.py
@@ -15,6 +15,9 @@
+from vllm.models.kimi_k3.amd.ops.third_party.kda import (
+    fused_recurrent_kda_packed_decode as fused_recurrent_kda_packed_decode_amd,
+)
@@ -31,6 +34,13 @@
+# The AMD and NVIDIA copies of the KDA kernels are vendored separately and are
+# free to diverge, so the shared-semantics tests below run against both.
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py
@@ -459,6 +459,7 @@ def fused_recurrent_kda_packed_decode_kernel(
+    stride_state_indices,
@@ -476,7 +477,7 @@ def fused_recurrent_kda_packed_decode_kernel(
-    state_idx = tl.load(state_indices + i_n).to(tl.int64)
+    state_idx = tl.load(state_indices + i_n * stride_state_indices).to(tl.int64)
@@ -560,8 +561,8 @@ def fused_recurrent_kda_packed_decode(
-    if state_indices.ndim != 1 or state_indices.stride(0) != 1:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_kda.py` modified +13/-1
  - runtime: `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py` modified +5/-3
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_kda.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51529 - [K3] Allow tpu to import kimi_k3.common

- 链接: https://github.com/vllm-project/vllm/pull/51529
- 状态/时间: merged / 2026-08-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/__init__.py`；关联提交 `04d13b5d6537`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-2，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[K3] Allow tpu to import kimi_k3.common」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/models/kimi_k3/__init__.py`；技术摘要: 覆盖「[K3] Allow tpu to import kimi_k3.common」；主要实现面是 `vllm/models/kimi_k3/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/__init__.py` modified +9/-2 (11 lines); hunks: -13,13 +13,20。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/__init__.py` modified +9/-2 (11 lines); hunks: -13,13 +13,20
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/__init__.py
@@ -13,13 +13,20 @@
-if TYPE_CHECKING or not current_platform.is_rocm():
+# TPU plugins import the shared ``common`` modules through this package, but
+# register their own model classes. Do not eagerly import a GPU implementation.
+if TYPE_CHECKING:
-else:
+elif current_platform.device_type == "tpu":
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/__init__.py` modified +9/-2
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51196 - [Kimi][MM] disable kimi_vit's dynamic torch.compile for TPU

- 链接: https://github.com/vllm-project/vllm/pull/51196
- 状态/时间: merged / 2026-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `7f58e8294a19`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi][MM] disable kimi_vit's dynamic torch.compile for TPU」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Kimi][MM] disable kimi_vit's dynamic torch.compile for TPU」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +1/-1 (2 lines); hunks: -61,7 +61,7 @@ def wrapper(org, interpolation_mode, shape):; symbols: wrapper, get_rope_shape，涉及 `wrapper, get_rope_shape`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +1/-1 (2 lines); hunks: -61,7 +61,7 @@ def wrapper(org, interpolation_mode, shape):; symbols: wrapper, get_rope_shape
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -61,7 +61,7 @@ def wrapper(org, interpolation_mode, shape):
-@torch.compile(dynamic=True)
+@torch.compile(dynamic=True, disable=current_platform.simple_compile_backend == "tpu")
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51253 - [ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path

- 链接: https://github.com/vllm-project/vllm/pull/51253
- 状态/时间: merged / 2026-08-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/__init__.py`, `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`；关联提交 `43d691ec6b1d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+453/-0，可读 patch 470 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `tests/models/kimi_k3/__init__.py`；技术摘要: 覆盖「[ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path」；主要实现面是 `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `tests/models/kimi_k3/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` added +297/-0 (297 lines); hunks: -0,0 +1,297; symbols: _build_transform, _tail_runner, method, _all_reduced，涉及 `_build_transform, _tail_runner, method`；`vllm/models/kimi_k3/amd/latent_moe_runner.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: ROCmLatentMoERunner, __init__, _shard_up_proj_tail, forward，涉及 `ROCmLatentMoERunner, __init__, _shard_up_proj_tail`；`tests/models/kimi_k3/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2；`vllm/models/kimi_k3/amd/linear.py` modified +2/-0 (2 lines); hunks: -62,6 +62,7; -289,6 +290,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_latent_moe_runner.py` added +297/-0 (297 lines); hunks: -0,0 +1,297; symbols: _build_transform, _tail_runner, method, _all_reduced
  - `vllm/models/kimi_k3/amd/latent_moe_runner.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: ROCmLatentMoERunner, __init__, _shard_up_proj_tail, forward
  - `tests/models/kimi_k3/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/kimi_k3/amd/linear.py` modified +2/-0 (2 lines); hunks: -62,6 +62,7; -289,6 +290,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_amd_latent_moe_runner.py
@@ -0,0 +1,297 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The ROCm latent-MoE tail must equal the replicated up-projection.
+A wrong shard offset or a dropped accumulation still runs and still produces
+plausible text, so these pin the arithmetic rather than the behaviour.
+"""
diff -- vllm/models/kimi_k3/amd/latent_moe_runner.py
@@ -0,0 +1,152 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import torch
+from vllm.distributed import (
+    get_tensor_model_parallel_rank,
+    tensor_model_parallel_all_reduce,
diff -- tests/models/kimi_k3/__init__.py
@@ -0,0 +1,2 @@
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_latent_moe_runner.py` added +297/-0; `tests/models/kimi_k3/__init__.py` added +2/-0
  - runtime: `vllm/models/kimi_k3/amd/latent_moe_runner.py` added +152/-0; `vllm/models/kimi_k3/amd/linear.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/__init__.py`, `tests/models/kimi_k3/test_amd_latent_moe_runner.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51249 - [Bugfix][Model] Add missing fused_qkv_a_proj to Kimi-Linear packed_modules_mapping

- 链接: https://github.com/vllm-project/vllm/pull/51249
- 状态/时间: merged / 2026-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `5fba75aefeed`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Add missing fused_qkv_a_proj to Kimi-Linear packed_modules_mapping」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix][Model] Add missing fused_qkv_a_proj to Kimi-Linear packed_modules_mapping」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1014,6 +1014,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, Supports...; symbols: KimiLinearModel, __init__，涉及 `KimiLinearModel, __init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1014,6 +1014,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, Supports...; symbols: KimiLinearModel, __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -1014,6 +1014,7 @@ class KimiLinearModel(nn.Module, EagleModelMixin, SupportsQuant):
+        "fused_qkv_a_proj": ["q_a_proj", "kv_a_proj_with_mqa"],
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50649 - [ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config

- 链接: https://github.com/vllm-project/vllm/pull/50649
- 状态/时间: merged / 2026-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`；关联提交 `f5cd862dbdaf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+556/-7，可读 patch 599 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`；技术摘要: 覆盖「[ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config」；主要实现面是 `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/kda.py` added +530/-0 (530 lines); hunks: -0,0 +1,530; symbols: KimiK3DeltaAttention, get_state_dtype, get_state_shape, __init__，涉及 `KimiK3DeltaAttention, get_state_dtype, get_state_shape`；`vllm/models/kimi_k3/amd/linear.py` modified +18/-6 (24 lines); hunks: -28,7 +28,7; -61,6 +61,7; symbols: __init__，涉及 `__init__`；`vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +8/-1 (9 lines); hunks: -28,6 +28,13; -39,7 +46,7。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/kda.py` added +530/-0 (530 lines); hunks: -0,0 +1,530; symbols: KimiK3DeltaAttention, get_state_dtype, get_state_shape, __init__
  - `vllm/models/kimi_k3/amd/linear.py` modified +18/-6 (24 lines); hunks: -28,7 +28,7; -61,6 +61,7; symbols: __init__
  - `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +8/-1 (9 lines); hunks: -28,6 +28,13; -39,7 +46,7
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -0,0 +1,530 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import torch
+from einops import rearrange
+from torch import nn
+from vllm.compilation.breakable_cudagraph import eager_break_during_capture
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -28,7 +28,7 @@
-    KimiGatedDeltaNetAttention,
+    KimiGatedDeltaNetAttention as KimiLinearGatedDeltaNetAttention,
@@ -61,6 +61,7 @@
+from vllm.models.kimi_k3.amd.kda import KimiK3DeltaAttention
@@ -472,11 +473,22 @@ def __init__(
-            self.self_attn = KimiGatedDeltaNetAttention(
diff -- vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py
@@ -28,6 +28,13 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/kda.py` added +530/-0; `vllm/models/kimi_k3/amd/linear.py` modified +18/-6; `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` modified +8/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50404 - [Model] Fix Kimi-K3 MLA with disabled context parallelism

- 链接: https://github.com/vllm-project/vllm/pull/50404
- 状态/时间: merged / 2026-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/mla.py`；关联提交 `c416f15710bb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-0，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Fix Kimi-K3 MLA with disabled context parallelism」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/mla.py`；技术摘要: 覆盖「[Model] Fix Kimi-K3 MLA with disabled context parallelism」；主要实现面是 `vllm/models/kimi_k3/nvidia/mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/mla.py` modified +5/-0 (5 lines); hunks: -301,6 +301,11 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/mla.py` modified +5/-0 (5 lines); hunks: -301,6 +301,11 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/mla.py
@@ -301,6 +301,11 @@ def __init__(
+        if getattr(self.impl, "dcp_world_size", -1) < 1:
+            # FlashAttention requires the cp_world_size is positive and the cp_rank
+            # is non negative; manually set here if not set by caller (-1 is unset)
+            self.impl.dcp_world_size = 1
+            self.impl.dcp_rank = 0
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/mla.py` modified +5/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50912 - [Kimi K3 Perf] option to shard the shared expert for non mega case, 16.98 GiB memory/GPU saved

- 链接: https://github.com/vllm-project/vllm/pull/50912
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `d31de3c421c0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+10/-18，可读 patch 98 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi K3 Perf] option to shard the shared expert for non mega case, 16.98 GiB memory/GPU saved」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Kimi K3 Perf] option to shard the shared expert for non mega case, 16.98 GiB memory/GPU saved」；主要实现面是 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_sequence_parallel.py` modified +6/-9 (15 lines); hunks: -267,21 +267,19 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkey...; -295,7 +293,6 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating，涉及 `test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating`；`vllm/models/kimi_k3/nvidia/model.py` modified +1/-9 (10 lines); hunks: -133,15 +133,14 @@ def shard_sequence_parallel_mlp(; -173,7 +172,6 @@ def __init__(; symbols: shard_sequence_parallel_mlp, __init__，涉及 `shard_sequence_parallel_mlp, __init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_sequence_parallel.py` modified +6/-9 (15 lines); hunks: -267,21 +267,19 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkey...; -295,7 +293,6 @@ def test_shard_sequence_parallel_mlp_gating(; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating
  - `vllm/models/kimi_k3/nvidia/model.py` modified +1/-9 (10 lines); hunks: -133,15 +133,14 @@ def shard_sequence_parallel_mlp(; -173,7 +172,6 @@ def __init__(; symbols: shard_sequence_parallel_mlp, __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_sequence_parallel.py
@@ -267,21 +267,19 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkeypatch):
-    ("enabled", "use_sequence_parallel", "eligible", "tp_size", "expected"),
+    ("enabled", "use_sequence_parallel", "tp_size", "expected"),
-        (True, True, True, 8, True),
-        (False, True, True, 8, False),  # opt-in only
-        (True, False, True, 8, False),  # replication only exists under SP
-        (True, True, False, 8, False),  # FusedMoE path owns the reduction
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -133,15 +133,14 @@ def shard_sequence_parallel_mlp(
-    eligible: bool,
-    if not (use_sequence_parallel and eligible and enabled):
+    if not (use_sequence_parallel and enabled):
@@ -173,7 +172,6 @@ def __init__(
-        can_shard_sequence_parallel: bool = False,
@@ -184,7 +182,6 @@ def __init__(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_sequence_parallel.py` modified +6/-9
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +1/-9
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_sequence_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50929 - [MM][CG] Support ViT full CUDA graph for Kimi-K2.5

- 链接: https://github.com/vllm-project/vllm/pull/50929
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `7cab4368f222`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+247/-1，可读 patch 287 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM][CG] Support ViT full CUDA graph for Kimi-K2.5」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[MM][CG] Support ViT full CUDA graph for Kimi-K2.5」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +247/-1 (248 lines); hunks: -8,7 +8,7; -25,10 +25,19; symbols: KimiK25ForConditionalGeneration, set_aux_hidden_state_layers, get_eagle3_aux_hidden_state_layers, _encoder_cudagraph_pad_totals，涉及 `KimiK25ForConditionalGeneration, set_aux_hidden_state_layers, get_eagle3_aux_hidden_state_layers`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +247/-1 (248 lines); hunks: -8,7 +8,7; -25,10 +25,19; symbols: KimiK25ForConditionalGeneration, set_aux_hidden_state_layers, get_eagle3_aux_hidden_state_layers, _encoder_cudagraph_pad_totals
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -8,7 +8,7 @@
-from typing import Annotated, Any, Literal
+from typing import TYPE_CHECKING, Annotated, Any, ClassVar, Literal
@@ -25,10 +25,19 @@
+    SupportsEncoderCudaGraph,
+if TYPE_CHECKING:
+    from vllm.v1.worker.encoder_cudagraph_defs import (
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +247/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50593 - [Kimi-K3][AMD] Fuse AttnRes state updates and norms

- 链接: https://github.com/vllm-project/vllm/pull/50593
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`；关联提交 `7ac2ec758208`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+208/-49，可读 patch 393 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3][AMD] Fuse AttnRes state updates and norms」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/amd/ops/attn_res.py`, `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[Kimi-K3][AMD] Fuse AttnRes state updates and norms」；主要实现面是 `vllm/models/kimi_k3/amd/ops/attn_res.py`, `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +101/-40 (141 lines); hunks: -7,6 +7,7; -15,69 +16,119; symbols: _attn_res_kernel, attn_res，涉及 `_attn_res_kernel, attn_res`；`tests/models/kimi_k3/test_amd_attn_res.py` modified +91/-0 (91 lines); hunks: -88,15 +88,106 @@ def test_amd_attn_res_matches_reference(; symbols: test_amd_attn_res_matches_reference, test_amd_attn_res_fused_contract，涉及 `test_amd_attn_res_matches_reference, test_amd_attn_res_fused_contract`；`vllm/models/kimi_k3/amd/linear.py` modified +16/-9 (25 lines); hunks: -141,17 +141,22 @@ def _apply_attn_res(; -610,19 +615,20 @@ def forward_attn_residual(; symbols: _apply_attn_res, forward_attn_residual，涉及 `_apply_attn_res, forward_attn_residual`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +101/-40 (141 lines); hunks: -7,6 +7,7; -15,69 +16,119; symbols: _attn_res_kernel, attn_res
  - `tests/models/kimi_k3/test_amd_attn_res.py` modified +91/-0 (91 lines); hunks: -88,15 +88,106 @@ def test_amd_attn_res_matches_reference(; symbols: test_amd_attn_res_matches_reference, test_amd_attn_res_fused_contract
  - `vllm/models/kimi_k3/amd/linear.py` modified +16/-9 (25 lines); hunks: -141,17 +141,22 @@ def _apply_attn_res(; -610,19 +615,20 @@ def forward_attn_residual(; symbols: _apply_attn_res, forward_attn_residual
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/ops/attn_res.py
@@ -7,6 +7,7 @@
@@ -15,69 +16,119 @@
+    delta_ptr,
+    output_norm_weight_ptr,
+    stride_delta_m: tl.constexpr,
+    block_write_idx: tl.constexpr,
+    output_norm_eps: tl.constexpr,
diff -- tests/models/kimi_k3/test_amd_attn_res.py
@@ -88,15 +88,106 @@ def test_amd_attn_res_matches_reference(
+        None,
+        None,
+        -1,
+        0.0,
+@pytest.mark.parametrize(
+    (
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -141,17 +141,22 @@ def _apply_attn_res(
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/ops/attn_res.py` modified +101/-40; `vllm/models/kimi_k3/amd/linear.py` modified +16/-9
  - tests: `tests/models/kimi_k3/test_amd_attn_res.py` modified +91/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_attn_res.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50886 - [Bugfix][Reasoning] kimi_k3: O(delta) reasoning-end check on the decode path

- 链接: https://github.com/vllm-project/vllm/pull/50886
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`；关联提交 `adbf08d977fb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+157/-10，可读 patch 202 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Reasoning] kimi_k3: O(delta) reasoning-end check on the decode path」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix][Reasoning] kimi_k3: O(delta) reasoning-end check on the decode path」；主要实现面是 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +95/-0 (95 lines); hunks: -248,3 +248,98 @@ def test_adjust_request_keeps_xtml_markers_contiguous():; symbols: test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end, last, test_is_reasoning_end_streaming_only_scans_the_step_window，涉及 `test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end, last`；`vllm/reasoning/kimi_k3_reasoning_parser.py` modified +62/-10 (72 lines); hunks: -22,7 +22,7; -36,17 +36,47; symbols: _match_at, _subseq_index, _newest_marker, KimiK3ReasoningParser，涉及 `_match_at, _subseq_index, _newest_marker`。
- 代码 diff 细节:
  - `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +95/-0 (95 lines); hunks: -248,3 +248,98 @@ def test_adjust_request_keeps_xtml_markers_contiguous():; symbols: test_adjust_request_keeps_xtml_markers_contiguous, _reference_is_reasoning_end, last, test_is_reasoning_end_streaming_only_scans_the_step_window
  - `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +62/-10 (72 lines); hunks: -22,7 +22,7; -36,17 +36,47; symbols: _match_at, _subseq_index, _newest_marker, KimiK3ReasoningParser
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_kimi_k3_reasoning_parser.py
@@ -248,3 +248,98 @@ def test_adjust_request_keeps_xtml_markers_contiguous():
+OPEN_IDS = [1, 2, 3]
+CLOSE_IDS = [4, 2, 3]
+def _reference_is_reasoning_end(input_ids: list[int]) -> bool:
+    """Full-sequence reference for the streaming check to be measured against.
+    Two independent last-occurrence scans, i.e. the straightforward reading of
+    "reasoning ended iff the newest think marker is a close marker".
diff -- vllm/reasoning/kimi_k3_reasoning_parser.py
@@ -22,7 +22,7 @@
-from collections.abc import Sequence
+from collections.abc import Iterable, Sequence
@@ -36,17 +36,47 @@
+def _match_at(haystack: Sequence[int], i: int, needle: Sequence[int]) -> bool:
+    """Whether *needle* occurs in *haystack* starting at *i*.
+    Compares element by element rather than slicing: ``haystack`` is usually a
```

- 已读文件:
  - tests: `tests/reasoning/test_kimi_k3_reasoning_parser.py` modified +95/-0
  - runtime: `vllm/reasoning/kimi_k3_reasoning_parser.py` modified +62/-10
- 验证与风险: diff 自带测试面 `tests/reasoning/test_kimi_k3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50567 - [Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch

- 链接: https://github.com/vllm-project/vllm/pull/50567
- 状态/时间: merged / 2026-08-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/ops/attn_res.py`；关联提交 `41ba11b8413c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-1，可读 patch 33 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/ops/attn_res.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/attn_res.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +4/-1 (5 lines); hunks: -187,14 +187,17 @@ def attn_res(; symbols: attn_res，涉及 `attn_res`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +4/-1 (5 lines); hunks: -187,14 +187,17 @@ def attn_res(; symbols: attn_res
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/attn_res.py
@@ -187,14 +187,17 @@ def attn_res(
-    # Triton handles block boundaries and final pre-norm output.
+    # Triton handles block boundaries and final pre-norm output. The native op
+    # is only compiled for SM100 under CUDA >= 13, so a device check alone is
+    # not enough to know it exists.
+        and hasattr(torch.ops._C, "kimi_k3_attn_res")
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/attn_res.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/ops/attn_res.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50656 - [Kimi-K3] Add option to shard the shared expert instead of replicating

- 链接: https://github.com/vllm-project/vllm/pull/50656
- 状态/时间: merged / 2026-08-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `5df9999fcfaa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+154/-3，可读 patch 242 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Add option to shard the shared expert instead of replicating」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Kimi-K3] Add option to shard the shared expert instead of replicating」；主要实现面是 `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_sequence_parallel.py` modified +79/-0 (79 lines); hunks: -10,6 +10,7; -265,6 +266,84 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkeyp...; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating, test_sharded_sequence_parallel_mlp_matches_replicated, test_sp_all_gather_uses_custom_kernel，涉及 `test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating, test_sharded_sequence_parallel_mlp_matches_replicated`；`vllm/models/kimi_k3/nvidia/model.py` modified +62/-3 (65 lines); hunks: -129,7 +129,42; -138,27 +173,38 @@ def __init__(; symbols: shard_sequence_parallel_mlp, KimiMLP, __init__，涉及 `shard_sequence_parallel_mlp, KimiMLP, __init__`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_sequence_parallel.py` modified +79/-0 (79 lines); hunks: -10,6 +10,7; -265,6 +266,84 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkeyp...; symbols: test_kimi_mtp_restores_sequence_parallel_output, test_shard_sequence_parallel_mlp_gating, test_sharded_sequence_parallel_mlp_matches_replicated, test_sp_all_gather_uses_custom_kernel
  - `vllm/models/kimi_k3/nvidia/model.py` modified +62/-3 (65 lines); hunks: -129,7 +129,42; -138,27 +173,38 @@ def __init__(; symbols: shard_sequence_parallel_mlp, KimiMLP, __init__
- 关键代码摘录:

```diff
diff -- tests/models/kimi_k3/test_sequence_parallel.py
@@ -10,6 +10,7 @@
+from vllm.model_executor.layers.activation import SiluAndMul
@@ -265,6 +266,84 @@ def test_kimi_mtp_restores_sequence_parallel_output(monkeypatch):
+@pytest.mark.parametrize(
+    ("enabled", "use_sequence_parallel", "eligible", "tp_size", "expected"),
+    [
+        (True, True, True, 8, True),
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -129,7 +129,42 @@
+def shard_sequence_parallel_mlp(
+    hidden_size: int,
+    intermediate_size: int,
+    use_sequence_parallel: bool,
+    eligible: bool,
+) -> bool:
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_sequence_parallel.py` modified +79/-0
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +62/-3
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_sequence_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50761 - [ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32

- 链接: https://github.com/vllm-project/vllm/pull/50761
- 状态/时间: merged / 2026-08-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/amd/linear.py`；关联提交 `c6668106760e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-1，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32」；主要实现面是 `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/amd/linear.py` modified +4/-1 (5 lines); hunks: -210,7 +210,10 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/amd/linear.py` modified +4/-1 (5 lines); hunks: -210,7 +210,10 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -210,7 +210,10 @@ def __init__(
-        self.gate.e_score_correction_bias = nn.Parameter(torch.empty(num_experts))
+        # Preserve FP32 checkpoint values and match FP32 router logits.
+        self.gate.e_score_correction_bias = nn.Parameter(
+            torch.empty(num_experts, dtype=torch.float32)
+        )
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/amd/linear.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/amd/linear.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50500 - [Compressed-Tensors] Support Kimi-K3 quantized models

- 链接: https://github.com/vllm-project/vllm/pull/50500
- 状态/时间: merged / 2026-07-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/model.py`；关联提交 `d87d2ca74791`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-1，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Compressed-Tensors] Support Kimi-K3 quantized models」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`；技术摘要: 覆盖「[Compressed-Tensors] Support Kimi-K3 quantized models」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` modified +8/-1 (9 lines); hunks: -951,7 +951,13 @@ def forward(; -1221,6 +1227,7 @@ def load_weights(; symbols: forward, KimiLinearModel, __init__, load_weights，涉及 `forward, KimiLinearModel, __init__`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +8/-1 (9 lines); hunks: -951,7 +951,13 @@ def forward(; -1221,6 +1227,7 @@ def load_weights(; symbols: forward, KimiLinearModel, __init__, load_weights
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -951,7 +951,13 @@ def forward(
-class KimiLinearModel(nn.Module, EagleModelMixin):
+class KimiLinearModel(nn.Module, EagleModelMixin, SupportsQuant):
+    packed_modules_mapping = {
+        "gate_up_proj": ["gate_proj", "up_proj"],
+        "in_proj_qkvgfab": ["q_proj", "k_proj", "v_proj", "b_proj", "f_a_proj"],
+        "conv1d": ["q_conv1d", "k_conv1d", "v_conv1d"],
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +8/-1
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50420 - [Frontend][Bugfix] Use default tool call IDs for Kimi K3 for conversation-level uniqueness

- 链接: https://github.com/vllm-project/vllm/pull/50420
- 状态/时间: merged / 2026-07-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`；关联提交 `ab98034d4ccc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+55/-53，可读 patch 275 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend][Bugfix] Use default tool call IDs for Kimi K3 for conversation-level uniqueness」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`；技术摘要: 覆盖「[Frontend][Bugfix] Use default tool call IDs for Kimi K3 for conversation-level uniqueness」；主要实现面是 `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +9/-3 (12 lines); hunks: -141,7 +141,6 @@ def test_extract_tool_calls_with_response_and_typed_argument...; -168,7 +167,6 @@ def test_delegating_parser_preserves_tool_calls_after_reason...; symbols: test_extract_tool_calls_with_response_and_typed_arguments, test_delegating_parser_preserves_tool_calls_after_reasoning, test_streaming_split_markers_do_not_leak, test_tool_call_ids_are_unique_across_messages，涉及 `test_extract_tool_calls_with_response_and_typed_arguments, test_delegating_parser_preserves_tool_calls_after_reasoning, test_streaming_split_markers_do_not_leak`；`vllm/tool_parsers/kimi_k3_tool_parser.py` modified +0/-10 (10 lines); hunks: -218,7 +218,6 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall |...; -234,16 +233,7 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall |...; symbols: _decode_call，涉及 `_decode_call`。
- 代码 diff 细节:
  - `tests/tool_use/test_kimi_k3_tool_parser.py` modified +9/-3 (12 lines); hunks: -141,7 +141,6 @@ def test_extract_tool_calls_with_response_and_typed_argument...; -168,7 +167,6 @@ def test_delegating_parser_preserves_tool_calls_after_reason...; symbols: test_extract_tool_calls_with_response_and_typed_arguments, test_delegating_parser_preserves_tool_calls_after_reasoning, test_streaming_split_markers_do_not_leak, test_tool_call_ids_are_unique_across_messages
  - `vllm/tool_parsers/kimi_k3_tool_parser.py` modified +0/-10 (10 lines); hunks: -218,7 +218,6 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall |...; -234,16 +233,7 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall |...; symbols: _decode_call
- 关键代码摘录:

```diff
diff -- tests/tool_use/test_kimi_k3_tool_parser.py
@@ -141,7 +141,6 @@ def test_extract_tool_calls_with_response_and_typed_arguments():
-    assert tool_call.id == "calc:0"
@@ -168,7 +167,6 @@ def test_delegating_parser_preserves_tool_calls_after_reasoning():
-    assert tool_calls[0].id == "calc:0"
@@ -364,11 +362,19 @@ def test_streaming_split_markers_do_not_leak():
-    assert tool_deltas[0].id == "calc:0"
+def test_tool_call_ids_are_unique_across_messages():
diff -- vllm/tool_parsers/kimi_k3_tool_parser.py
@@ -218,7 +218,6 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall | None:
-        tool_index = call_attrs.get("index", "")
@@ -234,16 +233,7 @@ def _decode_call(self, attrs: str, body: str) -> ToolCall | None:
-        tool_call_id = tool_name
-        if tool_index:
-            try:
-                tool_call_id = f"{tool_name}:{int(tool_index) - 1}"
```

- 已读文件:
  - tests: `tests/tool_use/test_kimi_k3_tool_parser.py` modified +9/-3
  - runtime: `vllm/tool_parsers/kimi_k3_tool_parser.py` modified +0/-10
- 验证与风险: diff 自带测试面 `tests/tool_use/test_kimi_k3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50000 - [New model] Kimi K3

- 链接: https://github.com/vllm-project/vllm/pull/50000
- 状态/时间: merged / 2026-07-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`, `vllm/models/kimi_k3/nvidia/dspark_mla.py`, `vllm/models/kimi_k3/nvidia/model.py` 等 6 个文件；关联提交 `aeeb36b1f171`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 82 个文件，+2931/-1349，可读 patch 6277 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[New model] Kimi K3」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/model_executor/models/kimi_linear.py`, `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[New model] Kimi K3」；主要实现面是 `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/model_executor/models/kimi_linear.py`, `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +482/-291 (773 lines); hunks: -1,32 +1,33; -36,49 +37,118; symbols: kda_attention, kda_attention_fake, a_log_weight_loader, loader，涉及 `kda_attention, kda_attention_fake, a_log_weight_loader`；`vllm/model_executor/models/kimi_linear.py` removed +0/-646 (646 lines); hunks: -1,646 +0,0; symbols: KimiMLP, __init__, forward, KimiMoE，涉及 `KimiMLP, __init__, forward`；`vllm/model_executor/models/kimi_k25_vit.py` modified +204/-25 (229 lines); hunks: -34,6 +34,7; -154,9 +155,7 @@ def __init__(; symbols: __init__, reset_parameters, forward, get_pos_embeds，涉及 `__init__, reset_parameters, forward`；`vllm/model_executor/warmup/kimi_k3_triton_warmup.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: _get_kda_layer, _warm_attn_res, _warm_recurrent_kda, kimi_k3_triton_warmup，涉及 `_get_kda_layer, _warm_attn_res, _warm_recurrent_kda`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +482/-291 (773 lines); hunks: -1,32 +1,33; -36,49 +37,118; symbols: kda_attention, kda_attention_fake, a_log_weight_loader, loader
  - `vllm/model_executor/models/kimi_linear.py` removed +0/-646 (646 lines); hunks: -1,646 +0,0; symbols: KimiMLP, __init__, forward, KimiMoE
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +204/-25 (229 lines); hunks: -34,6 +34,7; -154,9 +155,7 @@ def __init__(; symbols: __init__, reset_parameters, forward, get_pos_embeds
  - `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: _get_kda_layer, _warm_attn_res, _warm_recurrent_kda, kimi_k3_triton_warmup
  - `tests/models/test_dspark_mla.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: test_dspark_mla_uses_compile_free_model_entrypoint, test_dspark_mla_checkpoint_weight_mapping, test_dspark_mla_shares_frozen_target_weights_and_skips_training_head, test_dspark_markov_head_is_replicated
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py
@@ -1,32 +1,33 @@
+from collections.abc import Callable
+from torch.nn.parameter import Parameter
-from vllm.config import VllmConfig, get_current_vllm_config
-from vllm.distributed import (
-    divide,
-)
diff -- vllm/model_executor/models/kimi_linear.py
@@ -1,646 +0,0 @@
-# SPDX-License-Identifier: Apache-2.0
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
-from collections.abc import Iterable
-import torch
-from torch import nn
-from vllm.compilation.decorators import support_torch_compile
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -34,6 +34,7 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` modified +482/-291; `vllm/model_executor/models/kimi_linear.py` removed +0/-646; `vllm/model_executor/models/kimi_k25_vit.py` modified +204/-25; `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` added +182/-0; `vllm/models/kimi_k3/nvidia/dspark_mla.py` modified +1/-21; `vllm/transformers_utils/configs/kimi_linear.py` modified +17/-4
  - tests: `tests/models/test_dspark_mla.py` added +143/-0
- 验证与风险: diff 自带测试面 `requirements/test/cuda.txt`, `tests/kernels/moe/test_deepgemm.py`, `tests/models/registry.py`, `tests/models/test_dspark_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50262 - [ROCm][CI] Fix Kimi K3 KDA on ROCm

- 链接: https://github.com/vllm-project/vllm/pull/50262
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/nvidia/kda.py`；关联提交 `381b69162020`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+8/-2，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Fix Kimi K3 KDA on ROCm」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/nvidia/kda.py`；技术摘要: 覆盖「[ROCm][CI] Fix Kimi K3 KDA on ROCm」；主要实现面是 `vllm/models/kimi_k3/nvidia/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/kda.py` modified +2/-0 (2 lines); hunks: -164,6 +164,8 @@ def is_flashkda_supported(; symbols: is_flashkda_supported，涉及 `is_flashkda_supported`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/kda.py` modified +2/-0 (2 lines); hunks: -164,6 +164,8 @@ def is_flashkda_supported(; symbols: is_flashkda_supported
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/kda.py
@@ -164,6 +164,8 @@ def is_flashkda_supported(
+    if not current_platform.is_cuda():
+        return False
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/kda.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/nvidia/kda.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50093 - [Model] Add Kimi K3 support: Python frontend [2/2]

- 链接: https://github.com/vllm-project/vllm/pull/50093
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/renderers/test_kimi_k3.py`, `tests/tool_parsers/test_kimi_k3_named_tool_choice.py`, `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/parser/kimi_k3.py` 等 8 个文件；关联提交 `f5a7cce9b6a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 20 个文件，+3056/-5，可读 patch 3209 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add Kimi K3 support: Python frontend [2/2]」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`；技术摘要: 覆盖「[Model] Add Kimi K3 support: Python frontend [2/2]」；主要实现面是 `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_use/test_kimi_k3_tool_parser.py` added +600/-0 (600 lines); hunks: -0,0 +1,600; symbols: DummyTokenizer, get_vocab, encode, KimiK3DelegatingParser，涉及 `DummyTokenizer, get_vocab, encode`；`vllm/tool_parsers/kimi_k3_tool_parser.py` added +405/-0 (405 lines); hunks: -0,0 +1,405; symbols: _partial_tag_overlap, KimiK3ToolParser, __init__, adjust_request，涉及 `_partial_tag_overlap, KimiK3ToolParser, __init__`；`vllm/reasoning/kimi_k3_reasoning_parser.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _subseq_index, KimiK3ReasoningParser, __init__, reasoning_start_str，涉及 `_subseq_index, KimiK3ReasoningParser, __init__`；`tests/reasoning/test_kimi_k3_reasoning_parser.py` added +250/-0 (250 lines); hunks: -0,0 +1,250; symbols: DummyTokenizer, get_vocab, encode, ReasoningOnlyParser，涉及 `DummyTokenizer, get_vocab, encode`。
- 代码 diff 细节:
  - `tests/tool_use/test_kimi_k3_tool_parser.py` added +600/-0 (600 lines); hunks: -0,0 +1,600; symbols: DummyTokenizer, get_vocab, encode, KimiK3DelegatingParser
  - `vllm/tool_parsers/kimi_k3_tool_parser.py` added +405/-0 (405 lines); hunks: -0,0 +1,405; symbols: _partial_tag_overlap, KimiK3ToolParser, __init__, adjust_request
  - `vllm/reasoning/kimi_k3_reasoning_parser.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _subseq_index, KimiK3ReasoningParser, __init__, reasoning_start_str
  - `tests/reasoning/test_kimi_k3_reasoning_parser.py` added +250/-0 (250 lines); hunks: -0,0 +1,250; symbols: DummyTokenizer, get_vocab, encode, ReasoningOnlyParser
  - `tests/tool_parsers/test_kimi_k3_named_tool_choice.py` added +62/-0 (62 lines); hunks: -0,0 +1,62; symbols: _DummyTokenizer, get_vocab, encode, _request
- 关键代码摘录:

```diff
diff -- tests/tool_use/test_kimi_k3_tool_parser.py
@@ -0,0 +1,600 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import json
+import pytest
+from vllm.entrypoints.openai.chat_completion.protocol import (
+    ChatCompletionRequest,
diff -- vllm/tool_parsers/kimi_k3_tool_parser.py
@@ -0,0 +1,405 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Tool-call parser for the Kimi K3 (XTML) chat format.
+This turns the generated XTML ``response`` and ``tools`` channels back into
+OpenAI-compatible ``content`` and ``tool_calls``.
+K3 assistant tool calls live in a nested ``tools`` channel::
diff -- vllm/reasoning/kimi_k3_reasoning_parser.py
@@ -0,0 +1,371 @@
```

- 已读文件:
  - tests: `tests/tool_use/test_kimi_k3_tool_parser.py` added +600/-0; `tests/reasoning/test_kimi_k3_reasoning_parser.py` added +250/-0; `tests/tool_parsers/test_kimi_k3_named_tool_choice.py` added +62/-0; `tests/renderers/test_kimi_k3.py` added +353/-0
  - runtime: `vllm/tool_parsers/kimi_k3_tool_parser.py` added +405/-0; `vllm/reasoning/kimi_k3_reasoning_parser.py` added +371/-0; `vllm/renderers/kimi_k3.py` added +220/-0; `vllm/parser/kimi_k3.py` added +135/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/renderers/test_kimi_k3.py`, `tests/tool_parsers/test_kimi_k3_named_tool_choice.py`, `tests/tool_parsers/test_structural_tag_registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50089 - [Model] Add Kimi K3 support: model files and kernels [1/N]

- 链接: https://github.com/vllm-project/vllm/pull/50089
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_kimi_k3_latent_moe_tail.py`, `benchmarks/kernels/benchmark_kimi_k3_sp_collectives.py`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `tests/models/kimi_k3/test_attn_res.py`, `tests/models/kimi_k3/test_eagle3.py` 等 46 个文件；关联提交 `7c6729b76959`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 109 个文件，+28009/-773，可读 patch 30127 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add Kimi K3 support: model files and kernels [1/N]」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py`, `vllm/models/kimi_k3/amd/linear.py`；技术摘要: 覆盖「[Model] Add Kimi K3 support: model files and kernels [1/N]」；主要实现面是 `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py`, `vllm/models/kimi_k3/amd/linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/model.py` added +1859/-0 (1859 lines); hunks: -0,0 +1,1859; symbols: KimiMLP, __init__, forward, KimiRoutedOutputTransform，涉及 `KimiMLP, __init__, forward`；`vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py` added +1291/-0 (1291 lines); hunks: -0,0 +1,1291; symbols: _as_cute, validate_configuration, _epilogue_tma_store_add_shared, _compute_stages，涉及 `_as_cute, validate_configuration, _epilogue_tma_store_add_shared`；`vllm/models/kimi_k3/amd/linear.py` added +1065/-0 (1065 lines); hunks: -0,0 +1,1065; symbols: KimiMLP, __init__, forward, KimiRoutedOutputTransform，涉及 `KimiMLP, __init__, forward`；`vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` added +1012/-0 (1012 lines); hunks: -0,0 +1,1012; symbols: _mapping, validate_shape, _select_routed_schedule, AllReduceRMSNormWithReduceScatterEarlyExit，涉及 `_mapping, validate_shape, _select_routed_schedule`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/model.py` added +1859/-0 (1859 lines); hunks: -0,0 +1,1859; symbols: KimiMLP, __init__, forward, KimiRoutedOutputTransform
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py` added +1291/-0 (1291 lines); hunks: -0,0 +1,1291; symbols: _as_cute, validate_configuration, _epilogue_tma_store_add_shared, _compute_stages
  - `vllm/models/kimi_k3/amd/linear.py` added +1065/-0 (1065 lines); hunks: -0,0 +1,1065; symbols: KimiMLP, __init__, forward, KimiRoutedOutputTransform
  - `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` added +1012/-0 (1012 lines); hunks: -0,0 +1,1012; symbols: _mapping, validate_shape, _select_routed_schedule, AllReduceRMSNormWithReduceScatterEarlyExit
  - `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` added +938/-0 (938 lines); hunks: -0,0 +1,938; symbols: recompute_w_u_fwd_kernel, recompute_w_u_fwd, chunk_gla_fwd_kernel_o, chunk_gla_fwd_o_gk
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -0,0 +1,1859 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Kimi-K3 multimodal model implementation for vLLM."""
+import math
+from collections.abc import Iterable
+from typing import Any, cast
diff -- vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py
@@ -0,0 +1,1291 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright (c) 2025 - 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
+# SPDX-License-Identifier: BSD-3-Clause
+# Redistribution and use in source and binary forms, with or without
+# modification, are permitted provided that the following conditions are met:
diff -- vllm/models/kimi_k3/amd/linear.py
@@ -0,0 +1,1065 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` added +1859/-0; `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm.py` added +1291/-0; `vllm/models/kimi_k3/amd/linear.py` added +1065/-0; `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py` added +1012/-0; `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` added +938/-0; `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` added +935/-0
- 验证与风险: diff 自带测试面 `tests/distributed/test_custom_all_reduce.py`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `tests/kernels/core/test_activation.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50131 - [Bugfix] Add missing `vllm/models/kimi_k3/__init__.py`

- 链接: https://github.com/vllm-project/vllm/pull/50131
- 状态/时间: merged / 2026-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`；关联提交 `62d8db7c05af`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-0，可读 patch 6 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Add missing `vllm/models/kimi_k3/__init__.py`」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`；技术摘要: 覆盖「[Bugfix] Add missing `vllm/models/kimi_k3/__init__.py`」；主要实现面是 `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2；`vllm/models/kimi_k3/amd/ops/__init__.py` modified +2/-0 (2 lines); hunks: -0,0 +1,2。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
  - `vllm/models/kimi_k3/amd/ops/__init__.py` modified +2/-0 (2 lines); hunks: -0,0 +1,2
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/__init__.py
@@ -0,0 +1,2 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
diff -- vllm/models/kimi_k3/amd/ops/__init__.py
@@ -0,0 +1,2 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/__init__.py` added +2/-0; `vllm/models/kimi_k3/amd/ops/__init__.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #50090 - [Kimi-K3] Add AttnRes kernels

- 链接: https://github.com/vllm-project/vllm/pull/50090
- 状态/时间: merged / 2026-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/amd/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py` 等 8 个文件；关联提交 `61ac36802103`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1719/-0，可读 patch 1776 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kimi-K3] Add AttnRes kernels」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`；技术摘要: 覆盖「[Kimi-K3] Add AttnRes kernels」；主要实现面是 `vllm/models/kimi_k3/nvidia/ops/attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/kimi_k3/nvidia/ops/attn_res.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: get_attn_res_triton_warmup_profiles, _attn_res_kernel, attn_res，涉及 `get_attn_res_triton_warmup_profiles, _attn_res_kernel, attn_res`；`tests/models/kimi_k3/test_attn_res.py` added +193/-0 (193 lines); hunks: -0,0 +1,193; symbols: _randn_with_row_padding, _reference, test_attn_res, test_attn_res_block_counts，涉及 `_randn_with_row_padding, _reference, test_attn_res`；`vllm/models/kimi_k3/amd/ops/attn_res.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: _attn_res_kernel, attn_res，涉及 `_attn_res_kernel, attn_res`；`tests/models/kimi_k3/test_amd_attn_res.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: _randn_with_row_padding, _reference, test_amd_attn_res_matches_reference，涉及 `_randn_with_row_padding, _reference, test_amd_attn_res_matches_reference`。
- 代码 diff 细节:
  - `vllm/models/kimi_k3/nvidia/ops/attn_res.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: get_attn_res_triton_warmup_profiles, _attn_res_kernel, attn_res
  - `tests/models/kimi_k3/test_attn_res.py` added +193/-0 (193 lines); hunks: -0,0 +1,193; symbols: _randn_with_row_padding, _reference, test_attn_res, test_attn_res_block_counts
  - `vllm/models/kimi_k3/amd/ops/attn_res.py` added +132/-0 (132 lines); hunks: -0,0 +1,132; symbols: _attn_res_kernel, attn_res
  - `tests/models/kimi_k3/test_amd_attn_res.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: _randn_with_row_padding, _reference, test_amd_attn_res_matches_reference
  - `vllm/models/kimi_k3/nvidia/ops/__init__.py` added +6/-0 (6 lines); hunks: -0,0 +1,6
- 关键代码摘录:

```diff
diff -- vllm/models/kimi_k3/nvidia/ops/attn_res.py
@@ -0,0 +1,245 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# SPDX-FileCopyrightText: Songlin Yang, Yu Zhang, Zhiyuan Li
+#
+# This file contains code adapted from the flash-linear-attention project.
+# The original source code was licensed under the MIT license and included
diff -- tests/models/kimi_k3/test_attn_res.py
@@ -0,0 +1,193 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+import torch
+import torch.nn.functional as F
+from vllm.models.kimi_k3.nvidia.ops import attn_res
diff -- vllm/models/kimi_k3/amd/ops/attn_res.py
@@ -0,0 +1,132 @@
```

- 已读文件:
  - runtime: `vllm/models/kimi_k3/nvidia/ops/attn_res.py` added +245/-0; `vllm/models/kimi_k3/amd/ops/attn_res.py` added +132/-0; `vllm/models/kimi_k3/nvidia/ops/__init__.py` added +6/-0; `vllm/models/kimi_k3/amd/__init__.py` added +2/-0; `vllm/models/kimi_k3/nvidia/__init__.py` added +2/-0; `vllm/models/kimi_k3/amd/ops/__init__.py` added +0/-0
  - tests: `tests/models/kimi_k3/test_attn_res.py` added +193/-0; `tests/models/kimi_k3/test_amd_attn_res.py` added +102/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_attn_res.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47416 - [perf]Add fused Kimi image preprocessing

- 链接: https://github.com/vllm-project/vllm/pull/47416
- 状态/时间: merged / 2026-07-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`；关联提交 `5ad11172b791`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+402/-2，可读 patch 462 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[perf]Add fused Kimi image preprocessing」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`, `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[perf]Add fused Kimi image preprocessing」；主要实现面是 `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`, `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/processors/kimi_k25_vision_fused.py` added +352/-0 (352 lines); hunks: -0,0 +1,352; symbols: _write_fused_patches, navit_resize_image, navit_resize_video, _to_pil，涉及 `_write_fused_patches, navit_resize_image, navit_resize_video`；`vllm/model_executor/models/kimi_k25.py` modified +10/-0 (10 lines); hunks: -56,6 +56,10; -108,10 +112,16 @@ def __init__(self, ctx: InputProcessingContext) -> None:; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/transformers_utils/processors/kimi_k25_vision_fused.py` added +352/-0 (352 lines); hunks: -0,0 +1,352; symbols: _write_fused_patches, navit_resize_image, navit_resize_video, _to_pil
  - `vllm/model_executor/models/kimi_k25.py` modified +10/-0 (10 lines); hunks: -56,6 +56,10; -108,10 +112,16 @@ def __init__(self, ctx: InputProcessingContext) -> None:; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/processors/kimi_k25_vision_fused.py
@@ -0,0 +1,352 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Optimized CPU image processor for Kimi-K2.5/K2.6 vision chunks."""
+import io
+import json
+import math
diff -- vllm/model_executor/models/kimi_k25.py
@@ -56,6 +56,10 @@
+from vllm.transformers_utils.processors.kimi_k25_vision_fused import (
+    KimiK25FusedVisionProcessor,
+)
+from vllm.utils.import_utils import is_numba_available
@@ -108,10 +112,16 @@ def __init__(self, ctx: InputProcessingContext) -> None:
+        processor_cls = KimiK25FusedVisionProcessor if is_numba_available() else None
```

- 已读文件:
  - runtime: `vllm/transformers_utils/processors/kimi_k25_vision_fused.py` added +352/-0; `vllm/model_executor/models/kimi_k25.py` modified +10/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/processor.py`, `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46610 - [Frontend] Add Streaming Parser Engine and new Kimi k2.5/k2.6/k2.7 Parser

- 链接: https://github.com/vllm-project/vllm/pull/46610
- 状态/时间: merged / 2026-06-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/parser/kimi_k2.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`；关联提交 `2bc20e8abaf7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+397/-570，可读 patch 1069 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Add Streaming Parser Engine and new Kimi k2.5/k2.6/k2.7 Parser」；模型线: Kimi K2/K2.5/Linear/VL；类别: 文档/测试/CI；主要 diff: `vllm/tool_parsers/kimi_k2_tool_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`, `tests/reasoning/test_kimi_k2_reasoning_parser.py`；技术摘要: 覆盖「[Frontend] Add Streaming Parser Engine and new Kimi k2.5/k2.6/k2.7 Parser」；主要实现面是 `vllm/tool_parsers/kimi_k2_tool_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`, `tests/reasoning/test_kimi_k2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +4/-262 (266 lines); hunks: -1,278 +1,20; symbols: KimiK2ToolParser, __init__, adjust_request, extract_tool_calls，涉及 `KimiK2ToolParser, __init__, adjust_request`；`vllm/reasoning/kimi_k2_reasoning_parser.py` modified +3/-240 (243 lines); hunks: -1,245 +1,8; symbols: KimiK2ReasoningParser, __init__, reasoning_start_str, reasoning_end_str，涉及 `KimiK2ReasoningParser, __init__, reasoning_start_str`；`tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +5/-67 (72 lines); hunks: -7,7 +7,6; -33,20 +32,6 @@ def kimi_k2_tokenizer():; symbols: kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled, test_extract_reasoning_with_think_tags，涉及 `kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled`；`vllm/parser/kimi_k2.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: kimi_k2_config, KimiK2Parser, __init__, _extract_tool_id_and_name，涉及 `kimi_k2_config, KimiK2Parser, __init__`。
- 代码 diff 细节:
  - `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +4/-262 (266 lines); hunks: -1,278 +1,20; symbols: KimiK2ToolParser, __init__, adjust_request, extract_tool_calls
  - `vllm/reasoning/kimi_k2_reasoning_parser.py` modified +3/-240 (243 lines); hunks: -1,245 +1,8; symbols: KimiK2ReasoningParser, __init__, reasoning_start_str, reasoning_end_str
  - `tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +5/-67 (72 lines); hunks: -7,7 +7,6; -33,20 +32,6 @@ def kimi_k2_tokenizer():; symbols: kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled, test_extract_reasoning_with_think_tags
  - `vllm/parser/kimi_k2.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: kimi_k2_config, KimiK2Parser, __init__, _extract_tool_id_and_name
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/kimi_k2_tool_parser.py
@@ -1,278 +1,20 @@
-from collections.abc import Sequence
-import regex as re
-from vllm.entrypoints.openai.engine.protocol import (
-    DeltaFunctionCall,
-    DeltaMessage,
-    DeltaToolCall,
diff -- vllm/reasoning/kimi_k2_reasoning_parser.py
@@ -1,245 +1,8 @@
-from collections.abc import Iterable, Sequence
-from typing import TYPE_CHECKING
+from vllm.parser.engine.registered_adapters import KimiK2ParserReasoningAdapter
-from transformers import PreTrainedTokenizerBase
+KimiK2ReasoningParser = KimiK2ParserReasoningAdapter
-from vllm.entrypoints.openai.engine.protocol import DeltaMessage
diff -- tests/reasoning/test_kimi_k2_reasoning_parser.py
@@ -7,7 +7,6 @@
```

- 已读文件:
  - runtime: `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +4/-262; `vllm/reasoning/kimi_k2_reasoning_parser.py` modified +3/-240; `vllm/parser/kimi_k2.py` added +285/-0
  - tests: `tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +5/-67
- 验证与风险: diff 自带测试面 `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_kimi_k2_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41992 - [MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL

- 链接: https://github.com/vllm-project/vllm/pull/41992
- 状态/时间: merged / 2026-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`；关联提交 `fa85ead2f378`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+498/-39，可读 patch 726 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「[MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL」；主要实现面是 `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/moonvit.py` modified +266/-37 (303 lines); hunks: -45,7 +45,9; -110,23 +112,42 @@ def __init__(; symbols: __init__, reset_parameters, forward, get_pos_embeds，涉及 `__init__, reset_parameters, forward`；`vllm/model_executor/models/kimi_vl.py` modified +195/-2 (197 lines); hunks: -56,7 +56,11; -79,6 +83,7; symbols: get_replacement, KimiVLForConditionalGeneration, __init__, get_encoder_cudagraph_config，涉及 `get_replacement, KimiVLForConditionalGeneration, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/moonvit.py` modified +266/-37 (303 lines); hunks: -45,7 +45,9; -110,23 +112,42 @@ def __init__(; symbols: __init__, reset_parameters, forward, get_pos_embeds
  - `vllm/model_executor/models/kimi_vl.py` modified +195/-2 (197 lines); hunks: -56,7 +56,11; -79,6 +83,7; symbols: get_replacement, KimiVLForConditionalGeneration, __init__, get_encoder_cudagraph_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/moonvit.py
@@ -45,7 +45,9 @@
+from typing import Any
+import numpy as np
@@ -110,23 +112,42 @@ def __init__(
-    def forward(self, x: torch.Tensor, grid_hws: torch.Tensor) -> torch.Tensor:
-        pos_embs = []
-        for shape in grid_hws.tolist():
diff -- vllm/model_executor/models/kimi_vl.py
@@ -56,7 +56,11 @@
-from vllm.model_executor.models.interfaces import SupportsMultiModal, SupportsPP
+from vllm.model_executor.models.interfaces import (
+    SupportsEncoderCudaGraph,
+    SupportsMultiModal,
+    SupportsPP,
+)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/moonvit.py` modified +266/-37; `vllm/model_executor/models/kimi_vl.py` modified +195/-2
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation/test_vit_cudagraph.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44493 - [Bugfix]Fix Kimi-K2.5 FlashInfer ViT metadata

- 链接: https://github.com/vllm-project/vllm/pull/44493
- 状态/时间: merged / 2026-06-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `1bdc60ed53ad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+109/-28，可读 patch 260 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix]Fix Kimi-K2.5 FlashInfer ViT metadata」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Bugfix]Fix Kimi-K2.5 FlashInfer ViT metadata」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +108/-27 (135 lines); hunks: -154,9 +154,12 @@ def __init__(; -218,7 +221,9 @@ def __init__(; symbols: __init__, reset_parameters, forward，涉及 `__init__, reset_parameters, forward`；`vllm/model_executor/models/kimi_k25.py` modified +1/-1 (2 lines); hunks: -235,7 +235,7 @@ def _get_mm_fields_config(; symbols: _get_mm_fields_config, _call_hf_processor，涉及 `_get_mm_fields_config, _call_hf_processor`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +108/-27 (135 lines); hunks: -154,9 +154,12 @@ def __init__(; -218,7 +221,9 @@ def __init__(; symbols: __init__, reset_parameters, forward
  - `vllm/model_executor/models/kimi_k25.py` modified +1/-1 (2 lines); hunks: -235,7 +235,7 @@ def _get_mm_fields_config(; symbols: _get_mm_fields_config, _call_hf_processor
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -154,9 +154,12 @@ def __init__(
-    def forward(self, x: torch.Tensor, grid_thws: torch.Tensor) -> torch.Tensor:
+    def forward(
+        self, x: torch.Tensor, grid_thws: torch.Tensor | list[list[int]]
+    ) -> torch.Tensor:
-        for t, h, w in grid_thws.tolist():
+        grid_thw_list = grid_thws if isinstance(grid_thws, list) else grid_thws.tolist()
diff -- vllm/model_executor/models/kimi_k25.py
@@ -235,7 +235,7 @@ def _get_mm_fields_config(
-            grid_thws=MultiModalFieldConfig.batched("vision_chunk"),
+            grid_thws=MultiModalFieldConfig.batched("vision_chunk", keep_on_cpu=True),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +108/-27; `vllm/model_executor/models/kimi_k25.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42869 - [BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization

- 链接: https://github.com/vllm-project/vllm/pull/42869
- 状态/时间: merged / 2026-05-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `23c15acd770c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +6/-3 (9 lines); hunks: -339,9 +339,12 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +6/-3 (9 lines); hunks: -339,9 +339,12 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -339,9 +339,12 @@ def __init__(
-            self.vision_tower = self.vision_tower.to(
-                device=self.device, dtype=model_config.dtype
-            )
+            if self._maybe_ignore_quant_config(quant_config) is not None:
+                self.vision_tower = self.vision_tower.to(device=self.device)
+            else:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42081 - [Bug] Fix kimi dtype issue with `mm_projector_forward`

- 链接: https://github.com/vllm-project/vllm/pull/42081
- 状态/时间: merged / 2026-05-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `3f9c0c25b331`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-0，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] Fix kimi dtype issue with `mm_projector_forward`」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Bug] Fix kimi dtype issue with `mm_projector_forward`」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +3/-0 (3 lines); hunks: -618,6 +618,9 @@ def mm_projector_forward(mm_projector: torch.nn.Module, vt_o...; symbols: mm_projector_forward，涉及 `mm_projector_forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +3/-0 (3 lines); hunks: -618,6 +618,9 @@ def mm_projector_forward(mm_projector: torch.nn.Module, vt_o...; symbols: mm_projector_forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -618,6 +618,9 @@ def mm_projector_forward(mm_projector: torch.nn.Module, vt_output: list[torch.Te
+    projector_dtype = mm_projector.pre_norm.weight.dtype
+    if batched.dtype != projector_dtype:
+        batched = batched.to(projector_dtype)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41068 - [Bugfix] KimiK2ReasoningParser: guard against buffered end-token in streaming

- 链接: https://github.com/vllm-project/vllm/pull/41068
- 状态/时间: merged / 2026-05-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`；关联提交 `712ad0286c9a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+70/-0，可读 patch 102 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] KimiK2ReasoningParser: guard against buffered end-token in streaming」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] KimiK2ReasoningParser: guard against buffered end-token in streaming」；主要实现面是 `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +63/-0 (63 lines); hunks: -1,6 +1,8; -12,6 +14,20; symbols: mock_kimi_k2_tokenizer, kimi_k2_tokenizer, test_streaming_tool_section_ends_reasoning, test_streaming_end_token_id_buffered，涉及 `mock_kimi_k2_tokenizer, kimi_k2_tokenizer, test_streaming_tool_section_ends_reasoning`；`vllm/reasoning/kimi_k2_reasoning_parser.py` modified +7/-0 (7 lines); hunks: -221,6 +221,10 @@ def extract_reasoning_streaming(; -229,6 +233,9 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming，涉及 `extract_reasoning_streaming`。
- 代码 diff 细节:
  - `tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +63/-0 (63 lines); hunks: -1,6 +1,8; -12,6 +14,20; symbols: mock_kimi_k2_tokenizer, kimi_k2_tokenizer, test_streaming_tool_section_ends_reasoning, test_streaming_end_token_id_buffered
  - `vllm/reasoning/kimi_k2_reasoning_parser.py` modified +7/-0 (7 lines); hunks: -221,6 +221,10 @@ def extract_reasoning_streaming(; -229,6 +233,9 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_kimi_k2_reasoning_parser.py
@@ -1,6 +1,8 @@
+from unittest.mock import MagicMock
@@ -12,6 +14,20 @@
+@pytest.fixture
+def mock_kimi_k2_tokenizer():
+    tokenizer = MagicMock()
+    tokenizer.get_vocab.return_value = {
diff -- vllm/reasoning/kimi_k2_reasoning_parser.py
@@ -221,6 +221,10 @@ def extract_reasoning_streaming(
+            if self._end_token not in delta_text:
+                # Token ID arrived before text was flushed (stop-sequence buffering).
+                # Wait for the next delta when the text becomes visible.
+                return None
@@ -229,6 +233,9 @@ def extract_reasoning_streaming(
+            if self._tool_section_start_token not in delta_text:
```

- 已读文件:
  - tests: `tests/reasoning/test_kimi_k2_reasoning_parser.py` modified +63/-0
  - runtime: `vllm/reasoning/kimi_k2_reasoning_parser.py` modified +7/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_kimi_k2_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38579 - [Bugfix] Kimi-K2 tool parser streaming - fix token leakage, argument truncation, and content dropping

- 链接: https://github.com/vllm-project/vllm/pull/38579
- 状态/时间: merged / 2026-04-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`；关联提交 `03ce1c6ed908`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+684/-1405，可读 patch 2206 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Kimi-K2 tool parser streaming - fix token leakage, argument truncation, and content dropping」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Kimi-K2 tool parser streaming - fix token leakage, argument truncation, and content dropping」；主要实现面是 `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +525/-921 (1446 lines); hunks: -3,14 +3,20; -20,959 +26,557 @@ def kimi_k2_tokenizer():; symbols: kimi_k2_tokenizer, kimi_k2_tool_parser, parser, assert_tool_calls，涉及 `kimi_k2_tokenizer, kimi_k2_tool_parser, parser`；`vllm/tool_parsers/kimi_k2_tool_parser.py` modified +159/-484 (643 lines); hunks: -1,6 +1,5; -17,137 +16,59; symbols: KimiK2ToolParser, __init__, _check_and_strip_markers, _reset_section_state，涉及 `KimiK2ToolParser, __init__, _check_and_strip_markers`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +525/-921 (1446 lines); hunks: -3,14 +3,20; -20,959 +26,557 @@ def kimi_k2_tokenizer():; symbols: kimi_k2_tokenizer, kimi_k2_tool_parser, parser, assert_tool_calls
  - `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +159/-484 (643 lines); hunks: -1,6 +1,5; -17,137 +16,59; symbols: KimiK2ToolParser, __init__, _check_and_strip_markers, _reset_section_state
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_kimi_k2_tool_parser.py
@@ -3,14 +3,20 @@
+from unittest.mock import MagicMock
-from vllm.entrypoints.openai.engine.protocol import FunctionCall, ToolCall
+from tests.tool_parsers.utils import (
+    run_tool_extraction,
+    run_tool_extraction_streaming,
+)
diff -- vllm/tool_parsers/kimi_k2_tool_parser.py
@@ -1,6 +1,5 @@
-# code modified from deepseekv3_tool_parser.py
@@ -17,137 +16,59 @@
+from vllm.entrypoints.openai.responses.protocol import ResponsesRequest
+from vllm.tool_parsers.utils import partial_tag_overlap
-        self.current_tool_name_sent: bool = False
+        # Streaming state
```

- 已读文件:
  - tests: `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +525/-921
  - runtime: `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +159/-484
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_kimi_k2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39344 - fix(kimi_k25): resolve media_placeholder_token_id from tokenizer

- 链接: https://github.com/vllm-project/vllm/pull/39344
- 状态/时间: merged / 2026-04-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `17e787a7792b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+24/-3，可读 patch 41 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(kimi_k25): resolve media_placeholder_token_id from tokenizer」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「fix(kimi_k25): resolve media_placeholder_token_id from tokenizer」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +24/-3 (27 lines); hunks: -113,7 +113,29 @@ def __init__(self, ctx: InputProcessingContext) -> None:; -232,8 +254,7 @@ def _get_prompt_updates(; symbols: __init__, _get_prompt_updates, get_replacement，涉及 `__init__, _get_prompt_updates, get_replacement`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +24/-3 (27 lines); hunks: -113,7 +113,29 @@ def __init__(self, ctx: InputProcessingContext) -> None:; -232,8 +254,7 @@ def _get_prompt_updates(; symbols: __init__, _get_prompt_updates, get_replacement
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -113,7 +113,29 @@ def __init__(self, ctx: InputProcessingContext) -> None:
-        self.media_token_id = media_token_id = hf_config.media_placeholder_token_id
+        # Resolve token ID from the tokenizer because transformers v5
+        # may remap token IDs vs config.json.
+        config_token_id = hf_config.media_placeholder_token_id
+        resolved_token_id = tokenizer.convert_tokens_to_ids("<|media_pad|>")
+        is_valid_resolved = isinstance(resolved_token_id, int) and (
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +24/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37693 - [Model] Update Kimi-K25 and Isaac processors to fit HF-style

- 链接: https://github.com/vllm-project/vllm/pull/37693
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/processors/kimi_k25.py`；关联提交 `37aadf623786`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+128/-95，可读 patch 366 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Update Kimi-K25 and Isaac processors to fit HF-style」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/transformers_utils/processors/kimi_k25.py`, `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Model] Update Kimi-K25 and Isaac processors to fit HF-style」；主要实现面是 `vllm/transformers_utils/processors/kimi_k25.py`, `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/processors/kimi_k25.py` modified +54/-38 (92 lines); hunks: -1,38 +1,41; -42,31 +45,44 @@ def __call__(; symbols: KimiK25Processor, __init__, __call__，涉及 `KimiK25Processor, __init__, __call__`；`vllm/model_executor/models/kimi_k25.py` modified +16/-18 (34 lines); hunks: -104,19 +104,25 @@ class KimiK25ProcessingInfo(BaseProcessingInfo):; -132,20 +138,15 @@ def get_supported_mm_limits(self) -> Mapping[str, int | No...; symbols: KimiK25ProcessingInfo, __init__, get_hf_processor, get_supported_mm_limits，涉及 `KimiK25ProcessingInfo, __init__, get_hf_processor`。
- 代码 diff 细节:
  - `vllm/transformers_utils/processors/kimi_k25.py` modified +54/-38 (92 lines); hunks: -1,38 +1,41; -42,31 +45,44 @@ def __call__(; symbols: KimiK25Processor, __init__, __call__
  - `vllm/model_executor/models/kimi_k25.py` modified +16/-18 (34 lines); hunks: -104,19 +104,25 @@ class KimiK25ProcessingInfo(BaseProcessingInfo):; -132,20 +138,15 @@ def get_supported_mm_limits(self) -> Mapping[str, int | No...; symbols: KimiK25ProcessingInfo, __init__, get_hf_processor, get_supported_mm_limits
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/processors/kimi_k25.py
@@ -1,38 +1,41 @@
-import torch
-from transformers import BatchFeature
+from transformers import BaseImageProcessor, BatchFeature, TensorType
+from vllm.tokenizers.hf import HfTokenizer
-    attributes = ["tokenizer"]
-    tokenizer_class = "AutoTokenizer"
diff -- vllm/model_executor/models/kimi_k25.py
@@ -104,19 +104,25 @@ class KimiK25ProcessingInfo(BaseProcessingInfo):
-        self.hf_config = self.get_hf_config()
-        self.media_token_id = self.hf_config.media_placeholder_token_id
-        media_processor = cached_get_image_processor(
+        self.hf_config = hf_config = self.get_hf_config()
+        tokenizer = self.get_tokenizer()
+        image_processor = cached_get_image_processor(
```

- 已读文件:
  - runtime: `vllm/transformers_utils/processors/kimi_k25.py` modified +54/-38; `vllm/model_executor/models/kimi_k25.py` modified +16/-18
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/processors/isaac.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37438 - [Bugfix] Add Kimi-K2.5 reasoning/tool parser aliases and tool_call_id support

- 链接: https://github.com/vllm-project/vllm/pull/37438
- 状态/时间: merged / 2026-03-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_kimi_k2_reasoning_parser.py`；关联提交 `c63ca2b2e696`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+173/-18，可读 patch 227 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Add Kimi-K2.5 reasoning/tool parser aliases and tool_call_id support」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/reasoning/test_kimi_k2_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] Add Kimi-K2.5 reasoning/tool parser aliases and tool_call_id support」；主要实现面是 `tests/reasoning/test_kimi_k2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_kimi_k2_reasoning_parser.py` added +155/-0 (155 lines); hunks: -0,0 +1,155; symbols: kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled, test_extract_reasoning_with_think_tags，涉及 `kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled`。
- 代码 diff 细节:
  - `tests/reasoning/test_kimi_k2_reasoning_parser.py` added +155/-0 (155 lines); hunks: -0,0 +1,155; symbols: kimi_k2_tokenizer, test_parser_selection_thinking_enabled, test_parser_selection_thinking_disabled, test_extract_reasoning_with_think_tags
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_kimi_k2_reasoning_parser.py
@@ -0,0 +1,155 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest
+from vllm.entrypoints.openai.engine.protocol import DeltaMessage
+from vllm.reasoning.identity_reasoning_parser import IdentityReasoningParser
```

- 已读文件:
  - tests: `tests/reasoning/test_kimi_k2_reasoning_parser.py` added +155/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_kimi_k2_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36903 - [Misc] Clean up Kimi-audio whisper encoder loading

- 链接: https://github.com/vllm-project/vllm/pull/36903
- 状态/时间: merged / 2026-03-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_audio.py`；关联提交 `a8e8d62dd80f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+89/-116，可读 patch 382 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc] Clean up Kimi-audio whisper encoder loading」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_audio.py`；技术摘要: 覆盖「[Misc] Clean up Kimi-audio whisper encoder loading」；主要实现面是 `vllm/model_executor/models/kimi_audio.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_audio.py` modified +61/-111 (172 lines); hunks: -3,25 +3,21; -64,15 +60,6; symbols: _get_whisper_local_path, _get_feat_extract_output_lengths, KimiAudioWhisperEncoder, __init__，涉及 `_get_whisper_local_path, _get_feat_extract_output_lengths, KimiAudioWhisperEncoder`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_audio.py` modified +61/-111 (172 lines); hunks: -3,25 +3,21; -64,15 +60,6; symbols: _get_whisper_local_path, _get_feat_extract_output_lengths, KimiAudioWhisperEncoder, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_audio.py
@@ -3,25 +3,21 @@
-import os
-from huggingface_hub import snapshot_download
-from safetensors import safe_open
-from vllm.model_executor.model_loader.weight_utils import (
-    default_weight_loader,
-)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_audio.py` modified +61/-111
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/model_loader/default_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/kimi_audio.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #36361 - Kimi k2.5 MLA based eagle3

- 链接: https://github.com/vllm-project/vllm/pull/36361
- 状态/时间: merged / 2026-03-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `557389473755`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+499/-8，可读 patch 649 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Kimi k2.5 MLA based eagle3」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「Kimi k2.5 MLA based eagle3」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +14/-1 (15 lines); hunks: -28,6 +28,8; -311,7 +313,12 @@ def split_video_chunks(self, video):; symbols: split_video_chunks, KimiK25ForConditionalGeneration, compute_logits, set_aux_hidden_state_layers，涉及 `split_video_chunks, KimiK25ForConditionalGeneration, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +14/-1 (15 lines); hunks: -28,6 +28,8; -311,7 +313,12 @@ def split_video_chunks(self, video):; symbols: split_video_chunks, KimiK25ForConditionalGeneration, compute_logits, set_aux_hidden_state_layers
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -28,6 +28,8 @@
+    SupportsEagle,
+    SupportsEagle3,
@@ -311,7 +313,12 @@ def split_video_chunks(self, video):
-    nn.Module, SupportsMultiModal, SupportsPP, SupportsQuant
+    nn.Module,
+    SupportsMultiModal,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +14/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36127 - [Model] Add support for moonshotai/Kimi-Audio-7B-Instruct

- 链接: https://github.com/vllm-project/vllm/pull/36127
- 状态/时间: merged / 2026-03-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_audio.py`, `vllm/tokenizers/kimi_audio.py`, `vllm/transformers_utils/chat_templates/template_kimi_audio.jinja`, `vllm/transformers_utils/processors/kimi_audio.py`；关联提交 `42fadebecb79`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1446/-29，可读 patch 1583 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add support for moonshotai/Kimi-Audio-7B-Instruct」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/kimi_audio.py`, `vllm/tokenizers/kimi_audio.py`, `vllm/transformers_utils/processors/kimi_audio.py`；技术摘要: 覆盖「[Model] Add support for moonshotai/Kimi-Audio-7B-Instruct」；主要实现面是 `vllm/model_executor/models/kimi_audio.py`, `vllm/tokenizers/kimi_audio.py`, `vllm/transformers_utils/processors/kimi_audio.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_audio.py` added +725/-0 (725 lines); hunks: -0,0 +1,725; symbols: _get_feat_extract_output_lengths, KimiAudioWhisperEncoder, __init__, KimiAudioProcessingInfo，涉及 `_get_feat_extract_output_lengths, KimiAudioWhisperEncoder, __init__`；`vllm/tokenizers/kimi_audio.py` added +410/-0 (410 lines); hunks: -0,0 +1,410; symbols: _load_tiktoken_encoding, KimiAudioTokenizer, from_pretrained, __init__，涉及 `_load_tiktoken_encoding, KimiAudioTokenizer, from_pretrained`；`vllm/transformers_utils/processors/kimi_audio.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: _get_feat_extract_output_lengths, KimiAudioProcessor, __init__, check_argument_for_proper_class，涉及 `_get_feat_extract_output_lengths, KimiAudioProcessor, __init__`；`vllm/renderers/kimi_audio.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: KimiAudioRenderer, from_config，涉及 `KimiAudioRenderer, from_config`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_audio.py` added +725/-0 (725 lines); hunks: -0,0 +1,725; symbols: _get_feat_extract_output_lengths, KimiAudioWhisperEncoder, __init__, KimiAudioProcessingInfo
  - `vllm/tokenizers/kimi_audio.py` added +410/-0 (410 lines); hunks: -0,0 +1,410; symbols: _load_tiktoken_encoding, KimiAudioTokenizer, from_pretrained, __init__
  - `vllm/transformers_utils/processors/kimi_audio.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: _get_feat_extract_output_lengths, KimiAudioProcessor, __init__, check_argument_for_proper_class
  - `vllm/renderers/kimi_audio.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: KimiAudioRenderer, from_config
  - `vllm/transformers_utils/chat_templates/template_kimi_audio.jinja` added +13/-0 (13 lines); hunks: -0,0 +1,13
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_audio.py
@@ -0,0 +1,725 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Kimi-Audio model compatible with HuggingFace weights."""
+import os
+from collections.abc import Iterable, Mapping, Sequence
+from typing import Any, ClassVar, Literal
diff -- vllm/tokenizers/kimi_audio.py
@@ -0,0 +1,410 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Tokenizer for Kimi-Audio using TikToken."""
+import contextlib
+import json
+from pathlib import Path
diff -- vllm/transformers_utils/processors/kimi_audio.py
@@ -0,0 +1,163 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_audio.py` added +725/-0; `vllm/tokenizers/kimi_audio.py` added +410/-0; `vllm/transformers_utils/processors/kimi_audio.py` added +163/-0; `vllm/renderers/kimi_audio.py` added +49/-0; `vllm/transformers_utils/chat_templates/template_kimi_audio.jinja` added +13/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`, `tests/models/test_initialization.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36192 - [Security] Respect user trust_remote_code setting in NemotronVL and KimiK25

- 链接: https://github.com/vllm-project/vllm/pull/36192
- 状态/时间: merged / 2026-03-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `00bd08edeee5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-2，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Security] Respect user trust_remote_code setting in NemotronVL and KimiK25」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Security] Respect user trust_remote_code setting in NemotronVL and KimiK25」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +2/-1 (3 lines); hunks: -174,7 +174,8 @@ def __init__(self, ctx: InputProcessingContext) -> None:; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +2/-1 (3 lines); hunks: -174,7 +174,8 @@ def __init__(self, ctx: InputProcessingContext) -> None:; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -174,7 +174,8 @@ def __init__(self, ctx: InputProcessingContext) -> None:
-            self.ctx.model_config.model, trust_remote_code=True
+            self.ctx.model_config.model,
+            trust_remote_code=self.ctx.model_config.trust_remote_code,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/nemotron_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33646 - [Bugfix] Handle case when kimi ends reasoning with a tool call

- 链接: https://github.com/vllm-project/vllm/pull/33646
- 状态/时间: merged / 2026-02-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/reasoning/kimi_k2_reasoning_parser.py`；关联提交 `9251ed5c4fc6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+230/-2，可读 patch 240 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Handle case when kimi ends reasoning with a tool call」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/reasoning/kimi_k2_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] Handle case when kimi ends reasoning with a tool call」；主要实现面是 `vllm/reasoning/kimi_k2_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/kimi_k2_reasoning_parser.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: KimiK2ReasoningParser, __init__, _is_identity_mode, is_reasoning_end，涉及 `KimiK2ReasoningParser, __init__, _is_identity_mode`。
- 代码 diff 细节:
  - `vllm/reasoning/kimi_k2_reasoning_parser.py` added +228/-0 (228 lines); hunks: -0,0 +1,228; symbols: KimiK2ReasoningParser, __init__, _is_identity_mode, is_reasoning_end
- 关键代码摘录:

```diff
diff -- vllm/reasoning/kimi_k2_reasoning_parser.py
@@ -0,0 +1,228 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Sequence
+from transformers import PreTrainedTokenizerBase
+from vllm.entrypoints.openai.chat_completion.protocol import (
+    ChatCompletionRequest,
```

- 已读文件:
  - runtime: `vllm/reasoning/kimi_k2_reasoning_parser.py` added +228/-0
- 验证与风险: runtime 路径改动集中在 `vllm/reasoning/__init__.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34501 - [Bugfix] Add quant_config in ViT of Kimi-K2.5

- 链接: https://github.com/vllm-project/vllm/pull/34501
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `4a9952ec1b15`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-0，可读 patch 158 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Add quant_config in ViT of Kimi-K2.5」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Bugfix] Add quant_config in ViT of Kimi-K2.5」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` modified +15/-0 (15 lines); hunks: -28,6 +28,7; -304,6 +305,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/model_executor/models/kimi_k25.py` modified +11/-0 (11 lines); hunks: -23,6 +23,10; -361,6 +365,7 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config, _parse_and_validate_media_input，涉及 `__init__, _maybe_ignore_quant_config, _parse_and_validate_media_input`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +15/-0 (15 lines); hunks: -28,6 +28,7; -304,6 +305,7 @@ def __init__(; symbols: __init__
  - `vllm/model_executor/models/kimi_k25.py` modified +11/-0 (11 lines); hunks: -23,6 +23,10; -361,6 +365,7 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config, _parse_and_validate_media_input
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -28,6 +28,7 @@
+from vllm.model_executor.layers.quantization import QuantizationConfig
@@ -304,6 +305,7 @@ def __init__(
+        quant_config: QuantizationConfig | None = None,
@@ -314,13 +316,15 @@ def __init__(
+            quant_config=quant_config,
+            quant_config=quant_config,
diff -- vllm/model_executor/models/kimi_k25.py
@@ -23,6 +23,10 @@
+from vllm.model_executor.layers.quantization import QuantizationConfig
+from vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors import (
+    CompressedTensorsConfig,
+)
@@ -361,6 +365,7 @@ def __init__(
+                quant_config=self._maybe_ignore_quant_config(quant_config),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` modified +15/-0; `vllm/model_executor/models/kimi_k25.py` modified +11/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34427 - [Bugfix] Delete unused redundant code in Kimi-K2.5

- 链接: https://github.com/vllm-project/vllm/pull/34427
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `62788f99a4d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-5，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Delete unused redundant code in Kimi-K2.5」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Bugfix] Delete unused redundant code in Kimi-K2.5」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +0/-5 (5 lines); hunks: -11,7 +11,6; -378,10 +377,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +0/-5 (5 lines); hunks: -11,7 +11,6; -378,10 +377,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -11,7 +11,6 @@
-import copy
@@ -378,10 +377,6 @@ def __init__(
-        sub_vllm_config = copy.deepcopy(vllm_config)
-        sub_vllm_config.model_config.hf_config = (
-            sub_vllm_config.model_config.hf_config.text_config
-        )
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +0/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33876 - [Bugfix] Fix Kimi-K2.5 NVFP4 checkpoints weight loading

- 链接: https://github.com/vllm-project/vllm/pull/33876
- 状态/时间: merged / 2026-02-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `a2522839d87d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+15/-5，可读 patch 53 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Kimi-K2.5 NVFP4 checkpoints weight loading」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Bugfix] Fix Kimi-K2.5 NVFP4 checkpoints weight loading」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +14/-4 (18 lines); hunks: -24,7 +24,11; -302,7 +306,9 @@ def split_video_chunks(self, video):; symbols: split_video_chunks, KimiK25ForConditionalGeneration, compute_logits，涉及 `split_video_chunks, KimiK25ForConditionalGeneration, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +14/-4 (18 lines); hunks: -24,7 +24,11; -302,7 +306,9 @@ def split_video_chunks(self, video):; symbols: split_video_chunks, KimiK25ForConditionalGeneration, compute_logits
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -24,7 +24,11 @@
-from vllm.model_executor.models.interfaces import SupportsMultiModal, SupportsPP
+from vllm.model_executor.models.interfaces import (
+    SupportsMultiModal,
+    SupportsPP,
+    SupportsQuant,
+)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +14/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33562 - [Bugfix] Enable Kimi k25 processor test

- 链接: https://github.com/vllm-project/vllm/pull/33562
- 状态/时间: merged / 2026-02-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `4061dcf4c51a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+96/-12，可读 patch 221 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Enable Kimi k25 processor test」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Bugfix] Enable Kimi k25 processor test」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +27/-5 (32 lines); hunks: -96,16 +96,20 @@ class MoonshotKimiVAutoProcessor(ProcessorMixin):; -122,13 +126,30 @@ def __call__(; symbols: MoonshotKimiVAutoProcessor, __init__, __call__，涉及 `MoonshotKimiVAutoProcessor, __init__, __call__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +27/-5 (32 lines); hunks: -96,16 +96,20 @@ class MoonshotKimiVAutoProcessor(ProcessorMixin):; -122,13 +126,30 @@ def __call__(; symbols: MoonshotKimiVAutoProcessor, __init__, __call__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -96,16 +96,20 @@ class MoonshotKimiVAutoProcessor(ProcessorMixin):
-    def __init__(self, media_processor=None, tokenizer=None):
+    def __init__(
+        self, media_processor=None, tokenizer=None, media_token_id: int | None = None
+    ):
+        self.media_token_id = media_token_id
+        assert self.media_token_id is not None
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +27/-5
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_common.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33346 - [Models] Refactor Kimi-K2.5 weight loading

- 链接: https://github.com/vllm-project/vllm/pull/33346
- 状态/时间: merged / 2026-01-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；关联提交 `8bfc8d5600ed`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+40/-176，可读 patch 282 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Refactor Kimi-K2.5 weight loading」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；技术摘要: 覆盖「[Models] Refactor Kimi-K2.5 weight loading」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +38/-174 (212 lines); hunks: -23,16 +23,7; -64,7 +55,12; symbols: KimiK25ForConditionalGeneration, get_placeholder_str, __init__, _parse_and_validate_media_input，涉及 `KimiK25ForConditionalGeneration, get_placeholder_str, __init__`；`vllm/model_executor/models/kimi_k25_vit.py` modified +2/-2 (4 lines); hunks: -660,13 +660,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +38/-174 (212 lines); hunks: -23,16 +23,7; -64,7 +55,12; symbols: KimiK25ForConditionalGeneration, get_placeholder_str, __init__, _parse_and_validate_media_input
  - `vllm/model_executor/models/kimi_k25_vit.py` modified +2/-2 (4 lines); hunks: -660,13 +660,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -23,16 +23,7 @@
-from vllm.distributed import get_pp_group
-from vllm.model_executor.layers.fused_moe import SharedFusedMoE
-from vllm.model_executor.layers.logits_processor import LogitsProcessor
-from vllm.model_executor.layers.vocab_parallel_embedding import ParallelLMHead
-from vllm.model_executor.model_loader.weight_utils import (
-    default_weight_loader,
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -660,13 +660,13 @@ def __init__(
-            prefix=maybe_prefix(prefix, "linear_1"),
+            prefix=f"{prefix}.linear_1",
-            prefix=maybe_prefix(prefix, "linear_2"),
+            prefix=f"{prefix}.linear_2",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +38/-174; `vllm/model_executor/models/kimi_k25_vit.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33320 - [Backport] [Kimi-K2.5] Replace torch.cuda with current_platform for d…

- 链接: https://github.com/vllm-project/vllm/pull/33320
- 状态/时间: merged / 2026-01-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`；关联提交 `17b17c068453`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Backport] [Kimi-K2.5] Replace torch.cuda with current_platform for d…」；模型线: Kimi K2/K2.5/Linear/VL；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/kimi_k25.py`；技术摘要: 覆盖「[Backport] [Kimi-K2.5] Replace torch.cuda with current_platform for d…」；主要实现面是 `vllm/model_executor/models/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25.py` modified +2/-1 (3 lines); hunks: -58,6 +58,7; -320,7 +321,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25.py` modified +2/-1 (3 lines); hunks: -58,6 +58,7; -320,7 +321,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25.py
@@ -58,6 +58,7 @@
+from vllm.platforms import current_platform
@@ -320,7 +321,7 @@ def __init__(
-        self.device = torch.cuda.current_device()
+        self.device = current_platform.current_device()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_k25.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33131 - [Models] Kimi-K2.5

- 链接: https://github.com/vllm-project/vllm/pull/33131
- 状态/时间: merged / 2026-01-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/reasoning/kimi_k2_reasoning_parser.py`；关联提交 `b539f988e1ee`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 16 个文件，+1799/-8，可读 patch 2011 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Kimi-K2.5」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/configs/kimi_k25.py`；技术摘要: 覆盖「[Models] Kimi-K2.5」；主要实现面是 `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/configs/kimi_k25.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_k25_vit.py` added +678/-0 (678 lines); hunks: -0,0 +1,678; symbols: _apply_rope_input_validation, get_rope_shape_decorate, wrapper, get_rope_shape，涉及 `_apply_rope_input_validation, get_rope_shape_decorate, wrapper`；`vllm/model_executor/models/kimi_k25.py` added +581/-0 (581 lines); hunks: -0,0 +1,581; symbols: MaxImageTokenMeta, KimiK25MediaPixelInputs, MoonshotKimiVAutoProcessor, __init__，涉及 `MaxImageTokenMeta, KimiK25MediaPixelInputs, MoonshotKimiVAutoProcessor`；`vllm/transformers_utils/configs/kimi_k25.py` added +129/-0 (129 lines); hunks: -0,0 +1,129; symbols: KimiK25VisionConfig, __init__, KimiK25Config, hidden_size，涉及 `KimiK25VisionConfig, __init__, KimiK25Config`；`vllm/reasoning/kimi_k2_reasoning_parser.py` added +80/-0 (80 lines); hunks: -0,0 +1,80; symbols: KimiK2ReasoningParser, __init__, is_reasoning_end, is_reasoning_end_streaming，涉及 `KimiK2ReasoningParser, __init__, is_reasoning_end`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_k25_vit.py` added +678/-0 (678 lines); hunks: -0,0 +1,678; symbols: _apply_rope_input_validation, get_rope_shape_decorate, wrapper, get_rope_shape
  - `vllm/model_executor/models/kimi_k25.py` added +581/-0 (581 lines); hunks: -0,0 +1,581; symbols: MaxImageTokenMeta, KimiK25MediaPixelInputs, MoonshotKimiVAutoProcessor, __init__
  - `vllm/transformers_utils/configs/kimi_k25.py` added +129/-0 (129 lines); hunks: -0,0 +1,129; symbols: KimiK25VisionConfig, __init__, KimiK25Config, hidden_size
  - `vllm/reasoning/kimi_k2_reasoning_parser.py` added +80/-0 (80 lines); hunks: -0,0 +1,80; symbols: KimiK2ReasoningParser, __init__, is_reasoning_end, is_reasoning_end_streaming
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_k25_vit.py
@@ -0,0 +1,678 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""
+Vision tower implementation for Kimi-K2.5 model.
+This module provides the vision encoder components for Kimi-K2.5,
+including 3D patch embedding, RoPE position embedding, and
diff -- vllm/model_executor/models/kimi_k25.py
@@ -0,0 +1,581 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# ruff: noqa: E501
+"""
+Kimi-K2.5 Model Implementation for vLLM.
+Kimi-K2.5 extends Kimi-K2 with vision support
diff -- vllm/transformers_utils/configs/kimi_k25.py
@@ -0,0 +1,129 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_k25_vit.py` added +678/-0; `vllm/model_executor/models/kimi_k25.py` added +581/-0; `vllm/transformers_utils/configs/kimi_k25.py` added +129/-0; `vllm/reasoning/kimi_k2_reasoning_parser.py` added +80/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31738 - [Models]: Use `MMEncoderAttention` for MoonViT

- 链接: https://github.com/vllm-project/vllm/pull/31738
- 状态/时间: merged / 2026-01-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`；关联提交 `7101e0851f73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+72/-158，可读 patch 345 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models]: Use `MMEncoderAttention` for MoonViT」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「[Models]: Use `MMEncoderAttention` for MoonViT」；主要实现面是 `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/moonvit.py` modified +71/-157 (228 lines); hunks: -51,118 +51,20; -411,11 +313,19 @@ def __init__(; symbols: multihead_attention, sdpa_attention, _apply_rope_input_validation, __init__，涉及 `multihead_attention, sdpa_attention, _apply_rope_input_validation`；`vllm/model_executor/models/kimi_vl.py` modified +1/-1 (2 lines); hunks: -325,7 +325,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/moonvit.py` modified +71/-157 (228 lines); hunks: -51,118 +51,20; -411,11 +313,19 @@ def __init__(; symbols: multihead_attention, sdpa_attention, _apply_rope_input_validation, __init__
  - `vllm/model_executor/models/kimi_vl.py` modified +1/-1 (2 lines); hunks: -325,7 +325,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/moonvit.py
@@ -51,118 +51,20 @@
-from transformers.utils import is_flash_attn_2_available
+from vllm.attention.layers.mm_encoder_attention import MMEncoderAttention
+from vllm.config import MultiModalConfig
+from vllm.distributed import divide, get_tensor_model_parallel_world_size
-from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.layers.linear import (
diff -- vllm/model_executor/models/kimi_vl.py
@@ -325,7 +325,7 @@ def __init__(
-            self.use_data_parallel,
+            multimodal_config=model_config.multimodal_config,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/moonvit.py` modified +71/-157; `vllm/model_executor/models/kimi_vl.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31207 - fix: update kimi k2 tool parser logic

- 链接: https://github.com/vllm-project/vllm/pull/31207
- 状态/时间: merged / 2025-12-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`；关联提交 `358bfd315cad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+211/-202，可读 patch 511 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: update kimi k2 tool parser logic」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`；技术摘要: 覆盖「fix: update kimi k2 tool parser logic」；主要实现面是 `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +192/-191 (383 lines); hunks: -44,6 +44,33 @@ def assert_tool_calls(; -346,61 +373,32 @@ def test_token_leak_between_section_and_tool_begin(kimi_k2...; symbols: assert_tool_calls, run_streaming_sequence, test_extract_tool_calls_no_tools, test_token_leak_between_section_and_tool_begin，涉及 `assert_tool_calls, run_streaming_sequence, test_extract_tool_calls_no_tools`；`vllm/tool_parsers/kimi_k2_tool_parser.py` modified +19/-11 (30 lines); hunks: -122,7 +122,6 @@ def _check_and_strip_markers(self, text: str) -> tuple[str,...; -238,6 +237,7 @@ def extract_tool_calls_streaming(; symbols: _check_and_strip_markers, _reset_section_state, extract_tool_calls_streaming，涉及 `_check_and_strip_markers, _reset_section_state, extract_tool_calls_streaming`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +192/-191 (383 lines); hunks: -44,6 +44,33 @@ def assert_tool_calls(; -346,61 +373,32 @@ def test_token_leak_between_section_and_tool_begin(kimi_k2...; symbols: assert_tool_calls, run_streaming_sequence, test_extract_tool_calls_no_tools, test_token_leak_between_section_and_tool_begin
  - `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +19/-11 (30 lines); hunks: -122,7 +122,6 @@ def _check_and_strip_markers(self, text: str) -> tuple[str,...; -238,6 +237,7 @@ def extract_tool_calls_streaming(; symbols: _check_and_strip_markers, _reset_section_state, extract_tool_calls_streaming
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_kimi_k2_tool_parser.py
@@ -44,6 +44,33 @@ def assert_tool_calls(
+def run_streaming_sequence(parser, deltas):
+    """Helper to simulate a streaming sequence and return results."""
+    previous_text = ""
+    previous_token_ids: list[int] = []
+    results = []
+    for delta_text, delta_token_ids in deltas:
diff -- vllm/tool_parsers/kimi_k2_tool_parser.py
@@ -122,7 +122,6 @@ def _check_and_strip_markers(self, text: str) -> tuple[str, bool, bool]:
@@ -238,6 +237,7 @@ def extract_tool_calls_streaming(
@@ -252,13 +252,18 @@ def extract_tool_calls_streaming(
-                remaining = buffered_text
-                # Return remaining text as reasoning content if non-empty
-                if remaining.strip():
-                    return DeltaMessage(content=remaining)
```

- 已读文件:
  - tests: `tests/tool_parsers/test_kimi_k2_tool_parser.py` modified +192/-191
  - runtime: `vllm/tool_parsers/kimi_k2_tool_parser.py` modified +19/-11
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_kimi_k2_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29309 - [XPU]fix Kimi-VL-A3B-thinking on xpu

- 链接: https://github.com/vllm-project/vllm/pull/29309
- 状态/时间: merged / 2025-11-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/moonvit.py`；关联提交 `3cfa63ad9916`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+14/-6，可读 patch 52 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU]fix Kimi-VL-A3B-thinking on xpu」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/moonvit.py`；技术摘要: 覆盖「[XPU]fix Kimi-VL-A3B-thinking on xpu」；主要实现面是 `vllm/model_executor/models/moonvit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/moonvit.py` modified +14/-6 (20 lines); hunks: -56,10 +56,13; -106,10 +109,10 @@ def multihead_attention(; symbols: multihead_attention, Rope2DPosEmb, __init__，涉及 `multihead_attention, Rope2DPosEmb, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/moonvit.py` modified +14/-6 (20 lines); hunks: -56,10 +56,13; -106,10 +109,10 @@ def multihead_attention(; symbols: multihead_attention, Rope2DPosEmb, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/moonvit.py
@@ -56,10 +56,13 @@
+from vllm.platforms import current_platform
+elif current_platform.is_xpu():
+    from vllm.attention.utils.fa_utils import flash_attn_varlen_func
@@ -106,10 +109,10 @@ def multihead_attention(
-        q_cu_seqlens,
-        k_cu_seqlens,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/moonvit.py` modified +14/-6
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/moonvit.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27809 - [Model] Introduce Kimi Linear to vLLM

- 链接: https://github.com/vllm-project/vllm/pull/27809
- 状态/时间: merged / 2025-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/configs/kimi_linear.py`；关联提交 `4e68cc9b6aa2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1326/-49，可读 patch 1510 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Introduce Kimi Linear to vLLM」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/kimi_linear.py`, `vllm/transformers_utils/configs/kimi_linear.py`；技术摘要: 覆盖「[Model] Introduce Kimi Linear to vLLM」；主要实现面是 `vllm/model_executor/models/kimi_linear.py`, `vllm/transformers_utils/configs/kimi_linear.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_linear.py` added +663/-0 (663 lines); hunks: -0,0 +1,663; symbols: KimiMLP, __init__, forward, KimiMoE，涉及 `KimiMLP, __init__, forward`；`vllm/transformers_utils/configs/kimi_linear.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: KimiLinearConfig, __init__, is_mla, is_moe，涉及 `KimiLinearConfig, __init__, is_mla`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_linear.py` added +663/-0 (663 lines); hunks: -0,0 +1,663; symbols: KimiMLP, __init__, forward, KimiMoE
  - `vllm/transformers_utils/configs/kimi_linear.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: KimiLinearConfig, __init__, is_mla, is_moe
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_linear.py
@@ -0,0 +1,663 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+from typing import Any
+import torch
+from torch import nn
diff -- vllm/transformers_utils/configs/kimi_linear.py
@@ -0,0 +1,144 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from transformers.configuration_utils import PretrainedConfig
+from vllm.logger import init_logger
+logger = init_logger(__name__)
+class KimiLinearConfig(PretrainedConfig):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_linear.py` added +663/-0; `vllm/transformers_utils/configs/kimi_linear.py` added +144/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23817 - [Model] Support DP for ViT on Kimi-VL-A3B-Thinking-2506

- 链接: https://github.com/vllm-project/vllm/pull/23817
- 状态/时间: merged / 2025-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`；关联提交 `a0e0efd6bdcf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+157/-62，可读 patch 478 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support DP for ViT on Kimi-VL-A3B-Thinking-2506」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「[Model] Support DP for ViT on Kimi-VL-A3B-Thinking-2506」；主要实现面是 `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/moonvit.py` modified +55/-22 (77 lines); hunks: -42,7 +42,6; -55,6 +54,8; symbols: MLP2, __init__, forward, MoonVitEncoderLayer，涉及 `MLP2, __init__, forward`；`vllm/model_executor/models/kimi_vl.py` modified +39/-15 (54 lines); hunks: -56,6 +56,7; -76,6 +77,7; symbols: MaxImageTokenMeta, KimiVLMultiModalProjector, __init__, forward，涉及 `MaxImageTokenMeta, KimiVLMultiModalProjector, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/moonvit.py` modified +55/-22 (77 lines); hunks: -42,7 +42,6; -55,6 +54,8; symbols: MLP2, __init__, forward, MoonVitEncoderLayer
  - `vllm/model_executor/models/kimi_vl.py` modified +39/-15 (54 lines); hunks: -56,6 +56,7; -76,6 +77,7; symbols: MaxImageTokenMeta, KimiVLMultiModalProjector, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/moonvit.py
@@ -42,7 +42,6 @@
-import math
@@ -55,6 +54,8 @@
+from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.models.utils import maybe_prefix
@@ -383,21 +384,30 @@ class MLP2(nn.Module):
-    def __init__(self, dims: list[int], activation, bias=True):
diff -- vllm/model_executor/models/kimi_vl.py
@@ -56,6 +56,7 @@
+from vllm.model_executor.layers.linear import ReplicatedLinear
@@ -76,6 +77,7 @@
+from vllm.multimodal.utils import run_dp_sharded_mrope_vision_model
@@ -93,29 +95,35 @@ class MaxImageTokenMeta:
-    def __init__(self, config: KimiVLConfig):
+    def __init__(self, config: KimiVLConfig, \
```

- 已读文件:
  - runtime: `vllm/model_executor/models/moonvit.py` modified +55/-22; `vllm/model_executor/models/kimi_vl.py` modified +39/-15
- 验证与风险: diff 自带测试面 `tests/multimodal/test_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23114 - [Model] Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506

- 链接: https://github.com/vllm-project/vllm/pull/23114
- 状态/时间: merged / 2025-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`；关联提交 `fda9537c5e61`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+18/-13，可读 patch 77 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「[Model] Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506」；主要实现面是 `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_vl.py` modified +17/-12 (29 lines); hunks: -54,16 +54,16; -81,7 +81,7; symbols: get_replacement, KimiVLForConditionalGeneration, get_placeholder_str, __init__，涉及 `get_replacement, KimiVLForConditionalGeneration, get_placeholder_str`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_vl.py` modified +17/-12 (29 lines); hunks: -54,16 +54,16; -81,7 +81,7; symbols: get_replacement, KimiVLForConditionalGeneration, get_placeholder_str, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_vl.py
@@ -54,16 +54,16 @@
-from vllm.distributed import (get_tensor_model_parallel_rank,
-                              get_tensor_model_parallel_world_size)
+from vllm.distributed import get_pp_group
-from vllm.model_executor.models.interfaces import SupportsMultiModal
+from vllm.model_executor.models.interfaces import (SupportsMultiModal,
+                                                   SupportsPP)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_vl.py` modified +17/-12
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21769 - Migrate KimiVLImagePixelInputs to TensorSchema

- 链接: https://github.com/vllm-project/vllm/pull/21769
- 状态/时间: merged / 2025-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`；关联提交 `05fae021750b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+15/-9，可读 patch 55 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Migrate KimiVLImagePixelInputs to TensorSchema」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「Migrate KimiVLImagePixelInputs to TensorSchema」；主要实现面是 `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_vl.py` modified +15/-9 (24 lines); hunks: -46,7 +46,7; -79,6 +79,7; symbols: forward, KimiVLImagePixelInputs, _parse_and_validate_image_input，涉及 `forward, KimiVLImagePixelInputs, _parse_and_validate_image_input`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_vl.py` modified +15/-9 (24 lines); hunks: -46,7 +46,7; -79,6 +79,7; symbols: forward, KimiVLImagePixelInputs, _parse_and_validate_image_input
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_vl.py
@@ -46,7 +46,7 @@
-from typing import Any, Literal, Optional, TypedDict, Union
+from typing import Annotated, Any, Literal, Optional, Union
@@ -79,6 +79,7 @@
+from vllm.utils.tensor_schema import TensorSchema, TensorShape
@@ -118,15 +119,22 @@ def forward(self, image_features: torch.Tensor) -> torch.Tensor:
-class KimiVLImagePixelInputs(TypedDict):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_vl.py` modified +15/-9
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17156 - fix float16 support for kimi-vl

- 链接: https://github.com/vllm-project/vllm/pull/17156
- 状态/时间: merged / 2025-04-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`；关联提交 `69bff9bc8934`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix float16 support for kimi-vl」；模型线: Kimi K2/K2.5/Linear/VL；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「fix float16 support for kimi-vl」；主要实现面是 `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_vl.py` modified +1/-2 (3 lines); hunks: -340,8 +340,7 @@ def _parse_and_validate_image_input(; symbols: _parse_and_validate_image_input，涉及 `_parse_and_validate_image_input`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_vl.py` modified +1/-2 (3 lines); hunks: -340,8 +340,7 @@ def _parse_and_validate_image_input(; symbols: _parse_and_validate_image_input
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_vl.py
@@ -340,8 +340,7 @@ def _parse_and_validate_image_input(
-        # fp32 -> bf16
-        pixel_values = pixel_values.to(torch.bfloat16)
+        pixel_values = pixel_values.to(self.vision_tower.dtype)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_vl.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16833 - [Misc] Clean up Kimi-VL

- 链接: https://github.com/vllm-project/vllm/pull/16833
- 状态/时间: merged / 2025-04-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`；关联提交 `aadb6565628c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-44，可读 patch 139 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc] Clean up Kimi-VL」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/kimi_vl.py`；技术摘要: 覆盖「[Misc] Clean up Kimi-VL」；主要实现面是 `vllm/model_executor/models/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/kimi_vl.py` modified +17/-40 (57 lines); hunks: -56,7 +56,6; -70,22 +69,20; symbols: KimiVLProcessingInfo, get_hf_config, get_supported_mm_limits, get_num_image_tokens，涉及 `KimiVLProcessingInfo, get_hf_config, get_supported_mm_limits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/kimi_vl.py` modified +17/-40 (57 lines); hunks: -56,7 +56,6; -70,22 +69,20; symbols: KimiVLProcessingInfo, get_hf_config, get_supported_mm_limits, get_num_image_tokens
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/kimi_vl.py
@@ -56,7 +56,6 @@
-from vllm.logger import init_logger
@@ -70,22 +69,20 @@
-from vllm.multimodal.inputs import (MultiModalFieldConfig, MultiModalKwargs,
-                                    NestedTensors)
+from vllm.multimodal.inputs import (MultiModalDataDict, MultiModalFieldConfig,
+                                    MultiModalKwargs, NestedTensors)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/kimi_vl.py` modified +17/-40
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/kimi_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16387 - [Model][VLM] Add Kimi-VL model support

- 链接: https://github.com/vllm-project/vllm/pull/16387
- 状态/时间: merged / 2025-04-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`, `vllm/transformers_utils/configs/kimi_vl.py`, `vllm/transformers_utils/configs/moonvit.py`；关联提交 `b1308b84a3a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+1436/-14，可读 patch 1618 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][VLM] Add Kimi-VL model support」；模型线: Kimi K2/K2.5/Linear/VL；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/transformers_utils/configs/kimi_vl.py`；技术摘要: 覆盖「[Model][VLM] Add Kimi-VL model support」；主要实现面是 `vllm/model_executor/models/moonvit.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/transformers_utils/configs/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/moonvit.py` added +628/-0 (628 lines); hunks: -0,0 +1,628; symbols: multihead_attention, sdpa_attention, _apply_rope_input_validation, apply_rope，涉及 `multihead_attention, sdpa_attention, _apply_rope_input_validation`；`vllm/model_executor/models/kimi_vl.py` added +608/-0 (608 lines); hunks: -0,0 +1,608; symbols: MaxImageTokenMeta, KimiVLMultiModalProjector, __init__, forward，涉及 `MaxImageTokenMeta, KimiVLMultiModalProjector, __init__`；`vllm/transformers_utils/configs/kimi_vl.py` added +36/-0 (36 lines); hunks: -0,0 +1,36; symbols: KimiVLConfig, __init__，涉及 `KimiVLConfig, __init__`；`vllm/transformers_utils/configs/moonvit.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: MoonViTConfig, __init__，涉及 `MoonViTConfig, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/moonvit.py` added +628/-0 (628 lines); hunks: -0,0 +1,628; symbols: multihead_attention, sdpa_attention, _apply_rope_input_validation, apply_rope
  - `vllm/model_executor/models/kimi_vl.py` added +608/-0 (608 lines); hunks: -0,0 +1,608; symbols: MaxImageTokenMeta, KimiVLMultiModalProjector, __init__, forward
  - `vllm/transformers_utils/configs/kimi_vl.py` added +36/-0 (36 lines); hunks: -0,0 +1,36; symbols: KimiVLConfig, __init__
  - `vllm/transformers_utils/configs/moonvit.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: MoonViTConfig, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/moonvit.py
@@ -0,0 +1,628 @@
+# SPDX-License-Identifier: Apache-2.0
+# ruff: noqa: E501
+# Adapted from https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct/blob/main/modeling_kimi_vl.py
+# This file is meant to be used in kimi_vl.py only
+# Copyright 2025 The Moonshot AI Team, DeepSeek-AI, and HuggingFace Inc. team. All rights reserved.
+#
diff -- vllm/model_executor/models/kimi_vl.py
@@ -0,0 +1,608 @@
+# SPDX-License-Identifier: Apache-2.0
+# ruff: noqa: E501
+# Adapted from https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct/blob/main/modeling_kimi_vl.py
+# Copyright 2025 The Moonshot AI Team, DeepSeek-AI, and HuggingFace Inc. team. All rights reserved.
+#
+# The code is based on llava (llava/modeling_llava.py) and DeepSeek-V3 (DeepSeek-V3/modeling_deepseek.py), but modified for KimiVL.
diff -- vllm/transformers_utils/configs/kimi_vl.py
@@ -0,0 +1,36 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/models/moonvit.py` added +628/-0; `vllm/model_executor/models/kimi_vl.py` added +608/-0; `vllm/transformers_utils/configs/kimi_vl.py` added +36/-0; `vllm/transformers_utils/configs/moonvit.py` added +32/-0
- 验证与风险: diff 自带测试面 `tests/models/decoder_only/vision_language/test_models.py`, `tests/models/decoder_only/vision_language/vlm_utils/model_utils.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
