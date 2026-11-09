> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 11. 远程编译与验证

优化完成后，将 HIP 算子包上传到海光 HCU 服务器，编译并运行 test.py 验证优化效果。

### 11.1 服务器配置（动态读取）

服务器连接信息从项目根目录的 `test.env` 文件动态读取，**不要硬编码 IP 地址**。

**`test.env` 格式**：

```
# hygon
ssh -i ~/.ssh/id_ed25519 root@<HYGON_IP>
## container
<CONTAINER_NAME>
### path
<WORK_DIR>

# h20
ssh -i ~/.ssh/id_ed25519 root@<H20_IP>
## container
<CONTAINER_NAME>
### path
<WORK_DIR>
```

**解析规则**：
1. `# hygon` 段：海光 HCU 服务器（HIP 验证）
2. `# h20` 段：NVIDIA H20 服务器（CUDA 验证）
3. 从 `ssh` 行提取：SSH 密钥路径（`-i` 后的值）、用户名和 IP（`user@host`）
4. `## container` 下一行：Docker 容器名
5. `### path` 下一行：容器内工作目录

**使用前必须先读取 `test.env`**：用 Read 工具读取项目根目录下的 `test.env`，解析出以下变量，后续命令中使用这些变量替换：

| 变量 | 含义 | 示例值 |
|------|------|--------|
| `HYGON_SSH` | 海光 HCU 完整 SSH 命令前缀 | `ssh -i ~/.ssh/id_ed25519 root@<HYGON_IP>` |
| `HYGON_IP` | 海光 HCU IP | `<HYGON_IP>` |
| `HYGON_USER` | 海光 HCU 用户 | `root` |
| `HYGON_KEY` | SSH 密钥路径 | `~/.ssh/id_ed25519` |
| `HYGON_CONTAINER` | 海光 Docker 容器名 | `<HYGON_CONTAINER>` |
| `HYGON_WORKDIR` | 容器内工作目录 | `/workspace/kernels` |
| `H20_SSH` | H20 完整 SSH 命令前缀 | `ssh -i ~/.ssh/id_ed25519 root@<H20_IP>` |
| `H20_IP` | H20 IP | `<H20_IP>` |
| `H20_USER` | H20 用户 | `root` |
| `H20_KEY` | SSH 密钥路径 | `~/.ssh/id_ed25519` |
| `H20_CONTAINER` | H20 Docker 容器名 | `<H20_CONTAINER>` |
| `H20_WORKDIR` | 容器内工作目录 | `/workspace/kernels` |

### 11.2 验证流程

以下命令中的 `{变量名}` 均从 `test.env` 解析得到，执行时替换为实际值。

**上传算子包**：

```bash
scp -i {HYGON_KEY} -o ConnectTimeout=10 -r <算子名>_hip/ {HYGON_USER}@{HYGON_IP}:{HYGON_WORKDIR}/
```

**清理旧构建产物 + 编译**：

```bash
ssh -i {HYGON_KEY} -o ConnectTimeout=10 {HYGON_USER}@{HYGON_IP} \
  'docker exec {HYGON_CONTAINER} bash -c "cd {HYGON_WORKDIR}/<算子名>_hip && rm -rf build/ dist/ *.egg-info 2>/dev/null; CXX=hipcc python setup.py install 2>&1"'
```

**运行测试**：

```bash
ssh -i {HYGON_KEY} -o ConnectTimeout=10 {HYGON_USER}@{HYGON_IP} \
  'docker exec {HYGON_CONTAINER} bash -c "cd {HYGON_WORKDIR}/<算子名>_hip && python test.py 2>&1"'
```

如果 `docker exec` 报 "No such container" 或容器未运行，提示用户执行 `docker start {HYGON_CONTAINER}` 后重试。

### 11.3 错误处理

| 错误类型 | 处理方式 |
|---------|---------|
| SSH/SCP 连接失败 | 报告错误，提示检查网络/密钥，询问用户是否跳过远程验证 |
| 容器未运行 | 提示用户执行 `docker start bevformer`，询问是否重试 |
| 编译失败 | 展示完整编译输出，分析错误原因，修正代码后重新上传编译（最多重试 **2 次**） |
| 正确性测试失败 | 分析失败的 test case 和输出差异，修正优化代码后重新验证（最多重试 **2 次**） |

