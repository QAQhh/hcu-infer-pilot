# sglang Shared Framework Commits 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `.codespellrc` | `35456bae31` |
| `.coveragerc` | 无直接提交 |
| `.dockerignore` | 无直接提交 |
| `.git-blame-ignore-revs` | 无直接提交 |
| `.github/CI_PERMISSIONS.json` | 无直接提交 |
| `.github/CODEOWNERS` | 无直接提交 |
| `.github/FOLDER_README.md` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/1-bug-report.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/2-feature-request.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/3-playground-verified-cell.yml` | 无直接提交 |
| `.github/MAINTAINER.md` | 无直接提交 |
| `.github/actions/check-maintenance/action.yml` | 无直接提交 |
| `.github/actions/check-pr-test-health/action.test.cjs` | 无直接提交 |
| `.github/actions/check-pr-test-health/action.yml` | 无直接提交 |
| `.github/actions/download-rust-ext/action.yml` | 无直接提交 |
| `.github/actions/upload-cuda-coredumps/action.yml` | 无直接提交 |
| `.github/actions/wait-for-jobs/action.yml` | 无直接提交 |
| `.github/audit_permission.py` | 无直接提交 |
| `.github/labeler.yml` | 无直接提交 |
| `.github/linters/lychee-ci.toml` | 无直接提交 |
| `.github/linters/lychee.toml` | 无直接提交 |
| `.github/open-source-compliance.json` | `e3fee4310d`, `758a0a9890` |
| `.github/pull_request_template.md` | 无直接提交 |
| `.github/scripts/ci-labels.cjs` | 无直接提交 |
| `.github/scripts/pr-check-comment.cjs` | 无直接提交 |
| `.github/scripts/pr-title.test.cjs` | 无直接提交 |
| `.github/update_ci_permission.py` | 无直接提交 |
| `.github/workflows/_docker-build-and-publish.yml` | 无直接提交 |
| `.github/workflows/_docker-cleanup-nightly.yml` | 无直接提交 |
| `.github/workflows/_npu-analyze-failure.yml` | 无直接提交 |
| `.github/workflows/_npu-pr-test-stage.yml` | `c40703e6b4` |
| `.github/workflows/_npu-single-node-test-stage.yml` | `c40703e6b4` |
| `.github/workflows/_pr-test-check-changes.yml` | 无直接提交 |
| `.github/workflows/_pr-test-rust-ext-build.yml` | 无直接提交 |
| `.github/workflows/_pr-test-sgl-kernel-build.yml` | 无直接提交 |
| `.github/workflows/_pr-test-simulator-cpu.yml` | 无直接提交 |
| `.github/workflows/_pr-test-stage-cpu.yml` | 无直接提交 |
| `.github/workflows/_pr-test-stage.yml` | 无直接提交 |
| `.github/workflows/amd-aiter-scout.yml` | `111fea82f3`, `b2f0b830c2`, `b38f25513e` |
| `.github/workflows/amd-ci-job-monitor.yml` | `111fea82f3`, `b2f0b830c2`, `b38f25513e` |
| `.github/workflows/auto-tune.yml` | 无直接提交 |
| `.github/workflows/bot-bump-docs-version.yml` | `92ce544fac` |
| `.github/workflows/bot-bump-flashinfer-version.yml` | 无直接提交 |
| `.github/workflows/bot-bump-kernel-version-to-sglang.yml` | 无直接提交 |
| `.github/workflows/bot-bump-kernel-version.yml` | 无直接提交 |
| `.github/workflows/bot-bump-sglang-version.yml` | 无直接提交 |
| `.github/workflows/bot-cherry-pick.yml` | 无直接提交 |
| `.github/workflows/cancel-pr-workflows-on-close.yml` | 无直接提交 |
| `.github/workflows/cancel-unfinished-pr-tests.yml` | 无直接提交 |
| `.github/workflows/ci-auto-bisect.yml` | `dc5cd70892` |
| `.github/workflows/ci-coverage-overview.yml` | `111fea82f3`, `b2f0b830c2`, `b38f25513e` |
| `.github/workflows/ci-failure-monitor.yml` | 无直接提交 |
| `.github/workflows/ci-lark-notify.yml` | 无直接提交 |
| `.github/workflows/ci-model-inventory.yml` | `111fea82f3`, `b2f0b830c2` |
| `.github/workflows/close-inactive-issues.yml` | 无直接提交 |
| `.github/workflows/close-stale-prs.yml` | 无直接提交 |
| `.github/workflows/cookbook-deployment-smoke.yml` | `029b6e6418`, `a8543c8131`, `f89209aa84`, `87b9d5c85e`, `cc3758967d`, `78c700ee01`, `b6dd37e66a`, `f9b972b372`, `50b0d00518` |
| `.github/workflows/coverage-collection-npu.yml` | 无直接提交 |
| `.github/workflows/full-test-npu.yml` | 无直接提交 |
| `.github/workflows/hcu-feishu-notify-preview.yml` | `e05f146bed`, `9c69436eed`, `0ff7a014fe`, `65b7c42689`, `6ac12c2e50`, `2c21b95e60` |
| `.github/workflows/hcu-full-enabled.yml` | `e05f146bed`, `4c7a264e5c`, `dabae6b13a`, `71de6dd93d`, `02968a96de`, `bfa4011ad0`, `e3fee4310d` |
| `.github/workflows/hcu-manual-model-test.yml` | `e05f146bed`, `4c7a264e5c`, `e3fee4310d` |
| `.github/workflows/hcu-pd-1p1d.yml` | 无直接提交 |
| `.github/workflows/labeler.yml` | `e05f146bed`, `e3fee4310d`, `9ed791e147` |
| `.github/workflows/lint-hcu.yml` | `e05f146bed`, `3e6aaf09d8`, `69c73a1787`, `997e64560f`, `77939d9a53`, `8f848be4e7`, `358a337143`, `e3fee4310d` |
| `.github/workflows/lint.yml` | `111fea82f3`, `b2f0b830c2` |
| `.github/workflows/list-active-pr-runs.yml` | 无直接提交 |
| `.github/workflows/mlu-ci-reliability-report.yml` | 无直接提交 |
| `.github/workflows/nightly-72-gpu-gb200.yml` | 无直接提交 |
| `.github/workflows/nightly-amd-mi355x-disagg.yml` | `111fea82f3`, `b2f0b830c2` |
| `.github/workflows/nightly-experimental-sgl-router-docker.yml` | `111fea82f3`, `b2f0b830c2` |
| `.github/workflows/nightly-link-check.yml` | 无直接提交 |
| `.github/workflows/nightly-release-gateway.yml` | `990a1a798d` |
| `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml` | 无直接提交 |
| `.github/workflows/nightly-test-amd-miles-rocm10.yml` | 无直接提交 |
| `.github/workflows/nightly-test-amd.yml` | `111fea82f3`, `b2f0b830c2`, `b38f25513e` |
| `.github/workflows/nightly-test-hcu.yml` | `50b0d00518`, `e05f146bed`, `b5ca753bc8`, `adc1d69b2a`, `b5108cc7fe`, `2866df9948`, `a2de3b8cff`, `6a4a61efba`, `fb7f119564`, `1a5ce1750d`, `b0f2bb3a84`, `02968a96de`, ... (20 total) |
| `.github/workflows/nightly-test-image-hcu.yml` | `e05f146bed`, `0457572a14`, `8fa7122b3a` |
| `.github/workflows/nightly-test-intel-wheel.yml` | 无直接提交 |
| `.github/workflows/nightly-test-intel.yml` | `111fea82f3`, `b2f0b830c2`, `b38f25513e` |
| ... | 8314 more files omitted from table; all were used for git tracing. |

## 本地提交覆盖总览

- 来源工作树: `HYGON-AI/sglang-das`
- 生成日期: 2026-11-05
- 文档提交数: 460
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-02 | `594e1ae94c` | 测试/文档/基准 | [Chore] ci: Remove completed DashHub recovery workflow (#634) | `.github/workflows/dashhub-recover-41338132822.yml` |
| 2026-11-02 | `471ab82545` | 模型支持/运行时入口 | Add one-time DashHub recovery for run 41338132822 (#633) | `.github/workflows/dashhub-recover-41338132822.yml` |
| 2026-10-29 | `9fb319cc33` | 性能/后端优化 | [CI] optest: Require every enabled operator result (#622) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-29 | `db479b030f` | 性能/后端优化 | [CI] optest: Report outcome to DashHub (#619) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-29 | `25aa13e98f` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml (#617) | `.github/workflows/pr-test-hcu.yml` |
| 2026-10-28 | `fd98647ed1` | 缺陷修复 | [Fix] ci: Restore previous DashHub operator reporting (#614) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-28 | `029b6e6418` | 模型支持/运行时入口 | [CI] model-ci: Pass history token for daily comparison report (#607) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-28 | `098f31d695` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-10-28 | `6dac3481cd` | 缺陷修复 | [Fix] ci: Preserve model cases in DashHub operator reporting (#604) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-20 | `a8543c8131` | 模型支持/运行时入口 | [CI] cookbook: Add BW1000 deployment smoke tests (#570) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-19 | `f89209aa84` | 模型支持/运行时入口 | ci: pass package server to Cookbook model tests (#556) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-16 | `87b9d5c85e` | 测试/文档/基准 | Run cookbook deployment checks after HCU image publishing (#548) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-15 | `fc095e0598` | 缺陷修复 | fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533) | `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` |
| 2026-10-15 | `cc3758967d` | 通用实现调整 | Pass DashHub credential to deployment smoke controller (#534) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-14 | `78c700ee01` | 模型支持/运行时入口 | Add image input to cookbook deployment smoke workflow (#530) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `e295faff5d` | 性能/后端优化 | update ci name&&add optest log (#515) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-12 | `b6dd37e66a` | 测试/文档/基准 | Run cookbook smoke tests for all cases by default | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `f9b972b372` | 模型支持/运行时入口 | Use a clean checkout directory for the model smoke controller (#510) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `50b0d00518` | 模型支持/运行时入口 | Delegate HCU model deployment smoke CI to external controller (#503) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-10 | `3b0e4a0739` | 性能/后端优化 | [Fix] Bound crash diagnostics and fatal shutdown on main (#498) | `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` |
| 2026-10-10 | `4205397cbc` | 模型支持/运行时入口 | add password-free download code (#499) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-09 | `f0ee2a5059` | 缺陷修复 | FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473) | `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py` |
| 2026-10-09 | `fb46d17ad9` | 性能/后端优化 | add optest process (#481) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-09-30 | `e05f146bed` | 模型支持/运行时入口 | ci(hcu): migrate main workflows to organization runners (#463) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` |
| 2026-09-28 | `5e8269d55a` | 缺陷修复 | [BUGFIX]镜像DTK版本号不对 (#447) | `.github/workflows/release-docker-hcu.yml` |
| 2026-09-24 | `665b27d1fa` | 缺陷修复 | feat(ci) fix main build whl failed (#449) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-23 | `f2d49c2c0e` | 缺陷修复 | FIX(DSV4): 补全 system/reminder 结尾对话的 assistant 生成前缀并解析 markdown 伪工具调用 (#435) | `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`, `python/sglang/srt/function_call/deepseekv4_detector.py`, `test/registered/unit/function_call/test_deepseekv4_detector.py` |
| 2026-09-23 | `7be1324cf8` | 测试/文档/基准 | ci: report sglang nightly packages to DashHub (#424) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-23 | `2871c8fdd9` | 测试/文档/基准 | ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-22 | `b5ca753bc8` | 测试/文档/基准 | ci(hcu): run nightly against v0.5.18 and report its results (#432) | `.github/workflows/nightly-test-hcu.yml` |
| 2026-09-21 | `a981685e7f` | 缺陷修复 | fix release-pr-hcu.yml build sglang (#423) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-21 | `cb932f5fbd` | 测试/文档/基准 | feat(ci) compaity sgl-kernal main to v0.5.12 (#421) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-21 | `ae5c33991b` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-16 | `adc1d69b2a` | 测试/文档/基准 | ci(hcu): align main wheel builds with 0.5.18 runtime (#379) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `5c03a8e22f` | 测试/文档/基准 | [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-15 | `ae14a99e50` | 缺陷修复 | fix(ci): fix HCU wheel build target routing (#372) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `7c8272a3a3` | 缺陷修复 | [BUGFIX]更新AICC安装方式 (#367) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-14 | `575cf47976` | 测试/文档/基准 | ci(hcu): restore source mode for test-only PRs (#364) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-14 | `516261baf1` | 测试/文档/基准 | ci(hcu): register sampling test and adjust MMLU threshold (#359) | `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `b5108cc7fe` | 测试/文档/基准 | ci(hcu): use v0.5.18 image and restore eval dependencies (#347) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` |
| 2026-09-08 | `0af71f61b6` | 缺陷修复 | fix(ci): update HCU evaluation dependencies and asset paths (#325) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-09-04 | `0457572a14` | 测试/文档/基准 | [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308) | `.github/workflows/nightly-test-image-hcu.yml` |
| 2026-09-03 | `2828bde71d` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#299) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-02 | `6fe7ce9097` | 测试/文档/基准 | ci(hcu): restore run suite file filters (#290) | `test/run_suite.py` |
| 2026-09-02 | `9d261478d6` | 性能/后端优化 | [CI] Update HCU model asset paths on main (#285) | `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh` |
| 2026-09-01 | `8fa7122b3a` | 测试/文档/基准 | [FEATURE]构建镜像之后触发模型测试 (#277) | `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml` |
| 2026-08-31 | `e864c30287` | 测试/文档/基准 | ci: enable HCU PR tests for release branches (#272) | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-31 | `3ca61517d0` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-08-28 | `bc990ebd52` | 测试/文档/基准 | [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-28 | `68dcd498aa` | 测试/文档/基准 | [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-27 | `6b468d012b` | 性能/后端优化 | [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-27 | `7609d9af69` | 模型支持/运行时入口 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` |
| 2026-08-27 | `2866df9948` | 测试/文档/基准 | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-26 | `a2de3b8cff` | 测试/文档/基准 | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `f6d701c520` | 缺陷修复 | Fix stale HCU Stage B test paths | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-26 | `c94c3ca2c8` | 缺陷修复 | fix: gateway wheel is at workspace root target/wheels | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-26 | `8dd5daf2fa` | 测试/文档/基准 | Refine HCU and AMD CLI help text | `python/sglang/srt/server_args.py`, `test/run_suite.py` |
| 2026-08-26 | `990a1a798d` | 测试/文档/基准 | ci: disable scheduled gateway nightly release | `.github/workflows/nightly-release-gateway.yml` |
| 2026-08-24 | `fd41570479` | 通用实现调整 | Refine HCU platform diagnostics and CLI help | `python/sglang/srt/server_args.py` |
| 2026-08-21 | `d42ecf6fe9` | 缺陷修复 | Fix HCU detection and sanitized topology diagnostics | `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-25 | `6a4a61efba` | 性能/后端优化 | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `3e6aaf09d8` | 测试/文档/基准 | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `f2fc4e166b` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-08-25 | `69c73a1787` | 模型支持/运行时入口 | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `94e9fa4b1d` | 测试/文档/基准 | ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-25 | `59213c7e48` | 性能/后端优化 | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-25 | `d1adf7b503` | 测试/文档/基准 | [feature] manual compile ci | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-25 | `c40703e6b4` | 缺陷修复 | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` |
| 2026-08-24 | `261b8627f1` | 缺陷修复 | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` |
| 2026-08-20 | `37c5b30bb9` | 缺陷修复 | fix: extract full DTK version for three-part versions | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-08-21 | `a96aed11f0` | 性能/后端优化 | [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-08-20 | `27ce43c71d` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `72d1d2a73a` | 性能/后端优化 | [fix]solved other CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `f6b66222a0` | 通用实现调整 | revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0 | `.github/workflows/release-pr-hcu.yml` |
| 2026-08-20 | `11d08002bf` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `b628d29e1c` | 测试/文档/基准 | [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-20 | `fb7369fec0` | 缺陷修复 | [bugfix]删除无关文件 | `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942` |
| 2026-08-20 | `62a07586d9` | 性能/后端优化 | [feat] 适配HCU FA3 | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-17 | `9bbf3799d8` | 模型支持/运行时入口 | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` |
| 2026-08-14 | `fa309a1e19` | 性能/后端优化 | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-08-13 | `5e2ba659ea` | 性能/后端优化 | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-13 | `18e167b730` | 性能/后端优化 | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-13 | `54e3ed50f6` | 缺陷修复 | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` |
| 2026-08-12 | `fb7f119564` | 测试/文档/基准 | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-12 | `2083c069f7` | 性能/后端优化 | fix lint: apply pre-commit fixes to the EP MoE fallback change | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-11 | `ccbb65acb2` | 性能/后端优化 | [HCU][DSpark] Fix DP EP MoE fallback routing | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-10 | `b36730b417` | 性能/后端优化 | fix lint: apply pre-commit fixes to the mHC EAGLE changes | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py` |
| 2026-08-10 | `5fd89c7288` | 缺陷修复 | [BugFix] fix the inference tensor graph replay issues in MTP mode | `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-08-10 | `4a6fbed985` | 性能/后端优化 | [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config | `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-10 | `e3a9d595c9` | 缺陷修复 | [HCU][DSpark] Fix sampling parameter updates after graph capture | `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` |
| 2026-08-07 | `3de1323a9b` | 调度/缓存/PD | ci(hcu): normalize rebased PD suite names | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-07 | `3fbc8ae9ef` | 性能/后端优化 | test(hcu): align numerical references with v0.5.15 | `test/registered/hcu/kernels/test_attention_reference_hcu.py`, `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py` |
| 2026-08-07 | `76ced479ea` | 性能/后端优化 | test(hcu): use v0.5.15 FP8 kernel path | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` |
| 2026-08-07 | `ecf4756cea` | 测试/文档/基准 | test(hcu): isolate server guard unit test | `scripts/ci/hcu/test_hcu_server_guard.py` |
| 2026-08-07 | `dc5cd70892` | 测试/文档/基准 | ci: finalize v0.5.15 workflow policy | `.github/workflows/ci-auto-bisect.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/slash-command-handler.yml` |
| 2026-08-07 | `50736ebe71` | 测试/文档/基准 | ci(hcu): keep migration changes scoped | `README_HCU.md` |
| 2026-08-07 | `1a5ce1750d` | 测试/文档/基准 | ci(hcu): publish reasoning results to shared storage | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`, `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py` |
| 2026-08-07 | `4c7a264e5c` | 性能/后端优化 | ci(hcu): align model assets and selected-ref kernel | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-08-07 | `92ce544fac` | 测试/文档/基准 | ci: align v0.5.15 workflow triggers | `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml` |
| 2026-08-07 | `b59995e42d` | 缺陷修复 | fix(hcu): point PD smoke tests at a declared HCU suite | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-07 | `154a88c7b7` | 性能/后端优化 | fix lint: apply isort/black to the lmslim->lightop migration | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-08-06 | `b0f2bb3a84` | 缺陷修复 | fix(hcu): restore network_mode matrix keys dropped by the forward-port | `.github/workflows/nightly-test-hcu.yml` |
| 2026-08-06 | `f17440f19f` | 缺陷修复 | fix(hcu): restore original license headers dropped by the forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py` |
| 2026-08-06 | `8e2aba4bfa` | 性能/后端优化 | fix lint: apply isort/black to forward-port diff | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` |
| 2026-08-06 | `f1c6f56315` | 性能/后端优化 | fix(hcu): drop leftover source hunks that renaming and partial takes left behind | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-05 | `dabae6b13a` | 缺陷修复 | fix(ci): use PR files API for HCU wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-05 | `44bb481cf9` | 性能/后端优化 | fix(eplb): apply expert ID remapping for HCU fused TopK | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-05 | `2fb37eaace` | 缺陷修复 | fix(ci): align HCU Python wheel paths | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-05 | `71de6dd93d` | 缺陷修复 | fix(ci): align HCU gateway wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-05 | `2a342cdf1d` | 缺陷修复 | fix fp8 bug of triton | `python/sglang/srt/layers/attention/triton_ops/decode_attention.py` |
| 2026-08-04 | `8160ebe53c` | 缺陷修复 | fix(hcu): retain PD decode adapter callbacks | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-04 | `43d8d9ac1b` | 性能/后端优化 | style(hcu): fix lint for KME W8A8 lightop path | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-08-04 | `e8298ba909` | 缺陷修复 | fix(hcu): restore DP decode protocol constants | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-04 | `083d1d8b99` | 性能/后端优化 | fix(hcu): restore DeepGEMM PD helper and current cache API | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-08-04 | `cd60b74339` | 调度/缓存/PD | 修改hicache+pp并行 stage不一致问题commit提交格式 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` |
| 2026-08-03 | `143ee92872` | 性能/后端优化 | refactor(hcu): route KME W8A8 hipBLASLt through lightop | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-07-29 | `84bfd45c44` | 缺陷修复 | 修复hicache+pp并行 stage不一致问题 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py` |
| 2026-08-03 | `015f6d49a0` | 性能/后端优化 | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-08-03 | `de696eab9c` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `e6c4102592` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `3358846e55` | 调度/缓存/PD | Update quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `4d3aaf6aff` | 调度/缓存/PD | Update quality gate workflow for versioning and concurrency | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `286612da40` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `ff7f44b8ed` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `67ecec8dd1` | 缺陷修复 | fix(hcu): scope Feishu status to accuracy results | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-31 | `85dcec9474` | 缺陷修复 | fix(hcu): support Python 3.8 in Feishu notifier | `scripts/ci/hcu/hcu_ci_notify_feishu.py` |
| 2026-07-31 | `9c69436eed` | 缺陷修复 | fix(hcu): remove resend tool dependencies | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-31 | `0ff7a014fe` | 模型支持/运行时入口 | ci(hcu): support resending Feishu accuracy results | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-31 | `f556d3896e` | 性能/后端优化 | [FIX] 修复lmslim和lightop接口冲突问题 (#154) | `python/sglang/srt/layers/quantization/slimquant_w4a8.py` |
| 2026-07-31 | `b489942109` | 测试/文档/基准 | ci: install PyYAML for slash command handler (#156) | `.github/workflows/slash-command-handler.yml` |
| 2026-07-31 | `497c35457c` | 缺陷修复 | fix(scheduler): abort too-large requests instead of dead-looping | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` |
| 2026-07-31 | `dc015a0bc5` | 缺陷修复 | [PD] When PP is greater than 1, fix the request rollback when the KV cache is exhausted | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-07-31 | `83f43b3f4d` | 性能/后端优化 | [CI] Fix some CI errors | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-07-31 | `39d6912202` | 缺陷修复 | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-07-31 | `02968a96de` | 缺陷修复 | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` |
| 2026-07-30 | `17cf690afc` | 性能/后端优化 | style: fix HCU lint checks | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` |
| 2026-07-30 | `489170e5c4` | 性能/后端优化 | [FIX] 修复moe_w8a8重排函数删除问题 | `python/sglang/srt/layers/moe/moe_runner/lightop.py` |
| 2026-07-30 | `6ea38ee522` | 调度/缓存/PD | style(hcu): format PD helper registration | `test/registered/hcu/disaggregation/pd_hcu_utils.py` |
| 2026-07-30 | `b8389e5c5d` | 调度/缓存/PD | test(hcu): register PD helper for nightly collection | `test/registered/hcu/disaggregation/pd_hcu_utils.py` |
| 2026-07-29 | `111fea82f3` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` |
| 2026-07-29 | `b2f0b830c2` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` |
| 2026-07-29 | `be81ab4196` | 缺陷修复 | fix(dp): demote DP Decode StepInfo log to debug | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` |
| 2026-07-29 | `6a031254f5` | 测试/文档/基准 | ci(hcu): isolate nightly services and shared results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-29 | `e18e6b94bc` | 测试/文档/基准 | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-29 | `3b4327cd7b` | 性能/后端优化 | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` |
| 2026-07-29 | `58d475775e` | 缺陷修复 | fix(hcu): allow single-node context parallel tp16 | `python/sglang/srt/server_args.py` |
| 2026-07-29 | `d39d628ef3` | 性能/后端优化 | fix(hcu): enable NSA draft-extend cuda graph | `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-07-29 | `4e5a95fcb5` | 缺陷修复 | fix(pd): transfer MTP NSA topk seed metadata over Mooncake | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py` |
| 2026-07-29 | `6e7a53e865` | 性能/后端优化 | fix(hcu): select hipblaslt w8a8 layout by gfx arch | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-07-28 | `035ca766ff` | 缺陷修复 | fix(cache): forward Mamba indices in NSA offload | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-29 | `049f5e15ee` | 性能/后端优化 | [bugfix] 透传apply_routed_scaling_factor_on_output，防止moe_sum多乘routed_scaling_factor | `python/sglang/srt/layers/moe/topk.py` |
| 2026-07-29 | `92e95e3f51` | 性能/后端优化 | perf(mamba): flatten fused state scatter launch grid | `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py` |
| 2026-07-29 | `bfa4011ad0` | 测试/文档/基准 | ci(hcu): share wheel staging across runners | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` |
| 2026-07-28 | `fc59c96c54` | 缺陷修复 | fix lint: format line breaks and remove trailing whitespace | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-07-28 | `7b89bf6617` | 性能/后端优化 | fix: propagate return_hidden_states_before_norm flag for mHC target-verify | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-07-28 | `d0c4729899` | 调度/缓存/PD | ci: add HCU PD disaggregation smoke tests | `test/registered/hcu/disaggregation/pd_hcu_utils.py`, `test/registered/hcu/disaggregation/test_pd_basic_hcu.py`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py` |
| 2026-07-28 | `cd4802bbab` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-07-28 | `0305c5a3b9` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-28 | `9a4f82911e` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-28 | `997e64560f` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-07-28 | `77939d9a53` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-07-28 | `8f848be4e7` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-07-27 | `0710e82a02` | 调度/缓存/PD | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` |
| 2026-07-27 | `93c56ce71a` | 通用实现调整 | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` |
| 2026-07-27 | `163a92c142` | 缺陷修复 | fix(hcu):修改lightop的算子接口. | `python/sglang/srt/layers/activation.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-27 | `87e3831800` | 性能/后端优化 | fix: 移除旧的lmslim导入方式. | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-07-27 | `afac89e0e4` | 性能/后端优化 | feat(hcu): add KME W8A8 hipBLASLt path via METHODS=3 | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-07-24 | `a3efe5e533` | 性能/后端优化 | [bugfix]:修复lightop_per_token_quant_fp8调用前tensor准备. | `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/mem_cache/allocator.py` |
| 2026-07-24 | `88d4501a3b` | 调度/缓存/PD | Update quality gate workflow reference | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `9e13c77cee` | 缺陷修复 | fix(ci): use card v2 link button | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `4af8102057` | 缺陷修复 | fix(ci): use card v2 metadata component | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `65b7c42689` | 测试/文档/基准 | ci: use shared runner for Feishu preview | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-24 | `6ac12c2e50` | 测试/文档/基准 | ci: decouple Feishu preview from HCU runners | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-24 | `2c21b95e60` | 缺陷修复 | fix(ci): align Feishu accuracy table | `.github/workflows/hcu-feishu-notify-preview.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `9a8b1bd08e` | 调度/缓存/PD | Update quality gate workflow reference to new commit | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `eb6a340936` | 调度/缓存/PD | Update workflow reference to latest commit | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `f76d2cea38` | 通用实现调整 | Delete .github/workflows/quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-23 | `c3755b4d46` | 性能/后端优化 | fix: make DP local control broadcast opt-in via env | `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-07-23 | `e338cca156` | 缺陷修复 | ci(hcu): improve accuracy card and fix VLM model path | `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-23 | `83d2a2b4b1` | 缺陷修复 | fix(hcu): rename stale DCU HiCache identifiers | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` |
| 2026-07-22 | `8b38b9a258` | 调度/缓存/PD | Update comment for all_gather usage in scheduler | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` |
| 2026-07-22 | `421a13a808` | 测试/文档/基准 | ci(hcu): enable accuracy notification on default branch | `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-22 | `b1606885e0` | 缺陷修复 | Fix help text for custom all-reduce backend | `python/sglang/srt/server_args.py` |
| 2026-07-22 | `0b46ed36da` | 性能/后端优化 | fix: apply bias after HCU DeepGEMM FP8 linear | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-07-22 | `f391712f7f` | 缺陷修复 | fix(hcu): use HCU guard for MLA KV cache storage | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-22 | `7941e04191` | 缺陷修复 | fix: enable HiCache layout_dcu for hybrid Mamba and EAGLE draft | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` |
| 2026-07-22 | `1c40e365c8` | 调度/缓存/PD | support mla lightop | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-22 | `9fc04a7a2c` | 性能/后端优化 | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-07-21 | `7b6a9dd891` | 性能/后端优化 | 修复DeepseekV4精度问题 | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-21 | `ac56ca009f` | 测试/文档/基准 | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` |
| 2026-07-21 | `9864c84513` | 测试/文档/基准 | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-21 | `c1f3f08c8a` | 调度/缓存/PD | Update workflow reference to a new commit | `.github/workflows/quality-gate.yml` |
| 2026-07-21 | `e7ab054110` | 通用实现调整 | Delete .github/workflows/pr-quality-gate.yml | `.github/workflows/pr-quality-gate.yml` |
| 2026-07-21 | `14da9b10e4` | 调度/缓存/PD | Update workflow reference in quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-07-20 | `15a656ea69` | 测试/文档/基准 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` |
| 2026-07-20 | `e19d341ab8` | 调度/缓存/PD | Refactor quality gate workflow and update triggers | `.github/workflows/quality-gate.yml` |
| 2026-07-20 | `5543eb3df2` | 调度/缓存/PD | Rename quality-gate workflow and update triggers | `.github/workflows/quality-gate.yml` |
| 2026-07-20 | `5ac1f2418a` | 模型支持/运行时入口 | Add GitHub Actions workflow for quality gate | `.github/workflows/pr-quality-gate.yml` |
| 2026-07-20 | `811aa027d6` | 测试/文档/基准 | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `e47445d2fa` | 调度/缓存/PD | chore: clean leftover patch labels in PD Decode DP sync | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-07-20 | `81e3561aeb` | 测试/文档/基准 | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` |
| 2026-07-20 | `358a337143` | 缺陷修复 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-07-20 | `079275b811` | 模型支持/运行时入口 | ci: add local sensitive diff text gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `fe9f24924f` | 缺陷修复 | fix: prevent PD Decode DP hang under enable-dp-attention | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-07-16 | `37074c9af6` | 缺陷修复 | Fix dsv4 full token pool | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` |
| 2026-07-16 | `09d7a1d4ca` | 性能/后端优化 | support fabric aiter custom allreduce | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-07-16 | `d280691576` | 缺陷修复 | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-07-16 | `e5a2dd0419` | 缺陷修复 | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-07-16 | `339dfe4336` | 测试/文档/基准 | docs(dcu): define v0.5.15.post1 release workflow | `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md` |
| 2026-07-16 | `dc1323ba4c` | 测试/文档/基准 | docs(dcu): finalize v0.5.12_dev forward-port | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-15 | `49a10aec8c` | 测试/文档/基准 | docs(dcu): record 20260714 owner validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `f67cdf69bd` | 测试/文档/基准 | docs(dcu): record 20260714 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `20633db576` | 模型支持/运行时入口 | docs(dcu): add 20260714 conflict review | `docs/internal/dcu-main-catchup-20260714-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `324181561d` | 模型支持/运行时入口 | docs(dcu): add 20260713 conflict review | `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `0b30b7c9d2` | 测试/文档/基准 | docs(dcu): record 20260712 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `44f81e8f7a` | 测试/文档/基准 | docs(dcu): record 20260712 runtime gate status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `baa08af595` | 模型支持/运行时入口 | docs(dcu): add 20260712 conflict review | `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `1109d462d5` | 调度/缓存/PD | [Feature] Support PD different-TP transfer for hybrid SWA/NSA and unequal K/V item lens. | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-07-14 | `3e335fce8e` | 测试/文档/基准 | docs: correct 20260710 endpoint subject | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `3d77308ea3` | 测试/文档/基准 | docs: mark 20260710 catch-up validated | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `6630db3cfa` | 测试/文档/基准 | docs: record 20260710 pure-TP validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `24894692ea` | 缺陷修复 | fix: use runtime attention TP size in model warmup | `python/sglang/srt/model_executor/model_runner.py` |
| 2026-07-14 | `9d7fbb0174` | 模型支持/运行时入口 | docs: add 20260710 conflict review | `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `48c3c0997e` | 测试/文档/基准 | ci: run HCU text check in Python 3.10 container | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `f1c5eda31e` | 测试/文档/基准 | ci: require HCU runtime text check | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `c0e8edd741` | 性能/后端优化 | fix(dcu): initialize DeepEP dispatch dtype state | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-07-14 | `412d0ef9fa` | 模型支持/运行时入口 | docs(dcu): add 20260709 conflict review | `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `e3aa204a05` | 测试/文档/基准 | docs(dcu): require catch-up conflict reviews | `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-14 | `b9ca7c2adb` | 通用实现调整 | Refine copyright/license warning messages | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `d53953dbe7` | 测试/文档/基准 | ci: clean up HCU validation checks | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/tests/test_check_hcu_runtime_text.py` |
| 2026-07-14 | `2981595c7f` | 性能/后端优化 | [FIX] 修复走非dcu_fa下的报错 | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-07-13 | `516a35c40e` | 测试/文档/基准 | docs(dcu): record 20260703 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `c078943aa3` | 性能/后端优化 | chore: fix fused_moe lint issues | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-07-13 | `d8ed552da8` | 模型支持/运行时入口 | docs(dcu): add 20260629 conflict review | `docs/internal/dcu-main-catchup-20260629-conflict-review.md` |
| 2026-07-13 | `bf59e99fde` | 测试/文档/基准 | ci: harden HCU runtime text quality gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py` |
| 2026-07-13 | `24bcdba3b7` | 性能/后端优化 | feat: support AITER W4A16 MOE_C prefill | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-07-13 | `427726d609` | 缺陷修复 | fix: complete HCU runtime text cleanup | `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-07-13 | `8c797abd6f` | 测试/文档/基准 | Record 20260629 DCU runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `bd60c02238` | 通用实现调整 | Enhance quality gate workflow with new checks and branches | `.github/workflows/quality-gate.yml` |
| 2026-07-13 | `40c658e8ab` | 测试/文档/基准 | ci: harden HCU runtime text checker | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` |
| 2026-07-13 | `48489724d5` | 测试/文档/基准 | docs(dcu): record 20260623 catch-up runtime status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `cba9e72cc0` | 性能/后端优化 | [BugFix] skip some uncompatibal env setup in hip for DCU | `python/sglang/srt/server_args.py` |
| 2026-07-13 | `1123fc0382` | 测试/文档/基准 | ci: enforce HCU rename safety checks | `scripts/ci/hcu/hcu_rename_allowlist.txt`, `scripts/ci/hcu/test_verify_hcu_rename.py`, `scripts/ci/hcu/verify_hcu_registration.py` |
| 2026-07-13 | `9353ecb963` | 测试/文档/基准 | docs: complete HCU naming migration | `NOTICE`, `README.md`, `README_DCU.md` |
| 2026-07-13 | `de7170db00` | 性能/后端优化 | kernel: migrate DCU ops and wrappers to HCU | `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h` |
| 2026-07-13 | `e3fee4310d` | 模型支持/运行时入口 | ci: sync HCU workflows and scripts with current main | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-11 | `0395a2bd25` | 性能/后端优化 | fix: use lightop int8 deepep moe on dcu | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-07-11 | `390ad18e71` | 性能/后端优化 | ci: 修复 packed KV 测试注册导致的 DCU CI 收集失败 (#87) | `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`, `benchmark/kernels/pack_paged_kv_to_varlen/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/bench_pack_paged_kv_to_varlen.py` |
| 2026-07-09 | `b38f25513e` | 性能/后端优化 | ci: add manual HCU nightly workflow controls | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` |
| 2026-07-09 | `dccf1782b2` | 测试/文档/基准 | ci: disable HCU runtime text check job | `.github/workflows/quality-gate.yml` |
| 2026-07-09 | `d445921fe7` | 性能/后端优化 | 新增对RadixAttention层的判断 | `python/sglang/srt/layers/quantization/w8a8_int8.py` |
| 2026-07-09 | `616ba7b6d6` | 测试/文档/基准 | ci: reduce HCU runtime text check duplicate output | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `d7af9508db` | 调度/缓存/PD | style: apply CI hook formatting | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py` |
| 2026-07-09 | `fda6d44a45` | 测试/文档/基准 | ci: simplify HCU runtime text check failure message | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `8b4a7bdeb5` | 测试/文档/基准 | ci: refine HCU runtime text check message | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `4b0fcbd07e` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C17~C19 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `3e254b0413` | 通用实现调整 | style(distributed): apply pre-commit formatting to parallel_state.py | `python/sglang/srt/distributed/parallel_state.py` |
| 2026-07-09 | `cee45bc550` | 测试/文档/基准 | docs(dcu): record C17-C19 validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `01a6f1b945` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C14~C16 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `b452d6bd67` | 测试/文档/基准 | docs(dcu): record C14-C16 functional validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `1cea713a71` | 测试/文档/基准 | docs(dcu): record C14-C16 validation block | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `b6db54a9a1` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C11~C13 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `5d2c6854a9` | 性能/后端优化 | 0.5.12 MHA、GQA类hicache适配 | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` |
| 2026-07-08 | `bfaf180d14` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C10 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-07 | `fe4e1fea3d` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-07 | `ef36df96f6` | 模型支持/运行时入口 | chore: add header for DCU runtime text checker | `scripts/ci/dcu/check_no_amd_runtime_text.py` |
| 2026-07-07 | `9188d711e5` | 测试/文档/基准 | ci: rename HCU runtime text check script | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/check_no_amd_runtime_text.py` |
| 2026-07-07 | `d5f4d1c14f` | 性能/后端优化 | fix: skip expert distribution recording during CUDA graph capture | `python/sglang/srt/eplb/expert_distribution.py` |
| 2026-07-07 | `9bde26e7c7` | 通用实现调整 | 解耦vllm rms_norm | `python/sglang/srt/layers/layernorm.py` |
| 2026-07-07 | `3f920d4e06` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-07 | `0507e60908` | 缺陷修复 | fix: avoid amdsmi runtime logs on HCU | `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` |
| 2026-07-07 | `4d198708c3` | 性能/后端优化 | 解决sp下对padding的处理 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-07-06 | `cf59f46950` | 缺陷修复 | [bugfix]: avoid HYV3 PD KV compact remap | `python/sglang/srt/disaggregation/common/conn.py` |
| 2026-07-06 | `ec48fa7802` | 缺陷修复 | [bugfix]: 解决hy3开mtp下的精度问题. | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` |
| 2026-07-06 | `23cbd00e31` | 缺陷修复 | [bugfix]: 解决hy3非mtp下的精度问题 | `python/sglang/srt/disaggregation/prefill.py` |
| 2026-07-06 | `a1ed918ae7` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C09 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-06 | `fa6b75971f` | 性能/后端优化 | [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py` |
| 2026-07-06 | `88bb5176c8` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C08 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-05 | `36f3237527` | 性能/后端优化 | fix: refine HCU runtime log wording | `python/sglang/check_env.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-07-04 | `cd2e73a67c` | 性能/后端优化 | 优化lint扫描规则 | `.github/workflows/quality-gate.yml` |
| 2026-07-03 | `8efd2ad46e` | 性能/后端优化 | update w4a16 deepgemm interface | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-03 | `00063277c1` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C07 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-03 | `c3dc2e8eb2` | 通用实现调整 | feat: validate DCU attention backend compatibility | `python/sglang/srt/server_args.py` |
| 2026-07-03 | `ce2521017f` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-02 | `84bd983bad` | 模型支持/运行时入口 | ci: use local DCU reranker model | `.github/workflows/pr-test-dcu.yml` |
| 2026-07-02 | `dd26854396` | 性能/后端优化 | support w4a16 moe ep | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-07-02 | `fc2af93314` | 模型支持/运行时入口 | Add open-source compliance baseline workflow | `.github/workflows/open-source-compliance-baseline.yml` |
| 2026-07-02 | `758a0a9890` | 模型支持/运行时入口 | Add open-source compliance configuration file | `.github/open-source-compliance.json` |
| 2026-07-02 | `6332704295` | 测试/文档/基准 | ci: extend DCU stage-b per-file timeout | `.github/workflows/pr-test-dcu.yml` |
| 2026-07-01 | `ef3571f7b0` | 性能/后端优化 | 解决CI报错问题 | `python/sglang/srt/utils/cuda_ipc_transport_utils.py` |
| 2026-07-01 | `e6d4b3378c` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-01 | `998ffb809b` | 缺陷修复 | fix(fst): reclaim reserved memory after fastsafetensors weight load | `python/sglang/srt/model_loader/loader.py` |
| 2026-07-01 | `696cae936d` | 缺陷修复 | fix(fst): use local device in fastsafetensors iterator for multi-node loading | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-07-01 | `2b1fbe1e6c` | 性能/后端优化 | [CI] fix pre-commit lint errors surfaced after merging v0.5.12_dev | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-07-01 | `35456bae31` | 性能/后端优化 | [CI] fix pre-commit lint errors on megamoe w8a8 changed files | `.codespellrc`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-07-01 | `af015c4ce4` | 调度/缓存/PD | Update Trivy cache volume permissions | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-01 | `72f0237175` | 通用实现调整 | Remove credential keyword pattern from scan config | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-01 | `20f106c6b4` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-01 | `41db24a843` | 通用实现调整 | Enhance quality baseline scan with new checks | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-30 | `445eaafe5d` | 性能/后端优化 | [Perf] optimize aiter asm moe via shuffle weight | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-30 | `ff440b8971` | 测试/文档/基准 | docs(dcu): record C04 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `3910b3f9db` | 缺陷修复 | fix(scheduler): restore DCU empty-prefix location | `python/sglang/srt/managers/schedule_batch.py` |
| 2026-06-30 | `f2d0e86d71` | 性能/后端优化 | fix(dsv4): repair DCU sgl-kernel and JIT build | `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py` |
| 2026-06-30 | `bd10f999c3` | 缺陷修复 | Fix formatting and improve quality gate script | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `412236292d` | 调度/缓存/PD | Modify ruff command to use --no-cache | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `ea182d81e3` | 调度/缓存/PD | Update quality gate workflow with environment variables | `.github/workflows/quality-gate.yml` |
| 2026-06-09 | `c4d3532db8` | 性能/后端优化 | fix:dcu bypass triton normal_decode_set_metadata use normal_decode_set_metadata_lightop | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-03 | `5245654dc1` | 缺陷修复 | Fix: DCU bypass Triton get_last_loc and use native dcu_get_last_loc | `python/sglang/srt/mem_cache/common.py` |
| 2026-06-03 | `4e3fd3a350` | 性能/后端优化 | HY3修改 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-30 | `bda910adb6` | 性能/后端优化 | feat(dcu): integrate LightOp alloc-extend kernel | `python/sglang/srt/mem_cache/allocator.py` |
| 2026-06-30 | `f8b2eefcff` | 通用实现调整 | feat(dsv4): generalize top-k index transformation | `python/sglang/srt/layers/attention/dsv4/indexer.py` |
| 2026-06-30 | `f2e257f7ab` | 性能/后端优化 | feat(dcu): route sqrtsoftplus gating through LightOp | `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-30 | `b76f31cce4` | 通用实现调整 | Refactor quality-gate.yml with enhanced checks | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `93cf8edc41` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `d22548eb14` | 性能/后端优化 | feat(sgl-kernel): port l2norm kernel with tiled optimization for DCU | `python/sglang/srt/layers/attention/fla/l2norm.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/common_extension.cc` |
| 2026-06-30 | `c4cc0a73b6` | 性能/后端优化 | fix(dsv4): preserve DCU elementwise and topk paths | `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` |
| 2026-06-29 | `fa2430f455` | 测试/文档/基准 | Organize DCU nightly workflow modules | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-29 | `01216a18f2` | 测试/文档/基准 | Disable DCU remote weight loading nightly test | `test/registered/distributed/test_load_weights_from_remote_instance.py` |
| 2026-06-29 | `06889adc04` | 调度/缓存/PD | Disable DCU update weights from disk nightly test | `test/registered/rl/test_update_weights_from_disk.py` |
| 2026-06-29 | `0553e12d0a` | 性能/后端优化 | 修复合并分支产生的bug | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-29 | `83294cba6e` | 模型支持/运行时入口 | Add DCU nightly wheel release workflow with vendored-openssl support | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-29 | `395171de08` | 缺陷修复 | test: fix DCU MMMU local dataset selection | `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py` |
| 2026-06-28 | `f40a12fb51` | 性能/后端优化 | 修改IPC逻辑，每个rank下都开辟内存池，解决rank0偶发变慢的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py` |
| 2026-06-26 | `a2076d9aa7` | 测试/文档/基准 | test: use local DCU eval datasets | `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_mmlu.py` |
| 2026-06-26 | `00febcba4a` | 测试/文档/基准 | ci: reuse PR-staged DCU nightly wheels | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-26 | `21dfaaa4c2` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `8aa4b6eb52` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `7d807cb225` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `0c4fe5ebe9` | 测试/文档/基准 | ci: align DCU full wheel wait with PR staging | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-26 | `20eb46a704` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `db4759e78c` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `2f2abec114` | 测试/文档/基准 | ci: cover new DCU nightly suites in full enabled | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-26 | `ca7c7c54fc` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-25 | `c7a4903ad8` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-25 | `9abb848dba` | 性能/后端优化 | [Feat] support megamoe in the path of SGLANG_DCU_MEGA_MOE_RUNTIME=megamoe, and temporarily deepgeem path is still remained as backup | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-25 | `3dd1376ff3` | 缺陷修复 | docs: fix DCU README trailing whitespace | `README_DCU.md` |
| 2026-06-25 | `d1ea0b3aa2` | 模型支持/运行时入口 | ci: support configurable manual DCU model validation | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` |
| 2026-06-23 | `be7d10f53c` | 模型支持/运行时入口 | ci: add manual DCU unattended model test workflow | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` |
| 2026-06-18 | `cae6c44969` | 性能/后端优化 | [FEAT] implement the initial changes about w8a8 megamoe for DCU | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-06-25 | `4a08e1934a` | 性能/后端优化 | test: add DCU nightly 1 and 2 GPU suites | `test/registered/core/test_mm_process_config.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py` |
| 2026-06-25 | `85cd7901c6` | 性能/后端优化 | test: keep verified DCU smoke and accuracy cases only | `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py` |
| 2026-06-24 | `523756bde5` | 调度/缓存/PD | [docs(dcu)] log C01/C02 conflict ledger update | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-24 | `88ba08ad2b` | 性能/后端优化 | fix expert_location_dispatch_info is not define | `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-24 | `595f87c93e` | 测试/文档/基准 | Restore push trigger and CIUpload devpi upload | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-24 | `f4716f8ec5` | 模型支持/运行时入口 | Add DCU nightly wheel release workflow | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-24 | `00ce3e6d95` | 测试/文档/基准 | ci: stage DCU PR wheels locally | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-06-23 | `599b7490f1` | 缺陷修复 | bugfix: fix topk vmfault issue | `python/sglang/srt/layers/attention/dsv4/indexer.py` |
| 2026-06-23 | `9304b9e1da` | 测试/文档/基准 | ci: build DCU gateway wheel by default | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-23 | `de24697cb8` | 测试/文档/基准 | ci: disable PR trigger for DCU nightly workflow | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-23 | `9ed791e147` | 测试/文档/基准 | ci: run PR helper workflows on private runner | `.github/workflows/labeler.yml`, `.github/workflows/pr-states.yml` |
| 2026-06-23 | `ca95a26da7` | 模型支持/运行时入口 | ci: add DCU nightly workflow with wheel build | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-23 | `4b8a743d31` | 模型支持/运行时入口 | ci: add wheel mode to DCU full enabled | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-22 | `fdd9f8ecf3` | 缺陷修复 | [BUG FIX] fix SWA mem pool issue causing accept length decrease | `python/sglang/srt/mem_cache/swa_memory_pool.py` |
| 2026-06-22 | `0536e102c2` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-22 | `5d83cfe857` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-22 | `0fc338999b` | 性能/后端优化 | 修复dpsk r1 fp8启动时的报错问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-18 | `87aa66f4fb` | 性能/后端优化 | [BugFix] workaround fix of aiter custom allreduce in cuda-graph, would revert it after driver fix it | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-06-18 | `37a67648ff` | 调度/缓存/PD | Update Trivy scan configuration in workflow | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `e80c0644ac` | 调度/缓存/PD | Update Trivy and Semgrep commands in workflow | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `fa22ad5aeb` | 性能/后端优化 | Add options for encoding, dependencies, and SAST scans | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-17 | `983e644d4c` | 性能/后端优化 | fix: avoid redundant calls to forward_aiter and fp8 groupgemm kernels | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-12 | `82a5c469c6` | 性能/后端优化 | fix issues of w13_weight using | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-11 | `c0206c7c4a` | 性能/后端优化 | Release original layer.weight after deepgemm_weights conversion to avoid OOM | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-11 | `b3a4160a32` | 性能/后端优化 | 修复dpskv4-flash在pd分离下mtp精度问题 | `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-06-18 | `64fe76840f` | 通用实现调整 | [FEAT] remove vllm allreduce and dead import related | `README_DCU.md`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` |
| 2026-06-18 | `38299f5fbc` | 性能/后端优化 | 修复崩溃bug | `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-18 | `914d50fab3` | 通用实现调整 | Create quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-16 | `de2840d1d6` | 性能/后端优化 | 更新get_scheme函数为get_linear_scheme | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-06-16 | `bb70a2268f` | 性能/后端优化 | [Perf] Add packed paged KV varlen attention path | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`, `python/sglang/srt/server_args.py` |
| 2026-06-16 | `224e5449fb` | 缺陷修复 | [Bug Fix] fix swa mem pool duoble release | `python/sglang/srt/mem_cache/swa_memory_pool.py` |
| 2026-06-16 | `bd52e179c6` | 性能/后端优化 | fix: 修复EP bug | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-06-15 | `fb0a689006` | 通用实现调整 | Rename lint job to lint-dcu to avoid name collision with lint.yml | `.github/workflows/lint-dcu.yml` |
| 2026-06-15 | `bb5f2fc8af` | 测试/文档/基准 | ci: wait for DCU wheels on release workflow changes | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-15 | `548f9aa203` | 测试/文档/基准 | ci: skip GitHub artifact upload for DCU PR wheels | `.github/workflows/release-pr-dcu.yml` |
| 2026-06-15 | `63747e66f9` | 性能/后端优化 | [BugFix] sync to support the more args 'topk_weights' in deep_ep dispatch | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-06-15 | `bc649e255e` | 性能/后端优化 | [BUG FIX] fix swa fa accuracy because of page_table error | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-15 | `9da8b1176d` | 性能/后端优化 | [Feat] support unified fa without layout trans | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-15 | `0cdbfd7b06` | 模型支持/运行时入口 | Add lint-dcu.yml for DCU self-hosted runner, restore original lint.yml | `.github/workflows/lint-dcu.yml`, `.github/workflows/release-pypi-nightky-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-14 | `06331bc257` | 通用实现调整 | Refactor quality gate workflow for changed files check | `.github/workflows/quality-gate.yml` |
| 2026-06-14 | `84cc64ecda` | 通用实现调整 | Create quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-06-14 | `083e22033e` | 测试/文档/基准 | ci: auto-run DCU gate for impact paths | `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/server_args.py` |
| 2026-06-13 | `f9f0cb23d1` | 测试/文档/基准 | ci: auto-run DCU gate for DCU-owned changes | `.github/workflows/pr-test-dcu.yml`, `python/sglang/test/dcu_utils.py` |
| 2026-06-13 | `12a30ab42f` | 测试/文档/基准 | ci: stabilize DCU PR test workflow | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml` |
| 2026-06-11 | `637377248a` | 测试/文档/基准 | ci: install DCU wheel artifacts without dependencies | `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-06-11 | `eda451b27c` | 测试/文档/基准 | ci: pin DCU Engine tests to fa3 backend | `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/sampling/bw1100/test_original_logprobs_dcu.py` |
| 2026-06-11 | `033bc6b92e` | 性能/后端优化 | 重构aiter的重排逻辑 添加aiter log打印信息 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-11 | `52b5b9623c` | 测试/文档/基准 | ci: isolate DCU wheel wait checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-11 | `92a8ba840a` | 性能/后端优化 | [FEAT] cherry-pick and refactor from a0bcfe90, support moe triton backend and fix the acc issue in moe aiter backend | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` |
| 2026-06-08 | `f71c2ef804` | 缺陷修复 | [BugFix] fix the buffer shape unalgined issues of draft model warmup and decode forward in PD phase | `python/sglang/srt/managers/overlap_utils.py` |
| 2026-06-10 | `c066cf42f7` | 模型支持/运行时入口 | ci: add pull-requests:read permission to release-whl-dcu for PR file listing | `.github/workflows/release-whl-dcu.yml` |
| 2026-06-10 | `6b0e35b3fe` | 测试/文档/基准 | ci: prefer python3.9 for verify_dcu_registration on self-hosted runner | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-10 | `cbf9c1ce4d` | 测试/文档/基准 | ci: use self-hosted runner for pr-gate to avoid billing block | `.github/workflows/pr-gate.yml` |
| 2026-06-10 | `adaf77ef92` | 测试/文档/基准 | ci: always prefer self-hosted runner for pre-jobs to avoid billing block | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-10 | `e6e05f3229` | 测试/文档/基准 | ci: test auto-trigger push flow (no-op comment) | `test/registered/dcu/interface/test_dcu_smoke.py` |
| 2026-06-09 | `a6c6527cd9` | 缺陷修复 | fix: pass DCU_CI_USE_INSTALLED_WHEELS into docker container for wheel mode skip | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-09 | `e03bc0cf83` | 缺陷修复 | fix: skip PYTHONPATH assertion in wheel mode for stage-b test | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py` |
| 2026-06-09 | `6d25108aca` | 性能/后端优化 | aiter适配moe_w8a8_fp8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-06-09 | `0f1ea33035` | 模型支持/运行时入口 | ci: add DCU wheel sync path for PR tests | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-whl-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-08 | `1e1d77a76c` | 性能/后端优化 | 解决aiter显存溢出问题 | `.gitignore`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-06-05 | `51abece956` | 测试/文档/基准 | ci: remove DCU CSV coverage analyzer | `scripts/ci/dcu/analyze_dcu_csv_coverage.py` |
| 2026-06-05 | `d6a2b719af` | 模型支持/运行时入口 | ci: map DCU priority metrics model path | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-05 | `823bd922ff` | 测试/文档/基准 | ci: isolate DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `d8f350eedf` | 测试/文档/基准 | ci: avoid dispatch checkout permission issues | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `b95046afa0` | 测试/文档/基准 | ci: guard DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `7694afa394` | 性能/后端优化 | ci: refine DCU suite classification | `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/language/test_srt_backend.py` |
| 2026-06-04 | `cf7567773a` | 模型支持/运行时入口 | ci: map DCU Qwen2.5 0.5B model path | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-04 | `42ffb433b0` | 测试/文档/基准 | ci: avoid ROCR device remap in DCU runner | `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` |
| 2026-06-04 | `cad9d0c351` | 模型支持/运行时入口 | docs: add Apache license notices for DCU SGLang | `README.md`, `README_DCU.md`, `THIRD_PARTY_NOTICES.md` |
| 2026-06-04 | `22e57a7b30` | 测试/文档/基准 | ci: verify DCU full registration in container | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `598f2d61f0` | 模型支持/运行时入口 | ci: use local DCU model env defaults | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-04 | `099123603b` | 测试/文档/基准 | ci: run DCU full workflow on self-hosted runner | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `46efb284a6` | 调度/缓存/PD | ci: update dcu-full-enanled.yml | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `29b6895740` | 调度/缓存/PD | ci: update DCU test registration state | `.github/workflows/pr-test-dcu.yml`, `test/registered/metrics/test_metrics.py` |
| 2026-06-04 | `113d67786f` | 调度/缓存/PD | Update chunk_delta_h.py | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-06-04 | `27ea559793` | 通用实现调整 | 更新tilelang版本到0.1.9 | `python/pyproject.toml` |
| 2026-06-03 | `9022f2c340` | 缺陷修复 | [FIX] Initialize swa_v_head_dim in TritonAttnBackend and cleanup unused import | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-06-03 | `48d234263c` | 测试/文档/基准 | ci: pin DCU CI compatibility packages | `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-06-03 | `c190162be1` | 测试/文档/基准 | ci: clean DCU dispatch validation workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-03 | `494b4246f0` | 测试/文档/基准 | ci: allow DCU dispatch control jobs on runner | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-03 | `43375feaf7` | 测试/文档/基准 | ci: stabilize DCU PR required tests | `.github/workflows/pr-test-dcu.yml`, `python/sglang/__init__.py`, `python/sglang/lang/api.py` |
| 2026-06-03 | `fba9d715f2` | 性能/后端优化 | 修复decode_metadata算子，import不起来的问题 | `sgl-kernel/python/sgl_kernel/__init__.py` |
| 2026-06-03 | `d6baa08091` | 模型支持/运行时入口 | Add DCU wheel release workflow with CIUpload repair and devpi upload | `.github/workflows/release-pypi-nightky-dcu.yml` |
| 2026-06-03 | `f13630b2e2` | 缺陷修复 | fix 修复chunk_delta_h调用报错问题 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-06-03 | `7b86e4afd8` | 性能/后端优化 | 修改aiter prefill阶段的fla算子传参 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py` |
| 2026-06-02 | `a04b5628ec` | 性能/后端优化 | 支持triton版本flash_attn算子，方便排查PA精度问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` |
| 2026-06-01 | `32d9bb7ae2` | 性能/后端优化 | 修复fused_sigmoid_gating_delta_rule_update冲突问题 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-05-30 | `f7022899e5` | 性能/后端优化 | 增加decode_metadata sgl-kernel实现 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/attention/decode_metadata.cu` |
| 2026-05-26 | `5e3749568e` | 性能/后端优化 | 接入lightop layer_norm_fwd_1pass_opt算子实现 | `python/sglang/srt/layers/attention/fla/layernorm_gated.py` |
| 2026-06-02 | `fb2b0297e8` | 测试/文档/基准 | ci: use dcu-ci-pr runner label directly | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `6809e20836` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-06-01 | `cf08ece20a` | 测试/文档/基准 | ci: avoid forcing DCU page size in tests | `python/sglang/lang/api.py`, `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-01 | `40fbcab062` | 测试/文档/基准 | ci: run DCU required include-file set on PR | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `695956fc18` | 测试/文档/基准 | ci: apply DCU runtime defaults in CI | `python/sglang/lang/api.py` |
| 2026-06-01 | `e923247205` | 测试/文档/基准 | ci: route DCU validation to nmz4 runner | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `987a2c813d` | 测试/文档/基准 | ci: default DCU CI server backend to fa3 | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-01 | `ad7aece93b` | 测试/文档/基准 | ci: expand DCU PR validation matrix | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `ada40fccfd` | 测试/文档/基准 | ci: allow full DCU validation from run-ci label | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-01 | `69dd9eb0e2` | 测试/文档/基准 | test: align enabled DCU cases | `python/sglang/test/dcu_utils.py`, `test/registered/metrics/test_metrics.py` |
| 2026-05-25 | `3334b3c5e2` | 性能/后端优化 | [feature support] enable cp+ep by deegemm, ensure deepgemm ver>=da4b9c1 | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-01 | `584a9d2457` | 测试/文档/基准 | ci: allow DCU PR workflow on dcu-ci-pr | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `f0cfe1740f` | 模型支持/运行时入口 | ci: support DCU visible device selection | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-01 | `91b09c4464` | 模型支持/运行时入口 | test: allow DCU CI to override test models | `python/sglang/test/test_utils.py` |
| 2026-06-01 | `8f4d1af5c2` | 测试/文档/基准 | ci: use explicit DCU checkout | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `53a10162c8` | 测试/文档/基准 | ci: clear DCU checkout proxy config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `e362080200` | 测试/文档/基准 | ci: use static DCU git config path | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `6ba549a61c` | 测试/文档/基准 | ci: isolate DCU runner git config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `f7789462f0` | 模型支持/运行时入口 | ci: add DCU full enabled workflow | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-01 | `f981141bef` | 性能/后端优化 | moe_runner适配aiter_w8a8_int8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py` |
| 2026-05-29 | `4b76f0ef57` | 测试/文档/基准 | ci: stabilize DCU PR runner workspace cleanup | `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-05-29 | `35522f4910` | 通用实现调整 | 添加lightop提示信息 | `python/sglang/srt/server_args.py` |
| 2026-05-29 | `6a705f146b` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-05-28 | `93dac7dafa` | 性能/后端优化 | moe-runner-backend支持lightop_moe_w8a8 | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py` |
| 2026-05-28 | `02b73b2d38` | 缺陷修复 | ci: fix DCU local run suite execution | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`, `test/run_suite.py` |
| 2026-05-27 | `74ab583258` | 模型支持/运行时入口 | ci: add DCU PR CI validation flow | `.github/workflows/pr-test-dcu.yml`, `docs/dcu-pr-ci-visual-guide.html`, `python/sglang/test/ci/ci_register.py` |
| 2026-05-22 | `5cff5f5e7f` | 性能/后端优化 | [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0 | `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-05-14 | `5d756f9826` | 缺陷修复 | fix the mtp issues of metadata loc size | `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-04-29 | `9c1c299194` | 缺陷修复 | fix mhc with tile 0.1.9 | `python/sglang/srt/layers/mhc.py` |
| 2026-04-29 | `2e1710ded6` | 性能/后端优化 | fix jit for moe_fused_gate | `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-04-29 | `6236ca8f5d` | 性能/后端优化 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-04-28 | `22d8caf080` | 性能/后端优化 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` |

## 逐 Commit 审计卡

### Commit `594e1ae94c` - [Chore] ci: Remove completed DashHub recovery workflow (#634)

- 完整 hash: `594e1ae94c6103dabed4152a4ebbcca6fb049aeb`
- 时间/作者: 2026-11-02 / guochenyang
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `471ab82545` - Add one-time DashHub recovery for run 41338132822 (#633)

- 完整 hash: `471ab8254520c958d3c614e768a29b10423f7cf2`
- 时间/作者: 2026-11-02 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9fb319cc33` - [CI] optest: Require every enabled operator result (#622)

- 完整 hash: `9fb319cc33a15b624970b0f5e45020e2a573dc07`
- 时间/作者: 2026-10-29 / guochenyang
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `db479b030f` - [CI] optest: Report outcome to DashHub (#619)

- 完整 hash: `db479b030f0975dbda241bf46fc4556a89a02365`
- 时间/作者: 2026-10-29 / guochenyang
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `25aa13e98f` - fix(ci) rebase pr-test-hcu.yml (#617)

- 完整 hash: `25aa13e98fe76d262d87c0b798ec8a3215ffb703`
- 时间/作者: 2026-10-29 / 463975089
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fd98647ed1` - [Fix] ci: Restore previous DashHub operator reporting (#614)

- 完整 hash: `fd98647ed1fc3d911926ea9d399b69934303c104`
- 时间/作者: 2026-10-28 / guochenyang
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `029b6e6418` - [CI] model-ci: Pass history token for daily comparison report (#607)

- 完整 hash: `029b6e6418828280e22086449dfa174433d2788b`
- 时间/作者: 2026-10-28 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `098f31d695` - fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612)

- 完整 hash: `098f31d695ce94169e6adf9ce55109beb532b326`
- 时间/作者: 2026-10-28 / 463975089
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6dac3481cd` - [Fix] ci: Preserve model cases in DashHub operator reporting (#604)

- 完整 hash: `6dac3481cd73b48641f481b14858187d1936ee81`
- 时间/作者: 2026-10-28 / guochenyang
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `a8543c8131` - [CI] cookbook: Add BW1000 deployment smoke tests (#570)

- 完整 hash: `a8543c8131d429500411b8ba235b5411ddbabbd3`
- 时间/作者: 2026-10-20 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f89209aa84` - ci: pass package server to Cookbook model tests (#556)

- 完整 hash: `f89209aa84a4fd0619d0662f6adf6980740efc78`
- 时间/作者: 2026-10-19 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `87b9d5c85e` - Run cookbook deployment checks after HCU image publishing (#548)

- 完整 hash: `87b9d5c85eafab11fe18235718c1af37b348d784`
- 时间/作者: 2026-10-16 / guochenyang
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fc095e0598` - fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533)

- 完整 hash: `fc095e059889d2fae91e86a5b3e5fa19eb8d7a34`
- 时间/作者: 2026-10-15 / chaoyujiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/benchmark/datasets/common.py`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
  - tests: `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cc3758967d` - Pass DashHub credential to deployment smoke controller (#534)

- 完整 hash: `cc3758967d74748204015a050182e5ad176c8a08`
- 时间/作者: 2026-10-15 / guochenyang
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `78c700ee01` - Add image input to cookbook deployment smoke workflow (#530)

- 完整 hash: `78c700ee0100f215268a3a802538881f281f29e2`
- 时间/作者: 2026-10-14 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e295faff5d` - update ci name&&add optest log (#515)

- 完整 hash: `e295faff5dc889c97626f7bd25f6a8ca0a0f100c`
- 时间/作者: 2026-10-12 / Lee156
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b6dd37e66a` - Run cookbook smoke tests for all cases by default

- 完整 hash: `b6dd37e66ad4f820a75614c8b0e6f54ffa67c796`
- 时间/作者: 2026-10-12 / gcy
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f9b972b372` - Use a clean checkout directory for the model smoke controller (#510)

- 完整 hash: `f9b972b372f8695154301e2d7cee24195a963250`
- 时间/作者: 2026-10-12 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `50b0d00518` - Delegate HCU model deployment smoke CI to external controller (#503)

- 完整 hash: `50b0d005189ee23cf3046b86dc44986c5e6b9345`
- 时间/作者: 2026-10-12 / guochenyang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `3b0e4a0739` - [Fix] Bound crash diagnostics and fatal shutdown on main (#498)

- 完整 hash: `3b0e4a07393778001dcd518d2b11de225e1be8c8`
- 时间/作者: 2026-10-10 / 王启宇
- 自动分类: 性能/后端优化
- 主要文件: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`, `test/registered/unit/utils/test_bounded_fatal_shutdown.py`, `test/registered/unit/utils/test_bounded_pyspy.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/docs/references/environment_variables.mdx`
  - other: `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-perf: `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`
  - tests: `test/registered/unit/utils/test_bounded_fatal_shutdown.py`; `test/registered/unit/utils/test_bounded_pyspy.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4205397cbc` - add password-free download code (#499)

- 完整 hash: `4205397cbcf8c60852fadd7306cea32f2541a19d`
- 时间/作者: 2026-10-10 / Lee156
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f0ee2a5059` - FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473)

- 完整 hash: `f0ee2a5059c2d6a167bee3d996bca004276b3138`
- 时间/作者: 2026-10-09 / JackPeng
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_detokenizer_incremental.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `fb46d17ad9` - add optest process (#481)

- 完整 hash: `fb46d17ad9f633aa7fee521484262b0c26de560d`
- 时间/作者: 2026-10-09 / Lee156
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e05f146bed` - ci(hcu): migrate main workflows to organization runners (#463)

- 完整 hash: `e05f146bed9ca80c72a18a4946fd6f838d8e7774`
- 时间/作者: 2026-09-30 / dingxinlong
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/pr-states.yml` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/pr-states.yml` 等 12 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `5e8269d55a` - [BUGFIX]镜像DTK版本号不对 (#447)

- 完整 hash: `5e8269d55a8cf4629cc39a3171169f4aa8b4d14b`
- 时间/作者: 2026-09-28 / Crowder13
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `665b27d1fa` - feat(ci) fix main build whl failed (#449)

- 完整 hash: `665b27d1fa35017a437b0aa0099a5f8aa33e5d9b`
- 时间/作者: 2026-09-24 / 463975089
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f2d49c2c0e` - FIX(DSV4): 补全 system/reminder 结尾对话的 assistant 生成前缀并解析 markdown 伪工具调用 (#435)

- 完整 hash: `f2d49c2c0e3cb3ca4dd89130cb5e2a408b0ac54b`
- 时间/作者: 2026-09-23 / JackPeng
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`, `python/sglang/srt/function_call/deepseekv4_detector.py`, `test/registered/unit/function_call/test_deepseekv4_detector.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/function_call/deepseekv4_detector.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`
  - tests: `test/registered/unit/function_call/test_deepseekv4_detector.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `7be1324cf8` - ci: report sglang nightly packages to DashHub (#424)

- 完整 hash: `7be1324cf827dafe9f09ec3f86ade353801b5e1e`
- 时间/作者: 2026-09-23 / guochenyang
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2871c8fdd9` - ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438)

- 完整 hash: `2871c8fdd9594de894546b144d253c3dd88fd900`
- 时间/作者: 2026-09-23 / Crowder13
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b5ca753bc8` - ci(hcu): run nightly against v0.5.18 and report its results (#432)

- 完整 hash: `b5ca753bc8e054ce99b4c01b0369eb89c6870dbb`
- 时间/作者: 2026-09-22 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `a981685e7f` - fix release-pr-hcu.yml build sglang (#423)

- 完整 hash: `a981685e7f137a9e0629cbdcad2ad7bdd42017b9`
- 时间/作者: 2026-09-21 / 463975089
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `cb932f5fbd` - feat(ci) compaity sgl-kernal main to v0.5.12 (#421)

- 完整 hash: `cb932f5fbd904a577093a262c6a101834a1ef994`
- 时间/作者: 2026-09-21 / 463975089
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ae5c33991b` - Update quality gate workflow to use stable version

- 完整 hash: `ae5c33991be7f0e277f71c4e853c10fc11cbe627`
- 时间/作者: 2026-09-21 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `adc1d69b2a` - ci(hcu): align main wheel builds with 0.5.18 runtime (#379)

- 完整 hash: `adc1d69b2a610fc000ca27e4b92c72e9c1b85044`
- 时间/作者: 2026-09-16 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/test_hcu_build_alignment.py`, `scripts/ci/hcu/test_hcu_wheel_version.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/test_hcu_build_alignment.py`; `scripts/ci/hcu/test_hcu_wheel_version.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `5c03a8e22f` - [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376)

- 完整 hash: `5c03a8e22f8cfeef0f10cd909231862bd446cc30`
- 时间/作者: 2026-09-15 / Crowder13
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ae14a99e50` - fix(ci): fix HCU wheel build target routing (#372)

- 完整 hash: `ae14a99e502d0e5dbed8abf42e3b35eb8807c3c5`
- 时间/作者: 2026-09-15 / tianly
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `7c8272a3a3` - [BUGFIX]更新AICC安装方式 (#367)

- 完整 hash: `7c8272a3a32d25391c8bc20e0c0678d3c9ac895d`
- 时间/作者: 2026-09-15 / Crowder13
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `575cf47976` - ci(hcu): restore source mode for test-only PRs (#364)

- 完整 hash: `575cf47976761be9916048cfe2ca244b56d63fab`
- 时间/作者: 2026-09-14 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `516261baf1` - ci(hcu): register sampling test and adjust MMLU threshold (#359)

- 完整 hash: `516261baf108e56bcb4a03dc7294a936e9656a2d`
- 时间/作者: 2026-09-14 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b5108cc7fe` - ci(hcu): use v0.5.18 image and restore eval dependencies (#347)

- 完整 hash: `b5108cc7fea82d75da174f8f6681a843d43c462b`
- 时间/作者: 2026-09-14 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/utils/sgl_eval_ref.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/utils/sgl_eval_ref.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `0af71f61b6` - fix(ci): update HCU evaluation dependencies and asset paths (#325)

- 完整 hash: `0af71f61b693c2bd2817a678e007660222db9bf3`
- 时间/作者: 2026-09-08 / tianly
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0457572a14` - [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308)

- 完整 hash: `0457572a14edd55e05220726ff4a8af8b1931771`
- 时间/作者: 2026-09-04 / Crowder13
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2828bde71d` - ci(hcu): align llguidance and model asset paths (#299)

- 完整 hash: `2828bde71da3f5f6314aa4022ae7e163dfc33ada`
- 时间/作者: 2026-09-03 / dingxinlong
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `6fe7ce9097` - ci(hcu): restore run suite file filters (#290)

- 完整 hash: `6fe7ce9097c8e9f1b7dccefbe4834a7f928a78c2`
- 时间/作者: 2026-09-02 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `9d261478d6` - [CI] Update HCU model asset paths on main (#285)

- 完整 hash: `9d261478d6ace185f3e35a7211fc411b64d2057f`
- 时间/作者: 2026-09-02 / dingxinlong
- 自动分类: 性能/后端优化
- 主要文件: `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_exec.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/spec/test_ngram_speculative_decoding_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `8fa7122b3a` - [FEATURE]构建镜像之后触发模型测试 (#277)

- 完整 hash: `8fa7122b3ace4a4de48372ee3c4c3346871281d7`
- 时间/作者: 2026-09-01 / Crowder13
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
  - other: `docker/image-citest-conf-hcu.yaml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e864c30287` - ci: enable HCU PR tests for release branches (#272)

- 完整 hash: `e864c302870000325162a5788883997cc850ade8`
- 时间/作者: 2026-08-31 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `3ca61517d0` - ci-remove-amd-status-from-pr-summaries

- 完整 hash: `3ca61517d037e82ba19c981dd66ddaf0245e85cd`
- 时间/作者: 2026-08-31 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-states.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-states.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `bc990ebd52` - [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复)

- 完整 hash: `bc990ebd52e0ae2500dc3c0ab4eeba187e84965b`
- 时间/作者: 2026-08-28 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `68dcd498aa` - [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致

- 完整 hash: `68dcd498aa7550a39e7f53b6588e19785efd5cae`
- 时间/作者: 2026-08-28 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6b468d012b` - [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda

- 完整 hash: `6b468d012bcf693157cee193493842185165b93b`
- 时间/作者: 2026-08-27 / zhangyh15
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `7609d9af69` - [feature]适配hcu发包

- 完整 hash: `7609d9af69ac40ed6730564cde4934d5b3e4a540`
- 时间/作者: 2026-08-27 / zhangyh15
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`; `python/pyproject_hcu.toml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2866df9948` - ci(hcu): trust wheel build workspaces

- 完整 hash: `2866df9948b40e81405fcf5947ef74b8f744c9a3`
- 时间/作者: 2026-08-27 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `a2de3b8cff` - ci(hcu): use bash for wheel build jobs

- 完整 hash: `a2de3b8cffc365e5f813d2ddd6c7226abe29db90`
- 时间/作者: 2026-08-26 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f6d701c520` - Fix stale HCU Stage B test paths

- 完整 hash: `f6d701c520529490926e3c350682b7fe7ca6f9d0`
- 时间/作者: 2026-08-26 / reverie-hub
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c94c3ca2c8` - fix: gateway wheel is at workspace root target/wheels

- 完整 hash: `c94c3ca2c8341c501b46a32c750e32dfe8ce4e06`
- 时间/作者: 2026-08-26 / zhangyh15
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `8dd5daf2fa` - Refine HCU and AMD CLI help text

- 完整 hash: `8dd5daf2fa5555ab13751b159703124fd493a437`
- 时间/作者: 2026-08-26 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/srt/server_args.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/run_suite.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `990a1a798d` - ci: disable scheduled gateway nightly release

- 完整 hash: `990a1a798d40ccea97ef91c16a9d8cd8f25957e2`
- 时间/作者: 2026-08-26 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-release-gateway.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-release-gateway.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fd41570479` - Refine HCU platform diagnostics and CLI help

- 完整 hash: `fd415704795411fa8fcbc7d7571c41dcb3d1c431`
- 时间/作者: 2026-08-24 / reverie-hub
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d42ecf6fe9` - Fix HCU detection and sanitized topology diagnostics

- 完整 hash: `d42ecf6fe9854d6127c167959fe7bec30439b73b`
- 时间/作者: 2026-08-21 / reverie-hub
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6a4a61efba` - ci(hcu): detect runner workspace ownership

- 完整 hash: `6a4a61efba7f1a2d75bfe132d6589a459a0f2c1c`
- 时间/作者: 2026-08-25 / dddddddxl
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `3e6aaf09d8` - ci(hcu): allow fork checkout in target workflows

- 完整 hash: `3e6aaf09d878c40268294082de2abf032911bf1a`
- 时间/作者: 2026-08-25 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f2fc4e166b` - Update quality gate workflow to version 2.0.3

- 完整 hash: `f2fc4e166b64086a0ef22e99a96046bd5acf4cc1`
- 时间/作者: 2026-08-25 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `69c73a1787` - ci(hcu): support fork pull requests

- 完整 hash: `69c73a1787bdd189d88ba7cb3240dc34c46663a7`
- 时间/作者: 2026-08-25 / dddddddxl
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `94e9fa4b1d` - ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload)

- 完整 hash: `94e9fa4b1d10f14c6120bab4f5416caf6e318cd9`
- 时间/作者: 2026-08-25 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `59213c7e48` - Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED

- 完整 hash: `59213c7e48c978859b7086524aab5b0ccb500fc4`
- 时间/作者: 2026-08-25 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d1adf7b503` - [feature] manual compile ci

- 完整 hash: `d1adf7b503b20e64e07c38946a067ee90c428962`
- 时间/作者: 2026-08-25 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c40703e6b4` - fix(ci): clear the three Quality Gate blockers from the 20260824 sync

- 完整 hash: `c40703e6b494756f882f1e052d2d574350e5591a`
- 时间/作者: 2026-08-25 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/srt/server_args.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/nightly-test-npu.yml`
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `261b8627f1` - fix(hcu): restore 29 environ declarations the sync auto-merge dropped

- 完整 hash: `261b8627f107f553e26ce43b74d052c28a676bfd`
- 时间/作者: 2026-08-24 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/sync-official-main-20260824-summary.md`
  - other: `python/sglang/srt/environ.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `37c5b30bb9` - fix: extract full DTK version for three-part versions

- 完整 hash: `37c5b30bb9f24bbac284e5598a9219f71b6c06bf`
- 时间/作者: 2026-08-20 / zhangyh15
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-dcu.yml`; `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-dcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `a96aed11f0` - [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子

- 完整 hash: `a96aed11f05f65d18f5bd46446b4ca9b7ac82105`
- 时间/作者: 2026-08-21 / zhuwenbopro
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `27ce43c71d` - [fix]solved CI Test errors

- 完整 hash: `27ce43c71d9194fd473370a19f354e755b5ade86`
- 时间/作者: 2026-08-20 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `72d1d2a73a` - [fix]solved other CI Test errors

- 完整 hash: `72d1d2a73af94d8cdef717fd46cacf331665b32e`
- 时间/作者: 2026-08-20 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f6b66222a0` - revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0

- 完整 hash: `f6b66222a00a63851345729b7acd8d9855c2e184`
- 时间/作者: 2026-08-20 / zhangyh15
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `11d08002bf` - [fix]solved CI Test errors

- 完整 hash: `11d08002bfd60e96b4ff4d1210a69678a70de801`
- 时间/作者: 2026-08-20 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/arg_groups/overrides.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b628d29e1c` - [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本

- 完整 hash: `b628d29e1c2e33e291e647991eab213bc9c5dcc8`
- 时间/作者: 2026-08-20 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fb7369fec0` - [bugfix]删除无关文件

- 完整 hash: `fb7369fec0d5fd3a6bbb45515c95fba0ffc4efbf`
- 时间/作者: 2026-08-20 / chenyuege
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `62a07586d9` - [feat] 适配HCU FA3

- 完整 hash: `62a07586d98059ba83cf0b1a2e1d6496a8de2bed`
- 时间/作者: 2026-08-20 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`, `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9bbf3799d8` - docs(hcu): add the 20260817 official backport validation report

- 完整 hash: `9bbf3799d827a26d6768d569fc652b9837a31425`
- 时间/作者: 2026-08-17 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/backport-official-20260817-validation-report.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/backport-official-20260817-validation-report.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `fa309a1e19` - fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE

- 完整 hash: `fa309a1e19c40cd15a9f5cf6a14e8f0b701211f9`
- 时间/作者: 2026-08-14 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5e2ba659ea` - fix lint: apply pre-commit fixes to the dspark bugfixes

- 完整 hash: `5e2ba659ea4a3780b4c175940bd2537f5d34f56b`
- 时间/作者: 2026-08-13 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/speculative/dflash_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/speculative/dflash_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `18e167b730` - [BugFix] fix the client inference None errors in temperature>0 with a torch implementation

- 完整 hash: `18e167b7304e0cb9cc11094cc7f012ce630fd9fe`
- 时间/作者: 2026-08-13 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/speculative/dflash_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/speculative/dflash_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `54e3ed50f6` - [BugFix] fix the runtime errors in ep+dspark mode

- 完整 hash: `54e3ed50f6c00f8d1905841b9ab394efbebe213b`
- 时间/作者: 2026-08-13 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/speculative/dspark_components/dspark_draft.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/dspark_components/dspark_draft.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `fb7f119564` - ci(hcu): adapt wheel jobs to CIUpload 0.3

- 完整 hash: `fb7f119564646fcafbf36ae11361998223e3fa2b`
- 时间/作者: 2026-08-12 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2083c069f7` - fix lint: apply pre-commit fixes to the EP MoE fallback change

- 完整 hash: `2083c069f76aaa38db41ea78ea17157ef9532f02`
- 时间/作者: 2026-08-12 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ccbb65acb2` - [HCU][DSpark] Fix DP EP MoE fallback routing

- 完整 hash: `ccbb65acb26c1d42fbc729767c6b5d87caddb827`
- 时间/作者: 2026-08-11 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b36730b417` - fix lint: apply pre-commit fixes to the mHC EAGLE changes

- 完整 hash: `b36730b41733f8ddd3a4754210230067b1587ffb`
- 时间/作者: 2026-08-10 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_common.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5fd89c7288` - [BugFix] fix the inference tensor graph replay issues in MTP mode

- 完整 hash: `5fd89c72883270f2f931f07daee28a78fde2dbcb`
- 时间/作者: 2026-08-10 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/speculative/eagle_worker_common.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `4a6fbed985` - [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config

- 完整 hash: `4a6fbed98571481aae473799555ed3b3fd46d493`
- 时间/作者: 2026-08-10 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e3a9d595c9` - [HCU][DSpark] Fix sampling parameter updates after graph capture

- 完整 hash: `e3a9d595c9e048425141f6f384bd8cfd87ec5f85`
- 时间/作者: 2026-08-10 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3de1323a9b` - ci(hcu): normalize rebased PD suite names

- 完整 hash: `3de1323a9b955c7395391660c8efd531fccc733b`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/README.md`; `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`; `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3fbc8ae9ef` - test(hcu): align numerical references with v0.5.15

- 完整 hash: `3fbc8ae9efa869b6a4229021cae7af09419658a4`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/hcu/kernels/test_attention_reference_hcu.py`, `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/kernels/test_attention_reference_hcu.py`; `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `76ced479ea` - test(hcu): use v0.5.15 FP8 kernel path

- 完整 hash: `76ced479ea28a5d4f34c47e225bc7d416efa350c`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `ecf4756cea` - test(hcu): isolate server guard unit test

- 完整 hash: `ecf4756cea2d3d9a08a50dfc1fb0b4342a3fe3cc`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/hcu/test_hcu_server_guard.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `scripts/ci/hcu/test_hcu_server_guard.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dc5cd70892` - ci: finalize v0.5.15 workflow policy

- 完整 hash: `dc5cd708920beaa8c6b76be7ddc72cb1b4e6a2ce`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/ci-auto-bisect.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/slash-command-handler.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/ci-auto-bisect.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/slash-command-handler.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `50736ebe71` - ci(hcu): keep migration changes scoped

- 完整 hash: `50736ebe711fa247f945d601cfb9de438ee711a0`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `README_HCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_HCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `1a5ce1750d` - ci(hcu): publish reasoning results to shared storage

- 完整 hash: `1a5ce1750db03d590d791dbf4544c2109a46aeaa`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`, `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`; `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `4c7a264e5c` - ci(hcu): align model assets and selected-ref kernel

- 完整 hash: `4c7a264e5ce84e1d09a9c84158b0f104fb22cac1`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `92ce544fac` - ci: align v0.5.15 workflow triggers

- 完整 hash: `92ce544fac3ddcde09fe4bc8524adb32c7722aed`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml`, `.github/workflows/release-docker-runtime.yml`, `.github/workflows/release-docker-xeon.yml`, `.github/workflows/release-docker.yml`, `.github/workflows/release-pypi.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/bot-bump-docs-version.yml`; `.github/workflows/release-docker-amd.yml`; `.github/workflows/release-docker-npu.yml`; `.github/workflows/release-docker-runtime.yml`; `.github/workflows/release-docker-xeon.yml`; `.github/workflows/release-docker.yml`; `.github/workflows/release-pypi.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b59995e42d` - fix(hcu): point PD smoke tests at a declared HCU suite

- 完整 hash: `b59995e42dc3fb5d985b435a81ae97e16bbe0163`
- 时间/作者: 2026-08-07 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/README.md`; `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`; `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `154a88c7b7` - fix lint: apply isort/black to the lmslim->lightop migration

- 完整 hash: `154a88c7b748bd7ce4520194cdc94ced19e53439`
- 时间/作者: 2026-08-07 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b0f2bb3a84` - fix(hcu): restore network_mode matrix keys dropped by the forward-port

- 完整 hash: `b0f2bb3a84643e29eda30adb48c3aaa6e3b8bf6c`
- 时间/作者: 2026-08-06 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f17440f19f` - fix(hcu): restore original license headers dropped by the forward-port

- 完整 hash: `f17440f19f7168bbcf12e8bd5e1015b684360b88`
- 时间/作者: 2026-08-06 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_start_container.sh`
  - tests: `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `8e2aba4bfa` - fix lint: apply isort/black to forward-port diff

- 完整 hash: `8e2aba4bfa849b33963017aa074ddeb4d9710e98`
- 时间/作者: 2026-08-06 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_pd.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_pd.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/decode_attention.py`; `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f1c6f56315` - fix(hcu): drop leftover source hunks that renaming and partial takes left behind

- 完整 hash: `f1c6f56315d32e9184e1584be65a41f9f2efe221`
- 时间/作者: 2026-08-06 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dabae6b13a` - fix(ci): use PR files API for HCU wheel detection

- 完整 hash: `dabae6b13a2b6be718650ecbf51887ca0b70245b`
- 时间/作者: 2026-08-05 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `44bb481cf9` - fix(eplb): apply expert ID remapping for HCU fused TopK

- 完整 hash: `44bb481cf9550fb79ebc8302290b1ce224cb2f76`
- 时间/作者: 2026-08-05 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2fb37eaace` - fix(ci): align HCU Python wheel paths

- 完整 hash: `2fb37eaacebb19abafa369cc3d2de779b064bb3b`
- 时间/作者: 2026-08-05 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `71de6dd93d` - fix(ci): align HCU gateway wheel detection

- 完整 hash: `71de6dd93d32de13cdf3f91f0a1ea2c5bf507084`
- 时间/作者: 2026-08-05 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2a342cdf1d` - fix fp8 bug of triton

- 完整 hash: `2a342cdf1d656a8620a6a1657f471f6ee0e20aa7`
- 时间/作者: 2026-08-05 / sunjf
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/triton_ops/decode_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_ops/decode_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8160ebe53c` - fix(hcu): retain PD decode adapter callbacks

- 完整 hash: `8160ebe53c68d03beacbd1f29c269566f4309246`
- 时间/作者: 2026-08-04 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `43d8d9ac1b` - style(hcu): fix lint for KME W8A8 lightop path

- 完整 hash: `43d8d9ac1b8501ad32ab508f39af689ceb23a742`
- 时间/作者: 2026-08-04 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e8298ba909` - fix(hcu): restore DP decode protocol constants

- 完整 hash: `e8298ba909f62fb2d3511b9d1e9544bee60aaca2`
- 时间/作者: 2026-08-04 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `083d1d8b99` - fix(hcu): restore DeepGEMM PD helper and current cache API

- 完整 hash: `083d1d8b992fe769814bff832efdafc53f758028`
- 时间/作者: 2026-08-04 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cd60b74339` - 修改hicache+pp并行 stage不一致问题commit提交格式

- 完整 hash: `cd60b7433981dba9d7a90662e846ca29191fa4ee`
- 时间/作者: 2026-08-04 / xinleishang
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `143ee92872` - refactor(hcu): route KME W8A8 hipBLASLt through lightop

- 完整 hash: `143ee92872293cbe7d7224a58e0c2d6c5233f444`
- 时间/作者: 2026-08-03 / yht183
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `84bfd45c44` - 修复hicache+pp并行 stage不一致问题

- 完整 hash: `84bfd45c449c950b91a38740e48bab4a25fa1da8`
- 时间/作者: 2026-07-29 / shangxl
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/cache_init_params.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `015f6d49a0` - fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info

- 完整 hash: `015f6d49a06bfc7caffecf3dfb77b3c0a46f5ffe`
- 时间/作者: 2026-08-03 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/forward_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `de696eab9c` - Update quality gate workflow to version 2.0.1

- 完整 hash: `de696eab9cacc8b2f9c8473e5f5ca7f782a36a66`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e6c4102592` - Update quality gate workflow to version 2.0.1

- 完整 hash: `e6c41025927c2e15120f7ee8911005f5890adef5`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `3358846e55` - Update quality-gate.yml

- 完整 hash: `3358846e556ef4229eb098e45a99098be1b1b8ad`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `4d3aaf6aff` - Update quality gate workflow for versioning and concurrency

- 完整 hash: `4d3aaf6affc573b265df1c77a4620178d8c7f1a8`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `286612da40` - Update quality gate workflow to use version v2.0.0

- 完整 hash: `286612da40c357f62499b1b177636a3d2451ff14`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ff7f44b8ed` - Update quality gate workflow to use version v2.0.0

- 完整 hash: `ff7f44b8edf3acf125c9f73d8189997281766d83`
- 时间/作者: 2026-08-03 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `67ecec8dd1` - fix(hcu): scope Feishu status to accuracy results

- 完整 hash: `67ecec8dd142bd6da48507abe89a927649e094c2`
- 时间/作者: 2026-08-03 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `85dcec9474` - fix(hcu): support Python 3.8 in Feishu notifier

- 完整 hash: `85dcec9474c249b7e27f7c8fc87e8b485ae09155`
- 时间/作者: 2026-07-31 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9c69436eed` - fix(hcu): remove resend tool dependencies

- 完整 hash: `9c69436eed95e4c78f8a0707ff90094c6464eb1a`
- 时间/作者: 2026-07-31 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `0ff7a014fe` - ci(hcu): support resending Feishu accuracy results

- 完整 hash: `0ff7a014fe80fd0aa1a16173e3b874d11e288dae`
- 时间/作者: 2026-07-31 / LvJIA-RG
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f556d3896e` - [FIX] 修复lmslim和lightop接口冲突问题 (#154)

- 完整 hash: `f556d3896e67a4e4476fff375166621e2710f177`
- 时间/作者: 2026-07-31 / yangyn
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b489942109` - ci: install PyYAML for slash command handler (#156)

- 完整 hash: `b489942109fbe97885ce38e1abf362d2e867aa0e`
- 时间/作者: 2026-07-31 / dingxinlong
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/slash-command-handler.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/slash-command-handler.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `497c35457c` - fix(scheduler): abort too-large requests instead of dead-looping

- 完整 hash: `497c35457c32dde206f04796930e3e03ad1f80e1`
- 时间/作者: 2026-07-31 / chaoyujiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dc015a0bc5` - [PD] When PP is greater than 1, fix the request rollback when the KV cache is exhausted

- 完整 hash: `dc015a0bc5595bdd2e4e77d3d4f7953399a4cc64`
- 时间/作者: 2026-07-31 / liucong521
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `83f43b3f4d` - [CI] Fix some CI errors

- 完整 hash: `83f43b3f4dd0c183c4226942384b9bda85a3c8ab`
- 时间/作者: 2026-07-31 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `39d6912202` - fix(hcu): restore NETWORK_MODE default lost in forward-port

- 完整 hash: `39d6912202326be716e7f6a179addfd308b6d45c`
- 时间/作者: 2026-07-31 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_start_container.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_start_container.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `02968a96de` - fix(hcu): restore shared wheel staging root lost in forward-port

- 完整 hash: `02968a96de98145237578ec039464f6c85554c23`
- 时间/作者: 2026-07-31 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `17cf690afc` - style: fix HCU lint checks

- 完整 hash: `17cf690afc87f262966f51e2495eff98f731b6fd`
- 时间/作者: 2026-07-30 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py`, `python/sglang/srt/speculative/eagle_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_info.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/lightop.py`; `python/sglang/srt/layers/quantization/__init__.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `489170e5c4` - [FIX] 修复moe_w8a8重排函数删除问题

- 完整 hash: `489170e5c4bec22fb94ea9e7c2b902ac42165db4`
- 时间/作者: 2026-07-30 / yangyinan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/lightop.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/lightop.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6ea38ee522` - style(hcu): format PD helper registration

- 完整 hash: `6ea38ee522bd17db34111d6a1a784fc22c0008e4`
- 时间/作者: 2026-07-30 / LvJIA-RG
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/disaggregation/pd_hcu_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/disaggregation/pd_hcu_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b8389e5c5d` - test(hcu): register PD helper for nightly collection

- 完整 hash: `b8389e5c5da4629791f8d56e2a216dd91c5516ab`
- 时间/作者: 2026-07-30 / LvJIA-RG
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/disaggregation/pd_hcu_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/disaggregation/pd_hcu_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `111fea82f3` - ci: disable unused workflow triggers

- 完整 hash: `111fea82f3bf103b2f369bb75191364b144e5623`
- 时间/作者: 2026-07-29 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml`, `.github/workflows/ci-model-inventory.yml`, `.github/workflows/lint.yml`, `.github/workflows/nightly-amd-mi355x-disagg.yml`, `.github/workflows/nightly-experimental-sgl-router-docker.yml`, `.github/workflows/nightly-test-amd-miles-rocm700.yml` 等 36 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/ci-coverage-overview.yml`; `.github/workflows/ci-model-inventory.yml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-amd-mi355x-disagg.yml`; `.github/workflows/nightly-experimental-sgl-router-docker.yml`; `.github/workflows/nightly-test-amd-miles-rocm700.yml` 等 36 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b2f0b830c2` - ci: disable unused workflow triggers

- 完整 hash: `b2f0b830c298611c1e11ef9438f8abfd83f7fbe1`
- 时间/作者: 2026-07-29 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml`, `.github/workflows/ci-model-inventory.yml`, `.github/workflows/lint.yml`, `.github/workflows/nightly-amd-mi355x-disagg.yml`, `.github/workflows/nightly-experimental-sgl-router-docker.yml`, `.github/workflows/nightly-test-amd-miles-rocm720.yml` 等 39 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/ci-coverage-overview.yml`; `.github/workflows/ci-model-inventory.yml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-amd-mi355x-disagg.yml`; `.github/workflows/nightly-experimental-sgl-router-docker.yml`; `.github/workflows/nightly-test-amd-miles-rocm720.yml` 等 39 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `be81ab4196` - fix(dp): demote DP Decode StepInfo log to debug

- 完整 hash: `be81ab41964147b7a61aba65f26d2d33a689a5ea`
- 时间/作者: 2026-07-29 / yht183
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6a031254f5` - ci(hcu): isolate nightly services and shared results

- 完整 hash: `6a031254f52863cdd573365e3ad48dbcd78c4be8`
- 时间/作者: 2026-07-29 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_publish_accuracy.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e18e6b94bc` - docs(hcu): record daily forward-port 20260729

- 完整 hash: `e18e6b94bcf8c69103f286699960278ee4804b87`
- 时间/作者: 2026-07-29 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3b4327cd7b` - fix(hcu): support current LightOp fp8 quant API

- 完整 hash: `3b4327cd7bb428ab98828f0cdc31106d51cd86b2`
- 时间/作者: 2026-07-29 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `58d475775e` - fix(hcu): allow single-node context parallel tp16

- 完整 hash: `58d475775e6e87052ebe90aa302ccf7326b85385`
- 时间/作者: 2026-07-29 / maxiaobetter
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d39d628ef3` - fix(hcu): enable NSA draft-extend cuda graph

- 完整 hash: `d39d628ef31bd4d189624224ecd44e1bcf98ed36`
- 时间/作者: 2026-07-29 / maxiaobetter
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4e5a95fcb5` - fix(pd): transfer MTP NSA topk seed metadata over Mooncake

- 完整 hash: `4e5a95fcb50cb1872b03340b214c20aa55b0ce4d`
- 时间/作者: 2026-07-29 / maxiaobetter
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6e7a53e865` - fix(hcu): select hipblaslt w8a8 layout by gfx arch

- 完整 hash: `6e7a53e865615d9376c4db7b6b16eeffec68a479`
- 时间/作者: 2026-07-29 / maxiaobetter
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `035ca766ff` - fix(cache): forward Mamba indices in NSA offload

- 完整 hash: `035ca766ff24dc88ee6486957d6c8235e63c3706`
- 时间/作者: 2026-07-28 / maxiaobetter
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `049f5e15ee` - [bugfix] 透传apply_routed_scaling_factor_on_output，防止moe_sum多乘routed_scaling_factor

- 完整 hash: `049f5e15eef71c041918f850a5fecf0ce04f789c`
- 时间/作者: 2026-07-29 / whlwhlwhl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `92e95e3f51` - perf(mamba): flatten fused state scatter launch grid

- 完整 hash: `92e95e3f5154a717d811c3df99c72a451f661e10`
- 时间/作者: 2026-07-29 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bfa4011ad0` - ci(hcu): share wheel staging across runners

- 完整 hash: `bfa4011ad04d14c26a6af6b90ea2d82b84c874c9`
- 时间/作者: 2026-07-29 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fc59c96c54` - fix lint: format line breaks and remove trailing whitespace

- 完整 hash: `fc59c96c548711bef75180568c1575cb4dd891db`
- 时间/作者: 2026-07-28 / chaoyujiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `7b89bf6617` - fix: propagate return_hidden_states_before_norm flag for mHC target-verify

- 完整 hash: `7b89bf661791997607231bf19e8f9e633a4e6526`
- 时间/作者: 2026-07-28 / chaoyujiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/model_executor/cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d0c4729899` - ci: add HCU PD disaggregation smoke tests

- 完整 hash: `d0c47298995a2bff260743f3f877f84d5b23462f`
- 时间/作者: 2026-07-28 / tianlinyang77
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/disaggregation/pd_hcu_utils.py`, `test/registered/hcu/disaggregation/test_pd_basic_hcu.py`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`, `test/registered/hcu/disaggregation/test_pd_pp_hcu.py`, `test/registered/hcu/disaggregation/test_pd_transfer_backends_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/disaggregation/pd_hcu_utils.py`; `test/registered/hcu/disaggregation/test_pd_basic_hcu.py`; `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`; `test/registered/hcu/disaggregation/test_pd_hcu_utils.py`; `test/registered/hcu/disaggregation/test_pd_pp_hcu.py`; `test/registered/hcu/disaggregation/test_pd_transfer_backends_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cd4802bbab` - fix lint

- 完整 hash: `cd4802bbabdbfe22966cedac25f34e74df510b21`
- 时间/作者: 2026-07-28 / chaoyujiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0305c5a3b9` - fix lint

- 完整 hash: `0305c5a3b958a0a20d9cc02832df99834f142ff4`
- 时间/作者: 2026-07-28 / chaoyujiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9a4f82911e` - fix lint

- 完整 hash: `9a4f82911e68906182eedab2530368b511d91553`
- 时间/作者: 2026-07-28 / chaoyujiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `997e64560f` - ci: use configured HCU release image

- 完整 hash: `997e64560f65d6dffa96b191ca3eb3961903620a`
- 时间/作者: 2026-07-28 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `77939d9a53` - ci: use configured HCU release image

- 完整 hash: `77939d9a53074f6890a90f8376ce9dcc3ba5b3dc`
- 时间/作者: 2026-07-28 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `8f848be4e7` - ci: use configured HCU release image

- 完整 hash: `8f848be4e78c66bdd58aef38eaa433267c6725db`
- 时间/作者: 2026-07-28 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `0710e82a02` - Update quality gate workflow for new branch version

- 完整 hash: `0710e82a02c66a8add5fee45fab8355a92457d26`
- 时间/作者: 2026-07-27 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `93c56ce71a` - Refactor quality gate workflow and job configurations

- 完整 hash: `93c56ce71a2f7fc883316c0bb115c0c435b439b4`
- 时间/作者: 2026-07-27 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `163a92c142` - fix(hcu):修改lightop的算子接口.

- 完整 hash: `163a92c142ec5a1a6dae787228e0311bb864a61e`
- 时间/作者: 2026-07-27 / luoyao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/activation.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/activation.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `87e3831800` - fix: 移除旧的lmslim导入方式.

- 完整 hash: `87e3831800b3a93a3021c6830cc0241a8ca82327`
- 时间/作者: 2026-07-27 / luoyao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `afac89e0e4` - feat(hcu): add KME W8A8 hipBLASLt path via METHODS=3

- 完整 hash: `afac89e0e4e9582992824f48ba9c87f034a9c7dc`
- 时间/作者: 2026-07-27 / yht183
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a3efe5e533` - [bugfix]:修复lightop_per_token_quant_fp8调用前tensor准备.

- 完整 hash: `a3efe5e5335622c1526c09049e1b23d93a705f53`
- 时间/作者: 2026-07-24 / luoyao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/mem_cache/allocator.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`; `python/sglang/srt/mem_cache/allocator.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `88d4501a3b` - Update quality gate workflow reference

- 完整 hash: `88d4501a3b3af0c82a54dbb47573eab5481639ba`
- 时间/作者: 2026-07-24 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9e13c77cee` - fix(ci): use card v2 link button

- 完整 hash: `9e13c77cee439e6c6d1a7949f03330b9347ae380`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `4af8102057` - fix(ci): use card v2 metadata component

- 完整 hash: `4af8102057c065ef77492c9fae37bd789a4d291e`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `65b7c42689` - ci: use shared runner for Feishu preview

- 完整 hash: `65b7c426897363242a2851369ec4eb3348395f6f`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6ac12c2e50` - ci: decouple Feishu preview from HCU runners

- 完整 hash: `6ac12c2e503e26099d57d29dff7948c0fa51c6d4`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2c21b95e60` - fix(ci): align Feishu accuracy table

- 完整 hash: `2c21b95e604e6ae065f5455459e4cfb8096885ac`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9a8b1bd08e` - Update quality gate workflow reference to new commit

- 完整 hash: `9a8b1bd08e7638debad3d0f5ae14162677cf26ff`
- 时间/作者: 2026-07-24 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `eb6a340936` - Update workflow reference to latest commit

- 完整 hash: `eb6a34093612ed2f6b2fe17bd9567c529ba6b6f7`
- 时间/作者: 2026-07-24 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f76d2cea38` - Delete .github/workflows/quality-baseline-scan.yml

- 完整 hash: `f76d2cea388b5bbdf2ae5b4c49b00ea7955d6c59`
- 时间/作者: 2026-07-24 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c3755b4d46` - fix: make DP local control broadcast opt-in via env

- 完整 hash: `c3755b4d4605a042a0fa1b090649ede27606c481`
- 时间/作者: 2026-07-23 / yht183
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/managers/data_parallel_controller.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e338cca156` - ci(hcu): improve accuracy card and fix VLM model path

- 完整 hash: `e338cca1561d38d0f8e8d3b7805f6eef6b1c85d2`
- 时间/作者: 2026-07-23 / tianlinyang77
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `83d2a2b4b1` - fix(hcu): rename stale DCU HiCache identifiers

- 完整 hash: `83d2a2b4b1913b56a14af1d978c7bed1abbae2a3`
- 时间/作者: 2026-07-23 / lizhigong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/test/hcu_cookbook_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8b38b9a258` - Update comment for all_gather usage in scheduler

- 完整 hash: `8b38b9a258b2caae64dc9b7789b38aa74b56f524`
- 时间/作者: 2026-07-22 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `421a13a808` - ci(hcu): enable accuracy notification on default branch

- 完整 hash: `421a13a808ccb95dc8ea94ae55f170edf7324ffd`
- 时间/作者: 2026-07-22 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b1606885e0` - Fix help text for custom all-reduce backend

- 完整 hash: `b1606885e0a16b1c97322239aaf62ce3f1ddcdbb`
- 时间/作者: 2026-07-22 / Lvjiajia
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0b46ed36da` - fix: apply bias after HCU DeepGEMM FP8 linear

- 完整 hash: `0b46ed36dacfea86ef6a01dcc099af31af264de1`
- 时间/作者: 2026-07-22 / maxiaobetter
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f391712f7f` - fix(hcu): use HCU guard for MLA KV cache storage

- 完整 hash: `f391712f7fe803797b678c6c9cb8e3d001279bdd`
- 时间/作者: 2026-07-22 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7941e04191` - fix: enable HiCache layout_dcu for hybrid Mamba and EAGLE draft

- 完整 hash: `7941e04191ba6671f0aa4cddd7eab63241d80155`
- 时间/作者: 2026-07-22 / yaoht
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1c40e365c8` - support mla lightop

- 完整 hash: `1c40e365c892188032a4571dc0a902101f2b2c31`
- 时间/作者: 2026-07-22 / sunjf
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9fc04a7a2c` - [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault

- 完整 hash: `9fc04a7a2cebc525a96301d3e8e9515bb0a5b4b6`
- 时间/作者: 2026-07-22 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/mega_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7b6a9dd891` - 修复DeepseekV4精度问题

- 完整 hash: `7b6a9dd891870840e3c5793737b995c4d3bf0062`
- 时间/作者: 2026-07-21 / lijing
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ac56ca009f` - ci: follow main sensitive diff workflow

- 完整 hash: `ac56ca009f9acfd41248ff7c016bebaaea80b21d`
- 时间/作者: 2026-07-21 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9864c84513` - ci: use shared sensitive diff gate for HCU port

- 完整 hash: `9864c84513db1a9d774733f021d5c46931d71eaa`
- 时间/作者: 2026-07-21 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/hcu/check_sensitive_diff_text.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c1f3f08c8a` - Update workflow reference to a new commit

- 完整 hash: `c1f3f08c8a1f4aa48ddabe7a88997aac4e80b45d`
- 时间/作者: 2026-07-21 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e7ab054110` - Delete .github/workflows/pr-quality-gate.yml

- 完整 hash: `e7ab054110fbca1987b072597f32581ba795afcd`
- 时间/作者: 2026-07-21 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/pr-quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `14da9b10e4` - Update workflow reference in quality-gate.yml

- 完整 hash: `14da9b10e4e0e15ab993173d938019fc2ffde489`
- 时间/作者: 2026-07-21 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `15a656ea69` - test(hcu): align v0.5.15 compatibility tests

- 完整 hash: `15a656ea69e89095c927e214ff56703bb203d7b3`
- 时间/作者: 2026-07-20 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`; `test/registered/hcu/unit/test_profile_merger_hcu.py`; `test/registered/unit/server_args/test_server_args.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e19d341ab8` - Refactor quality gate workflow and update triggers

- 完整 hash: `e19d341ab8af7d50646008ff6711f9022a8b066d`
- 时间/作者: 2026-07-20 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `5543eb3df2` - Rename quality-gate workflow and update triggers

- 完整 hash: `5543eb3df2cb3156bfdc63a9cd5fbf0a7cdcd88b`
- 时间/作者: 2026-07-20 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `5ac1f2418a` - Add GitHub Actions workflow for quality gate

- 完整 hash: `5ac1f2418a595f502ace96a3cc3e9c19cb22f40f`
- 时间/作者: 2026-07-20 / Lvjiajia
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `811aa027d6` - ci: replace HCU runtime text check with sensitive diff gate

- 完整 hash: `811aa027d6a05c94166ab8bc0879efce3e1ff977`
- 时间/作者: 2026-07-20 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/hcu/check_hcu_runtime_text.py`; `scripts/ci/hcu/check_sensitive_diff_text.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e47445d2fa` - chore: clean leftover patch labels in PD Decode DP sync

- 完整 hash: `e47445d2fa28d2ddde2e261a73c15a83b8b702b0`
- 时间/作者: 2026-07-20 / yaoht
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `81e3561aeb` - ci(hcu): exclude two unstable PR tests

- 完整 hash: `81e3561aeb01ad52674d07a9304e521de5c1ef82`
- 时间/作者: 2026-07-20 / LvJIA-RG
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `358a337143` - fix(hcu): keep Harbor build image path

- 完整 hash: `358a337143a37bc177dd40bcbb60169ad33a53bd`
- 时间/作者: 2026-07-20 / tianlinyang77
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `079275b811` - ci: add local sensitive diff text gate

- 完整 hash: `079275b811254795400b9cd08e62f3b9e729ac09`
- 时间/作者: 2026-07-20 / reverie-hub
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/hcu/check_sensitive_diff_text.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fe9f24924f` - fix: prevent PD Decode DP hang under enable-dp-attention

- 完整 hash: `fe9f24924f2ba30247e9354fc60cb8dc8183f35c`
- 时间/作者: 2026-07-20 / yaoht
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `37074c9af6` - Fix dsv4 full token pool

- 完整 hash: `37074c9af6a735966d576d42dd98bfcc65bb5dd1`
- 时间/作者: 2026-07-16 / lijing
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `09d7a1d4ca` - support fabric aiter custom allreduce

- 完整 hash: `09d7a1d4ca14b017a68754ae270f481250bee368`
- 时间/作者: 2026-07-16 / sunjf
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/dcu_cookbook_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`
  - tests: `python/sglang/test/dcu_cookbook_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d280691576` - [bugfix]适配新的causal_conv1d接口

- 完整 hash: `d280691576a7639ec768c7f48b57d06d82187676`
- 时间/作者: 2026-07-16 / chenyuege
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e5a2dd0419` - [bugfix]适配新的causal_conv1d接口

- 完整 hash: `e5a2dd0419b07348ece0911d036c7dbbae0e2926`
- 时间/作者: 2026-07-16 / chenyuege
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `339dfe4336` - docs(dcu): define v0.5.15.post1 release workflow

- 完整 hash: `339dfe4336eea2ab37e6194a8c045f90223494f0`
- 时间/作者: 2026-07-16 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`; `docs/internal/dcu-main-migration-plan.md`; `docs/internal/dcu-v0.5.15-post1-dev-plan.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `dc1323ba4c` - docs(dcu): finalize v0.5.12_dev forward-port

- 完整 hash: `dc1323ba4cae06c266d3da57bf3012b32a2af1f9`
- 时间/作者: 2026-07-16 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`; `docs/internal/dcu-main-migration-plan.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `49a10aec8c` - docs(dcu): record 20260714 owner validation

- 完整 hash: `49a10aec8c2e5b84aca930f78795adf6651651be`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `f67cdf69bd` - docs(dcu): record 20260714 runtime blocker

- 完整 hash: `f67cdf69bd89c1feea0cb6cbe3abb20892097420`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `20633db576` - docs(dcu): add 20260714 conflict review

- 完整 hash: `20633db5760b026ad7393b5ac9ea3f05c90b86e5`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260714-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260714-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `324181561d` - docs(dcu): add 20260713 conflict review

- 完整 hash: `324181561d48cdc0ce51ab0e864ec19832b7267a`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260713-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0b30b7c9d2` - docs(dcu): record 20260712 runtime validation

- 完整 hash: `0b30b7c9d231c24660d7b6135a0d5eb6f59da8c0`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `44f81e8f7a` - docs(dcu): record 20260712 runtime gate status

- 完整 hash: `44f81e8f7af876a48bfc0eac5e15553a1b317858`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `baa08af595` - docs(dcu): add 20260712 conflict review

- 完整 hash: `baa08af5950aa514d26503ffda00db57121ee462`
- 时间/作者: 2026-07-15 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260712-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `1109d462d5` - [Feature] Support PD different-TP transfer for hybrid SWA/NSA and unequal K/V item lens.

- 完整 hash: `1109d462d57e084b3a3c5f7f03aacd709ff0ef0d`
- 时间/作者: 2026-07-15 / huojianqiang
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3e335fce8e` - docs: correct 20260710 endpoint subject

- 完整 hash: `3e335fce8e11eaa2d712d62889283a520dbc4898`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3d77308ea3` - docs: mark 20260710 catch-up validated

- 完整 hash: `3d77308ea3261e8c941bec187c9cd96ce6ac8c77`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `6630db3cfa` - docs: record 20260710 pure-TP validation

- 完整 hash: `6630db3cfa3f5db180d62b69c19be1b9c7e72966`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `24894692ea` - fix: use runtime attention TP size in model warmup

- 完整 hash: `24894692eab30e9c7b8f1062fc727728ae54a99b`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9d7fbb0174` - docs: add 20260710 conflict review

- 完整 hash: `9d7fbb0174ad0974fe37b1cf028dd25e60ab580c`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260710-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `48c3c0997e` - ci: run HCU text check in Python 3.10 container

- 完整 hash: `48c3c0997ef17daa34a6e482afdeb0620c1abcbc`
- 时间/作者: 2026-07-14 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f1c5eda31e` - ci: require HCU runtime text check

- 完整 hash: `f1c5eda31e795131f0e77d0c4b873b91793d32b4`
- 时间/作者: 2026-07-14 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c0e8edd741` - fix(dcu): initialize DeepEP dispatch dtype state

- 完整 hash: `c0e8edd7418a1da9803ff1e5ac7d0f8753ec8c1a`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `412d0ef9fa` - docs(dcu): add 20260709 conflict review

- 完整 hash: `412d0ef9fa0e99337936b32164e7d6cdb4bd5af4`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260709-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e3aa204a05` - docs(dcu): require catch-up conflict reviews

- 完整 hash: `e3aa204a05933dc6233a7be83395869012c1b179`
- 时间/作者: 2026-07-14 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260706-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/dcu-main-migration-plan.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b9ca7c2adb` - Refine copyright/license warning messages

- 完整 hash: `b9ca7c2adb3a8fd30f57ae9cdd7e05c4a72a2d2a`
- 时间/作者: 2026-07-14 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `d53953dbe7` - ci: clean up HCU validation checks

- 完整 hash: `d53953dbe7bdc6f4bf32c7acd7a92ab61eabafb5`
- 时间/作者: 2026-07-14 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/tests/test_check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - tests: `scripts/ci/hcu/tests/test_check_hcu_runtime_text.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `2981595c7f` - [FIX] 修复走非dcu_fa下的报错

- 完整 hash: `2981595c7f67279e2b7b1795d2c3f90c23d8cd5b`
- 时间/作者: 2026-07-14 / yangyn
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `516a35c40e` - docs(dcu): record 20260703 runtime blocker

- 完整 hash: `516a35c40e89c109686ac8f6f9c08fc80c3d3178`
- 时间/作者: 2026-07-13 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c078943aa3` - chore: fix fused_moe lint issues

- 完整 hash: `c078943aa3573b3e20b03bf92709b8557ea03131`
- 时间/作者: 2026-07-13 / whlwhlwhl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d8ed552da8` - docs(dcu): add 20260629 conflict review

- 完整 hash: `d8ed552da8e5c56d3a87f6bcf01a2d7add8bc568`
- 时间/作者: 2026-07-13 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-catchup-20260629-conflict-review.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-catchup-20260629-conflict-review.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `bf59e99fde` - ci: harden HCU runtime text quality gate

- 完整 hash: `bf59e99fde6f9d5b0d0f13f5bfcccc3233b3f439`
- 时间/作者: 2026-07-13 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/hcu/check_hcu_runtime_text.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `24bcdba3b7` - feat: support AITER W4A16 MOE_C prefill

- 完整 hash: `24bcdba3b722eb0543e6cae6c6f7215ff65db9f0`
- 时间/作者: 2026-07-13 / whlwhlwhl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `427726d609` - fix: complete HCU runtime text cleanup

- 完整 hash: `427726d60935cdc55d2b3c325b6d7f6eb280140e`
- 时间/作者: 2026-07-13 / reverie-hub
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/hcu_cookbook_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8c797abd6f` - Record 20260629 DCU runtime validation

- 完整 hash: `8c797abd6fc6e29ebc7cfbcc93ceffcc4bc9414e`
- 时间/作者: 2026-07-13 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `bd60c02238` - Enhance quality gate workflow with new checks and branches

- 完整 hash: `bd60c022380f37034d2f68a30ef840fa9221a4c1`
- 时间/作者: 2026-07-13 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `40c658e8ab` - ci: harden HCU runtime text checker

- 完整 hash: `40c658e8ab151271e6c01fe7f359acbfe862080d`
- 时间/作者: 2026-07-13 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/dcu/check_hcu_runtime_text.py`
  - tests: `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `48489724d5` - docs(dcu): record 20260623 catch-up runtime status

- 完整 hash: `48489724d57f2ff6648e0a8859643458ad8a3ac7`
- 时间/作者: 2026-07-13 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `cba9e72cc0` - [BugFix] skip some uncompatibal env setup in hip for DCU

- 完整 hash: `cba9e72cc037e2966983f61b95006c588fb3c76f`
- 时间/作者: 2026-07-13 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `1123fc0382` - ci: enforce HCU rename safety checks

- 完整 hash: `1123fc038237a1d7e3a0cbbd09b189fa9f260da8`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/hcu/hcu_rename_allowlist.txt`, `scripts/ci/hcu/test_verify_hcu_rename.py`, `scripts/ci/hcu/verify_hcu_registration.py`, `scripts/ci/hcu/verify_hcu_rename.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`; `scripts/ci/hcu/test_verify_hcu_rename.py`; `scripts/ci/hcu/verify_hcu_registration.py`; `scripts/ci/hcu/verify_hcu_rename.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9353ecb963` - docs: complete HCU naming migration

- 完整 hash: `9353ecb96312ed52fd5752af133437ea0abd001b`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `NOTICE`, `README.md`, `README_DCU.md`, `README_HCU.md`, `THIRD_PARTY_NOTICES.md`, `docs/dcu-pr-ci-visual-guide.html`, `docs/hcu-pr-ci-visual-guide.html`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`
  - other: `NOTICE`; `README.md`; `README_DCU.md`; `README_HCU.md`; `THIRD_PARTY_NOTICES.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `de7170db00` - kernel: migrate DCU ops and wrappers to HCU

- 完整 hash: `de7170db00755e66293b01020eaa805d246a971d`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/flash_mla.py`, `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/csrc/kvcacheio/transfer.cu`; `sgl-kernel/include/sgl_kernel_ops.h`; `sgl-kernel/python/sgl_kernel/flash_mla.py`; `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e3fee4310d` - ci: sync HCU workflows and scripts with current main

- 完整 hash: `e3fee4310dc196c44e29e6cc919377f9829b744f`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 33 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 18 个文件
  - other: `requirements_dcu.txt`; `requirements_hcu.txt`; `scripts/ci/dcu/check_hcu_runtime_text.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py` 等 15 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `0395a2bd25` - fix: use lightop int8 deepep moe on dcu

- 完整 hash: `0395a2bd25a195561dc5e8758f735cbcfb3d365d`
- 时间/作者: 2026-07-11 / yangql
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `390ad18e71` - ci: 修复 packed KV 测试注册导致的 DCU CI 收集失败 (#87)

- 完整 hash: `390ad18e713394cd02b55b354b3259a58cc34cfd`
- 时间/作者: 2026-07-11 / tianly
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`, `benchmark/kernels/pack_paged_kv_to_varlen/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/bench_pack_paged_kv_to_varlen.py`, `test/registered/attention/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/test_pack_paged_kv_to_varlen.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`; `benchmark/kernels/pack_paged_kv_to_varlen/pack_paged_kv_to_varlen_benchmark_results.md`
  - tests: `test/registered/attention/bench_pack_paged_kv_to_varlen.py`; `test/registered/attention/pack_paged_kv_to_varlen_benchmark_results.md`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b38f25513e` - ci: add manual HCU nightly workflow controls

- 完整 hash: `b38f25513eaf9fb0aab6e8422c681f6752bba147`
- 时间/作者: 2026-07-09 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/nightly-test-intel.yml`, `.github/workflows/nightly-test-npu.yml` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/ci-coverage-overview.yml`; `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/nightly-test-intel.yml`; `.github/workflows/nightly-test-npu.yml` 等 17 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `dccf1782b2` - ci: disable HCU runtime text check job

- 完整 hash: `dccf1782b25f91c48ceef33e8287f74aa22af707`
- 时间/作者: 2026-07-09 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `d445921fe7` - 新增对RadixAttention层的判断

- 完整 hash: `d445921fe7cf5095eb1248c4e091ebb5bd197bdb`
- 时间/作者: 2026-07-09 / WuFan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `616ba7b6d6` - ci: reduce HCU runtime text check duplicate output

- 完整 hash: `616ba7b6d6e4ed0ea08aafeb178f92d230253f4f`
- 时间/作者: 2026-07-09 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d7af9508db` - style: apply CI hook formatting

- 完整 hash: `d7af9508db9fce319582c6f691bb0c2ac8765a97`
- 时间/作者: 2026-07-09 / lizhigong
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/managers/cache_controller.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fda6d44a45` - ci: simplify HCU runtime text check failure message

- 完整 hash: `fda6d44a45781ec85484864af4c171b5a6723d2d`
- 时间/作者: 2026-07-09 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `8b4a7bdeb5` - ci: refine HCU runtime text check message

- 完整 hash: `8b4a7bdeb5ec8acd075d0f22582f813834526330`
- 时间/作者: 2026-07-09 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/check_hcu_runtime_text.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `4b0fcbd07e` - [Addition] deliver one validation doc of C17~C19

- 完整 hash: `4b0fcbd07e34d25862da32bf7f12362871093205`
- 时间/作者: 2026-07-09 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3e254b0413` - style(distributed): apply pre-commit formatting to parallel_state.py

- 完整 hash: `3e254b0413372d24abfd468f91c501567f753325`
- 时间/作者: 2026-07-09 / shiqiang
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cee45bc550` - docs(dcu): record C17-C19 validation

- 完整 hash: `cee45bc55003cc3fde2ea05c7d3405e4ea94282e`
- 时间/作者: 2026-07-09 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `01a6f1b945` - [Addition] deliver one validation doc of C14~C16

- 完整 hash: `01a6f1b945628daff0d067d75ddf103757996967`
- 时间/作者: 2026-07-09 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b452d6bd67` - docs(dcu): record C14-C16 functional validation

- 完整 hash: `b452d6bd674d5b8b293814ebb3a640758c4ce8cf`
- 时间/作者: 2026-07-08 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `1cea713a71` - docs(dcu): record C14-C16 validation block

- 完整 hash: `1cea713a71d1da6959ffcfc37ae271c3490ba74f`
- 时间/作者: 2026-07-08 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b6db54a9a1` - [Addition] deliver one validation doc of C11~C13

- 完整 hash: `b6db54a9a12fcbbfeb44330ab35c765b3e50f97c`
- 时间/作者: 2026-07-08 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `5d2c6854a9` - 0.5.12 MHA、GQA类hicache适配

- 完整 hash: `5d2c6854a95a5a22da3d696a871e7dbceb99bca7`
- 时间/作者: 2026-07-08 / shangxl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/server_args.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/csrc/kvcacheio/transfer.cu`; `sgl-kernel/include/sgl_kernel_ops.h` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bfaf180d14` - [Addition] deliver one validation doc of C10

- 完整 hash: `bfaf180d14cee58f87789a2a7345a52919933d12`
- 时间/作者: 2026-07-08 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `fe4e1fea3d` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `fe4e1fea3d9a7e309342f284368d1b5c19cc39a6`
- 时间/作者: 2026-07-07 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ef36df96f6` - chore: add header for DCU runtime text checker

- 完整 hash: `ef36df96f68e0137dd791e21575d64d2b18c401d`
- 时间/作者: 2026-07-07 / Lv Jiajia
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/dcu/check_no_amd_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/check_no_amd_runtime_text.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9188d711e5` - ci: rename HCU runtime text check script

- 完整 hash: `9188d711e5347c5b78b78d750bfc4019c87293b1`
- 时间/作者: 2026-07-07 / reverie-hub
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/check_no_amd_runtime_text.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
  - other: `scripts/ci/dcu/check_hcu_runtime_text.py`; `scripts/ci/dcu/check_no_amd_runtime_text.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `d5f4d1c14f` - fix: skip expert distribution recording during CUDA graph capture

- 完整 hash: `d5f4d1c14f7136dbddad203100dd039fafc87324`
- 时间/作者: 2026-07-07 / liuchy5
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/eplb/expert_distribution.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/eplb/expert_distribution.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9bde26e7c7` - 解耦vllm rms_norm

- 完整 hash: `9bde26e7c7a6fe0af4e1cb2ae41334e508e7492d`
- 时间/作者: 2026-07-07 / liucong
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3f920d4e06` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `3f920d4e06dad35236037abaff404b679de85440`
- 时间/作者: 2026-07-07 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0507e60908` - fix: avoid amdsmi runtime logs on HCU

- 完整 hash: `0507e60908a4781d2481583725297ec159927c83`
- 时间/作者: 2026-07-07 / reverie-hub
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4d198708c3` - 解决sp下对padding的处理

- 完整 hash: `4d198708c3cc32876aa990f5f36f2cb50bfba95a`
- 时间/作者: 2026-07-07 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cf59f46950` - [bugfix]: avoid HYV3 PD KV compact remap

- 完整 hash: `cf59f46950cffea5d97d1b9e43dfdeaf18611824`
- 时间/作者: 2026-07-06 / luoyao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ec48fa7802` - [bugfix]: 解决hy3开mtp下的精度问题.

- 完整 hash: `ec48fa780219f3fbe8c32777d7171eec988ea4e4`
- 时间/作者: 2026-07-06 / luoyao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `23cbd00e31` - [bugfix]: 解决hy3非mtp下的精度问题

- 完整 hash: `23cbd00e3154ff8e58e2c780d08e1110889bf02c`
- 时间/作者: 2026-07-06 / luoyao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/prefill.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/prefill.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `a1ed918ae7` - [Addition] deliver one validation doc of C09

- 完整 hash: `a1ed918ae77c8156fbe6aeaebad465995e0b5384`
- 时间/作者: 2026-07-06 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `fa6b75971f` - [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed

- 完整 hash: `fa6b75971f6c219b8644cb335777da0876186427`
- 时间/作者: 2026-07-06 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/triton_ops/metadata.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `88bb5176c8` - [Addition] deliver one validation doc of C08

- 完整 hash: `88bb5176c801f871d1c16d3c9d7568074ca7bad1`
- 时间/作者: 2026-07-06 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `36f3237527` - fix: refine HCU runtime log wording

- 完整 hash: `36f3237527fc0e07f196959ab9f76e1b460d2efb`
- 时间/作者: 2026-07-05 / reverie-hub
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py`, `sgl-kernel/csrc/mamba/causal_conv1d.cu`, `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/layers/quantization/mxfp4.py`; `python/sglang/srt/model_executor/cuda_graph_runner.py`; `sgl-kernel/csrc/mamba/causal_conv1d.cu`
  - tests: `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`; `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cd2e73a67c` - 优化lint扫描规则

- 完整 hash: `cd2e73a67c9607079672f90c4011ac8b264cb9c4`
- 时间/作者: 2026-07-04 / Lvjiajia
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `8efd2ad46e` - update w4a16 deepgemm interface

- 完整 hash: `8efd2ad46e4e635b228e788c5251fa24a8a97cf8`
- 时间/作者: 2026-07-03 / sunjf
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `00063277c1` - [Addition] deliver one validation doc of C07

- 完整 hash: `00063277c1c73582d32b7348463d3e9200baa012`
- 时间/作者: 2026-07-03 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c3dc2e8eb2` - feat: validate DCU attention backend compatibility

- 完整 hash: `c3dc2e8eb2b23234f49b3b69e362273da7025672`
- 时间/作者: 2026-07-03 / maxiao1
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ce2521017f` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `ce2521017fde170cc71e603f27d38048839114ba`
- 时间/作者: 2026-07-03 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `84bd983bad` - ci: use local DCU reranker model

- 完整 hash: `84bd983badb43fc5897565e49d0654c6382d55a8`
- 时间/作者: 2026-07-02 / dingxl
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `dd26854396` - support w4a16 moe ep

- 完整 hash: `dd268543965093016f4a4a1f75bf580ab8d21a66`
- 时间/作者: 2026-07-02 / sunjf
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fc2af93314` - Add open-source compliance baseline workflow

- 完整 hash: `fc2af93314f2cadc8b017f13d0f078444004570a`
- 时间/作者: 2026-07-02 / Lvjiajia
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/open-source-compliance-baseline.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/open-source-compliance-baseline.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `758a0a9890` - Add open-source compliance configuration file

- 完整 hash: `758a0a989008dbebafa366c47c94d6d627118001`
- 时间/作者: 2026-07-02 / Lvjiajia
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/open-source-compliance.json`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/open-source-compliance.json`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6332704295` - ci: extend DCU stage-b per-file timeout

- 完整 hash: `6332704295c7ed712a9bc0e32fb745976320d2dd`
- 时间/作者: 2026-07-02 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ef3571f7b0` - 解决CI报错问题

- 完整 hash: `ef3571f7b02a65daa0e312c8bf7e28ce426ab451`
- 时间/作者: 2026-07-01 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/utils/cuda_ipc_transport_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/utils/cuda_ipc_transport_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e6d4b3378c` - [Addition] deliver one validation doc

- 完整 hash: `e6d4b3378c17c04174757e4610480a6eea892bec`
- 时间/作者: 2026-07-01 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `998ffb809b` - fix(fst): reclaim reserved memory after fastsafetensors weight load

- 完整 hash: `998ffb809bcd2bd04314710976f81ec3c78732dd`
- 时间/作者: 2026-07-01 / lzb16
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/model_loader/loader.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/model_loader/loader.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `696cae936d` - fix(fst): use local device in fastsafetensors iterator for multi-node loading

- 完整 hash: `696cae936d1d1b48af8ef798385abe2490f0f9cf`
- 时间/作者: 2026-07-01 / lzb16
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/model_loader/weight_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/model_loader/weight_utils.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `2b1fbe1e6c` - [CI] fix pre-commit lint errors surfaced after merging v0.5.12_dev

- 完整 hash: `2b1fbe1e6c3729a158bddedcc979c93060e5fc2d`
- 时间/作者: 2026-07-01 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `35456bae31` - [CI] fix pre-commit lint errors on megamoe w8a8 changed files

- 完整 hash: `35456bae3139361eebd66bd4ae2f66715be8c3ff`
- 时间/作者: 2026-07-01 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `.codespellrc`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `.codespellrc`; `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `af015c4ce4` - Update Trivy cache volume permissions

- 完整 hash: `af015c4ce4c61eb2380fd61186e82e320317fe3a`
- 时间/作者: 2026-07-01 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `72f0237175` - Remove credential keyword pattern from scan config

- 完整 hash: `72f0237175ac03de56a9321f474eaf18a33b8426`
- 时间/作者: 2026-07-01 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `20f106c6b4` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `20f106c6b4a5cd5a3099802f0c59efc97b80d6d8`
- 时间/作者: 2026-07-01 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `41db24a843` - Enhance quality baseline scan with new checks

- 完整 hash: `41db24a8438fd8d9c2bc9badc67c114015530adb`
- 时间/作者: 2026-07-01 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `445eaafe5d` - [Perf] optimize aiter asm moe via shuffle weight

- 完整 hash: `445eaafe5d4802491ad124c29afd02c3e8193102`
- 时间/作者: 2026-06-30 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ff440b8971` - docs(dcu): record C04 runtime validation

- 完整 hash: `ff440b8971fa8642e2221455e33796ec5a6a277e`
- 时间/作者: 2026-06-30 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `3910b3f9db` - fix(scheduler): restore DCU empty-prefix location

- 完整 hash: `3910b3f9dbf43298328d0b83d5d63006675a3f0c`
- 时间/作者: 2026-06-30 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `f2d0e86d71` - fix(dsv4): repair DCU sgl-kernel and JIT build

- 完整 hash: `f2d0e86d71b3242666d72f22fce42bea42b1667f`
- 时间/作者: 2026-06-30 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `sgl-kernel/setup_hip.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bd10f999c3` - Fix formatting and improve quality gate script

- 完整 hash: `bd10f999c3ef41fe7dbbbfa0b68ae014503da172`
- 时间/作者: 2026-06-30 / Lvjiajia
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `412236292d` - Modify ruff command to use --no-cache

- 完整 hash: `412236292d4da4ab0288d24491b2230d512294c8`
- 时间/作者: 2026-06-30 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ea182d81e3` - Update quality gate workflow with environment variables

- 完整 hash: `ea182d81e3c554451fbb9ecbcfb5dc633dd6d0bf`
- 时间/作者: 2026-06-30 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c4d3532db8` - fix:dcu bypass triton normal_decode_set_metadata use normal_decode_set_metadata_lightop

- 完整 hash: `c4d3532db8815368557797e091c53da7c9888359`
- 时间/作者: 2026-06-09 / liuchy5
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5245654dc1` - Fix: DCU bypass Triton get_last_loc and use native dcu_get_last_loc

- 完整 hash: `5245654dc139406bd1105190a18cdc93ed001563`
- 时间/作者: 2026-06-03 / liuchy5
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4e3fd3a350` - HY3修改

- 完整 hash: `4e3fd3a35032366580b1246b4e458fcc120adf70`
- 时间/作者: 2026-06-03 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bda910adb6` - feat(dcu): integrate LightOp alloc-extend kernel

- 完整 hash: `bda910adb6cfb6b985cdc214c842afd859953cd7`
- 时间/作者: 2026-06-30 / whlwhlwhl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/mem_cache/allocator.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/allocator.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f8b2eefcff` - feat(dsv4): generalize top-k index transformation

- 完整 hash: `f8b2eefcff4f4cd163c16768ec2dca1f6aafce35`
- 时间/作者: 2026-06-30 / whlwhlwhl
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f2e257f7ab` - feat(dcu): route sqrtsoftplus gating through LightOp

- 完整 hash: `f2e257f7abfa5bd37e261029f955eb7120c7c6f9`
- 时间/作者: 2026-06-30 / whlwhlwhl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b76f31cce4` - Refactor quality-gate.yml with enhanced checks

- 完整 hash: `b76f31cce40284ca8c448d387299cf2c6fc99cbc`
- 时间/作者: 2026-06-30 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `93cf8edc41` - [Addition] deliver one validation doc

- 完整 hash: `93cf8edc419d8235856302c0cff1dcca890cac13`
- 时间/作者: 2026-06-30 / RyeYuan
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d22548eb14` - feat(sgl-kernel): port l2norm kernel with tiled optimization for DCU

- 完整 hash: `d22548eb140c3540dee73f7bd00e75e857e6d9b6`
- 时间/作者: 2026-06-30 / yaoht
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/l2norm.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/common_extension.cc`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/elementwise/l2norm_kernel.cu`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/__init__.py`, `sgl-kernel/python/sgl_kernel/elementwise.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/l2norm.py`; `sgl-kernel/CMakeLists.txt`; `sgl-kernel/csrc/common_extension.cc`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/csrc/elementwise/l2norm_kernel.cu`; `sgl-kernel/include/sgl_kernel_ops.h`; `sgl-kernel/python/sgl_kernel/__init__.py`; `sgl-kernel/python/sgl_kernel/elementwise.py` 等 10 个文件
  - tests: `sgl-kernel/tests/test_norm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c4cc0a73b6` - fix(dsv4): preserve DCU elementwise and topk paths

- 完整 hash: `c4cc0a73b69ec48614c91ca8e586a29152fc171a`
- 时间/作者: 2026-06-30 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fa2430f455` - Organize DCU nightly workflow modules

- 完整 hash: `fa2430f4554d65701a41200cba81ab29368b1604`
- 时间/作者: 2026-06-29 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `01216a18f2` - Disable DCU remote weight loading nightly test

- 完整 hash: `01216a18f2bf50b9f42d78f5661b3c0c79044e25`
- 时间/作者: 2026-06-29 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/distributed/test_load_weights_from_remote_instance.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/distributed/test_load_weights_from_remote_instance.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `06889adc04` - Disable DCU update weights from disk nightly test

- 完整 hash: `06889adc0413bb9e15f0fcd28f83b650a9b6c7e1`
- 时间/作者: 2026-06-29 / DCU CI Bot
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/rl/test_update_weights_from_disk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/rl/test_update_weights_from_disk.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0553e12d0a` - 修复合并分支产生的bug

- 完整 hash: `0553e12d0a592459eb81db9f4f2f6b5425aa0248`
- 时间/作者: 2026-06-29 / yangyn
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `83294cba6e` - Add DCU nightly wheel release workflow with vendored-openssl support

- 完整 hash: `83294cba6ebe071951ef82c4abb02d7ebc01b18b`
- 时间/作者: 2026-06-29 / zhangyh15
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `395171de08` - test: fix DCU MMMU local dataset selection

- 完整 hash: `395171de0880feabf43d13534e12dec97effe9c3`
- 时间/作者: 2026-06-29 / LvJIA-RG
- 自动分类: 缺陷修复
- 主要文件: `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f40a12fb51` - 修改IPC逻辑，每个rank下都开辟内存池，解决rank0偶发变慢的问题

- 完整 hash: `f40a12fb51df3af315e771bb1fa325a55a32c5f6`
- 时间/作者: 2026-06-28 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`
  - runtime-perf: `python/sglang/srt/utils/cuda_ipc_transport_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a2076d9aa7` - test: use local DCU eval datasets

- 完整 hash: `a2076d9aa7d8a2d3bbee58abe3a5384019f19431`
- 时间/作者: 2026-06-26 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_mmlu.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `00febcba4a` - ci: reuse PR-staged DCU nightly wheels

- 完整 hash: `00febcba4a6ca14ac932e04bf69c731361678ef4`
- 时间/作者: 2026-06-26 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `21dfaaa4c2` - Update dcu-manual-model-test.yml

- 完整 hash: `21dfaaa4c2cd4502f61947eb7e7034d8405eae3b`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `8aa4b6eb52` - Update dcu-manual-model-test.yml

- 完整 hash: `8aa4b6eb52d57e32cfbc87654e1a9eb0d9bb2439`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `7d807cb225` - Update dcu-manual-model-test.yml

- 完整 hash: `7d807cb225ce6aa1c2ef03e9c2f8b781472bb1fc`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `0c4fe5ebe9` - ci: align DCU full wheel wait with PR staging

- 完整 hash: `0c4fe5ebe956e24bf4efc519d69d771aef56d1a2`
- 时间/作者: 2026-06-26 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `20eb46a704` - Update dcu-manual-model-test.yml

- 完整 hash: `20eb46a70447944065b1b0fe2e307c1fcee8e87a`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `db4759e78c` - Update dcu-manual-model-test.yml

- 完整 hash: `db4759e78c9a88fd823218263e167446797216b1`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `2f2abec114` - ci: cover new DCU nightly suites in full enabled

- 完整 hash: `2f2abec1140d55d9dd0dbe8235dff01789093dc5`
- 时间/作者: 2026-06-26 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ca7c7c54fc` - Update dcu-manual-model-test.yml

- 完整 hash: `ca7c7c54fc42df8e3660ad135ce91b203d2a57d3`
- 时间/作者: 2026-06-26 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `c7a4903ad8` - Update dcu-manual-model-test.yml

- 完整 hash: `c7a4903ad808f942549ca8c6ab9d11cf6554ef40`
- 时间/作者: 2026-06-25 / Lyt
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9abb848dba` - [Feat] support megamoe in the path of SGLANG_DCU_MEGA_MOE_RUNTIME=megamoe, and temporarily deepgeem path is still remained as backup

- 完整 hash: `9abb848dba3e86f2ee9867dc5b3f5601d61b00a3`
- 时间/作者: 2026-06-25 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`; `python/sglang/srt/model_executor/cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3dd1376ff3` - docs: fix DCU README trailing whitespace

- 完整 hash: `3dd1376ff350e22b2b65e13bc4fc4a1f557c5db4`
- 时间/作者: 2026-06-25 / liyt6
- 自动分类: 缺陷修复
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d1ea0b3aa2` - ci: support configurable manual DCU model validation

- 完整 hash: `d1ea0b3aa24931f21ec8d9c13d08bf97b229c120`
- 时间/作者: 2026-06-25 / liyt6
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
  - other: `README_DCU.md`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `be7d10f53c` - ci: add manual DCU unattended model test workflow

- 完整 hash: `be7d10f53c6aa621b9835e1e4787e37e87573e5d`
- 时间/作者: 2026-06-23 / liyt6
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-manual-model-test.yml`
  - other: `README_DCU.md`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `cae6c44969` - [FEAT] implement the initial changes about w8a8 megamoe for DCU

- 完整 hash: `cae6c449697d4416ca24c08abfaa14984ad589c1`
- 时间/作者: 2026-06-18 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4a08e1934a` - test: add DCU nightly 1 and 2 GPU suites

- 完整 hash: `4a08e1934a12cf3ae6147b8db069517e68e641d5`
- 时间/作者: 2026-06-25 / tianlinyang77
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/core/test_mm_process_config.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py`, `test/registered/distributed/test_parallel_state.py`, `test/registered/perf/test_bench_one_batch_2gpu.py`, `test/registered/perf/test_bench_serving_2gpu.py`, `test/registered/rl/test_update_weights_from_disk.py`, `test/registered/rl/test_update_weights_from_distributed.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/core/test_mm_process_config.py`; `test/registered/distributed/test_data_parallelism.py`; `test/registered/distributed/test_load_weights_from_remote_instance.py`; `test/registered/distributed/test_parallel_state.py`; `test/registered/perf/test_bench_one_batch_2gpu.py`; `test/registered/perf/test_bench_serving_2gpu.py`; `test/registered/rl/test_update_weights_from_disk.py`; `test/registered/rl/test_update_weights_from_distributed.py` 等 19 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `85cd7901c6` - test: keep verified DCU smoke and accuracy cases only

- 完整 hash: `85cd7901c6998f48a8133ba5ab541df6765947a0`
- 时间/作者: 2026-06-25 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`, `test/registered/dcu/quant/test_torchao_smoke_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`; `test/registered/dcu/core/test_deterministic_fa3_dcu.py`; `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`; `test/registered/dcu/quant/test_torchao_smoke_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `523756bde5` - [docs(dcu)] log C01/C02 conflict ledger update

- 完整 hash: `523756bde5ea9d48e02c5b80378f4432416deda5`
- 时间/作者: 2026-06-24 / RyeYuan
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `88ba08ad2b` - fix expert_location_dispatch_info is not define

- 完整 hash: `88ba08ad2be1ff654a8a7b66e81328c84ae881f4`
- 时间/作者: 2026-06-24 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `595f87c93e` - Restore push trigger and CIUpload devpi upload

- 完整 hash: `595f87c93e27e80331efe7cec869fd4a0fabe3d1`
- 时间/作者: 2026-06-24 / zhangyh15
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f4716f8ec5` - Add DCU nightly wheel release workflow

- 完整 hash: `f4716f8ec58d9f8176d240206c859c13544ed8db`
- 时间/作者: 2026-06-24 / zhangyh15
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `00ce3e6d95` - ci: stage DCU PR wheels locally

- 完整 hash: `00ce3e6d9540042a5eda9614cb9a1878562eed96`
- 时间/作者: 2026-06-24 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`; `.github/workflows/release-pr-dcu.yml`
  - other: `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `599b7490f1` - bugfix: fix topk vmfault issue

- 完整 hash: `599b7490f1cbbee50a235a7eba71a553c32c39bb`
- 时间/作者: 2026-06-23 / Alone-wl
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9304b9e1da` - ci: build DCU gateway wheel by default

- 完整 hash: `9304b9e1dae08a36f9955068d91f44edc23af790`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `de24697cb8` - ci: disable PR trigger for DCU nightly workflow

- 完整 hash: `de24697cb863a43d1e67f34881f1f2612140b99d`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9ed791e147` - ci: run PR helper workflows on private runner

- 完整 hash: `9ed791e1479bfc5e2ad863377d7fecd323aa2cee`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/labeler.yml`, `.github/workflows/pr-states.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/labeler.yml`; `.github/workflows/pr-states.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ca95a26da7` - ci: add DCU nightly workflow with wheel build

- 完整 hash: `ca95a26da7647d8fbdd9bd8e4bfd4d2142a38058`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-dcu.yml`; `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `4b8a743d31` - ci: add wheel mode to DCU full enabled

- 完整 hash: `4b8a743d31671ca082c135564b670dffe23f2283`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fdd9f8ecf3` - [BUG FIX] fix SWA mem pool issue causing accept length decrease

- 完整 hash: `fdd9f8ecf39798d242670205ff0a3f5d4952958d`
- 时间/作者: 2026-06-22 / shiqiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/swa_memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/swa_memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0536e102c2` - [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs

- 完整 hash: `0536e102c270bd3658566dfa3a070d0a0af3f55c`
- 时间/作者: 2026-06-22 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/dcu-main-migration-plan.md`
  - other: `scripts/code_sync/dcu_main_migration.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `5d83cfe857` - [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs

- 完整 hash: `5d83cfe85774d2fd941e68dd6c3f98680e872704`
- 时间/作者: 2026-06-22 / RyeYuan
- 自动分类: 测试/文档/基准
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/dcu-main-migration-plan.md`
  - other: `scripts/code_sync/dcu_main_migration.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0fc338999b` - 修复dpsk r1 fp8启动时的报错问题

- 完整 hash: `0fc338999b429229900b78d29d0ac75f094d2b2a`
- 时间/作者: 2026-06-22 / lipenghui
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `87aa66f4fb` - [BugFix] workaround fix of aiter custom allreduce in cuda-graph, would revert it after driver fix it

- 完整 hash: `87aa66f4fbec076b1ef56ed3b948fe27c805903a`
- 时间/作者: 2026-06-18 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `37a67648ff` - Update Trivy scan configuration in workflow

- 完整 hash: `37a67648ff1d045ba5a35f911c2ae839515587d0`
- 时间/作者: 2026-06-18 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e80c0644ac` - Update Trivy and Semgrep commands in workflow

- 完整 hash: `e80c0644ac197210ce4b582d64f1cdcb747505de`
- 时间/作者: 2026-06-18 / Lvjiajia
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fa22ad5aeb` - Add options for encoding, dependencies, and SAST scans

- 完整 hash: `fa22ad5aebdfb803f5152f14dd756ceb0c726f0c`
- 时间/作者: 2026-06-18 / Lvjiajia
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `983e644d4c` - fix: avoid redundant calls to forward_aiter and fp8 groupgemm kernels

- 完整 hash: `983e644d4cc13ad3d4e91d65983109155a88ea23`
- 时间/作者: 2026-06-17 / caihl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `82a5c469c6` - fix issues of w13_weight using

- 完整 hash: `82a5c469c6658de6f5822bb7548f2bd2d2866f39`
- 时间/作者: 2026-06-12 / caihl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c0206c7c4a` - Release original layer.weight after deepgemm_weights conversion to avoid OOM

- 完整 hash: `c0206c7c4aa232af5fa6e47708a5656836ecab85`
- 时间/作者: 2026-06-11 / caihl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b3a4160a32` - 修复dpskv4-flash在pd分离下mtp精度问题

- 完整 hash: `b3a4160a32f126885e5ab88969aa4ee08efe9db1`
- 时间/作者: 2026-06-11 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/overlap_utils.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `64fe76840f` - [FEAT] remove vllm allreduce and dead import related

- 完整 hash: `64fe76840fa923875389027ae0515c86735def57`
- 时间/作者: 2026-06-18 / RyeYuan
- 自动分类: 通用实现调整
- 主要文件: `README_DCU.md`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`, `python/sglang/srt/distributed/parallel_state.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/parallel_state.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `38299f5fbc` - 修复崩溃bug

- 完整 hash: `38299f5fbcfa4bdc194ca577fd85f1b17c9967b0`
- 时间/作者: 2026-06-18 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/kernels.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `914d50fab3` - Create quality-baseline-scan.yml

- 完整 hash: `914d50fab3bc92138384b42b9f37bec5513a9c7d`
- 时间/作者: 2026-06-18 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-baseline-scan.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-baseline-scan.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `de2840d1d6` - 更新get_scheme函数为get_linear_scheme

- 完整 hash: `de2840d1d65bffd1d5f8297692d3b7cbf075c9ce`
- 时间/作者: 2026-06-16 / lipenghui
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bb70a2268f` - [Perf] Add packed paged KV varlen attention path

- 完整 hash: `bb70a2268faa88b431ac5ec613573ab4c14e1bec`
- 时间/作者: 2026-06-16 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`, `python/sglang/srt/server_args.py`, `test/registered/attention/bench_pack_paged_kv_to_varlen.py`, `test/registered/attention/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/test_pack_paged_kv_to_varlen.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`
  - tests: `test/registered/attention/bench_pack_paged_kv_to_varlen.py`; `test/registered/attention/pack_paged_kv_to_varlen_benchmark_results.md`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `224e5449fb` - [Bug Fix] fix swa mem pool duoble release

- 完整 hash: `224e5449fb20200f67b0744e16bce76ca0743f5d`
- 时间/作者: 2026-06-16 / shiqiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/swa_memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/swa_memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bd52e179c6` - fix: 修复EP bug

- 完整 hash: `bd52e179c66e1184418d2b6e53fca3034139b273`
- 时间/作者: 2026-06-16 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fb0a689006` - Rename lint job to lint-dcu to avoid name collision with lint.yml

- 完整 hash: `fb0a689006cd2bf2a51a499688e8a6cb65b78726`
- 时间/作者: 2026-06-15 / zhangyh15
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/lint-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `bb5f2fc8af` - ci: wait for DCU wheels on release workflow changes

- 完整 hash: `bb5f2fc8af48dafb2ef8370abe69da5ed4b60f1d`
- 时间/作者: 2026-06-15 / tianly
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `548f9aa203` - ci: skip GitHub artifact upload for DCU PR wheels

- 完整 hash: `548f9aa203029f946a26249061bde5ab258fb3d5`
- 时间/作者: 2026-06-15 / tianly
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pr-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pr-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `63747e66f9` - [BugFix] sync to support the more args 'topk_weights' in deep_ep dispatch

- 完整 hash: `63747e66f945d0d7dbd6df26213b79b40d35d0d2`
- 时间/作者: 2026-06-15 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bc649e255e` - [BUG FIX] fix swa fa accuracy because of page_table error

- 完整 hash: `bc649e255ebbe9428969d8174f86d1c3e7d9aac9`
- 时间/作者: 2026-06-15 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9da8b1176d` - [Feat] support unified fa without layout trans

- 完整 hash: `9da8b1176dcdad34ef5b1d2754fa011d29197861`
- 时间/作者: 2026-06-15 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0cdbfd7b06` - Add lint-dcu.yml for DCU self-hosted runner, restore original lint.yml

- 完整 hash: `0cdbfd7b06acaecc593ee811f09e05b97e100edf`
- 时间/作者: 2026-06-15 / zhangyh15
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/lint-dcu.yml`, `.github/workflows/release-pypi-nightky-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint-dcu.yml`; `.github/workflows/release-pypi-nightky-dcu.yml`; `.github/workflows/release-pypi-nightly-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `06331bc257` - Refactor quality gate workflow for changed files check

- 完整 hash: `06331bc2577f3b7123d7da208ad4c2a7a78b352b`
- 时间/作者: 2026-06-14 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `84cc64ecda` - Create quality-gate.yml

- 完整 hash: `84cc64ecda472cb1b7b245c467373c08cef3fa0f`
- 时间/作者: 2026-06-14 / Lvjiajia
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `083e22033e` - ci: auto-run DCU gate for impact paths

- 完整 hash: `083e22033e97a069394a80958807e3822e2d1fe0`
- 时间/作者: 2026-06-14 / tianly
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f9f0cb23d1` - ci: auto-run DCU gate for DCU-owned changes

- 完整 hash: `f9f0cb23d12197b17362b909629ef60ac4d95e7a`
- 时间/作者: 2026-06-13 / tianly
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `python/sglang/test/dcu_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `python/sglang/test/dcu_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `12a30ab42f` - ci: stabilize DCU PR test workflow

- 完整 hash: `12a30ab42f56cd8ccffc60c41b671c821d4478d6`
- 时间/作者: 2026-06-13 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml`, `.github/workflows/release-pypi-nightky-dcu.yml`, `.github/workflows/release-whl-dcu.yml`, `scripts/ci/dcu/dcu_ci_cleanup_container.sh`, `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/srt/bw1100/test_qwen25_0p5b_server_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`; `.github/workflows/release-pr-dcu.yml`; `.github/workflows/release-pypi-nightky-dcu.yml`; `.github/workflows/release-whl-dcu.yml`
  - other: `scripts/ci/dcu/dcu_ci_cleanup_container.sh`
  - tests: `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`; `test/registered/dcu/srt/bw1100/test_qwen25_0p5b_server_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `637377248a` - ci: install DCU wheel artifacts without dependencies

- 完整 hash: `637377248afc115a8db0aa52353d0ab3abdb0ed3`
- 时间/作者: 2026-06-11 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `eda451b27c` - ci: pin DCU Engine tests to fa3 backend

- 完整 hash: `eda451b27ca90501217cdb21f9fa6e66198e888c`
- 时间/作者: 2026-06-11 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/sampling/bw1100/test_original_logprobs_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`; `test/registered/dcu/sampling/bw1100/test_original_logprobs_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `033bc6b92e` - 重构aiter的重排逻辑 添加aiter log打印信息

- 完整 hash: `033bc6b92e7a115ca429bfc5fcfaed11b3d4288b`
- 时间/作者: 2026-06-11 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/moe/moe_runner/runner.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `52b5b9623c` - ci: isolate DCU wheel wait checkout workspace

- 完整 hash: `52b5b9623ced8949d028cd0d89a8cf2c7f68dd1a`
- 时间/作者: 2026-06-11 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `92a8ba840a` - [FEAT] cherry-pick and refactor from a0bcfe90, support moe triton backend and fix the acc issue in moe aiter backend

- 完整 hash: `92a8ba840a3f3dee451b8d0a9317843fcb5415c3`
- 时间/作者: 2026-06-11 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f71c2ef804` - [BugFix] fix the buffer shape unalgined issues of draft model warmup and decode forward in PD phase

- 完整 hash: `f71c2ef804e794660732cc4a8c93a2f0aac71172`
- 时间/作者: 2026-06-08 / RyeYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/overlap_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/overlap_utils.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c066cf42f7` - ci: add pull-requests:read permission to release-whl-dcu for PR file listing

- 完整 hash: `c066cf42f70f922491713725c5b693890cc74f5d`
- 时间/作者: 2026-06-10 / tianlinyang77
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-whl-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-whl-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6b0e35b3fe` - ci: prefer python3.9 for verify_dcu_registration on self-hosted runner

- 完整 hash: `6b0e35b3fe5b9bb3b6f88bd133185487b70ec51c`
- 时间/作者: 2026-06-10 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `cbf9c1ce4d` - ci: use self-hosted runner for pr-gate to avoid billing block

- 完整 hash: `cbf9c1ce4ddac5c2f52d22437dc7c8eae211f06c`
- 时间/作者: 2026-06-10 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-gate.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `adaf77ef92` - ci: always prefer self-hosted runner for pre-jobs to avoid billing block

- 完整 hash: `adaf77ef92bf4d5dd8b86e3c7cae6443985a2b37`
- 时间/作者: 2026-06-10 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e6e05f3229` - ci: test auto-trigger push flow (no-op comment)

- 完整 hash: `e6e05f32295f43a3ad0c4954cd9372cbec059176`
- 时间/作者: 2026-06-10 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/dcu/interface/test_dcu_smoke.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/interface/test_dcu_smoke.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a6c6527cd9` - fix: pass DCU_CI_USE_INSTALLED_WHEELS into docker container for wheel mode skip

- 完整 hash: `a6c6527cd92e6a15ca8d762d8697b48f7c4dd731`
- 时间/作者: 2026-06-09 / tianlinyang77
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e03bc0cf83` - fix: skip PYTHONPATH assertion in wheel mode for stage-b test

- 完整 hash: `e03bc0cf83ca3f20b88e0d73bf431f4cee49e3b3`
- 时间/作者: 2026-06-09 / tianlinyang77
- 自动分类: 缺陷修复
- 主要文件: `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `6d25108aca` - aiter适配moe_w8a8_fp8

- 完整 hash: `6d25108aca7225340084336f500ae19bd787dcfb`
- 时间/作者: 2026-06-09 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0f1ea33035` - ci: add DCU wheel sync path for PR tests

- 完整 hash: `0f1ea330354b8b113e7a7c6d81cbb3553a3ad7f0`
- 时间/作者: 2026-06-09 / dddddddxl
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-whl-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`; `.github/workflows/release-whl-dcu.yml`
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `1e1d77a76c` - 解决aiter显存溢出问题

- 完整 hash: `1e1d77a76cdaf1b3cb3ed1a3d7cb9f39b8e2d14d`
- 时间/作者: 2026-06-08 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `.gitignore`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `.gitignore`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `51abece956` - ci: remove DCU CSV coverage analyzer

- 完整 hash: `51abece95689f934afa3b03791dd39e43c8b0c3d`
- 时间/作者: 2026-06-05 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/analyze_dcu_csv_coverage.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/analyze_dcu_csv_coverage.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d6a2b719af` - ci: map DCU priority metrics model path

- 完整 hash: `d6a2b719af5d05d0a740e2fa37d855bd9955883b`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `823bd922ff` - ci: isolate DCU dispatch checkout workspace

- 完整 hash: `823bd922ffcc1f23c0e6bbf6cacec88ea7016f9f`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `d8f350eedf` - ci: avoid dispatch checkout permission issues

- 完整 hash: `d8f350eedf5fa9080cb1a6c37595c2bf2952693c`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `b95046afa0` - ci: guard DCU dispatch checkout workspace

- 完整 hash: `b95046afa07119ee257b0250d462021e08b43c10`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `7694afa394` - ci: refine DCU suite classification

- 完整 hash: `7694afa394b008be12bdea06ba376b28c9b3a500`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/language/test_srt_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`; `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`; `test/registered/language/test_srt_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cf7567773a` - ci: map DCU Qwen2.5 0.5B model path

- 完整 hash: `cf7567773afa61a9c0c78503f0642ff4a56e690e`
- 时间/作者: 2026-06-04 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `42ffb433b0` - ci: avoid ROCR device remap in DCU runner

- 完整 hash: `42ffb433b03bb5b59c19aab8c53ff6b132b8ac44`
- 时间/作者: 2026-06-04 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `cad9d0c351` - docs: add Apache license notices for DCU SGLang

- 完整 hash: `cad9d0c3519440015ecbc8df277e7cfa569eb608`
- 时间/作者: 2026-06-04 / Lv Jiajia
- 自动分类: 模型支持/运行时入口
- 主要文件: `README.md`, `README_DCU.md`, `THIRD_PARTY_NOTICES.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README.md`; `README_DCU.md`; `THIRD_PARTY_NOTICES.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `22e57a7b30` - ci: verify DCU full registration in container

- 完整 hash: `22e57a7b30d61d7d8686d3320629586fa47f013d`
- 时间/作者: 2026-06-04 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `598f2d61f0` - ci: use local DCU model env defaults

- 完整 hash: `598f2d61f0dc9278269ebd86c4bbb053acbe2a2e`
- 时间/作者: 2026-06-04 / tianlinyang77
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`
  - tests: `python/sglang/test/test_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `099123603b` - ci: run DCU full workflow on self-hosted runner

- 完整 hash: `099123603bbfe879aa7bbef73bf856759ed5c350`
- 时间/作者: 2026-06-04 / dddddddxl
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `46efb284a6` - ci: update dcu-full-enanled.yml

- 完整 hash: `46efb284a65ce0b22f26595df567ca2a44ce3083`
- 时间/作者: 2026-06-04 / dddddddxl
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `29b6895740` - ci: update DCU test registration state

- 完整 hash: `29b6895740a23ffad119c99f435264a37be5cdcd`
- 时间/作者: 2026-06-04 / dddddddxl
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `test/registered/metrics/test_metrics.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `test/registered/metrics/test_metrics.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `113d67786f` - Update chunk_delta_h.py

- 完整 hash: `113d67786f3306a5f51446e95706eab930657b65`
- 时间/作者: 2026-06-04 / yangyn
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `27ea559793` - 更新tilelang版本到0.1.9

- 完整 hash: `27ea5597933d24761e93d2933ecb7c0a9bda5c41`
- 时间/作者: 2026-06-04 / zhangyh15
- 自动分类: 通用实现调整
- 主要文件: `python/pyproject.toml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9022f2c340` - [FIX] Initialize swa_v_head_dim in TritonAttnBackend and cleanup unused import

- 完整 hash: `9022f2c340512cd3849de45e6e2a8b239091c2ac`
- 时间/作者: 2026-06-03 / shiqiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `48d234263c` - ci: pin DCU CI compatibility packages

- 完整 hash: `48d234263cb57f7cdea6320d66da363927a54414`
- 时间/作者: 2026-06-03 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c190162be1` - ci: clean DCU dispatch validation workspace

- 完整 hash: `c190162be18ef542d8c94f68604313b8b56764f9`
- 时间/作者: 2026-06-03 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `494b4246f0` - ci: allow DCU dispatch control jobs on runner

- 完整 hash: `494b4246f0f65f05e03586477d45dffd715c437a`
- 时间/作者: 2026-06-03 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `43375feaf7` - ci: stabilize DCU PR required tests

- 完整 hash: `43375feaf7699d3338e23ec0dff1eaabdf112c5c`
- 时间/作者: 2026-06-03 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `python/sglang/__init__.py`, `python/sglang/lang/api.py`, `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - other: `python/sglang/__init__.py`; `python/sglang/lang/api.py`; `scripts/ci/dcu/dcu_ci_exec.sh`
  - tests: `python/sglang/test/test_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `fba9d715f2` - 修复decode_metadata算子，import不起来的问题

- 完整 hash: `fba9d715f2f8699f55061331c690bc6a4beed4fb`
- 时间/作者: 2026-06-03 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `sgl-kernel/python/sgl_kernel/__init__.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `sgl-kernel/python/sgl_kernel/__init__.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d6baa08091` - Add DCU wheel release workflow with CIUpload repair and devpi upload

- 完整 hash: `d6baa08091544a0cb968f4df9b4be568adcdd6db`
- 时间/作者: 2026-06-03 / zhangyh15
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightky-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/release-pypi-nightky-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f13630b2e2` - fix 修复chunk_delta_h调用报错问题

- 完整 hash: `f13630b2e29c289e228995a6b3ad1a9be6b5e00d`
- 时间/作者: 2026-06-03 / yangyn1
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7b86e4afd8` - 修改aiter prefill阶段的fla算子传参

- 完整 hash: `7b86e4afd8645e2df9212db8564c84a9d5e70032`
- 时间/作者: 2026-06-03 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a04b5628ec` - 支持triton版本flash_attn算子，方便排查PA精度问题

- 完整 hash: `a04b5628ec2b6126c9e89b1f6a30fa07409b5919`
- 时间/作者: 2026-06-02 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `32d9bb7ae2` - 修复fused_sigmoid_gating_delta_rule_update冲突问题

- 完整 hash: `32d9bb7ae2686cfadc700e30ee6f8f3daad831c1`
- 时间/作者: 2026-06-01 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f7022899e5` - 增加decode_metadata sgl-kernel实现

- 完整 hash: `f7022899e5f048530be313a173b870f00b9fc73b`
- 时间/作者: 2026-05-30 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/attention/decode_metadata.cu`, `sgl-kernel/csrc/common_extension.cc`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/attention.py`, `sgl-kernel/setup_hip.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `sgl-kernel/CMakeLists.txt`; `sgl-kernel/csrc/attention/decode_metadata.cu`; `sgl-kernel/csrc/common_extension.cc`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/include/sgl_kernel_ops.h`; `sgl-kernel/python/sgl_kernel/attention.py`; `sgl-kernel/setup_hip.py` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5e3749568e` - 接入lightop layer_norm_fwd_1pass_opt算子实现

- 完整 hash: `5e3749568e0153dcecb951e402bc0c6454d4e3cb`
- 时间/作者: 2026-05-26 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fb2b0297e8` - ci: use dcu-ci-pr runner label directly

- 完整 hash: `fb2b0297e85293544a3a2caebda00f3551d6d543`
- 时间/作者: 2026-06-02 / tianly-ci
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6809e20836` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `6809e208365dcf6c881dfbfd08186759f4235f41`
- 时间/作者: 2026-06-01 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `cf08ece20a` - ci: avoid forcing DCU page size in tests

- 完整 hash: `cf08ece20ae2136890da76e052a2e7bf15634e8e`
- 时间/作者: 2026-06-01 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/lang/api.py`, `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/lang/api.py`; `scripts/ci/dcu/dcu_ci_exec.sh`
  - tests: `python/sglang/test/test_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `40fbcab062` - ci: run DCU required include-file set on PR

- 完整 hash: `40fbcab062cfcf1391cc62e6d06533fed33d516d`
- 时间/作者: 2026-06-01 / tianly-ci
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `695956fc18` - ci: apply DCU runtime defaults in CI

- 完整 hash: `695956fc18b4233438e41d220394984922569f04`
- 时间/作者: 2026-06-01 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/lang/api.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/lang/api.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e923247205` - ci: route DCU validation to nmz4 runner

- 完整 hash: `e923247205bfc50ec4200058122ae7d731528844`
- 时间/作者: 2026-06-01 / DCU CI Bot
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `987a2c813d` - ci: default DCU CI server backend to fa3

- 完整 hash: `987a2c813d9286decaffb4ac1701ed80175e20ca`
- 时间/作者: 2026-06-01 / tianly
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`
  - tests: `python/sglang/test/test_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `ad7aece93b` - ci: expand DCU PR validation matrix

- 完整 hash: `ad7aece93b5d77b35bca895554086cff134ccdaf`
- 时间/作者: 2026-06-01 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `ada40fccfd` - ci: allow full DCU validation from run-ci label

- 完整 hash: `ada40fccfd198bb7ac2b88202aeb0a8cc03805b3`
- 时间/作者: 2026-06-01 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `69dd9eb0e2` - test: align enabled DCU cases

- 完整 hash: `69dd9eb0e2a2dd1b2f415e86eb6b7222bd139328`
- 时间/作者: 2026-06-01 / tianlinyang77
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/test/dcu_utils.py`, `test/registered/metrics/test_metrics.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/dcu_utils.py`; `test/registered/metrics/test_metrics.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3334b3c5e2` - [feature support] enable cp+ep by deegemm, ensure deepgemm ver>=da4b9c1

- 完整 hash: `3334b3c5e2163e1768916b375e1f14c3e6dd388f`
- 时间/作者: 2026-05-25 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `584a9d2457` - ci: allow DCU PR workflow on dcu-ci-pr

- 完整 hash: `584a9d245791e8cd6fc927b878141d557a7f3120`
- 时间/作者: 2026-06-01 / tianly-ci
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f0cfe1740f` - ci: support DCU visible device selection

- 完整 hash: `f0cfe1740fdd6f79e71831e88e8b40082f954420`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `91b09c4464` - test: allow DCU CI to override test models

- 完整 hash: `91b09c446460abc13489ec7c59747e2a0174bc89`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/test/test_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/test_utils.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `8f4d1af5c2` - ci: use explicit DCU checkout

- 完整 hash: `8f4d1af5c2abe2f1db50aaf89face3f21a81945b`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `53a10162c8` - ci: clear DCU checkout proxy config

- 完整 hash: `53a10162c8b99958c0ae907544b712222251c6b7`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `e362080200` - ci: use static DCU git config path

- 完整 hash: `e3620802004c7e97fbc4eea90f70d7596a58f57c`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `6ba549a61c` - ci: isolate DCU runner git config

- 完整 hash: `6ba549a61c596e4d6d1e07b1636f198bf6389c35`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/pr-test-dcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f7789462f0` - ci: add DCU full enabled workflow

- 完整 hash: `f7789462f01158615f61a7c7d013f120a5ad3f4e`
- 时间/作者: 2026-06-01 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dcu-full-enabled.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/dcu-full-enabled.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f981141bef` - moe_runner适配aiter_w8a8_int8

- 完整 hash: `f981141befb3c0394d0da3d7e1f54253d2020263`
- 时间/作者: 2026-06-01 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4b76f0ef57` - ci: stabilize DCU PR runner workspace cleanup

- 完整 hash: `4b76f0ef57add43767596cb8e1960b794a6ac14a`
- 时间/作者: 2026-05-29 / tly123
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - other: `scripts/ci/dcu/dcu_ci_install_dependency.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `35522f4910` - 添加lightop提示信息

- 完整 hash: `35522f49101e26a1a3770df5053eacbc4420d65d`
- 时间/作者: 2026-05-29 / yangyn1
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `6a705f146b` - docs: sync LMSYS SGLang blog cards

- 完整 hash: `6a705f146b94da9d28b1ecc47f284349b78bc1ef`
- 时间/作者: 2026-05-29 / github-actions[bot]
- 自动分类: 测试/文档/基准
- 主要文件: `docs_new/index.mdx`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs_new/index.mdx`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `93dac7dafa` - moe-runner-backend支持lightop_moe_w8a8

- 完整 hash: `93dac7dafa458535698e81dbd5375f97929519b7`
- 时间/作者: 2026-05-28 / yangyn1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/lightop.py`; `python/sglang/srt/layers/moe/moe_runner/runner.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `02b73b2d38` - ci: fix DCU local run suite execution

- 完整 hash: `02b73b2d38b2eb10e0fe25605a3b134018b2502b`
- 时间/作者: 2026-05-28 / tly123
- 自动分类: 缺陷修复
- 主要文件: `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`; `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `74ab583258` - ci: add DCU PR CI validation flow

- 完整 hash: `74ab58325885a0242806c767946526d3ee87cde4`
- 时间/作者: 2026-05-27 / tly123
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `docs/dcu-pr-ci-visual-guide.html`, `python/sglang/test/ci/ci_register.py`, `scripts/ci/dcu/analyze_dcu_csv_coverage.py`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_install_dependency.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `scripts/ci/dcu/verify_dcu_registration.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`
  - other: `scripts/ci/dcu/analyze_dcu_csv_coverage.py`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py`
  - tests: `python/sglang/test/ci/ci_register.py`; `test/registered/dcu/interface/test_dcu_smoke.py`; `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`; `test/registered/dcu/interface/test_dcu_stage_b_flow_1.py`; `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `5cff5f5e7f` - [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0

- 完整 hash: `5cff5f5e7fb10b7b0922a21630a9d79a941b600f`
- 时间/作者: 2026-05-22 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/unquant.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5d756f9826` - fix the mtp issues of metadata loc size

- 完整 hash: `5d756f9826c74b70fb30c8fd351e6eb8ceb7dbd9`
- 时间/作者: 2026-05-14 / YuanYuan
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9c1c299194` - fix mhc with tile 0.1.9

- 完整 hash: `9c1c29919468f8a4e8075f42eeb281ba14b1842f`
- 时间/作者: 2026-04-29 / wangaq
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/mhc.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/mhc.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `2e1710ded6` - fix jit for moe_fused_gate

- 完整 hash: `2e1710ded62858f58cd46104cf5aa01701a0b358`
- 时间/作者: 2026-04-29 / wangaq
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6236ca8f5d` - [Feature] support rocm moe_fused_gate

- 完整 hash: `6236ca8f5d72fc06996085d6069e24bacdface22`
- 时间/作者: 2026-04-29 / Zhangzbb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `22d8caf080` - [Feature] support rocm moe_fused_gate

- 完整 hash: `22d8caf080301574b967755ec4dee50eb4906933`
- 时间/作者: 2026-04-28 / Zhangzbb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## hg-full-base 到 main 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 477（其中 merge 0）
- 分支更新段: `hg-full-base..main`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `.github/workflows/quality-gate.yml` | `84cc64ecd`, `06331bc25`, `b76f31cce`, `ea182d81e`, `412236292`, `bd10f999c`, `cd2e73a67`, `9188d711e`, `dccf1782b`, `e3fee4310`, `40c658e8a`, `bd60c0223`, ... (37 total) |
| `docs/internal/dcu-main-conflict-ledger.md` | `5d83cfe85`, `0536e102c`, `523756bde`, `93cf8edc4`, `ff440b897`, `e6d4b3378`, `00063277c`, `88bb5176c`, `a1ed918ae`, `bfaf180d1`, `b6db54a9a`, `1cea713a7`, ... (36 total) |
| `.github/workflows/pr-test-dcu.yml` | `74ab58325`, `4b76f0ef5`, `6ba549a61`, `e36208020`, `53a10162c`, `8f4d1af5c`, `f0cfe1740`, `584a9d245`, `ad7aece93`, `e92324720`, `40fbcab06`, `fb2b0297e`, ... (33 total) |
| `.github/workflows/release-pr-hcu.yml` | `e3fee4310`, `358a33714`, `8f848be4e`, `77939d9a5`, `997e64560`, `bfa4011ad`, `02968a96d`, `71de6dd93`, `dabae6b13`, `fb7f11956`, `b0dc28040`, `b628d29e1`, ... (26 total) |
| `.github/workflows/nightly-test-hcu.yml` | `b38f25513`, `e3fee4310`, `358a33714`, `5673a3972`, `421a13a80`, `8f848be4e`, `997e64560`, `bfa4011ad`, `6a031254f`, `02968a96d`, `b0f2bb3a8`, `1a5ce1750`, ... (22 total) |
| `.github/workflows/pr-test-hcu.yml` | `e3fee4310`, `d53953dbe`, `81e3561ae`, `5673a3972`, `bfa4011ad`, `02968a96d`, `71de6dd93`, `2fb37eaac`, `dabae6b13`, `dc5cd7089`, `b0dc28040`, `69c73a178`, ... (21 total) |
| `python/sglang/srt/server_args.py` | `93dac7daf`, `35522f491`, `f981141be`, `083e22033`, `bb70a2268`, `cae6c4496`, `9abb848db`, `35456bae3`, `c3dc2e8eb`, `36f323752`, `5d2c6854a`, `cba9e72cc`, ... (20 total) |
| `.github/workflows/dcu-full-enabled.yml` | `f7789462f`, `6ba549a61`, `e36208020`, `53a10162c`, `8f4d1af5c`, `f0cfe1740`, `ada40fccf`, `e92324720`, `46efb284a`, `099123603`, `22e57a7b3`, `12a30ab42`, ... (16 total) |
| `.github/workflows/release-docker-hcu.yml` | `b628d29e1`, `37c5b30bb`, `6b468d012`, `68dcd498a`, `8fa7122b3`, `7c8272a3a`, `5c03a8e22`, `2871c8fdd`, `5e8269d55`, `e05f146be`, `fb46d17ad`, `50b0d0051`, ... (15 total) |
| `.github/workflows/release-pypi-nightly-hcu.yml` | `b38f25513`, `e3fee4310`, `358a33714`, `8f848be4e`, `77939d9a5`, `997e64560`, `fb7f11956`, `b0dc28040`, `37c5b30bb`, `a2de3b8cf`, `7609d9af6`, `6b468d012`, ... (15 total) |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `3334b3c5e`, `82a5c469c`, `bd52e179c`, `983e644d4`, `38299f5fb`, `0553e12d0`, `dd2685439`, `8efd2ad46`, `0395a2bd2`, `7b6a9dd89`, `9a4f82911`, `0305c5a3b`, ... (13 total) |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `4e3fd3a35`, `6d25108ac`, `033bc6b92`, `c0206c7c4`, `82a5c469c`, `9abb848db`, `445eaafe5`, `35456bae3`, `2b1fbe1e6`, `4a6fbed98`, `b36730b41`, `ccbb65acb`, ... (13 total) |
| `scripts/ci/dcu/dcu_ci_exec.sh` | `74ab58325`, `f0cfe1740`, `987a2c813`, `cf08ece20`, `43375feaf`, `598f2d61f`, `f57339642`, `42ffb433b`, `cf7567773`, `d6a2b719a`, `0f1ea3303`, `a6c6527cd`, ... (13 total) |
| `.github/workflows/dcu-manual-model-test.yml` | `be7d10f53`, `d1ea0b3aa`, `c7a4903ad`, `ca7c7c54f`, `db4759e78`, `20eb46a70`, `7d807cb22`, `8aa4b6eb5`, `21dfaaa4c`, `e3fee4310` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `f7022899e`, `c4d3532db`, `9da8b1176`, `bc649e255`, `bb70a2268`, `fa6b75971`, `4d198708c`, `2981595c7`, `62a07586d`, `11d08002b` |
| `python/sglang/srt/managers/scheduler.py` | `b3a4160a3`, `fe9f24924`, `e47445d2f`, `7941e0419`, `83d2a2b4b`, `c3755b4d4`, `4e5a95fcb`, `84bfd45c4`, `dc015a0bc`, `497c35457` |
| `.github/workflows/cookbook-deployment-smoke.yml` | `50b0d0051`, `f9b972b37`, `b6dd37e66`, `78c700ee0`, `cc3758967`, `87b9d5c85`, `f89209aa8`, `a8543c813`, `029b6e641` |
| `.github/workflows/hcu-full-enabled.yml` | `e3fee4310`, `bfa4011ad`, `02968a96d`, `71de6dd93`, `dabae6b13`, `132b630bc`, `4c7a264e5`, `b0dc28040`, `e05f146be` |
| `.github/workflows/release-pypi-nightly-dcu.yml` | `0cdbfd7b0`, `ca95a26da`, `9304b9e1d`, `f4716f8ec`, `595f87c93`, `83294cba6`, `e3fee4310`, `b2f0b830c`, `37c5b30bb` |
| `.github/workflows/lint-hcu.yml` | `e3fee4310`, `358a33714`, `8f848be4e`, `77939d9a5`, `997e64560`, `69c73a178`, `3e6aaf09d`, `e05f146be` |
| `.github/workflows/quality-baseline-scan.yml` | `914d50fab`, `fa22ad5ae`, `e80c0644a`, `37a67648f`, `41db24a84`, `72f023717`, `af015c4ce`, `f76d2cea3` |
| `scripts/ci/hcu/hcu_ci_notify_feishu.py` | `5673a3972`, `e338cca15`, `2c21b95e6`, `4af810205`, `9e13c77ce`, `85dcec947`, `67ecec8dd`, `8e2aba4bf` |
| `.github/workflows/nightly-test-dcu.yml` | `ca95a26da`, `de24697cb`, `00febcba4`, `fa2430f45`, `e3fee4310`, `b2f0b830c`, `37c5b30bb` |
| `.github/workflows/nightly-test-operator-hcu.yml` | `fb46d17ad`, `4205397cb`, `e295faff5`, `6dac3481c`, `fd98647ed`, `db479b030`, `9fb319cc3` |
| `docker/hcu.Dockerfile` | `b628d29e1`, `7609d9af6`, `6b468d012`, `68dcd498a`, `7c8272a3a`, `5c03a8e22`, `2871c8fdd` |
| `scripts/ci/dcu/dcu_ci_install_dependency.sh` | `74ab58325`, `4b76f0ef5`, `48d234263`, `0f1ea3303`, `637377248`, `00ce3e6d9`, `e3fee4310` |
| `scripts/ci/hcu/hcu_ci_install_dependency.sh` | `e3fee4310`, `71de6dd93`, `dabae6b13`, `2828bde71`, `0af71f61b`, `575cf4797`, `adc1d69b2` |
| `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | `5673a3972`, `e338cca15`, `2c21b95e6`, `4af810205`, `9e13c77ce`, `6a031254f`, `67ecec8dd` |
| `.github/workflows/hcu-feishu-notify-preview.yml` | `2c21b95e6`, `6ac12c2e5`, `65b7c4268`, `0ff7a014f`, `9c69436ee`, `e05f146be` |
| `README_DCU.md` | `cad9d0c35`, `64fe76840`, `be7d10f53`, `d1ea0b3aa`, `3dd1376ff`, `9353ecb96` |
| `docs_new/index.mdx` | `6a705f146`, `6809e2083`, `20f106c6b`, `ce2521017`, `3f920d4e0`, `fe4e1fea3` |
| `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | `64d1765b4`, `6c1786bc4`, `ca9b264a2`, `7482123c3`, `d42ecf6fe`, `fd4157047` |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `a04b5628e`, `0fc338999`, `62a07586d`, `11d08002b`, `72d1d2a73`, `27ce43c71` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `f981141be`, `1e1d77a76`, `6d25108ac`, `033bc6b92`, `83f43b3f4`, `8e2aba4bf` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `6d25108ac`, `033bc6b92`, `cae6c4496`, `9abb848db`, `35456bae3`, `4d198708c` |
| `python/sglang/test/hcu_cookbook_utils.py` | `427726d60`, `83d2a2b4b`, `e338cca15`, `132b630bc`, `4c7a264e5`, `9d261478d` |
| `python/sglang/test/test_utils.py` | `91b09c446`, `987a2c813`, `cf08ece20`, `43375feaf`, `598f2d61f`, `f57339642` |
| `scripts/ci/dcu/check_hcu_runtime_text.py` | `9188d711e`, `8b4a7bdeb`, `fda6d44a4`, `616ba7b6d`, `e3fee4310`, `40c658e8a` |
| `scripts/ci/dcu/dcu_ci_start_container.sh` | `74ab58325`, `f0cfe1740`, `f57339642`, `42ffb433b`, `00ce3e6d9`, `e3fee4310` |
| `test/run_suite.py` | `74ab58325`, `02b73b2d3`, `4a08e1934`, `f17440f19`, `8dd5daf2f`, `6fe7ce909` |
| ... | 另有 403 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-28 | `22d8caf08` | `hg-full-base..main` | 性能/后端优化 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 6 个文件 |
| 2026-04-29 | `6236ca8f5` | `hg-full-base..main` | 性能/后端优化 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-04-29 | `2e1710ded` | `hg-full-base..main` | 性能/后端优化 | fix jit for moe_fused_gate | `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-04-29 | `9c1c29919` | `hg-full-base..main` | 缺陷修复 | fix mhc with tile 0.1.9 | `python/sglang/srt/layers/mhc.py` |
| 2026-05-14 | `5d756f982` | `hg-full-base..main` | 缺陷修复 | fix the mtp issues of metadata loc size | `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-05-21 | `aee2b606f` | `hg-full-base..main` | 性能/后端优化 | feat(diffusion): add ROCm SLA attention backend | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` 等 6 个文件 |
| 2026-05-22 | `5cff5f5e7` | `hg-full-base..main` | 性能/后端优化 | [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0 | `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-05-25 | `3334b3c5e` | `hg-full-base..main` | 性能/后端优化 | [feature support] enable cp+ep by deegemm, ensure deepgemm ver>=da4b9c1 | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-05-26 | `5e3749568` | `hg-full-base..main` | 性能/后端优化 | 接入lightop layer_norm_fwd_1pass_opt算子实现 | `python/sglang/srt/layers/attention/fla/layernorm_gated.py` |
| 2026-05-27 | `74ab58325` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add DCU PR CI validation flow | `.github/workflows/pr-test-dcu.yml`, `docs/dcu-pr-ci-visual-guide.html`, `python/sglang/test/ci/ci_register.py` 等 12 个文件 |
| 2026-05-28 | `02b73b2d3` | `hg-full-base..main` | 缺陷修复 | ci: fix DCU local run suite execution | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`, `test/run_suite.py` |
| 2026-05-28 | `93dac7daf` | `hg-full-base..main` | 性能/后端优化 | moe-runner-backend支持lightop_moe_w8a8 | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py` 等 5 个文件 |
| 2026-05-29 | `6a705f146` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-05-29 | `35522f491` | `hg-full-base..main` | 通用实现调整 | 添加lightop提示信息 | `python/sglang/srt/server_args.py` |
| 2026-05-29 | `4b76f0ef5` | `hg-full-base..main` | 测试/文档/基准 | ci: stabilize DCU PR runner workspace cleanup | `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-05-30 | `f7022899e` | `hg-full-base..main` | 性能/后端优化 | 增加decode_metadata sgl-kernel实现 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/attention/decode_metadata.cu` 等 9 个文件 |
| 2026-06-01 | `f981141be` | `hg-full-base..main` | 性能/后端优化 | moe_runner适配aiter_w8a8_int8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py` |
| 2026-06-01 | `f7789462f` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add DCU full enabled workflow | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-01 | `6ba549a61` | `hg-full-base..main` | 测试/文档/基准 | ci: isolate DCU runner git config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `e36208020` | `hg-full-base..main` | 测试/文档/基准 | ci: use static DCU git config path | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `53a10162c` | `hg-full-base..main` | 测试/文档/基准 | ci: clear DCU checkout proxy config | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `8f4d1af5c` | `hg-full-base..main` | 测试/文档/基准 | ci: use explicit DCU checkout | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `91b09c446` | `hg-full-base..main` | 模型支持/运行时入口 | test: allow DCU CI to override test models | `python/sglang/test/test_utils.py` |
| 2026-06-01 | `faff8208c` | `hg-full-base..main` | 缺陷修复 | fix: restore qwen2 rope config import | `python/sglang/srt/models/qwen2.py` |
| 2026-06-01 | `f0cfe1740` | `hg-full-base..main` | 模型支持/运行时入口 | ci: support DCU visible device selection | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` 等 4 个文件 |
| 2026-06-01 | `584a9d245` | `hg-full-base..main` | 测试/文档/基准 | ci: allow DCU PR workflow on dcu-ci-pr | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `69dd9eb0e` | `hg-full-base..main` | 测试/文档/基准 | test: align enabled DCU cases | `python/sglang/test/dcu_utils.py`, `test/registered/metrics/test_metrics.py` |
| 2026-06-01 | `ada40fccf` | `hg-full-base..main` | 测试/文档/基准 | ci: allow full DCU validation from run-ci label | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-01 | `ad7aece93` | `hg-full-base..main` | 测试/文档/基准 | ci: expand DCU PR validation matrix | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `987a2c813` | `hg-full-base..main` | 测试/文档/基准 | ci: default DCU CI server backend to fa3 | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-01 | `e92324720` | `hg-full-base..main` | 测试/文档/基准 | ci: route DCU validation to nmz4 runner | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `695956fc1` | `hg-full-base..main` | 测试/文档/基准 | ci: apply DCU runtime defaults in CI | `python/sglang/lang/api.py` |
| 2026-06-01 | `40fbcab06` | `hg-full-base..main` | 测试/文档/基准 | ci: run DCU required include-file set on PR | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-01 | `cf08ece20` | `hg-full-base..main` | 测试/文档/基准 | ci: avoid forcing DCU page size in tests | `python/sglang/lang/api.py`, `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-01 | `6809e2083` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-06-01 | `32d9bb7ae` | `hg-full-base..main` | 性能/后端优化 | 修复fused_sigmoid_gating_delta_rule_update冲突问题 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-06-02 | `fb2b0297e` | `hg-full-base..main` | 测试/文档/基准 | ci: use dcu-ci-pr runner label directly | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-02 | `a04b5628e` | `hg-full-base..main` | 性能/后端优化 | 支持triton版本flash_attn算子，方便排查PA精度问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` |
| 2026-06-03 | `7b86e4afd` | `hg-full-base..main` | 性能/后端优化 | 修改aiter prefill阶段的fla算子传参 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py` |
| 2026-06-03 | `f13630b2e` | `hg-full-base..main` | 缺陷修复 | fix 修复chunk_delta_h调用报错问题 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-06-03 | `d6baa0809` | `hg-full-base..main` | 模型支持/运行时入口 | Add DCU wheel release workflow with CIUpload repair and devpi upload | `.github/workflows/release-pypi-nightky-dcu.yml` |
| 2026-06-03 | `fba9d715f` | `hg-full-base..main` | 性能/后端优化 | 修复decode_metadata算子，import不起来的问题 | `sgl-kernel/python/sgl_kernel/__init__.py` |
| 2026-06-03 | `43375feaf` | `hg-full-base..main` | 测试/文档/基准 | ci: stabilize DCU PR required tests | `.github/workflows/pr-test-dcu.yml`, `python/sglang/__init__.py`, `python/sglang/lang/api.py` 等 5 个文件 |
| 2026-06-03 | `494b4246f` | `hg-full-base..main` | 测试/文档/基准 | ci: allow DCU dispatch control jobs on runner | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-03 | `c190162be` | `hg-full-base..main` | 测试/文档/基准 | ci: clean DCU dispatch validation workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-03 | `48d234263` | `hg-full-base..main` | 测试/文档/基准 | ci: pin DCU CI compatibility packages | `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-06-03 | `9022f2c34` | `hg-full-base..main` | 缺陷修复 | [FIX] Initialize swa_v_head_dim in TritonAttnBackend and cleanup unused import | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-06-03 | `4e3fd3a35` | `hg-full-base..main` | 性能/后端优化 | HY3修改 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-03 | `5245654dc` | `hg-full-base..main` | 缺陷修复 | Fix: DCU bypass Triton get_last_loc and use native dcu_get_last_loc | `python/sglang/srt/mem_cache/common.py` |
| 2026-06-04 | `27ea55979` | `hg-full-base..main` | 通用实现调整 | 更新tilelang版本到0.1.9 | `python/pyproject.toml` |
| 2026-06-04 | `113d67786` | `hg-full-base..main` | 调度/缓存/PD | Update chunk_delta_h.py | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-06-04 | `29b689574` | `hg-full-base..main` | 调度/缓存/PD | ci: update DCU test registration state | `.github/workflows/pr-test-dcu.yml`, `test/registered/metrics/test_metrics.py` |
| 2026-06-04 | `46efb284a` | `hg-full-base..main` | 调度/缓存/PD | ci: update dcu-full-enanled.yml | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `099123603` | `hg-full-base..main` | 测试/文档/基准 | ci: run DCU full workflow on self-hosted runner | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `598f2d61f` | `hg-full-base..main` | 模型支持/运行时入口 | ci: use local DCU model env defaults | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-04 | `22e57a7b3` | `hg-full-base..main` | 测试/文档/基准 | ci: verify DCU full registration in container | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-04 | `f57339642` | `hg-full-base..main` | 性能/后端优化 | ci: keep DCU test defaults official-friendly | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` 等 17 个文件 |
| 2026-06-04 | `cad9d0c35` | `hg-full-base..main` | 模型支持/运行时入口 | docs: add Apache license notices for DCU SGLang | `README.md`, `README_DCU.md`, `THIRD_PARTY_NOTICES.md` |
| 2026-06-04 | `42ffb433b` | `hg-full-base..main` | 测试/文档/基准 | ci: avoid ROCR device remap in DCU runner | `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` |
| 2026-06-04 | `cf7567773` | `hg-full-base..main` | 模型支持/运行时入口 | ci: map DCU Qwen2.5 0.5B model path | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-05 | `7694afa39` | `hg-full-base..main` | 性能/后端优化 | ci: refine DCU suite classification | `test/registered/dcu/kernels/test_sgl_kernel_smoke_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/language/test_srt_backend.py` |
| 2026-06-05 | `b95046afa` | `hg-full-base..main` | 测试/文档/基准 | ci: guard DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `d8f350eed` | `hg-full-base..main` | 测试/文档/基准 | ci: avoid dispatch checkout permission issues | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `823bd922f` | `hg-full-base..main` | 测试/文档/基准 | ci: isolate DCU dispatch checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-05 | `d6a2b719a` | `hg-full-base..main` | 模型支持/运行时入口 | ci: map DCU priority metrics model path | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-05 | `51abece95` | `hg-full-base..main` | 测试/文档/基准 | ci: remove DCU CSV coverage analyzer | `scripts/ci/dcu/analyze_dcu_csv_coverage.py` |
| 2026-06-08 | `1e1d77a76` | `hg-full-base..main` | 性能/后端优化 | 解决aiter显存溢出问题 | `.gitignore`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-06-08 | `f71c2ef80` | `hg-full-base..main` | 缺陷修复 | [BugFix] fix the buffer shape unalgined issues of draft model warmup and decode forward in PD phase | `python/sglang/srt/managers/overlap_utils.py` |
| 2026-06-09 | `0f1ea3303` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add DCU wheel sync path for PR tests | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-whl-dcu.yml`, `scripts/ci/dcu/dcu_ci_exec.sh` 等 4 个文件 |
| 2026-06-09 | `6d25108ac` | `hg-full-base..main` | 性能/后端优化 | aiter适配moe_w8a8_fp8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-06-09 | `e03bc0cf8` | `hg-full-base..main` | 缺陷修复 | fix: skip PYTHONPATH assertion in wheel mode for stage-b test | `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py` |
| 2026-06-09 | `a6c6527cd` | `hg-full-base..main` | 缺陷修复 | fix: pass DCU_CI_USE_INSTALLED_WHEELS into docker container for wheel mode skip | `scripts/ci/dcu/dcu_ci_exec.sh` |
| 2026-06-09 | `c4d3532db` | `hg-full-base..main` | 性能/后端优化 | fix:dcu bypass triton normal_decode_set_metadata use normal_decode_set_metadata_lightop | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-10 | `e6e05f322` | `hg-full-base..main` | 测试/文档/基准 | ci: test auto-trigger push flow (no-op comment) | `test/registered/dcu/interface/test_dcu_smoke.py` |
| 2026-06-10 | `adaf77ef9` | `hg-full-base..main` | 测试/文档/基准 | ci: always prefer self-hosted runner for pre-jobs to avoid billing block | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-10 | `cbf9c1ce4` | `hg-full-base..main` | 测试/文档/基准 | ci: use self-hosted runner for pr-gate to avoid billing block | `.github/workflows/pr-gate.yml` |
| 2026-06-10 | `6b0e35b3f` | `hg-full-base..main` | 测试/文档/基准 | ci: prefer python3.9 for verify_dcu_registration on self-hosted runner | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-10 | `c066cf42f` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add pull-requests:read permission to release-whl-dcu for PR file listing | `.github/workflows/release-whl-dcu.yml` |
| 2026-06-11 | `92a8ba840` | `hg-full-base..main` | 性能/后端优化 | [FEAT] cherry-pick and refactor from a0bcfe90, support moe triton backend and fix the acc issue in moe aiter backend | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` |
| 2026-06-11 | `52b5b9623` | `hg-full-base..main` | 测试/文档/基准 | ci: isolate DCU wheel wait checkout workspace | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-11 | `033bc6b92` | `hg-full-base..main` | 性能/后端优化 | 重构aiter的重排逻辑 添加aiter log打印信息 | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 5 个文件 |
| 2026-06-11 | `da04ee008` | `hg-full-base..main` | 缺陷修复 | ci: fix DCU PR required regressions | `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/models/qwen2.py`, `test/registered/core/test_hidden_states.py` 等 6 个文件 |
| 2026-06-11 | `eda451b27` | `hg-full-base..main` | 测试/文档/基准 | ci: pin DCU Engine tests to fa3 backend | `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/sampling/bw1100/test_original_logprobs_dcu.py` |
| 2026-06-11 | `637377248` | `hg-full-base..main` | 测试/文档/基准 | ci: install DCU wheel artifacts without dependencies | `scripts/ci/dcu/dcu_ci_install_dependency.sh` |
| 2026-06-11 | `b3a4160a3` | `hg-full-base..main` | 性能/后端优化 | 修复dpskv4-flash在pd分离下mtp精度问题 | `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-06-11 | `c0206c7c4` | `hg-full-base..main` | 性能/后端优化 | Release original layer.weight after deepgemm_weights conversion to avoid OOM | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-12 | `82a5c469c` | `hg-full-base..main` | 性能/后端优化 | fix issues of w13_weight using | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-13 | `12a30ab42` | `hg-full-base..main` | 测试/文档/基准 | ci: stabilize DCU PR test workflow | `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml` 等 8 个文件 |
| 2026-06-13 | `f9f0cb23d` | `hg-full-base..main` | 测试/文档/基准 | ci: auto-run DCU gate for DCU-owned changes | `.github/workflows/pr-test-dcu.yml`, `python/sglang/test/dcu_utils.py` |
| 2026-06-14 | `083e22033` | `hg-full-base..main` | 测试/文档/基准 | ci: auto-run DCU gate for impact paths | `.github/workflows/pr-test-dcu.yml`, `python/sglang/srt/server_args.py` |
| 2026-06-14 | `84cc64ecd` | `hg-full-base..main` | 通用实现调整 | Create quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-06-14 | `06331bc25` | `hg-full-base..main` | 通用实现调整 | Refactor quality gate workflow for changed files check | `.github/workflows/quality-gate.yml` |
| 2026-06-15 | `0cdbfd7b0` | `hg-full-base..main` | 模型支持/运行时入口 | Add lint-dcu.yml for DCU self-hosted runner, restore original lint.yml | `.github/workflows/lint-dcu.yml`, `.github/workflows/release-pypi-nightky-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-15 | `9da8b1176` | `hg-full-base..main` | 性能/后端优化 | [Feat] support unified fa without layout trans | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-15 | `bc649e255` | `hg-full-base..main` | 性能/后端优化 | [BUG FIX] fix swa fa accuracy because of page_table error | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-06-15 | `63747e66f` | `hg-full-base..main` | 性能/后端优化 | [BugFix] sync to support the more args 'topk_weights' in deep_ep dispatch | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-06-15 | `548f9aa20` | `hg-full-base..main` | 测试/文档/基准 | ci: skip GitHub artifact upload for DCU PR wheels | `.github/workflows/release-pr-dcu.yml` |
| 2026-06-15 | `bb5f2fc8a` | `hg-full-base..main` | 测试/文档/基准 | ci: wait for DCU wheels on release workflow changes | `.github/workflows/pr-test-dcu.yml` |
| 2026-06-15 | `fb0a68900` | `hg-full-base..main` | 通用实现调整 | Rename lint job to lint-dcu to avoid name collision with lint.yml | `.github/workflows/lint-dcu.yml` |
| 2026-06-16 | `bd52e179c` | `hg-full-base..main` | 性能/后端优化 | fix: 修复EP bug | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-06-16 | `224e5449f` | `hg-full-base..main` | 缺陷修复 | [Bug Fix] fix swa mem pool duoble release | `python/sglang/srt/mem_cache/swa_memory_pool.py` |
| 2026-06-16 | `bb70a2268` | `hg-full-base..main` | 性能/后端优化 | [Perf] Add packed paged KV varlen attention path | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/pack_paged_kv_to_varlen.py`, `python/sglang/srt/server_args.py` 等 6 个文件 |
| 2026-06-16 | `189d8c87e` | `hg-full-base..main` | 缺陷修复 | [bugfix]修复md文件中的格式问题 | `.claude/skills/sglang-profile-analyse/SKILL.md`, `python/sglang/srt/models/utils.py` |
| 2026-06-16 | `de2840d1d` | `hg-full-base..main` | 性能/后端优化 | 更新get_scheme函数为get_linear_scheme | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-06-17 | `983e644d4` | `hg-full-base..main` | 性能/后端优化 | fix: avoid redundant calls to forward_aiter and fp8 groupgemm kernels | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-18 | `914d50fab` | `hg-full-base..main` | 通用实现调整 | Create quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `38299f5fb` | `hg-full-base..main` | 性能/后端优化 | 修复崩溃bug | `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-18 | `64fe76840` | `hg-full-base..main` | 通用实现调整 | [FEAT] remove vllm allreduce and dead import related | `README_DCU.md`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 4 个文件 |
| 2026-06-18 | `fa22ad5ae` | `hg-full-base..main` | 性能/后端优化 | Add options for encoding, dependencies, and SAST scans | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `e80c0644a` | `hg-full-base..main` | 调度/缓存/PD | Update Trivy and Semgrep commands in workflow | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `37a67648f` | `hg-full-base..main` | 调度/缓存/PD | Update Trivy scan configuration in workflow | `.github/workflows/quality-baseline-scan.yml` |
| 2026-06-18 | `87aa66f4f` | `hg-full-base..main` | 性能/后端优化 | [BugFix] workaround fix of aiter custom allreduce in cuda-graph, would revert it after driver fix it | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-06-18 | `cae6c4496` | `hg-full-base..main` | 性能/后端优化 | [FEAT] implement the initial changes about w8a8 megamoe for DCU | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` 等 4 个文件 |
| 2026-06-22 | `0fc338999` | `hg-full-base..main` | 性能/后端优化 | 修复dpsk r1 fp8启动时的报错问题 | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-22 | `5d83cfe85` | `hg-full-base..main` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-22 | `0536e102c` | `hg-full-base..main` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-22 | `fdd9f8ecf` | `hg-full-base..main` | 缺陷修复 | [BUG FIX] fix SWA mem pool issue causing accept length decrease | `python/sglang/srt/mem_cache/swa_memory_pool.py` |
| 2026-06-23 | `51abf3148` | `hg-full-base..main` | 模型支持/运行时入口 | test: add DCU AI smoke cases to PR required | `.github/workflows/pr-test-dcu.yml`, `test/registered/dcu/openai_server/test_function_calling_dcu.py`, `test/registered/dcu/openai_server/test_hidden_states_base_dcu.py` 等 13 个文件 |
| 2026-06-23 | `4b8a743d3` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add wheel mode to DCU full enabled | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-23 | `ca95a26da` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add DCU nightly workflow with wheel build | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-23 | `9ed791e14` | `hg-full-base..main` | 测试/文档/基准 | ci: run PR helper workflows on private runner | `.github/workflows/labeler.yml`, `.github/workflows/pr-states.yml` |
| 2026-06-23 | `de24697cb` | `hg-full-base..main` | 测试/文档/基准 | ci: disable PR trigger for DCU nightly workflow | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-23 | `9304b9e1d` | `hg-full-base..main` | 测试/文档/基准 | ci: build DCU gateway wheel by default | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-23 | `be7d10f53` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add manual DCU unattended model test workflow | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` |
| 2026-06-24 | `00ce3e6d9` | `hg-full-base..main` | 测试/文档/基准 | ci: stage DCU PR wheels locally | `.github/workflows/pr-test-dcu.yml`, `.github/workflows/release-pr-dcu.yml`, `scripts/ci/dcu/dcu_ci_install_dependency.sh` 等 4 个文件 |
| 2026-06-24 | `f4716f8ec` | `hg-full-base..main` | 模型支持/运行时入口 | Add DCU nightly wheel release workflow | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-24 | `595f87c93` | `hg-full-base..main` | 测试/文档/基准 | Restore push trigger and CIUpload devpi upload | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-24 | `88ba08ad2` | `hg-full-base..main` | 性能/后端优化 | fix expert_location_dispatch_info is not define | `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-24 | `523756bde` | `hg-full-base..main` | 调度/缓存/PD | [docs(dcu)] log C01/C02 conflict ledger update | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-25 | `85cd7901c` | `hg-full-base..main` | 性能/后端优化 | test: keep verified DCU smoke and accuracy cases only | `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py` 等 4 个文件 |
| 2026-06-25 | `4a08e1934` | `hg-full-base..main` | 性能/后端优化 | test: add DCU nightly 1 and 2 GPU suites | `test/registered/core/test_mm_process_config.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py` 等 19 个文件 |
| 2026-06-25 | `d1ea0b3aa` | `hg-full-base..main` | 模型支持/运行时入口 | ci: support configurable manual DCU model validation | `.github/workflows/dcu-manual-model-test.yml`, `README_DCU.md` |
| 2026-06-25 | `3dd1376ff` | `hg-full-base..main` | 缺陷修复 | docs: fix DCU README trailing whitespace | `README_DCU.md` |
| 2026-06-25 | `9abb848db` | `hg-full-base..main` | 性能/后端优化 | [Feat] support megamoe in the path of SGLANG_DCU_MEGA_MOE_RUNTIME=megamoe, and temporarily deepgeem path is still remained as backup | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 7 个文件 |
| 2026-06-25 | `c7a4903ad` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `ca7c7c54f` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `2f2abec11` | `hg-full-base..main` | 测试/文档/基准 | ci: cover new DCU nightly suites in full enabled | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-26 | `db4759e78` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `20eb46a70` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `0c4fe5ebe` | `hg-full-base..main` | 测试/文档/基准 | ci: align DCU full wheel wait with PR staging | `.github/workflows/dcu-full-enabled.yml` |
| 2026-06-26 | `7d807cb22` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `8aa4b6eb5` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `21dfaaa4c` | `hg-full-base..main` | 调度/缓存/PD | Update dcu-manual-model-test.yml | `.github/workflows/dcu-manual-model-test.yml` |
| 2026-06-26 | `00febcba4` | `hg-full-base..main` | 测试/文档/基准 | ci: reuse PR-staged DCU nightly wheels | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-26 | `a2076d9aa` | `hg-full-base..main` | 测试/文档/基准 | test: use local DCU eval datasets | `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_mmlu.py` 等 4 个文件 |
| 2026-06-28 | `f40a12fb5` | `hg-full-base..main` | 性能/后端优化 | 修改IPC逻辑，每个rank下都开辟内存池，解决rank0偶发变慢的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py` |
| 2026-06-29 | `395171de0` | `hg-full-base..main` | 缺陷修复 | test: fix DCU MMMU local dataset selection | `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py` |
| 2026-06-29 | `83294cba6` | `hg-full-base..main` | 模型支持/运行时入口 | Add DCU nightly wheel release workflow with vendored-openssl support | `.github/workflows/release-pypi-nightly-dcu.yml` |
| 2026-06-29 | `0553e12d0` | `hg-full-base..main` | 性能/后端优化 | 修复合并分支产生的bug | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-06-29 | `06889adc0` | `hg-full-base..main` | 调度/缓存/PD | Disable DCU update weights from disk nightly test | `test/registered/rl/test_update_weights_from_disk.py` |
| 2026-06-29 | `01216a18f` | `hg-full-base..main` | 测试/文档/基准 | Disable DCU remote weight loading nightly test | `test/registered/distributed/test_load_weights_from_remote_instance.py` |
| 2026-06-29 | `75e928284` | `hg-full-base..main` | 性能/后端优化 | Register DCU tests in categorized nightly suites | `test/registered/constrained_decoding/test_constrained_decoding.py`, `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/embedding/bw1100/test_gte_qwen2_embedding_dcu.py` 等 28 个文件 |
| 2026-06-29 | `fa2430f45` | `hg-full-base..main` | 测试/文档/基准 | Organize DCU nightly workflow modules | `.github/workflows/nightly-test-dcu.yml` |
| 2026-06-30 | `d22548eb1` | `hg-full-base..main` | 性能/后端优化 | feat(sgl-kernel): port l2norm kernel with tiled optimization for DCU | `python/sglang/srt/layers/attention/fla/l2norm.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/common_extension.cc` 等 11 个文件 |
| 2026-06-30 | `93cf8edc4` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `b76f31cce` | `hg-full-base..main` | 通用实现调整 | Refactor quality-gate.yml with enhanced checks | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `f2e257f7a` | `hg-full-base..main` | 性能/后端优化 | feat(dcu): route sqrtsoftplus gating through LightOp | `python/sglang/srt/layers/moe/topk.py` |
| 2026-06-30 | `bda910adb` | `hg-full-base..main` | 性能/后端优化 | feat(dcu): integrate LightOp alloc-extend kernel | `python/sglang/srt/mem_cache/allocator.py` |
| 2026-06-30 | `ea182d81e` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow with environment variables | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `412236292` | `hg-full-base..main` | 调度/缓存/PD | Modify ruff command to use --no-cache | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `bd10f999c` | `hg-full-base..main` | 缺陷修复 | Fix formatting and improve quality gate script | `.github/workflows/quality-gate.yml` |
| 2026-06-30 | `3910b3f9d` | `hg-full-base..main` | 缺陷修复 | fix(scheduler): restore DCU empty-prefix location | `python/sglang/srt/managers/schedule_batch.py` |
| 2026-06-30 | `ff440b897` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record C04 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `445eaafe5` | `hg-full-base..main` | 性能/后端优化 | [Perf] optimize aiter asm moe via shuffle weight | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-07-01 | `41db24a84` | `hg-full-base..main` | 通用实现调整 | Enhance quality baseline scan with new checks | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-01 | `20f106c6b` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-01 | `72f023717` | `hg-full-base..main` | 通用实现调整 | Remove credential keyword pattern from scan config | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-01 | `af015c4ce` | `hg-full-base..main` | 调度/缓存/PD | Update Trivy cache volume permissions | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-01 | `35456bae3` | `hg-full-base..main` | 性能/后端优化 | [CI] fix pre-commit lint errors on megamoe w8a8 changed files | `.codespellrc`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 7 个文件 |
| 2026-07-01 | `2b1fbe1e6` | `hg-full-base..main` | 性能/后端优化 | [CI] fix pre-commit lint errors surfaced after merging v0.5.12_dev | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-07-01 | `696cae936` | `hg-full-base..main` | 缺陷修复 | fix(fst): use local device in fastsafetensors iterator for multi-node loading | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-07-01 | `998ffb809` | `hg-full-base..main` | 缺陷修复 | fix(fst): reclaim reserved memory after fastsafetensors weight load | `python/sglang/srt/model_loader/loader.py` |
| 2026-07-01 | `e6d4b3378` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-01 | `ef3571f7b` | `hg-full-base..main` | 性能/后端优化 | 解决CI报错问题 | `python/sglang/srt/utils/cuda_ipc_transport_utils.py` |
| 2026-07-02 | `633270429` | `hg-full-base..main` | 测试/文档/基准 | ci: extend DCU stage-b per-file timeout | `.github/workflows/pr-test-dcu.yml` |
| 2026-07-02 | `758a0a989` | `hg-full-base..main` | 模型支持/运行时入口 | Add open-source compliance configuration file | `.github/open-source-compliance.json` |
| 2026-07-02 | `fc2af9331` | `hg-full-base..main` | 模型支持/运行时入口 | Add open-source compliance baseline workflow | `.github/workflows/open-source-compliance-baseline.yml` |
| 2026-07-02 | `dd2685439` | `hg-full-base..main` | 性能/后端优化 | support w4a16 moe ep | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-07-02 | `84bd983ba` | `hg-full-base..main` | 模型支持/运行时入口 | ci: use local DCU reranker model | `.github/workflows/pr-test-dcu.yml` |
| 2026-07-03 | `ce2521017` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-03 | `c3dc2e8eb` | `hg-full-base..main` | 通用实现调整 | feat: validate DCU attention backend compatibility | `python/sglang/srt/server_args.py` |
| 2026-07-03 | `00063277c` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C07 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-03 | `8efd2ad46` | `hg-full-base..main` | 性能/后端优化 | update w4a16 deepgemm interface | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-04 | `cd2e73a67` | `hg-full-base..main` | 性能/后端优化 | 优化lint扫描规则 | `.github/workflows/quality-gate.yml` |
| 2026-07-05 | `36f323752` | `hg-full-base..main` | 性能/后端优化 | fix: refine HCU runtime log wording | `python/sglang/check_env.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/mxfp4.py` 等 9 个文件 |
| 2026-07-05 | `107be429b` | `hg-full-base..main` | 性能/后端优化 | chore: fix encoding baseline issues | `3rdparty/amd/profiling/torch_profiler.patch`, `docs/supported_models/specialized/reward_models.md`, `docs_new/docs/developer_guide/development_guide_using_docker.mdx` 等 13 个文件 |
| 2026-07-06 | `88bb5176c` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C08 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-06 | `10e17ae89` | `hg-full-base..main` | 通用实现调整 | loader: stream FSDP state dicts for Ulysses SP | `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py` |
| 2026-07-06 | `fd2163b9f` | `hg-full-base..main` | 通用实现调整 | wan: use full VAE path for I2V and TI2V | `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py` |
| 2026-07-06 | `cbb50e347` | `hg-full-base..main` | 模型支持/运行时入口 | profiler: add profile start step parameter | `python/sglang/multimodal_gen/configs/sample/sampling_params.py` |
| 2026-07-06 | `9a3c7dbb4` | `hg-full-base..main` | 性能/后端优化 | rocm: allow flash attention backend selection | `python/sglang/multimodal_gen/runtime/platforms/rocm.py` |
| 2026-07-06 | `fa6b75971` | `hg-full-base..main` | 性能/后端优化 | [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py` |
| 2026-07-06 | `bc13c0a98` | `hg-full-base..main` | 缺陷修复 | [sgl-diffusion] Fix Wan T2V VAE decode path | `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py` |
| 2026-07-06 | `a1ed918ae` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C09 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-06 | `23cbd00e3` | `hg-full-base..main` | 缺陷修复 | [bugfix]: 解决hy3非mtp下的精度问题 | `python/sglang/srt/disaggregation/prefill.py` |
| 2026-07-06 | `ec48fa780` | `hg-full-base..main` | 缺陷修复 | [bugfix]: 解决hy3开mtp下的精度问题. | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` 等 4 个文件 |
| 2026-07-06 | `cf59f4695` | `hg-full-base..main` | 缺陷修复 | [bugfix]: avoid HYV3 PD KV compact remap | `python/sglang/srt/disaggregation/common/conn.py` |
| 2026-07-07 | `4d198708c` | `hg-full-base..main` | 性能/后端优化 | 解决sp下对padding的处理 | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-07-07 | `0507e6090` | `hg-full-base..main` | 缺陷修复 | fix: avoid amdsmi runtime logs on HCU | `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` |
| 2026-07-07 | `3f920d4e0` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-07 | `9bde26e7c` | `hg-full-base..main` | 通用实现调整 | 解耦vllm rms_norm | `python/sglang/srt/layers/layernorm.py` |
| 2026-07-07 | `d5f4d1c14` | `hg-full-base..main` | 性能/后端优化 | fix: skip expert distribution recording during CUDA graph capture | `python/sglang/srt/eplb/expert_distribution.py` |
| 2026-07-07 | `9188d711e` | `hg-full-base..main` | 测试/文档/基准 | ci: rename HCU runtime text check script | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/check_no_amd_runtime_text.py` |
| 2026-07-07 | `ef36df96f` | `hg-full-base..main` | 模型支持/运行时入口 | chore: add header for DCU runtime text checker | `scripts/ci/dcu/check_no_amd_runtime_text.py` |
| 2026-07-07 | `fe4e1fea3` | `hg-full-base..main` | 测试/文档/基准 | docs: sync LMSYS SGLang blog cards | `docs_new/index.mdx` |
| 2026-07-08 | `bfaf180d1` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C10 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `5d2c6854a` | `hg-full-base..main` | 性能/后端优化 | 0.5.12 MHA、GQA类hicache适配 | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` 等 10 个文件 |
| 2026-07-08 | `b6db54a9a` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C11~C13 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `1cea713a7` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record C14-C16 validation block | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `b452d6bd6` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record C14-C16 functional validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `01a6f1b94` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C14~C16 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `cee45bc55` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record C17-C19 validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `3e254b041` | `hg-full-base..main` | 通用实现调整 | style(distributed): apply pre-commit formatting to parallel_state.py | `python/sglang/srt/distributed/parallel_state.py` |
| 2026-07-09 | `4b0fcbd07` | `hg-full-base..main` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C17~C19 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `8b4a7bdeb` | `hg-full-base..main` | 测试/文档/基准 | ci: refine HCU runtime text check message | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `fda6d44a4` | `hg-full-base..main` | 测试/文档/基准 | ci: simplify HCU runtime text check failure message | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `d7af9508d` | `hg-full-base..main` | 调度/缓存/PD | style: apply CI hook formatting | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py` |
| 2026-07-09 | `616ba7b6d` | `hg-full-base..main` | 测试/文档/基准 | ci: reduce HCU runtime text check duplicate output | `scripts/ci/dcu/check_hcu_runtime_text.py` |
| 2026-07-09 | `d445921fe` | `hg-full-base..main` | 性能/后端优化 | 新增对RadixAttention层的判断 | `python/sglang/srt/layers/quantization/w8a8_int8.py` |
| 2026-07-09 | `dccf1782b` | `hg-full-base..main` | 测试/文档/基准 | ci: disable HCU runtime text check job | `.github/workflows/quality-gate.yml` |
| 2026-07-09 | `b38f25513` | `hg-full-base..main` | 性能/后端优化 | ci: add manual HCU nightly workflow controls | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 17 个文件 |
| 2026-07-11 | `390ad18e7` | `hg-full-base..main` | 性能/后端优化 | ci: 修复 packed KV 测试注册导致的 DCU CI 收集失败 (#87) | `benchmark/kernels/pack_paged_kv_to_varlen/bench_pack_paged_kv_to_varlen.py`, `benchmark/kernels/pack_paged_kv_to_varlen/pack_paged_kv_to_varlen_benchmark_results.md`, `test/registered/attention/bench_pack_paged_kv_to_varlen.py` 等 5 个文件 |
| 2026-07-11 | `0395a2bd2` | `hg-full-base..main` | 性能/后端优化 | fix: use lightop int8 deepep moe on dcu | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-07-13 | `e3fee4310` | `hg-full-base..main` | 模型支持/运行时入口 | ci: sync HCU workflows and scripts with current main | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 33 个文件 |
| 2026-07-13 | `de7170db0` | `hg-full-base..main` | 性能/后端优化 | kernel: migrate DCU ops and wrappers to HCU | `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h` 等 5 个文件 |
| 2026-07-13 | `9353ecb96` | `hg-full-base..main` | 测试/文档/基准 | docs: complete HCU naming migration | `NOTICE`, `README.md`, `README_DCU.md` 等 7 个文件 |
| 2026-07-13 | `1123fc038` | `hg-full-base..main` | 测试/文档/基准 | ci: enforce HCU rename safety checks | `scripts/ci/hcu/hcu_rename_allowlist.txt`, `scripts/ci/hcu/test_verify_hcu_rename.py`, `scripts/ci/hcu/verify_hcu_registration.py` 等 4 个文件 |
| 2026-07-13 | `cba9e72cc` | `hg-full-base..main` | 性能/后端优化 | [BugFix] skip some uncompatibal env setup in hip for DCU | `python/sglang/srt/server_args.py` |
| 2026-07-13 | `48489724d` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260623 catch-up runtime status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `40c658e8a` | `hg-full-base..main` | 测试/文档/基准 | ci: harden HCU runtime text checker | `.github/workflows/quality-gate.yml`, `scripts/ci/dcu/check_hcu_runtime_text.py`, `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` |
| 2026-07-13 | `bd60c0223` | `hg-full-base..main` | 通用实现调整 | Enhance quality gate workflow with new checks and branches | `.github/workflows/quality-gate.yml` |
| 2026-07-13 | `1c70e76d5` | `hg-full-base..main` | 性能/后端优化 | test: use verified local HCU model paths | `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`, `test/registered/hcu/lora/bw1100/test_qwen3_lora_server_hcu.py`, `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_instruct_hcu.py` 等 8 个文件 |
| 2026-07-13 | `8c797abd6` | `hg-full-base..main` | 测试/文档/基准 | Record 20260629 DCU runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `427726d60` | `hg-full-base..main` | 缺陷修复 | fix: complete HCU runtime text cleanup | `python/sglang/multimodal_gen/runtime/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` 等 6 个文件 |
| 2026-07-13 | `24bcdba3b` | `hg-full-base..main` | 性能/后端优化 | feat: support AITER W4A16 MOE_C prefill | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-07-13 | `bf59e99fd` | `hg-full-base..main` | 测试/文档/基准 | ci: harden HCU runtime text quality gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py` |
| 2026-07-13 | `d8ed552da` | `hg-full-base..main` | 模型支持/运行时入口 | docs(dcu): add 20260629 conflict review | `docs/internal/dcu-main-catchup-20260629-conflict-review.md` |
| 2026-07-13 | `c078943aa` | `hg-full-base..main` | 性能/后端优化 | chore: fix fused_moe lint issues | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-07-13 | `516a35c40` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260703 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `2981595c7` | `hg-full-base..main` | 性能/后端优化 | [FIX] 修复走非dcu_fa下的报错 | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-07-14 | `d53953dbe` | `hg-full-base..main` | 测试/文档/基准 | ci: clean up HCU validation checks | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/tests/test_check_hcu_runtime_text.py` |
| 2026-07-14 | `b9ca7c2ad` | `hg-full-base..main` | 通用实现调整 | Refine copyright/license warning messages | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `e3aa204a0` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): require catch-up conflict reviews | `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-14 | `412d0ef9f` | `hg-full-base..main` | 模型支持/运行时入口 | docs(dcu): add 20260709 conflict review | `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `c0e8edd74` | `hg-full-base..main` | 性能/后端优化 | fix(dcu): initialize DeepEP dispatch dtype state | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-07-14 | `f1c5eda31` | `hg-full-base..main` | 测试/文档/基准 | ci: require HCU runtime text check | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `48c3c0997` | `hg-full-base..main` | 测试/文档/基准 | ci: run HCU text check in Python 3.10 container | `.github/workflows/quality-gate.yml` |
| 2026-07-14 | `9d7fbb017` | `hg-full-base..main` | 模型支持/运行时入口 | docs: add 20260710 conflict review | `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `24894692e` | `hg-full-base..main` | 缺陷修复 | fix: use runtime attention TP size in model warmup | `python/sglang/srt/model_executor/model_runner.py` |
| 2026-07-14 | `6630db3cf` | `hg-full-base..main` | 测试/文档/基准 | docs: record 20260710 pure-TP validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `3d77308ea` | `hg-full-base..main` | 测试/文档/基准 | docs: mark 20260710 catch-up validated | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `3e335fce8` | `hg-full-base..main` | 测试/文档/基准 | docs: correct 20260710 endpoint subject | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `1109d462d` | `hg-full-base..main` | 调度/缓存/PD | [Feature] Support PD different-TP transfer for hybrid SWA/NSA and unequal K/V item lens. | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-07-15 | `baa08af59` | `hg-full-base..main` | 模型支持/运行时入口 | docs(dcu): add 20260712 conflict review | `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `44f81e8f7` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260712 runtime gate status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `0b30b7c9d` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260712 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `324181561` | `hg-full-base..main` | 模型支持/运行时入口 | docs(dcu): add 20260713 conflict review | `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `20633db57` | `hg-full-base..main` | 模型支持/运行时入口 | docs(dcu): add 20260714 conflict review | `docs/internal/dcu-main-catchup-20260714-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `f67cdf69b` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260714 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `49a10aec8` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): record 20260714 owner validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-16 | `dc1323ba4` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): finalize v0.5.12_dev forward-port | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-16 | `339dfe433` | `hg-full-base..main` | 测试/文档/基准 | docs(dcu): define v0.5.15.post1 release workflow | `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md` |
| 2026-07-16 | `e5a2dd041` | `hg-full-base..main` | 缺陷修复 | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-07-16 | `d28069157` | `hg-full-base..main` | 缺陷修复 | [bugfix]适配新的causal_conv1d接口 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-07-16 | `09d7a1d4c` | `hg-full-base..main` | 性能/后端优化 | support fabric aiter custom allreduce | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/model_runner.py` 等 5 个文件 |
| 2026-07-20 | `fe9f24924` | `hg-full-base..main` | 缺陷修复 | fix: prevent PD Decode DP hang under enable-dp-attention | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 5 个文件 |
| 2026-07-20 | `079275b81` | `hg-full-base..main` | 模型支持/运行时入口 | ci: add local sensitive diff text gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `358a33714` | `hg-full-base..main` | 缺陷修复 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-07-20 | `0c44c350b` | `hg-full-base..main` | 通用实现调整 | feat: enable dynamic batching for LTX-2 T2V | `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/sample/ltx_2.py` |
| 2026-07-20 | `86575d776` | `hg-full-base..main` | 缺陷修复 | fix: support tensor-parallel transformer loading | `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/server_args.py` |
| 2026-07-20 | `6182c3e35` | `hg-full-base..main` | 缺陷修复 | fix: handle non-contiguous LTX attention outputs | `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` |
| 2026-07-20 | `81e3561ae` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` |
| 2026-07-20 | `e47445d2f` | `hg-full-base..main` | 调度/缓存/PD | chore: clean leftover patch labels in PD Decode DP sync | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 5 个文件 |
| 2026-07-20 | `811aa027d` | `hg-full-base..main` | 测试/文档/基准 | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `5ac1f2418` | `hg-full-base..main` | 模型支持/运行时入口 | Add GitHub Actions workflow for quality gate | `.github/workflows/pr-quality-gate.yml` |
| 2026-07-20 | `5543eb3df` | `hg-full-base..main` | 调度/缓存/PD | Rename quality-gate workflow and update triggers | `.github/workflows/quality-gate.yml` |
| 2026-07-20 | `e19d341ab` | `hg-full-base..main` | 调度/缓存/PD | Refactor quality gate workflow and update triggers | `.github/workflows/quality-gate.yml` |
| 2026-07-20 | `15a656ea6` | `hg-full-base..main` | 测试/文档/基准 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` |
| 2026-07-21 | `14da9b10e` | `hg-full-base..main` | 调度/缓存/PD | Update workflow reference in quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-07-21 | `e7ab05411` | `hg-full-base..main` | 通用实现调整 | Delete .github/workflows/pr-quality-gate.yml | `.github/workflows/pr-quality-gate.yml` |
| 2026-07-21 | `c1f3f08c8` | `hg-full-base..main` | 调度/缓存/PD | Update workflow reference to a new commit | `.github/workflows/quality-gate.yml` |
| 2026-07-21 | `9864c8451` | `hg-full-base..main` | 测试/文档/基准 | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-21 | `ac56ca009` | `hg-full-base..main` | 测试/文档/基准 | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` |
| 2026-07-21 | `7b6a9dd89` | `hg-full-base..main` | 性能/后端优化 | 修复DeepseekV4精度问题 | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-22 | `9fc04a7a2` | `hg-full-base..main` | 性能/后端优化 | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-07-22 | `1c40e365c` | `hg-full-base..main` | 调度/缓存/PD | support mla lightop | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-22 | `5673a3972` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): finalize nightly pre-merge safeguards | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py` 等 6 个文件 |
| 2026-07-22 | `7941e0419` | `hg-full-base..main` | 缺陷修复 | fix: enable HiCache layout_dcu for hybrid Mamba and EAGLE draft | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` |
| 2026-07-22 | `f391712f7` | `hg-full-base..main` | 缺陷修复 | fix(hcu): use HCU guard for MLA KV cache storage | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-22 | `0b46ed36d` | `hg-full-base..main` | 性能/后端优化 | fix: apply bias after HCU DeepGEMM FP8 linear | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-07-22 | `b1606885e` | `hg-full-base..main` | 缺陷修复 | Fix help text for custom all-reduce backend | `python/sglang/srt/server_args.py` |
| 2026-07-22 | `421a13a80` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): enable accuracy notification on default branch | `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-22 | `8b38b9a25` | `hg-full-base..main` | 调度/缓存/PD | Update comment for all_gather usage in scheduler | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` |
| 2026-07-23 | `83d2a2b4b` | `hg-full-base..main` | 缺陷修复 | fix(hcu): rename stale DCU HiCache identifiers | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` 等 4 个文件 |
| 2026-07-23 | `e338cca15` | `hg-full-base..main` | 缺陷修复 | ci(hcu): improve accuracy card and fix VLM model path | `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-23 | `c3755b4d4` | `hg-full-base..main` | 性能/后端优化 | fix: make DP local control broadcast opt-in via env | `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py` 等 4 个文件 |
| 2026-07-24 | `64d1765b4` | `hg-full-base..main` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-24 | `6c1786bc4` | `hg-full-base..main` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-24 | `ca9b264a2` | `hg-full-base..main` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-24 | `7482123c3` | `hg-full-base..main` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-24 | `f76d2cea3` | `hg-full-base..main` | 通用实现调整 | Delete .github/workflows/quality-baseline-scan.yml | `.github/workflows/quality-baseline-scan.yml` |
| 2026-07-24 | `eb6a34093` | `hg-full-base..main` | 调度/缓存/PD | Update workflow reference to latest commit | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `9a8b1bd08` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow reference to new commit | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `2c21b95e6` | `hg-full-base..main` | 缺陷修复 | fix(ci): align Feishu accuracy table | `.github/workflows/hcu-feishu-notify-preview.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `6ac12c2e5` | `hg-full-base..main` | 测试/文档/基准 | ci: decouple Feishu preview from HCU runners | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-24 | `65b7c4268` | `hg-full-base..main` | 测试/文档/基准 | ci: use shared runner for Feishu preview | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-24 | `4af810205` | `hg-full-base..main` | 缺陷修复 | fix(ci): use card v2 metadata component | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `9e13c77ce` | `hg-full-base..main` | 缺陷修复 | fix(ci): use card v2 link button | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-24 | `88d4501a3` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow reference | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `a3efe5e53` | `hg-full-base..main` | 性能/后端优化 | [bugfix]:修复lightop_per_token_quant_fp8调用前tensor准备. | `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/mem_cache/allocator.py` |
| 2026-07-27 | `afac89e0e` | `hg-full-base..main` | 性能/后端优化 | feat(hcu): add KME W8A8 hipBLASLt path via METHODS=3 | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-07-27 | `87e383180` | `hg-full-base..main` | 性能/后端优化 | fix: 移除旧的lmslim导入方式. | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-07-27 | `163a92c14` | `hg-full-base..main` | 缺陷修复 | fix(hcu):修改lightop的算子接口. | `python/sglang/srt/layers/activation.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-27 | `93c56ce71` | `hg-full-base..main` | 通用实现调整 | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` |
| 2026-07-27 | `0710e82a0` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` |
| 2026-07-28 | `8f848be4e` | `hg-full-base..main` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-07-28 | `77939d9a5` | `hg-full-base..main` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-07-28 | `997e64560` | `hg-full-base..main` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-07-28 | `9a4f82911` | `hg-full-base..main` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-28 | `0305c5a3b` | `hg-full-base..main` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-07-28 | `cd4802bba` | `hg-full-base..main` | 性能/后端优化 | fix lint | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-07-28 | `d0c472989` | `hg-full-base..main` | 调度/缓存/PD | ci: add HCU PD disaggregation smoke tests | `test/registered/hcu/disaggregation/pd_hcu_utils.py`, `test/registered/hcu/disaggregation/test_pd_basic_hcu.py`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py` 等 6 个文件 |
| 2026-07-28 | `7b89bf661` | `hg-full-base..main` | 性能/后端优化 | fix: propagate return_hidden_states_before_norm flag for mHC target-verify | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-07-28 | `fc59c96c5` | `hg-full-base..main` | 缺陷修复 | fix lint: format line breaks and remove trailing whitespace | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-07-28 | `035ca766f` | `hg-full-base..main` | 缺陷修复 | fix(cache): forward Mamba indices in NSA offload | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-29 | `bfa4011ad` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): share wheel staging across runners | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 |
| 2026-07-29 | `92e95e3f5` | `hg-full-base..main` | 性能/后端优化 | perf(mamba): flatten fused state scatter launch grid | `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py` |
| 2026-07-29 | `049f5e15e` | `hg-full-base..main` | 性能/后端优化 | [bugfix] 透传apply_routed_scaling_factor_on_output，防止moe_sum多乘routed_scaling_factor | `python/sglang/srt/layers/moe/topk.py` |
| 2026-07-29 | `6e7a53e86` | `hg-full-base..main` | 性能/后端优化 | fix(hcu): select hipblaslt w8a8 layout by gfx arch | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-07-29 | `4e5a95fcb` | `hg-full-base..main` | 缺陷修复 | fix(pd): transfer MTP NSA topk seed metadata over Mooncake | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py` 等 9 个文件 |
| 2026-07-29 | `58d475775` | `hg-full-base..main` | 缺陷修复 | fix(hcu): allow single-node context parallel tp16 | `python/sglang/srt/server_args.py` |
| 2026-07-29 | `3b4327cd7` | `hg-full-base..main` | 性能/后端优化 | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` |
| 2026-07-29 | `e18e6b94b` | `hg-full-base..main` | 测试/文档/基准 | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-29 | `6a031254f` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): isolate nightly services and shared results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-07-29 | `be81ab419` | `hg-full-base..main` | 缺陷修复 | fix(dp): demote DP Decode StepInfo log to debug | `python/sglang/srt/managers/scheduler_dp_attn_mixin.py` |
| 2026-07-29 | `b2f0b830c` | `hg-full-base..main` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 39 个文件 |
| 2026-07-29 | `111fea82f` | `hg-full-base..main` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 36 个文件 |
| 2026-07-29 | `84bfd45c4` | `hg-full-base..main` | 缺陷修复 | 修复hicache+pp并行 stage不一致问题 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py` 等 4 个文件 |
| 2026-07-30 | `b8389e5c5` | `hg-full-base..main` | 调度/缓存/PD | test(hcu): register PD helper for nightly collection | `test/registered/hcu/disaggregation/pd_hcu_utils.py` |
| 2026-07-30 | `6ea38ee52` | `hg-full-base..main` | 调度/缓存/PD | style(hcu): format PD helper registration | `test/registered/hcu/disaggregation/pd_hcu_utils.py` |
| 2026-07-30 | `489170e5c` | `hg-full-base..main` | 性能/后端优化 | [FIX] 修复moe_w8a8重排函数删除问题 | `python/sglang/srt/layers/moe/moe_runner/lightop.py` |
| 2026-07-30 | `17cf690af` | `hg-full-base..main` | 性能/后端优化 | style: fix HCU lint checks | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 4 个文件 |
| 2026-07-31 | `02968a96d` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 |
| 2026-07-31 | `39d691220` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-07-31 | `83f43b3f4` | `hg-full-base..main` | 性能/后端优化 | [CI] Fix some CI errors | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-07-31 | `dc015a0bc` | `hg-full-base..main` | 缺陷修复 | [PD] When PP is greater than 1, fix the request rollback when the KV cache is exhausted | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 11 个文件 |
| 2026-07-31 | `497c35457` | `hg-full-base..main` | 缺陷修复 | fix(scheduler): abort too-large requests instead of dead-looping | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` |
| 2026-07-31 | `b48994210` | `hg-full-base..main` | 测试/文档/基准 | ci: install PyYAML for slash command handler (#156) | `.github/workflows/slash-command-handler.yml` |
| 2026-07-31 | `f556d3896` | `hg-full-base..main` | 性能/后端优化 | [FIX] 修复lmslim和lightop接口冲突问题 (#154) | `python/sglang/srt/layers/quantization/slimquant_w4a8.py` |
| 2026-07-31 | `0ff7a014f` | `hg-full-base..main` | 模型支持/运行时入口 | ci(hcu): support resending Feishu accuracy results | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-31 | `9c69436ee` | `hg-full-base..main` | 缺陷修复 | fix(hcu): remove resend tool dependencies | `.github/workflows/hcu-feishu-notify-preview.yml` |
| 2026-07-31 | `85dcec947` | `hg-full-base..main` | 缺陷修复 | fix(hcu): support Python 3.8 in Feishu notifier | `scripts/ci/hcu/hcu_ci_notify_feishu.py` |
| 2026-08-03 | `67ecec8dd` | `hg-full-base..main` | 缺陷修复 | fix(hcu): scope Feishu status to accuracy results | `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-08-03 | `ff7f44b8e` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `286612da4` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `4d3aaf6af` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow for versioning and concurrency | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `3358846e5` | `hg-full-base..main` | 调度/缓存/PD | Update quality-gate.yml | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `e6c410259` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `de696eab9` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `015f6d49a` | `hg-full-base..main` | 性能/后端优化 | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-08-03 | `143ee9287` | `hg-full-base..main` | 性能/后端优化 | refactor(hcu): route KME W8A8 hipBLASLt through lightop | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-08-04 | `cd60b7433` | `hg-full-base..main` | 调度/缓存/PD | 修改hicache+pp并行 stage不一致问题commit提交格式 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` |
| 2026-08-04 | `083d1d8b9` | `hg-full-base..main` | 性能/后端优化 | fix(hcu): restore DeepGEMM PD helper and current cache API | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-08-04 | `e8298ba90` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore DP decode protocol constants | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-04 | `43d8d9ac1` | `hg-full-base..main` | 性能/后端优化 | style(hcu): fix lint for KME W8A8 lightop path | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-08-04 | `8160ebe53` | `hg-full-base..main` | 缺陷修复 | fix(hcu): retain PD decode adapter callbacks | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-05 | `2a342cdf1` | `hg-full-base..main` | 缺陷修复 | fix fp8 bug of triton | `python/sglang/srt/layers/attention/triton_ops/decode_attention.py` |
| 2026-08-05 | `71de6dd93` | `hg-full-base..main` | 缺陷修复 | fix(ci): align HCU gateway wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-08-05 | `2fb37eaac` | `hg-full-base..main` | 缺陷修复 | fix(ci): align HCU Python wheel paths | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-05 | `44bb481cf` | `hg-full-base..main` | 性能/后端优化 | fix(eplb): apply expert ID remapping for HCU fused TopK | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-05 | `dabae6b13` | `hg-full-base..main` | 缺陷修复 | fix(ci): use PR files API for HCU wheel detection | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-08-06 | `f1c6f5631` | `hg-full-base..main` | 性能/后端优化 | fix(hcu): drop leftover source hunks that renaming and partial takes left behind | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-06 | `8e2aba4bf` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply isort/black to forward-port diff | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 5 个文件 |
| 2026-08-06 | `f17440f19` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore original license headers dropped by the forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py` |
| 2026-08-06 | `b0f2bb3a8` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore network_mode matrix keys dropped by the forward-port | `.github/workflows/nightly-test-hcu.yml` |
| 2026-08-07 | `154a88c7b` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply isort/black to the lmslim->lightop migration | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-08-07 | `b59995e42` | `hg-full-base..main` | 缺陷修复 | fix(hcu): point PD smoke tests at a declared HCU suite | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-07 | `92ce544fa` | `hg-full-base..main` | 测试/文档/基准 | ci: align v0.5.15 workflow triggers | `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml` 等 7 个文件 |
| 2026-08-07 | `132b630bc` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): harden server lifecycle and model mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` 等 5 个文件 |
| 2026-08-07 | `4c7a264e5` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): align model assets and selected-ref kernel | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-08-07 | `1a5ce1750` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): publish reasoning results to shared storage | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`, `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py` |
| 2026-08-07 | `50736ebe7` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): keep migration changes scoped | `README_HCU.md` |
| 2026-08-07 | `dc5cd7089` | `hg-full-base..main` | 测试/文档/基准 | ci: finalize v0.5.15 workflow policy | `.github/workflows/ci-auto-bisect.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/slash-command-handler.yml` |
| 2026-08-07 | `ecf4756ce` | `hg-full-base..main` | 测试/文档/基准 | test(hcu): isolate server guard unit test | `scripts/ci/hcu/test_hcu_server_guard.py` |
| 2026-08-07 | `76ced479e` | `hg-full-base..main` | 性能/后端优化 | test(hcu): use v0.5.15 FP8 kernel path | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` |
| 2026-08-07 | `3fbc8ae9e` | `hg-full-base..main` | 性能/后端优化 | test(hcu): align numerical references with v0.5.15 | `test/registered/hcu/kernels/test_attention_reference_hcu.py`, `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py` |
| 2026-08-07 | `3de1323a9` | `hg-full-base..main` | 调度/缓存/PD | ci(hcu): normalize rebased PD suite names | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-10 | `e3a9d595c` | `hg-full-base..main` | 缺陷修复 | [HCU][DSpark] Fix sampling parameter updates after graph capture | `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` |
| 2026-08-10 | `4a6fbed98` | `hg-full-base..main` | 性能/后端优化 | [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config | `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-10 | `5fd89c728` | `hg-full-base..main` | 缺陷修复 | [BugFix] fix the inference tensor graph replay issues in MTP mode | `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-08-10 | `b36730b41` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply pre-commit fixes to the mHC EAGLE changes | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py` |
| 2026-08-11 | `ccbb65acb` | `hg-full-base..main` | 性能/后端优化 | [HCU][DSpark] Fix DP EP MoE fallback routing | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-12 | `2083c069f` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply pre-commit fixes to the EP MoE fallback change | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-12 | `fb7f11956` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 |
| 2026-08-13 | `54e3ed50f` | `hg-full-base..main` | 缺陷修复 | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` |
| 2026-08-13 | `18e167b73` | `hg-full-base..main` | 性能/后端优化 | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-13 | `5e2ba659e` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-14 | `fa309a1e1` | `hg-full-base..main` | 性能/后端优化 | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-08-17 | `9bbf3799d` | `hg-full-base..main` | 模型支持/运行时入口 | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` |
| 2026-08-18 | `b0dc28040` | `hg-full-base..main` | 性能/后端优化 | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` 等 9 个文件 |
| 2026-08-20 | `62a07586d` | `hg-full-base..main` | 性能/后端优化 | [feat] 适配HCU FA3 | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 5 个文件 |
| 2026-08-20 | `fb7369fec` | `hg-full-base..main` | 缺陷修复 | [bugfix]删除无关文件 | `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942` |
| 2026-08-20 | `b628d29e1` | `hg-full-base..main` | 测试/文档/基准 | [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-20 | `11d08002b` | `hg-full-base..main` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 4 个文件 |
| 2026-08-20 | `f6b66222a` | `hg-full-base..main` | 通用实现调整 | revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0 | `.github/workflows/release-pr-hcu.yml` |
| 2026-08-20 | `72d1d2a73` | `hg-full-base..main` | 性能/后端优化 | [fix]solved other CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `27ce43c71` | `hg-full-base..main` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `37c5b30bb` | `hg-full-base..main` | 缺陷修复 | fix: extract full DTK version for three-part versions | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` 等 4 个文件 |
| 2026-08-21 | `a96aed11f` | `hg-full-base..main` | 性能/后端优化 | [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-08-21 | `d42ecf6fe` | `hg-full-base..main` | 缺陷修复 | Fix HCU detection and sanitized topology diagnostics | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-24 | `261b8627f` | `hg-full-base..main` | 缺陷修复 | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` |
| 2026-08-24 | `fd4157047` | `hg-full-base..main` | 通用实现调整 | Refine HCU platform diagnostics and CLI help | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py` |
| 2026-08-25 | `c40703e6b` | `hg-full-base..main` | 缺陷修复 | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` 等 5 个文件 |
| 2026-08-25 | `d1adf7b50` | `hg-full-base..main` | 测试/文档/基准 | [feature] manual compile ci | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-25 | `59213c7e4` | `hg-full-base..main` | 性能/后端优化 | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-25 | `94e9fa4b1` | `hg-full-base..main` | 测试/文档/基准 | ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-25 | `69c73a178` | `hg-full-base..main` | 模型支持/运行时入口 | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `f2fc4e166` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-08-25 | `3e6aaf09d` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `6a4a61efb` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-26 | `990a1a798` | `hg-full-base..main` | 测试/文档/基准 | ci: disable scheduled gateway nightly release | `.github/workflows/nightly-release-gateway.yml` |
| 2026-08-26 | `8dd5daf2f` | `hg-full-base..main` | 测试/文档/基准 | Refine HCU and AMD CLI help text | `python/sglang/srt/server_args.py`, `test/run_suite.py` |
| 2026-08-26 | `c94c3ca2c` | `hg-full-base..main` | 缺陷修复 | fix: gateway wheel is at workspace root target/wheels | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-26 | `f6d701c52` | `hg-full-base..main` | 缺陷修复 | Fix stale HCU Stage B test paths | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-26 | `a2de3b8cf` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-27 | `2866df994` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-27 | `7609d9af6` | `hg-full-base..main` | 模型支持/运行时入口 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` |
| 2026-08-27 | `6b468d012` | `hg-full-base..main` | 性能/后端优化 | [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 |
| 2026-08-28 | `68dcd498a` | `hg-full-base..main` | 测试/文档/基准 | [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-28 | `bc990ebd5` | `hg-full-base..main` | 测试/文档/基准 | [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-31 | `3ca61517d` | `hg-full-base..main` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-08-31 | `e864c3028` | `hg-full-base..main` | 测试/文档/基准 | ci: enable HCU PR tests for release branches (#272) | `.github/workflows/pr-test-hcu.yml` |
| 2026-09-01 | `8fa7122b3` | `hg-full-base..main` | 测试/文档/基准 | [FEATURE]构建镜像之后触发模型测试 (#277) | `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml` |
| 2026-09-02 | `9d261478d` | `hg-full-base..main` | 性能/后端优化 | [CI] Update HCU model asset paths on main (#285) | `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh` 等 10 个文件 |
| 2026-09-02 | `6fe7ce909` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): restore run suite file filters (#290) | `test/run_suite.py` |
| 2026-09-03 | `2828bde71` | `hg-full-base..main` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#299) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-04 | `0457572a1` | `hg-full-base..main` | 测试/文档/基准 | [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308) | `.github/workflows/nightly-test-image-hcu.yml` |
| 2026-09-08 | `0af71f61b` | `hg-full-base..main` | 缺陷修复 | fix(ci): update HCU evaluation dependencies and asset paths (#325) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-09-14 | `b5108cc7f` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): use v0.5.18 image and restore eval dependencies (#347) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` 等 4 个文件 |
| 2026-09-14 | `516261baf` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): register sampling test and adjust MMLU threshold (#359) | `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `575cf4797` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): restore source mode for test-only PRs (#364) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-15 | `7c8272a3a` | `hg-full-base..main` | 缺陷修复 | [BUGFIX]更新AICC安装方式 (#367) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-15 | `ae14a99e5` | `hg-full-base..main` | 缺陷修复 | fix(ci): fix HCU wheel build target routing (#372) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `5c03a8e22` | `hg-full-base..main` | 测试/文档/基准 | [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-16 | `adc1d69b2` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): align main wheel builds with 0.5.18 runtime (#379) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 6 个文件 |
| 2026-09-21 | `ae5c33991` | `hg-full-base..main` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-21 | `cb932f5fb` | `hg-full-base..main` | 测试/文档/基准 | feat(ci) compaity sgl-kernal main to v0.5.12 (#421) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-21 | `a981685e7` | `hg-full-base..main` | 缺陷修复 | fix release-pr-hcu.yml build sglang (#423) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-22 | `b5ca753bc` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): run nightly against v0.5.18 and report its results (#432) | `.github/workflows/nightly-test-hcu.yml` |
| 2026-09-23 | `2871c8fdd` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-23 | `7be1324cf` | `hg-full-base..main` | 测试/文档/基准 | ci: report sglang nightly packages to DashHub (#424) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-24 | `665b27d1f` | `hg-full-base..main` | 缺陷修复 | feat(ci) fix main build whl failed (#449) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-28 | `5e8269d55` | `hg-full-base..main` | 缺陷修复 | [BUGFIX]镜像DTK版本号不对 (#447) | `.github/workflows/release-docker-hcu.yml` |
| 2026-09-30 | `e05f146be` | `hg-full-base..main` | 模型支持/运行时入口 | ci(hcu): migrate main workflows to organization runners (#463) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` 等 12 个文件 |
| 2026-10-09 | `fb46d17ad` | `hg-full-base..main` | 性能/后端优化 | add optest process (#481) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-09 | `f0ee2a505` | `hg-full-base..main` | 缺陷修复 | FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473) | `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py` |
| 2026-10-10 | `4205397cb` | `hg-full-base..main` | 模型支持/运行时入口 | add password-free download code (#499) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-10 | `3b0e4a073` | `hg-full-base..main` | 性能/后端优化 | [Fix] Bound crash diagnostics and fatal shutdown on main (#498) | `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` 等 6 个文件 |
| 2026-10-12 | `50b0d0051` | `hg-full-base..main` | 模型支持/运行时入口 | Delegate HCU model deployment smoke CI to external controller (#503) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-12 | `f9b972b37` | `hg-full-base..main` | 模型支持/运行时入口 | Use a clean checkout directory for the model smoke controller (#510) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `b6dd37e66` | `hg-full-base..main` | 测试/文档/基准 | Run cookbook smoke tests for all cases by default | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `e295faff5` | `hg-full-base..main` | 性能/后端优化 | update ci name&&add optest log (#515) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-14 | `78c700ee0` | `hg-full-base..main` | 模型支持/运行时入口 | Add image input to cookbook deployment smoke workflow (#530) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `cc3758967` | `hg-full-base..main` | 通用实现调整 | Pass DashHub credential to deployment smoke controller (#534) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `fc095e059` | `hg-full-base..main` | 缺陷修复 | fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533) | `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` 等 4 个文件 |
| 2026-10-16 | `87b9d5c85` | `hg-full-base..main` | 测试/文档/基准 | Run cookbook deployment checks after HCU image publishing (#548) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-19 | `f89209aa8` | `hg-full-base..main` | 模型支持/运行时入口 | ci: pass package server to Cookbook model tests (#556) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-20 | `a8543c813` | `hg-full-base..main` | 模型支持/运行时入口 | [CI] cookbook: Add BW1000 deployment smoke tests (#570) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-28 | `6dac3481c` | `hg-full-base..main` | 缺陷修复 | [Fix] ci: Preserve model cases in DashHub operator reporting (#604) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-28 | `098f31d69` | `hg-full-base..main` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-10-28 | `029b6e641` | `hg-full-base..main` | 模型支持/运行时入口 | [CI] model-ci: Pass history token for daily comparison report (#607) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-28 | `fd98647ed` | `hg-full-base..main` | 缺陷修复 | [Fix] ci: Restore previous DashHub operator reporting (#614) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-29 | `25aa13e98` | `hg-full-base..main` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml (#617) | `.github/workflows/pr-test-hcu.yml` |
| 2026-10-29 | `db479b030` | `hg-full-base..main` | 性能/后端优化 | [CI] optest: Report outcome to DashHub (#619) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-29 | `9fb319cc3` | `hg-full-base..main` | 性能/后端优化 | [CI] optest: Require every enabled operator result (#622) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-11-02 | `471ab8254` | `hg-full-base..main` | 模型支持/运行时入口 | Add one-time DashHub recovery for run 41338132822 (#633) | `.github/workflows/dashhub-recover-41338132822.yml` |
| 2026-11-02 | `594e1ae94` | `hg-full-base..main` | 测试/文档/基准 | [Chore] ci: Remove completed DashHub recovery workflow (#634) | `.github/workflows/dashhub-recover-41338132822.yml` |

### 逐 Commit 审计卡

- 时间线列出全部 477 个提交；审计卡只保留最近的 80 个。

#### Commit `fa309a1e1` - fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE

- 完整 hash: `fa309a1e19c40cd15a9f5cf6a14e8f0b701211f9`
- 时间/作者: 2026-08-14 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `9bbf3799d` - docs(hcu): add the 20260817 official backport validation report

- 完整 hash: `9bbf3799d827a26d6768d569fc652b9837a31425`
- 时间/作者: 2026-08-17 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/internal/backport-official-20260817-validation-report.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/backport-official-20260817-validation-report.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `b0dc28040` - Hcu/fix main kernel build path (#207)

- 完整 hash: `b0dc28040e611a27ea29979496c301395e3c10ed`
- 时间/作者: 2026-08-18 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`, `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`
  - tests: `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`; `test/registered/hcu/reranker/bw1100/test_qwen3_reranker_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `62a07586d` - [feat] 适配HCU FA3

- 完整 hash: `62a07586d98059ba83cf0b1a2e1d6496a8de2bed`
- 时间/作者: 2026-08-20 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`, `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `fb7369fec` - [bugfix]删除无关文件

- 完整 hash: `fb7369fec0d5fd3a6bbb45515c95fba0ffc4efbf`
- 时间/作者: 2026-08-20 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `b628d29e1` - [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本

- 完整 hash: `b628d29e1c2e33e291e647991eab213bc9c5dcc8`
- 时间/作者: 2026-08-20 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `11d08002b` - [fix]solved CI Test errors

- 完整 hash: `11d08002bfd60e96b4ff4d1210a69678a70de801`
- 时间/作者: 2026-08-20 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/kv_cache_dtype.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f6b66222a` - revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0

- 完整 hash: `f6b66222a00a63851345729b7acd8d9855c2e184`
- 时间/作者: 2026-08-20 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `72d1d2a73` - [fix]solved other CI Test errors

- 完整 hash: `72d1d2a73af94d8cdef717fd46cacf331665b32e`
- 时间/作者: 2026-08-20 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `27ce43c71` - [fix]solved CI Test errors

- 完整 hash: `27ce43c71d9194fd473370a19f354e755b5ade86`
- 时间/作者: 2026-08-20 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `37c5b30bb` - fix: extract full DTK version for three-part versions

- 完整 hash: `37c5b30bb9f24bbac284e5598a9219f71b6c06bf`
- 时间/作者: 2026-08-20 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-dcu.yml`; `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-dcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a96aed11f` - [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子

- 完整 hash: `a96aed11f05f65d18f5bd46446b4ca9b7ac82105`
- 时间/作者: 2026-08-21 / zhuwenbopro
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `d42ecf6fe` - Fix HCU detection and sanitized topology diagnostics

- 完整 hash: `d42ecf6fe9854d6127c167959fe7bec30439b73b`
- 时间/作者: 2026-08-21 / reverie-hub
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`; `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `261b8627f` - fix(hcu): restore 29 environ declarations the sync auto-merge dropped

- 完整 hash: `261b8627f107f553e26ce43b74d052c28a676bfd`
- 时间/作者: 2026-08-24 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/sync-official-main-20260824-summary.md`
  - other: `python/sglang/srt/environ.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `fd4157047` - Refine HCU platform diagnostics and CLI help

- 完整 hash: `fd415704795411fa8fcbc7d7571c41dcb3d1c431`
- 时间/作者: 2026-08-24 / reverie-hub
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c40703e6b` - fix(ci): clear the three Quality Gate blockers from the 20260824 sync

- 完整 hash: `c40703e6b494756f882f1e052d2d574350e5591a`
- 时间/作者: 2026-08-25 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/srt/server_args.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/nightly-test-npu.yml`
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `d1adf7b50` - [feature] manual compile ci

- 完整 hash: `d1adf7b503b20e64e07c38946a067ee90c428962`
- 时间/作者: 2026-08-25 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `59213c7e4` - Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED

- 完整 hash: `59213c7e48c978859b7086524aab5b0ccb500fc4`
- 时间/作者: 2026-08-25 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `94e9fa4b1` - ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload)

- 完整 hash: `94e9fa4b1d10f14c6120bab4f5416caf6e318cd9`
- 时间/作者: 2026-08-25 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `69c73a178` - ci(hcu): support fork pull requests

- 完整 hash: `69c73a1787bdd189d88ba7cb3240dc34c46663a7`
- 时间/作者: 2026-08-25 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f2fc4e166` - Update quality gate workflow to version 2.0.3

- 完整 hash: `f2fc4e166b64086a0ef22e99a96046bd5acf4cc1`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `hg-full-base..main`
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `3e6aaf09d` - ci(hcu): allow fork checkout in target workflows

- 完整 hash: `3e6aaf09d878c40268294082de2abf032911bf1a`
- 时间/作者: 2026-08-25 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/lint-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6a4a61efb` - ci(hcu): detect runner workspace ownership

- 完整 hash: `6a4a61efba7f1a2d75bfe132d6589a459a0f2c1c`
- 时间/作者: 2026-08-25 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `990a1a798` - ci: disable scheduled gateway nightly release

- 完整 hash: `990a1a798d40ccea97ef91c16a9d8cd8f25957e2`
- 时间/作者: 2026-08-26 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-release-gateway.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-release-gateway.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `8dd5daf2f` - Refine HCU and AMD CLI help text

- 完整 hash: `8dd5daf2fa5555ab13751b159703124fd493a437`
- 时间/作者: 2026-08-26 / reverie-hub
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/srt/server_args.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/run_suite.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c94c3ca2c` - fix: gateway wheel is at workspace root target/wheels

- 完整 hash: `c94c3ca2c8341c501b46a32c750e32dfe8ce4e06`
- 时间/作者: 2026-08-26 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f6d701c52` - Fix stale HCU Stage B test paths

- 完整 hash: `f6d701c520529490926e3c350682b7fe7ca6f9d0`
- 时间/作者: 2026-08-26 / reverie-hub
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a2de3b8cf` - ci(hcu): use bash for wheel build jobs

- 完整 hash: `a2de3b8cffc365e5f813d2ddd6c7226abe29db90`
- 时间/作者: 2026-08-26 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `2866df994` - ci(hcu): trust wheel build workspaces

- 完整 hash: `2866df9948b40e81405fcf5947ef74b8f744c9a3`
- 时间/作者: 2026-08-27 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `7609d9af6` - [feature]适配hcu发包

- 完整 hash: `7609d9af69ac40ed6730564cde4934d5b3e4a540`
- 时间/作者: 2026-08-27 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`; `python/pyproject_hcu.toml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6b468d012` - [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda

- 完整 hash: `6b468d012bcf693157cee193493842185165b93b`
- 时间/作者: 2026-08-27 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `68dcd498a` - [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致

- 完整 hash: `68dcd498aa7550a39e7f53b6588e19785efd5cae`
- 时间/作者: 2026-08-28 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `bc990ebd5` - [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复)

- 完整 hash: `bc990ebd52e0ae2500dc3c0ab4eeba187e84965b`
- 时间/作者: 2026-08-28 / zhangyh15
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `3ca61517d` - ci-remove-amd-status-from-pr-summaries

- 完整 hash: `3ca61517d037e82ba19c981dd66ddaf0245e85cd`
- 时间/作者: 2026-08-31 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-states.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-states.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e864c3028` - ci: enable HCU PR tests for release branches (#272)

- 完整 hash: `e864c302870000325162a5788883997cc850ade8`
- 时间/作者: 2026-08-31 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `8fa7122b3` - [FEATURE]构建镜像之后触发模型测试 (#277)

- 完整 hash: `8fa7122b3ace4a4de48372ee3c4c3346871281d7`
- 时间/作者: 2026-09-01 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
  - other: `docker/image-citest-conf-hcu.yaml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `9d261478d` - [CI] Update HCU model asset paths on main (#285)

- 完整 hash: `9d261478d6ace185f3e35a7211fc411b64d2057f`
- 时间/作者: 2026-09-02 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_exec.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/spec/test_ngram_speculative_decoding_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `6fe7ce909` - ci(hcu): restore run suite file filters (#290)

- 完整 hash: `6fe7ce9097c8e9f1b7dccefbe4834a7f928a78c2`
- 时间/作者: 2026-09-02 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `test/run_suite.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `2828bde71` - ci(hcu): align llguidance and model asset paths (#299)

- 完整 hash: `2828bde71da3f5f6314aa4022ae7e163dfc33ada`
- 时间/作者: 2026-09-03 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `0457572a1` - [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308)

- 完整 hash: `0457572a14edd55e05220726ff4a8af8b1931771`
- 时间/作者: 2026-09-04 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `0af71f61b` - fix(ci): update HCU evaluation dependencies and asset paths (#325)

- 完整 hash: `0af71f61b693c2bd2817a678e007660222db9bf3`
- 时间/作者: 2026-09-08 / tianly
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `b5108cc7f` - ci(hcu): use v0.5.18 image and restore eval dependencies (#347)

- 完整 hash: `b5108cc7fea82d75da174f8f6681a843d43c462b`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/utils/sgl_eval_ref.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/utils/sgl_eval_ref.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `516261baf` - ci(hcu): register sampling test and adjust MMLU threshold (#359)

- 完整 hash: `516261baf108e56bcb4a03dc7294a936e9656a2d`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `575cf4797` - ci(hcu): restore source mode for test-only PRs (#364)

- 完整 hash: `575cf47976761be9916048cfe2ca244b56d63fab`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `7c8272a3a` - [BUGFIX]更新AICC安装方式 (#367)

- 完整 hash: `7c8272a3a32d25391c8bc20e0c0678d3c9ac895d`
- 时间/作者: 2026-09-15 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `ae14a99e5` - fix(ci): fix HCU wheel build target routing (#372)

- 完整 hash: `ae14a99e502d0e5dbed8abf42e3b35eb8807c3c5`
- 时间/作者: 2026-09-15 / tianly
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `5c03a8e22` - [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376)

- 完整 hash: `5c03a8e22f8cfeef0f10cd909231862bd446cc30`
- 时间/作者: 2026-09-15 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `adc1d69b2` - ci(hcu): align main wheel builds with 0.5.18 runtime (#379)

- 完整 hash: `adc1d69b2a610fc000ca27e4b92c72e9c1b85044`
- 时间/作者: 2026-09-16 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/test_hcu_build_alignment.py`, `scripts/ci/hcu/test_hcu_wheel_version.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/test_hcu_build_alignment.py`; `scripts/ci/hcu/test_hcu_wheel_version.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `ae5c33991` - Update quality gate workflow to use stable version

- 完整 hash: `ae5c33991be7f0e277f71c4e853c10fc11cbe627`
- 时间/作者: 2026-09-21 / Lvjiajia
- 分支更新段: `hg-full-base..main`
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `cb932f5fb` - feat(ci) compaity sgl-kernal main to v0.5.12 (#421)

- 完整 hash: `cb932f5fbd904a577093a262c6a101834a1ef994`
- 时间/作者: 2026-09-21 / 463975089
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a981685e7` - fix release-pr-hcu.yml build sglang (#423)

- 完整 hash: `a981685e7f137a9e0629cbdcad2ad7bdd42017b9`
- 时间/作者: 2026-09-21 / 463975089
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `b5ca753bc` - ci(hcu): run nightly against v0.5.18 and report its results (#432)

- 完整 hash: `b5ca753bc8e054ce99b4c01b0369eb89c6870dbb`
- 时间/作者: 2026-09-22 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `2871c8fdd` - ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438)

- 完整 hash: `2871c8fdd9594de894546b144d253c3dd88fd900`
- 时间/作者: 2026-09-23 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `7be1324cf` - ci: report sglang nightly packages to DashHub (#424)

- 完整 hash: `7be1324cf827dafe9f09ec3f86ade353801b5e1e`
- 时间/作者: 2026-09-23 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `665b27d1f` - feat(ci) fix main build whl failed (#449)

- 完整 hash: `665b27d1fa35017a437b0aa0099a5f8aa33e5d9b`
- 时间/作者: 2026-09-24 / 463975089
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `5e8269d55` - [BUGFIX]镜像DTK版本号不对 (#447)

- 完整 hash: `5e8269d55a8cf4629cc39a3171169f4aa8b4d14b`
- 时间/作者: 2026-09-28 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e05f146be` - ci(hcu): migrate main workflows to organization runners (#463)

- 完整 hash: `e05f146bed9ca80c72a18a4946fd6f838d8e7774`
- 时间/作者: 2026-09-30 / dingxinlong
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/pr-states.yml` 等 12 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/pr-states.yml` 等 12 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fb46d17ad` - add optest process (#481)

- 完整 hash: `fb46d17ad9f633aa7fee521484262b0c26de560d`
- 时间/作者: 2026-10-09 / Lee156
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f0ee2a505` - FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473)

- 完整 hash: `f0ee2a5059c2d6a167bee3d996bca004276b3138`
- 时间/作者: 2026-10-09 / JackPeng
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_detokenizer_incremental.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `4205397cb` - add password-free download code (#499)

- 完整 hash: `4205397cbcf8c60852fadd7306cea32f2541a19d`
- 时间/作者: 2026-10-10 / Lee156
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `3b0e4a073` - [Fix] Bound crash diagnostics and fatal shutdown on main (#498)

- 完整 hash: `3b0e4a07393778001dcd518d2b11de225e1be8c8`
- 时间/作者: 2026-10-10 / 王启宇
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`, `test/registered/unit/utils/test_bounded_fatal_shutdown.py`, `test/registered/unit/utils/test_bounded_pyspy.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/docs/references/environment_variables.mdx`
  - other: `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-perf: `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`
  - tests: `test/registered/unit/utils/test_bounded_fatal_shutdown.py`; `test/registered/unit/utils/test_bounded_pyspy.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `50b0d0051` - Delegate HCU model deployment smoke CI to external controller (#503)

- 完整 hash: `50b0d005189ee23cf3046b86dc44986c5e6b9345`
- 时间/作者: 2026-10-12 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f9b972b37` - Use a clean checkout directory for the model smoke controller (#510)

- 完整 hash: `f9b972b372f8695154301e2d7cee24195a963250`
- 时间/作者: 2026-10-12 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `b6dd37e66` - Run cookbook smoke tests for all cases by default

- 完整 hash: `b6dd37e66ad4f820a75614c8b0e6f54ffa67c796`
- 时间/作者: 2026-10-12 / gcy
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e295faff5` - update ci name&&add optest log (#515)

- 完整 hash: `e295faff5dc889c97626f7bd25f6a8ca0a0f100c`
- 时间/作者: 2026-10-12 / Lee156
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `78c700ee0` - Add image input to cookbook deployment smoke workflow (#530)

- 完整 hash: `78c700ee0100f215268a3a802538881f281f29e2`
- 时间/作者: 2026-10-14 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `cc3758967` - Pass DashHub credential to deployment smoke controller (#534)

- 完整 hash: `cc3758967d74748204015a050182e5ad176c8a08`
- 时间/作者: 2026-10-15 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fc095e059` - fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533)

- 完整 hash: `fc095e059889d2fae91e86a5b3e5fa19eb8d7a34`
- 时间/作者: 2026-10-15 / chaoyujiang
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/benchmark/datasets/common.py`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
  - tests: `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `87b9d5c85` - Run cookbook deployment checks after HCU image publishing (#548)

- 完整 hash: `87b9d5c85eafab11fe18235718c1af37b348d784`
- 时间/作者: 2026-10-16 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f89209aa8` - ci: pass package server to Cookbook model tests (#556)

- 完整 hash: `f89209aa84a4fd0619d0662f6adf6980740efc78`
- 时间/作者: 2026-10-19 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a8543c813` - [CI] cookbook: Add BW1000 deployment smoke tests (#570)

- 完整 hash: `a8543c8131d429500411b8ba235b5411ddbabbd3`
- 时间/作者: 2026-10-20 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6dac3481c` - [Fix] ci: Preserve model cases in DashHub operator reporting (#604)

- 完整 hash: `6dac3481cd73b48641f481b14858187d1936ee81`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `098f31d69` - fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612)

- 完整 hash: `098f31d695ce94169e6adf9ce55109beb532b326`
- 时间/作者: 2026-10-28 / 463975089
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `029b6e641` - [CI] model-ci: Pass history token for daily comparison report (#607)

- 完整 hash: `029b6e6418828280e22086449dfa174433d2788b`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fd98647ed` - [Fix] ci: Restore previous DashHub operator reporting (#614)

- 完整 hash: `fd98647ed1fc3d911926ea9d399b69934303c104`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `25aa13e98` - fix(ci) rebase pr-test-hcu.yml (#617)

- 完整 hash: `25aa13e98fe76d262d87c0b798ec8a3215ffb703`
- 时间/作者: 2026-10-29 / 463975089
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `db479b030` - [CI] optest: Report outcome to DashHub (#619)

- 完整 hash: `db479b030f0975dbda241bf46fc4556a89a02365`
- 时间/作者: 2026-10-29 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `9fb319cc3` - [CI] optest: Require every enabled operator result (#622)

- 完整 hash: `9fb319cc33a15b624970b0f5e45020e2a573dc07`
- 时间/作者: 2026-10-29 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `471ab8254` - Add one-time DashHub recovery for run 41338132822 (#633)

- 完整 hash: `471ab8254520c958d3c614e768a29b10423f7cf2`
- 时间/作者: 2026-11-02 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `594e1ae94` - [Chore] ci: Remove completed DashHub recovery workflow (#634)

- 完整 hash: `594e1ae94c6103dabed4152a4ebbcca6fb049aeb`
- 时间/作者: 2026-11-02 / guochenyang
- 分支更新段: `hg-full-base..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
