# HCU Workload Playbooks

按工作负载补充主 `SKILL.md` 的通用闭环。只读取当前任务对应章节，不把历史主机、镜像、路径、batch 或性能数字当作当前事实。

## 目录

1. 通用进入条件
2. Hygon-Hub 自动驾驶模型
3. HCU LLM/VLM 推理服务
4. DriveDreamer
5. LingBot-VLA
6. 进入 HIP kernel 优化的条件

## 1. 通用进入条件

开始前固定：

- 当前仓库、commit/diff、容器 image digest 和实际 HostConfig；
- 目标硬件、DTK/HIP、torch、triton、框架扩展版本；
- 模型 config、数据/checkpoint fingerprint、seed、world size、batch/device、global batch 和 workers；
- 项目原生入口、最终展开命令、环境变量白名单和 accepted baseline；
- 性能、精度、显存、稳定性与停止条件。

先检查现有进程、容器和日志，避免在仍运行的模型或服务旁启动冲突实验。对源码、配置和容器内文件的持久修改先形成候选 diff，获得授权后再应用。

## 2. Hygon-Hub 自动驾驶模型

适用于 BEVFormer、BEVFusion、FlashOCC、MapTRv2、PointPillars、Sparse4D 等镜像/训练/eval 验收和后续优化。

### 入口与数据门禁

1. 读取当前模型 README、`one_step_data.sh`、根目录和模型目录的 `start*.sh`。
2. 使用模型自己的数据准备脚本，验证数据版本、样本数、目录结构和 checkpoint 来源。
3. 使用模型自己的 `start_<model>.sh` 或仓库明确入口；底层 `train.py`/`dist_train` 只用于已证明等价的诊断。
4. 从 launcher 捕获最终命令、world size、batch/device、global batch、compile/layout/custom-op 路径。
5. literal placeholder、路径、卡数或 batch 矛盾时停止，不为“跑通”猜参数。

### 分阶段 smoke

```text
import/config/startup
→ 1–5 个真实 iteration
→ 20 iteration
→ 稳定 100-iteration 窗口
→ 需要 loss 置信度时再扩到 500 iteration
→ 前序全绿且用户目标需要时 full run/eval
```

使用项目已有 max-iter/stop hook 或受控参数。记录每级 PID、命令、退出方式、日志和状态。不要静默关闭 compile、channels-last、TF32 或 custom op；用于隔离时标为诊断分支。

### 性能与精度

- 分开 compile/autotune/cold start 与 steady state。
- 基线和候选保持模型、数据、global batch、world size、workers、seed、入口和优化开关一致。
- 保存逐 iteration 原始数据；可用：

```bash
python <skill>/scripts/summarize_mmdet_log.py <log-file>
```

- batch sweep 固定 workers，worker sweep 固定 batch，以 global samples/s 比较，同时记录显存/OOM 边界。
- 正式 eval 使用项目官方 evaluator，固定 checkpoint、dataset/version、命令和任务指标。
- loss/mAP 回退时，用相同 batch/checkpoint/seed 比较 forward/backward 中间量并定位第一个发散点。

没有同口径 accepted baseline 时输出 `NO_COMPARABLE_BASELINE`，不拿历史数字填补。

## 3. HCU LLM/VLM 推理服务

把主机、通信、服务、性能和精度拆成逐级门禁。默认服务只在本机回环地址可见。

本整合包提供验收流程，不捆绑 RCCL tests、vLLM、压测客户端、模型 evaluator 或防火墙工具。先从目标镜像/项目解析其已批准命令和版本；缺少执行器时标 `NOT_AVAILABLE`，不要编造命令或自动安装系统软件。

### 安全硬规则

- 宿主机服务默认监听 `127.0.0.1`。bridge 容器即使内部监听 `0.0.0.0`，宿主机也只发布到 `127.0.0.1:<port>`。
- API key 使用本轮随机 secret，文件权限 `0600`，日志和报告只写 `REDACTED`；不要放进镜像、Git 或 Docker metadata。先检查当前 vLLM 是否支持安全的 secret-file/进程内注入；若只能使用可见 argv，记录暴露边界并要求用户接受，不能声称密钥已隐藏。
- `--trust-remote-code` 默认关闭；只有模型确实需要且代码来源已审查时开启。
- 模型目录只读；checkpoint/tokenizer/processor/custom code 都按可执行输入审查。
- VLM 媒体优先使用经过验证的内联内容或专用只读目录；默认禁用任意远程 URL 和宽泛本地路径访问，防止 SSRF 与文件泄漏。
- 不在 serving 容器内 `pip -U` 污染环境；accuracy evaluator 使用独立容器或锁定 venv。
- 只停止和删除本轮 manifest 记录的 PID、端口、容器和临时凭据。

