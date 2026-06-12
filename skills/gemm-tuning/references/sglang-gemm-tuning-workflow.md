# SGLang GEMM Tuning Workflow

Source documents:

- `https://r0ddbu55vzx.feishu.cn/docx/QVSndfw8coPSFBxiWkdcZPvanjf`
- `https://r0ddbu55vzx.feishu.cn/docx/PdupdKnAjo6Dh9x3OaUcHDsUnwd`

This workflow is adapted for:

- Service script: `/public/home/yangyn1/work_space/2026/sglang/run_model/minimax/run_qwen.sh`
- Work directory: `/public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning`
- Requested container: `yangyn_sglang`

## 1. Preflight

Check the requested container exists before doing live work:

```bash
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}' | grep -E 'yangyn_sglang|NAMES'
```

If `yangyn_sglang` is absent, report the available `yangyn_sglang*` containers and wait for permission before using another container. In the current node snapshot, `yangyn_sglang_qwen` was present and `yangyn_sglang` was not.

Create one run directory per capture:

```bash
mkdir -p /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/runs/$(date +%Y%m%d-%H%M%S)
```

## 2. Capture hipBLASLt Shapes

Start with a clean service run and enable hipBLASLt command logging:

```bash
export HIPBLASLT_LOG_MASK=32
bash /public/home/yangyn1/work_space/2026/sglang/run_model/minimax/run_qwen.sh 2>&1 | tee hipblaslt_capture.log
```

For vLLM, the source note says `--api-server-count 1` is needed, otherwise the expected prints may be missing. For SGLang, preserve the existing `run_qwen.sh` arguments unless the user asks to change them.

After the server is ready, send a small deterministic request. Prefer an existing repo request script such as:

```bash
bash /public/home/yangyn1/work_space/2026/sglang/run_model/minimax/req_qwen.sh
```

If no request script applies, use an OpenAI-compatible one-token request against the service port used by the run script.

Extract and deduplicate:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/extract_gemm_shapes.py \
  --kind hipblaslt \
  --input hipblaslt_capture.log \
  --tp 8 \
  --out-dir shapes
```

Important outputs:

- `hipblaslt_detail.csv`: every parsed record.
- `hipblaslt_report.csv`: grouped by trans/M/K with `N_range`.
- `hipblaslt_tuning.csv`: concrete N values with counts.
- `hipblaslt_sample.sh`: deduplicated `hipblaslt-bench` commands for tuning.

The source GLM5 W8A8 example found TN shapes such as:

```text
M=128 K=6144 N=1-16384
M=2624 K=6144 N=1-16384
M=4096 K=2048 N=1-16384
M=4096 K=6144 N=1-16384
M=6144 K=2048/12288/16384 N=1-16384
M=16384 K=2048 N=1-16384
M=24576 K=6144 N=1-16384
M=28672 K=512 N=1-16384
```

## 3. Generate and Apply hipBLASLt Config

Find the hipBLASLt benchmark tool. Common paths include:

```bash
/opt/dtk/lib/hipblaslt/benchmark_tool
/opt/dtk-26.04-rc4-ubuntu20.04/lib/hipblaslt/benchmark_tool
```

Then run:

```bash
chmod +x /path/to/benchmark_tool/hipblaslt-bench
chmod +x /path/to/benchmark_tool/hipblaslt_gentest.py
export PATH=/path/to/benchmark_tool:$PATH
HIPBLASLT_TUNING_FILE=hipblaslt.config bash shapes/hipblaslt_sample.sh
```

Validate by re-running the service with:

```bash
export HIPBLASLT_TUNING_OVERRIDE_FILE=/absolute/path/to/hipblaslt.config
export HIPBLASLT_LOG_LEVEL=4
```

The tuned log should include:

```text
HIPBLASLT_TUNING_OVERRIDE_FILE is the correct setting.
problem_override_from_file
Find solution with index:
```

Check with:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/check_tuning_hits.py \
  --log tuned_service.log \
  --expect hipblaslt
```

## 4. Capture rocBLAS Shapes

Restart the service cleanly and enable rocBLAS layer3 logging:

```bash
export ROCBLAS_LAYER=3
export TENSILE_DB=0x8000
bash /public/home/yangyn1/work_space/2026/sglang/run_model/minimax/run_qwen.sh 2>&1 | tee rocblas_capture.log
```

