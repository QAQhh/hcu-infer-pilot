---
schema_version: 1
owner: HCU Optimization Team
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/kernel-model-triage
---
# Skill Card


## Summary

面向海光 HCU/BW 系列、HIP/DTK、PyTorch/torch.compile、自定义算子和真实模型工作负载的一体化测试、性能诊断、精度回归定位与优化闭环。适用场景：通用或未单独覆盖的 HCU 训练/推理任务、单卡或多卡性能下降/OOM/编译问题、模型到 HIP kernel 的跨层诊断，以及 Hygon-Hub 自动驾驶、HCU LLM/VLM、DriveDreamer、LingBot-VLA 等工作负载的验收与优化。不适用场景：非海光 HCU 平台、只需要设备状态查询的简单任务，或没有可比基线和正确性 reference 却要求直接改写 kernel 的任务。


## Owner

HCU Optimization Team


## Source

Locally maintained at `das/SkillHub`, path `skills/kernel-model-triage`.


## License

Declared as `Apache-2.0`; see original source licensing and any preserved LICENSE/NOTICE material. Import does not relicense this content.


## Runtime and permissions

Requires a HCU host with ROCm and PyTorch to reproduce the workload and read precision data; some checks need hipprof counters. Writes diagnostic reports and comparison artifacts in the working directory and does not modify model checkpoints.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/kernel-model-triage`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: imported from the team's internal optimization
skills repository on the internal GitLab. The upstream project path and commit are
recorded in the merge request that introduced this skill.
