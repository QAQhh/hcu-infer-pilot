# vllm Shared Framework PRs 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `.clang-format` | [#4722](https://github.com/vllm-project/vllm/pull/4722) |
| `.dockerignore` | [#2237](https://github.com/vllm-project/vllm/pull/2237), [#7298](https://github.com/vllm-project/vllm/pull/7298), [#7824](https://github.com/vllm-project/vllm/pull/7824), [#8900](https://github.com/vllm-project/vllm/pull/8900), [#9375](https://github.com/vllm-project/vllm/pull/9375), [#36949](https://github.com/vllm-project/vllm/pull/36949), [#40848](https://github.com/vllm-project/vllm/pull/40848), [#44463](https://github.com/vllm-project/vllm/pull/44463), [#44497](https://github.com/vllm-project/vllm/pull/44497), [#48646](https://github.com/vllm-project/vllm/pull/48646), [#61302](https://github.com/vllm-project/vllm/pull/61302), [#61939](https://github.com/vllm-project/vllm/pull/61939), ... (13 total) |
| `.git-blame-ignore-revs` | [#26690](https://github.com/vllm-project/vllm/pull/26690) |
| `.github/CODEOWNERS` | [#8795](https://github.com/vllm-project/vllm/pull/8795), [#9210](https://github.com/vllm-project/vllm/pull/9210), [#10397](https://github.com/vllm-project/vllm/pull/10397), [#12228](https://github.com/vllm-project/vllm/pull/12228), [#12229](https://github.com/vllm-project/vllm/pull/12229), [#14496](https://github.com/vllm-project/vllm/pull/14496), [#17267](https://github.com/vllm-project/vllm/pull/17267), [#18387](https://github.com/vllm-project/vllm/pull/18387), [#18605](https://github.com/vllm-project/vllm/pull/18605), [#19247](https://github.com/vllm-project/vllm/pull/19247), [#20131](https://github.com/vllm-project/vllm/pull/20131), [#20513](https://github.com/vllm-project/vllm/pull/20513), ... (121 total) |
| `.github/CODE_OF_CONDUCT.md` | [#58572](https://github.com/vllm-project/vllm/pull/58572) |
| `.github/CONTRIBUTING.md` | [#58572](https://github.com/vllm-project/vllm/pull/58572) |
| `.github/FUNDING.yml` | [#6435](https://github.com/vllm-project/vllm/pull/6435), [#10426](https://github.com/vllm-project/vllm/pull/10426) |
| `.github/ISSUE_TEMPLATE/100-documentation.yml` | [#3412](https://github.com/vllm-project/vllm/pull/3412), [#3436](https://github.com/vllm-project/vllm/pull/3436), [#7809](https://github.com/vllm-project/vllm/pull/7809), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/200-installation.yml` | [#3412](https://github.com/vllm-project/vllm/pull/3412), [#4211](https://github.com/vllm-project/vllm/pull/4211), [#7809](https://github.com/vllm-project/vllm/pull/7809), [#16759](https://github.com/vllm-project/vllm/pull/16759) |
| `.github/ISSUE_TEMPLATE/300-usage.yml` | [#3412](https://github.com/vllm-project/vllm/pull/3412), [#4211](https://github.com/vllm-project/vllm/pull/4211), [#7809](https://github.com/vllm-project/vllm/pull/7809), [#16759](https://github.com/vllm-project/vllm/pull/16759) |
| `.github/ISSUE_TEMPLATE/400-bug-report.yml` | [#11667](https://github.com/vllm-project/vllm/pull/11667), [#12582](https://github.com/vllm-project/vllm/pull/12582), [#13407](https://github.com/vllm-project/vllm/pull/13407), [#16759](https://github.com/vllm-project/vllm/pull/16759), [#17486](https://github.com/vllm-project/vllm/pull/17486), [#18696](https://github.com/vllm-project/vllm/pull/18696), [#19365](https://github.com/vllm-project/vllm/pull/19365), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/450-ci-failure.yml` | [#18696](https://github.com/vllm-project/vllm/pull/18696), [#18699](https://github.com/vllm-project/vllm/pull/18699), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/500-feature-request.yml` | [#11667](https://github.com/vllm-project/vllm/pull/11667), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/700-performance-discussion.yml` | [#11667](https://github.com/vllm-project/vllm/pull/11667), [#16759](https://github.com/vllm-project/vllm/pull/16759), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/750-RFC.yml` | [#4401](https://github.com/vllm-project/vllm/pull/4401), [#7809](https://github.com/vllm-project/vllm/pull/7809), [#21279](https://github.com/vllm-project/vllm/pull/21279), [#25416](https://github.com/vllm-project/vllm/pull/25416), [#26671](https://github.com/vllm-project/vllm/pull/26671), [#26814](https://github.com/vllm-project/vllm/pull/26814) |
| `.github/ISSUE_TEMPLATE/config.yml` | [#3412](https://github.com/vllm-project/vllm/pull/3412), [#15226](https://github.com/vllm-project/vllm/pull/15226) |
| `.github/PULL_REQUEST_TEMPLATE.md` | [#3413](https://github.com/vllm-project/vllm/pull/3413), [#3478](https://github.com/vllm-project/vllm/pull/3478), [#6917](https://github.com/vllm-project/vllm/pull/6917), [#10159](https://github.com/vllm-project/vllm/pull/10159), [#12941](https://github.com/vllm-project/vllm/pull/12941), [#16276](https://github.com/vllm-project/vllm/pull/16276), [#18661](https://github.com/vllm-project/vllm/pull/18661), [#19086](https://github.com/vllm-project/vllm/pull/19086), [#19289](https://github.com/vllm-project/vllm/pull/19289), [#21851](https://github.com/vllm-project/vllm/pull/21851), [#22852](https://github.com/vllm-project/vllm/pull/22852), [#23598](https://github.com/vllm-project/vllm/pull/23598), ... (14 total) |
| `.github/actionlint.yaml` | [#45865](https://github.com/vllm-project/vllm/pull/45865), [#46769](https://github.com/vllm-project/vllm/pull/46769), [#54827](https://github.com/vllm-project/vllm/pull/54827) |
| `.github/codecov.yml` | [#58572](https://github.com/vllm-project/vllm/pull/58572) |
| `.github/dependabot.yml` | [#1217](https://github.com/vllm-project/vllm/pull/1217), [#9811](https://github.com/vllm-project/vllm/pull/9811), [#9935](https://github.com/vllm-project/vllm/pull/9935), [#10436](https://github.com/vllm-project/vllm/pull/10436), [#13994](https://github.com/vllm-project/vllm/pull/13994), [#39612](https://github.com/vllm-project/vllm/pull/39612) |
| `.github/mergify.yml` | [#9259](https://github.com/vllm-project/vllm/pull/9259), [#9804](https://github.com/vllm-project/vllm/pull/9804), [#10080](https://github.com/vllm-project/vllm/pull/10080), [#12280](https://github.com/vllm-project/vllm/pull/12280), [#13944](https://github.com/vllm-project/vllm/pull/13944), [#14402](https://github.com/vllm-project/vllm/pull/14402), [#14549](https://github.com/vllm-project/vllm/pull/14549), [#15560](https://github.com/vllm-project/vllm/pull/15560), [#15634](https://github.com/vllm-project/vllm/pull/15634), [#16298](https://github.com/vllm-project/vllm/pull/16298), [#16350](https://github.com/vllm-project/vllm/pull/16350), [#17055](https://github.com/vllm-project/vllm/pull/17055), ... (88 total) |
| `.github/scale-config.yml` | [#23840](https://github.com/vllm-project/vllm/pull/23840) |
| `.github/workflows/add_label_automerge.yml` | [#6381](https://github.com/vllm-project/vllm/pull/6381), [#7876](https://github.com/vllm-project/vllm/pull/7876), [#9197](https://github.com/vllm-project/vllm/pull/9197), [#9430](https://github.com/vllm-project/vllm/pull/9430), [#17730](https://github.com/vllm-project/vllm/pull/17730), [#18078](https://github.com/vllm-project/vllm/pull/18078), [#24413](https://github.com/vllm-project/vllm/pull/24413), [#39667](https://github.com/vllm-project/vllm/pull/39667), [#51095](https://github.com/vllm-project/vllm/pull/51095), [#55349](https://github.com/vllm-project/vllm/pull/55349) |
| `.github/workflows/buf.yml` | [#51276](https://github.com/vllm-project/vllm/pull/51276), [#55349](https://github.com/vllm-project/vllm/pull/55349), [#57046](https://github.com/vllm-project/vllm/pull/57046), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.github/workflows/issue_autolabel.yml` | [#20988](https://github.com/vllm-project/vllm/pull/20988), [#23942](https://github.com/vllm-project/vllm/pull/23942), [#24413](https://github.com/vllm-project/vllm/pull/24413), [#26753](https://github.com/vllm-project/vllm/pull/26753), [#29602](https://github.com/vllm-project/vllm/pull/29602), [#29610](https://github.com/vllm-project/vllm/pull/29610), [#37009](https://github.com/vllm-project/vllm/pull/37009), [#39312](https://github.com/vllm-project/vllm/pull/39312), [#39667](https://github.com/vllm-project/vllm/pull/39667), [#47132](https://github.com/vllm-project/vllm/pull/47132), [#48643](https://github.com/vllm-project/vllm/pull/48643), [#49398](https://github.com/vllm-project/vllm/pull/49398), ... (26 total) |
| `.github/workflows/macos-smoke-test.yml` | [#28688](https://github.com/vllm-project/vllm/pull/28688), [#28736](https://github.com/vllm-project/vllm/pull/28736), [#28752](https://github.com/vllm-project/vllm/pull/28752), [#28954](https://github.com/vllm-project/vllm/pull/28954), [#29293](https://github.com/vllm-project/vllm/pull/29293), [#30233](https://github.com/vllm-project/vllm/pull/30233), [#33002](https://github.com/vllm-project/vllm/pull/33002), [#33057](https://github.com/vllm-project/vllm/pull/33057), [#35775](https://github.com/vllm-project/vllm/pull/35775), [#37567](https://github.com/vllm-project/vllm/pull/37567), [#38290](https://github.com/vllm-project/vllm/pull/38290), [#39024](https://github.com/vllm-project/vllm/pull/39024), ... (16 total) |
| `.github/workflows/matchers/actionlint.json` | [#7876](https://github.com/vllm-project/vllm/pull/7876) |
| `.github/workflows/matchers/markdownlint.json` | [#21892](https://github.com/vllm-project/vllm/pull/21892) |
| `.github/workflows/matchers/mypy.json` | [#9512](https://github.com/vllm-project/vllm/pull/9512) |
| `.github/workflows/matchers/shellcheck.json` | [#52572](https://github.com/vllm-project/vllm/pull/52572) |
| `.github/workflows/new_pr_bot.yml` | [#37552](https://github.com/vllm-project/vllm/pull/37552), [#37999](https://github.com/vllm-project/vllm/pull/37999), [#39667](https://github.com/vllm-project/vllm/pull/39667), [#40114](https://github.com/vllm-project/vllm/pull/40114), [#50132](https://github.com/vllm-project/vllm/pull/50132), [#51732](https://github.com/vllm-project/vllm/pull/51732), [#52822](https://github.com/vllm-project/vllm/pull/52822), [#55349](https://github.com/vllm-project/vllm/pull/55349) |
| `.github/workflows/notify-ci-authorized.yml` | [#50414](https://github.com/vllm-project/vllm/pull/50414), [#51079](https://github.com/vllm-project/vllm/pull/51079), [#51095](https://github.com/vllm-project/vllm/pull/51095), [#55349](https://github.com/vllm-project/vllm/pull/55349), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.github/workflows/pip-compile-drift.yml` | [#59526](https://github.com/vllm-project/vllm/pull/59526) |
| `.github/workflows/pr-title.yml` | [#54263](https://github.com/vllm-project/vllm/pull/54263), [#54827](https://github.com/vllm-project/vllm/pull/54827), [#55349](https://github.com/vllm-project/vllm/pull/55349) |
| `.github/workflows/pre-commit.yml` | [#11975](https://github.com/vllm-project/vllm/pull/11975), [#12212](https://github.com/vllm-project/vllm/pull/12212), [#12279](https://github.com/vllm-project/vllm/pull/12279), [#12672](https://github.com/vllm-project/vllm/pull/12672), [#13162](https://github.com/vllm-project/vllm/pull/13162), [#17729](https://github.com/vllm-project/vllm/pull/17729), [#21892](https://github.com/vllm-project/vllm/pull/21892), [#21919](https://github.com/vllm-project/vllm/pull/21919), [#24414](https://github.com/vllm-project/vllm/pull/24414), [#29293](https://github.com/vllm-project/vllm/pull/29293), [#29768](https://github.com/vllm-project/vllm/pull/29768), [#30233](https://github.com/vllm-project/vllm/pull/30233), ... (27 total) |
| `.github/workflows/proto-crate.yml` | [#56365](https://github.com/vllm-project/vllm/pull/56365), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.github/workflows/recipes-preview.yml` | [#63259](https://github.com/vllm-project/vllm/pull/63259), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.github/workflows/recipes.yml` | [#61302](https://github.com/vllm-project/vllm/pull/61302), [#64241](https://github.com/vllm-project/vllm/pull/64241) |
| `.github/workflows/record-ci-approval.yml` | [#50414](https://github.com/vllm-project/vllm/pull/50414), [#51095](https://github.com/vllm-project/vllm/pull/51095), [#55349](https://github.com/vllm-project/vllm/pull/55349) |
| `.github/workflows/run-ci-command.yml` | [#50132](https://github.com/vllm-project/vllm/pull/50132), [#50211](https://github.com/vllm-project/vllm/pull/50211), [#51087](https://github.com/vllm-project/vllm/pull/51087), [#51127](https://github.com/vllm-project/vllm/pull/51127), [#51732](https://github.com/vllm-project/vllm/pull/51732), [#52822](https://github.com/vllm-project/vllm/pull/52822), [#55349](https://github.com/vllm-project/vllm/pull/55349), [#56169](https://github.com/vllm-project/vllm/pull/56169), [#60925](https://github.com/vllm-project/vllm/pull/60925), [#61592](https://github.com/vllm-project/vllm/pull/61592), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.github/workflows/scripts/build.sh` | [#746](https://github.com/vllm-project/vllm/pull/746), [#1527](https://github.com/vllm-project/vllm/pull/1527), [#2605](https://github.com/vllm-project/vllm/pull/2605), [#3801](https://github.com/vllm-project/vllm/pull/3801), [#3841](https://github.com/vllm-project/vllm/pull/3841), [#5036](https://github.com/vllm-project/vllm/pull/5036), [#8245](https://github.com/vllm-project/vllm/pull/8245), [#8834](https://github.com/vllm-project/vllm/pull/8834), [#8900](https://github.com/vllm-project/vllm/pull/8900), [#9375](https://github.com/vllm-project/vllm/pull/9375), [#12547](https://github.com/vllm-project/vllm/pull/12547), [#21599](https://github.com/vllm-project/vllm/pull/21599), ... (16 total) |
| `.github/workflows/scripts/create_release.js` | [#746](https://github.com/vllm-project/vllm/pull/746), [#4600](https://github.com/vllm-project/vllm/pull/4600), [#14561](https://github.com/vllm-project/vllm/pull/14561) |
| `.github/workflows/scripts/cuda-install.sh` | [#746](https://github.com/vllm-project/vllm/pull/746), [#1527](https://github.com/vllm-project/vllm/pull/1527), [#7925](https://github.com/vllm-project/vllm/pull/7925) |
| `.github/workflows/scripts/env.sh` | [#746](https://github.com/vllm-project/vllm/pull/746) |
| `.github/workflows/scripts/pytorch-install.sh` | [#746](https://github.com/vllm-project/vllm/pull/746), [#1377](https://github.com/vllm-project/vllm/pull/1377), [#1378](https://github.com/vllm-project/vllm/pull/1378), [#7925](https://github.com/vllm-project/vllm/pull/7925) |
| `.github/workflows/scripts/run_ci_command.py` | [#50132](https://github.com/vllm-project/vllm/pull/50132), [#50197](https://github.com/vllm-project/vllm/pull/50197), [#50318](https://github.com/vllm-project/vllm/pull/50318), [#50414](https://github.com/vllm-project/vllm/pull/50414), [#50481](https://github.com/vllm-project/vllm/pull/50481), [#51087](https://github.com/vllm-project/vllm/pull/51087), [#51095](https://github.com/vllm-project/vllm/pull/51095), [#51732](https://github.com/vllm-project/vllm/pull/51732), [#52822](https://github.com/vllm-project/vllm/pull/52822), [#54895](https://github.com/vllm-project/vllm/pull/54895), [#56169](https://github.com/vllm-project/vllm/pull/56169), [#60925](https://github.com/vllm-project/vllm/pull/60925), ... (16 total) |
| `.github/workflows/scripts/test_run_ci_command.py` | [#50132](https://github.com/vllm-project/vllm/pull/50132), [#50197](https://github.com/vllm-project/vllm/pull/50197), [#50318](https://github.com/vllm-project/vllm/pull/50318), [#50414](https://github.com/vllm-project/vllm/pull/50414), [#50481](https://github.com/vllm-project/vllm/pull/50481), [#51087](https://github.com/vllm-project/vllm/pull/51087), [#51095](https://github.com/vllm-project/vllm/pull/51095), [#51732](https://github.com/vllm-project/vllm/pull/51732), [#52822](https://github.com/vllm-project/vllm/pull/52822), [#54895](https://github.com/vllm-project/vllm/pull/54895), [#56169](https://github.com/vllm-project/vllm/pull/56169), [#60925](https://github.com/vllm-project/vllm/pull/60925), ... (15 total) |
| `.github/workflows/stale.yml` | [#9436](https://github.com/vllm-project/vllm/pull/9436), [#9661](https://github.com/vllm-project/vllm/pull/9661), [#9734](https://github.com/vllm-project/vllm/pull/9734), [#12462](https://github.com/vllm-project/vllm/pull/12462), [#24412](https://github.com/vllm-project/vllm/pull/24412), [#26272](https://github.com/vllm-project/vllm/pull/26272), [#29654](https://github.com/vllm-project/vllm/pull/29654), [#30234](https://github.com/vllm-project/vllm/pull/30234), [#35078](https://github.com/vllm-project/vllm/pull/35078), [#64328](https://github.com/vllm-project/vllm/pull/64328) |
| `.gitignore` | [#120](https://github.com/vllm-project/vllm/pull/120), [#140](https://github.com/vllm-project/vllm/pull/140), [#156](https://github.com/vllm-project/vllm/pull/156), [#261](https://github.com/vllm-project/vllm/pull/261), [#1032](https://github.com/vllm-project/vllm/pull/1032), [#1836](https://github.com/vllm-project/vllm/pull/1836), [#2172](https://github.com/vllm-project/vllm/pull/2172), [#3005](https://github.com/vllm-project/vllm/pull/3005), [#3269](https://github.com/vllm-project/vllm/pull/3269), [#3290](https://github.com/vllm-project/vllm/pull/3290), [#4225](https://github.com/vllm-project/vllm/pull/4225), [#4738](https://github.com/vllm-project/vllm/pull/4738), ... (58 total) |
| `.pre-commit-config.yaml` | [#11879](https://github.com/vllm-project/vllm/pull/11879), [#11975](https://github.com/vllm-project/vllm/pull/11975), [#12212](https://github.com/vllm-project/vllm/pull/12212), [#12217](https://github.com/vllm-project/vllm/pull/12217), [#12224](https://github.com/vllm-project/vllm/pull/12224), [#12475](https://github.com/vllm-project/vllm/pull/12475), [#12521](https://github.com/vllm-project/vllm/pull/12521), [#12547](https://github.com/vllm-project/vllm/pull/12547), [#12595](https://github.com/vllm-project/vllm/pull/12595), [#12628](https://github.com/vllm-project/vllm/pull/12628), [#12804](https://github.com/vllm-project/vllm/pull/12804), [#12880](https://github.com/vllm-project/vllm/pull/12880), ... (108 total) |
| `.readthedocs.yaml` | [#136](https://github.com/vllm-project/vllm/pull/136), [#6834](https://github.com/vllm-project/vllm/pull/6834), [#8464](https://github.com/vllm-project/vllm/pull/8464), [#9347](https://github.com/vllm-project/vllm/pull/9347), [#10038](https://github.com/vllm-project/vllm/pull/10038), [#12547](https://github.com/vllm-project/vllm/pull/12547), [#18145](https://github.com/vllm-project/vllm/pull/18145), [#21752](https://github.com/vllm-project/vllm/pull/21752), [#25580](https://github.com/vllm-project/vllm/pull/25580), [#34240](https://github.com/vllm-project/vllm/pull/34240), [#36135](https://github.com/vllm-project/vllm/pull/36135), [#36790](https://github.com/vllm-project/vllm/pull/36790), ... (17 total) |
| `AGENTS.md` | [#36877](https://github.com/vllm-project/vllm/pull/36877), [#36909](https://github.com/vllm-project/vllm/pull/36909), [#37819](https://github.com/vllm-project/vllm/pull/37819), [#38057](https://github.com/vllm-project/vllm/pull/38057), [#39024](https://github.com/vllm-project/vllm/pull/39024), [#43635](https://github.com/vllm-project/vllm/pull/43635), [#44635](https://github.com/vllm-project/vllm/pull/44635), [#44647](https://github.com/vllm-project/vllm/pull/44647), [#45274](https://github.com/vllm-project/vllm/pull/45274), [#45301](https://github.com/vllm-project/vllm/pull/45301), [#45975](https://github.com/vllm-project/vllm/pull/45975), [#46373](https://github.com/vllm-project/vllm/pull/46373), ... (20 total) |
| `CMakeLists.txt` | [#2830](https://github.com/vllm-project/vllm/pull/2830), [#3140](https://github.com/vllm-project/vllm/pull/3140), [#3287](https://github.com/vllm-project/vllm/pull/3287), [#3290](https://github.com/vllm-project/vllm/pull/3290), [#3527](https://github.com/vllm-project/vllm/pull/3527), [#3534](https://github.com/vllm-project/vllm/pull/3534), [#3634](https://github.com/vllm-project/vllm/pull/3634), [#3698](https://github.com/vllm-project/vllm/pull/3698), [#3805](https://github.com/vllm-project/vllm/pull/3805), [#3922](https://github.com/vllm-project/vllm/pull/3922), [#4244](https://github.com/vllm-project/vllm/pull/4244), [#4304](https://github.com/vllm-project/vllm/pull/4304), ... (327 total) |
| `DCO` | [#9803](https://github.com/vllm-project/vllm/pull/9803) |
| `LICENSE` | [#102](https://github.com/vllm-project/vllm/pull/102) |
| `MANIFEST.in` | [#140](https://github.com/vllm-project/vllm/pull/140), [#2830](https://github.com/vllm-project/vllm/pull/2830), [#3841](https://github.com/vllm-project/vllm/pull/3841), [#4559](https://github.com/vllm-project/vllm/pull/4559), [#6837](https://github.com/vllm-project/vllm/pull/6837), [#7938](https://github.com/vllm-project/vllm/pull/7938), [#12547](https://github.com/vllm-project/vllm/pull/12547), [#21159](https://github.com/vllm-project/vllm/pull/21159), [#44981](https://github.com/vllm-project/vllm/pull/44981) |
| `README.md` | [#109](https://github.com/vllm-project/vllm/pull/109), [#147](https://github.com/vllm-project/vllm/pull/147), [#150](https://github.com/vllm-project/vllm/pull/150), [#156](https://github.com/vllm-project/vllm/pull/156), [#161](https://github.com/vllm-project/vllm/pull/161), [#162](https://github.com/vllm-project/vllm/pull/162), [#163](https://github.com/vllm-project/vllm/pull/163), [#164](https://github.com/vllm-project/vllm/pull/164), [#166](https://github.com/vllm-project/vllm/pull/166), [#167](https://github.com/vllm-project/vllm/pull/167), [#213](https://github.com/vllm-project/vllm/pull/213), [#226](https://github.com/vllm-project/vllm/pull/226), ... (179 total) |
| `SECURITY.md` | [#8642](https://github.com/vllm-project/vllm/pull/8642), [#9132](https://github.com/vllm-project/vllm/pull/9132), [#9925](https://github.com/vllm-project/vllm/pull/9925), [#12175](https://github.com/vllm-project/vllm/pull/12175), [#18961](https://github.com/vllm-project/vllm/pull/18961), [#21119](https://github.com/vllm-project/vllm/pull/21119), [#22102](https://github.com/vllm-project/vllm/pull/22102), [#23532](https://github.com/vllm-project/vllm/pull/23532), [#45253](https://github.com/vllm-project/vllm/pull/45253), [#55476](https://github.com/vllm-project/vllm/pull/55476) |
| `benchmarks/README.md` | [#133](https://github.com/vllm-project/vllm/pull/133), [#150](https://github.com/vllm-project/vllm/pull/150), [#9851](https://github.com/vllm-project/vllm/pull/9851), [#12941](https://github.com/vllm-project/vllm/pull/12941), [#13063](https://github.com/vllm-project/vllm/pull/13063), [#14646](https://github.com/vllm-project/vllm/pull/14646), [#14654](https://github.com/vllm-project/vllm/pull/14654), [#14874](https://github.com/vllm-project/vllm/pull/14874), [#15170](https://github.com/vllm-project/vllm/pull/15170), [#15748](https://github.com/vllm-project/vllm/pull/15748), [#15998](https://github.com/vllm-project/vllm/pull/15998), [#16022](https://github.com/vllm-project/vllm/pull/16022), ... (32 total) |
| `benchmarks/__init__.py` | [#40167](https://github.com/vllm-project/vllm/pull/40167) |
| `benchmarks/attention_benchmarks/README.md` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#36398](https://github.com/vllm-project/vllm/pull/36398), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/__init__.py` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#35418](https://github.com/vllm-project/vllm/pull/35418) |
| `benchmarks/attention_benchmarks/batch_spec.py` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33810](https://github.com/vllm-project/vllm/pull/33810), [#52136](https://github.com/vllm-project/vllm/pull/52136) |
| `benchmarks/attention_benchmarks/benchmark.py` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#34732](https://github.com/vllm-project/vllm/pull/34732), [#37049](https://github.com/vllm-project/vllm/pull/37049), [#37115](https://github.com/vllm-project/vllm/pull/37115), [#39336](https://github.com/vllm-project/vllm/pull/39336), [#42669](https://github.com/vllm-project/vllm/pull/42669), [#43050](https://github.com/vllm-project/vllm/pull/43050), [#47327](https://github.com/vllm-project/vllm/pull/47327), [#48770](https://github.com/vllm-project/vllm/pull/48770), [#52136](https://github.com/vllm-project/vllm/pull/52136), [#53785](https://github.com/vllm-project/vllm/pull/53785), ... (14 total) |
| `benchmarks/attention_benchmarks/common.py` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#33810](https://github.com/vllm-project/vllm/pull/33810), [#34732](https://github.com/vllm-project/vllm/pull/34732), [#34934](https://github.com/vllm-project/vllm/pull/34934), [#35418](https://github.com/vllm-project/vllm/pull/35418), [#37115](https://github.com/vllm-project/vllm/pull/37115), [#39336](https://github.com/vllm-project/vllm/pull/39336), [#47327](https://github.com/vllm-project/vllm/pull/47327), [#48770](https://github.com/vllm-project/vllm/pull/48770), [#52136](https://github.com/vllm-project/vllm/pull/52136), [#59774](https://github.com/vllm-project/vllm/pull/59774) |
| `benchmarks/attention_benchmarks/configs/mla_decode.yaml` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#39336](https://github.com/vllm-project/vllm/pull/39336), [#41778](https://github.com/vllm-project/vllm/pull/41778) |
| `benchmarks/attention_benchmarks/configs/mla_fa4_fp8_output.yaml` | [#43050](https://github.com/vllm-project/vllm/pull/43050) |
| `benchmarks/attention_benchmarks/configs/mla_mixed_batch.yaml` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#37115](https://github.com/vllm-project/vllm/pull/37115), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/mla_prefill.yaml` | [#33451](https://github.com/vllm-project/vllm/pull/33451), [#34732](https://github.com/vllm-project/vllm/pull/34732), [#39336](https://github.com/vllm-project/vllm/pull/39336), [#41778](https://github.com/vllm-project/vllm/pull/41778) |
| `benchmarks/attention_benchmarks/configs/mla_sparse_decode.yaml` | [#37115](https://github.com/vllm-project/vllm/pull/37115), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa.yaml` | [#48770](https://github.com/vllm-project/vllm/pull/48770) |
| `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml` | [#53785](https://github.com/vllm-project/vllm/pull/53785) |
| `benchmarks/attention_benchmarks/configs/mla_sparse_mha_vs_mqa.yaml` | [#47327](https://github.com/vllm-project/vllm/pull/47327) |
| `benchmarks/attention_benchmarks/configs/mla_sparse_prefill.yaml` | [#34732](https://github.com/vllm-project/vllm/pull/34732), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/reorder_threshold.yaml` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/speculative_decode.yaml` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/standard_attention.yaml` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#33810](https://github.com/vllm-project/vllm/pull/33810), [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/standard_decode.yaml` | [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/configs/standard_prefill.yaml` | [#39336](https://github.com/vllm-project/vllm/pull/39336) |
| `benchmarks/attention_benchmarks/mla_runner.py` | [#26835](https://github.com/vllm-project/vllm/pull/26835), [#33451](https://github.com/vllm-project/vllm/pull/33451), [#34732](https://github.com/vllm-project/vllm/pull/34732), [#36085](https://github.com/vllm-project/vllm/pull/36085), [#36145](https://github.com/vllm-project/vllm/pull/36145), [#36216](https://github.com/vllm-project/vllm/pull/36216), [#37115](https://github.com/vllm-project/vllm/pull/37115), [#39336](https://github.com/vllm-project/vllm/pull/39336), [#40844](https://github.com/vllm-project/vllm/pull/40844), [#41778](https://github.com/vllm-project/vllm/pull/41778), [#42555](https://github.com/vllm-project/vllm/pull/42555), [#43050](https://github.com/vllm-project/vllm/pull/43050), ... (17 total) |
| ... | 7265 more files omitted from table; all were used for git tracing. |

## PR 覆盖总览

- git 追溯 PR 数: 36
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 36
- 历史截断: 旧版 shared 档案共 10,298 条 PR，本轮按「最新 200 条候选」抓取并渲染，更早条目仍保留在 git 历史中；需要全量请调大 `MODEL_PR_HISTORY_MAX_DOC_PRS` 后重跑。

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-05 | [#65875](https://github.com/vllm-project/vllm/pull/65875) | merged | [Bugfix][CI] Fix duplicate max_num_seqs in Llama Nemotron VL pooling test | `tests/models/multimodal/pooling/test_llama_nemotron_vl.py` |
| 2026-11-05 | [#64856](https://github.com/vllm-project/vllm/pull/64856) | merged | [Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace | `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py` |
| 2026-11-05 | [#64880](https://github.com/vllm-project/vllm/pull/64880) | merged | [Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters | `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` |
| 2026-11-05 | [#64886](https://github.com/vllm-project/vllm/pull/64886) | merged | [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes | `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/kimi_k3/amd/kda.py` |
| 2026-11-05 | [#65763](https://github.com/vllm-project/vllm/pull/65763) | merged | [CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic | `tests/kernels/attention/test_minimax_m3.py` |
| 2026-11-05 | [#65577](https://github.com/vllm-project/vllm/pull/65577) | merged | [MM] Support mm_device_do_normalize for Gemma 4 | `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`, `tests/models/multimodal/generation_ppl_test/gemma.py` |
| 2026-11-05 | [#65552](https://github.com/vllm-project/vllm/pull/65552) | merged | [CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype | `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` |
| 2026-11-04 | [#65542](https://github.com/vllm-project/vllm/pull/65542) | merged | [Kernel] Marlin: remove 8-bit (INT8/FP8) activation support, rely on Humming | `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_test.py` |
| 2026-11-04 | [#65537](https://github.com/vllm-project/vllm/pull/65537) | merged | [MiniMax-M3] Support sequence parallelism with pipeline parallelism | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-04 | [#64583](https://github.com/vllm-project/vllm/pull/64583) | merged | [Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode | `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py` |
| 2026-11-04 | [#65449](https://github.com/vllm-project/vllm/pull/65449) | merged | [Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state | `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-11-04 | [#65432](https://github.com/vllm-project/vllm/pull/65432) | merged | [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP | `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py` |
| 2026-11-04 | [#65087](https://github.com/vllm-project/vllm/pull/65087) | merged | [ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer | `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py` |
| 2026-11-03 | [#64723](https://github.com/vllm-project/vllm/pull/64723) | merged | [Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant | `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py` |
| 2026-11-03 | [#65496](https://github.com/vllm-project/vllm/pull/65496) | merged | [Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism | `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-03 | [#65030](https://github.com/vllm-project/vllm/pull/65030) | merged | [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes | `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py` |
| 2026-11-03 | [#65174](https://github.com/vllm-project/vllm/pull/65174) | merged | [Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig | `vllm/transformers_utils/configs/kimi_vl.py` |
| 2026-11-03 | [#65296](https://github.com/vllm-project/vllm/pull/65296) | merged | [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-11-03 | [#64974](https://github.com/vllm-project/vllm/pull/64974) | merged | [Refactor][DSv4.1] Remove duplicated code | `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-11-03 | [#65226](https://github.com/vllm-project/vllm/pull/65226) | merged | [Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences | `vllm/models/minimax_m3/common/encoder_cudagraph.py` |
| 2026-11-02 | [#65118](https://github.com/vllm-project/vllm/pull/65118) | merged | [Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path | `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py` |
| 2026-11-02 | [#64815](https://github.com/vllm-project/vllm/pull/64815) | merged | [Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel | `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` |
| 2026-11-02 | [#64984](https://github.com/vllm-project/vllm/pull/64984) | merged | [Bugfix][MM] Keep FlashInfer cu_seqlens halves aligned in Qwen3-VL encoder CUDA graph replay | `vllm/model_executor/models/qwen3_vl.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py` |
| 2026-11-02 | [#64734](https://github.com/vllm-project/vllm/pull/64734) | merged | [ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s | `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml` |
| 2026-11-02 | [#64852](https://github.com/vllm-project/vllm/pull/64852) | merged | [Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8 | `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py` |
| 2026-11-02 | [#64659](https://github.com/vllm-project/vllm/pull/64659) | merged | [Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE | `vllm/models/minimax_m3/nvidia/model.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py` |
| 2026-11-02 | [#64971](https://github.com/vllm-project/vllm/pull/64971) | merged | [Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages | `tests/entrypoints/scale_out/render/test_render.py`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/tokenizers_/test_deepseek_v41.py` |
| 2026-11-02 | [#64944](https://github.com/vllm-project/vllm/pull/64944) | merged | [Model] Nemotron-3.5-Transcribe: pack the audio tower's valid frames for MMEncoderAttention | `vllm/model_executor/models/nemotron3_5_transcribe_audio.py`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `docs/models/supported_models.md` |
| 2026-11-02 | [#65008](https://github.com/vllm-project/vllm/pull/65008) | merged | [CI] Lower gpu_memory_utilization in test_gemma4_lora | `tests/lora/test_gemma4_tp.py` |
| 2026-11-02 | [#64816](https://github.com/vllm-project/vllm/pull/64816) | merged | [Perf][DSv4.1] Vectorize first-layer HC expansion copy | `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/mhc/test_mhc_kernels.py` |
| 2026-10-31 | [#64675](https://github.com/vllm-project/vllm/pull/64675) | merged | [Bugfix][Parser] Parse closed Qwen3 tool parameters once while streaming | `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py` |
| 2026-10-30 | [#64509](https://github.com/vllm-project/vllm/pull/64509) | merged | [Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant | `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` |
| 2026-10-30 | [#64644](https://github.com/vllm-project/vllm/pull/64644) | merged | [CI] Fix mypy errors in test_glm5next.py | `tests/models/multimodal/processing/test_glm5next.py` |
| 2026-10-30 | [#64619](https://github.com/vllm-project/vllm/pull/64619) | merged | [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub | `tests/models/kimi_k3/test_amd_kda_checkpoint.py` |
| 2026-10-29 | [#64535](https://github.com/vllm-project/vllm/pull/64535) | merged | [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming | `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py` |
| 2026-10-29 | [#64506](https://github.com/vllm-project/vllm/pull/64506) | merged | [Bugfix][Model] Nemotron 3.5 Super VL: support the native transformers config | `tests/models/registry.py`, `docs/models/supported_models.md`, `vllm/model_executor/models/nano_nemotron_vl.py` |

## 逐 PR diff 审计卡

### PR #65875 - [Bugfix][CI] Fix duplicate max_num_seqs in Llama Nemotron VL pooling test

- 链接: https://github.com/vllm-project/vllm/pull/65875
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`；关联提交 `3eb8a5b16658`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-2，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][CI] Fix duplicate max_num_seqs in Llama Nemotron VL pooling test」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`；技术摘要: 覆盖「[Bugfix][CI] Fix duplicate max_num_seqs in Llama Nemotron VL pooling test」；主要实现面是 `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/pooling/test_llama_nemotron_vl.py` modified +3/-2 (5 lines); hunks: -71,22 +71,23 @@ def test_image_embeddings_without_chunked_prefill(; symbols: test_image_embeddings_without_chunked_prefill，涉及 `test_image_embeddings_without_chunked_prefill`。
- 代码 diff 细节:
  - `tests/models/multimodal/pooling/test_llama_nemotron_vl.py` modified +3/-2 (5 lines); hunks: -71,22 +71,23 @@ def test_image_embeddings_without_chunked_prefill(; symbols: test_image_embeddings_without_chunked_prefill
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/pooling/test_llama_nemotron_vl.py
@@ -71,22 +71,23 @@ def test_image_embeddings_without_chunked_prefill(
+    # ROCM_ENGINE_KWARGS also sets max_num_seqs, which this test needs at 2.
+    engine_kwargs = {**ROCM_ENGINE_KWARGS, "max_num_seqs": 2}
-        max_num_seqs=2,
-        **ROCM_ENGINE_KWARGS,
+        **engine_kwargs,
```

- 已读文件:
  - tests: `tests/models/multimodal/pooling/test_llama_nemotron_vl.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64856 - [Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace

- 链接: https://github.com/vllm-project/vllm/pull/64856
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`；关联提交 `6a6f8047968a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+72/-142，可读 patch 308 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace」；主要实现面是 `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #64880 - [Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters

- 链接: https://github.com/vllm-project/vllm/pull/64880
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/lora/test_layers.py`, `vllm/lora/layers/custom_layer.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/grouped_wo_a.py`, `vllm/models/deepseek_v4/compressor.py` 等 10 个文件；关联提交 `edc7181bdb59`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+215/-44，可读 patch 470 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`；技术摘要: 覆盖「[Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters」；主要实现面是 `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v4/compressor.py` modified +16/-1 (17 lines); hunks: -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -268,7 +276,14 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor，涉及 `get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward`；`vllm/models/deepseek_v4/attention.py` modified +5/-11 (16 lines); hunks: -48,6 +48,7; -268,9 +269,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score, indexer_weights_proj，涉及 `__init__, _run_parallel_input_projections, compressor_kv_score`；`vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8 (13 lines); hunks: -18,7 +18,6; -212,12 +211,10 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, _alloc_attn_out, __init__，涉及 `get_padded_num_q_heads, _o_proj, _alloc_attn_out`；`vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1 (11 lines); hunks: -1,6 +1,7; -15,6 +16,9; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason，涉及 `compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v4/compressor.py` modified +16/-1 (17 lines); hunks: -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -268,7 +276,14 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor
  - `vllm/models/deepseek_v4/attention.py` modified +5/-11 (16 lines); hunks: -48,6 +48,7; -268,9 +269,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score, indexer_weights_proj
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8 (13 lines); hunks: -18,7 +18,6; -212,12 +211,10 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, _alloc_attn_out, __init__
  - `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1 (11 lines); hunks: -1,6 +1,7; -15,6 +16,9; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason
  - `vllm/models/deepseek_v4/nvidia/flashmla.py` modified +3/-7 (10 lines); hunks: -12,10 +12,7; -59,12 +56,10 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _o_proj, get_padded_num_q_heads
- 关键代码摘录:

```diff
diff -- vllm/models/deepseek_v4/compressor.py
@@ -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:
+class DeepseekV4CompressorKVScoreLinear(MergedColumnParallelLinear):
+    """Fused ``wkv``/``wgate`` projection with the FP32 output the compressor
+    state accumulates in."""
+    def forward(self, input_: torch.Tensor) -> torch.Tensor:
+        return torch.mm(input_, self.weight.T, out_dtype=torch.float32)
@@ -268,7 +276,14 @@ def __init__(
diff -- vllm/models/deepseek_v4/attention.py
@@ -48,6 +48,7 @@
+from vllm.models.deepseek_v4.common.grouped_wo_a import DeepseekV4GroupedWoA
@@ -268,9 +269,10 @@ def __init__(
-        self.wo_a = ColumnParallelLinear(
+        self.wo_a = DeepseekV4GroupedWoA(
+            n_groups=self.n_groups,
@@ -696,11 +698,7 @@ def _run_parallel_input_projections(
diff -- vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py
@@ -18,7 +18,6 @@
```

- 已读文件:
  - runtime: `vllm/models/deepseek_v4/compressor.py` modified +16/-1; `vllm/models/deepseek_v4/attention.py` modified +5/-11; `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1; `vllm/models/deepseek_v4/nvidia/flashmla.py` modified +3/-7; `vllm/models/deepseek_v41/compressor.py` modified +1/-9
- 验证与风险: diff 自带测试面 `tests/lora/test_layers.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64886 - [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes

- 链接: https://github.com/vllm-project/vllm/pull/64886
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/distributed/weight_transfer/sparse_nccl_engine.py`, `vllm/model_executor/model_loader/reload/inplace.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/kimi_k3/amd/kda.py` 等 6 个文件；关联提交 `e5d0ef3527c9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+57/-16，可读 patch 140 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/kimi_k3/amd/kda.py`；技术摘要: 覆盖「[Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/kimi_k3/amd/kda.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13 (45 lines); hunks: -346,12 +346,15 @@ def test_decode_weights_staged_after_loading(; -412,20 +415,36 @@ def test_decode_weights_staged_after_loading(; symbols: test_decode_weights_staged_after_loading, check_staged，涉及 `test_decode_weights_staged_after_loading, check_staged`；`vllm/model_executor/model_loader/weight_utils.py` modified +13/-0 (13 lines); hunks: -1547,6 +1547,19 @@ def children_first(module: torch.nn.Module) -> Iterable[t...; symbols: children_first, refresh_derived_weights, default_weight_loader，涉及 `children_first, refresh_derived_weights, default_weight_loader`；`vllm/models/kimi_k3/amd/kda.py` modified +5/-3 (8 lines); hunks: -344,10 +344,12 @@ def __init__(; symbols: __init__, process_weights_after_loading, refresh_derived_weights，涉及 `__init__, process_weights_after_loading, refresh_derived_weights`；`vllm/models/kimi_k3/amd/mla.py` modified +3/-0 (3 lines); hunks: -185,6 +185,9 @@ def _build_w_fold(self) -> None:; symbols: _build_w_fold, process_weights_after_loading, refresh_derived_weights，涉及 `_build_w_fold, process_weights_after_loading, refresh_derived_weights`。
- 代码 diff 细节:
  - `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13 (45 lines); hunks: -346,12 +346,15 @@ def test_decode_weights_staged_after_loading(; -412,20 +415,36 @@ def test_decode_weights_staged_after_loading(; symbols: test_decode_weights_staged_after_loading, check_staged
  - `vllm/model_executor/model_loader/weight_utils.py` modified +13/-0 (13 lines); hunks: -1547,6 +1547,19 @@ def children_first(module: torch.nn.Module) -> Iterable[t...; symbols: children_first, refresh_derived_weights, default_weight_loader
  - `vllm/models/kimi_k3/amd/kda.py` modified +5/-3 (8 lines); hunks: -344,10 +344,12 @@ def __init__(; symbols: __init__, process_weights_after_loading, refresh_derived_weights
  - `vllm/models/kimi_k3/amd/mla.py` modified +3/-0 (3 lines); hunks: -185,6 +185,9 @@ def _build_w_fold(self) -> None:; symbols: _build_w_fold, process_weights_after_loading, refresh_derived_weights
  - `vllm/model_executor/model_loader/reload/inplace.py` modified +2/-0 (2 lines); hunks: -10,6 +10,7; -107,6 +108,7 @@ def reload_weights(; symbols: reload_weights
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
diff -- vllm/model_executor/model_loader/weight_utils.py
@@ -1547,6 +1547,19 @@ def children_first(module: torch.nn.Module) -> Iterable[torch.nn.Module]:
+@torch.no_grad()
+def refresh_derived_weights(model: torch.nn.Module) -> None:
+    """Call ``refresh_derived_weights()`` on every module that defines it, to
+    rebuild tensors kept out of ``state_dict()`` after the weights were
+    overwritten in place. Hooks must be idempotent, write in place and run no
+    collectives.
diff -- vllm/models/kimi_k3/amd/kda.py
@@ -344,10 +344,12 @@ def __init__(
```

- 已读文件:
  - tests: `tests/models/kimi_k3/test_amd_kda_decode.py` modified +32/-13
  - runtime: `vllm/model_executor/model_loader/weight_utils.py` modified +13/-0; `vllm/models/kimi_k3/amd/kda.py` modified +5/-3; `vllm/models/kimi_k3/amd/mla.py` modified +3/-0; `vllm/model_executor/model_loader/reload/inplace.py` modified +2/-0; `vllm/distributed/weight_transfer/sparse_nccl_engine.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/kimi_k3/test_amd_kda_decode.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65763 - [CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic

- 链接: https://github.com/vllm-project/vllm/pull/65763
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3.py`；关联提交 `4ab4404e2444`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+21/-4，可读 patch 43 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `tests/kernels/attention/test_minimax_m3.py`；技术摘要: 覆盖「[CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic」；主要实现面是 `tests/kernels/attention/test_minimax_m3.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #65577 - [MM] Support mm_device_do_normalize for Gemma 4

- 链接: https://github.com/vllm-project/vllm/pull/65577
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/design/mm_processing.md`, `tests/models/multimodal/generation_ppl_test/gemma.py`, `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/embedding_gemma2.py`, `vllm/model_executor/models/gemma4_mm.py` 等 6 个文件；关联提交 `495c61cfd96f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+114/-16，可读 patch 286 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM] Support mm_device_do_normalize for Gemma 4」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`, `tests/models/multimodal/generation_ppl_test/gemma.py`；技术摘要: 覆盖「[MM] Support mm_device_do_normalize for Gemma 4」；主要实现面是 `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`, `tests/models/multimodal/generation_ppl_test/gemma.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_gemma4.py` modified +75/-0 (75 lines); hunks: -10,6 +10,10; -20,6 +24,7; symbols: test_video_cache_is_independent_of_image_kwargs, pixels, test_mm_device_do_normalize, test_embed_patches_normalizes_channel_last_patches，涉及 `test_video_cache_is_independent_of_image_kwargs, pixels, test_mm_device_do_normalize`；`vllm/model_executor/models/gemma4_mm.py` modified +26/-16 (42 lines); hunks: -39,6 +39,7; -1049,6 +1050,7 @@ class Gemma4ForConditionalGeneration(; symbols: Gemma4ForConditionalGeneration, __init__, _encoder_chunk, _embed_patches，涉及 `Gemma4ForConditionalGeneration, __init__, _encoder_chunk`；`tests/models/multimodal/generation_ppl_test/gemma.py` modified +3/-0 (3 lines); hunks: -12,6 +12,9；`vllm/model_executor/models/embedding_gemma2.py` modified +3/-0 (3 lines); hunks: -24,6 +24,7; -1011,6 +1012,7 @@ class EmbeddingGemma2Model(nn.Module, SupportsMultiModal,...; symbols: EmbeddingGemma2Model, __init__，涉及 `EmbeddingGemma2Model, __init__`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_gemma4.py` modified +75/-0 (75 lines); hunks: -10,6 +10,10; -20,6 +24,7; symbols: test_video_cache_is_independent_of_image_kwargs, pixels, test_mm_device_do_normalize, test_embed_patches_normalizes_channel_last_patches
  - `vllm/model_executor/models/gemma4_mm.py` modified +26/-16 (42 lines); hunks: -39,6 +39,7; -1049,6 +1050,7 @@ class Gemma4ForConditionalGeneration(; symbols: Gemma4ForConditionalGeneration, __init__, _encoder_chunk, _embed_patches
  - `tests/models/multimodal/generation_ppl_test/gemma.py` modified +3/-0 (3 lines); hunks: -12,6 +12,9
  - `vllm/model_executor/models/embedding_gemma2.py` modified +3/-0 (3 lines); hunks: -24,6 +24,7; -1011,6 +1012,7 @@ class EmbeddingGemma2Model(nn.Module, SupportsMultiModal,...; symbols: EmbeddingGemma2Model, __init__
  - `vllm/model_executor/models/gemma4_unified.py` modified +3/-0 (3 lines); hunks: -239,6 +239,9 @@ class Gemma4UnifiedForConditionalGeneration(Gemma4ForConditi...; symbols: Gemma4UnifiedForConditionalGeneration
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/processing/test_gemma4.py
@@ -10,6 +10,10 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import (
+    FusedMMInputNorm,
+    build_mm_input_norm,
+)
@@ -20,6 +24,7 @@
+from vllm.platforms import current_platform
diff -- vllm/model_executor/models/gemma4_mm.py
@@ -39,6 +39,7 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
@@ -1049,6 +1050,7 @@ class Gemma4ForConditionalGeneration(
+    supports_mm_device_do_normalize = True
@@ -1100,6 +1102,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
+            self.vision_input_norm = build_mm_input_norm(vllm_config.model_config)
@@ -1299,6 +1302,23 @@ def _encoder_chunk(
diff -- tests/models/multimodal/generation_ppl_test/gemma.py
@@ -12,6 +12,9 @@
```

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_gemma4.py` modified +75/-0; `tests/models/multimodal/generation_ppl_test/gemma.py` modified +3/-0
  - runtime: `vllm/model_executor/models/gemma4_mm.py` modified +26/-16; `vllm/model_executor/models/embedding_gemma2.py` modified +3/-0; `vllm/model_executor/models/gemma4_unified.py` modified +3/-0
  - docs: `docs/design/mm_processing.md` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation_ppl_test/gemma.py`, `tests/models/multimodal/processing/test_gemma4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65552 - [CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype

- 链接: https://github.com/vllm-project/vllm/pull/65552
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`；关联提交 `19e3cfb4f8bf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`；技术摘要: 覆盖「[CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype」；主要实现面是 `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0 (1 lines); hunks: -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):; symbols: _Mxfp8Linear, __init__，涉及 `_Mxfp8Linear, __init__`。
- 代码 diff 细节:
  - `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0 (1 lines); hunks: -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):; symbols: _Mxfp8Linear, __init__
- 关键代码摘录:

```diff
diff -- tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py
@@ -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):
+        self.params_dtype = torch.bfloat16
```

- 已读文件:
  - tests: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65542 - [Kernel] Marlin: remove 8-bit (INT8/FP8) activation support, rely on Humming

- 链接: https://github.com/vllm-project/vllm/pull/65542
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `CMakeLists.txt`, `benchmarks/kernels/benchmark_machete.py`, `benchmarks/kernels/benchmark_marlin.py`, `docs/features/quantization/README.md`, `tests/config/test_config_generation.py` 等 37 个文件；关联提交 `ff9b7d3ae3ab`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 52 个文件，+489/-2531，可读 patch 6473 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Marlin: remove 8-bit (INT8/FP8) activation support, rely on Humming」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_test.py`；技术摘要: 覆盖「[Kernel] Marlin: remove 8-bit (INT8/FP8) activation support, rely on Humming」；主要实现面是 `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_test.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` modified +7/-119 (126 lines); hunks: -35,7 +35,6; -372,8 +371,6 @@ def make_wna16_moe_quant_config(; symbols: make_wna16_moe_quant_config, _process_weights_flashinfer，涉及 `make_wna16_moe_quant_config, _process_weights_flashinfer`；`vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py` modified +17/-98 (115 lines); hunks: -9,14 +9,12; -124,21 +122,12 @@ def nvfp4_marlin_process_scales(; symbols: nvfp4_marlin_process_scales, mxfp4_marlin_process_scales, nvfp4_marlin_process_global_scale, apply_fp4_marlin_linear，涉及 `nvfp4_marlin_process_scales, mxfp4_marlin_process_scales, nvfp4_marlin_process_global_scale`；`vllm/model_executor/layers/quantization/utils/marlin_utils_test.py` modified +29/-83 (112 lines); hunks: -5,8 +5,7; -29,19 +28,13 @@ def __init__(self, out_features, min_thread_n, max_parallel):; symbols: __init__, marlin_permute_weights, marlin_weights，涉及 `__init__, marlin_permute_weights, marlin_weights`；`vllm/model_executor/layers/quantization/utils/marlin_utils.py` modified +10/-91 (101 lines); hunks: -13,11 +13,6; -442,7 +437,6 @@ def _marlin_gemm(; symbols: _marlin_gemm, _marlin_gemm_fake, get_scale_perms，涉及 `_marlin_gemm, _marlin_gemm_fake, get_scale_perms`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` modified +7/-119 (126 lines); hunks: -35,7 +35,6; -372,8 +371,6 @@ def make_wna16_moe_quant_config(; symbols: make_wna16_moe_quant_config, _process_weights_flashinfer
  - `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py` modified +17/-98 (115 lines); hunks: -9,14 +9,12; -124,21 +122,12 @@ def nvfp4_marlin_process_scales(; symbols: nvfp4_marlin_process_scales, mxfp4_marlin_process_scales, nvfp4_marlin_process_global_scale, apply_fp4_marlin_linear
  - `vllm/model_executor/layers/quantization/utils/marlin_utils_test.py` modified +29/-83 (112 lines); hunks: -5,8 +5,7; -29,19 +28,13 @@ def __init__(self, out_features, min_thread_n, max_parallel):; symbols: __init__, marlin_permute_weights, marlin_weights
  - `vllm/model_executor/layers/quantization/utils/marlin_utils.py` modified +10/-91 (101 lines); hunks: -13,11 +13,6; -442,7 +437,6 @@ def _marlin_gemm(; symbols: _marlin_gemm, _marlin_gemm_fake, get_scale_perms
  - `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py` modified +1/-63 (64 lines); hunks: -35,10 +35,8; -78,8 +76,6 @@ def _fused_marlin_moe(; symbols: _fused_marlin_moe, fused_marlin_moe
- 关键代码摘录:

```diff
diff -- vllm/model_executor/layers/fused_moe/oracle/int_wna16.py
@@ -35,7 +35,6 @@
-    marlin_act_int8_process_scales,
@@ -372,8 +371,6 @@ def make_wna16_moe_quant_config(
-    a1_gscale: torch.Tensor | None = None,
-    a2_gscale: torch.Tensor | None = None,
@@ -388,8 +385,6 @@ def make_wna16_moe_quant_config(
-            a1_gscale=a1_gscale,
diff -- vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py
@@ -9,14 +9,12 @@
-    get_marlin_input_dtype,
-    marlin_quant_input,
@@ -124,21 +122,12 @@ def nvfp4_marlin_process_scales(
-def mxfp4_marlin_process_scales(marlin_scales, input_dtype=None):
+def mxfp4_marlin_process_scales(marlin_scales):
-    if input_dtype is None or input_dtype.itemsize == 2:
diff -- vllm/model_executor/layers/quantization/utils/marlin_utils_test.py
@@ -5,8 +5,7 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` modified +7/-119; `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py` modified +17/-98; `vllm/model_executor/layers/quantization/utils/marlin_utils_test.py` modified +29/-83; `vllm/model_executor/layers/quantization/utils/marlin_utils.py` modified +10/-91; `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py` modified +1/-63; `vllm/model_executor/layers/quantization/utils/marlin_utils_fp8.py` modified +4/-30
- 验证与风险: diff 自带测试面 `tests/config/test_config_generation.py`, `tests/kernels/moe/test_marlin_vs_trtllm_mxint4.py`, `tests/kernels/moe/test_moe.py`, `tests/kernels/quantization/test_marlin_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65537 - [MiniMax-M3] Support sequence parallelism with pipeline parallelism

- 链接: https://github.com/vllm-project/vllm/pull/65537
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `213e64562ba6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+13/-3，可读 patch 44 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MiniMax-M3] Support sequence parallelism with pipeline parallelism」；模型线: Shared Framework PRs；类别: 模型支持/运行时入口；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[MiniMax-M3] Support sequence parallelism with pipeline parallelism」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #64583 - [Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode

- 链接: https://github.com/vllm-project/vllm/pull/64583
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；关联提交 `75f67614971a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+48/-23，可读 patch 110 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`；技术摘要: 覆盖「[Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode」；主要实现面是 `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #65449 - [Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state

- 链接: https://github.com/vllm-project/vllm/pull/65449
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`；关联提交 `20d7dd9ac152`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+45/-5，可读 patch 122 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`；技术摘要: 覆盖「[Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state」；主要实现面是 `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5 (42 lines); hunks: -1,12 +1,15; -77,16 +80,14 @@ def make_vllm_config(; symbols: make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs，涉及 `make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs`；`vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0 (8 lines); hunks: -20,6 +20,7; -31,6 +32,7; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5 (42 lines); hunks: -1,12 +1,15; -77,16 +80,14 @@ def make_vllm_config(; symbols: make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0 (8 lines); hunks: -20,6 +20,7; -31,6 +32,7; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/model_executor/test_mistral_large_3_eagle.py
@@ -1,12 +1,15 @@
+from pathlib import Path
+from transformers import DeepseekV2Config
+from vllm.config import ModelConfig, ParallelConfig, VllmConfig, set_current_vllm_config
@@ -77,16 +80,14 @@ def make_vllm_config(
-        parallel_config=SimpleNamespace(
-            eplb_config=SimpleNamespace(num_redundant_experts=0),
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -20,6 +20,7 @@
+    DeepseekV2MoE,
@@ -31,6 +32,7 @@
+    get_fused_shared_expert_layers,
@@ -60,6 +62,7 @@ def __init__(
+        self.hidden_size = config.hidden_size
@@ -81,6 +84,11 @@ def __init__(
```

- 已读文件:
  - tests: `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0
- 验证与风险: diff 自带测试面 `tests/model_executor/test_mistral_large_3_eagle.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65432 - [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP

- 链接: https://github.com/vllm-project/vllm/pull/65432
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/models/minimax_m3/amd/indexer_nvfp4.py`；关联提交 `ca8bd4c05506`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+28/-0，可读 patch 53 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP」；主要实现面是 `vllm/models/minimax_m3/amd/indexer_nvfp4.py`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`；技术摘要: 覆盖「[ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer」；主要实现面是 `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #64723 - [Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant

- 链接: https://github.com/vllm-project/vllm/pull/64723
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`；关联提交 `523991fec066`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+424/-46，可读 patch 547 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`；技术摘要: 覆盖「[Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant」；主要实现面是 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _worker, make_linear, run_one, test_forward_fused，涉及 `_worker, make_linear, run_one`；`vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: _get_workspace, fused_allreduce_gemma_rms_norm_quant，涉及 `_get_workspace, fused_allreduce_gemma_rms_norm_quant`；`vllm/models/qwen3_5/nvidia/model.py` modified +69/-46 (115 lines); hunks: -125,6 +125,7; -179,13 +180,21 @@ class Qwen3_5RMSNorm(nn.Module):; symbols: Qwen3_5RMSNorm, __init__, forward，涉及 `Qwen3_5RMSNorm, __init__, forward`。
- 代码 diff 细节:
  - `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _worker, make_linear, run_one, test_forward_fused
  - `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: _get_workspace, fused_allreduce_gemma_rms_norm_quant
  - `vllm/models/qwen3_5/nvidia/model.py` modified +69/-46 (115 lines); hunks: -125,6 +125,7; -179,13 +180,21 @@ class Qwen3_5RMSNorm(nn.Module):; symbols: Qwen3_5RMSNorm, __init__, forward
- 关键代码摘录:

```diff
diff -- tests/models/qwen3_5/test_fused_allreduce_norm_quant.py
@@ -0,0 +1,186 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""TP2: ``Qwen3_5RMSNorm.forward_fused`` vs the unfused chain it replaces,
+(all-reduce +) Gemma norm, then scaled_fp8_quant / scaled_fp4_quant, for real
+ModelOpt static FP8 and NVFP4 consumers.
+All cases run in one 2-rank spawn; spawning per case re-imports vLLM and
diff -- vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py
@@ -0,0 +1,167 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""TP all-reduce + residual add + Gemma RMSNorm + consumer input quant.
+Calls FlashInfer's ``kARResidualRMSNormOut{FP8,FP4}Quant`` patterns directly
+(no torch.compile custom op). The kernel writes the bf16 normed activation
+(GDN's ``in_proj_ba`` reads it) next to the static FP8 / NVFP4 codes; its
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -125,6 +125,7 @@
```

- 已读文件:
  - tests: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0
  - runtime: `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0; `vllm/models/qwen3_5/nvidia/model.py` modified +69/-46
- 验证与风险: diff 自带测试面 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65496 - [Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism

- 链接: https://github.com/vllm-project/vllm/pull/65496
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `cc329910bd2e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-2，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #65030 - [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes

- 链接: https://github.com/vllm-project/vllm/pull/65030
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`；关联提交 `0eeae6a47333`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+71/-54，可读 patch 188 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`；技术摘要: 覆盖「[Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes」；主要实现面是 `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v4/common/vision.py` modified +53/-0 (53 lines); hunks: -39,6 +39,7; -393,6 +394,58 @@ def forward_packed(; symbols: _compute_vision_cos_sin, forward_packed, encode_images, run_dp_sharded_vision_tower，涉及 `_compute_vision_cos_sin, forward_packed, encode_images`；`vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34 (44 lines); hunks: -48,7 +48,7; -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object)...; symbols: _make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image, _process_image_input，涉及 `_make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image`；`vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -238,16 +239,9 @@ def _process_image_input(; symbols: _process_image_input，涉及 `_process_image_input`；`vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -220,16 +221,9 @@ def _process_image_input(; symbols: _process_image_input，涉及 `_process_image_input`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v4/common/vision.py` modified +53/-0 (53 lines); hunks: -39,6 +39,7; -393,6 +394,58 @@ def forward_packed(; symbols: _compute_vision_cos_sin, forward_packed, encode_images, run_dp_sharded_vision_tower
  - `vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34 (44 lines); hunks: -48,7 +48,7; -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object)...; symbols: _make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image, _process_image_input
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -238,16 +239,9 @@ def _process_image_input(; symbols: _process_image_input
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -220,16 +221,9 @@ def _process_image_input(; symbols: _process_image_input
- 关键代码摘录:

```diff
diff -- vllm/models/deepseek_v4/common/vision.py
@@ -39,6 +39,7 @@
+from vllm.v1.attention.backends.registry import AttentionBackendEnum
@@ -393,6 +394,58 @@ def forward_packed(
+def encode_images(
+    vision_model: DeepseekV4ViT,
+    aligner: DeepseekV4Aligner,
+    patches: torch.Tensor,
diff -- vllm/models/deepseek_v4/common/vl_model.py
@@ -48,7 +48,7 @@
-from .vision import DeepseekV4Aligner, DeepseekV4ViT
+from .vision import DeepseekV4Aligner, DeepseekV4ViT, encode_images
@@ -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object) -> dict | None:
-    def _encode_image(
-        self,
-        patches: torch.Tensor,
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -39,6 +39,7 @@
```

- 已读文件:
  - runtime: `vllm/models/deepseek_v4/common/vision.py` modified +53/-0; `vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34; `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10
- 验证与风险: runtime 路径改动集中在 `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #65174 - [Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig

- 链接: https://github.com/vllm-project/vllm/pull/65174
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/configs/kimi_vl.py`；关联提交 `2173d7121fc6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/transformers_utils/configs/kimi_vl.py`；技术摘要: 覆盖「[Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig」；主要实现面是 `vllm/transformers_utils/configs/kimi_vl.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #65296 - [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters

- 链接: https://github.com/vllm-project/vllm/pull/65296
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`；关联提交 `22d05b87bbc9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+18/-11，可读 patch 84 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters」；模型线: Shared Framework PRs；类别: 模型实现调整；主要 diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`；技术摘要: 覆盖「[Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters」；主要实现面是 `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8 (22 lines); hunks: -17,6 +17,7; -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:; symbols: prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a, prepare_compressor_gemm_fusion，涉及 `prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a`；`vllm/models/deepseek_v4/amd/model.py` modified +4/-3 (7 lines); hunks: -73,7 +73,7; -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward，涉及 `prepare_gateup_preshuffle, forward`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8 (22 lines); hunks: -17,6 +17,7; -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:; symbols: prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a, prepare_compressor_gemm_fusion
  - `vllm/models/deepseek_v4/amd/model.py` modified +4/-3 (7 lines); hunks: -73,7 +73,7; -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward
- 关键代码摘录:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -17,6 +17,7 @@
+from vllm.model_executor.utils import refill_derived, replace_parameter
@@ -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:
-        from vllm.model_executor.utils import replace_parameter
@@ -1122,10 +1122,13 @@ def _prep(linear) -> torch.Tensor | None:
-            return ws
+            # A plain tensor: assigning the scale Parameter itself would register
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -73,7 +73,7 @@
-from vllm.model_executor.utils import refill_derived
+from vllm.model_executor.utils import refill_derived, replace_parameter
@@ -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:
-        from vllm.model_executor.utils import replace_parameter
@@ -173,7 +172,9 @@ def prepare_gateup_preshuffle(self) -> None:
-        self._gateup_scale = ws
```

- 已读文件:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8; `vllm/models/deepseek_v4/amd/model.py` modified +4/-3
- 验证与风险: runtime 路径改动集中在 `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #64974 - [Refactor][DSv4.1] Remove duplicated code

- 链接: https://github.com/vllm-project/vllm/pull/64974
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/attention/test_flashinfer_sparse_mla_sm120_api.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/attention.py` 等 9 个文件；关联提交 `45d0ac9ee197`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+57/-328，可读 patch 737 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor][DSv4.1] Remove duplicated code」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py`；技术摘要: 覆盖「[Refactor][DSv4.1] Remove duplicated code」；主要实现面是 `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159 (170 lines); hunks: -30,6 +30,10; -56,131 +60,6; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices, _hf_config_int，涉及 `quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices`；`vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67 (80 lines); hunks: -9,6 +9,12; -33,72 +39,12; symbols: _get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads, _required_sm120_sparse_topk，涉及 `_get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads`；`vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41 (45 lines); hunks: -54,7 +54,6; -76,13 +75,14; symbols: _make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters, update_physical_experts_metadata，涉及 `_make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters`；`vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23 (32 lines); hunks: -806,17 +806,6 @@ def combine_topk_swa_indices(; -960,12 +949,9 @@ def dispatch( # type: ignore[override]; symbols: combine_topk_swa_indices, _hf_config_int, _scheduler_config_int, CombineTopkSwaIndicesKernel，涉及 `combine_topk_swa_indices, _hf_config_int, _scheduler_config_int`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159 (170 lines); hunks: -30,6 +30,10; -56,131 +60,6; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices, _hf_config_int
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67 (80 lines); hunks: -9,6 +9,12; -33,72 +39,12; symbols: _get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads, _required_sm120_sparse_topk
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41 (45 lines); hunks: -54,7 +54,6; -76,13 +75,14; symbols: _make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters, update_physical_experts_metadata
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23 (32 lines); hunks: -806,17 +806,6 @@ def combine_topk_swa_indices(; -960,12 +949,9 @@ def dispatch( # type: ignore[override]; symbols: combine_topk_swa_indices, _hf_config_int, _scheduler_config_int, CombineTopkSwaIndicesKernel
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +11/-11 (22 lines); hunks: -47,7 +47,7; -59,7 +59,7 @@ def _get_flashinfer_dsv4_workspace(device: torch.device) -> to...; symbols: _get_flashinfer_dsv4_workspace, get_flashinfer_dsv4_workspace, _packed_block_span, packed_block_span
- 关键代码摘录:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -30,6 +30,10 @@
+from vllm.models.deepseek_v4.common.ops.cache_utils import (
+    quantize_and_insert_k_kernel,
+    remap_flashinfer_index,
+)
@@ -56,131 +60,6 @@
-@triton.jit
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -9,6 +9,12 @@
+from vllm.models.deepseek_v4.nvidia.flashinfer_sparse import (
+    get_flashinfer_dsv4_workspace,
+    packed_block_span,
+    pad_to_supported_q_heads,
+    required_sm120_sparse_topk,
+)
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -54,7 +54,6 @@
```

- 已读文件:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67; `vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23; `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +11/-11; `vllm/models/deepseek_v41/attention.py` modified +2/-20
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_flashinfer_sparse_mla_sm120_api.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65226 - [Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences

- 链接: https://github.com/vllm-project/vllm/pull/65226
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/minimax_m3/common/encoder_cudagraph.py`；关联提交 `9a519c0585b6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-19，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/models/minimax_m3/common/encoder_cudagraph.py`；技术摘要: 覆盖「[Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences」；主要实现面是 `vllm/models/minimax_m3/common/encoder_cudagraph.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #65118 - [Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path

- 链接: https://github.com/vllm-project/vllm/pull/65118
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`；关联提交 `3fbc8d8b4fe0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-5，可读 patch 52 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`；技术摘要: 覆盖「[Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path」；主要实现面是 `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/parser/mistral/test_tool_calls.py` modified +23/-0 (23 lines); hunks: -38,6 +38,7; -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(; symbols: test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens，涉及 `test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens`；`vllm/parser/mistral.py` modified +3/-5 (8 lines); hunks: -396,11 +396,9 @@ def adjust_request(; symbols: adjust_request，涉及 `adjust_request`。
- 代码 diff 细节:
  - `tests/parser/mistral/test_tool_calls.py` modified +23/-0 (23 lines); hunks: -38,6 +38,7; -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(; symbols: test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens
  - `vllm/parser/mistral.py` modified +3/-5 (8 lines); hunks: -396,11 +396,9 @@ def adjust_request(; symbols: adjust_request
- 关键代码摘录:

```diff
diff -- tests/parser/mistral/test_tool_calls.py
@@ -38,6 +38,7 @@
+from vllm.entrypoints.openai.responses.protocol import ResponsesRequest
@@ -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(
+@pytest.mark.parametrize("responses", [True, False])
+def test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens(
+    mistral_tool_parser: MistralToolParser, responses: bool
+) -> None:
diff -- vllm/parser/mistral.py
@@ -396,11 +396,9 @@ def adjust_request(
-            request = super().adjust_request(request)
-            if request.tools and request.tool_choice != "none":
-                # Keep special tokens so the [TOOL_CALLS] marker
-                # survives for tool detection.
-                request.skip_special_tokens = False
+            # MistralTokenizer keeps the parser's special tokens when skipping.
```

- 已读文件:
  - tests: `tests/parser/mistral/test_tool_calls.py` modified +23/-0
  - runtime: `vllm/parser/mistral.py` modified +3/-5
- 验证与风险: diff 自带测试面 `tests/parser/mistral/test_tool_calls.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64815 - [Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel

- 链接: https://github.com/vllm-project/vllm/pull/64815
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/fusion/test_quant_activation_contract.py`, `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`；关联提交 `b5814faa25cf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+42/-7，可读 patch 129 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`；技术摘要: 覆盖「[Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel」；主要实现面是 `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/kernels/linear/mxfp8/pytorch.py` modified +28/-5 (33 lines); hunks: -3,12 +3,20; -37,6 +45,10 @@ def is_supported(; symbols: is_supported, can_implement, input_quant_key, process_weights_after_loading，涉及 `is_supported, can_implement, input_quant_key`；`vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1 (9 lines); hunks: -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -...; symbols: can_fuse_query_quant，涉及 `can_fuse_query_quant`；`vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1 (4 lines); hunks: -10,6 +10,7; -38,7 +39,8 @@ def _can_fuse_wo_a(layer: nn.Module) -> bool:; symbols: _can_fuse_wo_a，涉及 `_can_fuse_wo_a`；`tests/fusion/test_quant_activation_contract.py` modified +3/-0 (3 lines); hunks: -16,6 +16,7; -73,6 +74,8; symbols: _all_kernel_classes，涉及 `_all_kernel_classes`。
- 代码 diff 细节:
  - `vllm/model_executor/kernels/linear/mxfp8/pytorch.py` modified +28/-5 (33 lines); hunks: -3,12 +3,20; -37,6 +45,10 @@ def is_supported(; symbols: is_supported, can_implement, input_quant_key, process_weights_after_loading
  - `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1 (9 lines); hunks: -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -...; symbols: can_fuse_query_quant
  - `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1 (4 lines); hunks: -10,6 +10,7; -38,7 +39,8 @@ def _can_fuse_wo_a(layer: nn.Module) -> bool:; symbols: _can_fuse_wo_a
  - `tests/fusion/test_quant_activation_contract.py` modified +3/-0 (3 lines); hunks: -16,6 +16,7; -73,6 +74,8; symbols: _all_kernel_classes
- 关键代码摘录:

```diff
diff -- vllm/model_executor/kernels/linear/mxfp8/pytorch.py
@@ -3,12 +3,20 @@
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
+    as_quantized_activation,
+)
+from vllm.model_executor.layers.quantization.utils.quant_utils import (
+    QuantKey,
diff -- vllm/models/deepseek_v41/common/ops/query_quant.py
@@ -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -> bool:
+    from vllm.model_executor.kernels.linear.mxfp8.pytorch import (
+        TorchMxFp8LinearKernel,
+    )
-        in (FlashInferCutedslMxfp8LinearKernel, FlashInferCutlassMxfp8LinearKernel)
+        in (
+            FlashInferCutedslMxfp8LinearKernel,
diff -- vllm/models/deepseek_v41/nvidia/ops/o_proj.py
@@ -10,6 +10,7 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/kernels/linear/mxfp8/pytorch.py` modified +28/-5; `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1
  - tests: `tests/fusion/test_quant_activation_contract.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/fusion/test_quant_activation_contract.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64984 - [Bugfix][MM] Keep FlashInfer cu_seqlens halves aligned in Qwen3-VL encoder CUDA graph replay

- 链接: https://github.com/vllm-project/vllm/pull/64984
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/qwen3_vl.py`；关联提交 `45fc9fd0485d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+108/-0，可读 patch 133 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MM] Keep FlashInfer cu_seqlens halves aligned in Qwen3-VL encoder CUDA graph replay」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_vl.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`；技术摘要: 覆盖「[Bugfix][MM] Keep FlashInfer cu_seqlens halves aligned in Qwen3-VL encoder CUDA graph replay」；主要实现面是 `vllm/model_executor/models/qwen3_vl.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_vl.py` modified +16/-0 (16 lines); hunks: -120,6 +120,7; -144,6 +145,8; symbols: get_encoder_cudagraph_config，涉及 `get_encoder_cudagraph_config`；`tests/v1/cudagraph/test_encoder_cudagraph.py` modified +92/-0 (92 lines); hunks: -1522,3 +1522,95 @@ def test_user_budgets_negative_raises(self):; symbols: test_user_budgets_negative_raises, TestFlashInferCuSeqlensPadding, _cu_seqlens, _qwen3_vl_padding_fn，涉及 `test_user_budgets_negative_raises, TestFlashInferCuSeqlensPadding, _cu_seqlens`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_vl.py` modified +16/-0 (16 lines); hunks: -120,6 +120,7; -144,6 +145,8; symbols: get_encoder_cudagraph_config
  - `tests/v1/cudagraph/test_encoder_cudagraph.py` modified +92/-0 (92 lines); hunks: -1522,3 +1522,95 @@ def test_user_budgets_negative_raises(self):; symbols: test_user_budgets_negative_raises, TestFlashInferCuSeqlensPadding, _cu_seqlens, _qwen3_vl_padding_fn
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_vl.py
@@ -120,6 +120,7 @@
+from vllm.v1.attention.backends.registry import AttentionBackendEnum
@@ -144,6 +145,8 @@
+    _pad_cumulative_seqlens_buffer,
+    _pad_flashinfer_cu_seqlens_buffer,
@@ -2146,6 +2149,19 @@ def get_encoder_cudagraph_config(self):
+            # FlashInfer packs the q/k/o and v offsets into one cu_seqlens
diff -- tests/v1/cudagraph/test_encoder_cudagraph.py
@@ -1522,3 +1522,95 @@ def test_user_budgets_negative_raises(self):
+# ---------------------------------------------------------------------------
+# FlashInfer cu_seqlens replay padding (no GPU required)
+# ---------------------------------------------------------------------------
+class TestFlashInferCuSeqlensPadding:
+    """A replay pads its cu_seqlens into the buffer captured at a larger batch
+    size. The padded buffer must equal the cu_seqlens computed for the same
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_vl.py` modified +16/-0
  - tests: `tests/v1/cudagraph/test_encoder_cudagraph.py` modified +92/-0
- 验证与风险: diff 自带测试面 `tests/v1/cudagraph/test_encoder_cudagraph.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64734 - [ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s

- 链接: https://github.com/vllm-project/vllm/pull/64734
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml`；关联提交 `a708b0f639ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml`；技术摘要: 覆盖「[ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s」；主要实现面是 `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"；`tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"
  - `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml
@@ -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"
-startup_max_wait_seconds: 1200
+startup_max_wait_seconds: 1800
diff -- tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml
@@ -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-V3.2"
-startup_max_wait_seconds: 1200
+startup_max_wait_seconds: 1800
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml` modified +1/-1; `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64852 - [Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8

- 链接: https://github.com/vllm-project/vllm/pull/64852
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`；关联提交 `318c4db661d9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+336/-3，可读 patch 367 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8」；主要实现面是 `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`, `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 反查来源: `git log --name-only -- <model-files>` 反查到 `benchmarks/kernels/benchmark_gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `vllm/models/minimax_m3/nvidia/model.py`；关联提交 `37e16689fa4c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+229/-20，可读 patch 559 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/minimax_m3/nvidia/model.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py`；技术摘要: 覆盖「[Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE」；主要实现面是 `vllm/models/minimax_m3/nvidia/model.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14 (190 lines); hunks: -13,6 +13,7; -111,6 +112,7; symbols: _supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel, _maybe_init_gemm_rs，涉及 `_supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel`；`vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py` modified +20/-5 (25 lines); hunks: -41,7 +41,12; -984,7 +989,9 @@ def should_run(self, x: torch.Tensor) -> bool:; symbols: should_run, apply，涉及 `should_run, apply`；`tests/kernels/test_gemm_rs_ar.py` modified +25/-0 (25 lines); hunks: -165,6 +165,31 @@ def _run_mode(; symbols: _run_mode，涉及 `_run_mode`；`benchmarks/kernels/benchmark_gemm_rs_ar.py` modified +8/-1 (9 lines); hunks: -18,6 +18,11; -45,10 +50,12。
- 代码 diff 细节:
  - `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14 (190 lines); hunks: -13,6 +13,7; -111,6 +112,7; symbols: _supports_qkv_fused_epilogue, _use_mega_moe, _use_sequence_parallel, _maybe_init_gemm_rs
  - `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py` modified +20/-5 (25 lines); hunks: -41,7 +41,12; -984,7 +989,9 @@ def should_run(self, x: torch.Tensor) -> bool:; symbols: should_run, apply
  - `tests/kernels/test_gemm_rs_ar.py` modified +25/-0 (25 lines); hunks: -165,6 +165,31 @@ def _run_mode(; symbols: _run_mode
  - `benchmarks/kernels/benchmark_gemm_rs_ar.py` modified +8/-1 (9 lines); hunks: -18,6 +18,11; -45,10 +50,12
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
diff -- vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py
@@ -41,7 +41,12 @@
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
+    as_quantized_activation,
+)
+from vllm.model_executor.layers.quantization.utils.quant_utils import kMxfp8Dynamic
@@ -984,7 +989,9 @@ def should_run(self, x: torch.Tensor) -> bool:
diff -- tests/kernels/test_gemm_rs_ar.py
@@ -165,6 +165,31 @@ def _run_mode(
```

- 已读文件:
  - runtime: `vllm/models/minimax_m3/nvidia/model.py` modified +176/-14; `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py` modified +20/-5
  - tests: `tests/kernels/test_gemm_rs_ar.py` modified +25/-0
  - other: `benchmarks/kernels/benchmark_gemm_rs_ar.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/kernels/test_gemm_rs_ar.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64971 - [Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages

- 链接: https://github.com/vllm-project/vllm/pull/64971
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/entrypoints/anthropic/serving.py`, `vllm/tokenizers/deepseek_v41.py`；关联提交 `c215f1483524`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+150/-11，可读 patch 224 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/entrypoints/scale_out/render/test_render.py`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/tokenizers_/test_deepseek_v41.py`；技术摘要: 覆盖「[Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages」；主要实现面是 `tests/entrypoints/scale_out/render/test_render.py`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/tokenizers_/test_deepseek_v41.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/entrypoints/scale_out/render/test_render.py` modified +86/-0 (86 lines); hunks: -40,6 +40,7; -1081,3 +1082,88 @@ async def test_tokenize_matches_chat_render_for_gpt_oss(g...; symbols: test_tokenize_matches_chat_render_for_gpt_oss, deepseek_v41_server, test_messages_render_tool_search_result_for_deepseek_v41，涉及 `test_tokenize_matches_chat_render_for_gpt_oss, deepseek_v41_server, test_messages_render_tool_search_result_for_deepseek_v41`；`tests/entrypoints/anthropic/test_anthropic_messages_conversion.py` modified +31/-0 (31 lines); hunks: -405,6 +405,37 @@ def test_tool_result_with_multiple_images(self):; symbols: test_tool_result_with_multiple_images, test_tool_result_with_tool_references, test_tool_result_none_content，涉及 `test_tool_result_with_multiple_images, test_tool_result_with_tool_references, test_tool_result_none_content`；`tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():; symbols: test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media，涉及 `test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media`；`vllm/entrypoints/anthropic/serving.py` modified +8/-10 (18 lines); hunks: -657,11 +657,18 @@ def _convert_user_tool_result(; -676,15 +683,6 @@ def _convert_user_tool_result(; symbols: _convert_user_tool_result, _build_base_request，涉及 `_convert_user_tool_result, _build_base_request`。
- 代码 diff 细节:
  - `tests/entrypoints/scale_out/render/test_render.py` modified +86/-0 (86 lines); hunks: -40,6 +40,7; -1081,3 +1082,88 @@ async def test_tokenize_matches_chat_render_for_gpt_oss(g...; symbols: test_tokenize_matches_chat_render_for_gpt_oss, deepseek_v41_server, test_messages_render_tool_search_result_for_deepseek_v41
  - `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py` modified +31/-0 (31 lines); hunks: -405,6 +405,37 @@ def test_tool_result_with_multiple_images(self):; symbols: test_tool_result_with_multiple_images, test_tool_result_with_tool_references, test_tool_result_none_content
  - `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():; symbols: test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media
  - `vllm/entrypoints/anthropic/serving.py` modified +8/-10 (18 lines); hunks: -657,11 +657,18 @@ def _convert_user_tool_result(; -676,15 +683,6 @@ def _convert_user_tool_result(; symbols: _convert_user_tool_result, _build_base_request
  - `vllm/tokenizers/deepseek_v41.py` modified +7/-1 (8 lines); hunks: -29,7 +29,7 @@ def _normalize_messages(; -54,12 +54,18 @@ def _normalize_messages(; symbols: _normalize_messages
- 关键代码摘录:

```diff
diff -- tests/entrypoints/scale_out/render/test_render.py
@@ -40,6 +40,7 @@
+DEEPSEEK_V41_MODEL_NAME = "deepseek-ai/DeepSeek-V4.1-Flash"
@@ -1081,3 +1082,88 @@ async def test_tokenize_matches_chat_render_for_gpt_oss(gpt_oss_server):
+@pytest.fixture(scope="module")
+def deepseek_v41_server():
+    args = [
+        "--tokenizer-mode",
diff -- tests/entrypoints/anthropic/test_anthropic_messages_conversion.py
@@ -405,6 +405,37 @@ def test_tool_result_with_multiple_images(self):
+    def test_tool_result_with_tool_references(self):
+        """A tool_result with tool_reference items stays one tool message, with
+        the references first, so templates pair one result with one call."""
+        request = self._make_tool_result_request(
+            [
+                {"type": "text", "text": "2 tools found"},
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():
```

- 已读文件:
  - tests: `tests/entrypoints/scale_out/render/test_render.py` modified +86/-0; `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py` modified +31/-0; `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0
  - runtime: `vllm/entrypoints/anthropic/serving.py` modified +8/-10; `vllm/tokenizers/deepseek_v41.py` modified +7/-1
- 验证与风险: diff 自带测试面 `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `tests/tokenizers_/test_deepseek_v41.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64944 - [Model] Nemotron-3.5-Transcribe: pack the audio tower's valid frames for MMEncoderAttention

- 链接: https://github.com/vllm-project/vllm/pull/64944
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `vllm/model_executor/models/nemotron3_5_transcribe_audio.py`；关联提交 `dfe4a3025d89`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+216/-33，可读 patch 392 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Nemotron-3.5-Transcribe: pack the audio tower's valid frames for MMEncoderAttention」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/nemotron3_5_transcribe_audio.py`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `docs/models/supported_models.md`；技术摘要: 覆盖「[Model] Nemotron-3.5-Transcribe: pack the audio tower's valid frames for MMEncoderAttention」；主要实现面是 `vllm/model_executor/models/nemotron3_5_transcribe_audio.py`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `docs/models/supported_models.md`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/nemotron3_5_transcribe_audio.py` modified +137/-32 (169 lines); hunks: -21,15 +21,20; -261,7 +266,26 @@ def forward(; symbols: forward, output_lengths, PackedFrames, MultiHeadAttention，涉及 `forward, output_lengths, PackedFrames`；`tests/models/multimodal/processing/test_nemotron3_5_transcribe.py` modified +72/-1 (73 lines); hunks: -240,9 +240,15 @@ def tiny_tower(dist_init):; -458,3 +464,68 @@ def test_audio_tower_encodes_each_clip_as_if_alone(tiny_tow...; symbols: tiny_tower, test_audio_tower_encodes_each_clip_as_if_alone, test_encoder_packs_each_rows_valid_frames, test_encoder_runs_only_the_valid_frames，涉及 `tiny_tower, test_audio_tower_encodes_each_clip_as_if_alone, test_encoder_packs_each_rows_valid_frames`；`docs/models/supported_models.md` modified +7/-0 (7 lines); hunks: -776,6 +776,13 @@ Speech2Text models trained specifically for Automatic Speec...。
- 代码 diff 细节:
  - `vllm/model_executor/models/nemotron3_5_transcribe_audio.py` modified +137/-32 (169 lines); hunks: -21,15 +21,20; -261,7 +266,26 @@ def forward(; symbols: forward, output_lengths, PackedFrames, MultiHeadAttention
  - `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py` modified +72/-1 (73 lines); hunks: -240,9 +240,15 @@ def tiny_tower(dist_init):; -458,3 +464,68 @@ def test_audio_tower_encodes_each_clip_as_if_alone(tiny_tow...; symbols: tiny_tower, test_audio_tower_encodes_each_clip_as_if_alone, test_encoder_packs_each_rows_valid_frames, test_encoder_runs_only_the_valid_frames
  - `docs/models/supported_models.md` modified +7/-0 (7 lines); hunks: -776,6 +776,13 @@ Speech2Text models trained specifically for Automatic Speec...
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/nemotron3_5_transcribe_audio.py
@@ -21,15 +21,20 @@
+import numpy as np
+from vllm.model_executor.layers.attention.mm_encoder_attention import (
+    MMEncoderAttention,
+)
+from .vision import get_multimodal_config
@@ -261,7 +266,26 @@ def forward(
diff -- tests/models/multimodal/processing/test_nemotron3_5_transcribe.py
@@ -240,9 +240,15 @@ def tiny_tower(dist_init):
+    from vllm.platforms import current_platform
-    tower = Nemotron3_5TranscribeAudioTower(TINY_AUDIO_CONFIG).eval()
+    # vLLM registers the encoder attention ops for the platform's device only.
+    tower = (
+        Nemotron3_5TranscribeAudioTower(TINY_AUDIO_CONFIG)
+        .eval()
diff -- docs/models/supported_models.md
@@ -776,6 +776,13 @@ Speech2Text models trained specifically for Automatic Speech Recognition.
```

- 已读文件:
  - runtime: `vllm/model_executor/models/nemotron3_5_transcribe_audio.py` modified +137/-32
  - tests: `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py` modified +72/-1
  - docs: `docs/models/supported_models.md` modified +7/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #65008 - [CI] Lower gpu_memory_utilization in test_gemma4_lora

- 链接: https://github.com/vllm-project/vllm/pull/65008
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/lora/test_gemma4_tp.py`；关联提交 `08e3f264583e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Lower gpu_memory_utilization in test_gemma4_lora」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `tests/lora/test_gemma4_tp.py`；技术摘要: 覆盖「[CI] Lower gpu_memory_utilization in test_gemma4_lora」；主要实现面是 `tests/lora/test_gemma4_tp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/lora/test_gemma4_tp.py` modified +1/-0 (1 lines); hunks: -62,6 +62,7 @@ def test_gemma4_lora(gemma4_vision_lora_files):; symbols: test_gemma4_lora，涉及 `test_gemma4_lora`。
- 代码 diff 细节:
  - `tests/lora/test_gemma4_tp.py` modified +1/-0 (1 lines); hunks: -62,6 +62,7 @@ def test_gemma4_lora(gemma4_vision_lora_files):; symbols: test_gemma4_lora
- 关键代码摘录:

```diff
diff -- tests/lora/test_gemma4_tp.py
@@ -62,6 +62,7 @@ def test_gemma4_lora(gemma4_vision_lora_files):
+        gpu_memory_utilization=0.8,
```

- 已读文件:
  - tests: `tests/lora/test_gemma4_tp.py` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/lora/test_gemma4_tp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64816 - [Perf][DSv4.1] Vectorize first-layer HC expansion copy

- 链接: https://github.com/vllm-project/vllm/pull/64816
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/mhc/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`；关联提交 `ea836290a716`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+69/-1，可读 patch 106 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][DSv4.1] Vectorize first-layer HC expansion copy」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/mhc/test_mhc_kernels.py`；技术摘要: 覆盖「[Perf][DSv4.1] Vectorize first-layer HC expansion copy」；主要实现面是 `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/mhc/test_mhc_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0 (33 lines); hunks: -19,6 +19,7; -320,3 +321,35 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, _hc_expand_kernel, hc_expand，涉及 `mhc_shifted_post_pre, _hc_expand_kernel, hc_expand`；`vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -110,6 +110,7; -527,7 +528,7 @@ def forward(; symbols: forward，涉及 `forward`；`tests/kernels/mhc/test_mhc_kernels.py` modified +34/-0 (34 lines); hunks: -46,6 +46,7; -1889,3 +1890,36 @@ def test_mhc_fused_post_pre_delayed_falls_back_for_large_...; symbols: test_mhc_fused_post_pre_delayed_falls_back_for_large_batches, test_hc_expand_preserves_bits_in_eager_and_graph, check，涉及 `test_mhc_fused_post_pre_delayed_falls_back_for_large_batches, test_hc_expand_preserves_bits_in_eager_and_graph, check`。
- 代码 diff 细节:
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0 (33 lines); hunks: -19,6 +19,7; -320,3 +321,35 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, _hc_expand_kernel, hc_expand
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -110,6 +110,7; -527,7 +528,7 @@ def forward(; symbols: forward
  - `tests/kernels/mhc/test_mhc_kernels.py` modified +34/-0 (34 lines); hunks: -46,6 +46,7; -1889,3 +1890,36 @@ def test_mhc_fused_post_pre_delayed_falls_back_for_large_...; symbols: test_mhc_fused_post_pre_delayed_falls_back_for_large_batches, test_hc_expand_preserves_bits_in_eager_and_graph, check
- 关键代码摘录:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -19,6 +19,7 @@
+from vllm.triton_utils import tl, triton
@@ -320,3 +321,35 @@ def mhc_shifted_post_pre(
+@triton.jit
+def _hc_expand_kernel(
+    x,
+    out,
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -110,6 +110,7 @@
+    hc_expand,
@@ -527,7 +528,7 @@ def forward(
-                residual = x.unsqueeze(1).expand(-1, self.hc_mult, -1).contiguous()
+                residual = hc_expand(x, self.hc_mult)
diff -- tests/kernels/mhc/test_mhc_kernels.py
@@ -46,6 +46,7 @@
+from vllm.models.deepseek_v41.nvidia.ops.mhc import hc_expand
@@ -1889,3 +1890,36 @@ def test_mhc_fused_post_pre_delayed_falls_back_for_large_batches():
```

- 已读文件:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1
  - tests: `tests/kernels/mhc/test_mhc_kernels.py` modified +34/-0
- 验证与风险: diff 自带测试面 `tests/kernels/mhc/test_mhc_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64675 - [Bugfix][Parser] Parse closed Qwen3 tool parameters once while streaming

- 链接: https://github.com/vllm-project/vllm/pull/64675
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`；关联提交 `c7a683bde590`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+160/-18，可读 patch 241 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Parser] Parse closed Qwen3 tool parameters once while streaming」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`；技术摘要: 覆盖「[Bugfix][Parser] Parse closed Qwen3 tool parameters once while streaming」；主要实现面是 `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/parser/engine/test_qwen3.py` modified +94/-0 (94 lines); hunks: -819,6 +819,14 @@ def test_partial_value_with_angle_bracket_and_complete_para...; -908,6 +916,92 @@ def counting_converter(raw_args: str, partial: bool) -> str:; symbols: test_partial_value_with_angle_bracket_and_complete_param, TestArgValueExtender, counting_converter, test_repeated_closed_params_stream_non_streaming_arguments，涉及 `test_partial_value_with_angle_bracket_and_complete_param, TestArgValueExtender, counting_converter`；`vllm/parser/qwen3.py` modified +66/-18 (84 lines); hunks: -56,6 +56,7; -67,22 +68,60 @@ def _trim_wrapping_newlines(value: str) -> str:; symbols: _trim_wrapping_newlines, _qwen3_arg_converter, _ClosedParams, __init__，涉及 `_trim_wrapping_newlines, _qwen3_arg_converter, _ClosedParams`。
- 代码 diff 细节:
  - `tests/parser/engine/test_qwen3.py` modified +94/-0 (94 lines); hunks: -819,6 +819,14 @@ def test_partial_value_with_angle_bracket_and_complete_para...; -908,6 +916,92 @@ def counting_converter(raw_args: str, partial: bool) -> str:; symbols: test_partial_value_with_angle_bracket_and_complete_param, TestArgValueExtender, counting_converter, test_repeated_closed_params_stream_non_streaming_arguments
  - `vllm/parser/qwen3.py` modified +66/-18 (84 lines); hunks: -56,6 +56,7; -67,22 +68,60 @@ def _trim_wrapping_newlines(value: str) -> str:; symbols: _trim_wrapping_newlines, _qwen3_arg_converter, _ClosedParams, __init__
- 关键代码摘录:

```diff
diff -- tests/parser/engine/test_qwen3.py
@@ -819,6 +819,14 @@ def test_partial_value_with_angle_bracket_and_complete_param(self):
+# A model stuck in a loop repeats closed parameters inside one call.
+LOOP_HEAD = (
+    "<tool_call>\n<function=write_file>\n<parameter=path>\n/repo/app.py\n</parameter>\n"
+)
+LOOP_PARAMS = (
+    "<parameter=content>\na > b\n</parameter>\n<parameter=mode>\n644\n</parameter>\n"
diff -- vllm/parser/qwen3.py
@@ -56,6 +56,7 @@
+_PARAM_OPENER_RE = re.compile(r"<\s*parameter\s*=")
@@ -67,22 +68,60 @@ def _trim_wrapping_newlines(value: str) -> str:
-def _qwen3_arg_converter(raw_args: str, partial: bool) -> str:
-    params: dict[str, object] = {}
+class _ClosedParams:
+    """Closed parameters of a raw argument text, reused by longer texts.
```

- 已读文件:
  - tests: `tests/parser/engine/test_qwen3.py` modified +94/-0
  - runtime: `vllm/parser/qwen3.py` modified +66/-18
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_qwen3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64509 - [Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant

- 链接: https://github.com/vllm-project/vllm/pull/64509
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/core/test_fused_sigmoid_gate_mul.py`, `tests/kernels/mamba/test_gdn_output_projection.py`, `tests/models/qwen3_5/__init__.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`, `vllm/kernels/triton/fused_sigmoid_gate_mul.py` 等 10 个文件；关联提交 `6c19299fca37`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+668/-34，可读 patch 994 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant」；模型线: Shared Framework PRs；类别: 性能/后端优化；主要 diff: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`；技术摘要: 覆盖「[Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant」；主要实现面是 `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel, gemma_add_rms_norm_quant，涉及 `_rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel`；`vllm/models/qwen3_5/nvidia/model.py` modified +125/-18 (143 lines); hunks: -50,6 +50,11; -60,6 +65,14; symbols: _norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm, forward，涉及 `_norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm`；`tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _fp8_codes, _fp4_codes, _swizzled_sf_rows, test_gemma_add_rms_norm_quant_matches_chain，涉及 `_fp8_codes, _fp4_codes, _swizzled_sf_rows`；`vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` modified +18/-8 (26 lines); hunks: -28,6 +28,7; -577,6 +578,9 @@ def __init__(; symbols: __init__, forward_hip, forward_cuda，涉及 `__init__, forward_hip, forward_cuda`。
- 代码 diff 细节:
  - `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel, gemma_add_rms_norm_quant
  - `vllm/models/qwen3_5/nvidia/model.py` modified +125/-18 (143 lines); hunks: -50,6 +50,11; -60,6 +65,14; symbols: _norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm, forward
  - `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _fp8_codes, _fp4_codes, _swizzled_sf_rows, test_gemma_add_rms_norm_quant_matches_chain
  - `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` modified +18/-8 (26 lines); hunks: -28,6 +28,7; -577,6 +578,9 @@ def __init__(; symbols: __init__, forward_hip, forward_cuda
  - `vllm/model_executor/models/qwen3_next.py` modified +21/-4 (25 lines); hunks: -28,6 +28,10; -50,6 +54,9; symbols: _project_qkv_gate, forward
- 关键代码摘录:

```diff
diff -- vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py
@@ -0,0 +1,216 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Gemma (1 + w) add-RMSNorm fused with the consumer linear's input quant.
+Replaces ``gemma_fused_add_rmsnorm`` followed by a standalone static FP8
+(``scaled_fp8_quant``) or NVFP4 (``scaled_fp4_quant``) kernel. The quantized
+values are computed from the bf16-rounded normed activation with the same
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -50,6 +50,11 @@
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
+    get_input_quant_key,
+)
+from vllm.model_executor.layers.linear import LinearBase
@@ -60,6 +65,14 @@
diff -- tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py
@@ -0,0 +1,109 @@
```

- 已读文件:
  - runtime: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0; `vllm/models/qwen3_5/nvidia/model.py` modified +125/-18; `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` modified +18/-8; `vllm/model_executor/models/qwen3_next.py` modified +21/-4; `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` modified +15/-0
  - tests: `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0; `tests/models/qwen3_5/__init__.py` added +2/-0; `tests/kernels/core/test_fused_sigmoid_gate_mul.py` modified +65/-0
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_fused_sigmoid_gate_mul.py`, `tests/kernels/mamba/test_gdn_output_projection.py`, `tests/models/qwen3_5/__init__.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64644 - [CI] Fix mypy errors in test_glm5next.py

- 链接: https://github.com/vllm-project/vllm/pull/64644
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm5next.py`；关联提交 `335dd77b0916`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-5，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Fix mypy errors in test_glm5next.py」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/models/multimodal/processing/test_glm5next.py`；技术摘要: 覆盖「[CI] Fix mypy errors in test_glm5next.py」；主要实现面是 `tests/models/multimodal/processing/test_glm5next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames，涉及 `test_glm5_raw_video_timestamps_follow_sampled_frames`。
- 代码 diff 细节:
  - `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5 (12 lines); hunks: -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():; symbols: test_glm5_raw_video_timestamps_follow_sampled_frames
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/processing/test_glm5next.py
@@ -158,14 +158,16 @@ def test_glm5_raw_video_timestamps_follow_sampled_frames():
-    item = raw["mm_kwargs"]["video"][0].get_data()
+    video_item = raw["mm_kwargs"]["video"][0]
+    assert video_item is not None
+    item = video_item.get_data()
-    grid_t = int(grid.reshape(-1)[0] if hasattr(grid, "reshape") else grid[0])
-    if hasattr(timestamps, "reshape"):
```

- 已读文件:
  - tests: `tests/models/multimodal/processing/test_glm5next.py` modified +7/-5
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64619 - [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub

- 链接: https://github.com/vllm-project/vllm/pull/64619
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`；关联提交 `daccf69eb222`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub」；模型线: Shared Framework PRs；类别: 文档/测试/CI；主要 diff: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`；技术摘要: 覆盖「[CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub」；主要实现面是 `tests/models/kimi_k3/test_amd_kda_checkpoint.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #64535 - [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming

- 链接: https://github.com/vllm-project/vllm/pull/64535
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`；关联提交 `255431b5ed87`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+112/-8，可读 patch 181 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`；技术摘要: 覆盖「[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming」；主要实现面是 `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments，涉及 `test_thinking_disabled, _pieces, counting_converter`；`vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter，涉及 `_ClosedArgs, __init__, _glm47_parse_args`。
- 代码 diff 细节:
  - `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments
  - `vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter
- 关键代码摘录:

```diff
diff -- tests/parser/engine/test_glm47_moe.py
@@ -18,6 +18,7 @@
+from vllm.parser import glm47_moe
@@ -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):
+# A model stuck in a loop repeats closed argument pairs inside one call.
+LOOP_HEAD = (
+    f"{THINK_END}{TOOL_CALL_START}Write\n"
+    "<arg_key>file_path</arg_key><arg_value>/repo/app.py</arg_value>\n"
diff -- vllm/parser/glm47_moe.py
@@ -64,18 +64,47 @@
+class _ClosedArgs:
+    """Closed key/value pairs of a raw argument text, reused by longer texts.
+    Raw arguments only grow while a call streams, so a parse of a text that
+    extends ``text`` resumes after its last closed value.
+    """
+    __slots__ = ("text", "params", "outside")
```

- 已读文件:
  - tests: `tests/parser/engine/test_glm47_moe.py` modified +61/-0
  - runtime: `vllm/parser/glm47_moe.py` modified +51/-8
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_glm47_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64506 - [Bugfix][Model] Nemotron 3.5 Super VL: support the native transformers config

- 链接: https://github.com/vllm-project/vllm/pull/64506
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/nano_nemotron_vl.py`；关联提交 `510d15c49e98`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+16/-5，可读 patch 52 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Nemotron 3.5 Super VL: support the native transformers config」；模型线: Shared Framework PRs；类别: 缺陷修复；主要 diff: `tests/models/registry.py`, `docs/models/supported_models.md`, `vllm/model_executor/models/nano_nemotron_vl.py`；技术摘要: 覆盖「[Bugfix][Model] Nemotron 3.5 Super VL: support the native transformers config」；主要实现面是 `tests/models/registry.py`, `docs/models/supported_models.md`, `vllm/model_executor/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/registry.py` modified +7/-2 (9 lines); hunks: -1253,9 +1253,14 @@ def check_available_online(; symbols: check_available_online，涉及 `check_available_online`；`docs/models/supported_models.md` modified +6/-2 (8 lines); hunks: -610,6 +610,7 @@ These models primarily accept the [`LLM.generate`](./generat...; -722,10 +723,13 @@ Some models are supported only via the [Transformers model...；`vllm/model_executor/models/nano_nemotron_vl.py` modified +3/-1 (4 lines); hunks: -997,7 +997,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/models/registry.py` modified +7/-2 (9 lines); hunks: -1253,9 +1253,14 @@ def check_available_online(; symbols: check_available_online
  - `docs/models/supported_models.md` modified +6/-2 (8 lines); hunks: -610,6 +610,7 @@ These models primarily accept the [`LLM.generate`](./generat...; -722,10 +723,13 @@ Some models are supported only via the [Transformers model...
  - `vllm/model_executor/models/nano_nemotron_vl.py` modified +3/-1 (4 lines); hunks: -997,7 +997,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/models/registry.py
@@ -1253,9 +1253,14 @@ def check_available_online(
-    # TODO: Change repo id once pertinent archs are public.
-        "nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16", is_available_online=False
+        "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16",
+        min_transformers_version="5.18.0",
+        max_model_len=4096,
+        use_original_num_layers=True,
diff -- docs/models/supported_models.md
@@ -610,6 +610,7 @@ These models primarily accept the [`LLM.generate`](./generative_models.md#llmgen
+| `NemotronH_Omni_Reasoning_V3` | Nemotron 3.5 Super VL | T + I<sup>E+</sup> + V<sup>+</sup> | `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`, `nvidia/NVIDIA-Nemotron-3.5-Su
@@ -722,10 +723,13 @@ Some models are supported only via the [Transformers modeling backend](#transfor
-    Both Nemotron Nano architecture names map to the same vLLM implementation.
+    Both Nemotron Nano architecture names and `NemotronH_Omni_Reasoning_V3` map to
+    the same vLLM implementation.
-    image and video only.
diff -- vllm/model_executor/models/nano_nemotron_vl.py
@@ -997,7 +997,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
```

- 已读文件:
  - tests: `tests/models/registry.py` modified +7/-2
  - docs: `docs/models/supported_models.md` modified +6/-2
  - runtime: `vllm/model_executor/models/nano_nemotron_vl.py` modified +3/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
