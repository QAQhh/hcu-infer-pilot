# LightOp 算子智能体闭环

用户希望为 DCU/ROCm 新增 LightOp 算子或优化已有算子时，使用此流程。由 agent 直接执行 HIP 证据驱动闭环；优化选法、目标 ISA 核验和消融遵循 [HIP 优化规则](hip-optimization-rules.md)。

不要将其用于通用 CUDA/NVIDIA kernel 调优。优先考虑 HIP C++、ROCm PyTorch 扩展、已有 LightOp 模式、MIOpen/rocBLAS/hipBLASLt、Composable Kernel 或 Triton AMD；所选路线必须已被本地仓库支持，或由用户明确要求。

## 输入契约

实施前恢复或定义以下内容：

```text
K: 算子语义、输入/输出张量、dtype/layout/mode 约束
R: 正确性参考，通常为原生 PyTorch、已有 LightOp 路径，或处理边界情况的小型显式 oracle
W: 工作负载分布，包括目标 shape、dtype、模型场景、gfx 架构、layout/连续性、
   reduction/axis 细节、epsilon 或 mode 参数、有效带宽公式，以及时延/吞吐比较目标
E: 执行环境，包括 Docker 容器/镜像或直接宿主、环境中的 LightOp 路径、可见 DCU 设备、
   DTK/ROCm/PyTorch 版本、构建命令、测试命令、benchmark 命令和通过阈值
```

仅当 `K`、`R`、`W`、目标 DCU/gfx 架构、比较基线、执行环境、通过阈值或硬性范围约束缺失，且无法从 LightOp 仓库安全推断时，才询问用户。输入齐备后，由闭环负责检查、研究、实现路线、性能分析深度、benchmark 扩展和调优谱系等战术选择。

## 定位 LightOp

默认在 LightOp checkout 上工作，不使用独立的 CUDA 实验。LightOp 根目录包含：

```text
setup.py
lightop/__init__.py
lightop/csrc/export.cpp
test/
```

按以下顺序查找：

1. 用户提供的路径。
2. 当前工作目录。
3. 当前工作区附近名为 `lightop` 的同级目录。

没有找到 checkout 时，询问其路径。用户明确要求独立实验时，将实验放在 LightOp 外部，但记录最终候选如何合入 LightOp 源码树。

## 执行环境

构建、正确性、benchmark 和性能分析使用同一套环境。用户指定 Docker 容器或镜像时，将 Docker 纳入验收契约。优先使用非交互命令，便于捕获日志和复现同一条命令：

```bash
docker exec <container> bash -lc 'cd /path/in/container/lightop && <command>'
```

指定 Docker 为执行环境时，LightOp 安装与构建也必须通过这一准确的 `docker exec` 形式执行，不能在宿主上构建该任务。容器内安装命令始终为 `python setup.py install`，可按需加 `PYTORCH_ROCM_ARCH=...` 前缀；不能使用 `setup_torch29.py`，正常迭代不删除 `build/`。

用户提供镜像而非运行中的容器时，询问或推断宿主 LightOp 路径，并暴露 DCU 设备运行：

```bash
docker run --rm --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --network=host \
  -v <host-lightop>:/workspace/lightop <image> \
  bash -lc 'cd /workspace/lightop && <command>'
```

首次构建前记录：

- 容器名或镜像 tag；不用 Docker 时记为 `direct-host`。
- 从执行命令视角看到的 LightOp 路径，不只记录宿主路径。
- `HIP_VISIBLE_DEVICES`、`HSA_VISIBLE_DEVICES` 等设备可见性环境变量。
- 性能运行前的 DCU 状态命令与所选卡：`hy-smi` 或 `rocm-smi`、观测到的 HCU 利用率和显存占用，以及 benchmark/profile 使用的 `HIP_VISIBLE_DEVICES=<idle-card>`。
- `PYTORCH_ROCM_ARCH`、DTK/ROCm、PyTorch 和 HIP 版本、设备名称及 `gcnArchName`。
- 准确的构建/安装、导入冒烟、正确性、benchmark 和 profiler 命令。
- 通过/失败阈值：正确性数值容差，以及相对基线的性能目标。
- benchmark 稳定性规则：预热与重复次数、汇总统计量（p50/p90/mean）、可接受噪声带和构成有效优化的最小变化量。

