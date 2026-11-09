---
name: kernel-hip-optimize
description: 海光 HCU HIP/CK Tile kernel 迭代优化器。使用 hipprof→roofline 量化→ISA 验证（dccobjdump）→Branch 探索→Ablation 归因→经验记录的完整闭环，对 HIP kernel 进行多轮迭代优化。适用：需要对 HIP kernel 进行迭代深度优化。不适用：仅需一次性 roofline 分析的场景。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
---

# Hygon HIP Kernel Iterative Optimizer

## 本技能的功能

通过运行测量循环优化海光 HCU HIP 或 CK Tile kernel，以 Python 参考实现为基准：

1. 验证环境和 baseline/参考契约，
2. 使用 `hipprof` 对当前最佳 kernel 进行 profiling，
3. 将 compute、memory 和 latency 差距分类为轴预算，
4. 从 HCU 方法注册表选择优化方法，
5. 生成 K 个具有不同实现参数的分支 kernel，
6. 编译、验证和 benchmark 分支，
7. 对冠军 kernel 进行 profiling，消融所选方法，并使用 `dccobjdump` 验证 ISA，
8. 更新状态并输出最终总结。

使用确定性脚本进行环境检查、profiling、benchmarking、消融、ISA 检查、状态更新和总结。仅在方法选择、代码修改和修复时使用 agent 推理。

## 关键要点

1. **Roofline 风格的轴预算**：根据测量的 HCU 计数器和时序分配 compute、memory 和 latency 方法槽位。
2. **分支与选择**：为同一方法集生成多个变体，benchmark 所有有效分支，保留最快的冠军。
3. **消融归因**：仅在移除某个方法后明确损害冠军性能时保留该方法。
4. **HCU ISA 验证**：使用 `references/hcu_isa_signatures.json` 中的 `dccobjdump` 模式；最终证明是生成的 ISA，而非源码意图。
5. **源码支持的 builtin 纪律**：HCU 或 AMD 命名的 builtin 仅在调用形式有 HCU KB 源码、编译探测或现有项目代码支持时才是候选。单独的 `__has_builtin` 失败不足以拒绝源码支持的 builtin。
6. **CK Tile 优先**：对 GEMM/conv/norm/MoE 模板工作优先使用 CK Tile；不要直接移植 CUTLASS 假设。
7. **模糊情况深入搜索**：对于不清楚的硬件错误、无法解释的性能回归或不符合预期的编译器/工具行为，在猜测之前搜索本地 HCU 知识库和源码支持的参考项目。本地参考不足时允许网络搜索。

## 输入

开始前准备好以下内容：

- baseline kernel 文件：`.hip`、`.cu`、`.cpp`、`.cc`、`.cxx` 或 `.py`
- Python 参考文件，暴露 `reference(**kwargs)`
- 维度 JSON，如 `{"N":1048576}` 或 `{"M":4096,"N":4096,"K":4096}`

如果用户仅提供参考文件和 shape，首先使用同级 `kernel-hip-baseline` skill 生成并通过正确性验证 `kernel.hip` 和 benchmark 兼容的 `ref.py`。在生成的 baseline 通过 preflight 和 benchmark 正确性验证之前，不要开始优化迭代。

还接受结构化的上游交接：

- advisor 导出的 `kernel_handoff_manifest.json`，或
- 包含 `kernel_handoff_manifest` 的 `optimization_context.json`

消费该 manifest 时，至少读取：

- `routing.recommended_route`
- `routing.handoff_ready`
- `handoff_targets.kernel_optimizer`
- `handoff_targets.baseline_generator`
- `operator_contract.dims`
- `operator_contract.ptr_size_hint`
- `hotspot`
- `evidence`

不要将 manifest 视为 optimizer 可以开始的证明。仅在以下情况直接开始：

- `handoff_targets.kernel_optimizer.ready == true`

如果 manifest 仅标记 `baseline_generator.ready == true`，先经过 baseline-generator 阶段，等待正确性验证通过的 `kernel.hip + ref.py`。

可选：

- 迭代次数，默认 `3`
- `--ncu-num`，保留为 HCU 的 top-K 指标计数（与 CUDA skill 兼容）
- 每迭代分支数，默认 `4`
- `--ptr-size`，当 benchmark 分配需要显式元素计数时
- warmup 和 repeat 计数，用于 benchmark 稳定性

如果必需输入缺失且无法推断，简短询问一次。

## 环境

