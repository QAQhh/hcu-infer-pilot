---
name: kernel-hip-baseline
description: 从 Torch、Triton、TileLang、Python 或 CUDA/C++ 参考实现生成海光 HCU HIP/C++ baseline kernel 和正确性 harness。同时支持 CUDA→HIP/HCU 自动转换，产出正确性验证通过的可编译 HIP kernel baseline。适用：需要从已有实现快速生成 HCU HIP baseline kernel。不适用：已有完整 HIP 实现且通过正确性验证的场景。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
---

# Hygon HIP Baseline Generator

## 用途

在 `kernel-hip-optimize` 运行之前创建缺失的 baseline 阶段。本 skill 将参考实现 + shape 转换为包含以下内容的 case 目录：

- `kernel.hip`：保守的 HIP/C++ baseline，暴露 `extern "C" void solve(...)`；
- `ref.py`：benchmark 兼容的参考包装器，暴露 `reference(...)`；
- `baseline_manifest.json`：检测到的算子、签名、假设和后续命令；
- 可选的编译/正确性修复日志。

当用户提供 CUDA `.cu`、`.cuh`、C++ 扩展或 CUDA 库代码（而非 Torch/Triton/TileLang/Python 参考实现）时，也会处理 CUDA→HIP/HCU baseline 转换。在此模式下，产出仍是正确性优先的 HIP baseline + benchmark 兼容参考实现，但转换必须基于证据而非简单的重命名。

只有在 baseline 对参考实现通过正确性验证后，才启动迭代性能优化器。

路径规则：不要假设目标项目下存在 `skills/...` 目录。从已加载的 skill 文件解析脚本：

- `<baseline-skill>` 是包含此 `SKILL.md` 的目录。
- `<optimizer-skill>` 是同级目录 `<baseline-skill>/../kernel-hip-optimize`。
- 运行命令前，验证以下文件存在：`<baseline-skill>/scripts/inspect_ref.py`、`<baseline-skill>/scripts/generate_baseline.py`、`<baseline-skill>/scripts/run_kernel_handoff.py`、`<optimizer-skill>/scripts/preflight.py`、`<optimizer-skill>/scripts/benchmark.py`、`<optimizer-skill>/scripts/orchestrate.py`、`<optimizer-skill>/scripts/auto_kernel_optimize.py`、`<optimizer-skill>/scripts/run_auto_loop.py`。
- 对于没有 advisor manifest 的原始输入，优先使用 `<baseline-skill>/scripts/extract_contract.py` 创建与 `run_kernel_handoff.py` 消费的相同的 `kernel_handoff_manifest.json` 契约。

## 输入

必需：

- 参考或源文件：通常是 `.py`，包含 Torch、Triton、TileLang 或混合 Python 代码；或者是需要 HIP/HCU 转换的 CUDA/C++ 源文件，如 `.cu`、`.cuh`、`.cpp`、`.cc`、`.cxx` 或扩展代码；
- shape JSON，例如 `{"N":1048576}` 或 `{"M":1024,"N":1024,"K":1024}`。

还接受结构化的上游交接：

- advisor 导出的 `kernel_handoff_manifest.json`，或
- 包含 `kernel_handoff_manifest` 的 `optimization_context.json`

消费该 manifest 时，至少读取：

- `routing.recommended_route`
- `routing.handoff_ready`
- `hotspot`
- `operator_contract.preferred_reference`
- `operator_contract.reference_candidates`
- `operator_contract.dims`
- `operator_contract.ptr_size_hint`
- `handoff_targets.baseline_generator`
- `next_actions`

不要假设 manifest 总是意味着"立即开始"。它也可能表示"kernel 路由被阻塞"或"契约不完整"。如果 `handoff_targets.baseline_generator.ready != true`，先列出缺失字段，而不是伪造输入。

可选：