### 验证顺序

1. 只读采集 host、HCU、topology/NUMA、software、监听端口和现有进程，选择完全空闲的卡。
2. 在选定卡上跑 RCCL correctness/bandwidth；失败后再下钻 GDR/RDMA/XDP，不先改网络。
3. 复刻已接受容器或使用最小安全模板，模型只读挂载。
4. 回环启动 vLLM，记录脱敏后的最终命令、PID、env allowlist、load milestone 和健康状态；检查宿主机/容器 HostIp、IPv4/IPv6 listener 以及新增的分布式辅助端口，不能只看一个 API 端口。
5. 运行 API smoke；VLM 必须包含真实图像/视频请求，不能只跑文本。
6. 运行 closed-loop concurrency sweep；容量测试再增加 open-loop request-rate sweep。采样前固定独立 series 数、每点请求数/时长、warmup 和扩样停止条件。
7. 在隔离 evaluator 中先 smoke 再跑正式 accuracy。
8. teardown 并报告最终端口、进程、容器、时钟和临时文件状态。

### 最低报告口径

- 性能：实际 input/output tokens、成功/失败/超时、duration、request/s、token/s、TTFT、TPOT/ITL、E2E P50/P90/P95/P99、显存和重复统计。失败和超时保留在总请求分母中。
- 多卡：RCCL、rank/NUMA mapping、TP size 和每卡显存。
- 精度：模型/权重 hash、tokenizer/chat template、dataset revision、evaluator/version、generation config 和 seed。
- VLM/VLA：媒体解码、processor/template 以及至少一个视觉任务或样例。

服务对外暴露、host network、防火墙、SSH、时钟或系统软件变更均需单独授权。

## 4. DriveDreamer

### 数据和路径

- 验证 nuScenes 处理结果、HDMap、模型路径、符号链接和生成的 dataset config。
- 不复用历史 `/cfs`、`DREAMER_MODELS_DIR` 或容器路径；从当前脚本和挂载重新发现。
- 优先使用临时 runner、环境覆盖和 checkout 外的 run-scoped artifact 目录。

### 性能定位

先把 step 分解为 data wait、VAE encode、UNet、backward、optimizer、EMA 和 launcher/runtime overhead。不要在未证明热点前扫大量模型参数。

对 `rank0_step_timings.json` 使用：

```bash
python <skill>/scripts/analyze_step_timings.py \
  --start 101 --tail 200 --global-batch <verified-global-batch> \
  --label baseline <baseline.json> \
  --label candidate <candidate.json>
```

脚本不会为缺失 timing 填零，也不会猜 global batch。A/B 保持 seed、容器、数据和窗口一致，比较 loss、finite/NaN steps、grad scale、median/P90 step time 和 stage timing。

launcher 在产物已经落盘后出现 cleanup error 时，先检查日志/JSON 是否有效，不直接判训练失败。

## 5. LingBot-VLA

### 环境适配

- 使用当前验证过且 digest 固定的 DTK image。
- 保留基础镜像中的 DTK torch、torchvision、triton 和 flash-attn；禁止 pip 覆盖为 CUDA/upstream torch wheel。
- `torchcodec` 没有匹配 HCU 构建时，优先让 LeRobot 视频加载使用 `pyav`。
- 模型、Qwen/LingBot checkpoint、LeRobot dataset 和 norm stats 均记录来源、版本与 hash。
- 包镜像或 Hugging Face mirror 只是传输渠道，不能替代版本固定和完整性校验。

### Benchmark

1. 从实际配置推导 `global_batch = micro_batch × accumulation × data_parallel_size`。
2. 为每次运行创建唯一日志，先验证日志确实属于当前 PID/开始时间：

```bash
python <skill>/scripts/extract_current_log.py \
  --current <project-log> --launcher <launcher-log> \
  --marker <run-start-marker> \
  --output current_run.log
```

3. 丢弃 warmup 后统计稳定窗口：

```bash
python <skill>/scripts/parse_lingbot_step_times.py current_run.log \
  --config <verified-config.yaml>
```

4. 同时报告 step time、samples/s、loss、显存、卡数和配置 hash。

privileged、host network、host IPC、root 用户或可写源码挂载只能作为有证据的显式例外。

## 6. 进入 HIP kernel 优化的条件

只有 profiler 证明某个自定义 HIP kernel 对目标端到端指标有足够上限，并且已经建立 production shape、forward/backward reference、稳定样本和 fallback 时，才读取 `references/hip_kernel_tuning.md`。

如果主瓶颈仍是数据、RCCL、框架 graph、MIOpen/rocBLAS、服务调度或模型算法，留在对应模型章节处理，不用 kernel microbenchmark 代替端到端结论。
