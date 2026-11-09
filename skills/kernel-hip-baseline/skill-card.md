---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-hip-baseline
---
# Skill Card


## Summary

从 Torch、Triton、TileLang、Python 或 CUDA/C++ 参考实现生成海光 HCU HIP/C++ baseline kernel 和正确性 harness。同时支持 CUDA→HIP/HCU 自动转换，产出正确性验证通过的可编译 HIP kernel baseline。适用：需要从已有实现快速生成 HCU HIP baseline kernel。不适用：已有完整 HIP 实现且通过正确性验证的场景。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-hip-baseline`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Requires a HCU host with ROCm/HIP and the build toolchain for the generated kernel; the correctness harness is executed locally. Writes generated kernels, harnesses and benchmark artifacts in the output directory.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-hip-baseline`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