- case 输出目录；
- dtype/容差假设；
- 当参考实现返回 tensor 时的预期输出名称；
- 用于验证的远程 HCU 设备 ID。
- 已有的 baseline kernel 文件。如果用户已有 `kernel.hip`/`.cu`/C++ 加 `ref.py` 和 dims，使用 `extract_contract.py --baseline ... --ref ... --dims ...` 创建 `kernel_optimizer.ready=true` 的 manifest 并跳过 baseline 生成。

如果 ref 文件未明确暴露可运行的 Python oracle，先为最可信的路径创建包装器。Triton 和 TileLang kernel 通常是实现参考而非正确性 oracle；当同一文件中有 Torch 等效实现时优先使用。

如果输入是 CUDA 源文件，保留原始文件并在生成的 case 旁边创建转换后的 HIP 产物。不要覆盖用户的 CUDA 源文件。优先使用诸如 `kernel_original.cu`、`kernel.hip`、`hipify_report.md`、`cuda_to_hip_manifest.json` 等名称，或将相同信息包含在 `baseline_manifest.json` 中。

## 工作流

### 0. 需要时提取标准交接契约

如果用户仅提供 Python 参考实现和 dims，先创建 manifest：

```bash
python <baseline-skill>/scripts/extract_contract.py \
  --ref ./ref.py \
  --dims '{"N":1048576}' \
  --out ./kernel_handoff_manifest.json
```

如果用户已有经过验证或有候选资格的 HIP/CUDA/C++ kernel 加 Python 参考实现，创建 optimizer-ready 的 manifest：

```bash
python <baseline-skill>/scripts/extract_contract.py \
  --baseline ./kernel.hip \
  --ref ./ref.py \
  --dims '{"N":1048576}' \
  --out ./kernel_handoff_manifest.json
```

提取器是保守的。缺少 dims 或 Python oracle 时会阻塞。它不验证 dtype/layout 语义；benchmark 正确性门控仍然是权威的。

对于已有的 HIP/CUDA/C++ kernel，manifest 还记录：

- 解析出的 `solve(...)` 签名，
- const 指针输入、可变指针输出和标量 dims，
- 结构化的 `operator_contract.semantic_fields`，覆盖参数数量、指针 dtype 混合、动态 shape 标量、步长/layout 提示、掩码元数据、ragged/jagged 元数据、workspace 缓冲区、可能的 in-place 别名、索引参数和原子操作使用，
- 检测到的算子族，如 `flat_copy`、`flat_elementwise`、`flat_axpy`、`flat_reduction_sum`、`gather`、`scatter`、`index_add`、`softmax`、`layernorm` 或 `matmul`，
- 当源 shape 可识别时支持的 optimizer 端生成器。

如果签名无法解析，提取器将交接标记为阻塞，而不是让 optimizer 稍后在 `benchmark.py` 中失败。

### 1. 如果输入是 advisor 或提取的 kernel handoff manifest

优先使用闭环驱动：

```bash
python <baseline-skill>/scripts/run_kernel_handoff.py \
  --manifest <kernel_handoff_manifest.json-or-optimization_context.json> \
  --out-root ./hygon_kernel_handoff_cases \
  --iterations 3 \
  --branches 4
```

此默认模式验证交接，生成或解析 benchmark 契约，并运行 `kernel-hip-optimize` 设置。要在同一命令中运行深度 kernel 优化循环，添加 `--auto-loop`：

```bash
python <baseline-skill>/scripts/run_kernel_handoff.py \
  --manifest <kernel_handoff_manifest.json-or-optimization_context.json> \
  --out-root ./hygon_kernel_handoff_cases \
  --iterations 3 \
  --branches 4 \
  --auto-loop
```

当目标环境或 manifest 质量不确定时，先使用 `--dry-run`：

```bash
python <baseline-skill>/scripts/run_kernel_handoff.py \
  --manifest <kernel_handoff_manifest.json-or-optimization_context.json> \
  --out-root ./hygon_kernel_handoff_cases \
  --dry-run
```

驱动按以下决策顺序执行：

