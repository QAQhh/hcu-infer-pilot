---
name: gemm-tuning
description: 面向 DCU/ROCm 上 SGLang 或 vLLM 服务的 GEMM tuning skill。用于抓取 hipBLASLt 或 rocBLAS GEMM shape、日志去重、生成 tuning 输入、运行 hipBLASLt tuning 或 rocBLAS auto_select、通过 HIPBLASLT_TUNING_OVERRIDE_FILE 或 ROCBLAS_TENSILE_LIBPATH 验证调优产物，并生成中文调优报告。用户提到 GEMM tuning、gemm tuing、hipblaslt tuning、rocblas tuning、BLAS auto_select、shape capture、SGLang run_qwen.sh 等请求时使用。
metadata:
  requires:
    bins: ["python3", "docker"]
---

# GEMM Tuning

这个 skill 用于把 SGLang/vLLM 模型服务日志转换成 hipBLASLt 或 rocBLAS 的 GEMM 调优输入，运行对应调优流程，验证模型服务是否使用调优产物，并产出中文 Markdown 报告。

## 运行上下文

- `SKILL_DIR`：当前 skill 根目录。默认是本文件所在目录，例如 `/public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning`。
- `RUN_DIR`：本次运行目录。默认放在 `${SKILL_DIR}/runs/<timestamp>`，但用户指定其他工作目录时应使用用户给出的目录。
- 服务启动脚本：优先使用用户指定脚本；未指定时可参考 `/public/home/yangyn1/work_space/2026/sglang/run_model/minimax/run_qwen.sh`。
- 容器：优先使用用户指定容器；未指定时优先尝试 `yangyn_sglang`。如果不存在，列出可用的 `yangyn_sglang*` 容器并请求用户确认，不要自行切换到不相关容器。
- 模型路径、端口、TP、量化方式、后端类型都应从用户请求、启动脚本或服务日志中确认，不要写死某一次调优的值。

## 核心流程

1. 开始 live capture 或服务验证前，按需阅读 `references/sglang-gemm-tuning-workflow.md`；做 rocBLAS auto_select 前，阅读 `references/rocblas-auto-select.md`。
2. 每次干净服务启动只启用一种 BLAS 日志模式：
   - hipBLASLt：`HIPBLASLT_LOG_MASK=32`
   - rocBLAS：`ROCBLAS_LAYER=3` 和 `TENSILE_DB=0x8000`
3. 在选定容器内启动服务，发送一个小请求确认服务可用，并把原始日志、请求、响应保存在本次 `RUN_DIR`。
4. 使用 `${SKILL_DIR}/scripts/extract_gemm_shapes.py` 从日志里提取并去重 shape。
5. 执行 tuning：
   - hipBLASLt：运行去重后的 `hipblaslt_sample.sh`，通过 `HIPBLASLT_TUNING_FILE=hipblaslt.config` 生成配置。
   - rocBLAS：准备 `configs/tuning_args.txt`，把 layer3 或 CSV 输入复制到 auto_select 工具输入目录，再运行 `Auto_tuning.py`。
6. 使用调优产物重新启动服务：
   - hipBLASLt：`HIPBLASLT_TUNING_OVERRIDE_FILE=/path/to/hipblaslt.config`
   - rocBLAS：`ROCBLAS_TENSILE_LIBPATH=/path/to/library_gpu*`
7. 用和基线一致的请求或 benchmark 验证服务；必要时用 `${SKILL_DIR}/scripts/check_tuning_hits.py` 检查日志里是否出现调优命中证据。
8. 完成前必须用 `${SKILL_DIR}/scripts/generate_tuning_report.py` 生成 `tuning_report.md`。

## 报告要求

`tuning_report.md` 必须主要使用中文，并包含以下信息：

- 模型侧抓取到的 shape 信息和提取出的 CSV 路径。
- tuning 前后的 GEMM 算子性能；有条件时使用显式的 baseline/tuned benchmark 文件。
- 最终 tuning 文件或目录路径。
- 模型端使用 tuning 产物所需的准确环境变量。
- 请求验证结果、token usage、服务日志路径。
- 如果缺少 baseline/tuned 性能证据，必须在报告中说明缺口，不要编造性能数据。

## 复用性约束

- 不要把某次运行的 `RUN_DIR`、模型路径、容器名、端口、GPU 平台或 `library_gpu*` 写死到脚本调用里；这些值应来自用户输入、环境探测或本次运行产物。
- 只把 `${SKILL_DIR}/scripts` 视为固定工具入口；调优输入、日志和产物都应写到本次 `RUN_DIR`。
- baseline 和 tuned 两轮除 tuning 环境变量外应保持一致。
- hipBLASLt 和 rocBLAS 日志模式需要分开启动服务抓取，避免混杂。
- rocBLAS auto_select 默认不要设置 `should_clean=1`，除非用户明确允许删除旧的 optimization artifacts。
- 不要自动覆盖系统 rocBLAS 配置目录；验证时优先使用 `ROCBLAS_TENSILE_LIBPATH` 指向本次产物目录。
- 如果日志或产物由 Docker 容器内 root 用户生成，报告也应在同一容器内生成，避免宿主侧权限问题。
- 任务结束前停止本次启动的模型服务，除非用户明确要求保留。

## 常用命令模板

设置 skill 根目录：

```bash
SKILL_DIR=/public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning
RUN_DIR=${SKILL_DIR}/runs/$(date +%Y%m%d-%H%M%S)
mkdir -p "${RUN_DIR}"
```

提取 hipBLASLt shape：

```bash
python3 "${SKILL_DIR}/scripts/extract_gemm_shapes.py" \
  --kind hipblaslt \
  --input "${RUN_DIR}/hipblaslt_capture.log" \
  --tp 8 \
  --out-dir "${RUN_DIR}/shapes"
```

提取 rocBLAS shape：

```bash
python3 "${SKILL_DIR}/scripts/extract_gemm_shapes.py" \
  --kind rocblas \
  --input "${RUN_DIR}/rocblas_capture.log" \
  --tp 8 \
  --default-gemmtype int8 \
  --out-dir "${RUN_DIR}/shapes"
```

检查 tuning 命中证据：

```bash
python3 "${SKILL_DIR}/scripts/check_tuning_hits.py" \
  --log "${RUN_DIR}/tuned_service.log" \
  --expect rocblas
```

生成中文报告：

```bash
python3 "${SKILL_DIR}/scripts/generate_tuning_report.py" \
  --run-dir "${RUN_DIR}" \
  --backend rocblas \
  --model-path /path/to/model \
  --service-script /path/to/start_service.sh \
  --shape-dir "${RUN_DIR}/shapes" \
  --baseline-perf "${RUN_DIR}/baseline_gemm_perf.csv" \
  --tuned-perf "${RUN_DIR}/tuned_gemm_perf.csv" \
  --tuning-artifact /path/to/library_gpu*
```

容器内生成报告示例：

```bash
docker exec <container> python3 "${SKILL_DIR}/scripts/generate_tuning_report.py" \
  --run-dir "${RUN_DIR}" \
  --backend rocblas \
  --tuning-artifact /path/to/library_gpu*
```