当目标 HCU 在远程时，通过项目远程工作流运行 HCU 验证。当前工作流在加载 DTK/modules 后直接进入计算节点；不使用 Docker。保持源码编辑在本地，远程执行前同步。

`hygon_tmp/` 仅是一个临时空间，用于临时探测、冒烟测试 case、生成的跟踪、拉取的日志和其他验证产物。不要将 `hygon_tmp/` 下的固定文件名作为 skill 契约的一部分，也不要将其中生成的任何运行视为项目源码资产。

必需或期望的工具：

- `hipcc`
- `hipprof`
- `dccobjdump`
- `rocminfo`
- `rocm-smi`
- Python 3.10+ 及项目 benchmark 依赖
- CK Tile 头文件（用于 CK Tile kernel）
- 可选的 `/opt/dtk` 下的 DTK 分析工具，包括可用的 PMC/SQTT 相关工具

首先探测环境：

```bash
python <skill>/scripts/check_env.py --out ./env.json
```

探测记录 gfx 目标、DTK 工具、`hipprof` 可用性、`dccobjdump`、CK Tile include 发现和降级 profiling 标志。如果计数器不可用，继续使用时序、源码检查、有用的 SQTT、代码对象资源分析和 ISA 证据，但告知用户 profiling 已降级。

## 快速路径命令

常规运行使用 `orchestrate.py`：

```bash
python <skill>/scripts/orchestrate.py setup \
  --baseline ./kernel.hip \
  --ref ./ref.py \
  --iterations 2 \
  --branches 2 \
  --ptr-size 1048576 \
  --dims '{"N":1048576}'

python <skill>/scripts/orchestrate.py open-iter \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1

python <skill>/scripts/auto_kernel_optimize.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1 \
  --prepare-only

python <skill>/scripts/orchestrate.py close-iter \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1

python <skill>/scripts/orchestrate.py finalize \
  --run-dir ./run_YYYYMMDD_HHMMSS
```

`setup` 运行环境/preflight/状态初始化并播种 baseline。`open-iter` 对当前最佳进行 profiling 并写入 `hcu_top.json` 和 `roofline.json`。`auto_kernel_optimize.py` 根据测量证据选择方法并写入 `methods.json`、`analysis.md` 和分支 kernel。`close-iter` 验证方法、探索分支、对冠军进行 profiling、消融、运行 ISA 检查并更新状态。`finalize` 写入 `summary.md`。

对于 `setup` 后的常规自动循环，使用：

```bash
python <skill>/scripts/run_auto_loop.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --max-iters 3 \
  --branches 4 \
  --warmup 2 \
  --repeat 5 \
  --finalize
```

`run_auto_loop.py` 在需要时运行 `open-iter`，然后是 `auto_kernel_optimize.py`、`orchestrate.py close-iter` 和可选的 `finalize`，对每次迭代执行。在命令失败、接近峰值 roofline 或 `iterations_total` 时停止。

对于 `open-iter` 后的单次自动方法选择和分支准备步骤，使用：

```bash
python <skill>/scripts/auto_kernel_optimize.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1 \
  --prepare-only
```

要在无外部循环的情况下为单个迭代验证完整的 optimizer 状态机：

```bash
python <skill>/scripts/auto_kernel_optimize.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1 \
  --warmup 2 \
  --repeat 5 \
  --finalize
```

`auto_kernel_optimize.py` 当前实现证据驱动的方法选择加保守的分支具现化：

- 读取 `state.json`、`itervN/roofline.json`、`itervN/hcu_top.json` 和方法注册表；
- 读取 `references/kernel_family_catalog.json` 并输出 `itervN/kernel_family_guidance.json` 用于复杂族分类；
- 使用 roofline `axis_budget` 决定为 compute/memory/latency 选择多少方法；
- 从当前 `solve(...)` 契约检测生成器能力，包括平坦拷贝、平坦 elementwise、平坦 reduction、gather/scatter/index-add、逐行 softmax/layernorm、简单 matmul、不可转换和泛型可转换源；
- 匹配 P0 复杂 kernel 族作为咨询指导：
  - attention / QK / AV / causal mask / bias 融合；
  - gather / scatter / index_add / embedding backward；
  - jagged / ragged / sparse tensor 路径；
  - segmented reduction / 类 scan 的分组 reduction 设置；
  - 模型局部的自定义 autograd backward；