除非用户明确要求分开执行，且两个路径指向同一已编译扩展，否则不混用宿主构建和容器测试。

## LightOp 集成位置

新增或修改算子前，先检查最接近的已有算子族并遵循其风格。

新增融合算子时，先从名称、所需语义或提供的实现草图恢复融合组成。设计新 kernel 前，搜索 LightOp 中融合前的单算子和相关融合实现。以本地实现作为 API 形式、张量验证、dispatch/config 风格、正确性参考、benchmark 比较与性能预期的首要基线。找不到匹配的本地基线时，记录查询词和缺失结果，再退回 PyTorch 或小型显式 oracle 参考。

核心源码位置：

```text
lightop/csrc/<family>/*.cu|*.cuh|*.h|*.cpp
lightop/csrc/export.cpp
lightop/<python_wrapper>.py
lightop/__init__.py
setup.py
test/test_<op>.py
test/<family>/*benchmark*.py
lightop/config*.py
```

LightOp HIP/C++ kernel 源码使用 `.cu`。不要为 LightOp 算子创建或编辑手写 `.hip` 文件；本地构建产生的 `.hip` 视为生成产物，不是最终应提交的源码格式。

LightOp 开发一致性门槛：

- 编辑前检查最接近的同族实现，遵循其目录布局、文件命名、C++ namespace 风格、include 顺序、launch helper 风格、宏与 dispatch 模式、错误检查习惯和格式。
- Python wrapper 的导入、张量/设备/dtype 检查、连续性处理、可选参数、返回形状、fallback 或报错行为与现有风格一致。本地已有模式时，不发明新的用户接口封装方式。
- 遵循 `lightop/csrc/export.cpp` 的绑定风格，包括符号名、参数顺序、`m.def(...)` 位置及公共 API 暴露规则。
- 测试的 seed、容差、dtype/shape 覆盖、同步、skip 逻辑和命令行行为遵循现有 `test/` 风格。不为单个任务引入新测试框架或许多一次性测试入口。
- 新增配置表、dispatcher 分支、shape key、环境变量或 benchmark CLI 参数前，先遵循已有 benchmark/config 约定。
- 不引入无关依赖、直接内置外来 kernel、生成源码、广泛重构、无关格式修改或其他项目布局；用户明确要求且计划记录原因时除外。
- 最终报告前做一致性复核：列出修改文件、遵循的相近 LightOp 文件和有意偏离之处；确认没有手写 `.hip` 源码、无关算子族修改或 `test/` 下额外的最终测试。

典型新增算子清单：

- 融合算子需检查各组成单算子的 wrapper、绑定、kernel、测试、benchmark、配置路径，以及数据搬运或 epilogue 结构相似的邻近融合 kernel。
- 组成算子存在时，用未融合的 LightOp 组合建立首次正确性和 benchmark 基线；否则采用最接近的 LightOp 实现加 PyTorch 参考。
- 在最接近的 `lightop/csrc/` 算子族中新增或修改 HIP/C++ 实现。只有现有算子族都不合适时才创建新族。
- 在 `lightop/csrc/export.cpp` 中通过 `m.def(...)` 暴露 C++ 符号。
- Python wrapper 使用 `from . import op`，保留 LightOp 的张量验证风格。
- 只有算子面向用户时，才从 `lightop/__init__.py` 导出公共 API。
- 创建新 `csrc/<family>` 目录时更新 `setup.py` 的源码 glob。用户未明确要求维护旧元数据时，不添加并行的 `setup_torch29.py` 构建路线。
- 性能依赖 shape/gfx 专用选择时，在 `lightop/config*.py` 更新或新增相应 config/dispatcher 表。
- 在 `test/` 下增加最终聚焦的正确性/性能测试，按公共算子或目标 kernel 命名为 `test_<operator_name>.py`。每个任务只保留这一个最终测试；辅助 benchmark、候选测试、扫描配置、PMC 解析器、临时参考及其他辅助脚本放在 `.lightop-kernel-agent/`。不能仅将最终验证脚本留在该目录，它用于记录和临时证据，不是 LightOp 的正式测试入口。

