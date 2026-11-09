# kernel-model-triage

海光 HCU 模型到 kernel 的一体化优化 Skill。流程、参考材料和随附分析脚本可作为单目录交付；DTK、profiler、RCCL tests、模型数据和项目 evaluator 仍由目标环境提供。用于建立可信基线、定位跨层瓶颈、运行精度门禁、验证性能收益，并覆盖常见自动驾驶、LLM/VLM、DriveDreamer 和 LingBot-VLA 工作负载。

## 特点

- 单目录交付，不依赖个人环境中的其他 Skill。
- 核心工作流放在 `SKILL.md`，详细协议按需放在 `references/`。
- 自带环境采集、统计、张量比较、HIP 风险扫描和模型日志分析脚本。
- 所有收益必须从 kernel 逐级传导到 operator、模型和目标卡数/并发。

## 目录

```text
kernel-model-triage/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── measurement_protocol.md
│   ├── correctness_protocol.md
│   ├── profiling_playbook.md
│   ├── hip_kernel_tuning.md
│   ├── workload_playbooks.md
│   ├── validation_and_repro.md
│   └── case_studies.md
└── scripts/
    ├── collect_hcu_snapshot.sh
    ├── benchmark_stats.py
    ├── compare_tensors.py
    ├── scan_hip_kernel.py
    ├── summarize_mmdet_log.py
    ├── analyze_step_timings.py
    ├── extract_current_log.py
    └── parse_lingbot_step_times.py
```

使用时直接调用 `$kernel-model-triage`，或让支持 Skill 自动匹配的 AI 根据 `description` 触发。

## 合入其他 GitLab

复制整个 `kernel-model-triage/` 目录，不要只复制 `SKILL.md`。目标仓库如果按技术域组织，可放到 `skills/operator-tuning/`；其他布局只需保证目录名仍为 `kernel-model-triage`，并保持 `references/`、`scripts/` 和 `agents/` 的相对结构。

合入后运行目标仓库自己的 Skill 校验，并至少执行：

```bash
cd kernel-model-triage
python scripts/benchmark_stats.py --self-test
python scripts/scan_hip_kernel.py --self-test
bash -n scripts/collect_hcu_snapshot.sh
```