- 按直接 `hcu_top` 触发指标、SQTT 提示、代码对象资源压力、生成器能力、架构特性对同一轴的方法进行排序，然后以注册表优先级作为平局决胜；
- 生成注册表有效的 `itervN/methods.json`，包含 `hcu_evidence`、`trigger_strength`、`selection_score`、`generator_capability`、`expected_metric_shift` 和有效的 `skipped_higher` 原因；
- 默认保留一个 no-op 后备分支；
- 当当前最佳是可转换的时候，输出简单的方法驱动的 HIP 源码变体，当前包括指针 `__restrict__`、`#pragma unroll`、launch bounds 和简单 launch-block 几何变体的安全组合；
- 当来源契约被识别时，输出专门的分支生成器。当前内置的专门生成器覆盖：
  - 平坦拷贝：`float4` 向量化拷贝和每线程两元素拷贝变体；
  - 平坦 elementwise / scale / 类 AXPY 表达式：当右侧是安全的平坦表达式时，线程粗化和每线程四元素变体；
  - 平坦 reduction sum：块级共享内存 sum 与原子输出累积；
  - gather/scatter/index_add：粗化平坦索引变体，`index_add` 使用 `atomicAdd` 并依赖正确性门控处理重复索引语义；
  - 逐行 softmax：每块一行，使用共享内存 max/sum reduction；
  - 逐行 layernorm：每块一行，使用共享内存 mean/variance reduction 和可选的 gamma/beta 应用；
  - 简单逐行 reduction：每块一行处理逐行 sum/max 契约；
  - 简单逐行 top1：每块一行处理精确的逐行 argmax/top1 契约；
  - 平坦 fill：对简单 `out[i] = scalar_or_constant` 契约的粗化 fill；
  - 简单 `solve(A,B,out,M,N,K)` matmul kernel，使用 `A[row*K+k] * B[k*N+col]`：tiled LDS matmul 候选，具有 tile-size 和 launch-bound 变体；
  - CK Tile 模板透传，当 CK Tile 头文件可用且 `HYGON_CK_TILE_TEMPLATE=<source>` 指向经过验证的 `extern "C" void solve(...)` CK Tile 源时；
- 写入 `itervN/branch_plan.json` 以便失败或获胜的转换可以被审计；
- 写入 `itervN/kernel_family_guidance.json`，包含匹配的族、要捕获的契约字段、候选方法、语义陷阱、正确性门控、库引用和停止原因；
- 在分支探索后写入 `itervN/champion_methods.json`，当获胜分支仅实现所选方法的子集时。ISA 检查和状态更新随后使用冠军的实际声明，而不是过度归因每个选中的方法；
- 写入 `itervN/analysis.md`；
- 可选调用 `orchestrate.py close-iter` 和 `finalize`。
- 经过验证的运行后，可选使用 `scripts/record_kernel_experience.py` 记录可重用的经验。这会写入需要审核的 JSONL 目录条目以及 RAG 收件箱中的 Markdown 卡片；它不重建 RAG 索引或覆盖正确性门控。
- 使用 `scripts/review_kernel_experiences.py` 审核学到的经验卡片。默认仅报告；需要显式的 `--approve <id-or-file>` 将卡片标记为 `review_approved`。
- 审核后使用 `scripts/rebuild_rag_index_after_review.py` 重建 HCU RAG 索引。默认是 dry-run 且仅 BM25；完整的 FAISS 嵌入重建是显式的，因为可能代价较高。

这是有意保守的：分支候选在提升前仍必须通过编译、正确性、benchmark、hipprof 和 ISA 检查。对于泛型重写不安全或不适用的情况，使用 `--branch-mode noop` 或编写方法特定的分支生成器。

在 optimizer 运行后捕获可重用的经验：

```bash
python <skill>/scripts/record_kernel_experience.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --output-dir ./learned_kernel_experience
```

在重建任何 RAG 索引前审核生成的 Markdown。学到的条目是未来 agent 的候选知识；它们不替代语义、benchmark、奇偶校验、准确度或 profile-diff 门控。

审核后 dry-run 索引重建：

```bash
python <skill>/scripts/review_kernel_experiences.py \
  --inbox <repo>/knowledge-base/hygon-extend/kernel-optimization-catalog/learned-experiences \
  --report-json ./experience_review_report.json \
  --report-md ./experience_review_report.md

python <skill>/scripts/review_kernel_experiences.py \
  --inbox <repo>/knowledge-base/hygon-extend/kernel-optimization-catalog/learned-experiences \
  --approve <experience-id-or-md-file> \
  --reviewer <name> \
  --notes "semantic/benchmark/profile-diff gates reviewed"

python <skill>/scripts/rebuild_rag_index_after_review.py \
  --review-report ./experience_review_report.json \
  --mode bm25 \
  --execute
```

