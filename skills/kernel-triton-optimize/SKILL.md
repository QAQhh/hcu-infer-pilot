---
name: kernel-triton-optimize
description: 海光 HCU/HCU Python/Triton kernel 的 roofline 驱动迭代优化器。通过固定配置 benchmark、xcu/hipprof profiling、本地 KB 知识检索、Triton IR/cache 捕获、dccobjdump ISA 验证、Branch 探索择优、Ablation 消融归因的完整闭环，对 Triton kernel 进行多轮迭代深度优化。覆盖 compute/memory/latency 三轴 18+ 优化方法，支持 gfx928/gfx92a/gfx936/gfx938/gfx946/gfx948 多架构。适用：需要对 HCU 上的 Triton kernel 进行 roofline 驱动的迭代深度优化。不适用：仅需单次 benchmark 或不需要完整迭代闭环的简单场景。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
  peer_of: kernel-triton-baseline
---

# Hygon Triton Kernel Optimizer

给定 `kernel.py` + `ref.py` + shape 选择 JSON / `--dims`，在用户选择的海光 HCU 运行时目标上使用固定配置（`--disable-autotune`）、本地 KB 证据、profiler 证据和 Triton IR/ISA 验证运行 roofline 引导的分支选择循环。

## 必需的输入

- `kernel.py` 暴露 `setup(**kwargs)` 和 `run_kernel(**kwargs)` — 这是用于优化的**输入 baseline**（固定配置 `DEFAULT_CONFIG`，`--disable-autotune`）。它必须包含/支持任务可能优化的每个 shape，无论是作为默认值、文件内 shape 表还是 case 逻辑。除非用户明确要求修改原生 case 源码，否则将此 case 根目录中的文件视为只读，并在 `run_YYYYMMDD_HHMMSS/` 下优化副本。
- `ref.py` 暴露 `reference(**kwargs)` — **仅 Python 可调用的正确性 oracle**。它可以是纯 Python/PyTorch、Triton、HIPC 或通过 Python 接口包装的其他后端；PyTorch **不是**必需的。非 Python 原始参考文件除非由 `ref.py` 包装，否则不兼容 benchmark。如果没有独立的 Python 参考是可行的，将原始 `kernel.py` 行为冻结在 `ref.py` 后面并优化一个单独的副本。
- Skill 流程的 shape 选择输入，如 shape JSON、`--dims` 或 case 支持的 `shape_list`。使用它选择一个 shape、一个子集或 `kernel.py` 支持的所有 shape 的默认值。

如果没有 benchmark 兼容的 `kernel.py`，或没有可调用的 `ref.py` / 冻结的原始 oracle，首先使用同级 `kernel-triton-baseline`。
选择要优化的具体 shape 后，此 optimizer skill 写入/更新 `shape.json` 作为运行的标准化 shape 选择记录。baseline 生成器不需要提供 `shape.json`。

**Benchmark 纪律：** `orchestrate.py` / `run_iteration.py` / `tune_configs.py` / `branch_explore.py` / `ablate.py` / `profile_*` 默认使用 `scripts/benchmark.py`，其默认模式仍运行一次 `reference()` 进行正确性检查但**不计时** `ref.py`。优化指标来自 `kernel.py`。仅在显式需要 `reference` 时序或 `speedup_vs_reference` 时传递 `--bench-reference`。

命令示例中的 `<skill>` 解析为运行时可用的已安装 skill 目录路径（例如此 `kernel-triton-optimize/` 目录的绝对路径）。

## 源码修改边界

将 case 的原生实现文件视为只读，除非用户明确要求更改它们。

- **不要**编辑 case 根目录中的源文件，如 `./demo.py`、`./kernel.py`、`./ref.py` 或原始 case 附带的其他手写 harness/源文件。
- 使用 `scripts/orchestrate.py setup` 创建 `run_YYYYMMDD_HHMMSS/`，然后仅在该运行目录中的文件上进行优化工作。
- 安全编辑的位置是 `run_YYYYMMDD_HHMMSS/` 下的运行拥有的副本和产物，例如 `baseline/kernel.py`、`iterv*/branches/*/kernel.py`、迭代报告、配置 JSON 文件和最终提升的输出如 `final_kernel.py`。运行的 `baseline/kernel.py` 是一个工作副本：可以为其适配 agent 调用、benchmark 兼容性、测试或完成 skill 工作流，但这些更改必须保留在运行目录内，不得复制回原生 case 源码。
- 此 skill 显式管理的 case 根目录中的控制和交付产物，如 `shape.json`、`dispatch_manifest.json`、`optimized_kernel.py`、`optimized_config.json`、`optimization_summary.md`、`final_bench.json`、`final_kernel_manifest.json`、`attempt_timeline.*` 和 `irs/`，可以在工作流需要时创建或更新。这些不得替代原生实现文件，除非用户明确要求。
- 如果更改原始 case 源文件会有帮助，先停下来询问用户，而不是静默修补原生实现。

