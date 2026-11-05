# sglang unclassified Local Commit Optimization History

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## Local-only branch update from hg-full-base to main

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 246 (merges: 215)
- Branch segments: `hg-full-base..main`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `test/registered/unit/server_args/test_server_args.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `16d7caa10`, `50bacb028`, ... (19 total) |
| `test/registered/unit/managers/test_prefill_adder.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `50bacb028`, `ee0f2375e`, ... (17 total) |
| `python/sglang/srt/environ.py` | `2d561a3ec`, `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, ... (16 total) |
| `python/sglang/srt/models/deepseek_v4.py` | `2d561a3ec`, `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, ... (16 total) |
| `test/registered/unit/function_call/test_function_call_parser.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `16d7caa10`, `50bacb028`, ... (16 total) |
| `test/registered/unit/mem_cache/test_radix_cache_unit.py` | `90205d601`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `b7bd14f19`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, ... (16 total) |
| `python/sglang/srt/layers/moe/topk.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (15 total) |
| `python/sglang/srt/mem_cache/memory_pool.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (15 total) |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (15 total) |
| `python/sglang/srt/models/deepseek_v2.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (15 total) |
| `python/sglang/srt/utils/common.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (15 total) |
| `test/registered/unit/mem_cache/test_swa_unittest.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `b7bd14f19`, `16d7caa10`, `50bacb028`, `ee0f2375e`, ... (15 total) |
| `test/registered/unit/parser/test_reasoning_parser.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `50bacb028`, `ee0f2375e`, ... (15 total) |
| `test/run_suite.py` | `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, ... (15 total) |
| `python/sglang/srt/disaggregation/decode.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/disaggregation/prefill.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/distributed/parallel_state.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/layers/layernorm.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/layers/moe/mega_moe.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/managers/schedule_batch.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/managers/scheduler.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/model_executor/model_runner.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (14 total) |
| `python/sglang/srt/server_args.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, ... (14 total) |
| `test/registered/unit/model_loader/test_modelopt_loader.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `ba31df0c0`, `b7bd14f19`, `16d7caa10`, `ee0f2375e`, ... (14 total) |
| `python/sglang/srt/arg_groups/overrides.py` | `b781224d4`, `ba31df0c0`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/configs/model_config.py` | `aa2309e22`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (13 total) |
| `python/sglang/srt/layers/attention/attention_registry.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (13 total) |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/layers/dp_attention.py` | `2d561a3ec`, `b781224d4`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `aa2309e22`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/model_executor/pool_configurator.py` | `2d561a3ec`, `b781224d4`, `ba31df0c0`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, ... (13 total) |
| `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` | `ba31df0c0`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, ... (13 total) |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `2d561a3ec`, `b97d7df6e`, `16d7caa10`, `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, ... (13 total) |
| `test/registered/attention/test_triton_attention_kernels.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `b7bd14f19`, `50bacb028`, `ee0f2375e`, `4975d6490`, ... (13 total) |
| `test/registered/radix_cache/test_radix_attention.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `b7bd14f19`, `16d7caa10`, `50bacb028`, `ee0f2375e`, ... (13 total) |
| `test/registered/scheduler/test_retract_decode.py` | `90205d601`, `cc279bcf6`, `4d9dc6618`, `2d561a3ec`, `f38f1a5d2`, `bb9bb4b2d`, `c43b06722`, `b781224d4`, `b7bd14f19`, `ee0f2375e`, `ab43824b0`, `36b93840b`, ... (13 total) |
| ... | 10837 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-04-27 | `547981c68` | `hg-full-base..main` | 缺陷修复 | fix for load model |  |
| 2026-05-21 | `e797eb690` | `hg-full-base..main` | 缺陷修复 | fix bug |  |
| 2026-05-29 | `90205d601` | `hg-full-base..main` | 性能/后端优化 | test: sync validated DCU registered cases | `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` and 202 files in total |
| 2026-06-03 | `45b95c0ad` | `hg-full-base..main` | 通用实现调整 | Merge branch 'v0.5.12_dev_liucong' of https://developer.sourcefind.cn/codes/OpenDAS/sglang into v0.5.12_dev_liucong | no direct file change / merge |
| 2026-06-03 | `fb3900b24` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #5 from HYGON-AI/zyh-test-ci | no direct file change / merge |
| 2026-06-03 | `40802b348` | `hg-full-base..main` | 通用实现调整 | Merge remote-tracking branch 'v0.5.12_dev_liucong/v0.5.12_dev' into v0.5.12_dev | no direct file change / merge |
| 2026-06-03 | `4f14e4618` | `hg-full-base..main` | 通用实现调整 | Merge pull request #6 from HYGON-AI/v0.5.12_dev_liucong | no direct file change / merge |
| 2026-06-04 | `947a5554f` | `hg-full-base..main` | 缺陷修复 | Merge pull request #7 from HYGON-AI/v0.5.12_dev_swa_fix | no direct file change / merge |
| 2026-06-04 | `e7b91b4cc` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #8 from HYGON-AI/zyh-test-ci | no direct file change / merge |
| 2026-06-04 | `6a5a6f5e9` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'v0.5.12_dev' into v0.5.12_dev_moe_runer | no direct file change / merge |
| 2026-06-04 | `33468b69a` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #9 from HYGON-AI/v0.5.12_dev_moe_runer | no direct file change / merge |
| 2026-06-05 | `cc279bcf6` | `hg-full-base..main` | 性能/后端优化 | ci: rename DCU BW1000 tests to BW1100 | `.github/workflows/pr-test-dcu.yml`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` and 165 files in total |
| 2026-06-09 | `ab857fb79` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #10 from HYGON-AI/docs/license-apache-dcu | no direct file change / merge |
| 2026-06-11 | `11c0badb2` | `hg-full-base..main` | 测试/文档/基准 | Merge dcu-ci-pr into v0.5.12_dev for DCU CI | no direct file change / merge |
| 2026-06-11 | `4d9dc6618` | `hg-full-base..main` | 性能/后端优化 | ci: reduce DCU CI mainline intrusion | `.github/workflows/pr-gate.yml`, `.github/workflows/release-whl-dcu.yml`, `python/sglang/__init__.py` and 151 files in total |
| 2026-06-11 | `bea273016` | `hg-full-base..main` | 通用实现调整 | Merge branch 'v0.5.12_dev' into v0.5.12_dev_dpsk_v4 | no direct file change / merge |
| 2026-06-11 | `890a55077` | `hg-full-base..main` | 通用实现调整 | Merge pull request #12 from HYGON-AI/v0.5.12_dev_dpsk_v4 | no direct file change / merge |
| 2026-06-12 | `04faad946` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #13 from HYGON-AI/0611-dcu-ci-merge | no direct file change / merge |
| 2026-06-13 | `2ccdb54c5` | `hg-full-base..main` | 性能/后端优化 | [feat]增加sglang性能分析skill，注意当前还处于试用阶段 | `.claude/skills/sglang-profile-analyse/SKILL.md` |
| 2026-06-14 | `ae315e505` | `hg-full-base..main` | 模型支持/运行时入口 | Merge pull request #22 from HYGON-AI/add-quality-gate | no direct file change / merge |
| 2026-06-15 | `e98c3e175` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #15 from HYGON-AI/v0.5.12_dev_moe_runer | no direct file change / merge |
| 2026-06-15 | `26fa81060` | `hg-full-base..main` | 通用实现调整 | Merge pull request #25 from HYGON-AI/v0.5.12_dev_unified_attn | no direct file change / merge |
| 2026-06-15 | `b0855ae72` | `hg-full-base..main` | 测试/文档/基准 | Merge remote-tracking branch 'origin/v0.5.12_dev' into zyh-test-lint | no direct file change / merge |
| 2026-06-15 | `3e0abe65f` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #16 from HYGON-AI/zyh-test-lint | no direct file change / merge |
| 2026-06-16 | `24aaafde8` | `hg-full-base..main` | 通用实现调整 | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_chenyue | no direct file change / merge |
| 2026-06-16 | `6ba33abbc` | `hg-full-base..main` | 通用实现调整 | Merge pull request #17 from HYGON-AI/v0.5.12_dev_chenyue | no direct file change / merge |
| 2026-06-16 | `42588bb8c` | `hg-full-base..main` | 通用实现调整 | Merge pull request #30 from HYGON-AI/v0.5.12_dev_lph | no direct file change / merge |
| 2026-06-17 | `5cf4efb7e` | `hg-full-base..main` | 通用实现调整 | Merge pull request #28 from HYGON-AI/v0.5.12_dev_maxiao | no direct file change / merge |
| 2026-06-17 | `07e426bf5` | `hg-full-base..main` | 缺陷修复 | Merge pull request #29 from HYGON-AI/v0.5.12_dev_swa_pool_fix | no direct file change / merge |
| 2026-06-17 | `e0bb491ba` | `hg-full-base..main` | 性能/后端优化 | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_moe_runer | no direct file change / merge |
| 2026-06-17 | `e1352aca0` | `hg-full-base..main` | 性能/后端优化 | Merge remote-tracking branch 'origin/v0.5.12_dev' into v0.5.12_dev_moe_runer | no direct file change / merge |
| 2026-06-18 | `965fc8196` | `hg-full-base..main` | 模型支持/运行时入口 | Merge pull request #33 from HYGON-AI/add-quality-gate | no direct file change / merge |
| 2026-06-18 | `cb53b9685` | `hg-full-base..main` | 通用实现调整 | Merge pull request #35 from HYGON-AI/v0.5.12_dev_rye_vllm-allreduce-deprecate | no direct file change / merge |
| 2026-06-18 | `e0da81b8a` | `hg-full-base..main` | 模型支持/运行时入口 | Merge pull request #37 from HYGON-AI/add-quality-gate | no direct file change / merge |
| 2026-06-23 | `dc4e95ea9` | `hg-full-base..main` | 通用实现调整 | Merge pull request #38 from HYGON-AI/v0.5.12_dev_maxiao | no direct file change / merge |
| 2026-06-23 | `9f41a0a0a` | `hg-full-base..main` | 缺陷修复 | Merge pull request #39 from HYGON-AI/fix/dpsk-r1-fp8-startup | no direct file change / merge |
| 2026-06-23 | `0fc998757` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C01 | no direct file change / merge |
| 2026-06-23 | `ac9332fc1` | `hg-full-base..main` | 缺陷修复 | Merge pull request #41 from HYGON-AI/v0.5.12_dev_swa_mem_pool_fix | no direct file change / merge |
| 2026-06-23 | `a643b4108` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #42 from HYGON-AI/0623-dcu-ci-merge-clean | no direct file change / merge |
| 2026-06-23 | `571813832` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C02 | no direct file change / merge |
| 2026-06-24 | `2a6333012` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #44 from HYGON-AI/temp-pr-test | no direct file change / merge |
| 2026-06-24 | `8303d60f7` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C03 | no direct file change / merge |
| 2026-06-25 | `4a6b5a816` | `hg-full-base..main` | 模型支持/运行时入口 | Merge pull request #49 from HYGON-AI/feature/manual-dcu-unattended-model-test | no direct file change / merge |
| 2026-06-29 | `86d6fd542` | `hg-full-base..main` | 缺陷修复 | Merge pull request #50 from HYGON-AI/fix/dcu-runtime-log-sanitize | no direct file change / merge |
| 2026-06-29 | `5f2985983` | `hg-full-base..main` | 通用实现调整 | Merge pull request #48 from HYGON-AI/v0.5.12_dev_maxiao | no direct file change / merge |
| 2026-06-29 | `347434c31` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #51 from HYGON-AI/temp-pr-test | no direct file change / merge |
| 2026-06-29 | `1a8266b2c` | `hg-full-base..main` | 测试/文档/基准 | Merge remote-tracking branch 'origin/test-pr-trigger-dcu-0625' into HEAD | no direct file change / merge |
| 2026-06-30 | `810624fbe` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C04 | no direct file change / merge |
| 2026-06-30 | `91b1aa386` | `hg-full-base..main` | 调度/缓存/PD | Merge pull request #53 from HYGON-AI/v0.5.12_dev_hy3_pd | no direct file change / merge |
| 2026-06-30 | `08c1fd5a0` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C05 | no direct file change / merge |
| 2026-07-01 | `7ced3e2c7` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'v0.5.12_dev' into v0.5.12_dev_rye_megamoe | no direct file change / merge |
| 2026-07-01 | `5eebbee0f` | `hg-full-base..main` | 缺陷修复 | Merge pull request #57 from HYGON-AI/lzb/fst-multinode-device-fix | no direct file change / merge |
| 2026-07-01 | `16cff03a2` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C06 | no direct file change / merge |
| 2026-07-02 | `66ed7efb4` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #55 from HYGON-AI/v0.5.12_dev_rye_megamoe | no direct file change / merge |
| 2026-07-02 | `4d23b7e41` | `hg-full-base..main` | 通用实现调整 | Merge pull request #56 from HYGON-AI/v0.5.12_dev_liucong | no direct file change / merge |
| 2026-07-02 | `07dbcb715` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #54 from HYGON-AI/aiter_asm_shuffle | no direct file change / merge |
| 2026-07-02 | `4763e7a9b` | `hg-full-base..main` | 调度/缓存/PD | Merge pull request #58 from HYGON-AI/lzb/fst-empty-cache-reclaim | no direct file change / merge |
| 2026-07-02 | `1fa5343d1` | `hg-full-base..main` | 通用实现调整 | Merge remote-tracking branch 'origin/v0.5.12_dev' into codex/pr59-review | no direct file change / merge |
| 2026-07-02 | `593df5e14` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C07 | no direct file change / merge |
| 2026-07-02 | `abc5b4e0e` | `hg-full-base..main` | 通用实现调整 | Merge pull request #59 from HYGON-AI/sgl0512_wanghl_dev | no direct file change / merge |
| 2026-07-03 | `ec812cf6e` | `hg-full-base..main` | 通用实现调整 | Merge pull request #60 from HYGON-AI/v0.5.12_dev_ep_w4a16 | no direct file change / merge |
| 2026-07-03 | `01f8caf22` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C08 | no direct file change / merge |
| 2026-07-03 | `59689b572` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #63 from HYGON-AI/v0.5.12_dev_w4a16_deepgemm | no direct file change / merge |
| 2026-07-05 | `2d561a3ec` | `hg-full-base..main` | 性能/后端优化 | chore: add modification notices for DCU changes | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py` and 254 files in total |
| 2026-07-06 | `2ada58179` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C09 | no direct file change / merge |
| 2026-07-06 | `7401b75cf` | `hg-full-base..main` | 通用实现调整 | Merge pull request #65 from HYGON-AI/v0.5.12_dev_ywl | no direct file change / merge |
| 2026-07-06 | `9eb6129e4` | `hg-full-base..main` | 通用实现调整 | Merge pull request #62 from HYGON-AI/v0.5.12_dev_attnbackend | no direct file change / merge |
| 2026-07-06 | `dd96c4cb8` | `hg-full-base..main` | 通用实现调整 | Merge pull request #66 from HYGON-AI/v0.5.12_dev_ywl | no direct file change / merge |
| 2026-07-07 | `5f232f552` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoint C10 | no direct file change / merge |
| 2026-07-07 | `2285ae0a6` | `hg-full-base..main` | 调度/缓存/PD | Merge pull request #68 from HYGON-AI/v0.5.12_dev_hy3_pd_disaggregation | no direct file change / merge |
| 2026-07-07 | `e9c2e28b5` | `hg-full-base..main` | 缺陷修复 | Merge branch 'v0.5.12_dev' into fix/dcu-runtime-log-sanitize | no direct file change / merge |
| 2026-07-07 | `2d48f0170` | `hg-full-base..main` | 缺陷修复 | Merge pull request #69 from HYGON-AI/fix/dcu-runtime-log-sanitize | no direct file change / merge |
| 2026-07-07 | `f33aed3c8` | `hg-full-base..main` | 通用实现调整 | Merge pull request #75 from HYGON-AI/v0.5.12_dev_rmsnorm | no direct file change / merge |
| 2026-07-07 | `18ad4faac` | `hg-full-base..main` | 缺陷修复 | Merge remote-tracking branch 'origin/v0.5.12_dev' into fix/open-source-compliance-202607 | no direct file change / merge |
| 2026-07-07 | `249ea9001` | `hg-full-base..main` | 缺陷修复 | Merge pull request #77 from HYGON-AI/fix/hcu-runtime-log-sanitize | no direct file change / merge |
| 2026-07-08 | `3bacdc963` | `hg-full-base..main` | 缺陷修复 | Merge remote-tracking branch 'origin/v0.5.12_dev' into fix/open-source-compliance-202607 | no direct file change / merge |
| 2026-07-08 | `5796eff14` | `hg-full-base..main` | 缺陷修复 | Merge pull request #76 from HYGON-AI/fix/open-source-compliance-202607 | no direct file change / merge |
| 2026-07-08 | `bae695b56` | `hg-full-base..main` | 测试/文档/基准 | Merge official main checkpoints C11-C13 | no direct file change / merge |
| 2026-07-08 | `293fa64f0` | `hg-full-base..main` | 测试/文档/基准 | Merge commit '2ad00faae1f4f413330fbc1241dc2c79f44ac4d4' into sync/official-main-C14-C16-20260616 | no direct file change / merge |
| 2026-07-08 | `63d3aece4` | `hg-full-base..main` | 通用实现调整 | merge v0.5.12_dev_eplb_hy3 into v0.5.12_dev | no direct file change / merge |
| 2026-07-09 | `15abf620c` | `hg-full-base..main` | 测试/文档/基准 | Merge official SGLang C17-C19 into DCU bootstrap | no direct file change / merge |
| 2026-07-09 | `44f1d2b06` | `hg-full-base..main` | 通用实现调整 | Merge pull request #82 from HYGON-AI/v0.5.12_dev_lj | no direct file change / merge |
| 2026-07-09 | `76d14014a` | `hg-full-base..main` | 测试/文档/基准 | Merge official main bootstrap C01-C19 into main | no direct file change / merge |
| 2026-07-09 | `d8f3057b3` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catchup 20260623 into DCU main | no direct file change / merge |
| 2026-07-10 | `c7258ab3c` | `hg-full-base..main` | 通用实现调整 | Merge pull request #80 from HYGON-AI/v0.5.12_dev_sxl | no direct file change / merge |
| 2026-07-13 | `a8d65f781` | `hg-full-base..main` | 通用实现调整 | Merge pull request #89 from HYGON-AI/v0.5.12_dev_yql | no direct file change / merge |
| 2026-07-13 | `f38f1a5d2` | `hg-full-base..main` | 性能/后端优化 | test: sync HCU registrations with current main | `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py` and 322 files in total |
| 2026-07-13 | `2da685949` | `hg-full-base..main` | 缺陷修复 | Merge pull request #91 from HYGON-AI/fix/v0512dev-compliance-headers-20260713 | no direct file change / merge |
| 2026-07-13 | `b9cf8ac56` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catchup 20260625 into DCU main | no direct file change / merge |
| 2026-07-13 | `bb9bb4b2d` | `hg-full-base..main` | 性能/后端优化 | ci: rename HCU PR stage suites | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `docs/hcu-pr-ci-visual-guide.html` and 157 files in total |
| 2026-07-13 | `dcd4013b3` | `hg-full-base..main` | 测试/文档/基准 | Merge official SGLang main through 2026-06-29 | no direct file change / merge |
| 2026-07-13 | `c4de02791` | `hg-full-base..main` | 测试/文档/基准 | Merge official SGLang main through 2026-07-03 | no direct file change / merge |
| 2026-07-14 | `dacd24f57` | `hg-full-base..main` | 测试/文档/基准 | ci:resolve-hcu-ci-path-rename-conflicts | no direct file change / merge |
| 2026-07-14 | `f96aaeb79` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catch-up through 20260706 | no direct file change / merge |
| 2026-07-14 | `962a83462` | `hg-full-base..main` | 通用实现调整 | Merge pull request #94 from HYGON-AI/Sherlolo-patch-1 | no direct file change / merge |
| 2026-07-14 | `6cd17f3e3` | `hg-full-base..main` | 测试/文档/基准 | Merge official SGLang main through 2026-07-09 | no direct file change / merge |
| 2026-07-14 | `311ead633` | `hg-full-base..main` | 性能/后端优化 | fix:merge-hcu-flashattention-token-accounting | no direct file change / merge |
| 2026-07-14 | `1a2c734e5` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catch-up through 20260710 | no direct file change / merge |
| 2026-07-15 | `9ec22c5c9` | `hg-full-base..main` | 测试/文档/基准 | Merge sync/official-main-catchup-20260710 into main | no direct file change / merge |
| 2026-07-15 | `7fa6d89c3` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catch-up through 20260712 | no direct file change / merge |
| 2026-07-15 | `e59b241df` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #92 from HYGON-AI/fuse_moe_w4a16 | no direct file change / merge |
| 2026-07-15 | `4cc240b90` | `hg-full-base..main` | 测试/文档/基准 | Merge official main catch-up through 20260713 | no direct file change / merge |
| 2026-07-15 | `21a4a455e` | `hg-full-base..main` | 测试/文档/基准 | Merge official main through v0.5.15.post1 equivalent | no direct file change / merge |
| 2026-07-15 | `d67c7e44e` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 1 | no direct file change / merge |
| 2026-07-15 | `d71a069b7` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 2 | no direct file change / merge |
| 2026-07-15 | `0d3dbd7ab` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 3 | no direct file change / merge |
| 2026-07-16 | `69315951c` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 4 | no direct file change / merge |
| 2026-07-16 | `bdd8d46cc` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 5 | no direct file change / merge |
| 2026-07-16 | `7df16485f` | `hg-full-base..main` | 通用实现调整 | merge(dcu): land v0.5.12_dev forward-port on main | no direct file change / merge |
| 2026-07-16 | `993a79e08` | `hg-full-base..main` | 通用实现调整 | Merge pull request #99 from HYGON-AI/v0.5.12_dev_pp_with_eplb | no direct file change / merge |
| 2026-07-16 | `9b4a5e3ec` | `hg-full-base..main` | 通用实现调整 | Merge pull request #101 from HYGON-AI/v0.5.12_dev_chenyue_causal_conv1d | no direct file change / merge |
| 2026-07-17 | `20828205d` | `hg-full-base..main` | 通用实现调整 | Merge pull request #103 from HYGON-AI/v0.5.12_dev_fabric_custom_all_reduce | no direct file change / merge |
| 2026-07-17 | `17f20798e` | `hg-full-base..main` | 通用实现调整 | Merge pull request #102 from HYGON-AI/v0.5.12_dev_chenyue_causal_conv1d | no direct file change / merge |
| 2026-07-20 | `cc0ab8f37` | `hg-full-base..main` | 缺陷修复 | Merge pull request #105 from HYGON-AI/v0.5.12_dev_bug | no direct file change / merge |
| 2026-07-20 | `c43b06722` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` and 372 files in total |
| 2026-07-20 | `b1d4bf66c` | `hg-full-base..main` | 通用实现调整 | Merge pull request #104 from HYGON-AI/v0.5.12_dev_dsv4_pool | no direct file change / merge |
| 2026-07-20 | `235b13465` | `hg-full-base..main` | 通用实现调整 | Merge pull request #107 from HYGON-AI/feat/ltx2-dynamic-batching-tp | no direct file change / merge |
| 2026-07-21 | `2d509d387` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #113 from HYGON-AI/v0.5.15.post1_dev_rye_megamoe_cp | no direct file change / merge |
| 2026-07-21 | `4859ed3b8` | `hg-full-base..main` | 测试/文档/基准 | Merge official main daily 20260721 | no direct file change / merge |
| 2026-07-22 | `e20e686c7` | `hg-full-base..main` | 通用实现调整 | merge: sync v0.5.15.post1_dev into HCU port | no direct file change / merge |
| 2026-07-22 | `f0d6741cc` | `hg-full-base..main` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev daily 20260722 | no direct file change / merge |
| 2026-07-22 | `c32209f6d` | `hg-full-base..main` | 通用实现调整 | Merge pull request #115 from HYGON-AI/v0.5.15_dev_lzg | no direct file change / merge |
| 2026-07-22 | `1f3d470dc` | `hg-full-base..main` | 通用实现调整 | merge(dcu): integrate origin/v0.5.15.post1_dev PR#115 into forward-port 20260722 | no direct file change / merge |
| 2026-07-22 | `c34b8da18` | `hg-full-base..main` | 通用实现调整 | Resolve HCU rename merge conflicts | no direct file change / merge |
| 2026-07-22 | `7f488ac95` | `hg-full-base..main` | 通用实现调整 | Merge pull request #116 from HYGON-AI/v0.5.12_dev_mla_lightop | no direct file change / merge |
| 2026-07-22 | `124cb938b` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #119 from HYGON-AI/0713-hcu-sglang-test | no direct file change / merge |
| 2026-07-22 | `4783c39c6` | `hg-full-base..main` | 缺陷修复 | Merge pull request #118 from HYGON-AI/fix-dpskv4 | no direct file change / merge |
| 2026-07-22 | `aa2309e22` | `hg-full-base..main` | 性能/后端优化 | chore(compliance): add HYGON headers and provenance | `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py` and 169 files in total |
| 2026-07-22 | `d8df1885d` | `hg-full-base..main` | 调度/缓存/PD | Merge pull request #117 from HYGON-AI/v0.5.12_dev_yaoht_hicache | no direct file change / merge |
| 2026-07-23 | `4459f2e56` | `hg-full-base..main` | 缺陷修复 | Merge pull request #121 from HYGON-AI/fix/open-source-compliance-20260722-latest | no direct file change / merge |
| 2026-07-23 | `ddc07f769` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #120 from HYGON-AI/fix-hcu-deepgemm-fp8-linear-bias | no direct file change / merge |
| 2026-07-23 | `599610198` | `hg-full-base..main` | 测试/文档/基准 | merge: sync latest v0.5.15.post1_dev into HCU port | no direct file change / merge |
| 2026-07-23 | `bee4b423f` | `hg-full-base..main` | 通用实现调整 | Merge pull request #114 from HYGON-AI/hcu/v0.5.15.post1-port | no direct file change / merge |
| 2026-07-24 | `b781224d4` | `hg-full-base..main` | 性能/后端优化 | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` and 466 files in total |
| 2026-07-24 | `cb01580d4` | `hg-full-base..main` | 通用实现调整 | Merge pull request #124 from HYGON-AI/sanitize-hcu-runtime-log-audit-20260723 | no direct file change / merge |
| 2026-07-25 | `0acecf398` | `hg-full-base..main` | 通用实现调整 | Merge branch 'v0.5.12_dev_lightop_ly' into v0.5.12_dev | no direct file change / merge |
| 2026-07-27 | `49764eb37` | `hg-full-base..main` | 通用实现调整 | Merge pull request #131 from HYGON-AI/lvjia-repoguy-patch-1 | no direct file change / merge |
| 2026-07-28 | `f3f52d4ca` | `hg-full-base..main` | 通用实现调整 | Merge pull request #129 from HYGON-AI/v0.5.12_dev_lightop | no direct file change / merge |
| 2026-07-28 | `42908ff67` | `hg-full-base..main` | 通用实现调整 | Merge pull request #130 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | no direct file change / merge |
| 2026-07-28 | `4aa6d4552` | `hg-full-base..main` | 通用实现调整 | Merge pull request #134 from HYGON-AI/dpsk-v4-int8-new-2 | no direct file change / merge |
| 2026-07-28 | `1bd7b4664` | `hg-full-base..main` | 通用实现调整 | Merge pull request #138 from HYGON-AI/dpsk-int8-mtp | no direct file change / merge |
| 2026-07-29 | `ac04c9cb4` | `hg-full-base..main` | 通用实现调整 | Merge pull request #139 from HYGON-AI/0729-hcu-wheel-shared-staging | no direct file change / merge |
| 2026-07-29 | `ba31df0c0` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` and 1924 files in total |
| 2026-07-29 | `d42b0a3bf` | `hg-full-base..main` | 通用实现调整 | merge(hcu): forward-port v0.5.12_dev daily 20260729 | no direct file change / merge |
| 2026-07-29 | `277d9c6f5` | `hg-full-base..main` | 通用实现调整 | Merge pull request #140 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | no direct file change / merge |
| 2026-07-29 | `3bd903cb2` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #147 from HYGON-AI/ci/align-workflows-main-0729 | no direct file change / merge |
| 2026-07-29 | `cce4bdd61` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #148 from HYGON-AI/ci/align-workflows-v0515-0729 | no direct file change / merge |
| 2026-07-29 | `fde49599a` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #144 from HYGON-AI/moe_fuse_gate_bug_fix | no direct file change / merge |
| 2026-07-29 | `ec651411a` | `hg-full-base..main` | 通用实现调整 | Merge pull request #143 from HYGON-AI/v0.5.12_dev_lc | no direct file change / merge |
| 2026-07-29 | `ed331a148` | `hg-full-base..main` | 通用实现调整 | Merge pull request #141 from HYGON-AI/v0.5.12_dev_maxiao | no direct file change / merge |
| 2026-07-30 | `1a5a9521a` | `hg-full-base..main` | 通用实现调整 | Merge pull request #151 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | no direct file change / merge |
| 2026-07-31 | `603b95cea` | `hg-full-base..main` | 调度/缓存/PD | Merge pull request #137 from HYGON-AI/ci/hcu-pd-smoke-v0.5.12 | no direct file change / merge |
| 2026-07-31 | `6b778d9ae` | `hg-full-base..main` | 模型支持/运行时入口 | [Router] Add Anthropic Messages thinking support | `sgl-model-gateway/src/middleware.rs`, `sgl-model-gateway/src/routers/anthropic.rs`, `sgl-model-gateway/src/routers/mod.rs` and 4 files in total |
| 2026-08-01 | `f4054ca15` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #153 from HYGON-AI/v0.5.12_dev_chenyue_moe_c | no direct file change / merge |
| 2026-08-01 | `3eb90b8a6` | `hg-full-base..main` | 缺陷修复 | Merge pull request #155 from HYGON-AI/longprompt-deadloop-fix | no direct file change / merge |
| 2026-08-03 | `d08093cb4` | `hg-full-base..main` | 通用实现调整 | Merge pull request #158 from HYGON-AI/lvj-repox-patch-1 | no direct file change / merge |
| 2026-08-03 | `5fafd197c` | `hg-full-base..main` | 缺陷修复 | Merge pull request #159 from HYGON-AI/fix/hcu-feishu-accuracy-status | no direct file change / merge |
| 2026-08-03 | `b97d7df6e` | `hg-full-base..main` | 性能/后端优化 | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` and 184 files in total |
| 2026-08-04 | `8bb597e2c` | `hg-full-base..main` | 通用实现调整 | Merge commit 'd703c086ff42655c602b85c9f0ac935215f8c4cc' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `2ceaca5ef` | `hg-full-base..main` | 通用实现调整 | Merge commit '2d509d387218fb0e71ca4880cba8c56570316ab3' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `050d160da` | `hg-full-base..main` | 通用实现调整 | Merge commit 'f0d6741cc1fc14ad8d74a12777345d23ec8ed7fc' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `4315f50a0` | `hg-full-base..main` | 通用实现调整 | Merge commit '1f3d470dc5ff3365a87ae317ea12ef341335fffe' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `9c451b2d2` | `hg-full-base..main` | 通用实现调整 | Merge commit '9fc04a7a2cebc525a96301d3e8e9515bb0a5b4b6' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `7ac99d59b` | `hg-full-base..main` | 通用实现调整 | Merge commit 'c43b06722' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `1462076bb` | `hg-full-base..main` | 通用实现调整 | Merge commit '1e2fec228' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `de2659dc6` | `hg-full-base..main` | 通用实现调整 | Merge commit '358a33714' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `bb91d55c7` | `hg-full-base..main` | 通用实现调整 | Merge commit '416bbd9b9' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `515526331` | `hg-full-base..main` | 通用实现调整 | Merge commit '81e3561ae' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `0792d89a9` | `hg-full-base..main` | 通用实现调整 | Merge commit '811aa027d' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `235a6b991` | `hg-full-base..main` | 通用实现调整 | Merge commit '15a656ea6' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `b2e118b59` | `hg-full-base..main` | 通用实现调整 | Merge commit '9864c8451' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `a822ab35c` | `hg-full-base..main` | 通用实现调整 | Merge commit '9b86479ac' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `8bb3f9ecb` | `hg-full-base..main` | 通用实现调整 | Merge commit 'ac56ca009' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `d91d2c7d7` | `hg-full-base..main` | 通用实现调整 | Merge commit 'bee4b423f68fa27792f5d8ed79eb9ecbb5e0f4e6' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `f628e2a98` | `hg-full-base..main` | 通用实现调整 | Merge commit '7482123c3' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `128f5f73b` | `hg-full-base..main` | 通用实现调整 | Merge commit '0710e82a0' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `fc4bd96f4` | `hg-full-base..main` | 通用实现调整 | Merge commit '997e64560' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `19889fe0e` | `hg-full-base..main` | 通用实现调整 | Merge commit 'cce4bdd61' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `e1ad3a989` | `hg-full-base..main` | 通用实现调整 | Merge commit 'e7106de94' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `9e305f571` | `hg-full-base..main` | 通用实现调整 | Merge commit 'd08093cb4' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `74d439192` | `hg-full-base..main` | 通用实现调整 | Merge commit 'de696eab9' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-04 | `9dda7e375` | `hg-full-base..main` | 通用实现调整 | Merge commit 'b97d7df6e' into forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-05 | `bba6b88d3` | `hg-full-base..main` | 通用实现调整 | Merge pull request #160 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme | no direct file change / merge |
| 2026-08-05 | `6d85dc772` | `hg-full-base..main` | 通用实现调整 | Merge pull request #161 from HYGON-AI/v0.5.12_dev_sxl | no direct file change / merge |
| 2026-08-05 | `d20f0063d` | `hg-full-base..main` | 缺陷修复 | Merge pull request #165 from HYGON-AI/v0.5.12_dev_triton_fp8_bug_fix | no direct file change / merge |
| 2026-08-05 | `54d01422a` | `hg-full-base..main` | 缺陷修复 | Merge pull request #163 from HYGON-AI/fix-dpsk-mtp-assert | no direct file change / merge |
| 2026-08-05 | `f320ce265` | `hg-full-base..main` | 缺陷修复 | Merge pull request #164 from HYGON-AI/longprompt-deadloop-fix | no direct file change / merge |
| 2026-08-05 | `20ba56a96` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #166 from HYGON-AI/v0.5.12_dev_opt_c128_state_pool | no direct file change / merge |
| 2026-08-06 | `b1b81c18f` | `hg-full-base..main` | 缺陷修复 | Merge pull request #169 from HYGON-AI/fix/hcu-wheel-gateway-classification | no direct file change / merge |
| 2026-08-06 | `1672d9e47` | `hg-full-base..main` | 通用实现调整 | Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804 | no direct file change / merge |
| 2026-08-06 | `b91477f29` | `hg-full-base..main` | 通用实现调整 | chore(hcu): anchor forward-port base to ac04c9cb (no content change) | no direct file change / merge |
| 2026-08-06 | `4da105483` | `hg-full-base..main` | 通用实现调整 | merge(hcu): forward-port v0.5.12_dev daily 20260806 (ac04c9cb..b1b81c18f) | no direct file change / merge |
| 2026-08-06 | `34b6864a2` | `hg-full-base..main` | 通用实现调整 | Merge pull request #173 from HYGON-AI/forward-port/v0.5.12-dev-daily-20260806 | no direct file change / merge |
| 2026-08-07 | `eda349619` | `hg-full-base..main` | 测试/文档/基准 | chore(hcu): anchor daily sync base to official edc0e5489 (no content change) | no direct file change / merge |
| 2026-08-07 | `654ff007e` | `hg-full-base..main` | 缺陷修复 | [BugFix] fix the lmslim and lightop calling issues regressions (#176) | no direct file change / merge |
| 2026-08-07 | `b7bd14f19` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): normalize HCU suite names | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` and 199 files in total |
| 2026-08-10 | `80e01615e` | `hg-full-base..main` | 测试/文档/基准 | Sync/official main daily 20260807 | no direct file change / merge |
| 2026-08-10 | `37b7742e7` | `hg-full-base..main` | 测试/文档/基准 | Sync/official main 20260810 (v0.5.17) | no direct file change / merge |
| 2026-08-10 | `6f86e904d` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #179 from HYGON-AI/sync/official-main-20260810 | no direct file change / merge |
| 2026-08-10 | `8f7a660e5` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #183 from HYGON-AI/sync/official-main-20260810 | no direct file change / merge |
| 2026-08-11 | `ad1fea5d7` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci | no direct file change / merge |
| 2026-08-12 | `5daa79af7` | `hg-full-base..main` | 通用实现调整 | merge(hcu): forward-port v0.5.15.post1_dev through 20260811 | no direct file change / merge |
| 2026-08-12 | `9b76db90d` | `hg-full-base..main` | 通用实现调整 | Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811 | no direct file change / merge |
| 2026-08-12 | `856b425b8` | `hg-full-base..main` | 缺陷修复 | Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix | no direct file change / merge |
| 2026-08-12 | `74e12e1e8` | `hg-full-base..main` | 缺陷修复 | Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515 | no direct file change / merge |
| 2026-08-13 | `97a1938e2` | `hg-full-base..main` | 缺陷修复 | Merge pull request #192 from HYGON-AI/rye_dspark_bugfix | no direct file change / merge |
| 2026-08-14 | `1c349c31f` | `hg-full-base..main` | 通用实现调整 | merge(hcu): forward-port v0.5.15.post1_dev through 20260813 | no direct file change / merge |
| 2026-08-17 | `d95af36e1` | `hg-full-base..main` | 通用实现调整 | Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813 | no direct file change / merge |
| 2026-08-17 | `9f4368f10` | `hg-full-base..main` | 测试/文档/基准 | merge(hcu): backport official main through 20260817 (92b1d382c7) | no direct file change / merge |
| 2026-08-17 | `d20a4750f` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #208 from HYGON-AI/backport/official-main-20260817 | no direct file change / merge |
| 2026-08-24 | `4a540f118` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | no direct file change / merge |
| 2026-08-24 | `2e8f1408b` | `hg-full-base..main` | 通用实现调整 | Merge pull request #214 from Crowder13/main | no direct file change / merge |
| 2026-08-24 | `7676961ba` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | no direct file change / merge |
| 2026-08-25 | `16d7caa10` | `hg-full-base..main` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` and 1857 files in total |
| 2026-08-25 | `dd41b1f06` | `hg-full-base..main` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | no direct file change / merge |
| 2026-08-25 | `97aa7a298` | `hg-full-base..main` | 通用实现调整 | Merge pull request #224 from dddddddxl/hcu/fork-pr-target | no direct file change / merge |
| 2026-08-25 | `4eacd3c36` | `hg-full-base..main` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | no direct file change / merge |
| 2026-08-25 | `8ba0c9376` | `hg-full-base..main` | 通用实现调整 | Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout | no direct file change / merge |
| 2026-08-25 | `7481b1f54` | `hg-full-base..main` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | no direct file change / merge |
| 2026-08-25 | `a3cfa2a97` | `hg-full-base..main` | 测试/文档/基准 | Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824 | no direct file change / merge |
| 2026-08-25 | `d445b357f` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | no direct file change / merge |
| 2026-08-25 | `688659c15` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership | no direct file change / merge |
| 2026-08-26 | `ed9037191` | `hg-full-base..main` | 缺陷修复 | Merge pull request #238 from dddddddxl/hcu/fix-bash-shell-main | no direct file change / merge |
| 2026-08-26 | `c832752c7` | `hg-full-base..main` | 通用实现调整 | Merge remote-tracking branch 'origin/main' into review/pr-230 | no direct file change / merge |
| 2026-08-26 | `26c6e0fb3` | `hg-full-base..main` | 通用实现调整 | Merge pull request #230 from reverie-hub/hcu/sanitize-runtime | no direct file change / merge |
| 2026-08-27 | `a15b56677` | `hg-full-base..main` | 通用实现调整 | Merge branch 'HYGON-AI:main' into main | no direct file change / merge |
| 2026-08-27 | `fd402a780` | `hg-full-base..main` | 缺陷修复 | Merge pull request #246 from dddddddxl/hcu/fix-safe-directory-main | no direct file change / merge |
| 2026-08-27 | `dc7b624e9` | `hg-full-base..main` | 通用实现调整 | Merge branch 'HYGON-AI:main' into main | no direct file change / merge |
| 2026-08-28 | `13c60ec0d` | `hg-full-base..main` | 通用实现调整 | Merge pull request #254 from Crowder13/main | no direct file change / merge |
| 2026-08-31 | `5cf052bd0` | `hg-full-base..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | no direct file change / merge |
| 2026-08-31 | `20ee2b297` | `hg-full-base..main` | 性能/后端优化 | Merge pull request #216 from Zhuwenbopro/feature/aiter-adaptation-zhuwenbo | no direct file change / merge |
| 2026-08-31 | `cc6b7c948` | `hg-full-base..main` | 通用实现调整 | Merge pull request #269 from dddddddxl/hcu/remove-amd-pr-state-main | no direct file change / merge |
| 2026-09-01 | `50bacb028` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` and 1435 files in total |
| 2026-09-03 | `d150cf2ac` | `hg-full-base..main` | 缺陷修复 | [BUGFIX]torchaudio使用hcu的版本 (#298) | `docker/hcu.Dockerfile` |
| 2026-09-07 | `df05aa9f9` | `hg-full-base..main` | 测试/文档/基准 | [FEATURE] daily镜像里面加装ai-dynamo (#313) | `docker/hcu.Dockerfile` |
| 2026-09-08 | `ee0f2375e` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` and 3600 files in total |
| 2026-09-14 | `ca25bc427` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` and 1792 files in total |
| 2026-09-20 | `16229e94d` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` and 1583 files in total |
| 2026-09-23 | `2f9a696ab` | `hg-full-base..main` | 测试/文档/基准 | [FEATURE] 基础镜像内置 shca 驱动 (#440) | `docker/hcu.Dockerfile` |
| 2026-09-28 | `6049c219e` | `hg-full-base..main` | 性能/后端优化 | Glm5.3 flash (#427) | `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc` and 196 files in total |
| 2026-09-29 | `ab43824b0` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` and 2902 files in total |
| 2026-09-30 | `756ae5b4f` | `hg-full-base..main` | 性能/后端优化 | Sync/20260929 rye rel 2 main (#470) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` and 313 files in total |
| 2026-10-08 | `5cf6ed7f7` | `hg-full-base..main` | 性能/后端优化 | [BUGFIX]镜像增加安装megamoe (#479) | `docker/hcu.Dockerfile` |
| 2026-10-12 | `36b93840b` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` and 3300 files in total |
| 2026-10-20 | `4975d6490` | `hg-full-base..main` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` and 3006 files in total |
| 2026-10-21 | `5f67ce01c` | `hg-full-base..main` | 性能/后端优化 | Sync/rel 2 main 20261021 dsv4 validated (#576) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore` and 321 files in total |

### Per-Commit Audit Cards

- The timeline lists all 246 commits; audit cards cover only the most recent 80.

#### Commit `bb91d55c7` - Merge commit '416bbd9b9' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `bb91d55c7ab3b90cc09139d5f6c1b92301ee46fe`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `515526331` - Merge commit '81e3561ae' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `5155263318cf7b01fa78ed0606f330b9e76d7db4`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `0792d89a9` - Merge commit '811aa027d' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `0792d89a997bdc052b84469179e107928543c521`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `235a6b991` - Merge commit '15a656ea6' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `235a6b99156b98a95255264a42741465a0c534c5`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `b2e118b59` - Merge commit '9864c8451' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `b2e118b59a6f7a5762e70e821a430d3ff525894d`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `a822ab35c` - Merge commit '9b86479ac' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `a822ab35c92cc04fdbe4952d559d5fcff7471898`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `8bb3f9ecb` - Merge commit 'ac56ca009' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `8bb3f9ecbb788865a359428361afbb60833f303b`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `d91d2c7d7` - Merge commit 'bee4b423f68fa27792f5d8ed79eb9ecbb5e0f4e6' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `d91d2c7d72c8aa86fd871a978e82fc989663c03a`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `f628e2a98` - Merge commit '7482123c3' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `f628e2a9840d4dd0ef850f8fe8a193761b01b27a`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `128f5f73b` - Merge commit '0710e82a0' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `128f5f73b6ff1885819fe35889a076ab1cc57b41`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `fc4bd96f4` - Merge commit '997e64560' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `fc4bd96f4346ee32b05f9713b4c2e5aa3f3a584c`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `19889fe0e` - Merge commit 'cce4bdd61' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `19889fe0e241c5613ddcd3db6c82b2a11d01b36e`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `e1ad3a989` - Merge commit 'e7106de94' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `e1ad3a98986cfb1809b1ec5999e62029786d0cda`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `9e305f571` - Merge commit 'd08093cb4' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `9e305f5717087f05b2f415bd641e4c4d903dbdb3`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `74d439192` - Merge commit 'de696eab9' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `74d439192d38be421aecd837ae692785ca5bface`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `9dda7e375` - Merge commit 'b97d7df6e' into forward-port/v0.5.15-post1-dev-20260804

- Full hash: `9dda7e375e0a8a8815ebacafec60cb8015cd77c3`
- Date/author: 2026-08-04 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `bba6b88d3` - Merge pull request #160 from HYGON-AI/v0.5.12_dev_yaoht_hy3-w8a8-kme

- Full hash: `bba6b88d35a46e625ac63dcfded4bb018e36c058`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `6d85dc772` - Merge pull request #161 from HYGON-AI/v0.5.12_dev_sxl

- Full hash: `6d85dc772b80562970c1ce03e3350b257d4c13bf`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `d20f0063d` - Merge pull request #165 from HYGON-AI/v0.5.12_dev_triton_fp8_bug_fix

- Full hash: `d20f0063d77fffd1bbced7b8e8f978f18fe9b728`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `54d01422a` - Merge pull request #163 from HYGON-AI/fix-dpsk-mtp-assert

- Full hash: `54d01422ab76854de5eda5b85c89055839d2e0e9`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `f320ce265` - Merge pull request #164 from HYGON-AI/longprompt-deadloop-fix

- Full hash: `f320ce2655d86e9f0e012326c635f9a4dd1f81ed`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `20ba56a96` - Merge pull request #166 from HYGON-AI/v0.5.12_dev_opt_c128_state_pool

- Full hash: `20ba56a96f9a14a25cebaeb1ad6b5c8423c0bf67`
- Date/author: 2026-08-05 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `b1b81c18f` - Merge pull request #169 from HYGON-AI/fix/hcu-wheel-gateway-classification

- Full hash: `b1b81c18f096e4c26f1705e1d1c6861c1d364585`
- Date/author: 2026-08-06 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `1672d9e47` - Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804

- Full hash: `1672d9e470a59c952e881dfebe9bae6ac914656e`
- Date/author: 2026-08-06 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `b91477f29` - chore(hcu): anchor forward-port base to ac04c9cb (no content change)

- Full hash: `b91477f2961992d12adb427475d633118cdc9fe3`
- Date/author: 2026-08-06 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `4da105483` - merge(hcu): forward-port v0.5.12_dev daily 20260806 (ac04c9cb..b1b81c18f)

- Full hash: `4da105483f725fb89c5689a4f299abb09f305571`
- Date/author: 2026-08-06 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `34b6864a2` - Merge pull request #173 from HYGON-AI/forward-port/v0.5.12-dev-daily-20260806

- Full hash: `34b6864a208cb053f0dffaec4f54ea0df0d4788a`
- Date/author: 2026-08-06 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `eda349619` - chore(hcu): anchor daily sync base to official edc0e5489 (no content change)

- Full hash: `eda349619bd4ca60246bea0a2623c4b494bd7ea9`
- Date/author: 2026-08-07 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `654ff007e` - [BugFix] fix the lmslim and lightop calling issues regressions (#176)

- Full hash: `654ff007ee5e1f60aee5b7a07a42fcac7a61ff93`
- Date/author: 2026-08-07 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `b7bd14f19` - ci(hcu): normalize HCU suite names

- Full hash: `b7bd14f19898fe547e644590f0096bef715f0072`
- Date/author: 2026-08-07 / LvJIA-RG
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md`, `scripts/ci/hcu/hcu_ci_pd.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_deterministic.py` 等 199 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_pd.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_deterministic.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py` 等 194 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `80e01615e` - Sync/official main daily 20260807

- Full hash: `80e01615e8ea05d69b290ee983490bf4f44c599e`
- Date/author: 2026-08-10 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `37b7742e7` - Sync/official main 20260810 (v0.5.17)

- Full hash: `37b7742e7e55116c01f8565fe578b2478c476560`
- Date/author: 2026-08-10 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `6f86e904d` - Merge pull request #179 from HYGON-AI/sync/official-main-20260810

- Full hash: `6f86e904d21870cf1f638e4713725ecca120f757`
- Date/author: 2026-08-10 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `8f7a660e5` - Merge pull request #183 from HYGON-AI/sync/official-main-20260810

- Full hash: `8f7a660e58527db05b130f5609d95b86885f84da`
- Date/author: 2026-08-10 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `ad1fea5d7` - Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci

- Full hash: `ad1fea5d74f6264de5734bee8971bbade980343d`
- Date/author: 2026-08-11 / dingxinlong
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `5daa79af7` - merge(hcu): forward-port v0.5.15.post1_dev through 20260811

- Full hash: `5daa79af74da9583663ed20eb29779320ce7bece`
- Date/author: 2026-08-12 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `9b76db90d` - Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811

- Full hash: `9b76db90d66ff3f0379f66a52b24102bf7fb264d`
- Date/author: 2026-08-12 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `856b425b8` - Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix

- Full hash: `856b425b86102879467e89dc3912c76af654643c`
- Date/author: 2026-08-12 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `74e12e1e8` - Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515

- Full hash: `74e12e1e8fbd5e38be975645f64355df8b671e57`
- Date/author: 2026-08-12 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `97a1938e2` - Merge pull request #192 from HYGON-AI/rye_dspark_bugfix

- Full hash: `97a1938e2bd04cffd7f07570e7d91679034c4dbc`
- Date/author: 2026-08-13 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `1c349c31f` - merge(hcu): forward-port v0.5.15.post1_dev through 20260813

- Full hash: `1c349c31fc7f51c71c63d812b1213b3fe1f47edf`
- Date/author: 2026-08-14 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `d95af36e1` - Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813

- Full hash: `d95af36e1331aa3c7064eb837dd7103b6406b8a8`
- Date/author: 2026-08-17 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `9f4368f10` - merge(hcu): backport official main through 20260817 (92b1d382c7)

- Full hash: `9f4368f104fbf93f744eafef685ebe8f8a94ff3c`
- Date/author: 2026-08-17 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `d20a4750f` - Merge pull request #208 from HYGON-AI/backport/official-main-20260817

- Full hash: `d20a4750f11e581c0691752f3d6b7389312a6819`
- Date/author: 2026-08-17 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `4a540f118` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- Full hash: `4a540f1186efe80fe46b6459c199f9d2f883974f`
- Date/author: 2026-08-24 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `2e8f1408b` - Merge pull request #214 from Crowder13/main

- Full hash: `2e8f1408b42432408dc0087dec9f8520204d5a75`
- Date/author: 2026-08-24 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `7676961ba` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- Full hash: `7676961ba770d5327714e7220186a1943c25c594`
- Date/author: 2026-08-24 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `16d7caa10` - sync(hcu): official main through 20260824 (c8e1ddc707)

- Full hash: `16d7caa1065abd2af782f3afc35c3dc4da745cde`
- Date/author: 2026-08-25 / RyeYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/diffusion-authoring.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl` 等 1857 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/labeler.yml`; `.github/update_ci_permission.py`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 42 个文件
  - docs-bench: `benchmark/hicache/bench_buffer_mode.py`; `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`; `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`; `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/Google/Gemma4.mdx` 等 115 个文件
  - other: `.claude/rules/comment-style.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/references/diffusion-authoring.md`; `.claude/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl`; `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `.claude/skills/sglang-runtime-context/SKILL.md` 等 288 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/sgl-kv-indexer/.gitignore`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml` 等 257 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `python/sglang/kernel_api_logging.py`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/cpu/activation.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 453 个文件
  - tests: `experimental/sgl-router/sgl-kv-indexer/tests/common/id.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/net.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/memory_integration.rs`; `experimental/sgl-router/tests/component/policies/cache_aware_zmq.rs`; `experimental/sgl-router/tests/e2e/chat_completions/test_two_router_convergence.py`; `experimental/sgl-router/tests/e2e/infra/gateway.py` 等 702 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `dd41b1f06` - Merge branch 'main' into sync/official-main-daily-20260824

- Full hash: `dd41b1f06dee84cdb3a77eb2a4c3cdd64306bebc`
- Date/author: 2026-08-25 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `97aa7a298` - Merge pull request #224 from dddddddxl/hcu/fork-pr-target

- Full hash: `97aa7a298a3274cddc7b19c55123fed05e112336`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `4eacd3c36` - Merge branch 'main' into sync/official-main-daily-20260824

- Full hash: `4eacd3c36d9ee880fae87ea072e22fb5bf641b30`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `8ba0c9376` - Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout

- Full hash: `8ba0c9376f157769b4fd8bccb560af739b61d15b`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `7481b1f54` - Merge branch 'main' into sync/official-main-daily-20260824

- Full hash: `7481b1f5430eb91025166a3f0a6a9e920ef8348a`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `a3cfa2a97` - Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824

- Full hash: `a3cfa2a979442d114187460e31d42f3fb4744441`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `d445b357f` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- Full hash: `d445b357fd702592f289a6e72161901a72c69df0`
- Date/author: 2026-08-25 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `688659c15` - Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership

- Full hash: `688659c15694195ee0c6fab18de26b60b313b82f`
- Date/author: 2026-08-25 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `ed9037191` - Merge pull request #238 from dddddddxl/hcu/fix-bash-shell-main

- Full hash: `ed903719178b9f6592d9160aabedbd6d55679c12`
- Date/author: 2026-08-26 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `c832752c7` - Merge remote-tracking branch 'origin/main' into review/pr-230

- Full hash: `c832752c72ec3fb573ca121d88e109940d621729`
- Date/author: 2026-08-26 / dddddddxl
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `26c6e0fb3` - Merge pull request #230 from reverie-hub/hcu/sanitize-runtime

- Full hash: `26c6e0fb3d9557be7c9f9a9a3b4ef48b1bbbb561`
- Date/author: 2026-08-26 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `a15b56677` - Merge branch 'HYGON-AI:main' into main

- Full hash: `a15b56677625f2f4c9906559376a97f70b86636e`
- Date/author: 2026-08-27 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `fd402a780` - Merge pull request #246 from dddddddxl/hcu/fix-safe-directory-main

- Full hash: `fd402a7803ec007123f6a201b8d27f73071b156a`
- Date/author: 2026-08-27 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `dc7b624e9` - Merge branch 'HYGON-AI:main' into main

- Full hash: `dc7b624e97ff48076819a10c5a08f89f2a8dcc23`
- Date/author: 2026-08-27 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `13c60ec0d` - Merge pull request #254 from Crowder13/main

- Full hash: `13c60ec0d41c2880f2f4cd811f13a93cc9677684`
- Date/author: 2026-08-28 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `5cf052bd0` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- Full hash: `5cf052bd014a50378029315ef0654a2318badf1f`
- Date/author: 2026-08-31 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `20ee2b297` - Merge pull request #216 from Zhuwenbopro/feature/aiter-adaptation-zhuwenbo

- Full hash: `20ee2b297f01e602a640c9219d658c643b3c306c`
- Date/author: 2026-08-31 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `cc6b7c948` - Merge pull request #269 from dddddddxl/hcu/remove-amd-pr-state-main

- Full hash: `cc6b7c9481e9696bdeea86a63f769ce835b03a4b`
- Date/author: 2026-08-31 / Lvjiajia
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `50bacb028` - Sync/official main daily 20260831 (#273)

- Full hash: `50bacb028023ba6d0155267a7c0f7841d5ec3fd7`
- Date/author: 2026-09-01 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/nightly-test-npu.yml` 等 1435 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/CI_PERMISSIONS.json`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-stage.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/nightly-test-npu.yml`; `.github/workflows/pr-test-amd-extra.yml` 等 21 个文件
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/lean_kernel_sweep.py`; `benchmark/unified_memory/bench_peer_aware_eviction.py`; `docs/cards/logos/ibm.png`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` 等 100 个文件
  - other: `.claude/skills/sglang-runtime-context/SKILL.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134`; `docker/kimi_k3/apply_deepep_k3_patch.sh`; `docker/kimi_k3/kimi_k3_cu12.Dockerfile`; `docker/kimi_k3/kimi_k3_cu13.Dockerfile`; `docker/npu.Dockerfile`; `python/pyproject.toml` 等 299 个文件
  - runtime-model: `python/sglang/benchmark/one_batch_server.py`; `python/sglang/launch_server.py`; `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/configs/models/encoders/base.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/longcat_image.py` 等 133 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/cmake/flashmla.cmake`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`; `python/sglang/kernels/aot/csrc/cpu/extend.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 396 个文件
  - tests: `python/sglang/multimodal_gen/test/run_suite.py`; `python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py`; `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`; `python/sglang/multimodal_gen/test/server/ascend/test_glm_image_distributed.py`; `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`; `python/sglang/multimodal_gen/test/server/gpu_cases.py`; `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`; `python/sglang/multimodal_gen/test/server/test_server_common.py` 等 486 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `d150cf2ac` - [BUGFIX]torchaudio使用hcu的版本 (#298)

- Full hash: `d150cf2acd16a9b416c399ab3662264684b3962b`
- Date/author: 2026-09-03 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `docker/hcu.Dockerfile`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `df05aa9f9` - [FEATURE] daily镜像里面加装ai-dynamo (#313)

- Full hash: `df05aa9f9dac6b5fe4fd4ce3fd5ee86a35106b62`
- Date/author: 2026-09-07 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `docker/hcu.Dockerfile`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `ee0f2375e` - Sync/official main daily 20260907 (#328)

- Full hash: `ee0f2375e5fb285e4fb021a9831fa88018244679`
- Date/author: 2026-09-08 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py` 等 3600 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/_pr-test-rust-ext-build.yml`; `.github/workflows/_pr-test-simulator-cpu.yml` 等 43 个文件
  - docs-bench: `benchmark/asr/bench_sglang.py`; `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_client.py`; `benchmark/hf3fs/bench_storage.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/hicache/bench_mix.py`; `benchmark/hicache/bench_multiturn.py` 等 133 个文件
  - other: `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`; `.claude/skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.git-blame-ignore-revs`; `.gitignore` 等 510 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/policy_select.rs`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 402 个文件
  - runtime-perf: `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `python/sglang/kernels/aot/benchmark/bench_amd_deterministic_allreduce.py` 等 683 个文件
  - tests: `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_add_imports.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_extract_symbols_to_new_module.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_assign.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_symbol.py`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs` 等 1829 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ca25bc427` - Sync/official main daily 20260914 (#362)

- Full hash: `ca25bc4275b93e02a48a2f8158835f372fee3553`
- Date/author: 2026-09-14 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.codespellrc` 等 1792 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/workflows/_docker-build-and-publish.yml` 等 44 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_int8_checkpoint_reuse.py`; `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`; `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/simulator/bench_runner.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 130 个文件
  - other: `.claude/rules/unit-test-admission.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.codespellrc`; `.gitleaksignore`; `3rdparty/amd/wheel/README.md` 等 284 个文件
  - runtime-model: `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/src/policies/buckets.rs`; `experimental/sgl-router/src/policies/mod.rs`; `experimental/sgl-router/src/proxy/mod.rs`; `experimental/sgl-router/src/proxy/sse.rs`; `experimental/sgl-router/src/server/metrics.rs`; `experimental/sgl-router/src/server/routes/chat.rs`; `python/sglang/launch_server.py` 等 148 个文件
  - runtime-perf: `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`; `3rdparty/amd/wheel/sgl-kernel/rename_wheels_rocm.sh`; `docker/patches/sgl-kernel-gfx1151.sh`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/Dockerfile` 等 412 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/proxy/bucket_routing.rs`; `experimental/sgl-router/tests/proxy/chat_routing.rs`; `python/sglang/kernels/aot/tests/test_awq_dequant.py`; `python/sglang/kernels/aot/tests/test_cutlass_mla.py`; `python/sglang/kernels/aot/tests/test_flash_attn_sparse.py`; `python/sglang/kernels/aot/tests/test_fused_qk_norm_rope.py` 等 774 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `16229e94d` - Sync/official main daily 20260920 (#410)

- Full hash: `16229e94d0a0a218875ab0db2133c12d9695abd1`
- Date/author: 2026-09-20 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 1583 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/bot-bump-sglang-version.yml`; `.github/workflows/ci-coverage-overview.yml` 等 26 个文件
  - docs-bench: `benchmark/agentic-rollout/README.md`; `benchmark/agentic-rollout/explore.py`; `benchmark/agentic-rollout/metrics.py`; `benchmark/agentic-rollout/plot.py`; `benchmark/agentic-rollout/simulate.py`; `benchmark/agentic-rollout/spec/README.md`; `benchmark/agentic-rollout/spec/evidence/feature-00-session-hicache-latency.md`; `benchmark/agentic-rollout/spec/feature-00-session-hicache-latency.md` 等 127 个文件
  - other: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`; `.claude/skills/ci-test-audit/SKILL.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.gitignore`; `.gitleaksignore`; `docker/Dockerfile.cu134`; `docker/npu.Dockerfile` 等 217 个文件
  - runtime-model: `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/deny.toml`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json` 等 234 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/cpu/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/cpu/bmm.cpp` 等 443 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `benchmark/agentic-rollout/tests/test_explore.py`; `benchmark/agentic-rollout/tests/test_simulate.py`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs`; `experimental/sgl-router/tests/component/policies/kv_events_two_subscribers.rs`; `experimental/sgl-router/tests/component/policies/zmq_helpers.rs` 等 536 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2f9a696ab` - [FEATURE] 基础镜像内置 shca 驱动 (#440)

- Full hash: `2f9a696abd7055f8cdc545b168b1bcd730cc6109`
- Date/author: 2026-09-23 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `docker/hcu.Dockerfile`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `6049c219e` - Glm5.3 flash (#427)

- Full hash: `6049c219ec044420bbacce7eddfe7ae31e031625`
- Date/author: 2026-09-28 / leon.wang
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/kpool_write_plan.cu`, `python/sglang/kernels/aot/csrc/elementwise/topk.hip`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/python/sgl_kernel/__init__.py` 等 196 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/__init__.py`; `python/sglang/srt/arg_groups/fields/parallel.py`; `python/sglang/srt/arg_groups/fields/serving.py`; `python/sglang/srt/arg_groups/fields/spec.py`; `python/sglang/srt/arg_groups/model_hook.py`; `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`; `python/sglang/srt/arg_groups/overrides.py` 等 73 个文件
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/glm5_next.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/disaggregation/encoder/server.py`; `python/sglang/srt/entrypoints/anthropic/serving.py`; `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/entrypoints/http_server.py` 等 33 个文件
  - runtime-perf: `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/kpool_write_plan.cu`; `python/sglang/kernels/aot/csrc/elementwise/topk.hip`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/python/sgl_kernel/__init__.py` 等 88 个文件
  - tests: `test/manual/test_hcu_delta_rule_cuda.py`; `test/registered/quant/test_fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ab43824b0` - Sync/official main daily 20260928 (#452)

- Full hash: `ab43824b09055fc790bd5a9166a6a6182b1bccc3`
- Date/author: 2026-09-29 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 2902 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/actions/check-pr-test-health/action.test.cjs`; `.github/actions/check-pr-test-health/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml` 等 42 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/disaggregation/bench_cached_prefix.py`; `benchmark/dllm/README.md`; `benchmark/dllm/bench_diffusion_gemma.py`; `benchmark/gsm8k/README.md`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/io/bench_mm_token_padding.py` 等 209 个文件
  - other: `.claude/rules/cookbook-first.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/clean-startup-log/SKILL.md`; `.claude/skills/clean-startup-log/references/noise-sources.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/env-var-conventions/SKILL.md`; `.claude/skills/generate-profile/SKILL.md` 等 383 个文件
  - runtime-model: `.pre-commit-config.yaml`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/src/buckets_reorg.rs` 等 312 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/kernel-organization/SKILL.md`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `python/sglang/kernels/README.md` 等 898 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/main.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/decode.rs`; `experimental/sgl-router/tests/component/policies/fused_score.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs` 等 1058 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `756ae5b4f` - Sync/20260929 rye rel 2 main (#470)

- Full hash: `756ae5b4fe26cf9ad666d46cda6c45b14b3abc60`
- Date/author: 2026-09-30 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `README_HCU.md`, `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `benchmark/glm53/README.md`, `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py` 等 313 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/quality-gate.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`; `benchmark/glm53/README.md`; `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`; `docs/internal/README_BF16_FLASHMLA.md`
  - other: `README_HCU.md`; `python/pyproject_hcu.toml`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`; `python/sglang/srt/arg_groups/choices.py`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 63 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`; `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py` 等 33 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu`; `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh` 等 158 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `test/hcu_humaneval_judge.py`; `test/manual/ep/test_kimi_k3_eplb.py`; `test/manual/layers/test_hy4_ihc_tilelang.py` 等 51 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5cf6ed7f7` - [BUGFIX]镜像增加安装megamoe (#479)

- Full hash: `5cf6ed7f71fac8dab1983923c93e2d42074079c3`
- Date/author: 2026-10-08 / Crowder13
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `docker/hcu.Dockerfile`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `36b93840b` - Sync/official main daily 20261009 (#500)

- Full hash: `36b93840b54b8c41fe395e6f3e3f9a5463fe17ba`
- Date/author: 2026-10-12 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`, `.agents/skills/ci-test-audit/SKILL.md`, `.agents/skills/ci-test-audit/action-items.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/clean-startup-log/SKILL.md` 等 3300 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/check-maintenance/action.yml`; `.github/labeler.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/kernels/bench_block_verification.py`; `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/.mintignore`; `docs/cards/logos/gigachat.png`; `docs/cards/logos/iquestlab.png`; `docs/cards/logos/perplexity.png` 等 190 个文件
  - other: `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`; `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`; `.agents/skills/ci-test-audit/SKILL.md`; `.agents/skills/ci-test-audit/action-items.md`; `.agents/skills/clean-startup-log/SKILL.md`; `.agents/skills/clean-startup-log/references/noise-sources.md`; `.agents/skills/compute-mamba-ratio/SKILL.md`; `.agents/skills/cookbook-add-model/SKILL.md` 等 596 个文件
  - runtime-model: `.agents/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.agents/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.agents/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile` 等 470 个文件
  - runtime-perf: `.agents/skills/add-jit-kernel/SKILL.md`; `.agents/skills/add-sgl-kernel/SKILL.md`; `.agents/skills/debug-cuda-crash/SKILL.md`; `.agents/skills/debug-distributed-hang/SKILL.md`; `.agents/skills/kernel-organization/SKILL.md`; `.agents/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `.claude/rules/kernel-benchmark.md`; `.claude/skills/add-jit-kernel/SKILL.md` 等 816 个文件
  - tests: `.agents/skills/kl-consistency-test/SKILL.md`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/conftest.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/generator_testlib.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extract_functions.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extracts.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_imports.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_main_single_commit.py` 等 1190 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4975d6490` - Sync/official main daily 20261019 (#560)

- Full hash: `4975d6490ac2c71c2d88c8a86b96a6f7061050ab`
- Date/author: 2026-10-20 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md`, `.agents/skills/processor-model-parity/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.claude/rules/prefer-sgl-eval.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 3006 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/pull_request_template.md`; `.github/scripts/pr-check-comment.cjs` 等 60 个文件
  - docs-bench: `benchmark/hicache/bench_host_memory_migration.py`; `benchmark/kernels/lora_csgmv/bench_csgmv_split_k.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/cards/logos/cloudflare.png`; `docs/cards/logos/reflection.png`; `docs/cookbook/autoregressive/Cloudflare/clef.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 211 个文件
  - other: `.agents/skills/cookbook-add-model/SKILL.md`; `.agents/skills/generate-profile/SKILL.md`; `.agents/skills/processor-model-parity/SKILL.md`; `.claude/rules/prefer-sgl-eval.md`; `.gitignore`; `README.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134` 等 521 个文件
  - runtime-model: `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/ARCHITECTURE.md`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/REFERENCE.md` 等 516 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/README.md`; `python/sglang/kernels/__init__.py`; `python/sglang/kernels/aot/benchmark/bench_dsv4_norm_rope.py`; `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py` 等 711 个文件
  - tests: `.agents/skills/write-sglang-test/SKILL.md`; `docs/scripts/tests/diffusion-builders.test.mjs`; `docs/scripts/tests/wan-animate-2-config.test.mjs`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_peer_bootstrap.rs`; `experimental/sgl-router/tests/component/policies_reorg.rs` 等 987 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5f67ce01c` - Sync/rel 2 main 20261021 dsv4 validated (#576)

- Full hash: `5f67ce01c3ec1894916d16627eaca4959fbe2d90`
- Date/author: 2026-10-21 / YuanYuan
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `docs/internal/rel-2-main-20261020-release-updates.md`, `python/sglang/benchmark/serving.py` 等 321 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`; `docs/internal/rel-2-main-20261020-release-updates.md`
  - other: `.gitignore`; `python/sglang/benchmark/serving.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/exec_.py`; `python/sglang/srt/arg_groups/fields/memory.py`; `python/sglang/srt/arg_groups/fields/schedule.py` 等 56 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vit_utils.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py` 等 26 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py` 等 131 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`; `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/kits/linker_load_failure_kit.py`; `test/manual/hcu/test_kimi_k3_serial_sbo.py` 等 102 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
