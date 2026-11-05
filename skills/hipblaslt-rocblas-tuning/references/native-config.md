# 原生配置与版本约束

## hipBLASLt

优先读取容器内当前 benchmark `--help`、头文件和配置解析器。既有 NMZ/DTK 构建使用字符串枚举：

```text
--algo_method heuristic --requested_solution -1
--api_method c --workspace 0 --cold_iters 3 --iters 10
--initialization rand_int --print_kernel_info
HIPBLASLT_TUNING_FILE=<each-point.config>
```

`--algo_method 0` 在该构建不可用；只计时默认 heuristic 一项也不等于完成搜索。按 index 测量的命令可能是 `--algo_method index --solution_index <index>`，先核对当前 help。大尺寸 `--verify/-v` 可能执行昂贵 CPU reference，按当前库能力选合适验证策略，不以没报错代替数值验证。

既有 native 格式首行为精确构建标识，之后**每个记录前重复 header**，行首四空格，使用 LF：

```text
Git Version: 15b13d25-dirty
    transA,transB,...,m,n,k,...,us,solution_index,gcnArchName,CUs
    T,N,...,65536,4096,1536,...,2643.97,INDEX,gfx938:sramecc+:xnack-,64
    transA,transB,...,m,n,k,...,us,solution_index,gcnArchName,CUs
    T,N,...,65536,4095,1536,...,2643.97,INDEX,gfx938:sramecc+:xnack-,64
```

省略号仅说明布局，不能拿此示意当可加载 config。使用真实 bench 产生的完整列；`gemm_plan.py` 逐列保留再更新目标维度/派生 stride。原始 `us`、Gflops、rotating_buffer 来自源 benchmark，复制行不会产生目标测量值；后者在 `all-m.csv` 和 mapping 单独记录。solution index、Git Version、gcnArchName、CU 和 dtype 必须匹配当前库。

若当前部署的 override 格式不是此版本，改 writer 与 reader，先用一个完整点确认加载、核对 selected kernel，再批量生成；不能只让 CSV 语法解析通过。

## NMZ rocBLAS

这不是另一个 hipBLASLt override 文件。已验证的外部 vendor tuner 布局：

```text
rocblas-autotune/
  src/ source-all/ source-test/ source-quick/ configs/
  csv_size/csv/captured-powers.csv
  optimization_artifacts/custom/results/csv/{bf16,bss}_TN.csv
  optimization_configs/new/config/library_gpu6/
```

CSV 输入列：

```text
gemmtype,TransA,TransB,M,N,K,B,lda,ldb,ldc,ldd,stride_a,stride_b,stride_c,stride_d,alpha,beta
```

`bf16` 表示 BF16→BF16，`bss` 表示 BF16→FP32。当前适配器不把其他 dtype 强行映射进这两类。输入 flags 若 C/D dtype 不同、特殊 algo/flags 或额外 epilogue，需要先适配。

`roc_vendor.py prepare` 只复制必要 framework 源码到实验目录，并写 powers 输入、源码/config 哈希。不会安装框架。使用前确认 vendor 版本和其 Python/编译依赖已存在；运行 `tune` 会在隔离副本中编译并执行 GPU 搜索。该版本初始化器可能 chmod 自己目录、清空环境和设置 `ROCBLAS_UNSELECT_CHECK=1`，所以不能直接在共享原框架里运行，也不能把搜索环境继承到精度验证或模型。

当前适配器调用的私有 API：

```python
app = GemmTunerApp(config_path)
app._prepare_configs(runtime_root)
result = app._extract_sizes()
app._run_tuning(result, runtime_root)
app._generate_configs(result, is_final=False)
```

适配器检查方法/签名，不等于兼容所有 vendor 版本。若目录命名、ConfigMappings、生成逻辑改变，要检查当前源实现并更新适配器，不伪造生成成功。`generate` 避免再次调用会清空结果的构造器，用同构建配置从已补齐 CSV 重新生成 native 文件。

注意：

- `tuning_args.txt` 中 hardware_type、CU 和 GPU 列表要匹配设备；`update_target_config=0` 保证不更新全局配置。样例为单卡以方便隔离，按授权资源改为多卡。
- `fill-roc` 按 M/N/K/B、alpha/beta、ld 和可表示的 stride 匹配源点。vendor 输出可能不记录 ldd、stride_d；输入保留这些信息，单 batch 未使用的 A/B stride 可归零。
- native custom dispatch 可能只以 dtype/trans/M/N/K/B 为 key。若两套不同布局会产生同一 native key，脚本拒绝生成；这类情况需要模型侧区分 dispatch 或框架支持更丰富 key，不能“选一个覆盖另一个”。
- 最近复制后的 gflops 是源点数据，需保留来源，并在全 M 验证 CSV 记录实际耗时。
- 仅复制 powers 的 CSV 不会产生全部 dispatch。必须填充后重新生成 `.dat`/kernel TXT 等 native 文件，并带上当前系统 native 目录中未重新生成的必需文件/二进制。适配器仅补缺失文件，不替换系统库。
- `ROCBLAS_TENSILE_LIBPATH` 指向完整 **library_gpu6 目录**。不要指向 CSV、上层框架目录或不完整的 `.dat` 集合。
- 复制到其他节点后校验文件清单与 SHA256；绝对路径可以不同，但二进制、config 与构建必须相同。验证 provenance 中的路径发生迁移时应重新做当前环境清单与运行验证，不直接编辑哈希绕过检查。

## 历史样例，非当前实测承诺

2026-10-15 的 S1/S2、`yangyn-deepseek-w4a8-1014-2017`、gfx938/64CU、W4A8 INT8、CP8 运行：32768→1 捕获为本地 token cap4096，6 个 hip family、7 个 roc family；其中 logits cap1，总计157个搜索点、49153个整数目标形状。hip 有5个形状必须取下一个最近兼容点：一 family 的 M3/5/6→8，另两 family 的 M3→4。证明“最近复制后必须再检查”有实际必要。

该运行的 precision 是每形状128输出位置、整数合成分布的抽样。部分 kernel 有显著加速，但也有中间 M 退化；不得把某个最大加速比当全范围保证。32k 模型前后运行日志开关不同，旧 wall time 不能视为严格端到端性能结论。原始业务启动脚本、节点和路径仅为历史上下文，不作为 skill 默认启动行为。