Send the same request workload used for hipBLASLt. Then extract:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/extract_gemm_shapes.py \
  --kind rocblas \
  --input rocblas_capture.log \
  --tp 8 \
  --default-gemmtype int8 \
  --out-dir shapes
```

Important outputs:

- `rocblas_detail.csv`: every parsed record.
- `rocblas_summary.csv`: grouped by trans/M/K with `N_range`.
- `rocblas_layer3_dedup.log`: deduplicated `rocblas-bench` layer3 lines when present.
- `rocblas_auto_select_size.csv`: CSV fallback for auto_select `source=csv`.

The source GLM5 W8A8 example found shapes such as:

```text
NN M=32 K=6144 N=1-16384
NN M=256 K=512/6144 N=1-16384
TN M=512 K=192 N=1-16384
TN M=6144 K=12288 N=1-16384
TN M=154880 K=6144 N=1-1024
```

## 5. Run rocBLAS auto_select

Read `references/rocblas-auto-select.md` before running this part. The short version:

```bash
cd /opt/dtk/lib/rocblas/auto_select_test/auto_select_tools
source /opt/dtk/env.sh
python3 Auto_tuning.py 2>&1 | tee tuning.log
```

For layer3 input, copy:

```bash
cp /path/to/shapes/rocblas_layer3_dedup.log rocblas_layer3_size/
```

For CSV fallback, copy:

```bash
cp /path/to/shapes/rocblas_auto_select_size.csv csv_size/csv/size.csv
```

Apply the generated config by environment variable:

```bash
export ROCBLAS_TENSILE_LIBPATH=/path/to/optimization_configs/new/config/library_gpu6
```

Do not overwrite system rocBLAS config directories during validation.

## 6. Performance and Correctness Validation

Use identical baseline and tuned workloads:

- Same model path, quantization, TP/PP/DP, memory settings, batch/input/output lengths.
- Same request script or benchmark.
- Only tuning variables differ.

For the Qwen script, validate both:

- Correctness: one small OpenAI-compatible request returns sane text and no error.
- Performance: same throughput/latency benchmark before and after tuning, if a benchmark script is available.

Keep this evidence in the run directory:

- `baseline_service.log`
- `tuned_service.log`
- baseline GEMM operator benchmark output, for example `baseline_gemm_perf.csv` or `baseline_gemm_perf.log`
- tuned GEMM operator benchmark output, for example `tuned_gemm_perf.csv` or `tuned_gemm_perf.log`
- extracted CSVs
- `hipblaslt.config` and/or `library_gpu*`
- request or benchmark output
- `tuning_report.md`

## 7. Final Tuning Report

After tuning and validation, always generate a Markdown report in the run directory:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/generate_tuning_report.py \
  --run-dir /path/to/run-dir \
  --backend rocblas \
  --model-path /path/to/model \
  --service-script /public/home/yangyn1/work_space/2026/sglang/run_model/minimax/run_qwen.sh \
  --baseline-perf /path/to/baseline_gemm_perf.csv \
  --tuned-perf /path/to/tuned_gemm_perf.csv \
  --tuning-artifact /path/to/optimization_configs/new/config/library_gpu6
```

The report must summarize:

- this tuning run's result and whether request validation passed.
- model-side captured shapes, including summary/detail CSV paths and tuning input path.
- pre-tuning GEMM operator performance and post-tuning GEMM operator performance.
- final tuning file or directory path.
- exact service-side environment variable to use the tuned file:
  - hipBLASLt: `HIPBLASLT_TUNING_OVERRIDE_FILE=/path/to/hipblaslt.config`
  - rocBLAS: `ROCBLAS_TENSILE_LIBPATH=/path/to/library_gpu*`

The generated Markdown report should be Chinese-first: headings, table labels, explanatory text, and missing-evidence notes should use Chinese. Keep command names, file paths, environment variables, backend names, and raw metric keys in their original technical form.

If baseline/tuned GEMM performance data is missing, do not estimate it. Generate the report anyway and clearly mark the performance comparison as incomplete.

If the run directory is container-owned, generate the report from inside the selected container:

```bash
docker exec yangyn_sglang_qwen python3 \
  /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/generate_tuning_report.py \
  --run-dir /path/to/run-dir \
  --backend rocblas \
  --baseline-perf /path/to/baseline_gemm_perf.csv \
  --tuned-perf /path/to/tuned_gemm_perf.csv \
  --tuning-artifact /path/to/optimization_configs/new/config/library_gpu6
```
