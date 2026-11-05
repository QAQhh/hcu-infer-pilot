# 操作流程与命令

以下在**用户指定的容器内**运行；`SKILL`、`RUN`、bench、库、GPU 路径均替换成当前真实值。脚本不含 SSH、容器启动或服务自动重启。不要把旧节点和旧镜像当默认环境。

## 1. 固定环境与抓取路径

保存节点/容器镜像 digest、模型/量化版本、SGLang commit 和 dirty diff、启动脚本副本及实际参数、TP/PP/EP/CP、prefill chunk cap、GPU 架构/CU、驱动/运行时版本、BLAS 动态库实际解析路径。用 `ldd`、进程 `/proc/<pid>/maps` 等验证加载来源，不能只看 `/opt` 的文件名。各 rank 一致性需逐节点确认。

在**获准执行该项实验**的专用服务启动副本中打开已确认支持的日志选项，既有 NMZ 构建用 `HIPBLASLT_LOG_MASK=32`、`ROCBLAS_LAYER=2`。基线清除继承的 tuning override。确认每个 rank 的日志不互相打断：优先当前库支持的独立 log 文件选项；不清楚选项时检查当前头文件/源码，不猜环境变量。记录所有 rank 文件。合并 stdout 可能把两条命令串到一行，提取器会拒绝，不能忽略被拒绝行就宣称 shape 全覆盖。

若服务已停止而本次只要求整理、分析或生成配置，停在离线步骤。若本次授权抓取/调优，则使用用户指定脚本副本启动；服务启动前后状态均记入实验记录。

```bash
SKILL=/absolute/path/to/hipblaslt-rocblas-tuning
RUN=/absolute/path/to/new-run
mkdir -p "$RUN"
python3 "$SKILL/scripts/identity.py" \
  --arch gfx938 --cu 64 --hipblaslt-git-version 15b13d25-dirty \
  --file /actual/path/to/libhipblaslt.so \
  --file /actual/path/to/librocblas.so \
  --file /matched/path/to/hipblaslt-bench \
  --out "$RUN/identity.json"
```

这些 arch/CU/version 是历史示例。Git Version 以当前匹配 bench 输出的 native 配置第一行为准。保存 `hipblaslt-bench --help`；旧 benchmark 与新库混用、枚举参数类型变化均会使搜索或索引失效。

## 2. 抓取输入 32768、输出 1

以 input_ids 指定长度，token-id 要在模型 vocab 内且非特殊 token，不用“32k 字符”代替。脚本会 warmup，再清空专用服务 prefix cache，记录日志 start/end 字节，然后只抓一个请求。执行期间服务不能混入别的流量。API 随版本变化时先查本地 SGLang 路由实现并适配，不把 HTTP 200 当 token 数正确。

```bash
python3 "$SKILL/scripts/capture_32k.py" \
  --base-url http://SERVICE_HOST:PORT \
  --out "$RUN/capture" --token-id 1000 \
  --log /shared/rank0.log --log /shared/rank1.log \
  --profile-dir "$RUN/traces"
```

`--log` 需要包含全部节点/rank；运行端须能直接读取这些文件，必要时先建立共享采集路径或按节点分别记录同一请求的字节边界。多节点 profiler 输出也必须汇总。核对 response 的 prompt_tokens=32768、completion_tokens=1、cached_tokens=0，检查每个 rank 的 trace 完整且 prefill 走到目标路径。prof 外层 `toks=32768` 可能是全局计数，CP 本地 M 要看实际 GEMM 参数/张量/kernel，不能只看外层标记。

```bash
python3 "$SKILL/scripts/gemm_plan.py" extract \
  --sources "$RUN/capture/log-sources.json" \
  --out "$RUN/captured.json" --rejected "$RUN/rejected.json"
```

截取失败或日志交织时保留失败记录并重新采集。异步日志须先确认写出完毕，必要时按明确的请求结束标记修正 end 边界；不能把尚未刷出的日志当作没有调用。

## 3. 确认 token 轴与 stride，生成计划

复制 `assets/layout-rules.nmz-tn.json` 为实验 rules。规则 match 按捕获 flags 选择，必须恰好命中一个规则；没匹配到的算子会报错而非静默省略。`token_axis` 为实际随 token 数变化的 BLAS 维度；`linear` 仅列已确认等于整数系数×tokenM 的 flags。其余 flags 固定参与 family key。