不要批量批准生成的卡片，除非 agent 已检查语义契约、benchmark 契约、正确性/奇偶校验证据和 profile-diff 或端到端证据。RAG 索引构建器跳过未标记为 `review_approved` 或 `approved` 的 `learned-kernel-experience` 卡片。

`kernel_family_guidance.json` 是建议性的。它应该指导 agent 推理和契约捕获，而不是强制补丁。如果指导匹配一个复杂族，agent 仍必须检查源码、验证算子契约、运行奇偶校验或模型冒烟测试，然后决定是否继续当前目标、切换目标或因剩余提升空间过小而停止。

## 如果输入是 advisor kernel handoff manifest

从 advisor 输出开始时，优先使用同级 baseline skill 的闭环驱动：

```bash
python <baseline-skill>/../kernel-hip-baseline/scripts/run_kernel_handoff.py \
  --manifest <kernel_handoff_manifest.json-or-optimization_context.json> \
  --out-root ./hygon_kernel_handoff_cases \
  --iterations 3 \
  --branches 4 \
  --auto-loop
```

不带 `--auto-loop` 时，驱动在 optimizer 设置后停止，并输出 optimizer `run_dir` 以及后续自动循环命令。带 `--auto-loop` 时，它通过 `run_auto_loop.py` 继续：证据选择、分支生成、编译/正确性/benchmark、冠军 profiling、状态更新和总结。

在任何 optimizer 命令前应用此门控：

1. 检查 `handoff_targets.kernel_optimizer.ready`。
   - 如果为 `true`，使用：
     - `handoff_targets.kernel_optimizer.baseline_kernel_path`
     - `handoff_targets.kernel_optimizer.python_reference_path`
     - `handoff_targets.kernel_optimizer.dims`
     - `handoff_targets.kernel_optimizer.ptr_size_hint`
   - 闭环驱动可以执行此直接的 `orchestrate.py setup` 调用。
2. 如果 `handoff_targets.kernel_optimizer.ready` 为 `false` 但 `handoff_targets.baseline_generator.ready` 为 `true`，不要启动优化。
   - 先运行 `kernel-hip-baseline` 以具现化 `kernel.hip` 和 `ref.py`。
3. 如果两者都为 `false`，停止并显示 manifest 的 `missing_fields`，不要发明 benchmark 契约。

仅使用 `hotspot` 和 `evidence` 来确定方法优先级和解释为何选择 kernel 路由。它们不替代 optimizer 所需的 baseline/reference/dims 契约。

如果闭环驱动以 `closed_loop_setup_ready` 或 `optimizer_setup_ready` 完成，从输出的 `optimizer_setup.state` / `optimizer_setup.run_dir` 继续正常的 optimizer 工作，通常是通过运行 `run_auto_loop.py`。如果它以 `optimizer_auto_loop_completed` 完成，检查 `<optimizer-run-dir>/summary.md`、`<optimizer-run-dir>/auto_loop_report.json` 和每个 `itervN/branch_results.json`。

## 详细循环

> 详细内容见 [详细循环：步骤 0-8](references/optimizer-loop.md)。

## Hygon 特定硬性规则

