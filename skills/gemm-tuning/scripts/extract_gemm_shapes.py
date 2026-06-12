#!/usr/bin/env python3
import argparse
import csv
import os
import re
import stat
import sys
from collections import Counter, defaultdict


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract hipBLASLt and rocBLAS GEMM shapes from serving logs."
    )
    parser.add_argument("--kind", choices=["auto", "hipblaslt", "rocblas"], default="auto")
    parser.add_argument("-i", "--input", required=True, help="Input service log")
    parser.add_argument("--out-dir", default=".", help="Output directory")
    parser.add_argument("--tp", default="", help="Tensor parallel size for reports")
    parser.add_argument(
        "--default-gemmtype",
        default="int8",
        help="GEMM type for rocBLAS CSV fallback when it cannot be inferred",
    )
    return parser.parse_args()


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def pick(pattern, text, flags=re.IGNORECASE):
    match = re.search(pattern, text, flags)
    return match.group(1) if match else ""


def normalize_spaces(text):
    return re.sub(r"\s+", " ", text).strip()


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def infer_gemmtype_from_rocblas_bench(line, default_gemmtype):
    fn = pick(r"(?:^|\s)-f\s+(\S+)", line)
    a_type = pick(r"--a_type\s+(\S+)", line)
    b_type = pick(r"--b_type\s+(\S+)", line)
    d_type = pick(r"--d_type\s+(\S+)", line)
    compute_type = pick(r"--compute_type\s+(\S+)", line)
    math_mode = pick(r"--math_mode\s+(\S+)", line)

    if math_mode == "1":
        return "tf32"
    if "i8" in (a_type + b_type).lower() or "8i" in (a_type + b_type).lower():
        return "int8"
    if "bf16" in (a_type + b_type + d_type + compute_type).lower():
        return "bf16"
    if "f16" in (a_type + b_type + d_type).lower():
        return "hpa"
    if fn in ("gemm", "gemm_ex") and (
        "f32" in (a_type + b_type + d_type + compute_type).lower()
    ):
        return "sgemm"
    return default_gemmtype


def extract_hipblaslt_commands(text):
    flat = normalize_spaces(text)
    pattern = re.compile(
        r"(hipblaslt-bench\b.*?--activation_type\s+\S+)", re.IGNORECASE
    )
    return [normalize_spaces(item) for item in pattern.findall(flat)]


def hipblaslt_key(cmd):
    return (
        pick(r"--api_method\s+(\S+)", cmd),
        pick(r"(?:^|\s)-m\s+(\d+)", cmd),
        pick(r"(?:^|\s)-n\s+(\d+)", cmd),
        pick(r"(?:^|\s)-k\s+(\d+)", cmd),
        pick(r"--lda\s+(\d+)", cmd),
        pick(r"--ldb\s+(\d+)", cmd),
        pick(r"--ldc\s+(\d+)", cmd),
        pick(r"--ldd\s+(\d+)", cmd),
        pick(r"--stride_a\s+(\d+)", cmd),
        pick(r"--stride_b\s+(\d+)", cmd),
        pick(r"--stride_c\s+(\d+)", cmd),
        pick(r"--stride_d\s+(\d+)", cmd),
        pick(r"--alpha\s+(\S+)", cmd),
        pick(r"--beta\s+(\S+)", cmd),
        pick(r"--transA\s+([TN])", cmd).upper(),
        pick(r"--transB\s+([TN])", cmd).upper(),
        pick(r"--batch_count\s+(\d+)", cmd),
        pick(r"--scaleA\s+(\S+)", cmd),
        pick(r"--scaleB\s+(\S+)", cmd),
        pick(r"--a_type\s+(\S+)", cmd),
        pick(r"--b_type\s+(\S+)", cmd),
        pick(r"--c_type\s+(\S+)", cmd),
        pick(r"--d_type\s+(\S+)", cmd),
        pick(r"--scale_type\s+(\S+)", cmd),
        pick(r"--bias_type\s+(\S+)", cmd),
        pick(r"--compute_type\s+(\S+)", cmd),
        pick(r"--activation_type\s+(\S+)", cmd),
    )