**重试流程**：修正代码 → 重新上传（scp） → 清理旧构建产物 → 重新编译 → 重新测试。总重试次数不超过 2 次，超出后将当前状态展示给用户并请求人工介入。

### 11.4 验证结果摘要

远程验证完成后，输出如下摘要（包含优化前后性能对比）：

```
============================================================
  远程验证结果摘要 — HCU 优化
============================================================

  算子名称:          <算子名>
  服务器:            {HYGON_IP} / {HYGON_CONTAINER}

  编译状态:          ✓ 成功 / ✗ 失败（附原因）
  正确性测试:        X/Y passed

  --- 性能对比（优化前 vs 优化后） ---
  规模          优化前           优化后           加速比
  Small         x.xxx ms         x.xxx ms         x.xx×
  Medium        x.xxx ms         x.xxx ms         x.xx×
  Large         x.xxx ms         x.xxx ms         x.xx×

  --- 优化分析 ---
  优化前瓶颈:        <Memory-bound / Compute-bound / Latency-bound>
  优化后瓶颈:        <Memory-bound / Compute-bound / Latency-bound>
  带宽利用率变化:     xx.x% → xx.x%
  计算利用率变化:     xx.x% → xx.x%
============================================================
```

如果没有优化前的基准数据，则仅展示优化后的性能数据，并注明"无基准数据对比"。

### 12. 生成本地验证报告

远程验证完成后，将 test.py 输出解析并生成本地验证报告。报告同时输出 **Markdown、PDF、可交互 HTML** 三种格式。

#### 12.1 报告目录与文件名

- 报告存放目录：项目根目录下的 `report/`
- 基础文件名格式：`report/<算子名>_optimize_<YYYYMMDD_HHMMSS>`
- 同时生成三个文件：
  - `report/<算子名>_optimize_<YYYYMMDD_HHMMSS>.md` — Markdown 源文件（可 Git 跟踪）
  - `report/<算子名>_optimize_<YYYYMMDD_HHMMSS>.html` — 可交互 HTML（含 Plotly 图表、可排序表格、可折叠章节）
  - `report/<算子名>_optimize_<YYYYMMDD_HHMMSS>.pdf` — PDF（适合归档和打印）
- 时间戳精确到秒，保证不冲突
- 示例：`report/<算子名>_optimize_20260301_143052.{md,html,pdf}`

#### 12.2 报告内容要求

报告精简为 6 个章节，重点突出**性能提升**和**下一步优化方向**，避免冗余的设备参数、编译细节和代码片段：

| 章节 | 内容 | 要求 |
|------|------|------|
| 1. 优化概览 | 算子名称、源文件路径、基准版本、目标架构（一行写明关键参数） | 精简，不单独列设备参数表 |
| 2. 正确性验证 | pass/fail 总结（一句话） | 全部通过时无需逐条列出 |
| 3. 性能对比 | Forward + Backward 各规模 latency、加速比 | **核心章节**，加粗标注显著加速比 |
| 4. 优化措施与效果 | 所采用的优化手段 + 实测效果说明 | 每项必须写明实际效果（不是预期） |
| 5. 瓶颈分析 | 瓶颈类型、算术强度、为何 Forward/Backward 效果不同 | 用文字说明因果关系，不仅列指标 |
| 6. 结论 | **结果总结** + **下一步可优化方向表** | **必填**，结论用文字概括；下一步列表含预期收益和复杂度 |

> **关键原则**：报告面向工程师快速获取优化效果和下一步行动，不是存档。去掉设备信息表、编译信息表、代码片段——这些在源码和构建日志中已有。

#### 12.3 Markdown 报告模板

