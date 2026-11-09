> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 详细循环

### 步骤 0：preflight

使用：

```bash
python <skill>/scripts/preflight.py \
  --baseline ./kernel.hip \
  --ref ./ref.py \
  --dims '{"N":1048576}'
```

直接暴露契约失败。如果参考无法运行或 baseline 无法编译/benchmark，不要开始优化。

### 步骤 1：初始化并播种 baseline

正常路径：

```bash
python <skill>/scripts/orchestrate.py setup --baseline ... --ref ... --dims ...
```

手动路径：

```bash
python <skill>/scripts/state.py init --baseline ./kernel.hip --ref ./ref.py --dims '{"N":1048576}' --env ./env.json
python <skill>/scripts/run_iteration.py seed-baseline --state ./run_*/state.json
```

运行文件夹是 baseline 旁边的 `run_YYYYMMDD_HHMMSS/`，包含 `state.json`、复制的 baseline 产物和 benchmark 结果。

### 步骤 2：profile 当前最佳并预算方法

使用：

```bash
python <skill>/scripts/profile_hipprof.py \
  --state ./run_*/state.json \
  --iter 1 \
  --which best_input \
  --pmc-mode all

python <skill>/scripts/roofline.py \
  --state ./run_*/state.json \
  --iter 1
```

读取：

- `iterv{i}/hcu_top.json`
- `iterv{i}/roofline.json`
- `state.json`
- 当前 `best_file`

如果所有差距都接近峰值，提前停止并总结。否则使用 `axis_budget` 决定每个轴选择多少方法。

如果 optimizer 已连续完成**三次迭代**而未对前次最佳有实质性的额外改进，在选取更多源码更改之前触发 SQTT/工具诊断。"实质性"通常意味着超过 `state.json` 中配置的噪声阈值（默认 2%）且可通过 profiler/ISA 证据解释，而不仅仅是单个带噪声的时序采样。诊断应该：

1. 对当前最佳或最新冠军运行 `profile_hipprof.py`，使用 `--pmc-mode none --sqtt-type 1 --sqtt-output-type 0 --sqtt-data-dir <itervN>/sqtt_json/`；
2. 使用 `scripts/analyze_sqtt.py` 分析产物；
3. 如果本地或远程有 `perfetto`，使用 `scripts/analyze_perfetto_trace.py` 分析代表性 `thread_trace_*.json` 文件；
4. 使用 SQTT/Perfetto 证据决定下一个方法应针对 waitcnt 放置、issue 停顿、分支分歧、LDS/bank 行为、cache/全局内存压力，还是 kernel 已经接近实际上限。

对于模糊的硬件错误或无法解释的回归，可以更早运行 SQTT，但不要使其成为每次迭代的强制性成本。

### 步骤 3：选择方法

按顺序读取这些参考，仅加载需要的部分：

1. `references/optimization_catalog.md` 了解方法意图、触发条件、跳过规则和组合规则。
2. `references/method_registry.json` 了解机器验证的方法 ID、轴、优先级、需求和预期 ISA 签名。
3. `references/hcu_metrics_guide.md` 了解指标到原因的映射和 hipprof/PMC 解读。
4. `references/hcu_isa_signatures.json` 了解最终的 dccobjdump 模式名称。

选择规则：

1. 使用 `roofline.json.axis_budget` 分配每个轴接收多少方法。
2. 对每个轴，从测量证据中评分注册表方法：
   - `roofline` 轴增量和 bound 分类；
   - `hcu_top` 触发指标与 `trigger_metric` 和 `trigger_direction` 匹配；
   - SQTT 提示，如 waitcnt、类停顿命中、分支计数、vmem/LDS/matrix 指令混合；
   - 代码对象资源压力，如高 VGPR/SGPR/LDS；
   - 目标架构和 `arch_feature_map` 特性可用性。
3. 跳过已选择、标记为无效、实现失败、架构不兼容或特性不可用的方法。
4. 首先按证据分数排名，其次按注册表优先级。如果某个轴上没有方法有直接触发证据，在该轴预算内回退到注册表优先级，并记录空/弱证据。
5. 在最终排名前应用生成器能力偏置。有安全分支生成器用于检测到的契约的方法可以提升；对于平坦 elementwise/copy kernel，仅矩阵、仅 CK Tile 或仅 MMAC 的方法被降级，除非有直接证据和真正的生成器证明其合理。
6. 选择恰好 `sum(axis_budget)` 个方法，除非没有有效方法存在；如果更少，在 `analysis.md` 中解释每个缺失的槽位。
7. 保持所选方法互兼容。避免选择两个只是换种说法描述同一流水线或 tiling 变更的方法。

写入：

- `iterv{i}/methods.json`，匹配 `templates/methods.schema.json`
- `iterv{i}/analysis.md`，遵循 `templates/iteration_report.md`

在生成分支前验证：

```bash
python <skill>/scripts/validate_methods.py \
  --methods ./run_*/iterv1/methods.json \
  --state ./run_*/state.json
```

### 步骤 4：生成分支 kernel

在 `iterv{i}/branches/b1..bK/` 下生成 K 个分支。所有分支应实现相同的方法集，但实现细节不同：

- tile 大小和向量宽度，
- wave/block 映射，
- LDS 布局和 bank 冲突策略，
- 流水线阶段数，
- CK Tile 策略名称和模板参数，
- 直接 load/store 路径与 LDS staging，
- 当必须强制编译器输出时使用内联汇编或 builtin 形式。

自动路径使用 `auto_kernel_optimize.py --branch-mode method_transform`，保持分支 1 为 no-op 后备，稍后用专门的生成器填充后续分支，然后在可能时使用保守的源码变体。它将确切的计划写入 `iterv{i}/branch_plan.json`。

