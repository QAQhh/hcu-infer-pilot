# Validation and Reproduction

用于把模型优化从“跑快了”变成“可交付、可复查、可复现”。

## 目录

1. 验证分层
2. Benchmark 口径
3. Run manifest 模板
4. 复现文档模板
5. 汇报模板
6. 常见坑

## 验证分层

### 算子级

必须覆盖：
- 典型生产 shape。
- 边界输入：空输入、near-boundary 坐标、重复点、overflow、clip/max_voxels、stride=2 或不支持 shape。
- 输出语义：坐标顺序、行顺序、点顺序、截断顺序、有效 mask。
- backward：每个梯度张量都要比对，不能只看 loss 不报错。
- arch 分支：当前卡型（如 `gfx938`）和旧卡型编译路径不能互相破坏。

适用示例：
- PointPillars voxelize：除 coors/counts 外，还要比对每个 voxel 内保留点和 VFE 前后特征。
- Sparse4D deformable aggregation：重点查 `grad_mc_ms_feat`、权重/位置梯度、special path 的 arch 宏。
- BEVFormer DCNv2：用真实 DCN shape 做 fwd/bwd smoke，确认 fallback shape 不崩。

### 模型级

必须覆盖：
- 用户指定的正常日志/配置口径，例如 batch、workers、seed、epoch iter 数。
- 至少一个稳定训练窗口，例如 `iter 100-200`。
- loss 是否 NaN、是否接近用户正常基线；有 mAP 时优先跑 mAP。
- `data_time`、显存、均值和中位数，避免单个 outlier 误导。

### 分布式级

单卡快、多卡慢时必须检查：
- all-reduce 微基准，排除 RCCL/NCCL 物理链路问题。
- 每 rank 是否都在 profiler/compile/autotune。
- `find_unused_parameters` 是否每步扫图。
- DataLoader workers、pin_memory、prefetch、NUMA 绑定、线程池是否被 world size 放大。
- 是否存在某个 rank residual GPU/CPU 占用。

## Benchmark 口径

不要比较：
- 第 1 个 iter。
- torch.compile 首轮 graph build。
- MIOpen find/autotune。
- profiler start/stop/flush 所在 step。
- 不同 batch、不同 workers、不同 seed 下的 loss 点，除非明确说明。

建议表格：

| 方案 | batch/GPU | workers/GPU | window | mean | median | memory | loss/mAP | 备注 |
|---|---:|---:|---|---:|---:|---:|---:|---|

batch sweep 用吞吐：

```text
microstep_samples_per_sec = (world_size * batch_per_gpu) / mean_microstep_time
optimizer_step_samples_per_sec = (world_size * batch_per_gpu * grad_accum) / mean_full_optimizer_step_time
```

Choose one formula according to the measured interval; do not combine effective batch with microstep time.

worker sweep 保持 batch 不变；batch sweep 保持 workers 不变。

## Run manifest 模板

`collect_hcu_snapshot.sh` 只是只读环境快照，不等于完整 run manifest。每个基线和候选另保存以下字段；无法获取的项写 `UNKNOWN/NOT_AVAILABLE`，不要静默省略：

```yaml
run_id: <unique-id>
timestamp_utc: <iso8601>
objective_and_acceptance: <metric/correctness/resource/stop rules>
repository:
  path: <absolute-or-redacted>
  commit: <sha>
  dirty_diff_hash: <sha256-or-CLEAN>
runtime:
  host_fingerprint: <redacted-id>
  device_and_arch: <product/gcnArchName/CU/wave>
  driver_dtk_hip_torch_triton: <versions>
  container_image_digest: <digest-or-NOT_APPLICABLE>
  audited_host_config: <artifact-path-or-NOT_APPLICABLE>
workload:
  entry_and_full_command: <redacted-command>
  env_allowlist: <artifact-path>
  model_config_hash: <sha256>
  data_checkpoint_fingerprint: <sha256/manifest>
  seed_shape_dtype_layout: <values>
  world_batch_accum_workers: <values>
operator_if_applicable:
  source_wrapper_build_entry: <paths>
  loaded_binary_hash: <sha256>
  launch_stream_arch_flags: <values>
artifacts:
  raw_samples: <path>
  logs_traces_profiles: <paths>
  correctness_results: <paths>
  patch_and_rollback: <paths>
```

分享 manifest 前复核内部路径、拓扑、软件版本和白名单变量；不得写入密码、token、私钥、完整环境或未脱敏命令参数。

## 复现文档模板

```markdown
# <模型> 优化复现说明

## 环境
- 容器:
- 卡型:
- DTK/ROCm:
- torch/triton/mmcv:
- 数据集路径:

## 基线
- 启动命令:
- 配置:
- 日志:
- 稳定窗口:
- loss/mAP:

## 修改点
- 文件 1:
- 文件 2:
- 环境变量:
- fallback/开关:

## 验证
- 算子精度:
- 端到端 loss/mAP:
- 性能窗口:

## 复现命令
```bash
...
```

## 预期结果
| 指标 | 基线 | 优化 |
|---|---:|---:|

## 回退
```bash
...
```
```

## 汇报模板

用于给领导或评审看：

```markdown
# <模型> AI 辅助性能优化汇报

## 需求输入与验收口径
- 原始需求:
- 约束:
- 验收标准:

## 技术路线
1. 基线采集
2. profiler 定位
3. 精度门禁
4. 优化实现
5. 端到端验证

## 生成效果对比
| 项目 | 优化前 | 优化后 | 提升 |

## 关键代码片段
只放能说明问题的 wrapper/kernel/config 片段，不贴整文件。

## 效率估算
- 人工预计:
- AI 辅助耗时:
- 交互轮数:
- token/上下文估算:
- 注意: 若平台未暴露精确 token，标注为估算。

## 风险控制
- 精度验证:
- 回退方式:
- 不采纳的方案及原因:
```

## 常见坑

| 现象 | 高概率原因 | 正确处理 |
|---|---|---|
| microbench 很快但 loss NaN | 输出语义/顺序/截断不等价 | 建完整 reference validator，默认回退 |
| profiler 后 OOM | profiler + compile/cudagraphs + 动态 shape | 关闭 profiler 做训练；写最小复现给 runtime 侧 |
| 单卡快 8 卡慢 | DataLoader/线程池/DDP unused 检测 | 限线程、降 workers、测 all-reduce、用 static graph |
| 加内存仍 OOM | pinned memory/HIP host registration/NUMA 限制 | 查栈，不把 CPU DRAM 当唯一瓶颈 |
| 替换 site-packages 没端到端收益 | 缺少 layout/cache/wrapper 组合 | 优先项目内 override，并测完整 iter 窗口 |
| fp16 更慢或失败 | Inductor/MIOpen layout 或 custom op meta 不兼容 | 回退 fp32，先证明半精度本身有收益 |
