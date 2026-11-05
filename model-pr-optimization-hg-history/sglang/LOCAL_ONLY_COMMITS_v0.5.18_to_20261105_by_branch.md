# SGLang release/20260825_v0.5.18..release_v0.5.18_deepseekv4 分支更新本地独有提交索引

## 范围与口径

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 官方仓库: `https://github.com/sgl-project/sglang.git`
- 官方 refs: 已 fetch 到本地 `refs/remotes/github-official/*`
- 筛选方法: 每个分支更新段内，commit hash 不可从官方 GitHub refs 到达，即记录为本地 fork 独有提交。
- 说明: 合并提交也保留；合并提交没有直接文件 diff 时，`主要涉及` 标记为 `无直接文件变更/merge`。
- 生成日期: 2026-11-05

## 数量汇总

| 分支更新段 | 范围内提交数 | 本地独有提交数 | 其中 merge |
| --- | ---: | ---: | ---: |
| `release/20260825_v0.5.18..main` | 95 | 95 | 13 |
| `release/20260825_v0.5.18..release/20261023_v0.5.18_welm` | 1 | 1 | 0 |
| `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 9 | 9 | 0 |
| 合计 | 105 | 105 | 13 |

## 分桶分布

| 桶 | 提交数 |
| --- | ---: |
| `deepseek-v3-r1` | 2 |
| `deepseek-v31` | 2 |
| `deepseek-v32` | 2 |
| `deepseek-v4` | 10 |
| `mixtral-quark-int4fp8-moe` | 1 |
| `qwen3-coder` | 1 |
| `qwen3-core` | 1 |
| `shared` | 67 |
| `unclassified` | 27 |

- 同一提交可同时进入多个模型桶，所以各桶之和大于本地独有提交总数。

## 重复检查

- 本次未计算 `git patch-id`（克隆不含文件内容）；仅按「标题相同且文件集相同」检查疑似重复。
- 未发现标题与文件集都相同的提交。

## 提交索引

### `release/20260825_v0.5.18..main`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | `a96aed11f` | zhuwenbopro | [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` | shared |
| 2026-08-21 | `2c0d45485` | reverie-hub | Sanitize HCU platform naming and runtime messages | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-daily-20260721-conflict-review.md`, `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md` 等 21 个文件 | mixtral-quark-int4fp8-moe |
| 2026-08-21 | `d42ecf6fe` | reverie-hub | Fix HCU detection and sanitized topology diagnostics | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt` | shared |
| 2026-08-24 | `4a540f118` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `7676961ba` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
| 2026-08-24 | `fd4157047` | reverie-hub | Refine HCU platform diagnostics and CLI help | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py` | shared |
| 2026-08-25 | `d1adf7b50` | zhangyh15 | [feature] manual compile ci | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-25 | `94e9fa4b1` | zhangyh15 | ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload) | `.github/workflows/release-whl-manual-hcu.yml` | shared |
| 2026-08-25 | `d445b357f` | lizhigong | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge | unclassified |
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

### `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-10-23 | `962617b2d` | sunjf | WeLM v4.5 support on HCU (squash of yaoyupings/sglang-das v0.5.18_welm) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/configs/model_config.py` 等 55 个文件 | shared |

### `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | `785529a7c` | 千纱都 | perf(cache): add opt-in Mooncake lookup, layout read, and KV reclamation optimizations (#543) | `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` 等 19 个文件 | deepseek-v4 |
| 2026-10-16 | `423934574` | JingLee | feat(dsv4): add opt-in paged MQA logits row chunking (#541) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` | deepseek-v4 |
| 2026-10-16 | `d8a04fcc1` | JingLee | [Fix] Reduce DSV4 prefill KV workspace memory (#552) | `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/environ.py` 等 5 个文件 | deepseek-v4 |
| 2026-10-20 | `eaa872862` | zhengzhi | fix: support API key with multiple tokenizer workers (#559) | `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/auth.py`, `test/registered/unit/entrypoints/test_http_server_auth_config.py` 等 5 个文件 | shared |
| 2026-10-20 | `4c5ac2ee0` | 千纱都 | fix(disagg): defer cached-prefix sends during cache loads (#562) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/manual/hicache/test_pd_cached_prefix_load_ordering.py` | shared |
| 2026-10-23 | `f0a0530ce` | JingLee | [Fix] grammar: 同步 Prefill CP 的 Grammar 请求准入与失败状态 (#589) | `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/constrained/test_grammar_manager.py` | shared |
| 2026-10-27 | `834293ee4` | zhengzhi | [Fix] disaggregation: 修复 DeepSeek V4 PD 清理同步与消息处理 (#600) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/sampler.py` 等 7 个文件 | deepseek-v4 |
| 2026-10-29 | `dc8e09ba9` | chaoyujiang | [DSV4][HCU] Fix speculative compression state retention in c_plan (#609) | `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh` | deepseek-v4 |
| 2026-10-30 | `c66f34363` | zhengzhi | [Fix] TokenizerManager: 修复客户端断开后已下发请求未被终止的问题 (#628) | `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` | shared |
