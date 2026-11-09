---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-hip-optimize
---
# Skill Card


## Summary

海光 HCU HIP/CK Tile kernel 迭代优化器。使用 hipprof→roofline 量化→ISA 验证（dccobjdump）→Branch 探索→Ablation 归因→经验记录的完整闭环，对 HIP kernel 进行多轮迭代优化。适用：需要对 HIP kernel 进行迭代深度优化。不适用：仅需一次性 roofline 分析的场景。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-hip-optimize`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Requires a HCU host with ROCm/HIP, hipprof and dccobjdump, plus the bundled Python tooling under scripts/; profiling and kernel builds run on the local or a remote HCU host. Writes optimization state, branches, reports and generated kernels under the run directory.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-hip-optimize`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