```markdown
# <算子名> — HCU 性能优化报告

**生成时间**: YYYY-MM-DD HH:MM:SS

---

## 1. 优化概览

| 项目 | 值 |
|------|-----|
| 算子名称 | <算子名> |
| 优化目标 | <HIP 源文件路径> |
| 基准版本 | <基准文件路径> (未优化 HIP 迁移版) |
| 目标架构 | 海光 <设备型号> HCU (gfx926), <CU数> CU, HBM <带宽> GB/s |

## 2. 正确性验证

<一句话总结，例如：优化前后均通过全部 X 项测试，X/X passed。>

## 3. 性能对比

### Forward

| 规模 | 优化前 | 优化后 | 加速比 |
|------|-------|-------|-------|
| Small | x.xxx ms | x.xxx ms | x.xx× |
| Medium | x.xxx ms | x.xxx ms | x.xx× |
| Large | x.xxx ms | x.xxx ms | x.xx× |

### Backward

| 规模 | 优化前 | 优化后 | 加速比 |
|------|-------|-------|-------|
| Small | x.xxx ms | x.xxx ms | **x.xx×** |
| Medium | x.xxx ms | x.xxx ms | **x.xx×** |
| Large | x.xxx ms | x.xxx ms | **x.xx×** |

## 4. 优化措施与效果

| 优化措施 | 应用目标 | 效果 |
|---------|---------|------|
| <措施 1> | <Forward/Backward/...> | <实测效果，非预期> |
| <措施 2> | <Forward/Backward/...> | <实测效果，非预期> |

## 5. 瓶颈分析

<用文字说明：当前瓶颈类型、算术强度、为什么某些优化有效/无效>

## 6. 结论

<文字总结本轮优化结果：哪些方向有效、提升多少、当前瓶颈是什么>

### 下一步可优化方向

| 方向 | 预期收益 | 复杂度 | 说明 |
|------|---------|--------|------|
| <方向 1> | 高/中/低 | 高/中/低 | <一句话说明> |
| <方向 2> | 高/中/低 | 高/中/低 | <一句话说明> |
```

#### 12.4 生成指令

按以下步骤生成报告：

1. **创建报告目录**：
   ```bash
   mkdir -p report
   ```

2. **获取时间戳**：
   ```bash
   TIMESTAMP=$(date +%Y%m%d_%H%M%S)
   ```

3. **解析 test.py 输出**：从 Step 11 捕获的远程测试输出中，按 12.5 的规则提取各项数据（优化前后两组）。

4. **使用 Write 工具写入 Markdown 报告**：将解析后的数据填充到 12.3 模板中，写入 `report/<算子名>_optimize_${TIMESTAMP}.md`。

5. **生成 HTML 和 PDF**：调用报告转换脚本，从 Markdown 生成可交互 HTML 和 PDF：
   ```bash
   python scripts/generate_report.py report/<算子名>_optimize_${TIMESTAMP}.md
   ```

   该脚本自动生成同名的 `.html` 和 `.pdf` 文件。

   **HTML 特性**（通过 Plotly + 原生 JS 实现）：
   - 优化前后性能对比柱状图
   - 可排序表格（点击表头升/降序）
   - 可折叠章节（点击 h2 标题展开/收起）
   - PASS/FAIL 自动着色
   - 响应式布局 + 暗色模式支持

   **PDF 特性**（通过 weasyprint 生成）：
   - A4 排版，中文字体支持（自动查找系统 CJK 字体并通过 `@font-face` 嵌入）
   - 表格自动分页避免截断
   - 适合归档和打印
   - **CJK 字体依赖**：系统需安装中文字体，推荐 `sudo yum install google-noto-sans-cjk-sc-fonts`（或 `apt install fonts-noto-cjk`）

   **依赖**：`pip install mistune jinja2 weasyprint`（如无 weasyprint 则跳过 PDF）

6. **输出报告路径**：告知用户所有已生成的报告文件路径。

#### 12.5 数据提取规则

从 test.py 输出中提取数据的匹配模式：