- 将 wavefront 大小视为 64。重新检查每个 CUDA warp-size 假设。
- 对 HCU 模板 kernel 使用 CK Tile 而不是 CUTLASS。
- 当可用时使用 `hipprof --pmc --pmc-type 3` 获取常规 PMC 风格数据。当 PMC 无法解释停顿且环境支持时，使用 SQTT/stat-stall 工具。
- 当内存读写行为重要时，除常规 `--pmc` 外，使用 `hipprof --pmc-read --pmc-type 3` 和 `hipprof --pmc-write --pmc-type 3`。捆绑的 profiler 默认使用 `--pmc-mode all` 并将这些 CSV 合并到 `hcu_top.json` 中。
- 编译后使用 `hipprof --codeobj-analyze <elf-or-so-file>` 检查 VGPR/SGPR/LDS 压力。将高寄存器压力视为寄存器控制、占用率和延迟决策的一级信号。
- 对模糊的停顿或指令流问题使用 SQTT，并在连续三次无实质性改进的迭代后自动考虑：`hipprof --sqtt --sqtt-type 1`、`stat_stall`、`stat_valu` 或 `all`，取决于跟踪大小。对于 JSON 优先使用 `--sqtt-output-type 0`，当跟踪较大时使用 `--sqtt-data-dir <dir>/`。使用 `scripts/analyze_sqtt.py` 分析生成的 `thread_trace_*.json`；当 Python `perfetto` 包可用时，使用 `scripts/analyze_perfetto_trace.py` 获取 PerfettoSQL 摘要。当它们是诊断探测而非运行产物时，将大型临时跟踪保留在 `hygon_tmp/` 下。
- SQTT 导出可能需要 `llvm-objdump` 在 `PATH` 中，因为 `hipprof` 在创建跟踪 JSON 时内部调用它。这不是 `dccobjdump` 的替代品：optimizer 的 HCU ISA 验证和模式检查仍必须使用 DTK `dccobjdump`。
- 当需要指令、寄存器、LDS 或占用率证据时，使用 `dccobjdump --inputs=<binary> --show-sass --show-instruction-encoding --separate-functions` 加 resource/symbol dump。
- 将没有相关 vector/global/matrix 指令的 dump 文件视为不确定，而非立即实现失败。
- 当硬件相关错误消息、profiler 症状、编译器 lowering 选择、waitcnt 危害或性能下降不清楚时，使用深度 HCU KB 搜索找到匹配的参考项目并检查它们的 kernel 如何实现相同模式。如果本地 KB 不足，在网络上搜索 ROCm/AMD/CK Tile/HIP 材料，并将其作为类比，直到 Hygon 编译和 ISA 验证确认。
- 对于内存方法，查找 HCU global/buffer/flat load/store 族、向量宽度、LDS 路径、合并症状，以及通过 LDS staging 时的 `buffer_load_*_lds` 或 `raw_buffer_load_lds`。
- 对于矩阵或 tensor 路径，记住海光 tensorcore 相关指令与 AMD 命名不同。仅将 AMD/ROCm/MFMA 材料作为类比，除非 `dccobjdump` 证明了最终的 Hygon `v_mmac` 或矩阵指令。
- 不要引入 FP4 策略；当前海光 HCU 目标不为此工作流暴露 FP4 硬件路径。
- 对于 gfx938，源码支持的 `__builtin_hcu_*` 转换、MMAC、matrix-load 和 DS-read 助手仅可使用 HCU KB 或现有源码示例中的确切签名。依赖之前先进行编译探测。
- 对于 gfx936，AMD 命名的 `__builtin_amdgcn_*` MMAC 形式和内联汇编模式仅在源码支持或探测支持时才是候选，然后由最终 ISA 验证。
- 不要从 AMD 文档、电子表格行或助记符猜测中发明 builtin 名称。
- 如果编译器调度或 lowering 阻止了优化，作为最后手段使用内联汇编，并添加所需的 `s_waitcnt`、`s_barrier` 和危害处理。
- 对于 global-to-LDS 和 LDS-to-compute 流水线，检查 global-load 消费者的 `s_waitcnt vmcnt(0)` 和 LDS/scalar 消费者的 `s_waitcnt lgkmcnt(0)`。
- 对于已知的 matrix/LDS 模式，有用的最终 ISA 族包括 `ds_read_m32x16_b16`、`ds_read_m32x16_b16_alt`、`ds_read_m32x32_b8`、`ds_read_m32x64_b4`、`ds_read_m32x8_b32`、`ds_permute_b32`、`ds_bpermute_b32`、`matrix_load`、`v_mmac`、`v_pk_*`、VOP3R/VOP3P 和资源等待指令。使用 JSON 签名进行精确匹配。

## Builtin 和汇编验证工作流

当方法需要 builtin 或内联汇编时：

1. 首先在 HCU KB 中搜索确切的 gfx 目标、builtin 名称、调用签名和源码示例。
2. 如果不确定，在特定任务的临时目录（如 `hygon_tmp/<probe-name>/`）下创建或更新最小编译探测。
3. 使用目标 `--offload-arch` 远程运行探测，使用你刚创建的实际探测路径，例如：

```bash
python3 <probe-path> --arch gfx938
```

4. 从方法实现中移除不支持的调用形式，或将其标记为该目标不可用。
5. 使用 `dccobjdump` 验证最终优化的 kernel；仅编译成功是不够的。

使用以下证据层次：

1. benchmark 正确性和时序，
2. `hipprof`/PMC/SQTT 瓶颈证据，
3. 源码支持的 builtin 或汇编可用性编译探测，
4. 最终 `dccobjdump` ISA 和资源证据。