## 运行时边界

Optimizer 需要 HCU 运行时证据，但不要求或依赖单独的远程执行 skill。选择的运行时目标可以是远程主机/容器、本地容器或当前 shell。

在生成证据的命令之前，识别运行时目标、工作目录、可见的 GPU/设备策略以及如果非本地执行时的回拷路径。使用当前上下文中可用的任何 shell、SSH、容器或编排机制。将本地 KB/源码检查保留在 agent/控制端；使用运行时目标进行 Triton/HIP/Python 执行、benchmark、`xcu`/`hipprof`、Triton cache/IR 提取、代码对象收集和 `dccobjdump`。

当用户选择直接/本地执行时，不要发明远程主机、容器、路径或 GPU。

## 核心循环

0. 原生 autotune 公平性预步骤：
   在接受或创建固定配置 `kernel.py` 之前，检查原始源文件中是否有 `@triton.autotune`。如果存在原生 autotune，首先对选定的目标 shape/key 运行原始 autotune 空间，捕获 Triton 获胜配置，然后才在优化包装器中移除/bypass autotune。将获胜配置烘焙到 `DEFAULT_CONFIG` 或通过 `--config-json` / `--config-path` 传递，并记录来源，如原生源路径/hash、autotune key/dims 和获胜配置。不要从后来的固定包装器推断或重建原生 autotune 搜索空间，也不要将 `tune_configs.py` 结果用作原生 baseline 获胜配置的证明。
1. Shape 选择和可选的 shape-family 规划：
   从 `kernel.py` 支持的 shape 中选择本次优化的具体 shape，然后将它们写入 `shape.json`。当 `shape.json` 中 shape 数量多或某个关键维度跨度大时运行 `scripts/shape_families.py`。最多使用 `small` / `middle` / `large` 三个族，每个族优化一个代表，然后用 `dispatch_manifest.json` 合并。每个族/代表必须能被 `kernel.py` 运行。
2. 设置：
   对每个选定的 shape/族运行一次 `scripts/orchestrate.py setup`，创建 `run_YYYYMMDD_HHMMSS/`，验证 `setup()` / `run_kernel()` / `reference()`，播种 baseline，对迭代 1 进行 profiling，并产出 `roofline.json`。不要对相同 dims 的持续优化重新运行 `setup`；用 `open-iter`、`close-iter`、`tune_configs` 和 `finalize` 复用已有的 `state.json`。
3. 语义预步骤：
   在配置/tile 调优之前，运行 Formula-First Analysis：推导每个输出公式，找到语义重写候选项，然后将它们与实际循环/索引/掩码代码协调。使用 `references/triton_semantic_prepass.md` 进行思维循环/prompt，使用 `references/triton_optimization_memory.md` 进行历史 case 回顾：直接匹配、类比启发、拒绝条目和重用守卫。在 `iterv1/analysis.md` 中记录 `## Kernel Computation Logic`、`## Formula-First Analysis`、`## Loop / Candidate Inventory` 和 `## Semantic Pre-Pass Result`，但不要强制表格；优先考虑算法优化候选项和尝试/拒绝/推迟的证据。仅提升与 `ref.py` 等效且有计时证据的重写。在 `attempt_timeline.json` 中将更改源码的重写记录为 `semantic_rewrite`；`tune_configs.py` 将后续 sweep 记录为一个合并的 `config_tune` 事件。
4. 固定配置调优：
   在可能时推断有限的配置 key/range，可选写入 `iterv{i}/tuning_space.json`，并使用 `--disable-autotune` 纪律运行 `scripts/tune_configs.py`。Benchmark/profiling 产物必须记录 `bench.json.active_config`。
5. 每次迭代：
   运行/打开 profile 和 roofline，查询本地 KB，选择方法，编写分支 kernel，验证方法，关闭迭代，对冠军进行 profiling，捕获 Triton IRs/cache，运行消融，运行 ISA 检查，更新状态。
6. 最终调优：
   如果之前提升了任何源码重写/配置/分支/shape bucket，在最终化之前使用 `--final-tune --promote-if-better` 运行一次真正的最终调优迭代。
