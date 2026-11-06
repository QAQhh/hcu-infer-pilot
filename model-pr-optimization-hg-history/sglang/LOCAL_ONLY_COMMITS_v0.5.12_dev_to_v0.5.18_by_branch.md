# SGLang v0.5.12_dev..release/20260825_v0.5.18 分支更新本地独有提交索引

## 范围与口径

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 官方仓库: `https://github.com/sgl-project/sglang.git`
- 官方 refs: 已 fetch 到本地 `refs/remotes/github-official/*`
- 筛选方法: 每个分支更新段内，commit hash 不可从官方 GitHub refs 到达，即记录为本地 fork 独有提交。
- 说明: 合并提交也保留；合并提交没有直接文件 diff 时，`主要涉及` 标记为 `无直接文件变更/merge`。
- 生成日期: 2026-11-03

## 数量汇总

| 分支更新段 | 范围内提交数 | 本地独有提交数 | 其中 merge |
| --- | ---: | ---: | ---: |
| `v0.5.12_dev..v0.5.15.post1_dev` | 2649 | 166 | 50 |
| `v0.5.15.post1_dev..release/20260825_v0.5.18` | 1927 | 382 | 74 |
| 合计 | 4576 | 548 | 124 |

## 分桶分布

| 桶 | 提交数 |
| --- | ---: |
| `deepseek-v3-r1` | 22 |
| `deepseek-v31` | 21 |
| `deepseek-v32` | 22 |
| `deepseek-v4` | 48 |
| `glm45` | 2 |
| `glm46-glm47` | 2 |
| `glm5-glm51` | 11 |
| `gpt-oss` | 1 |
| `hunyuan3-preview` | 10 |
| `kimi` | 25 |
| `mimo-v2-flash` | 4 |
| `minimax` | 21 |
| `mixtral-quark-int4fp8-moe` | 4 |
| `nemotron-super` | 1 |
| `qwen-vlm-omni-asr` | 3 |
| `qwen3-coder` | 16 |
| `qwen3-core` | 17 |
| `qwen3-next` | 1 |
| `qwen35` | 8 |
| `qwen36` | 8 |
| `qwen4-exp` | 11 |
| `shared` | 281 |
| `unclassified` | 122 |

- 同一提交可同时进入多个模型桶，所以各桶之和大于本地独有提交总数。

## 重复检查

- 本次未计算 `git patch-id`（克隆不含文件内容）；仅按「标题相同且文件集相同」检查疑似重复。
- 疑似重复: `5d83cfe85`, `0536e102c`，标题 `[SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs`。索引中均保留。
- 疑似重复: `93cf8edc4`, `e6d4b3378`，标题 `[Addition] deliver one validation doc`。索引中均保留。
- 疑似重复: `7482123c3`, `6c1786bc4`，标题 `fix(hcu): prefer hcusmi for platform detection`。索引中均保留。
- 疑似重复: `de696eab9`, `e6c410259`，标题 `Update quality gate workflow to version 2.0.1`。索引中均保留。
- 疑似重复: `93b801826`, `f2fc4e166`，标题 `Update quality gate workflow to version 2.0.3`。索引中均保留。
- 疑似重复: `c8ba30447`, `50beda6a9`，标题 `Update quality gate workflow to use stable version`。索引中均保留。

## 提交索引

