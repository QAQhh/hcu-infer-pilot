---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-hip-handbook
---
# Skill Card


## Summary

海光 BW 系列 HCU HIP Kernel 深度性能优化指南（3500+ 行）。覆盖 roofline 分析、指令级优化（ISA 验证、dccobjdump）、共享内存/LDS 调优、Occupancy 计算、Branch 选择与 Ablation 归因、CK Tile kernel 优化等核心技术。适用：需要对 BW 系列 HCU 上的 HIP kernel 进行深度性能优化。不适用：NVIDIA GPU 环境。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-hip-handbook`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Knowledge-only skill: reading the bundled reference material needs no tooling, while the examples assume a HCU host with ROCm/DTK when they are applied. The skill itself writes nothing.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-hip-handbook`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