1. 检查 `routing.recommended_route`。
   - 如果不是 `kernel_optimization` 或 `framework_operator_rewrite`，默认不启动 baseline 生成。
2. 如果 `handoff_targets.kernel_optimizer.ready == true`，跳过 baseline 生成，直接调用 optimizer `orchestrate.py setup`。
3. 否则检查 `handoff_targets.baseline_generator.ready`。
   - 如果为 `false`，停止并报告 `missing_fields`。
4. 读取：
   - `operator_contract.preferred_reference.path`
   - 后备 `operator_contract.reference_candidates[*]`
   - `operator_contract.dims`
   - 可选 `operator_contract.ptr_size_hint`
5. 使用首选的本地 Python 源作为自动 baseline 输入。
   - 如果首选候选项是 CUDA/C++/HIP 或框架源（如 ATen 内部代码），停止并返回 `unsupported_reference_contract`，除非用户明确要求手动转换。
6. 生成 `kernel.hip`、`ref.py`、`baseline_manifest.json`，然后调用 optimizer `orchestrate.py setup`。
7. 将 advisor manifest 携带到 case 目录中，保存为 `advisor_kernel_handoff_manifest.json`。不要覆盖它。
8. 如果设置了 `--auto-loop`，调用 optimizer `run_auto_loop.py` 运行证据驱动的方法选择、分支生成、分支验证、冠军 profiling、归因/状态更新，以及可选的最终总结。

需要查看的输出：

- `<case-dir>/handoff_run_report.json`：交接决策、命令、设置状态，以及启用时的 auto-loop 状态。
- `<case-dir>/baseline_manifest.json`：当需要 baseline 生成时生成的 baseline 契约。
- `<optimizer-run-dir>/auto_loop_report.json`：当启用 `--auto-loop` 时的自动迭代报告。
- `<optimizer-run-dir>/summary.md`：循环完成时的最终 kernel 优化总结。

### 2. 检查参考实现

运行：

```bash
python <baseline-skill>/scripts/inspect_ref.py \
  --ref <ref-file> \
  --dims '<shape-json>' \
  --out <case-dir>/ref_analysis.json
```

在 PowerShell 上，优先使用 `--dims-file <case-dir>/shape.json` 或显式转义 JSON 引号。

编写 kernel 代码前读取 `ref_analysis.json`。它识别导入、函数、装饰器、可能的参考函数、tensor 参数、in-place 输出参数、返回风格和算子族。

算子族提示是有意保守的：

- `matmul`：`torch.matmul`、`@`、`tl.dot`、类似 GEMM 的 TileLang 调用，或 dims 包含 `M,N,K`；
- `elementwise`：向量形参考实现，包含简单算术、激活、掩码或单输出映射；
- `reduction`：`sum`、`max`、`mean`、norm、类 softmax 模式；
- `unknown`：需要 agent 根据源码检查编写 baseline。

### 3. 需要时转换 CUDA 输入

当源是 CUDA/C++ 而非直接的 Python/Torch/Triton/TileLang oracle 时，在正常的 scaffold/验证之前创建 HIP/HCU baseline。使用以下证据顺序：

1. 首先搜索本地 HCU RAG KB。从 AMD/NVIDIA 对比条目和 CUDA→HIP 映射表开始，特别是：
   - `comparisons/hip-cuda-programming-comparison.md`
   - `comparisons/rocm-vs-cuda.md`
   - `amd-knowledge-base/layer-2-compute-stack/hip/cuda-to-hip-porting.md`
   - `amd-knowledge-base/layer-6-extended/optimize-guides/L2-optional/cuda-runtime-api-hip.md`
   - 当出现这些 API 时，库特定的映射表如 `cublas-api-hip.md`、`cusparse-api-hip.md`、`curand`、`cufft`、`cusolver` 和 `cub` 映射。
