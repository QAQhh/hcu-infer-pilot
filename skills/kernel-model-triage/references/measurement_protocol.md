# HCU Measurement Protocol

## 目录

1. 测量契约
2. 采样设计
3. 计时边界
4. 统计与判定
5. 多卡、训练和服务指标
6. 报告最低字段

## 1. 测量契约

在采样前固定：commit/diff、镜像 ID、设备、驱动/DTK、时钟策略、功耗模式、shape、dtype、layout、batch、并发、卡数、数据、checkpoint、seed、CPU/NUMA、线程数和环境变量。任一关键项变化都建立新 series。

把指标分为主指标、正确性/资源门禁指标和诊断指标。

## 2. 采样设计

- cold start、compile、autotune、cache warmup 与 steady state 分开。
- 先用时间序列确认稳定区间，不固定假设丢前 N 次。
- 保存每次原始值、时间戳和异常事件。
- 采样前预注册最小独立 series 数、每个 series 的最小样本/时长和扩样停止条件；尾延迟或 CI 未收敛时继续采样。
- 候选和基线尽量 A/B/A/B 交替运行。
- 可复现输入时优先配对比较；样本数量相同不等于配对。
- 覆盖生产主 shape，并增加 small/medium/large。
- 长训练窗口要保持相同 epoch/data/compile 状态。

## 3. 计时边界

### GPU kernel/operator

使用 device event 或 profiler duration；读取前同步。明确是否包含 launch、layout、allocation、forward、backward 和 optimizer。重用 event；graph 分别报告 capture 与 replay。

### 训练

说明 `time/iter` 是否包含 DataLoader、gradient sync、optimizer、EMA、日志与 checkpoint，并让 batch 与计时边界一致：

```text
microstep: global_micro_batch / median_microstep_time
optimizer step: global_effective_batch / median_full_optimizer_step_time
global_effective_batch = world_size * batch_per_device * gradient_accumulation_steps
```

### 在线推理/LLM

区分 closed-loop concurrency 与 open-loop request rate；同时报告成功率、tokens/s、request throughput、TTFT、TPOT/ITL 和 E2E P50/P90/P95/P99。固定 token 长度、sampling、template 与 cache 状态。

```text
TTFT = client send timestamp → first token received timestamp
TPOT = (E2E - TTFT) / (actual_output_tokens - 1), actual_output_tokens > 1
request/s = successful_requests / steady_window_duration
```

失败、超时和取消请求保留在总请求分母中；不能只对成功请求采样后声称服务稳定。

## 4. 统计与判定

最低报告：`n`、mean、median、min、max、P90、P95、standard deviation、CV、MAD。

- 重尾或抖动时以 median/P90/P95 为主。
- 独立 series 用 unpaired bootstrap speedup 95% CI；确实一一匹配时才用 `--paired`。
- 请求级延迟、训练 step 和连续 trace 常有时间相关性。不要把相关样本直接当作独立同分布数据；优先对独立 run 聚合，或使用经说明的 block/cluster bootstrap。
- 延迟 speedup 为 `baseline/candidate`；吞吐为 `candidate/baseline`。
- correctness 通过、CI 不跨无收益线、资源不超限且 E2E 同方向时才标 `VALIDATED`。
- 样本少或差异与噪声同量级时标 `INCONCLUSIVE`。

`<skill>/scripts/benchmark_stats.py` 提供一致的数值分位数和普通 sample-level bootstrap，但假设输入可视为独立样本；它不计算失败率、超时或稳态区间，不能替代服务 benchmark 结果解析和时间序列检查。

脚本只对 median 提供 bootstrap CI。P99 是硬 SLO 时，必须准备足够尾部样本，并在独立 run 或 block/cluster 层计算 tail CI；不能仅凭脚本输出的单个 P99 点估计通过验收。

## 5. 多卡、训练和服务指标

```text
scaling_efficiency = throughput_N / (N * throughput_1)
```

同时记录每 rank step time、straggler、all-reduce、通信占比、CPU/NUMA 和 device mapping。batch sweep 固定 workers；worker sweep 固定 batch。OOM/稳定性失败也记录。

profiler 运行用于定位；最终验收默认使用低开销运行。

## 6. 报告最低字段

```text
Series/run ID and environment fingerprint
Command, variables, workload, timing boundary
Warmup/stability rule and raw sample path
n / median / P90 / P95 / P99 / CV / MAD / CI
Speedup definition
Correctness/resource gates
Known anomalies and exclusions with reasons
```

不得只保留过滤后的数字。