例如 INT8 TN：权重 `[out,K]` 左乘 activation `[tokenM,K]`，BLAS m=out、n=tokenM、k=K；strideB=K×tokenM、strideC/D=out×tokenM。多头 batch16：ldb=65536，strideB=4096 **固定**，C/D stride=1024×tokenM。不能给后者套单 GEMM 的 strideB 缩放。

捕获同 family 多个 token 长度能检验规则；只有一个长度时必须结合调用代码/布局确认，数学上整除不等于语义正确。

```bash
cp "$SKILL/assets/layout-rules.nmz-tn.json" "$RUN/layout-rules.json"
# 审核并按实际 family 修改 layout-rules.json
python3 "$SKILL/scripts/gemm_plan.py" plan \
  --captured "$RUN/captured.json" --rules "$RUN/layout-rules.json" \
  --identity "$RUN/identity.json" --out "$RUN/plan.json"
```

每个 family 独立取捕获最大 tokenM，不把 logits M=1 强行扩到4096。CP padding、chunked prefill、TP 分片可能改变 cap；如32k请求只抓到局部 chunk cap，需要先明确用户要覆盖的真实调度上限，再补充对应捕获。`1..cap` tokenM 也并不保证覆盖其他 batch、序列打包和算法分支。

计划 cap4096 → 13 点 `1,2,4,8,16,32,64,128,256,512,1024,2048,4096`；cap3000 → 同序列到2048，另加3000。

## 4A. hipBLASLt 搜索、兼容选择与完整 config

```bash
python3 "$SKILL/scripts/tune_hip.py" --plan "$RUN/plan.json" \
  --bench /matched/path/to/hipblaslt-bench --gpus 0,1,2,3 \
  --out "$RUN/hip-points"
```

默认 warmup3/iters10、workspace0，`--algo_method heuristic --requested_solution -1` 搜索多个候选。若模型使用不同 workspace，上述脚本和验证器要一起改成运行时值；不可把 workspace>0 结果放给 workspace0 的模型。脚本每个 GPU 一个 worker，完整保存命令、原生输出、solution index、源点耗时。输出目录须全新，不自动拿旧结果续跑。

可先生成**未验证副本**供审查，不用于最终交付：

```bash
python3 "$SKILL/scripts/gemm_plan.py" fill-hip \
  --plan "$RUN/plan.json" --points "$RUN/hip-points/points.json" \
  --out "$RUN/hip.provisional.config" --mapping "$RUN/hip.provisional.mapping.json"
```

随后执行第5节 hip 验证器：对全部 `1..cap` 按最近顺序调用 support check，跳过不兼容点并做精度/计时。使用验证结果生成最终配置：

```bash
python3 "$SKILL/scripts/gemm_plan.py" fill-hip \
  --plan "$RUN/plan.json" --points "$RUN/hip-points/points.json" \
  --validation "$RUN/hip-verify/all-m.csv" \
  --out "$RUN/hipblaslt.all-m.config" --mapping "$RUN/hip.mapping.json"
```

没有兼容点时停止，不用默认 kernel 隐藏空洞。正确性失败也不能仅因为另一个候选“更快”就忽略错误；诊断实现/布局并增加所需点，重新验证。

## 4B. rocBLAS NMZ 原生分支

读取 [native-config.md](native-config.md)。此分支依赖已有且版本匹配的外部 `rocblas-autotune`，skill 不提供该框架或二进制库。若环境使用 upstream Tensile/TensileLite 等不同调优器，应先适配当前原生生成流程，不能执行 NMZ 私有 API。

```bash
cp "$SKILL/assets/nmz-tuning-args.txt" "$RUN/tuning_args.txt"
# 将 gpu_ids、cu_count 等改为当前设备；不要启用覆盖系统库的设置
python3 "$SKILL/scripts/roc_vendor.py" prepare --plan "$RUN/plan.json" \
  --source /matched/path/to/rocblas-autotune \
  --vendor-config "$RUN/tuning_args.txt" --work "$RUN/roc-work"
python3 "$SKILL/scripts/roc_vendor.py" tune --plan "$RUN/plan.json" \
  --work "$RUN/roc-work" --runtime-root /actual/path/to/rocblas \
  --native-library /actual/path/to/rocblas/library_gpu6
```