7. 最终化：
   运行 `scripts/orchestrate.py finalize`，然后验证最终交付物，仅在最终化门控通过或记录降级证据后编写简洁的最终回复。当任务优化多于一个 shape/case/族时，合成一个 case 级别的 `optimization_summary.md`，在一个紧凑表格中比较所有最终 shape，并指向每个运行的 `summary.md`、`final_kernel.py`、配置、benchmark、roofline 和 profile 产物。

文本等效（步骤 0 = 循环前；步骤 1–3 映射到核心循环 1、2+5、6–7）：

```text
0. check_env + preflight     → env.json；验证 setup()/run_kernel() 契约
1. orchestrate.py setup      → run_YYYYMMDD_HHMMSS/，播种 baseline，对 iter 1 进行 profile+roofline
   setup 是每个 dims/族一次性的；为所有后续步骤复用输出的 state.json
   Agent 语义预步骤   → references/triton_semantic_prepass.md 中的最小模板：
                        公式 + 循环/候选清单 + 结果；
                        references/triton_optimization_memory.md 中的历史 case 回顾；
                        可选源码重写（使用 scripts/record_attempt.py --kind semantic_rewrite
                        记录为 pending/success/failure，基于证据）；
                        当搜索空间已知时定义 tuning_space.json
   可选：tune_configs.py --search-level broad
                              → tune_results.json + accepted_configs.json + config_acceptance.md
2. for i in 1..N:
     a. open-iter（或 i=1 的 setup）：xcu best_input（-K kernel filter），hipprof fallback（--disable-autotune）→ hcu_top.json
     b. roofline.py：delta_c, delta_m, delta_l      → roofline.json + axis_budget
        如果 near_peak（所有 deltas < 0.15）→ 提前停止
     c. 在本地 agent/控制主机上 query_kb.py     → kb_evidence.* / kb_unavailable.json
     d. Agent 选择方法（每个轴 b_axis 个，上限=2） → methods.json + analysis.md
        validate_methods.py 在分支之前
     e. Agent 编写 K 个分支 kernel（相同方法，不同 tiles/configs）
     f. orchestrate.py close-iter / branch_explore → champion kernel + bench.json
     g. 如果 champion 失败：修复源码/配置并重试 close-iter
     h. xcu/hipprof champion（-K filter）+ Triton cache 捕获 → kernel.xcu 或 kernel.hipprof + irs/*/{.ttir,.ttgir,.hsaco}
     i. ablate.py                                  → attribution.json
     j. isa_check.py（dccobjdump + TTGIR patterns） → isa_check.json
     k. state.py update                            → state.json（+ 方法列表）
3-pre. 最终调优迭代（如果之前做了提升变更）
                              → iterv{last+1}/tune_results.json + accepted_configs.json；
                                 可能更新 state.best_config
3. orchestrate.py finalize    → summary.md、final_kernel.py（烘焙 DEFAULT_CONFIG）、cache archive；
                                 Agent 审核是否应将提升的优化追加到
                                 references/triton_optimization_memory.md 以供未来语义预步骤重用
   多 shape 打包      → case 级别 optimization_summary.md + optimized_kernel.py/config/manifest
                        当优化了多个具体目标 shape 时
```

## 最简命令流程