def is_valid_hipblaslt_key(key):
    required = [0, 1, 2, 3, 14, 15, 19, 20, 23, 25, 26]
    return all(key[i] for i in required)


def parse_hipblaslt(text):
    commands = extract_hipblaslt_commands(text)
    records = []
    dedup = []
    seen = set()
    invalid = 0

    for cmd in commands:
        key = hipblaslt_key(cmd)
        if not is_valid_hipblaslt_key(key):
            invalid += 1
            continue
        if key not in seen:
            seen.add(key)
            dedup.append(cmd)
        records.append(
            {
                "trans": key[14] + key[15],
                "m": int(key[1]),
                "n": int(key[2]),
                "k": int(key[3]),
            }
        )

    return records, dedup, len(commands), invalid


def write_hipblaslt_outputs(text, out_dir, tp):
    records, dedup, candidate_count, invalid_count = parse_hipblaslt(text)
    if not records:
        return {
            "records": 0,
            "candidates": candidate_count,
            "invalid": invalid_count,
            "files": [],
        }

    detail_rows = [["index", "trans", "M", "N", "K", "tp"]]
    for index, rec in enumerate(records, 1):
        detail_rows.append([index, rec["trans"], rec["m"], rec["n"], rec["k"], tp])

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["trans"], rec["m"], rec["k"], tp)].append(rec["n"])

    report_rows = [["hipblaslt gemm size", "", "", "", ""]]
    report_rows.append(["trans", "M", "N_range", "K", "tp"])
    first = True
    for key, n_list in sorted(groups.items()):
        trans, m, k, tp_value = key
        n_min = min(n_list)
        n_max = max(n_list)
        n_range = str(n_min) if n_min == n_max else "%s-%s" % (n_min, n_max)
        report_rows.append([trans, m, n_range, k, tp_value if first else ""])
        first = False

    counter = Counter((rec["trans"], rec["m"], rec["n"], rec["k"], tp) for rec in records)
    tuning_rows = [["hipblaslt tuning sizes", "", "", "", "", ""]]
    tuning_rows.append(["trans", "M", "N", "K", "tp", "count"])
    for key, count in sorted(counter.items()):
        trans, m, n, k, tp_value = key
        tuning_rows.append([trans, m, n, k, tp_value, count])

    detail = os.path.join(out_dir, "hipblaslt_detail.csv")
    report = os.path.join(out_dir, "hipblaslt_report.csv")
    tuning = os.path.join(out_dir, "hipblaslt_tuning.csv")
    sample = os.path.join(out_dir, "hipblaslt_sample.sh")

    write_csv(detail, detail_rows)
    write_csv(report, report_rows)
    write_csv(tuning, tuning_rows)
    with open(sample, "w", encoding="utf-8") as f:
        f.write("\n".join(dedup))
        if dedup:
            f.write("\n")
    os.chmod(sample, os.stat(sample).st_mode | stat.S_IXUSR)

    return {
        "records": len(records),
        "candidates": candidate_count,
        "invalid": invalid_count,
        "unique": len(dedup),
        "files": [detail, report, tuning, sample],
    }


def parse_rocblas_bench_line(line, default_gemmtype):
    ta = pick(r"--transposeA\s+([TN])\b", line)
    tb = pick(r"--transposeB\s+([TN])\b", line)
    m = pick(r"(?:^|\s)-m\s+(\d+)\b", line)
    n = pick(r"(?:^|\s)-n\s+(\d+)\b", line)
    k = pick(r"(?:^|\s)-k\s+(\d+)\b", line)
    if not (ta and tb and m and n and k):
        return None
    return {
        "trans": ta.upper() + tb.upper(),
        "ta": ta.upper(),
        "tb": tb.upper(),
        "m": int(m),
        "n": int(n),
        "k": int(k),
        "gemmtype": infer_gemmtype_from_rocblas_bench(line, default_gemmtype),
        "bench": normalize_spaces(line),
    }


