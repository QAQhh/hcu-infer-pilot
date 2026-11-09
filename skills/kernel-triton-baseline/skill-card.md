---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-triton-baseline
---
# Skill Card


## Summary

海光 HCU Python/Triton 正确性优先基线生成器。从 Torch/Python/Triton 参考实现 + shape hints 生成 benchmark 兼容的 kernel.py 和 ref.py 基线 case，作为 kernel-triton-optimize 的前置步骤。支持 matmul/GEMM/elementwise 的自动生成，Reduction/Attention/MoE 需人工手写。适用：需要从已有参考实现快速生成 Triton kernel 基线并验证正确性。不适用：已有完整 benchmark-compatible Triton kernel 的场景。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-triton-baseline`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Requires a HCU host with ROCm, Triton and PyTorch; the generated kernel and reference harness are executed locally. Writes generated kernels, harnesses and benchmark artifacts in the output directory.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-triton-baseline`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