```bash
# 首先写入为此 optimizer 运行选择的具体 shape 写入 shape.json。
# 当 shape.json 包含多个 shape 或 shape 跨越大时的可选前置步骤。
python <skill>/scripts/shape_families.py \
  --shapes ./shape.json \
  --out ./shape_family_plan.json \
  --key-dim M

# 如果 shape_family_plan.json 有 required=true，分开运行 setup/open/close/finalize
# 对每个族代表 dims。传递 --shape-family small|middle|large
# 用于族运行，以便 state.json 记录为何存在多个 run_* 目录。
# 如果 ./kernel.py 是从带 @triton.autotune 的原生源派生的，在删除/bypass 它之前运行
# 原生 autotune 空间，然后通过 --config-json/--config-path 传递恢复到的获胜配置，
# 或将来源烘焙到包装器中。
# 如果原生源不兼容 benchmark，创建一个临时探测包装器，
# 原封不动地保留原始的 @triton.autotune configs/key。
python <skill>/scripts/orchestrate.py setup \
  --baseline ./kernel.py \
  --ref ./ref.py \
  --dims '{"N":16777216}' \
  --iterations 1 \
  --branches 2
# setup 创建 run_YYYYMMDD_HHMMSS/ 后，保持 ./kernel.py 和 ./demo.py 不变。
# 仅在运行目录副本/产物下编写所有 kernel 编辑。
# --dims 是必需的：始终传递为本运行选择的具体 shape。
# kernel.py 必须通过默认值、文件内 shape 表或 case 逻辑支持请求的 shape。
# setup 拒绝在已有 run_* 目录下的 baseline，并拒绝具有相同 dims 的重复同级运行。
# 仅为有意的隔离实验传递 --allow-nested-run-baseline 或
# --allow-duplicate-dims，并记录原因。

# 配置调优前的 Agent 端语义预步骤：
# 1. 在 iterv1/analysis.md 中填充来自 references/triton_semantic_prepass.md 的最小模板；
# 2. 检查 references/triton_optimization_memory.md 寻找可重用的模式；
# 3. 如果创建了更改源码的候选，显式记录：
#      python <skill>/scripts/record_attempt.py --run-dir ./run_YYYYMMDD_HHMMSS \
#        --iter 1 --kind semantic_rewrite --candidate "<name>" \
#        --status pending --outcome "candidate_created_before_validation"
#    在 ref.py 正确性 + 固定配置计时后，追加同一候选的 success/failure 事件。
#    tune_configs.py 将为后续 sweep 添加一个合并的 config_tune 事件；不要手动记录每个配置。
# 4. 当可调 key 清晰时，写入 iterv1/tuning_space.json。

python <skill>/scripts/tune_configs.py \
  --state ./run_*/state.json \
  --iter 1 \
  --op-kind memory \
  --search-level broad \
  --max-configs 64

# 如果 agent 编写了有限调优空间，显式传递它。
#   --candidates ./run_YYYYMMDD_HHMMSS/iterv1/tuning_space.json
# tune_configs.py 使用默认 benchmark 脚本，除非给出 --benchmark。

# 注意：profile_hcu.py 在 setup、open-iter 和 close-iter 期间由 orchestrate.py 自动调用。
# 对于 Python/Triton kernel，profile_hcu.py 委托给 profile_xcu.py，
# 它传递 xcu -K 自动（第一个 @triton.jit def 的前两个下划线 token，
# 例如 chunk_kda_fwd_* -> chunk_kda）。
# 使用 --kernel-name 覆盖；仅当需要所有 dispatch 时使用 --no-kernel-filter。
# 记录在 hcu_top.json 中作为 xcu_kernel_filter 和 selected_kernel。
# 在配置 sweep 或手动配置更改后独立调用 profile_hcu。
python <skill>/scripts/profile_hcu.py \
  --state ./run_YYYYMMDD_HHMMSS/state.json \
  --iter 1 \
  --which best_input \
  --config-path ./run_YYYYMMDD_HHMMSS/iterv1/accepted_configs.json \
  --disable-autotune
# 可选：--kernel-name chunk_kda   # 更严格的 xcu -K 子串
# 可选：--no-kernel-filter        # profile 每个 dispatch（慢，大）

# 或 profile 手动选择的固定配置：
# python <skill>/scripts/profile_hcu.py \
#   --state ./run_YYYYMMDD_HHMMSS/state.json \
#   --iter 1 \
#   --which best_input \
#   --config-json '{"BLOCK_SIZE":1024,"num_warps":4}' \
#   --disable-autotune

# 在编写 methods/branches 或 Hygon 特定配置注册表之前，在本地 agent/控制主机上运行。
# 使用从 env/state 检测到的目标架构。
python <skill>/scripts/query_kb.py \
  --out-dir ./run_YYYYMMDD_HHMMSS/iterv1 \
  --iter 1 \
  --target-arch <detected-gfx-arch> \
  --op-kind memory \
  --dims '{"N":16777216}' \
  --context "语义预步骤和 broad tuning 后的当前瓶颈，选定的 shape，kernel 模式，dtype 和疑似 Triton codegen 问题"

# Agent 编写 methods.json 和分支 kernel，然后验证方法。
python <skill>/scripts/validate_methods.py \
  --methods ./run_YYYYMMDD_HHMMSS/iterv1/methods.json \
  --state ./run_YYYYMMDD_HHMMSS/state.json \
  --registry <skill>/references/triton_method_registry.json

python <skill>/scripts/orchestrate.py close-iter \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1

# 在任何先前迭代提升了更快的源码重写/配置/分支/shape bucket 时，最终化前必需。
# 使用下一个迭代号。
python <skill>/scripts/tune_configs.py \
  --state ./run_YYYYMMDD_HHMMSS/state.json \
  --iter <final_tune_iter> \
  --which best_input \
  --op-kind memory \
  --search-level broad \
  --max-configs 64 \
  --final-tune \
  --promote-if-better

python <skill>/scripts/orchestrate.py finalize \
  --run-dir ./run_YYYYMMDD_HHMMSS

# 对于多族运行，在所有族运行后写入 dispatch_manifest.json 并验证合并的交付物。
# 对于任何多 shape/多 case 任务，还要编写一个 case 级别 optimization_summary.md，
# 比较所有最终化的 shape 并链接每个运行的 summary/artifact。
python <skill>/scripts/final_validate.py \
  --run-dir ./families/small/run_YYYYMMDD_HHMMSS \
  --case-dir . \
  --shape-family-plan ./shape_family_plan.json \
  --dispatch-manifest ./dispatch_manifest.json
```