仅优化已有算子的清单：

- 定位当前 Python wrapper、导出的 C++ 绑定、kernel launch 路径、config/dispatcher 分支和已有测试/benchmark。
- 除非用户明确要求破坏性变更，否则保留公共 API。
- 不为已有算子的优化任务增加新公共 API。
- 不创建无关算子文件或新算子族。
- 不修改无关算子族。
- 优先只改目标算子的 kernel 源码、launcher、必要 dispatcher/config 项、聚焦测试和 benchmark 覆盖。
- 在选定执行环境中直接完成安装、正确性、benchmark、性能分析和调优；除非现有测试/benchmark 无法覆盖目标，否则不绕到新增算子的集成流程。
- 修改范围限定为任务所需的算子族、绑定、测试、benchmark 和调优表。
- 用户只需指定目标算子和测试文件，指定文件作为必需的最终验证文件。未指定时推断或创建 `test/test_<operator_name>.py`。不在 `test/` 下增加其他任务专用测试，辅助 benchmark、解析和扫描脚本放在 `.lightop-kernel-agent/`。
- 优化回退或只改善非目标 shape 时，记录被拒绝的谱系。

## DCU/ROCm 默认规则

- LightOp 测试中的 PyTorch `torch.cuda` namespace 视为 ROCm 运行时接口。
- 优先 `hipcc`/ROCm 扩展构建，不采用仅 NVIDIA 的编译路径。
- 提交的 LightOp kernel 源码扩展名使用 `.cu`，不手写提交 `.hip` 算子文件。构建生成的 `.hip` 保留为构建产物，不作为源码修改。
- 遵守 `PYTORCH_ROCM_ARCH`；未设置时从 `torch.cuda.get_device_properties(0).gcnArchName` 推断 gfx。
- 本地 LightOp setup 已采用默认 `gfx928;gfx936;gfx938` 时优先沿用，除非用户给出更窄目标。
- 不在 LightOp 路径中引入 CUDA-only 头文件、PTX/SASS 假设、CUTLASS/CuTe、Nsight Compute、TMA/WGMMA/tcgen05 或 NVIDIA 架构规则。
- 借鉴 CUDA 来源时，转换为 ROCm 概念，并记录来源仅用于跨平台启发。

可用的环境探测命令：

```bash
python - <<'PY'
import torch
print("torch:", torch.__version__)
print("hip:", torch.version.hip)
print("device:", torch.cuda.get_device_name(0))
print("gcn:", torch.cuda.get_device_properties(0).gcnArchName)
PY
hipcc --version
```

## 性能设备门槛

任何 benchmark 或 profiling 命令执行前，在目标环境检查卡状态，将运行固定到空闲卡。

- 性能命令前立即执行 `hy-smi` 或 `rocm-smi`。
- 选择 HCU 利用率和显存占用都低的卡。没有足够空闲、能产生稳定结果的卡时，延后运行，或记录结果受噪声影响，不能作为最终证据。
- benchmark 和 profiler 命令加 `HIP_VISIBLE_DEVICES=<card>` 前缀。基线/候选配对比较使用同一张卡，除非比较目的就是跨设备行为。
- 在尝试台账或 profile 产物目录记录所选卡、HCU 利用率、显存占用和准确命令。
- 首次优化编辑前，在同一执行环境和所选卡上校准设备带宽。在 `.lightop-kernel-agent/device-bandwidth.txt` 记录实际读、写、复制/读写和简单 triad 带宽、缓冲区大小、dtype、所选卡和命令。将其作为判断用户有效带宽目标是否合理的基线。

示例：