2. 使用 ROCm HIPIFY 文档作为上游规则来源。对于生产环境或复杂 C++，优先使用 `hipify-clang`，因为它用 Clang 解析 CUDA 并报告转换失败；仅对快速/简单代码使用 `hipify-perl`。对于 PyTorch CUDA 扩展、基于 CMake 的 PyTorch 子模块或具有自定义 include 重写的项目，查阅并遵循官方 `ROCm/hipify_torch` 仓库模式和自定义映射支持。
3. 在目标环境中有可用工具时运行自动 hipify 过程，保留日志：
   - `hipify-clang <file.cu> --cuda-path=<cuda-path> --print-stats -- <includes-and-defines>`
   - 或 `python hipify_cli.py --config-json <config>` 用于 `hipify_torch` 风格的项目。
   如果存在 `compile_commands.json`，优先使用它，使 include 路径和宏与实际构建匹配。
4. 手动审查每个未转换的符号、警告、include、宏、启动包装器、库调用和设备 intrinsic。HIPIFY 是起点，不是正确性证明。

对于缺失或不确定的映射，在判断 API 不受支持之前搜索远程 DTK/ROCm 安装。某些类 CUDA 函数不在 KB 或公开文档中，但存在于已安装的 DTK 头文件或库中。

使用目标项目的远程工作流检查实际 HCU 环境。搜索可能的根目录如 `/opt/dtk`、`/opt/rocm`、`/usr/include`、项目提供的 CK/hip 头文件和活跃的 conda 或 module 路径。有 `rg` 时优先使用：

```bash
rg -n "cudaFunction|cuFunction|hipFunction|rocFunction" /opt/dtk /opt/rocm /usr/include 2>/dev/null
```

如果确切的 CUDA 名称不存在，尝试系统性的替换和库族变体：

- `cuda*` -> `hip*`，`cuda*` 常量/枚举 -> `hip*`
- `cu*` 驱动 API -> 可用的 `hip*` 模块/驱动风格 API
- `cublas*` -> 先 `hipblas*`，再 `rocblas*`
- `cusparse*` -> 先 `hipsparse*`，再 `rocsparse*`
- `curand*` -> 先 `hiprand*`，再 `rocrand*`
- `cufft*` -> 先 `hipfft*`，再 `rocfft*`
- `cusolver*` -> 先 `hipsolver*`，再 `rocsolver*`
- `cub::` -> 先 `hipcub::`，再 `rocprim::`
- CUDA 头文件如 `cuda_runtime.h`、`cuda_fp16.h` 和 `cuda_bf16.h` -> HIP/ROCm 等效头文件如 `hip/hip_runtime.h`、`hip/hip_fp16.h` 和 DTK 中验证过的可用 bf16 头文件。

不要仅凭命名对称就发明映射。只有在满足以下至少一个条件时才信任映射：

- KB 或 ROCm/HIPIFY 表格记录了它；
- `hipify-clang` 或 `hipify_torch` 转换了它，且后续审查未发现矛盾；
- DTK/ROCm 安装包含匹配的声明、包装器、示例或库符号；
- 使用 `hipcc` 的最小编译探测在目标 HCU 工具链上成功。

在 manifest 或报告中记录每个非显而易见的映射的证据：原始 CUDA 符号、选择的 HIP/HCU 符号、证据来源和任何注意事项。如果不存在可信映射，保留一个小型兼容性包装器或用支持的 HIP/ROCm 原语重写操作，然后在优化前验证正确性。

### 4. 搭建 baseline case

运行：

```bash
python <baseline-skill>/scripts/generate_baseline.py \
  --analysis <case-dir>/ref_analysis.json \
  --out-dir <case-dir> \
  --op auto
```

生成器处理常见的平坦 elementwise 和朴素 matmul baseline。对于不支持或模糊的 ref，让脚本生成包装器和 manifest，然后使用分析结果手动编辑 `kernel.hip`。

生成的代码故意保持简单。它应该正确且易于调试，而不是快速。

### 5. 尽可能本地验证，需要 HCU 时远程验证

使用 Hygon optimizer preflight 和 benchmark 脚本：