## 循环输出

`iterv{i}/` 下的每次迭代输出通常包括：

- `methods.json`
- `analysis.md`
- `roofline.json`
- `hcu_top.json`
- `bench.json`
- `attribution.json`
- `isa_check.json`
- `kb_evidence.*` 或 `kb_unavailable.json`
- `attempt_timeline.json`
- `irs/`

`scripts/orchestrate.py setup`、`open-iter`、`close-iter` 和 `finalize` 是确定性的运行时目标步骤。Agent 端推理处理语义预步骤、KB 查询解读、方法选择、分支编写、失败修复和可重用记忆审核。

## 本地 KB 工作流

在 `setup` 或 `open-iter` 创建了迭代目录之后、编写 `methods.json`、分支 kernel 或配置注册表之前，在本地 agent/控制主机上运行 `scripts/query_kb.py`。从 `state.json.target_arch`、`state.json.env.primary_gfx_arch` 或 `env.json.primary_gfx_arch` 传递目标架构，加上 shape、op 类型、dtype、当前瓶颈和编译器/profile 症状。

使用额外的 `--query` 术语搜索确切的工具输出、错误消息、指令名称、Triton 特性名称或源项目提示。使用额外的 `--optimize` 术语进行工作负载特定的优化指导。

如果助手写出 `kb_evidence.*`，在 `analysis.md` 中引用相关发现，特别是针对 Hygon 特定的声明。如果它写出 `kb_unavailable.json`，继续使用本地源码检查、benchmark、Triton IR 和 ISA 证明，但明确标记迭代为 KB 降级。

在以下情况重新查询 KB：

- 目标架构变更；
- 瓶颈分类实质性变更；
- 所选方法依赖于 Hygon 特定的 lowering、builtins、MMAC/MLS 行为、buffer 操作或等待语义；
- 编译器诊断、Triton cache IR、profiler 指标或 ISA dump 与预期矛盾。

## 硬性规则