```bash
hy-smi || rocm-smi
bash <skill-root>/scripts/measure-device-bandwidth.sh \
  --docker <container> \
  --workdir <container-lightop> \
  --hip-visible-devices <idle-card> \
  --output .lightop-kernel-agent/device-bandwidth.txt
HIP_VISIBLE_DEVICES=<idle-card> python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof python test/<family>/benchmark_<op>.py
```

直接在宿主执行时，省略 `--docker`，传入 `--workdir <lightop-root>`，或从 LightOp 根目录运行脚本。

设备选择门槛和设备带宽校准没有记录时，不将性能数字作为可采取行动的结论；用户明确接受证据缺失时除外。

## 工作流

### 阶段 1：检查与计划

1. 定位 LightOp 根目录和目标算子族。
2. 恢复 `K`、`R`、`W`、目标 gfx 架构、基线命令和成功阈值。
3. 检查已有 wrapper、绑定、kernel、配置表、测试及 benchmark。
4. 新融合算子按所需名称、名称词项、组成单算子名和语义搜索融合前的单算子及相关融合 kernel。记录选择的基线：未融合 LightOp 组合、相近融合实现、PyTorch 参考，或明确记录“未找到本地基线”。
5. 首次优化编辑前，建议查询 `lightop-kernel-knowledge`，了解本地 LightOp 模式、ROCm/DCU 上游证据、Hygon/DCU 源码参考和内置语料中的可迁移思路。能影响首次实现路线时就使用。
6. 在首个正式实现谱系开始前，在闭环状态中写简洁的研究摘要。
7. 编辑代码前定义 benchmark 契约：准确目标 shape、dtype/layout/连续性、axis/mode/epsilon、有效带宽公式、预热与重复次数、汇总统计量、噪声带，以及基线和候选将使用的 benchmark 命令。

### 阶段 2：实现与验证

1. 首次优化编辑前建立基线矩阵：运行正确性，校准所选卡的设备带宽，再在所选空闲卡上对目标工作负载做足够重复，报告 p50/p90 或 mean、有效带宽、方差/噪声、卡状态、设备读/写/复制带宽及命令行。保存到尝试台账和 `kernel_opt_readme.md`。
2. 做能满足当前任务与验收要求的最小 LightOp 源码修改。
3. 按目标架构构建 LightOp。
4. 运行目标正确性测试。在对 `W` 做 benchmark 前执行性能设备门槛，并用 `HIP_VISIBLE_DEVICES` 固定设备。
5. 记录每个候选结果：正确性失败、构建失败、回退、平台期或改善。
6. 每个通过正确性的优化候选先运行普通同步 benchmark；下次修改 kernel 或 dispatch 前，对同一代表性目标 shape 收集 `hipprof --pmc` 证据。采集缓存计数器、LDS/bank-conflict 线索、occupancy/资源信号，以及准确命令输出或工具不支持的原因。用 `dcu-profiler-report` 将这些证据转为下一次编辑。
7. 每候选 PMC 证据和 benchmark 仍无法解释下一次编辑时，调用更深入的 `dcu-profiler-report` 分析。
8. 首个通过正确性的候选未达到性能阈值时，继续进入性能分析与调优，不能宣布完成。

### 阶段 3：调优与集成

1. 为 `W` 建立性能映射。
2. 每个优化谱系聚焦一个主要假设，如向量化访存、block/thread 映射、寄存器压力、LDS 布局、occupancy、launch 配置、epilogue 融合或 shape 特化。不要在一个候选中混合多项无关技术；代码结构导致无法拆分时，记录原因。
3. 只有实测表明不同区间需要不同选择时，才添加 shape/gfx 感知的 dispatch 或配置表项。
4. 对所有触及的 dtype/layout/mode 重跑正确性。
5. 重跑定义 `W` 的 benchmark 及相近回归保护用例。
6. 每次通过正确性的优化编辑后重采每候选 `hipprof --pmc`。下次编辑前总结缓存行为、LDS/bank conflict、occupancy/资源压力，以及一个由 profiler 支持的下一步动作。
7. 候选谱系正确性失败、收益未超过噪声/稳定性阈值或仅改善非目标 shape 时，从最终路径拒绝或回退该谱系。缺少 profile/resource/ISA 时区分任务验收缺口与方法归因缺口，按 HIP 优化规则记录降级或 inconclusive；不能宣称缺失证据已通过。保留拒绝及归因记录，不静默覆盖。
8. 达到目标后做最终保护性验证：目标正确性、所选卡上重复的目标 benchmark，以及适用的邻近 shape/dtype 回归。
9. 总结最终代码路径、fallback 行为、不支持区间和剩余风险。