当分支由专门的生成器生成时，它必须在 `branch_plan.json` 中声明 `claimed_method_ids`。`branch_explore.py` 将获胜分支的 `claimed_methods` 写入 `iterv{i}/champion_methods.json`；`sass_check.py` 和 `state.py update` 使用该冠军声明文件进行归因。这防止分支因 advisor 选择但冠军源码未实际实现的方法而受到惩罚。

对于 GEMM/conv/norm/MoE 风格的 kernel，当操作 shape 适合时，优先使用 CK Tile 策略和已知的快速路径，如 `TLS`、`MLS`、`WASP`、`cshuffle`、`wavelet`、`persistent`、`split-k`、`preshuffle` 和 DS-read 矩阵变体。

CK Tile 自动化是有意模板门控的。首先探测：

```bash
python <skill>/scripts/generate_ck_tile_candidates.py \
  --state ./run_*/state.json \
  --family gemm \
  --out ./run_*/ck_tile_candidates.json
```

如果有经过项目验证的 CK Tile 源码暴露 `extern "C" void solve(...)`，将其交给 auto loop：

```bash
python <skill>/scripts/generate_ck_tile_candidates.py \
  --state ./run_*/state.json \
  --family gemm \
  --template ./ck_tile_solve.hip \
  --copy-template

HYGON_CK_TILE_TEMPLATE=./run_*/ck_tile_template.hip \
python <skill>/scripts/run_auto_loop.py --run-dir ./run_* --max-iters 1 --branches 4 --finalize
```

不要将 CK Tile/MMAC 方法标记为已实现，除非分支编译通过、正确性通过、获胜或保持为有效候选，且 ISA 验证看到预期的 Hygon/CK Tile 指令模式。

### 步骤 5：分支探索和修复

使用：

```bash
python <skill>/scripts/branch_explore.py \
  --state ./run_*/state.json \
  --iter 1
```

或让 `orchestrate.py close-iter` 运行它。如果所有分支失败，检查分支的 `bench.json`、`bench.stderr.txt`、编译器日志和验证错误。修复分支源码并重新运行。当分支从未编译或从未通过正确性时，不要将方法标记为无效。

`run_auto_loop.py` 有一个受保护的修复回退：当分支探索返回"所有分支失败"状态时，它可以重新生成 no-op 分支并重试 close-iter 一次。这使 optimizer 状态机可恢复，同时保留失败的分支日志用于后续生成器修复。

修复层是保守的。`repair_branches.py` 分类编译、契约、正确性和运行时失败，写入带有失败指导的 `repair_report.json`，然后输出当前最佳回退以及小的修复变体，如更安全的 block 维度、移除 launch bounds 或指针 restrict。这些分支仍需要编译/正确性/benchmark 验证；修复不会直接提升失败的源码。

### 步骤 6：profile 冠军、消融、验证 ISA

使用：

```bash
python <skill>/scripts/profile_hipprof.py \
  --state ./run_*/state.json \
  --iter 1 \
  --which kernel

python <skill>/scripts/ablate.py \
  --state ./run_*/state.json \
  --iter 1

python <skill>/scripts/sass_check.py \
  --state ./run_*/state.json \
  --iter 1
```

`sass_check.py` 的命名是为了 CUDA 兼容性，但在本 skill 上它使用 `dccobjdump` 和 HCU 签名模式运行 HCU ISA 验证。

`orchestrate.py close-iter` 在 `ablate.py` 之前运行 `generate_ablations.py`。消融优先选择不声明被移除方法的已生成分支替代，然后回退到中性 no-op 归因。`ablation_manifest.json` 记录置信度，并将 benchmark 所需的消融与中性占位符分开，因此报告不会将 no-op 拷贝视为贡献的证明。

### 步骤 7：模型集成 scaffold

在冠军 kernel 被选择后，创建模型局部的扩展 scaffold：

```bash
python <skill>/scripts/scaffold_model_integration.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --out-dir ./hygon_custom_op \
  --name hygon_custom_op \
  --env-var HYGON_CUSTOM_OP
```

scaffold 复制冠军 kernel 并写入：

- `kernel.hip`
- `<name>.cpp`
- `wrapper.py`
- `README.integration.md`
- `smoke_integration.py`
- `integration_manifest.json`

对于简单平坦一元和简单 matmul `solve(...)` 签名，生成的 C++ 包装器包含真实的 PyTorch tensor 编组。对于其他签名，它仍是手动 scaffold，manifest 标记 `status=scaffold_only`。始终使用生成的环境变量门控模型调用点，并在性能测试前使用 `<ENV>_STRICT=1` 验证。

### 步骤 8：更新状态和总结

使用：

```bash
python <skill>/scripts/state.py update \
  --state ./run_*/state.json \
  --iter 1 \
  --kernel ./run_*/iterv1/kernel.hip \
  --bench ./run_*/iterv1/bench.json \
  --methods-json ./run_*/iterv1/methods.json \
  --attribution ./run_*/iterv1/attribution.json \
  --sass-check ./run_*/iterv1/isa_check.json

python <skill>/scripts/summarize.py \
  --state ./run_*/state.json \
  --out ./run_*/summary.md
```

状态规则：

- 将每个尝试的方法添加到 `selected_methods`。
- 仅在归因积极超过噪声且存在预期 ISA 证据时，将方法添加到 `effective_methods`。
- 当 ISA 证据存在但归因不积极时，将方法添加到 `ineffective_methods`。
- 当代码编译通过但相关 dump 中缺少预期 ISA 证据时，将方法添加到 `implementation_failed_methods`。
- 如果分支更快但声明的某个方法的 ISA 证据缺失，如果正确则保留更快的 kernel，但将该方法记录为实现失败。