- **Baseline 公平性 — 原生 autotune 获胜配置**：如果原生/原始 kernel 使用 `@triton.autotune`，对每个目标 shape/key 与该确切原生 autotune 空间的固定配置获胜者进行比较。不要从后来的固定包装器重建空间，也不要将 `tune_configs.py` 结果替代原生获胜者。脚本强制 case：当 benchmark baseline 仍包含 `triton.autotune` 时，`orchestrate.py setup --baseline-autotune auto` 探测 Triton 的 `Autotuner.best_config` / `bench.json.active_config` 并在 `--disable-autotune` 下重新播种 baseline。Agent 证明 case：当包装器已移除 autotune 时，`orchestrate.py setup` 必须看到显式的 `--config-json` / `--config-path` 或包装器中的获胜者来源（例如 `AUTOTUNE_BASELINE_PROVENANCE` / `AUTOTUNE_WINNER_CONFIG` 包含原生源、源 hash、autotune key/dims 和配置）。没有该证据，setup 必须失败；不要继续使用降级的 baseline。如果原始没有 autotune，直接使用它。
- 固定配置证据是强制性的：传递 `--disable-autotune`，记录 `bench.json.active_config`，将纯配置加速视为固定配置获胜，除非消融证明了算法方法。
- 保持证据角色分离：本地 KB/源码检查保留在 agent/控制端；运行时目标生成 benchmark/profile/IR/ISA 证据。不要将本地 KB 安装到远程/运行时容器中。
- 不要在没有证明的情况下做 Hygon 特定的声明：MMAC layout、`tl.dot` lowering、`tl.matrix_load`/MLS、buffer 操作、指针窄化和架构差异需要本地 KB/源码证据加上相关的生成 IR/ISA。
- 优先空闲设备和 profiler 证据：在可能时使用空闲/最低利用率的 HCU；优先使用 `xcu`，显式标记 `hipprof` fallback，永远不要从事件时序中发明硬件带宽/利用率/cache 指标。如果设备不空闲或非独占，标记时序可能受污染；小增益不应作为最终结论呈现，并在可能时在空闲设备上重新运行。
- 证据层次（高到低）：本地 HCU KB / 可追溯源码 > 正确性 + 固定配置时序 > xcu 硬件计数器 > hipprof/PMC/SQTT fallback > Triton cache IR（`.ttir`、`.ttgir`、`.amdgcn`）> `dccobjdump` ISA（VGPR、LDS、occupancy）。不要仅从 `tt.load` 声明合并；对需要 ISA 证明但在 ISA 缺失时的方法不要默认 `verified=True`。
- Shape-family 纪律：在优化下一个族之前，检查前一个族冠军；普通的源码/配置改进可以传递，但 Split-K / Stream-K 风格的算法调度变更不得盲目在族间重用。这是必需的实践，不是 `methods.json` 方法。
- 不要将 aiter `fused_moe` 或 attention 业务代码复制到本 skill 中。仅将其用作配置设计和 shape bucket 的参考。
- 原生 case 源码保持冻结：`setup` 后，不要修补原始 case 根目录中的实现或 harness 文件。在活动的 `run_YYYYMMDD_HHMMSS/` 目录下编写 harness 适配、baseline 副本调整、kernel 重写、分支变体和提升的输出，除非用户明确要求运行目录外的源码更改。
- 对于 `xcu`，保持默认 kernel filter（`-K`）以便 setup/ref 噪声 kernel 不被 profile。如果 `hcu_top.json` 为空或 `selected_kernel` 错误，使用 `available_dispatches` 或 `kernel.xcu/*_dispatch_results_summary_info.csv` 中 GPU 符号的子串传递 `--kernel-name`（Triton 编译名称可能与 Python `@triton.jit` def 不同）。
- 失败证据保持失败：如果 KB 不可用，写入 `kb_unavailable.json`；如果更快的分支缺少声明的 TTGIR/ISA 证明或指针范围证明，将该方法标记为未证明或实现失败。当证据降级时（KB 不可用、profiler 空、ISA 缺失），继续使用最佳可用证据并显式记录失败。参见 `references/hcu_arch_and_triton_notes.md` §6.4 了解失败模式处理。

## 契约

`kernel.py` 必须暴露 `setup(**kwargs)` 和 `run_kernel(**kwargs)`。`setup()` 使用 shape 选择 kwargs/dims 加上 `seed`、`config`、`config_key`、`disable_autotune` 和 `target_arch` 调用；它必须容忍这些 kwargs。将要进行 benchmark/优化的每个目标 shape 放在 `kernel.py` 中。`shape.json`、`--dims` 或 `shape_list` 可以选择要运行的支持的 shape；如果 case 工作流未提供选择器，运行默认 shape 集。Optimizer 选择具体的目标 shape 后，在 `shape.json` 中记录它们。Case 根目录 `kernel.py` 是冻结的输入 baseline，除非用户明确要求在那里进行源码编辑；在 `run_YYYYMMDD_HHMMSS/` 内的复制 kernel 上执行兼容性修复、测试挂钩和优化编辑。

`setup()` 必须返回 `{"inputs": dict, "outputs": list}`。每个输出名称必须作为 key 出现在 `inputs` 中；kernel 将结果写入相同的 tensor 引用。可选返回字段由 benchmark/report/finalization 消费的是 `kernel_kwargs`、`reference_inputs`、`active_config`、`config_source`、`config_key` 和 `config_hit`。

**`ref.py` 契约：** `reference(**kwargs)` 必须匹配 case 的 tensor 契约（需要时来自 `setup()` 的 `reference_inputs`），并且必须可从 Python 调用。可选的模块级 `atol` / `rtol` 和 `REF_BACKEND`（`"triton"`、`"pytorch"`、`"hipc"` 等）记录在 `preflight` / `bench.json` 中。**不要**仅为 skill 将工作中的 Triton/HIP 语义 ref 转换为 PyTorch；**不要**将 ref 计时视为优化目标。当提升语义重写时，针对 `ref.py` 证明等效性，而不是针对非正式的 PyTorch 重新实现。当使用原始 Triton kernel 作为 oracle 时，将其冻结在 `ref.py` 中，仅编辑优化目标。