## 性能目标规范

用户给出带宽、时延、吞吐或加速目标时，将阈值纳入验收契约。

- 最佳正确性通过候选仍未达标时，不宣称完成。只能报告为当前最佳结果，并给出瓶颈证据和下一步。
- 每个通过正确性的候选记录 shape、dtype、layout/mode、kernel 或 dispatch 配置、实测带宽/时延、比较基线，以及改善、回退或平台期的原因。
- 每个通过正确性的优化候选，在决定下次编辑前记录代表性工作负载的配对 `hipprof --pmc` 证据。摘要必须讨论缓存行为、内存/缓存流量、LDS 或 bank-conflict 证据、occupancy/资源压力，并且只给出一个下一步 LightOp kernel、launcher、dispatcher、config 或 benchmark 编辑。已安装 DTK 无法提供某个 PMC 计数器或 occupancy 信号时，记录准确命令和失败，不能猜测。
- 性能改善只有超过计划定义的 benchmark 噪声/稳定性阈值，才算有效。变化在噪声带内时记为 inconclusive 或平台期，不能算优化胜利。
- 首个通过正确性的候选未达标后，停止前必须开展性能分析与调优闭环。
- 在任务预算允许且有新证据时探索不同优化谱系；不能为凑次数重复失败方法。达到预算、连续三轮无实质改善或目标不可达时，按 HIP 优化规则诊断并停止。
- 连续两个通过正确性的候选未达标时，下一次 kernel 或 dispatch 编辑前必须同时完成：
  - 一次 `lightop-kernel-knowledge` 研究，覆盖目标算子族的本地 LightOp 模式（归约/归一化任务才查 layernorm/rmsnorm/fused-norm）、相关 ROCm/DCU 上游证据，以及语料中可迁移的归约/向量化思路。
  - 针对代表性目标 shape 的 `dcu-profiler-report` 摘要。
- 第二次通过正确性的优化尝试，相对相关父版本或基线提升不足 5% 时，下次优化编辑前必须进行深度 `dcu-profiler-report` 分析。内容包括 `hipprof` PMC all 模式、可用时的 SQTT JSON、`dccobjdump` 反汇编、code-object 资源用量，以及明确的 LDS/寄存器/occupancy 证据，或逐项记录不可用原因。
- 该门槛后的下一次编辑必须只指定一个具体的 LightOp kernel、绑定、dispatcher、config 或 benchmark 修改，并引用所依据的知识和 profiler 证据。
- 不凭直觉、源码检查或预期硬件行为宣称优化有效。进入优化台账必须有实测且通过正确性的 benchmark、基线或父版本比较，以及每候选 PMC/profile/资源证据。
- 必需调优谱系完成后仍未达标时，总结最佳候选、失败谱系、profiler 瓶颈类别、不支持区间和最可能的下一步工程投入。不能将算子描述为性能已完成。

## 必需的闭环状态

闭环状态保存在 LightOp checkout 的本地目录，不默认纳入版本管理：

```text
.lightop-kernel-agent/plan.md
.lightop-kernel-agent/research-digest.md
.lightop-kernel-agent/attempt-ledger.md
.lightop-kernel-agent/kernel_opt_readme.md
.lightop-kernel-agent/state.json
.lightop-kernel-agent/optimization-ledger.md
.lightop-kernel-agent/lineage.jsonl
.lightop-kernel-agent/performance-map.json
.lightop-kernel-agent/tuning-decisions.md
.lightop-kernel-agent/profile-artifacts/
```