def parse_rocblas_api_line(line, default_gemmtype):
    match = re.search(
        r"rocblas_gemm(?:_strided_batched)?_ex,([TN]),([TN]),(\d+),(\d+),(\d+),",
        line,
        re.IGNORECASE,
    )
    if not match:
        return None
    ta = match.group(1).upper()
    tb = match.group(2).upper()
    return {
        "trans": ta + tb,
        "ta": ta,
        "tb": tb,
        "m": int(match.group(3)),
        "n": int(match.group(4)),
        "k": int(match.group(5)),
        "gemmtype": default_gemmtype,
        "bench": "",
    }


def parse_rocblas(text, default_gemmtype):
    records = []
    bench_lines = []
    seen_bench = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        record = None
        if "rocblas-bench" in line:
            record = parse_rocblas_bench_line(line, default_gemmtype)
        elif "rocblas_gemm_ex," in line or "rocblas_gemm_strided_batched_ex," in line:
            record = parse_rocblas_api_line(line, default_gemmtype)
        if record is None:
            continue
        records.append(record)
        if record["bench"] and record["bench"] not in seen_bench:
            seen_bench.add(record["bench"])
            bench_lines.append(record["bench"])
    return records, bench_lines


def write_rocblas_outputs(text, out_dir, tp, default_gemmtype):
    records, bench_lines = parse_rocblas(text, default_gemmtype)
    if not records:
        return {"records": 0, "files": []}

    detail_rows = [["index", "gemmtype", "trans", "M", "N", "K", "tp"]]
    for index, rec in enumerate(records, 1):
        detail_rows.append(
            [index, rec["gemmtype"], rec["trans"], rec["m"], rec["n"], rec["k"], tp]
        )

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["trans"], rec["m"], rec["k"], tp)].append(rec["n"])

    summary_rows = [["rocblas gemm size", "", "", "", ""]]
    summary_rows.append(["trans", "M", "N_range", "K", "tp"])
    first = True
    for key, n_list in sorted(groups.items()):
        trans, m, k, tp_value = key
        n_min = min(n_list)
        n_max = max(n_list)
        n_range = str(n_min) if n_min == n_max else "%s-%s" % (n_min, n_max)
        summary_rows.append([trans, m, n_range, k, tp_value if first else ""])
        first = False

    csv_counter = Counter(
        (rec["gemmtype"], rec["ta"], rec["tb"], rec["m"], rec["n"], rec["k"], 1)
        for rec in records
    )
    auto_rows = [["gemmtype", "TransA", "TransB", "M", "N", "K", "B"]]
    for key in sorted(csv_counter.keys()):
        auto_rows.append(list(key))

    detail = os.path.join(out_dir, "rocblas_detail.csv")
    summary = os.path.join(out_dir, "rocblas_summary.csv")
    auto_csv = os.path.join(out_dir, "rocblas_auto_select_size.csv")
    layer3 = os.path.join(out_dir, "rocblas_layer3_dedup.log")

    write_csv(detail, detail_rows)
    write_csv(summary, summary_rows)
    write_csv(auto_csv, auto_rows)
    with open(layer3, "w", encoding="utf-8") as f:
        f.write("\n".join(bench_lines))
        if bench_lines:
            f.write("\n")

    return {
        "records": len(records),
        "unique_layer3": len(bench_lines),
        "files": [detail, summary, auto_csv, layer3],
    }


def print_result(name, result):
    print("[%s]" % name)
    for key in sorted(result.keys()):
        if key == "files":
            continue
        print("  %s: %s" % (key, result[key]))
    for path in result.get("files", []):
        print("  file: %s" % path)


def main():
    args = parse_args()
    if not os.path.exists(args.input):
        print("[ERROR] input not found: %s" % args.input, file=sys.stderr)
        return 1

    ensure_dir(args.out_dir)
    text = read_text(args.input)
    any_records = False

    if args.kind in ("auto", "hipblaslt"):
        result = write_hipblaslt_outputs(text, args.out_dir, args.tp)
        print_result("hipblaslt", result)
        any_records = any_records or result.get("records", 0) > 0

    if args.kind in ("auto", "rocblas"):
        result = write_rocblas_outputs(text, args.out_dir, args.tp, args.default_gemmtype)
        print_result("rocblas", result)
        any_records = any_records or result.get("records", 0) > 0

    if not any_records:
        print("[ERROR] no GEMM records found", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