备份 powers 结果到不可变副本，再最近点补齐。生成器输入目录中只能保留本次对应的结果 CSV；其他残留 CSV 会使来源校验失败。

```bash
cp -a "$RUN/roc-work/optimization_artifacts/custom/results/csv" "$RUN/roc-power-results"
python3 "$SKILL/scripts/gemm_plan.py" fill-roc --plan "$RUN/plan.json" \
  --source "$RUN/roc-power-results" --out "$RUN/roc-filled-results" \
  --mapping "$RUN/roc.mapping.json"
cp "$RUN/roc-filled-results/"*.csv "$RUN/roc-work/optimization_artifacts/custom/results/csv/"
python3 "$SKILL/scripts/roc_vendor.py" generate --plan "$RUN/plan.json" \
  --work "$RUN/roc-work" --native-library /actual/path/to/rocblas/library_gpu6
```

roc nearest CSV 此时仍为未验证副本；第5节全部目标 M 验证通过并确认 native kernel 命中后才可交付。如果某个最近 kernel 不支持目标 M，保留原 CSV，把该目标的 bestkernel 换成下一个最近同 family 候选，更新 mapping/provenance 后重新生成与验证。附带自动适配器对这类 roc 失败**直接报错**，不自动宣称已完成 fallback；按实际框架的支持查询/bench 结果实现适配或增加新点并重新规划。

## 5. 全整数 M 单算子精度和性能

先读 [validation.md](validation.md) 确认适用范围；其他 dtype/布局改用匹配验证器。

```bash
python3 "$SKILL/scripts/verify_operators.py" --library hipblaslt \
  --plan "$RUN/plan.json" --points "$RUN/hip-points/points.json" \
  --hipcc /actual/runtime/bin/hipcc --gpus 0,1,2,3 --out "$RUN/hip-verify"
python3 "$SKILL/scripts/verify_operators.py" --library rocblas \
  --plan "$RUN/plan.json" --hipcc /actual/runtime/bin/hipcc --gpus 0,1,2,3 \
  --roc-library "$RUN/roc-work/optimization_configs/new/config/library_gpu6" \
  --roc-mapping "$RUN/roc.mapping.json" --out "$RUN/roc-verify"
python3 "$SKILL/scripts/report.py" --library hipblaslt --plan "$RUN/plan.json" \
  --csv "$RUN/hip-verify/all-m.csv" --out "$RUN/hip-report"
python3 "$SKILL/scripts/report.py" --library rocblas --plan "$RUN/plan.json" \
  --csv "$RUN/roc-verify/all-m.csv" --out "$RUN/roc-report"
```

两个分支**顺序执行**，不能同时占同一 GPU。全 M baseline 可能很慢；调整迭代前估算所需时间，双方使用相同迭代数，不偷偷把 baseline 只跑一次。每行记录 baseline_us、tuned_us、speedup，family 汇总包含最大 M 的实际耗时、最低/中位/几何平均加速和退化数量。每次 `out` 使用新目录；重点尺寸至少独立重复3轮，报告中位数及波动。正式精度验收补真实分布与更完整输出 reference，不能用128点合成样本代替。

## 6. 运行时核对与交付

仅在用户授权模型运行时，把以下环境注入启动脚本**副本**，对所有对应 rank/节点生效：

```bash
export HIPBLASLT_TUNING_OVERRIDE_FILE=/absolute/run/hipblaslt.all-m.config
export ROCBLAS_TENSILE_LIBPATH=/absolute/run/roc-work/optimization_configs/new/config/library_gpu6
```

去掉抓取日志和搜索专用选项；另留一个可控 kernel 命中诊断运行，确认各 rank 读取路径、版本、selected solution/kernel 对应本次配置。hip 支持检查和直接按 index 验证通过不等于 runtime override 已命中；roc 不报错也不等于没有回落默认路径。复抓32k1的模型 prof 对照。需要严格端到端性能时，baseline/tuned 的 logging、profile、cache、warmup、输入等必须相同。

最终目录保留原始证据与完整 native config、哈希清单、plan、mapping 和全 M CSV。报告有无退化及处置；如需保留 baseline 解处理显著退化点，记录例外并重新验证、不能仍宣称全部按最近点复制。数据集精度仅在用户要求时另执行指定数据集/think 设置。按用户最新要求停止实验服务，保留产物路径；不要因为 skill 自带流程扩大执行范围。