创建状态前确认 `.lightop-kernel-agent/` 已被忽略（可使用仓库本地 `.git/info/exclude`）。除非用户明确要求跟踪证据产物，否则不提交闭环状态。

每个已做 benchmark 的候选之后，都必须更新 `kernel_opt_readme.md`，采用以下格式：

```markdown
# Kernel 优化日志

## 基线矩阵
- 目标工作负载：
- 有效带宽公式：
- 设备门槛：
- 设备带宽校准：读/写/复制/triad 带宽、缓冲大小、所选卡、命令：
- 构建/测试/benchmark 命令：
- 基线 p50/p90/mean、方差/噪声：

## 迭代 <N>：<一个主要假设>
- 假设：
- 修改文件：
- 代码/配置修改：
- 构建命令/结果：
- 正确性命令/结果：
- 设备状态与 HIP_VISIBLE_DEVICES：
- Benchmark 表：基线/父版本/候选、p50/p90/mean、有效 BW、变化量、噪声阈值：
- 每候选 PMC/profile/资源证据：缓存行为、LDS/bank conflict、occupancy/资源压力、不可用计数器：
- 决策：keep | reject | inconclusive
- 原因：
- 下一步：
```

## 构建、测试与基准测量

在选定环境的 LightOp 根目录构建。无论安装哪一版 PyTorch，LightOp 构建始终使用 `python setup.py install`，不切换到 `setup_torch29.py`。

```bash
PYTORCH_ROCM_ARCH='gfx928;gfx936;gfx938' python setup.py install
```

选定环境为 Docker 时，使用用户提供的容器路径封装同一命令：

```bash
docker exec <container> bash -lc 'cd <container-lightop> && PYTORCH_ROCM_ARCH="gfx928;gfx936;gfx938" python setup.py install'
```

尝试之间保留现有 `build/`，以便增量扩展构建复用编译产物。`python setup.py install` 可能创建或更新正常 setuptools 子目录，如 `build/bdist.*`、`build/lib.*`、`build/temp.*`；保留并在下次构建复用。正常构建/测试/调优闭环不删除、重命名、移动或重建 `build/` 及其子目录；用户明确要求干净构建，或证明确有缓存过期/损坏时除外。

`rm -rf build`、`python setup_torch29.py install`，或对绑定 Docker 的任务在宿主执行 `python setup.py install`，均违反本 Skill，除非用户明确覆盖该规则。

安装后，在同一环境做导入冒烟测试：

```bash
python - <<'PY'
import torch, lightop
print("torch:", torch.__version__)
print("hip:", torch.version.hip)
print("lightop:", getattr(lightop, "__file__", "unknown"))
print("device:", torch.cuda.get_device_name(0))
print("gcn:", torch.cuda.get_device_properties(0).gcnArchName)
PY
```

先运行最窄且相关的测试：

```bash
cd test
python test_<op>.py
```

新算子的最终验证必须放在 `test/test_<operator_name>.py`。优化任务使用用户指定测试；未指定时推断或创建该文件。最终测试先针对选定参考做数值正确性，再执行性能部分：10 次预热、100 次计时迭代，在计时区间前后显式 `torch.cuda.synchronize()`。报告目标工作负载的平均微秒时间和有效带宽。

`test/` 下应只有一个最终任务测试文件。临时候选测试、独立 benchmark、PMC 解析器、扫描配置和探索参考脚本放在 `.lightop-kernel-agent/`；由单个最终 `test/test_<operator_name>.py` 覆盖接受的正确性和性能检查。

正确性参考必须是 PyTorch、Triton、已有 LightOp 组合，或用户准确提供的 oracle。测试脚本可以有小型 benchmark harness；不能将 `.lightop-kernel-agent/final_test.py`、`.lightop-kernel-agent/bench_baseline.py` 等仅用于记录的脚本当作最终 LightOp 验证入口。

最终回复和 `kernel_opt_readme.md` 必须以简洁 Markdown 表格展示最终验证，至少包含：测试文件、参考、shape、dtype、正确性结果、平均时间（us）、有效带宽、所选卡及命令。