### `v0.5.12_dev..v0.5.15.post1_dev`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | `94659d14a` | SYChen123 | [dsv4] cp support megamoe | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-22 | `5d83cfe85` | RyeYuan | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` | shared |
| 2026-06-22 | `0536e102c` | RyeYuan | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` | shared |
| 2026-06-23 | `0fc998757` | RyeYuan | Merge official main checkpoint C01 | 无直接文件变更/merge | unclassified |
| 2026-06-23 | `571813832` | RyeYuan | Merge official main checkpoint C02 | 无直接文件变更/merge | unclassified |
| 2026-06-24 | `523756bde` | RyeYuan | [docs(dcu)] log C01/C02 conflict ledger update | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-24 | `5b19ad464` | RyeYuan | [fix(deepseek-v4)]: keep DCU on non-HIP attention backend + compressor | `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py` | deepseek-v4 |
| 2026-06-24 | `1b2694156` | RyeYuan | [fix(deepseek-v4)]: remove unused codes and use ScheduleBatch extend_lens/prefix_lens in init_new | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-06-24 | `8303d60f7` | RyeYuan | Merge official main checkpoint C03 | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `c4cc0a73b` | RyeYuan | fix(dsv4): preserve DCU elementwise and topk paths | `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-06-30 | `93cf8edc4` | RyeYuan | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-30 | `810624fbe` | RyeYuan | Merge official main checkpoint C04 | 无直接文件变更/merge | unclassified |
| 2026-06-30 | `f2d0e86d7` | RyeYuan | fix(dsv4): repair DCU sgl-kernel and JIT build | `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py` | deepseek-v4 |
| 2026-06-30 | `3910b3f9d` | RyeYuan | fix(scheduler): restore DCU empty-prefix location | `python/sglang/srt/managers/schedule_batch.py` | shared |
| 2026-06-30 | `ff440b897` | RyeYuan | docs(dcu): record C04 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-06-30 | `08c1fd5a0` | RyeYuan | Merge official main checkpoint C05 | 无直接文件变更/merge | unclassified |
| 2026-07-01 | `e6d4b3378` | RyeYuan | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-01 | `16cff03a2` | RyeYuan | Merge official main checkpoint C06 | 无直接文件变更/merge | unclassified |
| 2026-07-02 | `249a70dbe` | RyeYuan | [Addition] deliver one validation doc and support multi-stream in hip backend | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-02 | `593df5e14` | RyeYuan | Merge official main checkpoint C07 | 无直接文件变更/merge | unclassified |
| 2026-07-03 | `fc241f4ad` | RyeYuan | [BugFix] Sync to official changes to remove first pre-warmup of mHC | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-03 | `00063277c` | RyeYuan | [Addition] deliver one validation doc of C07 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-03 | `01f8caf22` | RyeYuan | Merge official main checkpoint C08 | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `88bb5176c` | RyeYuan | [Addition] deliver one validation doc of C08 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-06 | `2ada58179` | RyeYuan | Merge official main checkpoint C09 | 无直接文件变更/merge | unclassified |
| 2026-07-06 | `fa6b75971` | RyeYuan | [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py` | shared |
| 2026-07-06 | `ad2ff869c` | RyeYuan | [BugFix] Backport partial bugfixes from C10 and also have to assign SGLANG_USE_AITER_AG=0 to ensure accuracy now | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` 等 9 个文件 | deepseek-v4 |
| 2026-07-06 | `a1ed918ae` | RyeYuan | [Addition] deliver one validation doc of C09 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-07 | `5f232f552` | RyeYuan | Merge official main checkpoint C10 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `bfaf180d1` | RyeYuan | [Addition] deliver one validation doc of C10 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `bae695b56` | RyeYuan | Merge official main checkpoints C11-C13 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `b6db54a9a` | RyeYuan | [Addition] deliver one validation doc of C11~C13 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `293fa64f0` | RyeYuan | Merge commit '2ad00faae1f4f413330fbc1241dc2c79f44ac4d4' into sync/official-main-C14-C16-20260616 | 无直接文件变更/merge | unclassified |
| 2026-07-08 | `1cea713a7` | RyeYuan | docs(dcu): record C14-C16 validation block | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-08 | `b452d6bd6` | RyeYuan | docs(dcu): record C14-C16 functional validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `01a6f1b94` | RyeYuan | [Addition] deliver one validation doc of C14~C16 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `15abf620c` | RyeYuan | Merge official SGLang C17-C19 into DCU bootstrap | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `cee45bc55` | RyeYuan | docs(dcu): record C17-C19 validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `4b0fcbd07` | RyeYuan | [Addition] deliver one validation doc of C17~C19 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-09 | `76d14014a` | RyeYuan | Merge official main bootstrap C01-C19 into main | 无直接文件变更/merge | unclassified |
| 2026-07-09 | `d8f3057b3` | RyeYuan | Merge official main catchup 20260623 into DCU main | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `cba9e72cc` | RyeYuan | [BugFix] skip some uncompatibal env setup in hip for DCU | `python/sglang/srt/server_args.py` | shared |
| 2026-07-13 | `48489724d` | RyeYuan | docs(dcu): record 20260623 catch-up runtime status | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-13 | `b9cf8ac56` | RyeYuan | Merge official main catchup 20260625 into DCU main | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `dcd4013b3` | RyeYuan | Merge official SGLang main through 2026-06-29 | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `8c797abd6` | RyeYuan | Record 20260629 DCU runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-13 | `d8ed552da` | RyeYuan | docs(dcu): add 20260629 conflict review | `docs/internal/dcu-main-catchup-20260629-conflict-review.md` | shared |
| 2026-07-13 | `c4de02791` | RyeYuan | Merge official SGLang main through 2026-07-03 | 无直接文件变更/merge | unclassified |
| 2026-07-13 | `6bf9d1872` | RyeYuan | fix(dcu): reconcile DSV4 prewarm and fused Q imports | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-13 | `516a35c40` | RyeYuan | docs(dcu): record 20260703 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `84a8a08ac` | RyeYuan | [BugFix] skip pre-warmup of mHC for DCU and update validation docs | `docs/internal/dcu-main-catchup-20260703-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-07-14 | `f96aaeb79` | RyeYuan | Merge official main catch-up through 20260706 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `b5f9777d2` | RyeYuan | Fix DCU DSV4 hash top-k router dtype | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-07-14 | `e3aa204a0` | RyeYuan | docs(dcu): require catch-up conflict reviews | `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md` | shared |
| 2026-07-14 | `6cd17f3e3` | RyeYuan | Merge official SGLang main through 2026-07-09 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `412d0ef9f` | RyeYuan | docs(dcu): add 20260709 conflict review | `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `c0e8edd74` | RyeYuan | fix(dcu): initialize DeepEP dispatch dtype state | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-07-14 | `6e0a964d1` | yuchenyang | Fix DeepSeek fused RMS quant MoE path | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-14 | `1a2c734e5` | RyeYuan | Merge official main catch-up through 20260710 | 无直接文件变更/merge | unclassified |
| 2026-07-14 | `9d7fbb017` | RyeYuan | docs: add 20260710 conflict review | `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `24894692e` | RyeYuan | fix: use runtime attention TP size in model warmup | `python/sglang/srt/model_executor/model_runner.py` | shared |
| 2026-07-14 | `6630db3cf` | RyeYuan | docs: record 20260710 pure-TP validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `3d77308ea` | RyeYuan | docs: mark 20260710 catch-up validated | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-14 | `3e335fce8` | RyeYuan | docs: correct 20260710 endpoint subject | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `0f6c8298b` | RyeYuan | Revert "Fix DeepSeek fused RMS quant MoE path" | `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-07-15 | `9ec22c5c9` | RyeYuan | Merge sync/official-main-catchup-20260710 into main | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `7fa6d89c3` | RyeYuan | Merge official main catch-up through 20260712 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `baa08af59` | RyeYuan | docs(dcu): add 20260712 conflict review | `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `44f81e8f7` | RyeYuan | docs(dcu): record 20260712 runtime gate status | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `0b30b7c9d` | RyeYuan | docs(dcu): record 20260712 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-15 | `4cc240b90` | RyeYuan | Merge official main catch-up through 20260713 | 无直接文件变更/merge | unclassified |
| 2026-07-15 | `324181561` | RyeYuan | docs(dcu): add 20260713 conflict review | `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` | shared |
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
| 2026-07-17 | `d703c086f` | RyeYuan | [BugFix] Fix the accuracy issues of DeepSeek-V4 in TP/CP/DP/EP | `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/allocator/paged.py` | deepseek-v4 |
| 2026-07-20 | `c43b06722` | tianlinyang77 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 372 个文件 | unclassified |
| 2026-07-20 | `1e2fec228` | tianlinyang77 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, glm45, glm46-glm47, hunyuan3-preview, mimo-v2-flash, minimax, mixtral-quark-int4fp8-moe, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-20 | `358a33714` | tianlinyang77 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-07-20 | `416bbd9b9` | reverie-hub | chore(hcu): complete platform wording cleanup | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `docs/internal/dcu-main-catchup-20260629-conflict-review.md` 等 28 个文件 | mixtral-quark-int4fp8-moe |
| 2026-07-20 | `81e3561ae` | LvJIA-RG | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-07-20 | `811aa027d` | reverie-hub | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` | shared |
| 2026-07-20 | `15a656ea6` | tianlinyang77 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` | shared |
| 2026-07-21 | `e876bb9ff` | RyeYuan | [FEAT] support cp+MegaMoE in prefill w/o cuda-graph | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 5 个文件 | deepseek-v4 |
| 2026-07-21 | `470ae85b5` | RyeYuan | style: apply pre-commit formatting (black/isort/ruff) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` 等 4 个文件 | deepseek-v4 |
| 2026-07-21 | `2d509d387` | lizhigong | Merge pull request #113 from HYGON-AI/v0.5.15.post1_dev_rye_megamoe_cp | 无直接文件变更/merge | unclassified |
| 2026-07-21 | `9864c8451` | reverie-hub | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` | shared |
| 2026-07-21 | `9b86479ac` | tianlinyang77 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` 等 14 个文件 | qwen35, qwen36 |
| 2026-07-21 | `ac56ca009` | reverie-hub | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-22 | `e20e686c7` | tianlinyang77 | merge: sync v0.5.15.post1_dev into HCU port | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `f0d6741cc` | RyeYuan | merge(dcu): forward-port v0.5.12_dev daily 20260722 | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `6e5326678` | lizhigong | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-07-22 | `c32209f6d` | lizhigong | Merge pull request #115 from HYGON-AI/v0.5.15_dev_lzg | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `1f3d470dc` | RyeYuan | merge(dcu): integrate origin/v0.5.15.post1_dev PR#115 into forward-port 20260722 | 无直接文件变更/merge | unclassified |
| 2026-07-22 | `9fc04a7a2` | RyeYuan | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` | shared |
| 2026-07-23 | `599610198` | tianlinyang77 | merge: sync latest v0.5.15.post1_dev into HCU port | 无直接文件变更/merge | unclassified |
| 2026-07-23 | `bee4b423f` | lizhigong | Merge pull request #114 from HYGON-AI/hcu/v0.5.15.post1-port | 无直接文件变更/merge | unclassified |
| 2026-07-24 | `7482123c3` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-27 | `0710e82a0` | Lvjiajia | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-28 | `997e64560` | LvJIA-RG | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 | shared |
| 2026-07-29 | `d42b0a3bf` | RyeYuan | merge(hcu): forward-port v0.5.12_dev daily 20260729 | 无直接文件变更/merge | unclassified |
| 2026-07-29 | `3b4327cd7` | RyeYuan | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` | shared |
| 2026-07-29 | `e18e6b94b` | RyeYuan | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` | shared |
| 2026-07-29 | `25ffedc22` | RyeYuan | fix(hcu): repair forward-port compatibility gaps | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` 等 15 个文件 | deepseek-v4, qwen3-core |
| 2026-07-29 | `111fea82f` | LvJIA-RG | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 36 个文件 | shared |
| 2026-07-29 | `cce4bdd61` | dddddddxl | Merge pull request #148 from HYGON-AI/ci/align-workflows-v0515-0729 | 无直接文件变更/merge | unclassified |
| 2026-07-31 | `02968a96d` | RyeYuan | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 | shared |
| 2026-07-31 | `123e9539e` | RyeYuan | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, hunyuan3-preview, mimo-v2-flash, minimax, mixtral-quark-int4fp8-moe, qwen-vlm-omni-asr, qwen3-coder, qwen3-core, qwen35 |
| 2026-07-31 | `39d691220` | RyeYuan | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` | shared |
| 2026-07-31 | `e7106de94` | RyeYuan | V0.5.15.post1 dev to support dspark on HCU (#142) | `python/sglang/benchmark/dspark_sps_profiler.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py` 等 8 个文件 | deepseek-v4 |
| 2026-08-03 | `286612da4` | Lvjiajia | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `d08093cb4` | Lvjiajia | Merge pull request #158 from HYGON-AI/lvj-repox-patch-1 | 无直接文件变更/merge | unclassified |
| 2026-08-03 | `de696eab9` | Lvjiajia | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `015f6d49a` | RyeYuan | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` | shared |
| 2026-08-03 | `b97d7df6e` | RyeYuan | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` 等 184 个文件 | unclassified |
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
| 2026-08-10 | `d76d3f185` | yuchenyang | Adapt MiniMax-H3 for v0.5.15 | `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py` 等 84 个文件 | minimax |
| 2026-08-10 | `abe7d784d` | lizhigong | Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt | 无直接文件变更/merge | minimax |
| 2026-08-11 | `ad1fea5d7` | dingxinlong | Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci | 无直接文件变更/merge | unclassified |
| 2026-08-11 | `ccbb65acb` | RyeYuan | [HCU][DSpark] Fix DP EP MoE fallback routing | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-12 | `2083c069f` | RyeYuan | fix lint: apply pre-commit fixes to the EP MoE fallback change | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-12 | `856b425b8` | YuanYuan | Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `fb7f11956` | LvJIA-RG | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 | shared |
| 2026-08-12 | `74e12e1e8` | lizhigong | Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515 | 无直接文件变更/merge | unclassified |
| 2026-08-13 | `54e3ed50f` | RyeYuan | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` | shared |
| 2026-08-13 | `18e167b73` | RyeYuan | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` | shared |
| 2026-08-13 | `5e2ba659e` | RyeYuan | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` | shared |
| 2026-08-13 | `97a1938e2` | YuanYuan | Merge pull request #192 from HYGON-AI/rye_dspark_bugfix | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `93b801826` | Lvjiajia | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` | shared |
| 2026-09-21 | `c8ba30447` | Lvjiajia | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` | shared |

### `v0.5.15.post1_dev..release/20260825_v0.5.18`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-21 | `4859ed3b8` | RyeYuan | Merge official main daily 20260721 | 无直接文件变更/merge | unclassified |
| 2026-07-21 | `a596be0dc` | RyeYuan | [BugFix] Fix DeepSeek-V4 pure-TP startup after official main daily 20260721 merge | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/utils/compile.py` 等 7 个文件 | deepseek-v4 |
| 2026-07-24 | `b781224d4` | LvJIA-RG | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 466 个文件 | unclassified |
| 2026-07-24 | `cb01580d4` | lizhigong | Merge pull request #124 from HYGON-AI/sanitize-hcu-runtime-log-audit-20260723 | 无直接文件变更/merge | unclassified |
| 2026-07-24 | `6c1786bc4` | LvJIA-RG | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | shared |
| 2026-07-27 | `93c56ce71` | Lvjiajia | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` | shared |
| 2026-07-27 | `49764eb37` | Lvjiajia | Merge pull request #131 from HYGON-AI/lvjia-repoguy-patch-1 | 无直接文件变更/merge | unclassified |
| 2026-07-28 | `77939d9a5` | LvJIA-RG | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-07-29 | `ba31df0c0` | RyeYuan | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` 等 1924 个文件 | unclassified |
| 2026-07-29 | `b2f0b830c` | LvJIA-RG | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 39 个文件 | shared |
| 2026-07-29 | `3bd903cb2` | dddddddxl | Merge pull request #147 from HYGON-AI/ci/align-workflows-main-0729 | 无直接文件变更/merge | unclassified |
| 2026-07-30 | `785804bfb` | shiqiang | fix triton moe path but accuracy fail | `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/mxfp4.py` | kimi |
| 2026-07-31 | `a0cc11498` | RyeYuan | [BugFix] fix the mxfp4 triton accuracy issues | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | shared |
| 2026-08-03 | `4d3aaf6af` | Lvjiajia | Update quality gate workflow for versioning and concurrency | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-03 | `e6c410259` | Lvjiajia | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` | shared |
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
| 2026-08-04 | `8160ebe53` | RyeYuan | fix(hcu): retain PD decode adapter callbacks | `python/sglang/srt/managers/scheduler_components/dp_attn.py` | shared |
| 2026-08-04 | `31576cba7` | shiqiang | feat: integrate hcu_mla and causal_conv1d modules | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` 等 5 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-08-04 | `a7931170f` | shiqiang | sytnx fix | `python/sglang/srt/server_args.py` | shared |
| 2026-08-05 | `a0840f493` | RyeYuan | [BugFix] recall hcu changes in pre_mhc changes to fix the accuracy issues | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-08-06 | `1672d9e47` | lizhigong | Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge | unclassified |
| 2026-08-06 | `a6ce82576` | shiqiang | feat: support flash kda, hcu triton kda and hcu triton attn residual | `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py` 等 8 个文件 | kimi |
| 2026-08-07 | `eda349619` | RyeYuan | chore(hcu): anchor daily sync base to official edc0e5489 (no content change) | 无直接文件变更/merge | unclassified |
| 2026-08-07 | `12ba645c7` | shiqiang | feat: support WFP4A16 hipc moe for kimi-k3 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | kimi |
| 2026-08-07 | `6e2576a74` | shiqiang | fix: route hcu_mla prefill through the chunked prefix cache path | `python/sglang/srt/server_args.py` | shared |
| 2026-08-10 | `80e01615e` | RyeYuan | Sync/official main daily 20260807 | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `37b7742e7` | RyeYuan | Sync/official main 20260810 (v0.5.17) | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `6f86e904d` | lizhigong | Merge pull request #179 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge | unclassified |
| 2026-08-10 | `e3a9d595c` | RyeYuan | [HCU][DSpark] Fix sampling parameter updates after graph capture | `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` | shared |
| 2026-08-10 | `4a6fbed98` | RyeYuan | [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config | `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-08-10 | `5fd89c728` | RyeYuan | [BugFix] fix the inference tensor graph replay issues in MTP mode | `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` | shared |
| 2026-08-10 | `b36730b41` | RyeYuan | fix lint: apply pre-commit fixes to the mHC EAGLE changes | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py` | shared |
| 2026-08-10 | `8f7a660e5` | YuanYuan | Merge pull request #183 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge | unclassified |
| 2026-08-11 | `8084b5cac` | zhaosong1 | merge: fix kimi-k3 merge conflict | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, kimi |
| 2026-08-11 | `9c60fd0fd` | shiqiang | fix: fix situ activation jit error | `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh` 等 4 个文件 | kimi |
| 2026-08-11 | `4a004a87b` | shiqiang | fix: route KDA packed decode to the HCU operator kernel | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` | shared |
| 2026-08-12 | `5daa79af7` | RyeYuan | merge(hcu): forward-port v0.5.15.post1_dev through 20260811 | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `9b76db90d` | YuanYuan | Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811 | 无直接文件变更/merge | unclassified |
| 2026-08-12 | `7d3e54a20` | shiqiang | feat: support aiter gdn fwd op | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py` | shared |
| 2026-08-12 | `9287931ed` | shiqiang | feat: support triton moe wfp4 afp8 tc | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | shared |
| 2026-08-13 | `00468ade3` | shiqiang | perf: route K3 attention-residual aggregation to the HCU kernel on large batches | `python/sglang/srt/layers/attn_residual.py` | kimi |
| 2026-08-13 | `39dc297c2` | shiqiang | feat: optimize Triton MXFP4 W4A8 scaling | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | shared |
| 2026-08-13 | `38eea340e` | shiqiang | fix: correct Kimi-K3 INT4 MoE accuracy via slimquant quant Triton W4A16 path | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/server_args.py` | kimi |
| 2026-08-13 | `0d55c3dcc` | shiqiang | fix: remove debug info | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-13 | `c11fc7982` | shiqiang | feat: add INT4 MoE W4A8 int8 tensor-core path for slimquant HCU | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-13 | `83ab58f2e` | maxiaobetter | fix(quant): 修复 HCU W8A8 hipBLASLt 权重布局 | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_w8a8_int8_hcu_layout.py` | shared |
| 2026-08-13 | `832ed3b14` | maxiaobetter | feat(moe): 增加 locality-fair static dispatch 策略 | `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/eplb/test_compute_logical_to_rank_dispatch_physical_map.py` | shared |
| 2026-08-13 | `143df0a3e` | maxiaobetter | fix(attention): 恢复 HCU DSA FlashMLA backend 路由 | `python/sglang/srt/layers/attention/dsa/flashmla_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_flashmla_backend.py` | shared |
| 2026-08-13 | `ccfc91c5d` | maxiaobetter | fix(attention): 保留 IFB/MTP 的 DSA effective forward mode | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py` 等 5 个文件 | shared |
| 2026-08-13 | `75cc77fa2` | maxiaobetter | fix(attention): 修复 IFB/MTP FlashMLA padded rows | `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_forward_batch_utils.py` | shared |
| 2026-08-13 | `902de5d3d` | maxiaobetter | fix(attention): 修复 HCU DSA FlashMLA metadata replay | `python/sglang/srt/layers/attention/dsa/flashmla_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_flashmla_backend.py` | shared |
| 2026-08-13 | `18b106418` | maxiaobetter | feat(attention): 恢复 HCU LightOp DSA indexer 路径 | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/paged_mqa_logits_backend.py`, `python/sglang/srt/server_args.py` 等 4 个文件 | shared |
| 2026-08-13 | `0dd9ab211` | maxiaobetter | fix(attention): 按 head_dim 归一化 DSA indexer | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/unit/layers/attention/dsa/test_hcu_indexer.py` | shared |
| 2026-08-13 | `43f1a8b2a` | maxiaobetter | fix(attention): 启用 HCU DSA MTP draft-extend CUDA graph | `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_graph_support.py` | shared |
| 2026-08-14 | `1c349c31f` | RyeYuan | merge(hcu): forward-port v0.5.15.post1_dev through 20260813 | 无直接文件变更/merge | unclassified |
| 2026-08-14 | `fa309a1e1` | RyeYuan | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | shared |
| 2026-08-14 | `288ab2445` | shiqiang | fix: fix submit_nogds_read failed when use fastsafetensors load | `python/sglang/srt/model_loader/weight_utils.py` | shared |
| 2026-08-14 | `1535858ca` | shiqiang | fix: refactor mxfp4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 | shared |
| 2026-08-15 | `68d20891f` | shiqiang | fix: refactor kimi k3 int4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 | kimi |
| 2026-08-15 | `3190629e7` | shiqiang | fix: correct blockshape is none when use aiter moe for channel w4a8 model | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-17 | `d95af36e1` | YuanYuan | Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813 | 无直接文件变更/merge | unclassified |
| 2026-08-17 | `9f4368f10` | RyeYuan | merge(hcu): backport official main through 20260817 (92b1d382c7) | 无直接文件变更/merge | unclassified |
| 2026-08-17 | `9bbf3799d` | RyeYuan | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` | shared |
| 2026-08-17 | `d20a4750f` | YuanYuan | Merge pull request #208 from HYGON-AI/backport/official-main-20260817 | 无直接文件变更/merge | unclassified |
| 2026-08-18 | `b0dc28040` | dingxinlong | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` 等 9 个文件 | shared |
| 2026-08-18 | `38cdca36f` | shiqiang | feat: support w4a8 hipc moe for k3 int4_w4a16 model | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | kimi |
| 2026-08-18 | `e3a192d66` | shiqiang | feat: update kda default value and support boltops chunk delta rule | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py` 等 4 个文件 | shared |
| 2026-08-19 | `ef56737fc` | shiqiang | fix: update w4a8 moe default backend | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-19 | `c4212e944` | WuFan | 适配kimi-k3-w4a8-huawei | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py` 等 17 个文件 | kimi |
| 2026-08-19 | `45d26d754` | maxiaobetter | perf(kernel): add HCU MLA query concat kernel | `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu` 等 7 个文件 | shared |
| 2026-08-19 | `1653683bd` | maxiaobetter | perf(hcu): port sparse page MQA with mask TopK to DSA | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py` 等 5 个文件 | shared |
| 2026-08-19 | `94bacd49a` | maxiaobetter | perf(hcu): reuse sorted DSA TopK indices | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-08-19 | `f475e6569` | maxiaobetter | perf(dsa): compact shared index-K cache | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py` 等 8 个文件 | shared |
| 2026-08-19 | `a306b8023` | maxiaobetter | feat(hcu): port gfx936 INT8 DSA index cache | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` 等 7 个文件 | shared |
| 2026-08-19 | `f41bb0f58` | maxiaobetter | feat(hcu): support INT8 DSA cache in Mooncake PD | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py` 等 8 个文件 | shared |
| 2026-08-19 | `3d12a3ce1` | maxiaobetter | fix(hcu): stabilize DSA MTP metadata replay | `python/sglang/kernels/jit/csrc/elementwise/fused_metadata_copy.cuh`, `python/sglang/kernels/ops/attention/fused_metadata_copy.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py` 等 4 个文件 | shared |
| 2026-08-19 | `51e53affe` | maxiaobetter | perf(hcu): reuse DSA target verify graph metadata | `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py` | shared |
| 2026-08-19 | `873465654` | maxiaobetter | fix(dsa): correct compact index cache handling | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` 等 10 个文件 | shared |
| 2026-08-19 | `6a51f2a38` | maxiaobetter | fix(hcu): register SlimQuant W4A8 Marlin quantization | `python/sglang/srt/server_args.py` | shared |
| 2026-08-19 | `8a11867b1` | maxiaobetter | feat(hcu): extend DSA LayerSplit for PP and HiCache | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 11 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-08-19 | `0cf9a653e` | maxiaobetter | fix(glm5.2): restore raw DSA config fields | `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers.py` | glm5-glm51 |
| 2026-08-19 | `afe5219d0` | maxiaobetter | fix(scheduler): use parallel state for PD decode sync | `python/sglang/srt/managers/scheduler.py` | shared |
| 2026-08-19 | `0d243f4f1` | maxiaobetter | fix(hcu): restore async metadata copies and padded dispatch | `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/moe/test_topk_padded_region.py` | shared |
| 2026-08-19 | `ed017ea38` | maxiaobetter | fix(hcu): use LayerSplit scratch for fused index writes | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/index_key_cache.py` 等 4 个文件 | shared |
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
| 2026-08-20 | `a6a8e0d5d` | shiqiang | fix: read MXFP4 group_size from model config instead of hardcoding 32 | `python/sglang/srt/layers/quantization/mxfp4.py` | shared |
| 2026-08-20 | `6de39e28a` | shiqiang | refactor(hcu): replace vendored KDA kernels with boltops | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py` 等 8 个文件 | kimi |
| 2026-08-20 | `650a58304` | maxiaobetter | fix(hcu): skip padded tokens for legacy DeepGEMM MoE | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-08-20 | `b001a8d21` | maxiaobetter | perf(hcu): reduce TopK and DSA replay overhead | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` | shared |
| 2026-08-20 | `dcbfd4230` | maxiaobetter | perf(hcu): avoid redundant padded weight mask | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-08-20 | `9e3dd4834` | maxiaobetter | perf(hcu): fuse DeepEP topk id cast | `python/sglang/srt/layers/moe/topk.py` | shared |
| 2026-08-20 | `5aedbbcc9` | maxiaobetter | perf(hcu): overlap LayerSplit index cache broadcast | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 5 个文件 | shared |
| 2026-08-24 | `0d49fbb93` | lizhigong | Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev | 无直接文件变更/merge | minimax |
| 2026-08-24 | `2e8f1408b` | lizhigong | Merge pull request #214 from Crowder13/main | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `261b8627f` | RyeYuan | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` | shared |
| 2026-08-24 | `238c81b4c` | wufan | 优化因数据拷贝导致的性能问题 | `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`, `python/sglang/srt/hardware_backend/npu/moe/matmul.py` | shared |
| 2026-08-24 | `6e2f11552` | luosyx | fix(hcu): align speculative index cache lengths | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` | shared |
| 2026-08-24 | `59fb95973` | luosyx | feat(hcu): add INT8 indexer cache for DeepSeek-V4 | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py` 等 6 个文件 | deepseek-v4 |
| 2026-08-25 | `16d7caa10` | RyeYuan | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 1857 个文件 | unclassified |
| 2026-08-25 | `dd41b1f06` | YuanYuan | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `c40703e6b` | RyeYuan | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` 等 5 个文件 | shared |
| 2026-08-25 | `7b3548f97` | RyeYuan | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` 等 48 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, qwen-vlm-omni-asr, qwen35 |
| 2026-08-25 | `59213c7e4` | RyeYuan | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` | shared |
| 2026-08-25 | `69c73a178` | dddddddxl | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `97aa7a298` | Lvjiajia | Merge pull request #224 from dddddddxl/hcu/fork-pr-target | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `f2fc4e166` | Lvjiajia | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` | shared |
| 2026-08-25 | `4eacd3c36` | Lvjiajia | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `3e6aaf09d` | dddddddxl | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `8ba0c9376` | Lvjiajia | Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `7481b1f54` | Lvjiajia | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `a3cfa2a97` | Lvjiajia | Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824 | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `6a4a61efb` | dddddddxl | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-25 | `688659c15` | Lvjiajia | Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership | 无直接文件变更/merge | unclassified |
| 2026-08-25 | `e04856c1d` | Codex | fix(minimax-h3): allow HCU full-loop denoise | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` | minimax |
| 2026-08-25 | `ce113101c` | zhangpc3 | fix(minimax-h3): avoid sharing refined prompts with CacheDiT | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` | minimax |
| 2026-08-25 | `b921d697a` | shiqiang | feat: support contiguous and masked hipc kernel for deepep normal and low_latency mode | `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 4 个文件 | shared |
| 2026-08-25 | `88f910e94` | shiqiang | fix: preserve release fuse_swiglu with source Kimi MoE | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | kimi |
| 2026-08-25 | `7164456e7` | shiqiang | fix: preserve target lightop int8 quantization | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | shared |
| 2026-08-26 | `8b50a269f` | zhangyh15 | bugfix router路径不对 | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `530d6363b` | YuanYuan | Merge pull request #231 from s1mplezpc/0518-minimaxh3-dev | 无直接文件变更/merge | minimax |
| 2026-08-26 | `d5882c133` | zhangyh15 | [feature] 发包流水支持手动触发,手动触发不上传pypi | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `726db6820` | YuanYuan | Merge all deepseek-v4 updated features including DSpark and more into v0.5.18 release. | `docs/internal/README_BF16_FLASHMLA.md`, `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/arg_groups/speculative_hook.py` 等 44 个文件 | deepseek-v4 |
| 2026-08-26 | `038467e8b` | shiqiang | fix: fix lightop moe align vimfault | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-08-26 | `32f86c628` | liuzj512 | fix(hy3): align LightOp routed scaling factor handling | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-08-26 | `502516539` | maxiaobetter | style: format GLM 5.2 forward-port files | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/utils/hf_transformers/config.py` 等 5 个文件 | glm5-glm51 |
| 2026-08-26 | `6ba4328e9` | zhangyh15 | ci(hcu): release 发包流水触发方式改为 push | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `89d8ac7b1` | lizhigong | Merge pull request #233 from Crowder13/release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `c063dda9a` | lizhigong | Merge pull request #234 from liuzj512/fix/hy3-lightop-rsf | 无直接文件变更/merge | hunyuan3-preview |
| 2026-08-26 | `93c930c6f` | shiqiang | fix: fix aiter shuffle func not found | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-26 | `d8db8bb3e` | maxiaobetter | fix(dsa): complete LayerSplit HiCache paths | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` 等 11 个文件 | shared |
| 2026-08-26 | `5efbf9c3b` | zhangyh15 | debug: gateway 构建加日志排查 wheel 路径，临时只编 router | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `5c6fb2e29` | lizhigong | Merge pull request #236 from daishiqiang123/20260825_v0.5.18_kimi_k3 | 无直接文件变更/merge | kimi |
| 2026-08-26 | `0669c1842` | maxiaobetter | fix(quantization): defer SlimQuant MoE backend resolution | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-26 | `700dd657d` | lizhigong | Merge pull request #237 from HYGON-AI/zyh/test-release-workflow | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `63610c2ff` | dddddddxl | ci(hcu): enable checks for release branches | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/quality-gate.yml` | shared |
| 2026-08-26 | `d39c77a23` | dddddddxl | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-26 | `5f2c97ef7` | Lvjiajia | Merge pull request #239 from dddddddxl/hcu/enable-v0518-ci | 无直接文件变更/merge | unclassified |
| 2026-08-26 | `1db0108f3` | Crowder13 | [CI bugfix]工作目录没有清理导致权限变root (#240) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` | shared |
| 2026-08-26 | `b57ecddf2` | aivictor0901-tech | fix(moe): fix W4A8 DeepEP accuracy with SwiGLU clamp | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-08-27 | `f292fa0e3` | dddddddxl | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-08-27 | `779f1bea2` | Crowder13 | [bugfix] CI打包版本更新为0.5.18 (#244) | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-08-27 | `91856a154` | Lvjiajia | Merge pull request #245 from dddddddxl/hcu/fix-safe-directory-v0518 | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `1679428e0` | Codex | [FEAT][DSpark] 1. Support the p/d radix cache w/ DSpark by PR:https://github.com/sgl-project/sglang/pull/31097; 2. SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & --disaggregation-decode-enable-radix-cache should be enable in D | `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` 等 14 个文件 | shared |
| 2026-08-27 | `d8a06d0c2` | lizhigong | Merge pull request #247 from RyeYuan/feat/rye_20260827_deepseek-v4_dspark_radix-cache | 无直接文件变更/merge | deepseek-v4 |
| 2026-08-27 | `6721affc2` | Crowder13 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` | shared |
| 2026-08-27 | `d92a60a7f` | lizhigong | Merge pull request #250 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-27 | `561186ca9` | jiafei96 | kimi-k3 dspark support (#249) | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py` 等 4 个文件 | kimi |
| 2026-08-27 | `cff97568f` | luosyx | Merge feature/glm52-forward-port-v0.5.18 into release/20260825_v0.5.18 | 无直接文件变更/merge | glm5-glm51 |
| 2026-08-27 | `dc1b54b42` | luosyx | fix(hcu): tolerate deepgemm without contiguous HIPC kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-08-27 | `b065e598a` | luosyx | fix(hcu): restore slimquant backend logger | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-08-27 | `962ab75e4` | luosyx | fix(hcu): default to compatible masked W4A8 kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-08-27 | `2ec9f04ae` | WuFan | [feat]: use aiter moe for kimi-k3-w4a8-huawei | `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py` | kimi |
| 2026-08-27 | `253e326c3` | luosyx | fix(disagg): avoid duplicate KV transfer in worker | `python/sglang/srt/disaggregation/mooncake/conn.py` | shared |
| 2026-08-27 | `42185e316` | aivictor0901-tech | fix(moe): apply SwiGLU clamp in contiguous W4A8 path | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-08-27 | `e769cde2e` | Crowder13 | hcu ci: docker 镜像 daily 定时构建, router 改用 vendored openssl, 补装 flash_kda (#252) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 | shared |
| 2026-08-28 | `5f314b004` | aivictor0901-tech | fix(dspark): transfer draft KV from PD prefill | `python/sglang/srt/speculative/dspark_components/dspark_disaggregation.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` | shared |
| 2026-08-28 | `3cf589201` | lizhigong | Merge pull request #253 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `8a65f5ecd` | wufan | Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `b4b3aaee6` | wufan | Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `52cddf2fa` | wufan | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `45c5fad8d` | wufan | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `1cac982c2` | wufan | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `c16848ebe` | lizhigong | Merge pull request #251 from wufan-ToBeWater/release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-28 | `72dac21ce` | Crowder13 | [bugfix] torchaudio版本装的不对 (#257) | `docker/hcu.Dockerfile` | unclassified |
| 2026-08-28 | `31a159567` | shiqiang | fix: use the model's MoE topk for DeepEP RDMA buffer sizing | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-08-28 | `11852ed1c` | lizhigong | Merge pull request #256 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | 无直接文件变更/merge | glm5-glm51 |
| 2026-08-28 | `845f99085` | luosyx | fix(spec): handle zero-token verify results | `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` | shared |
| 2026-08-28 | `c3846f222` | luosyx | perf(hcu): consume INT8 DSA index cache directly | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` | shared |
| 2026-08-29 | `ea6b50308` | lizhigong | Merge pull request #260 from daishiqiang123/0.5.18_kimi_deepep_fix | 无直接文件变更/merge | kimi |
| 2026-08-29 | `1b8d95c85` | lizhigong | Merge pull request #258 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge | unclassified |
| 2026-08-29 | `bf037e528` | shangxl | fix(hicache): synchronize L3 prefetch across PP ranks | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hicache_storage.py` 等 11 个文件 | shared |
| 2026-08-31 | `3a160688a` | lizhigong | Merge pull request #262 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | 无直接文件变更/merge | glm5-glm51 |
| 2026-08-31 | `2d4eb83cc` | lizhigong | Merge pull request #261 from xinleishang/fix/20260829_v0.5.18_hicache_pp | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `bf9245607` | dddddddxl | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` | shared |
| 2026-08-31 | `6378905dc` | Lvjiajia | Merge pull request #270 from dddddddxl/hcu/remove-amd-pr-state-v0518 | 无直接文件变更/merge | unclassified |
| 2026-08-31 | `75a242b3a` | xingjinliang | fix(attention): running Qwen3-0.6B dismatch shape of one step off policy | `python/sglang/srt/layers/attention/flashattention_backend.py` | qwen3-coder, qwen3-core |
| 2026-08-31 | `84a65ccdd` | lizhigong | Merge pull request #271 from xingjinliang/fix/dismatch-shape-of-one-step-off-policy | 无直接文件变更/merge | unclassified |
| 2026-09-01 | `ddbbccde8` | JingLee | feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274) | `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 32 个文件 | deepseek-v4, kimi |
| 2026-09-01 | `685051c47` | YuanYuan | [bugfix] removed the http warning info in the skip-warmup mode (#276) | `python/sglang/srt/entrypoints/http_server.py` | shared |
| 2026-09-01 | `867eeada1` | chaoyujiang | fix: gracefully handle unsupported KV cache schemes (#268) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` | shared |
| 2026-09-01 | `c18c8d4bb` | Yongqiang Duan | compressor 通信优化 RLC（all-to-all + 本地压缩 + all-gather） (#275) | `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py` 等 8 个文件 | deepseek-v4 |
| 2026-09-01 | `8ae13700d` | GarrySnail | fix(hcu): port PD disaggregation accuracy fix to v0.5.18 release (#266) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` 等 5 个文件 | shared |
| 2026-09-01 | `1316e9887` | lipenghui | fix(hcu): enable W4A8 DeepEP aiter path and FlashMLA workspace reuse (#265) | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | deepseek-v4 |
| 2026-09-02 | `6614bebc7` | lizhigong | feat(hcu): add BHSD KV-cache support while preserving legacy HCU FA (#282) | `docker/hcu.Dockerfile`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` 等 11 个文件 | shared |
| 2026-09-02 | `4fea017b1` | maxiaobetter | fix(hcu): sample linear MTP target verification (#280) | `python/sglang/srt/speculative/eagle_utils.py` | shared |
| 2026-09-02 | `0e2a6e743` | Wenbo Zhu | Feat/bolt recompute w u (#278) | `python/sglang/kernels/ops/attention/fla/wy_fast.py` | shared |
| 2026-09-02 | `556337109` | wufan | [feat]:用lightop的gemm_w8a8_smooth代替triton实现，提升性能 (#279) | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` 等 4 个文件 | shared |
| 2026-09-02 | `0ce4bc716` | dingxinlong | [CI] Use v0.5.18 HCU image and update model paths (#287) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md` 等 12 个文件 | shared |
| 2026-09-02 | `f5a24dc84` | Crowder13 | [FEATURE]0.5.18镜像新增安装nixl (#283) | `docker/hcu.Dockerfile` | unclassified |
| 2026-09-02 | `3b678f293` | Crowder13 | [BUGFIX] HCU环境不需要依赖flashinfer (#289) | `python/pyproject_hcu.toml` | shared |
| 2026-09-03 | `ab91a15c8` | YuanYuan | [bugfix] 1.fix the accuracy issue in Decode radix-cache enable due to… (#291) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/common.py` | shared |
| 2026-09-03 | `aa89102b1` | liuzj512 | fix(hy3): align MoE forward context with current API (#292) | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-09-03 | `2a1b589b3` | lizhigong | fix(hcu): support BSHD multi-batch varlen attention and PD disaggregation (#288) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` | shared |
| 2026-09-03 | `f8bfbc60f` | GarrySnail | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` 等 100 个文件 | qwen-vlm-omni-asr, qwen3-coder, qwen3-core, qwen35, qwen4-exp |
| 2026-09-03 | `b0f501598` | YuanYuan | [BugFix] fix the bug that certain chat/completion in DSpark goes to C… (#294) | `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py` | shared |
| 2026-09-03 | `f656a2ed2` | YuanYuan | [BugFix] fix the bug by removing old monkey patch of mhc (#296) | `python/sglang/kernels/ops/layernorm/mhc.py` | shared |
| 2026-09-03 | `2b855b5be` | dingxinlong | ci(hcu): align llguidance and model asset paths (#300) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` | shared |
| 2026-09-03 | `20c5f927f` | YuanYuan | [BugFix] Remove the dependency of prefill radix-cache with decode-pre… (#302) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py` 等 5 个文件 | shared |
| 2026-09-04 | `9153913d6` | Wenbo Zhu | fix(speculative): remove unsupported server args (#304) | `python/sglang/srt/layers/attention/flashattention_backend.py` | shared |
| 2026-09-04 | `c2544d8ae` | Jane | fix(hcu): repair two upstream-refactor call-site regressions (#303) | `python/sglang/srt/models/hunyuan_v3.py` | hunyuan3-preview |
| 2026-09-04 | `71117e8d9` | GarrySnail | feat(hcu): qwen38 flash next int8 w8a8 support (#310) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` | qwen3-coder, qwen3-core |
| 2026-09-04 | `f35668e41` | JingLee | [perf] add opt-in LightOp KV allocation kernel (#307) | `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/paged.py` | shared |
| 2026-09-04 | `4c9d666cd` | daishiqiang123 | fix: fix deepep and dspark conflict (#306) | `python/sglang/srt/arg_groups/speculative_hook.py` | shared |
| 2026-09-04 | `44b7bc846` | YuanYuan | [BugFix] support the MegaMoE func in DSpark model (#309) | `python/sglang/srt/layers/moe/mega_moe.py` | shared |
| 2026-09-04 | `ff5ffaa1a` | GarrySnail | fix(hcu): keep DeepSeek W4A8 Linear quantized while Qwen3.8 uses expe… (#312) | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | qwen3-coder, qwen3-core |
| 2026-09-07 | `a12f08de7` | Jane | Hy3 support sp ep (#311) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 9 个文件 | hunyuan3-preview |
| 2026-09-07 | `3bc09034b` | chaoyujiang | feat(bench): add --gsp-input-ids to skip server tokenization (#315) | `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` | shared |
| 2026-09-07 | `cdea7a5db` | Wenbo Zhu | fix(hcu): use available RMSNorm kernel op (#321) | `python/sglang/srt/layers/layernorm.py` | shared |
| 2026-09-07 | `ba2dec637` | lzb16 | fix(fst): reclaim device cache after each weight batch (#322) | `python/sglang/srt/model_loader/weight_utils.py` | shared |
| 2026-09-07 | `4c367dbd5` | JingLee | feat(dsv4,hcu): support BF16/FP8 and INT8/INT8 indexer paths on gfx936 (#323) | `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/kernels/ops/attention/dsv4/__init__.py` 等 8 个文件 | deepseek-v4 |
| 2026-09-07 | `cd8f78f01` | maxiaobetter | fix(hcu): include MLA absorb q kernel in HIP build (#293) |  | unclassified |
| 2026-09-08 | `056b21d82` | daishiqiang123 | opt: optimize situ_quant op form lightop lib (#324) | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-09-08 | `c338e5fd0` | JingLee | perf(dsv4): optimize EP gather, paged K-cache, and mHC CP split (#327) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-09-08 | `47b97c0f7` | GarrySnail | fix(hcu): avoid gfx936 QSA LDS overflow (#326) | `python/sglang/srt/layers/attention/qsa/sparse_attn.py` | shared |
| 2026-09-08 | `700649f36` | chenyuege | 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` 等 5 个文件 | qwen3-coder, qwen3-core, qwen36 |
| 2026-09-08 | `57beb6b4a` | lizhigong | ci(hcu): align PR wheel version with release 0.5.18 (#295) | `.github/workflows/release-pr-hcu.yml`, `README_HCU.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py` 等 9 个文件 | shared |
| 2026-09-09 | `e2c65d880` | JingLee | refactor(dsv4): use categorized LightOp mHC API (#332) | `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-09-09 | `e6540308c` | lizhigong | fix bug: Refactor is_fp8_fnuz function for clarity | `python/sglang/kernels/ops/quantization/fp8_kernel.py` | shared |
| 2026-09-09 | `b10bb8c6e` | YuanYuan | [FEAT] support the dspark megamoe-int4 by packing signed-int4 to int8 (#333) | `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py` 等 5 个文件 | shared |
| 2026-09-10 | `6d5931922` | lizhigong | test(hcu): derive FP8 quant reference bounds from the output dtype (#337) | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` | shared |
| 2026-09-10 | `551a71d4d` | liuzj512 | Feature/hy4 ihc tilelang 5commits (#336) | `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh` 等 25 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-09-10 | `ebe9c77f2` | Crowder13 | [FEATURE]同步编译python3.10和python3.12, 上传whl包后记录信息至dashub (#338) | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-09-10 | `a494caa1e` | Yongqiang Duan | perf(hcu): use AITER IPC collectives for DP TP-MoE (#340) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py` | shared |
| 2026-09-10 | `4cdd9d36e` | wufan | Release/20260825 v0.5.18 (#339) | `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` | shared |
| 2026-09-11 | `4603df038` | chenyuege | [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341) | `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` 等 5 个文件 | qwen3-coder, qwen3-core, qwen36 |
| 2026-09-11 | `cb50fb561` | daishiqiang123 | feat: support mimo v2 flash channel fp8 for 5.18 (#343) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py` | mimo-v2-flash |
| 2026-09-11 | `77ba00139` | daishiqiang123 | fix: fix pd fake prefill mode and attn_tp_size bug (#345) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py` | shared |
| 2026-09-12 | `fa95ae084` | daishiqiang123 | fix and opt: fix dspark eagle error and optimize attn tp comm from ai… (#342) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py` | shared |
| 2026-09-12 | `050129f5b` | chenyuege | [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` 等 6 个文件 | qwen3-coder, qwen3-core, qwen36 |
| 2026-09-12 | `44d9bdc2e` | GarrySnail | feat(qwen3_8): support AITER EP and INT8 PLE offload (#350) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` 等 9 个文件 | qwen3-coder, qwen3-core, qwen4-exp |
| 2026-09-12 | `647229c6e` | dingxinlong | ci(hcu): pin v0.5.18 image fallback and shared eval wheels (#348) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` | shared |
| 2026-09-14 | `4af5b4974` | daishiqiang123 | Mimo v2 pro update and bug fix (#354) | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/mimo_v2_nextn.py` | mimo-v2-flash |
| 2026-09-14 | `4a7532fef` | chenyuege | fix(hcu): keep DFLASH FP8 sliding attention on native FlashAttention (#356) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_native_swa.py`, `test/manual/test_hcu_native_swa.py` | shared |
| 2026-09-14 | `feff664df` | liuzj512 | Hy3 sp ep lightop clean (#355) | `python/sglang/srt/layers/moe/utils.py` | hunyuan3-preview |
| 2026-09-14 | `74ee9054e` | dingxinlong | ci(hcu): fix v0.5.18 PR runtime consistency (#363) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/sampling/test_pytorch_sampling_backend.py` | shared |
| 2026-09-14 | `f2379b09c` | Jane | feat:Hy3 support sp ep (#360) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` 等 5 个文件 | hunyuan3-preview |
| 2026-09-14 | `5077850b7` | jiafei96 | support fabric aiter custom allreduce (#361) | `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py` 等 5 个文件 | shared |
| 2026-09-14 | `5817f8359` | GarrySnail | fix(qwen4): correct INT8 PLE dequant on GPU path and enable AITER EP offload (#365) | `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/qwen4_exp.py` | qwen4-exp |
| 2026-09-14 | `72df69c80` | Crowder13 | [BUGFIX]缺少token声明导致打包信息无法推送至Dashub (#366) | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-09-15 | `86cdce034` | dingxinlong | ci(hcu): align v0.5.18 wheel builds with torch 2.11 (#368) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` | shared |
| 2026-09-15 | `45b20a85c` | Wenbo Zhu | Fix ValueError: Add type annotations to fuse_situ_mul_quant_ep (#369) | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-09-15 | `7c7da44a7` | dingxinlong | ci(hcu): fix stale v0.5.18 PR test paths (#370) | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-09-15 | `35d915ef2` | Fafap131 | feat: support hy4 cp (#358) | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/hunyuan_v4.py` | shared |
| 2026-09-15 | `0f88700ac` | xinleishang | feat(mem-cache): support direct L3 external linker cache without test file (#373) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` 等 31 个文件 | shared |
| 2026-09-15 | `37f23f55a` | Yongqiang Duan | perf(dsv4): auto-dispatch BF16-to-FP32 GEMM backends (#375) | `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`, `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py` 等 10 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-09-15 | `b04678a94` | GarrySnail | fix(qwen4): load INT8 MTP fc projections with ReplicatedLinear (#378) | `python/sglang/srt/models/qwen4_exp_mtp.py` | qwen4-exp |
| 2026-09-16 | `b80d0d1bb` | yangyn | [fix] 修复w8a8-fp8-v4pro精度问题 (#380) | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-09-16 | `7df099eb6` | maxiaobetter | feat(moe): 增加 EP 绝对均衡性能测试开关 (#383) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_balance.py`, `python/sglang/srt/layers/moe/hash_topk.py` 等 4 个文件 | shared |
| 2026-09-16 | `2bb5e81e5` | maxiaobetter | feat(spec): 支持节点内 Draft LM-head 词表并行 (#385) | `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 6 个文件 | shared |
| 2026-09-16 | `4f224d2b6` | JingLee | perf(dsv4): support paged MQA logits for prefill (#389) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 29 个文件 | deepseek-v4 |
| 2026-09-16 | `6bf8197dd` | JingLee | Revert "perf(dsv4): support paged MQA logits for prefill (#389)" (#390) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 29 个文件 | deepseek-v4 |
| 2026-09-17 | `f6a092ec7` | GarrySnail | fix(qwen4): flatten MTP fc_hidden input before quantized GEMM (#391) | `python/sglang/srt/models/qwen4_exp_mtp.py` | qwen4-exp |
| 2026-09-17 | `07214443b` | GarrySnail | feat(qsa): use FA sparse GQA for HIP chunk-prefill extend (#392) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` | shared |
| 2026-09-17 | `f4d13c6b8` | chenyuege | [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py` | qwen3-coder, qwen3-core, qwen36 |
| 2026-09-17 | `2df70449a` | maxiaobetter | feat(layersplit): 支持单层 MTP Draft KV 分片与缓存复用 (#387) | `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` 等 10 个文件 | shared |
| 2026-09-17 | `7db5ec177` | maxiaobetter | feat(lplb): 支持 HIP 静态 LP 副本概率分发 (#386) | `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh` 等 10 个文件 | shared |
| 2026-09-17 | `98e923533` | maxiaobetter | fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384) | `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 6 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm5-glm51 |
| 2026-09-17 | `c4ef6d3a4` | maxiaobetter | fix(dsa): 修复 MQA 显存预算与 CP/MTP 索引补齐 (#382) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py` | shared |
| 2026-09-17 | `055812e0d` | Yongqiang Duan | [Perf] DSV4：融合 Indexer Q 侧 INT8 量化，减少冗余量化算子 (#396) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/q_indexer_int8.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 4 个文件 | deepseek-v4 |
| 2026-09-17 | `eb4f0ad89` | yangyn | [feat]适配 w4a8-int8-megamoe (#394) | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | shared |
| 2026-09-17 | `fc7ebb3d0` | leichuan | [Unified Cache] Improve Mooncake direct I/O, observability, and reliability (#398) | `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` 等 13 个文件 | deepseek-v4 |
| 2026-09-18 | `2ed02ec34` | JingLee | feat(dsv4): support paged MQA logits for prefill、support and optimize CP LayerSplit cache with Mooncake direct L3 (#395) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 25 个文件 | deepseek-v4 |
| 2026-09-20 | `16e9b3867` | chenyuege | feat(hcu): support BF16 KV for Qwen DFLASH2 attention (#405) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/manual/test_hcu_dflash_native_block16.py` | shared |
| 2026-09-20 | `ccc15a6f3` | leichuan | feat(cache): integrate Mooncake ReadPlan and optimize page-wise loading for direct linker (#404) | `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` 等 6 个文件 | shared |
| 2026-09-20 | `c496509fb` | lizhigong | fix(mmgen): declare MiniMax H3 request extensions in the OpenAPI document (#399) | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py` 等 4 个文件 | minimax |
| 2026-09-20 | `98ba405a2` | Wenbo Zhu | fix(aiter): w13 权重 shuffle 改回 gemm2 布局，修复 w8a8 变体乱码 (#401) | `python/sglang/srt/layers/moe/moe_runner/aiter.py` | shared |
| 2026-09-20 | `4c219c5f3` | daishiqiang123 | opt: opt dense moe ag and nonzero bubble (#406) | `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/environ.py` 等 5 个文件 | kimi |
| 2026-09-20 | `602fb4a30` | YuanYuan | [FEAT] Support the BCG with CP-V2 and expect to improve TTFT from 10%… (#407) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py` 等 9 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-09-20 | `05c58e82f` | maxiaobetter | fix(dsa): 修复 gfx938 72CU sparse MQA 路由与 HCU 判断 (#409) | `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/attention/dsa_backend.py` | shared |
| 2026-09-20 | `8eb6acd22` | daishiqiang123 | feat(moe): support EPLB for Kimi K3 with DSpark bug fix (#411) | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` 等 5 个文件 | kimi |
| 2026-09-20 | `2b8d2b04a` | GarrySnail | fix(qwen4): support channelwise FP8 and INT8 PLE ngram embeddings (#413) | `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py` | qwen4-exp |
| 2026-09-22 | `50beda6a9` | Lvjiajia | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` | shared |
| 2026-09-23 | `31262cd68` | daishiqiang | fix: fix deepep num_rdma_bytes count correct (#437) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-09-23 | `90f80c6bd` | Wenbo Zhu | feat(moe): 增加 aiter moe_c 后端选定环境变量 (#415) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` | shared |
| 2026-09-23 | `2df2a10f8` | Phy | fix(mmgen): align MiniMax H3 OpenAPI contract (#426) | `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` | minimax |
| 2026-09-23 | `6c0330d8d` | lipenghui | fix(w4a8): 修复 HIPC MoE scale 重复乘 16 与 HCU RoPE 启动越界 (#439) | `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` 等 4 个文件 | shared |
| 2026-09-23 | `2f93be6c5` | daishiqiang | fix(kvcache): handle zero full iterations for asymmetric KV cache (#425) | `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh` | shared |
| 2026-09-23 | `066a95af7` | daishiqiang | fix: fix lightop situ import regression bug and deepgemm w4a8 op interface change (#428) | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-09-23 | `c3bbbd807` | GarrySnail | fix(hcu): serve packed channel INT4 MoE and route QSA MQA through BoltOPs (#434) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`, `python/sglang/srt/layers/attention/qsa/mqa.py` 等 6 个文件 | qwen4-exp |
| 2026-09-23 | `ea1c297dc` | Yongqiang Duan | perf: 为 HCU gfx936 DeepSeek-V4 增加 INT8 Persistent Paged MQA Logits (#436) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/paged_mqa_pers_jit.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 4 个文件 | deepseek-v4 |
| 2026-09-30 | `6086af28d` | dingxinlong | ci(hcu): migrate v0.5.18 workflows to organization runners (#465) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` 等 11 个文件 | shared |
| 2026-09-30 | `100533036` | ybhe1110 | [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py` 等 21 个文件 | deepseek-v4, glm5-glm51 |
| 2026-09-30 | `1828115e0` | jiafei96 | fix w4a16 moe asm error (#462) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` | shared |
| 2026-09-30 | `4ba29d557` | liuzj512 | [HY4][HCU] Enable fp8_e4m3 KV cache with learnable attention sink (#418) | `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py` 等 4 个文件 | deepseek-v4 |
| 2026-09-30 | `8effe1350` | WenQ7 | feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py` 等 140 个文件 | minimax, mixtral-quark-int4fp8-moe |
| 2026-09-30 | `3854f7754` | daishiqiang | opt(kda): update kda verify decode op from boltops (#458) | `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` | shared |
| 2026-09-30 | `08ea4dec7` | zhengzhi | fix(dsv4): resolve Flash-0731 W4A8 API and general_fc accuracy issues (#450) | `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/function_call/base_format_detector.py` 等 9 个文件 | deepseek-v3-r1, deepseek-v32, deepseek-v4 |
| 2026-09-30 | `76e87a951` | lipenghui | fix(hcu): serve DeepSeek-V3.2 INT8, FP8, and BF16 in sglang0.5.18 (#466) | `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/communicator.py` 等 9 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4 |
| 2026-09-30 | `e885e7223` | wu ju | fix(hcu): restore ForwardBatch RMS quantization flag (#469) | `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_forward_batch_hcu_state.py` | shared |
| 2026-10-08 | `cfa865d33` | chaoyujiang | fix deepgemm masked fp8 api upstream (#472) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-10-08 | `f31521614` | zhangang1221 | fix(hcu): enable EAGLE draft decoding for DeepSeek MLA (#477) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/models/deepseek_v2.py` 等 4 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32 |
| 2026-10-08 | `b7e4eae12` | Wenbo Zhu | fix: remove alt_stream overlap copy when writing KV cache (#478) | `python/sglang/srt/mem_cache/memory_pool.py` | shared |
| 2026-10-08 | `7fa7729c1` | leichuan | fix(cache): harden Mooncake ReadPlan and PP direct-L3 cache loading (#482) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` 等 27 个文件 | shared |
| 2026-10-09 | `2cc1bcc28` | maxiaobetter | fix(deepgemm): 统一 INT8/FP8 权重重排与 FP8 masked GEMM 接口 (#484) | `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 6 个文件 | shared |
| 2026-10-09 | `723ac998c` | qieshiniao | 修复 GLM-5.1/5.2 DSA 服务兼容性并优化 CP decode FlashMLA (#475) | `.github/workflows/pr-test-hcu.yml`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` 等 32 个文件 | glm5-glm51 |
| 2026-10-09 | `2bf2890f8` | lipenghui | fix(hcu): correct DeepSeek-V3.1 FP8 decode under CUDA graph (#483) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py` 等 5 个文件 | deepseek-v3-r1, deepseek-v31 |
| 2026-10-09 | `a06c34ef7` | lizhigong | fix(ci): stage-b include 列表容忍分支差异的测试文件 (#485) | `.github/workflows/pr-test-hcu.yml` | shared |
| 2026-10-09 | `6ca7a1bd6` | maxiaobetter | fix(test): 修复 unified attention 单测 KV 索引构造 (#489) | `test/registered/attention/test_triton_attention_kernels.py` | shared |
| 2026-10-09 | `b3632f0be` | liuzj512 | fix(qwen3_moe): quantise MoE gate for compressed-tensors FP8 checkpoints (#492) | `python/sglang/srt/models/qwen3_moe.py` | qwen3-coder, qwen3-core |
| 2026-10-09 | `1882acd8c` | maxiaobetter | fix(moe): restore DeepEP normal combine for HCU groupgemm (#491) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | shared |
| 2026-10-09 | `bfbff7f68` | WenQ7 | fix(hcu): preserve INT8 MoE fallback and restore AITER W8A8 compatibility (#487) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 7 个文件 | shared |
| 2026-10-10 | `966f6da1b` | chaoyujiang | fix(hcu): avoid double packing channel FP8 DeepGEMM weights (#497) | `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-10-10 | `e1eaf0829` | maxiaobetter | fix(moe): guard SBO setup for flat DeepEP dispatch (#501) | `python/sglang/srt/batch_overlap/single_batch_overlap.py` | shared |
| 2026-10-10 | `f106c5360` | Yongqiang Duan | perf(hcu): 优化小 batch W8A8 INT8 GEMM 的 Tiling 选择 (#502) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | shared |
| 2026-10-12 | `2ac651d8f` | maxiaobetter | fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506) | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm5-glm51 |
| 2026-10-12 | `c9a84fca9` | daishiqiang | [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507) | `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py` 等 17 个文件 | deepseek-v3-r1, deepseek-v31, deepseek-v32, kimi |
| 2026-10-12 | `49bb75c79` | zhangpc3 | fix(diffusion): upload all video outputs to cloud storage | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py` | shared |
| 2026-10-12 | `aebf1a9f4` | chaoyujiang | fix(hcu): fix SlimQuant INT8 DeepEP routing and DeepGEMM weight packing (#514) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` | shared |
| 2026-10-13 | `018e5799a` | Wenbo Zhu | Fix/hcu aiter moe inplace (#517) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/models/qwen2_moe.py` | shared |
| 2026-10-13 | `71b2ee4ea` | daishiqiang | perf: add opt-in asynchronous prebuilt token H2D (#516) | `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/environ.py` 等 4 个文件 | shared |
| 2026-10-13 | `9dd4e2e80` | FrankXu0908 | [diffusion] attention: fix HCU Wan SLA and FA family admission (#519) | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py` 等 7 个文件 | shared |
| 2026-10-13 | `3b5ca6e33` | GarrySnail | fix(qwen4_exp): BF16 PLE offload OOM, channel-FP8/INT8 aiter accuracy, and PLE/MTP decode graph fixes (#513) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` 等 27 个文件 | qwen4-exp |
| 2026-10-13 | `3604cec31` | maxiaobetter | fix(hcu): 修复 GLM W4A8 target 的 BF16 MTP 加载与 DeepEP 通信 (#520) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/glm4_moe.py` | glm45, glm46-glm47 |
| 2026-10-13 | `b290dcf39` | chenyuege | [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522) | `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 5 个文件 | qwen3-coder, qwen3-core, qwen36 |
| 2026-10-14 | `5f31aec46` | WenQ7 | fix(aiter): avoid duplicate MoE weights outside MiniMax-M3 (#526) | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/models/minimax_m3.py` 等 6 个文件 | minimax |
| 2026-10-14 | `40c9ec29b` | maxiaobetter | fix(scheduler): keep DP health probes on the generation path (#528) | `python/sglang/srt/managers/scheduler.py` | shared |
| 2026-10-14 | `0ac3b2f83` | s1mplezpc | feat(MiniMax-H3): support MiniMax-H3 channel-wise INT8/FP8 inference on HCU (#532) | `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h` 等 9 个文件 | minimax |
| 2026-10-15 | `ea3acdbe9` | JingLee | feat(dsv4): add opt-in paged MQA logits row chunking (#536) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-10-15 | `5b6302252` | lipenghui | fix(hcu): keep packed FP8 Q on the old MLA path for Kimi K3 (#537) | `python/sglang/srt/layers/attention/hcu_mla_backend.py` | kimi |
| 2026-10-15 | `c2666f4b5` | yangyn | [fix] 修复cp 逻辑：解决实际 token 不被整除时不走 cp 的问题 (#538) | `python/sglang/srt/layers/attention/dsa/utils.py` | shared |
| 2026-10-15 | `3c2b52667` | Songge | fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | deepseek-v3-r1, deepseek-v31, deepseek-v32, glm5-glm51 |
| 2026-10-16 | `6fd9d5644` | chenyuege | [Bugfix] 修复Qwen3.5-122B-A10B-Channel-FP8重复输出的问题 (#545) | `python/sglang/srt/layers/quantization/w8a8_fp8.py` | qwen3-coder, qwen3-core, qwen35 |
| 2026-10-16 | `6fe59ce1a` | Crowder13 | ci: release-pypi-nightly-hcu 多版本编译 (dtk26.04/py3.10+3.12, dtk26.10/py3.12) [rel/20260825_v0.5.18] (#544) | `.github/workflows/release-pypi-nightly-hcu.yml` | shared |
| 2026-10-16 | `23d1def83` | YuanYuan | [FEAT] support megamoe with deegemm in deepseek-v4 (#525) | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` | deepseek-v4 |
| 2026-10-16 | `ae065131d` | daishiqiang | feat(kimi-k3): add opt-in serial shared-expert overlap for DeepEP (#540) | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/k3_sbo_gemm.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 6 个文件 | kimi |
| 2026-10-16 | `da90edf06` | daishiqiang | fix(k3): fix aiter ar shape mismatch and some entries accept rate=1 (#546) | `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/logits_processor.py` | kimi |
| 2026-10-16 | `7586e89f5` | GarrySnail | fix(qwen4-exp): calibrate QSA e4m3 KV scales during graph capture (#551) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` | qwen4-exp |
| 2026-10-16 | `0bb71f0c7` | yangyn | [fix] 解决 w4a8 aiter moe 不支持 swiglu_limit 功能 (#550) | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | shared |
| 2026-10-19 | `b9e0052e9` | GarrySnail | fix(hcu): keep the w8a8 smooth asm fast path off on gfx928 (#555) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | shared |
| 2026-10-20 | `a031c979a` | liuzj512 | [fix] 修复非 AITER 路径下 compressed-tensors W8A8 FP8 MoE 权重被错误补齐导致输出乱码 (#564) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-10-20 | `030f6254f` | daishiqiang | perf(attention): add paged split-KV support and opt-in DSpark V2 (#553) | `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py` | shared |
| 2026-10-20 | `8bec8605f` | GarrySnail | fix(qwen4_exp): fall int8/fp8 PLE pinned alloc back to pageable + hostRegister on HIP OOM (#572) | `python/sglang/srt/models/qwen4_exp.py` | qwen4-exp |
| 2026-10-20 | `19175a690` | XiaokunDing | [Feat] build: Add build wheel scripts (#569) | `README_HCU.md`, `scripts/build_hcu_wheels.sh` | shared |
| 2026-10-21 | `9f7bfb351` | Jane | fix(hcu): skip the w8a8 smooth asm fast path when M=0 (#573) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | shared |
| 2026-10-21 | `414c323ef` | GarrySnail | [Perf] qwen4-exp: Enable fp8 e4m3 QSA indexer decode with incremental shadow pool (#574) | `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py` 等 4 个文件 | qwen4-exp |
| 2026-10-21 | `cda280cdf` | WenQ7 | [Fix] moe: Restrict DeepEPMoE runner delegation to MiniMax-M3 (#577) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py` 等 4 个文件 | minimax |
| 2026-10-22 | `464bebd64` | maxiaobetter | [Fix][v0.5.18] Backport reasoning token accounting fix from upstream #41460 (#579) | `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` | shared |
| 2026-10-23 | `a12acccb2` | s1mplezpc | fix(minimax-h3): avoid full-video clone in VAE postprocessing (#583) | `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py` | minimax |
| 2026-10-23 | `e7fb26db7` | daishiqiang | fix(acc): fix k3-int4 tp16 acc wrong (#587) | `python/sglang/srt/models/kimi_k3.py` | kimi |
| 2026-10-26 | `cbaf42c07` | chaoyujiang | Fix auxiliary HiCache load-back pending collisions (#591) | `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py` | shared |
| 2026-10-27 | `9f60f813d` | chaoyujiang | [DSV4][HCU] Fix speculative compression state retention and configure Torch Top512 sorting (#597) | `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-10-28 | `1343bb07e` | yangyn | [Fix] deepgemm: 修复 w8a8-fp8 旧版重排逻辑 (#608) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | shared |
| 2026-10-31 | `5c859fcfd` | s1mplezpc | [Fix] minimax-h3: prevent repeated-request OOM and fix row-quantization dispatch (#629) | `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` 等 6 个文件 | minimax |
| 2026-11-03 | `729879dce` | Songge | [Fix] quantization: 修复 INT4/INT8 混合量化模型加载 (#631) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py` | minimax |
| 2026-11-03 | `448c57ad4` | liuzj512 | [fix] 修复 w8a8_int8 量化时视觉层 qkv_proj 未命中忽略名单导致被错误量化 (#632) | `python/sglang/srt/layers/quantization/w8a8_int8.py` | shared |
| 2026-11-03 | `c760e11b4` | daishiqiang | fix: fix w4a8 int4 deepgemm hipc kernel interface mismatch (#638) | `python/sglang/srt/layers/moe/ep_moe/layer.py` | shared |
| 2026-11-03 | `2c841655f` | lipenghui | fix(hcu): limit INT8 marlin MoE bypass to DeepSeek so HY3 keeps lightop (#639) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` | hunyuan3-preview |