```bash
python <optimizer-skill>/scripts/preflight.py \
  --baseline <case-dir>/kernel.hip \
  --ref <case-dir>/ref.py \
  --dims '<shape-json>' \
  --out <case-dir>/preflight.json

HIP_VISIBLE_DEVICES=<device> python <optimizer-skill>/scripts/benchmark.py \
  <case-dir>/kernel.hip \
  --ref <case-dir>/ref.py \
  --ptr-size <num-elements> \
  --warmup 2 \
  --repeat 5 \
  --json-out <case-dir>/baseline_bench.json \
  --N=<N>
```

对于矩阵 shape，传递 `--M=<M> --N=<N> --K=<K>` 并将 `--ptr-size` 设置为足够容纳最大平坦输入/输出 tensor 的值，通常为 `max(M*K, K*N, M*N)`。

如果验证必须在远程 HCU 上运行，使用仓库的 `remote-ssh-docker-workflow` skill。如果生成的 case 是项目产物，保持在正常 case 目录中。仓库根目录下的 `hygon_tmp/` 仅用于临时探测和临时日志。

### 6. 在优化前调试正确性

在 baseline 正确性仍然失败时不要启动性能迭代。

使用以下修复顺序：

1. 检查 `preflight.json`、`baseline_bench.json` 和 benchmark stderr；
2. 确认 `solve(...)` 参数名称与 `ref.py reference(...)` 匹配；
3. 确认输出参数是非 const 指针参数，且参考实现以 in-place 方式写入它们；
4. 确认平坦 tensor 视图匹配 shape：elementwise `N`、matmul `A[M,K]`、`B[K,N]`、`C[M,N]`；
5. 缩小到小 shape 并添加临时调试打印或 CPU 端参考检查；
6. 只有在正确性通过后才移除调试代码并继续。

使用 `references/ref_to_baseline_patterns.md` 获取框架特定的转换模式。

### 7. 交接给优化器

在 `baseline_bench.json` 报告正确性通过后：

```bash
python <optimizer-skill>/scripts/orchestrate.py setup \
  --baseline <case-dir>/kernel.hip \
  --ref <case-dir>/ref.py \
  --dims '<shape-json>' \
  --ptr-size <num-elements> \
  --iterations <user-selected-iterations> \
  --branches <branches-per-iteration>
```

迭代次数不由本 skill 选择。如果用户未提供，请询问用户。

## 规则

- 将参考语义视为真值的来源；baseline 速度是次要的。
- 保持生成的 HIP baseline 简单：每个输出元素一个线程，不激进做 tiling，不使用内联汇编，除非 baseline 无法简单表达否则不使用 CK Tile。
- 保留原始参考文件；生成适配器 `ref.py` 而不是重写用户文件。
- 如果原始参考返回一个 tensor，生成的 `ref.py` 必须将其复制到输出 tensor 中，以便现有 benchmark 可以比较输出。
- 如果原始参考修改了输出 tensor，在 `solve(...)` 中保留这些名称。
- 对于 Triton/TileLang 文件，不要假设被装饰的 kernel 是 oracle。如果存在纯 Torch 的 `reference`、`torch_ref`、`ref`、`forward` 或 `golden` 函数，优先使用。
- 对于 CUDA 输入，使用 HIPIFY/KB/DTK 证据创建保守的 HIP baseline，然后再进行性能工作。保留原始 CUDA 文件，记录映射证据，并对不确定的转换进行编译探测。
- 在 `baseline_manifest.json` 中记录不支持的假设；不要静默发明 dtype、layout、broadcasting 或 reduction 语义。
- 不要将 `hygon_tmp/` 用作已提交的接口。它仅是临时空间。

## 资源

- `scripts/inspect_ref.py`：基于 AST 的参考实现检查和算子分类。
- `scripts/generate_baseline.py`：包装器和保守的 HIP baseline 搭建。
- `references/ref_to_baseline_patterns.md`：针对 Torch、Triton 和 TileLang ref 的实用转换和调试指南。