## 方法选择

在选择方法或编写分支之前：

0. 确认 shape-family 规划（核心循环步骤 1）和调优空间定义（步骤 4）已在当前迭代中处理。
1. 使用 `roofline.json`、`hcu_top.json`、当前 `bench.json.active_config`、Triton IR 和本地 KB 证据对剩余瓶颈进行分类。
2. 仅读取下面列出的所需参考文件。
3. 对每个正轴预算按优先级扫描方法。
4. 跳过已尝试的方法，除非瓶颈或证据发生变化。
5. 跳过被目标架构、dtype、layout、Triton 支持、配置契约或先前实现失败阻塞的方法。
6. 保持所选方法互兼容，避免将相同的 tile/config/codegen 更改以不同名称计数。
7. 在 `analysis.md` 中解释所选和高优先级被跳过的原因，然后在分支前运行 `scripts/validate_methods.py`。

## Agent 执行指南

### methods.json 格式

在 `close-iter` 前写入 `iterv{i}/methods.json`。Schema：`templates/methods.schema.json`。必需字段：

```json
{
  "iter": 1,
  "methods": [
    {
      "id": "triton.vectorized_load_store",
      "name": "Vectorized Load/Store",
      "axis": "memory",
      "priority": 3,
      "description": "在证明对齐和连续访问后使用更宽的向量化内存操作",
      "skipped_higher": [
        {"id": "triton.coalesced_load_store", "priority": 1, "reason": "already_selected"},
        {"id": "triton.mask_simplification", "priority": 2, "reason": "no_trigger"}
      ]
    }
  ]
}
```

- `id` 必须存在于 `references/triton_method_registry.json` 中。
- `axis` 是 `compute`、`memory`、`latency` 之一。
- `priority` 必须匹配注册表条目。
- `skipped_higher[].reason` 是以下之一：`already_selected`、`arch_incompatible`、`feature_unavailable`、`skip_condition`、`no_trigger`。
- 方法总数 1-6，每个轴最多 2 个。
- 在 `close-iter` 前运行 `validate_methods.py` 捕获 schema 和注册表错误。

### 分支编写

编写 `methods.json` 后，在 `iterv{i}/branches/` 下创建 K 个分支 kernel：

```
iterv{i}/branches/
  b1/
    kernel.py          # 必需 — 相同的 setup()/run_kernel() 契约
    config.json        # 可选 — 此分支的配置覆盖
  b2/
    kernel.py
    config.json
```

- **Agent 编写**：`kernel.py`（必需）和 `config.json`（可选）。
- **脚本生成**：`bench.json`、`bench.stderr.txt` — 不要编写这些。
- 每个 `kernel.py` 必须遵循相同的契约（setup + run_kernel）。
- 创建分支时不要编辑 `./demo.py`、case 根目录的 `./kernel.py` 或其他原生 case 文件；分支 kernel 必须仅存在于 `iterv{i}/branches/` 或 `run_YYYYMMDD_HHMMSS/` 中的其他文件下。
- 分支共享相同的方法，但在 tile 大小、`num_warps`、`num_stages` 或其他配置参数上不同。
- 如果分支需要固定配置，写入 `branches/b*/config.json` 或传递配置选项给 `close-iter`；`branch_explore` 不会隐式注入 `state.best_config`。

### analysis.md 先决条件

`close-iter` 验证 `iterv{i}/analysis.md` 包含非占位的 `## Kernel Computation Logic` 节。没有它，`close-iter` 以代码 3 退出。至少写入：

- **Tensor 角色和 shape**：输入、输出、dtype、layout 假设。
- **数学公式**：例如 `C[m,n] = sum_k A[m,k] * B[k,n]`。

参见 `templates/iteration_report.md` 获取完整模板。

### close-iter 前阅读清单

在编写 `methods.json` 和分支 kernel 前，按顺序阅读这些文件：

1. `state.json` — 当前最佳、历史、有效/无效/失败方法。
2. `iterv{i}/roofline.json` — 轴预算（`axis_budget.compute/memory/latency`）、`bound`、`near_peak`。
3. `iterv{i}/hcu_top.json` — profiler 指标、`profiler_selection`、降级标志。
4. `iterv{i}/accepted_configs.json` 或 `tune_results.json` — 配置 sweep 结果（如果运行了 tune_configs）。
5. `iterv{i}/kb_evidence.md` 或 `kb_unavailable.json` — KB 证据状态。
6. `iterv{i}/irs/` — Triton IR 产物（如果已提取）。

