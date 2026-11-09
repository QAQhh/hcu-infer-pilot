---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-triton-optimize
---
# Skill Card


## Summary

海光 HCU/HCU Python/Triton kernel 的 roofline 驱动迭代优化器。通过固定配置 benchmark、xcu/hipprof profiling、本地 KB 知识检索、Triton IR/cache 捕获、dccobjdump ISA 验证、Branch 探索择优、Ablation 消融归因的完整闭环，对 Triton kernel 进行多轮迭代深度优化。覆盖 compute/memory/latency 三轴 18+ 优化方法，支持 gfx928/gfx92a/gfx936/gfx938/gfx946/gfx948 多架构。适用：需要对 HCU 上的 Triton kernel 进行 roofline 驱动的迭代深度优化。不适用：仅需单次 benchmark 或不需要完整迭代闭环的简单场景。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-triton-optimize`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Requires a HCU host with ROCm, Triton, PyTorch, hipprof and dccobjdump, plus the bundled tooling under scripts/; the iteration loop builds, profiles and validates kernels on a HCU host. Writes kernels, profiling artifacts, IR dumps and reports under the run directory.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-triton-optimize`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
