# Case Studies

从 5 个历史实验对话提炼。原始日志/manifest 未随 Skill 分发，因此数值只能作为带方向感的历史叙述，不能单独引用为证据、基线或验收阈值。使用这些案例时只借鉴方法和失败模式；当前任务必须重新采集完整证据。

## 目录

1. PointPillars / voxelize
2. FlashOCC / no-code first
3. Sparse4D / deformable aggregation
4. MapTRv2 / profiler OOM and 8-GPU slowdown
5. BEVFormer / DCNv2 hipDNN combination

## PointPillars / voxelize

用户目标：按 `pp.md` 优化 PointPillars，重点是 `voxeli/hard voxelize` 算子。

关键经验：
- 先做了 atomic dense-grid 快路径，裸速度很好，但只验证坐标和计数，漏掉 voxel 内点内容、点顺序、截断顺序，导致 loss NaN。
- 正确做法是先恢复精度安全默认路径，再补完整 validator：CPU/MMCV reference、normal/boundary/overflow/max_voxels、逐 voxel 内容、canonical 点集、VFE 相关差异。
- 最终采用精确 GPU sort/group 路径，对齐当前 MMCV deterministic 语义，同时保留环境变量回退。
- 端到端必须按用户确认的 `log.log` 口径验证：`batch_size=10`、`num_workers=10`、`352 iter/epoch`，不能拿错误 batch 的 NaN 日志当正常基线。

结果：
- 100k 点算子 microbench：约 `18.28 ms -> 1.09 ms`，约 `16.8x`。
- 同 `bs=10` 端到端：原路径约 `1.33s/iter`，优化路径约 `0.43s/iter`。
- `iter 350/352` loss：优化版约 `2.5932`，用户正常日志 `2.5561`，无 NaN。

可复用原则：
- voxelize、NMS、采样类算子不能只验 shape/count。
- 非确定 atomic 快路径默认不要上线；先证明截断和保留集合等价。
- 性能与精度冲突时，先关闭优化保护训练，再做 safe fast。

## FlashOCC / no-code first

用户目标：模型性能本来还行，优先不改代码；如果收益大再动 kernel。

关键经验：
- rocBLAS 自动选优命中 top GEMM，但实际 bench 大多只有 ±1% 波动，有的退化，因此不应用 Tensile 配置。
- profiler 显示主要瓶颈是 MIOpen conv；custom `bev_pool_v2` forward 约 `2.16ms/step`，backward kernel 约 `36.3ms/step`，不是主瓶颈。
- `with_cp=False` 是低风险配置收益：显存充足时关闭 backbone checkpoint，减少重计算。
- fp16 不是免费收益：compile+fp16 触发 stride/layout 问题，eager fp16 稳态约 `1.37-1.38s/iter`，比 fp32 no-cp 慢。
- NHWC、Inductor layout optimization、coordinate descent tuning 都应保留；关闭会失败或变慢。
- batch sweep 粗扫显示每卡 `bs=24` 是当前较优，`bs=56` OOM；如果收益有限，不继续硬挖 kernel。

结果：
- `with_cp=True` 到 `with_cp=False`：`1.1399s/iter -> 1.0283s/iter`，吞吐提升 `10.85%`。
- 显存约 `32.6GB -> 59.5GB`，147GB 卡可接受。

可复用原则：
- 用户说“尽量不改代码”时，要把 no-code 配置/运行时优化跑完并记录无收益项。
- 如果自定义 kernel 不是主耗时，不要为单点小收益引入维护成本。

## Sparse4D / deformable aggregation

用户目标：重写 deformable aggregation，性能提升小则不改；改动需备份。

关键经验：
- 当前工作区已有 deformable aggregation 改动，先当作用户基线，备份源码、生成 HIP 文件和 `.so`。
- 发现 `gfx938` 下特化 backward 的原子分支只包 `__gfx936__`，导致 `grad_mc_ms_feat` 漏写为 0。优化必须先修正确性。
- 修复后再做性能：去掉 backward 无用大 clone、消除 forward 无竞争 atomic、补 launch bounds、收窄 arch 宏。
- 单 op 结果强，但仍跑 8 卡端到端 `iter 100-200` 验证。
- batch size 摸高用吞吐判断；`bs=48/GPU` 吞吐最高但显存高，按用户“摸高性能”需求采用。worker 不盲目加，`w=24` 比 `w=15` 慢。

结果：
- backward 算子估算：`13.883/26.261/50.822 ms -> 3.201/5.969/11.488 ms`（bs=1/2/4）。
- 端到端原 batch：旧日志 `1.4699s/iter`，新结果 `1.2736s/iter`，提升 `13.36%`。
- batch sweep：`bs=15` 吞吐约 `94.22 samples/s`；`bs=32` 约 `105.40`；`bs=48` 约 `108.12`，但显存约 `113.5GB/GPU`。