然后根据需要阅读参考文件：

| 步骤 | 阅读 | 原因 |
|------|------|-----|
| 语义预步骤 | `triton_semantic_prepass.md`、`triton_optimization_memory.md` | 调优前的算法简化 |
| 方法选择 | `triton_optimization_catalog.md`、`triton_method_registry.json` | 选择匹配瓶颈的方法 |
| 方法验证 | `triton_method_registry.json` | 确认 id/priority/axis 匹配 |
| ISA/TTGIR 检查 | `hcu_triton_isa_signatures.json`、`hcu_arch_and_triton_notes.md` | 验证 lowering 和架构规则 |
| 配置设计 | `hcu_triton_config_patterns.md` | Shape-bucketed 配置注册表 |
| 指标解读 | `hcu_triton_metrics_guide.md` | xcu/hipprof 指标阅读 |
| 最终化 | `finalization_and_reporting.md` | 最终门控和摘要要求 |
| Inductor 反馈 | `torch_inductor_aot_feedback.md` | 仅当 kernel 是 Inductor 生成时 |

### close-iter 失败修复

当 `close-iter` 失败时：

| 退出码 | 含义 | 修复步骤 |
|--------|------|---------|
| 2 | 未产生有效分支 | 检查 `branches/b*/bench.json` 和 `bench.stderr.txt`；修复编译/运行错误、正确性失败、数值问题、边界处理、dtype 或配置假设；重试 `close-iter` |
| 3 | analysis.md 缺少 Kernel Computation Logic | 编写完整的 `## Kernel Computation Logic` 节；重试 `close-iter` |

修复后，仅重新运行 `close-iter` — 不要重新运行 `setup` 或 `open-iter`。如果 `methods.json` 需要更改（例如删除失败的方法），更新它并在重试前重新运行 `validate_methods.py`。

## 最终化门控

在遵循 `references/finalization_and_reporting.md` 之前不要发送优化运行的最终回复。至少，最终化必须产出 `final_kernel.py`、`summary.md`、最终配置/manifest 产物、尝试时间线产物、最终正确性/计时、profiler 或降级 profiler 证据、Triton cache/IR 证据或记录的失败尝试，以及 ISA 证据或记录的失败尝试。

最终 `summary.md` 必须以人为先：以紧凑的标题指标表开头，将环境/工具链细节保留在最终 kernel 快照/指标表中，用数学公式描述计算，避免转储 Python Reference Form 代码，并使用链接/对象嵌入的 `attempt_timeline.svg`，其点暴露每个尝试的悬停详情。

在最终报告编写期间，将提升的源码重写/配置敏感的惯用模式与 `references/triton_optimization_memory.md` 进行比较。仅在模式紧凑、可重用、可证明等效且有正确性/计时证据支持时才追加记忆条目。

如果输入 kernel 是由 Torch Inductor、AOTInductor、`torch.compile` 或 AOT 包生成的，在编写 `summary.md` 中的 `## Torch Inductor AOT Feedback` 前阅读 `references/torch_inductor_aot_feedback.md`。

## 按需阅读参考资料

- `references/finalization_and_reporting.md`：最终调优需求、最终化门控、最终 `summary.md` 节、降级证据处理。
- `references/torch_inductor_aot_feedback.md`：何时以及如何将手动 Triton 优化映射回 PyTorch Inductor/AOT 杠杆。
- `references/triton_semantic_prepass.md`：setup 之后、初始配置调优之前的强制性语义预步骤。
- `references/triton_optimization_memory.md`：历史上可重用的语义重写和优化 kernel 模式。
- `references/triton_optimization_catalog.md`：方法意图、触发条件、跳过规则和组合。
- `references/triton_method_registry.json`：方法 ID、优先级、需求和预期证据。
- `references/hcu_triton_metrics_guide.md`：xcu 优先指标加 hipprof/PMC/SQTT fallback 解读。
- `references/hcu_triton_isa_signatures.json`：通过 `isa_check.py` 的自动化 TTGIR 和 `dccobjdump` 检查。
- `references/hcu_arch_and_triton_notes.md`：HCU 架构、TTGIR 操作、layout 编码、LinearLayout、buffer-op lowering 说明、Hygon/Triton 规则、模糊行为调查、lowering/ISA 检查和失败模式。
- `references/hcu_triton_config_patterns.md`：针对配置敏感工作负载的有限 shape-bucketed 注册表。