每次 benchmark 前都执行本 Skill 的性能设备门槛：保存 `hy-smi` 或 `rocm-smi` 状态，选择低利用率、低显存占用卡，并用 `HIP_VISIBLE_DEVICES=<idle-card>` 运行。基线与候选复用同一张所选卡。

每个通过正确性的优化候选之后，下次编辑前对同一代表性 benchmark shape 收集 PMC 证据。复用所选卡，产物存入 `.lightop-kernel-agent/profile-artifacts/<version>/`，执行已支持的形式，例如：

```bash
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc --pmc-type 3 \
  -o .lightop-kernel-agent/profile-artifacts/<version>/hipprof-pmc-all/pmc \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-read --pmc-type 3 \
  -o .lightop-kernel-agent/profile-artifacts/<version>/hipprof-pmc-all/pmc-read \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-write --pmc-type 3 \
  -o .lightop-kernel-agent/profile-artifacts/<version>/hipprof-pmc-all/pmc-write \
  python test/<family>/benchmark_<op>.py
```

用 PMC 摘要检查缓存行为、内存/缓存流量、LDS 或 bank conflict、occupancy/资源压力，并决定下一项具体编辑。已安装 DTK 不支持某个计数器、`--pmc` 模式或 occupancy 信号时，将尝试命令和错误输出保存到产物目录。

不能仅凭构建通过宣称成功。LightOp 算子修改只有完成安装、导入冒烟、目标正确性、benchmark 比较和必需的每候选 PMC/profile 证据才算完成。异步 DCU 工作未同步时，不根据 Python 墙钟计时宣称加速。

基线和候选比较使用相同 benchmark 命令、所选卡、工作负载 shape 和有效带宽公式。工作负载契约改变时，重新建立基线矩阵并说明原因。

## 性能分析

每个通过正确性的优化候选后，自主调用 `dcu-profiler-report`，解释强制要求的 `hipprof --pmc` 采集，并生成下一次编辑。摘要可简洁，但必须解释缓存行为、LDS/bank-conflict 线索、occupancy/资源压力，以及且仅有一个 profiler 支持的下一步动作。

出现以下任一情况，从每候选必需 PMC 分析升级为深度分析：

- 基线 benchmark 已通过，但没有 profile 摘要。
- 正确候选相对基线或先前最佳在 +/-2% 范围内。
- 正确候选在重要 shape 上回退。
- benchmark 进入平台期，下一次编辑不明确。
- 首个通过正确性的候选未达到用户性能目标。
- 连续两个通过正确性的候选未达标；下一次 kernel 或 dispatch 编辑前，将本次分析与 `lightop-kernel-knowledge` 研究配对完成。
- 第二次通过正确性的优化尝试相对父版本或基线提升不足 5%。这是强制深度分析门槛，不是启发式建议。
- 候选明显快于预期，需要解释。
- 复核者要求性能分析证据。

profile 产物保存在 `.lightop-kernel-agent/profile-artifacts/` 或用户指定的证据目录。每份摘要末尾必须且只能给出一个具体下一步 kernel 修改，或明确说明为什么分析结果无法支持行动。

触发第二次优化 <5% 门槛时，摘要必须包含 `hipprof` PMC all、支持时的 SQTT JSON、`dccobjdump` 反汇编、code-object 资源用量，以及 LDS/寄存器/occupancy 证据。缺少工具时，记录准确的尝试命令，不能用猜测替代缺失证据。

## 计划要求

用普通 Markdown 写入 `.lightop-kernel-agent/plan.md`，为以下内容设置验收项：