可复用原则：
- kernel 提速前先修 gradient correctness。
- arch 宏要覆盖当前卡型，但不能破坏旧 arch 编译。
- batch/worker 是独立变量，不能一起扫。

## MapTRv2 / profiler OOM and 8-GPU slowdown

用户目标：定位启动性能异常和 profiler OOM；后续把 8 卡性能调回正常，不影响精度。

关键经验：
- profiler 被硬编码开启，8 卡每个 rank 都写 trace，第 1 step 和第 22 step flush 严重污染性能。
- `torch.compile + profiler + cudagraphs + CPU boundary + GT valid 数变化` 可复现 boolean mask indexing 假大分配，例如 `666GiB/1190GiB`。关闭 profiler 可绕过这类 OOM。
- 关闭 profiler 后的新 OOM 是另一类：DataLoader `pin memory thread` 触发 HIP OOM，不是普通 CPU DRAM 不足，也不是加内存条一定解决。
- 8 卡巨大裂化不是 RCCL 链路慢：1GiB all-reduce 约 `0.014s`，算法带宽约 `131GB/s`。
- 真正的多卡慢由 CPU/DataLoader/线程池和 DDP unused 检测放大：原配置 `workers_per_gpu=48`，8 卡即 384 worker；OpenCV/torch/BLAS 默认线程会指数级放大。
- 固定 unused 参数场景可用 `static_graph=True`，避免每轮 `find_unused_parameters=True` 扫图；前提是确认 unused 集合固定，且不减少训练计算。

保留改动：
- 启动脚本加线程限制：`OPENCV_FOR_THREADS_NUM=1`、`OMP_NUM_THREADS=1`、`MKL_NUM_THREADS=1`、`OPENBLAS_NUM_THREADS=1`、`NUMEXPR_NUM_THREADS=1`。
- `workers_per_gpu=2`，`samples_per_gpu=12` 保持。
- `find_unused_parameters=False` + `ddp_static_graph=True`，并让训练封装读取 `ddp_static_graph`。
- MSDA 改为优先使用 `lightop.op`，fallback 到 mmcv `_ext`，并适配 pybind 位置参数。

结果：
- 单卡约 `1.25s/iter`，异常 8 卡约 `6.36s/iter`。
- 线程限制 + workers 降低 + static graph 后，8 卡回到约 `1.46-1.57s/iter`。
- 8 卡吞吐约 `65.8 samples/s`，相对单卡约 `6.8x`，scaling efficiency 约 `85%`。

可复用原则：
- OOM 要按栈分类：fake GPU allocation、pin memory、CPU allocator、VMFault 不是同一个问题。
- 复现脚本默认参数必须贴近真实形状；压力测试要显式 `--case stress`，避免误报。
- BS sweep 脚本如果没生效或用户叫停，应清理 `/tmp` 产物和后台任务。

## BEVFormer / DCNv2 hipDNN combination

用户目标：优化 BEVFormer，要求先看 rocBLAS 自动选优，再按 profiler 找瓶颈。

关键经验：
- profiler 显示主瓶颈不是普通 GEMM，而是 DCNv2 `modulated_deformable_*` 前后向；rocBLAS 不是主杠杆。
- workspace 根目录已有 `modulated_deform_conv.py`，但当前 Python 实际加载 site-packages 的 mmcv 实现；需要确认 import/registry。
- 直接替换 MMCV 文件可以让 DCN microbench 接近项目内方案，但端到端仍慢，因为缺少本地 override 的缓存、layout 和 GridMask 配套。
- hipDNN graph cache 是关键：torch.compile/Dynamo 下 tuple/SymInt key 会出现“打印相同但反复 miss”，导致每轮重建图。将 cache key 压成纯字符串后，端到端恢复到 `1.7-1.8s`。
- stride=1 DCNv2 走 hipDNN；stride=2 或不支持 shape 走 fallback。保持 channels_last，避免额外 NCHW contiguous。
- profiler 默认开启会污染 benchmark，改为显式开关；benchmark 用 max-iter hook 自动停。
- GridMask `rotate=1` 实际旋转角为 0 时，走 GPU 快路径，避免无意义 PIL 转换。

结果：
- baseline：`2.5934s/iter`。
- 只替换 mmcv 文件：`2.5571s/iter`。
- 项目内组合方案最终：mean `1.7711s`、median `1.7657s`（iter 100-200），提升约 `31.7%`。

可复用原则：
- 算子 microbench 一致不代表端到端一致；图缓存、layout、Python 包装和预处理都会决定最终速度。
- 修改安装包要慎用，优先项目内注册 override；如果用户要求替换 site-packages，必须备份并记录 hash。
