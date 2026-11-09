---
schema_version: 1
owner: yangyinan
license: MIT
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/dcu-profiler-report
---
# Skill Card


## Summary

Use when a LightOp DCU/ROCm operator needs profiling evidence: run hipprof or deeper ROCm/DTK profilers, capture synchronized benchmark logs, summarize API/kernel/memory time, inspect counters or AMDGPU ISA when available, and produce exactly one concrete next operator edit.


## Owner

yangyinan


## Source

Locally maintained at `das/SkillHub`, path `skills/dcu-profiler-report`.


## License

Declared as `MIT`; see the bundled [LICENSE](LICENSE) for the complete terms, source attribution and applicable mixed-package scope. The supplied source declares MIT; this import does not relicense that content.


## Runtime and permissions

See [SKILL.md](SKILL.md) and linked domain references for tool, GPU, container, network and artifact-write requirements. No Humanize runtime, hooks or generic skills are included. No inference, GPU tuning, external review or hook installation is executed by this import.


## Local catalog import

This copy is maintained in `das/SkillHub` at `skills/dcu-profiler-report`, not synchronized upstream. Existing instructions, attribution and validation statements describe the imported source; review their applicability before publishing this copy. No skill code was executed by the importer.

Additional origin or attribution: One-time domain-skill import from lightop-skiils/humanize/skills/ncu-report/SKILL.md. Maintained by yangyinan; original authorship and domain license declarations are retained. No claim of original authorship is made by catalog inclusion. Humanize generic skills and runtime are not bundled; integrations refer to https://github.com/PolyArch/humanize. The independent LightOp device-bandwidth helper is retained from the supplied LightOp-specific additions; it is absent from the recorded official Humanize tree.