- LightOp 根目录、目标算子族、公共 API 和修改文件。
- 新融合算子的融合前单算子搜索结果、相关融合实现搜索结果，以及选定基线/参考路径。
- 明确的 `K`、`R`、`W`、目标 gfx 架构、基线命令、比较目标及严格排除范围。
- 工作负载契约：目标 shape、dtype、layout/连续性、axis/mode、epsilon 或其他数学参数、有效带宽公式和准确成功指标。
- 明确的 `E`：Docker 容器/镜像或直接宿主模式、环境内 LightOp 路径、可见设备选择、安装/冒烟/正确性/benchmark/profiler 命令和通过阈值。
- 设备门槛：`hy-smi` 或 `rocm-smi`、空闲卡选择标准、benchmark/profile 必需的 `HIP_VISIBLE_DEVICES=<idle-card>` 前缀，以及状态输出保存位置。
- 首次优化编辑前的设备带宽校准：准确命令、所选卡、缓冲区大小、dtype、实测读/写/复制/triad 带宽、产物路径，以及如何约束或解释目标有效带宽阈值。
- 对 `W`、边界情况、dtype/layout/mode 边界和基线/参考一致性的正确性覆盖。
- LightOp 开发一致性清单：采用哪些同族文件作风格参考、遵循的 wrapper/绑定/config/测试/benchmark 约定、允许偏离及禁止修改的文件。
- 构建命令、ROCm/DTK/PyTorch 版本、`PYTORCH_ROCM_ARCH` 和设备元数据。
- benchmark 方法：预热、重复、同步、逐 shape 计时、适用的 p50/p90 或 mean、方差/噪声带、最小有效变化量和环境元数据。
- 必需最终测试策略：新算子增加 `test/test_<operator_name>.py`；优化任务使用用户指定文件，或推断/创建该文件。先正确性，再做 10 次预热和 100 次计时，报告平均 us 与有效带宽；参考为 PyTorch、Triton、已有 LightOp 组合或用户 oracle。`test/` 下只新增一个最终任务测试；辅助脚本放在 `.lightop-kernel-agent/`。
- 每个通过正确性的优化编辑之后采集 `hipprof --pmc`，记录产物路径、卡、代表性 shape、缓存计数器或缺失原因、LDS/bank-conflict 证据、occupancy/资源解释和 profiler 支持的下一次编辑。
- 首次优化编辑前必需的基线矩阵：卡状态、设备带宽校准、重复计时、有效带宽、噪声/稳定性估计。
- 迭代规范：每个谱系只围绕一个主要假设，明确 keep/reject/inconclusive 决策规则、任务时间或迭代预算、平台期诊断和停止条件；未给预算时根据任务范围记录合理预算，不能无限循环。
- 研究摘要：本地 LightOp 模式，以及实质影响路线的上游/源码证据。
- 每个候选的尝试台账。
- 每个 benchmark 候选之后按固定模板更新 `kernel_opt_readme.md`。
- 优化台账只接纳正确且实测改善的候选。
- 性能目标规范：首次未达标触发调优；连续两次正确性通过但未达标时，下次编辑前同时补 `lightop-kernel-knowledge` 研究和 `dcu-profiler-report` 证据；未达到目标不能报告完成。
- 低收益规范：第二次通过正确性的优化提升不足 5% 时，下次编辑必须等待深度证据：`hipprof` PMC all、可用时的 SQTT JSON、`dccobjdump`、code-object 资源用量及 LDS/寄存器/occupancy 分析。
- `W` 包含多个区间时的调优决策与 dispatcher/config 更新。
- 最终正确性矩阵、benchmark 矩阵、fallback 路径、不支持区间、必需 `test/` 文件中的最终达标保护性验证、简洁结果表、LightOp 一致性复核和剩余风险。

## 直接执行与恢复

完成计划和基线后，直接按阶段 1–3 执行，不调用外部循环启动器。每轮顺序为：profile 当前最佳 → 选择主要假设 → 实现候选 → 构建/正确性 → 同卡配对 benchmark → profile/ISA/必要消融 → keep/reject/inconclusive → 更新状态。

恢复任务时读取 `plan.md`、`state.json`、研究摘要及最后一轮台账，核对当前源码哈希、已安装扩展路径和设备/工具链。环境或工作负载发生变化时重新测基线，不能继承旧环境的性能结论。没有成功编译或通过正确性的候选不能晋升。

停止条件与方法归因见 [HIP 优化规则](hip-optimization-rules.md)。仅当用户请求版本管理操作时，暂存或提交相应修改。