## 模糊的硬件或性能行为

当 optimizer 遇到不清楚的 HCU 行为时，不要停留在通用 GPU 建议。按以下顺序继续调查：

1. 搜索本地 HCU KB，查找确切的 gfx 目标、工具输出、助记符、builtin、编译器诊断、profiler 计数器或 CK Tile 路径。
2. 检查 KB 找到的源码支持的参考项目，仅复制源码中可见调用签名、目标守卫、布局契约和等待规则的模式。
3. 如果本地证据不足，搜索网络上的 ROCm、AMD GPU、HIP、LLVM AMDGPU 或 CK Tile 参考资料。将这些发现标记为类比，直到 Hygon `hipcc` 和 `dccobjdump` 确认。
4. 在仓库根目录 `hygon_tmp/` 下的特定任务临时目录中构建最小编译或运行时探测。将探测输入、源码、日志、PMC read/write 输出、SQTT JSON/HTML/stat 文件、代码对象分析日志、dump 和摘要保留在那里，但不要将这些临时文件名作为稳定的工作流入口引用。
5. 将确认的发现反馈到分支实现、方法注释或参考文件中。移除或隔离不支持的假设。

对不清楚的错误、意外减速、profiler/工具矛盾、不支持的 intrinsic 问题、代码生成意外和疑似 waitcnt/LDS/MMAC 危害使用此路径。

## 失败模式

- `hipprof` 写入降级或空的指标：继续使用时序和 ISA 证据，但披露降级的 profiling。
- 硬件特定错误或不清楚的性能回归：深入搜索 HCU KB 和参考项目，可选使用网络来源作为类比，然后在 `hygon_tmp/` 中创建最小编译探测后再修改主 kernel。
- `dccobjdump` 找不到二进制文件或相关函数：在声明方法失败前检查编译产物和符号名称。
- 预期 ISA 模式在相关 dump 中缺失：将方法标记为实现失败，即使分支更快。
- 所有分支正确性或编译失败：修复源码并重试；不要从失败的分支更新方法归因。
- 冠军加速仅来自超参数：将归因较低的方法记录为无效，即使 kernel 更快。
- Builtin 存在于 AMD 材料中但不在 HCU 源码/探测中：不要将其用作 HCU 声明。
- `__has_builtin` 对源码支持的 HCU builtins 报告缺失：将该探测视为不确定，改为编译确切的调用形式。
- 远程 HCU 访问不可用：在 `hygon_tmp/` 下准备本地脚本/探测，请用户远程运行它们，然后处理返回的日志。

## 参考资料

仅在需要时加载参考资料：

- `references/optimization_catalog.md`：人类可读的优化目录，触发条件、跳过规则、组合指导和 HCU 特定策略。
- `references/method_registry.json`：结构化方法 ID、优先级、需求、签名和验证元数据。
- `references/hcu_metrics_guide.md`：hipprof/PMC/SQTT 指标、瓶颈解释和工具使用说明。
- `references/hcu_isa_signatures.json`：用于 HCU ISA 验证的 dccobjdump 模式组。
- `examples/walkthrough.md`：用于调试或演示工作流的完整演练。

## 输出契约

每次运行创建：

```text
<baseline-dir>/run_YYYYMMDD_HHMMSS/
|-- env.json
|-- state.json
|-- baseline/
|   |-- <baseline copy>
|   `-- bench.json
|-- iterv1/
|   |-- analysis.md
|   |-- methods.json
|   |-- hcu_top.json
|   |-- roofline.json
|   |-- best_input.hipprof.csv
|   |-- best_input.hipprof.log
|   |-- best_input.hipprof.codeobj_analyze.log
|   |-- best_input.hipprof.sqtt_analysis.json
|   |-- kernel.<ext>
|   |-- kernel.hipprof.csv
|   |-- kernel.hipprof.log
|   |-- kernel.hipprof.codeobj_analyze.log
|   |-- kernel.hipprof.sqtt_analysis.json
|   |-- bench.json
|   |-- attribution.json
|   |-- isa_check.json
|   `-- branches/
|       |-- b1/
|       |-- b2/
|       `-- ...
|-- iterv2/
`-- summary.md
```

最终面向用户的回答应报告最佳加速比、冠军路径、有效方法、实现失败的方法、profiling/ISA 注意事项以及无法运行的远程验证。
## 详细参考

- 详细循环：步骤 0-8：[references/optimizer-loop.md](references/optimizer-loop.md)