| 字段 | 匹配模式 | 说明 |
|------|---------|------|
| 设备型号 | `Device: <name>` 或 `GPU: <name>` | test.py 输出的设备信息行 |
| 正确性 pass/fail | `PASS` / `FAIL` / `passed` / `failed` | 每个 test case 结果 |
| 最大绝对误差 | `max abs error: <float>` 或 `atol: <float>` | 浮点格式，含科学记数法 |
| 最大相对误差 | `max rel error: <float>` 或 `rtol: <float>` | 浮点格式，含科学记数法 |
| 平均延迟 | `avg: <float> ms` 或 `mean: <float> ms` | 毫秒单位 |
| 有效带宽 | `bandwidth: <float> GB/s` 或 `throughput: <float> GB/s` | GB/s 单位 |
| 带宽利用率 | `bandwidth utilization: <float>%` 或 `BW util: <float>%` | 百分比 |
| 计算利用率 | `compute utilization: <float>%` 或 `compute util: <float>%` | 百分比 |
| 瓶颈类型 | `bottleneck: <type>` 或 `Memory-bound` / `Compute-bound` / `Latency-bound` | 瓶颈分类关键字 |
| 加速比 | `speedup: <float>x` 或从优化前后延迟计算 | 优化后相对优化前的加速 |
| 编译器版本 | `compiler: <version>` 或从编译输出提取 | 编译器版本信息 |

> **注意**：如果 test.py 输出格式与上述模式不完全匹配，应灵活提取可用数据，缺失字段标注"N/A"。如果没有优化前的基准数据，优化前列填"N/A"，加速比标注"无基准"。

#### 12.6 多版本对比报告（含 CUDA 基线）

当进行了多轮优化或需要与 CUDA 原版对比时，报告需扩展为三维对比：**HCU 优化前 → HCU 优化后 → CUDA 基线**。

**数据来源**：
1. **HCU 多版本数据**：使用 `bench_all.py` 在同一 HCU 服务器上同时 benchmark 所有版本，确保公平对比
2. **CUDA 基线数据**：从 `report/` 下已有的迁移报告中提取 H20/A100 等 CUDA 设备的性能数据
3. **GPU 硬件参数**：从 `references/gpu参数对比.csv` 读取峰值带宽、FP32 算力等参数

**bench_all.py 模板**：

```python
"""Comprehensive benchmark: all HIP versions on HCU"""
import torch, sys

# Import all versions
versions = {}
for name in ['<算子>_hip', '<算子>_hip_opt', '<算子>_hip_opt2']:
    try:
        versions[name] = __import__(name)
    except ImportError:
        print(f"  [SKIP] {name} not installed")

# Benchmark function using CUDA events for accurate GPU timing
def benchmark(func, args, n_warmup=10, n_iter=100):
    for _ in range(n_warmup): func(*args)
    torch.cuda.synchronize()
    times = []
    for _ in range(n_iter):
        start = torch.cuda.Event(enable_timing=True)
        end = torch.cuda.Event(enable_timing=True)
        start.record(); func(*args); end.record()
        torch.cuda.synchronize()
        times.append(start.elapsed_time(end))
    return sum(times)/len(times), min(times)

# Run all versions on all sizes, output summary + speedup table
```

**报告额外章节**：

在标准 6 章节基础上，性能对比（章节 3）需包含：

```markdown
### 3.1 HCU 多版本对比（Forward/Backward 分表）
| 规模 | 原迁移 | 第一轮优化 | 第二轮优化 | opt2 vs 原迁移 |

### 3.2 HCU vs CUDA 对比
| 规模 | CUDA Forward | HCU opt2 Forward | HCU/CUDA 比 | CUDA Backward | HCU opt2 Backward | HCU/CUDA 比 |

### 3.3 优化进展总结
| 规模 | 原迁移 HCU/CUDA 比 | opt2 HCU/CUDA 比 |
```

**HCU vs CUDA 差距分析要点**：
- 带宽差异（如 H20 4000 GB/s vs BW1000 1800 GB/s = 2.2x）
- Cache 容量差异（如 H20 L2 50MB vs BW1000 L2 8MB）
- Wavefront/Warp 大小差异对特定 kernel 的影响
- 编译器成熟度差异

---
