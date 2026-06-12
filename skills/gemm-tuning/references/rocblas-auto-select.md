# rocBLAS auto_select Reference

The auto_select tool tunes rocBLAS GEMM sizes and emits config files for `ROCBLAS_TENSILE_LIBPATH`.

## Tool Location

Common directory:

```bash
/opt/dtk/lib/rocblas/auto_select_test/auto_select_tools
```

Some environments may use a versioned DTK path. Search for `Auto_tuning.py` if needed.

## Required Config

Edit `configs/tuning_args.txt`. At minimum, set:

```text
mode=user
source=layer3
hardware_type=NMZ
strategy=common
gpu_ids=0 1 2 3 4 5 6 7
should_clean=0
chunk_size=10
tune_warmup_times=2
tune_loop_times=4
bench_warmup_times=2
bench_loop_times=10
test_times=2
enable_bestkernel_csv=0
cu_count=72
update_target_config=0
enable_mk_n_threshold=0
```

Use `scripts/prepare_rocblas_tuning_args.py` to update the file without hand editing:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/prepare_rocblas_tuning_args.py \
  --file configs/tuning_args.txt \
  --source layer3 \
  --hardware-type NMZ \
  --gpu-ids "0 1 2 3 4 5 6 7" \
  --cu-count 72 \
  --chunk-size 10 \
  --test-times 2
```

## Input Formats

### Layer3

Set during capture:

```bash
export ROCBLAS_LAYER=3
export TENSILE_DB=0x8000
```

Put one `rocblas-bench` command per line in:

```bash
rocblas_layer3_size/
```

Layer3 is preferred when the log already contains `rocblas-bench` commands.

### CSV

Put CSV files in:

```bash
csv_size/csv/
```

Header:

```text
gemmtype,TransA,TransB,M,N,K,B
```

Example:

```text
int8,T,N,4096,128,6144,1
bf16,N,N,4096,128,4096,1
```

For KME/ECO/BW/NMZ hpa/bf16/int8 NN or TN with B=1, `N=-` may be used to let the tool enumerate N. Prefer concrete N values when shapes came from a serving log.

## Platform Mapping

```text
ZF   -> library       -> sgemm, hpa, hgemm
ZF2  -> library_gpu2  -> sgemm, hpa, hgemm, dgemm
KM   -> library_gpu3  -> sgemm, hpa
KME  -> library_gpu4  -> sgemm, hpa, bf16, int8
ECO  -> library_gpu4  -> sgemm, hpa, bf16, int8
BW   -> library_gpu5  -> sgemm, hpa, dgemm, bf16, int8, bss, cgemm, zgemm, tf32
NMZ  -> library_gpu6  -> sgemm, hpa, dgemm, bf16, int8, bss, cgemm, zgemm, tf32
```

Supported transpose types for sgemm/hpa/dgemm/bf16/int8/bss:

```text
NN NT TN TT
```

## Running

```bash
cd /opt/dtk/lib/rocblas/auto_select_test/auto_select_tools
source /opt/dtk/env.sh
python3 Auto_tuning.py 2>&1 | tee tuning.log
```

Use `should_clean=0` to resume after interruption. Use `should_clean=1` only when intentionally deleting previous artifacts.

## Outputs

Final config directory:

```bash
optimization_configs/new/config/library_*
```

Final result CSV:

```bash
optimization_results/merged_results_*.csv
```

Copy or record these files in the run directory before generating the final report:

```bash
cp -a optimization_configs/new/config/library_gpu6 /path/to/run-dir/
cp -a optimization_results/merged_results_*.csv /path/to/run-dir/ 2>/dev/null || true
```

Use the config through:

```bash
export ROCBLAS_TENSILE_LIBPATH=$(pwd)/optimization_configs/new/config/library_gpu6
```

Do not use `update_target_config=1` during first validation because it can overwrite source config files.

After the tuned service validation, generate `tuning_report.md` with:

```bash
python3 /public/home/yangyn1/work_space/2026/sglang/dcu-infer-pilot/skills/gemm-tuning/scripts/generate_tuning_report.py \
  --run-dir /path/to/run-dir \
  --backend rocblas \
  --baseline-perf /path/to/baseline_gemm_perf.csv \
  --tuned-perf /path/to/tuned_gemm_perf.csv \
  --tuning-artifact /path/to/optimization_configs/new/config/library_gpu6
```

## Common Failures

- "No valid size": wrong `hardware_type`, unsupported `gemmtype`, unsupported transpose, or malformed input.
- Failed common tuning tasks: inspect `optimization_artifacts/{tune_type}/{gemm_type}/{transpose}/log/`.
- Empty kernel result: check that no unrelated BLAS environment variables are forcing a bad library path.
