#!/usr/bin/env python3
import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report for a GEMM tuning run."
    )
    parser.add_argument("--run-dir", required=True, help="Run directory to summarize")
    parser.add_argument(
        "--backend",
        choices=["hipblaslt", "rocblas"],
        default="rocblas",
        help="Tuning backend used for this run",
    )
    parser.add_argument("--model-path", default="", help="Model path used by serving")
    parser.add_argument("--service-script", default="", help="Service startup script")
    parser.add_argument("--baseline-perf", default="", help="CSV/log for pre-tuning GEMM performance")
    parser.add_argument("--tuned-perf", default="", help="CSV/log for post-tuning GEMM performance")
    parser.add_argument("--tuning-artifact", default="", help="Final tuning file or directory")
    parser.add_argument("--shape-dir", default="", help="Directory containing extracted shape CSVs")
    parser.add_argument("--baseline-log", default="", help="Baseline serving log")
    parser.add_argument("--tuned-log", default="", help="Tuned serving log")
    parser.add_argument("--request-result", default="", help="Correctness request output JSON")
    parser.add_argument("--output", default="", help="Output Markdown path")
    return parser.parse_args()


def read_text(path):
    if not path or not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def read_csv_rows(path, limit=None):
    if not path or not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8-sig", errors="ignore", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows[:limit] if limit else rows


def existing(path):
    return path if path and os.path.exists(path) else ""


def find_first(root, names):
    if not root or not os.path.isdir(root):
        return ""
    for dirpath, _, filenames in os.walk(root):
        for name in names:
            if name in filenames:
                return os.path.join(dirpath, name)
    return ""


def find_shape_dir(run_dir, backend):
    preferred = [
        "shapes_bench",
        "shapes_trace",
        "shapes",
        "shape",
    ]
    for name in preferred:
        path = os.path.join(run_dir, name)
        if os.path.isdir(path):
            if backend == "rocblas" and os.path.exists(
                os.path.join(path, "rocblas_summary.csv")
            ):
                return path
            if backend == "hipblaslt" and os.path.exists(
                os.path.join(path, "hipblaslt_report.csv")
            ):
                return path
    return ""


def find_request(run_dir):
    for name in ("request.json", "request_result.json", "chat_completion.json"):
        path = os.path.join(run_dir, name)
        if os.path.exists(path):
            return path
    return ""


def find_tuning_artifact(run_dir, backend):
    if backend == "hipblaslt":
        names = ["hipblaslt.config"]
        found = find_first(run_dir, names)
        if found:
            return found
    else:
        for dirpath, dirnames, _ in os.walk(run_dir):
            for dirname in dirnames:
                if dirname.startswith("library_gpu") or dirname == "library":
                    return os.path.join(dirpath, dirname)
        found = find_first(run_dir, ["rocblas_TensileLibrary.dat"])
        if found:
            return os.path.dirname(found)
    return ""


def md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def md_table(headers, rows):
    if not rows:
        return "_无数据。_\n"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(md_escape(cell) for cell in row) + " |")
    return "\n".join(out) + "\n"


def parse_shape_summary(path):
    rows = []
    if not path or not os.path.exists(path):
        return rows
    with open(path, "r", encoding="utf-8-sig", errors="ignore", newline="") as f:
        raw_rows = [row for row in csv.reader(f) if any(cell.strip() for cell in row)]
    header_index = -1
    for idx, row in enumerate(raw_rows):
        normalized = [cell.strip().lower() for cell in row]
        if "trans" in normalized and "m" in normalized and "k" in normalized:
            header_index = idx
            break
    if header_index < 0:
        return rows
    headers = [cell.strip() for cell in raw_rows[header_index]]
    for row in raw_rows[header_index + 1 :]:
        item = {}
        for index, header in enumerate(headers):
            item[header] = row[index].strip() if index < len(row) else ""
        rows.append(item)
    return rows


def summarize_shapes(shape_dir, backend):
    if backend == "hipblaslt":
        summary = os.path.join(shape_dir, "hipblaslt_report.csv")
        detail = os.path.join(shape_dir, "hipblaslt_detail.csv")
        tuning_input = os.path.join(shape_dir, "hipblaslt_sample.sh")
    else:
        summary = os.path.join(shape_dir, "rocblas_summary.csv")
        detail = os.path.join(shape_dir, "rocblas_detail.csv")
        tuning_input = os.path.join(shape_dir, "rocblas_layer3_dedup.log")
        if not os.path.exists(tuning_input):
            tuning_input = os.path.join(shape_dir, "rocblas_auto_select_size.csv")

    rows = parse_shape_summary(summary)
    detail_count = len(read_csv_rows(detail)) if detail else 0
    tuning_line_count = 0
    if os.path.exists(tuning_input):
        with open(tuning_input, "r", encoding="utf-8", errors="ignore") as f:
            tuning_line_count = sum(1 for line in f if line.strip())

    return {
        "summary": summary if os.path.exists(summary) else "",
        "detail": detail if os.path.exists(detail) else "",
        "tuning_input": tuning_input if os.path.exists(tuning_input) else "",
        "rows": rows,
        "detail_count": detail_count,
        "tuning_line_count": tuning_line_count,
    }


PERF_COLUMNS = [
    "time",
    "time_ms",
    "ms",
    "avg_ms",
    "median_ms",
    "us",
    "tflops",
    "gflops",
    "gb_s",
    "bandwidth",
]


def to_float(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?", text)
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def shape_key(row):
    keys = []
    for name in ("gemmtype", "trans", "TransA", "TransB", "M", "N", "K", "B"):
        if name in row:
            keys.append(str(row.get(name, "")).strip())
    if keys:
        return "|".join(keys)
    return "|".join(str(row.get(name, "")).strip() for name in sorted(row.keys())[:6])


def parse_perf_file(path):
    if not path or not os.path.exists(path):
        return {"path": path, "rows": [], "note": "未提供"}

    text = read_text(path)
    rows = []

    try:
        with open(path, "r", encoding="utf-8-sig", errors="ignore", newline="") as f:
            sample = f.read(4096)
            f.seek(0)
            dialect = csv.Sniffer().sniff(sample, delimiters=",\t ")
            reader = csv.DictReader(f, dialect=dialect)
            if reader.fieldnames:
                rows = [row for row in reader if row]
    except Exception:
        rows = []

    if rows:
        return {"path": path, "rows": rows, "note": ""}

    parsed = []
    for line in text.splitlines():
        if not line.strip():
            continue
        values = {}
        for match in re.finditer(r"([A-Za-z_][A-Za-z0-9_./-]*)\s*[=:]\s*([^\s,]+)", line):
            values[match.group(1)] = match.group(2)
        if values:
            values["_line"] = line.strip()
            parsed.append(values)
    return {"path": path, "rows": parsed, "note": "" if parsed else "未解析到有效行"}


def select_metric_columns(rows):
    if not rows:
        return []
    keys = set()
    for row in rows[:50]:
        keys.update(row.keys())
    selected = []
    for key in keys:
        lowered = key.strip().lower()
        if lowered in PERF_COLUMNS or any(token in lowered for token in PERF_COLUMNS):
            selected.append(key)
    return sorted(selected)


def perf_comparison(baseline_path, tuned_path):
    base = parse_perf_file(baseline_path)
    tuned = parse_perf_file(tuned_path)
    base_rows = base["rows"]
    tuned_rows = tuned["rows"]
    base_metrics = select_metric_columns(base_rows)
    tuned_metrics = select_metric_columns(tuned_rows)
    metrics = [m for m in base_metrics if m in tuned_metrics]
    if not metrics:
        metrics = sorted(set(base_metrics + tuned_metrics))

    by_key_tuned = {shape_key(row): row for row in tuned_rows}
    rows = []
    for row in base_rows:
        key = shape_key(row)
        tuned_row = by_key_tuned.get(key)
        if not tuned_row:
            continue
        for metric in metrics:
            b = to_float(row.get(metric))
            t = to_float(tuned_row.get(metric))
            if b is None or t is None:
                continue
            if "time" in metric.lower() or metric.lower().endswith("ms") or metric.lower() == "us":
                delta = (b - t) / b * 100 if b else 0
                direction = "延迟越低越好"
            else:
                delta = (t - b) / b * 100 if b else 0
                direction = "吞吐越高越好"
            rows.append([key, metric, "%.6g" % b, "%.6g" % t, "%.2f%%" % delta, direction])
            break
        if len(rows) >= 50:
            break

    return {
        "baseline": base,
        "tuned": tuned,
        "metrics": metrics,
        "rows": rows,
    }


def parse_request(path):
    if not path or not os.path.exists(path):
        return {}
    text = read_text(path)
    try:
        data = json.loads(text)
    except Exception:
        return {"raw": text[:500]}
    result = {
        "id": data.get("id", ""),
        "model": data.get("model", ""),
    }
    usage = data.get("usage") or {}
    if usage:
        result["prompt_tokens"] = usage.get("prompt_tokens", "")
        result["completion_tokens"] = usage.get("completion_tokens", "")
        result["total_tokens"] = usage.get("total_tokens", "")
    choices = data.get("choices") or []
    if choices:
        message = choices[0].get("message") or {}
        result["finish_reason"] = choices[0].get("finish_reason", "")
        result["content"] = (message.get("content") or "")[:180]
    return result


def model_usage(backend, artifact):
    if backend == "hipblaslt":
        env = "HIPBLASLT_TUNING_OVERRIDE_FILE=%s" % artifact
        note = "在启动模型服务前设置该环境变量。"
    else:
        env = "ROCBLAS_TENSILE_LIBPATH=%s" % artifact
        note = "在启动模型服务前设置该环境变量；验证阶段不要覆盖系统 rocBLAS 配置目录。"
    return env, note


def main():
    args = parse_args()
    run_dir = os.path.abspath(args.run_dir)
    if not os.path.isdir(run_dir):
        print("[ERROR] run-dir not found: %s" % run_dir, file=sys.stderr)
        return 1

    shape_dir = existing(args.shape_dir) or find_shape_dir(run_dir, args.backend)
    request_path = existing(args.request_result) or find_request(run_dir)
    tuning_artifact = existing(args.tuning_artifact) or find_tuning_artifact(
        run_dir, args.backend
    )
    output = args.output or os.path.join(run_dir, "tuning_report.md")

    shape_info = summarize_shapes(shape_dir, args.backend) if shape_dir else {
        "summary": "",
        "detail": "",
        "tuning_input": "",
        "rows": [],
        "detail_count": 0,
        "tuning_line_count": 0,
    }
    perf = perf_comparison(args.baseline_perf, args.tuned_perf)
    request = parse_request(request_path)

    usage_env, usage_note = model_usage(args.backend, tuning_artifact or "<未找到调优产物>")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append("# GEMM 调优报告")
    lines.append("")
    lines.append("生成时间：`%s`" % now)
    lines.append("")
    lines.append("## 运行摘要")
    lines.append("")
    lines.append(md_table(
        ["项目", "内容"],
        [
            ["调优后端", args.backend],
            ["运行目录", run_dir],
            ["模型路径", args.model_path or request.get("model", "") or "未提供"],
            ["服务启动脚本", args.service_script or "未提供"],
            ["Shape 目录", shape_dir or "未找到"],
            ["调优产物", tuning_artifact or "未找到"],
        ],
    ))

    lines.append("## 正确性验证")
    lines.append("")
    if request:
        field_names = {
            "id": "请求 ID",
            "model": "模型",
            "prompt_tokens": "输入 token 数",
            "completion_tokens": "输出 token 数",
            "total_tokens": "总 token 数",
            "finish_reason": "结束原因",
            "content": "返回内容片段",
            "raw": "原始内容片段",
        }
        rows = [[field_names.get(key, key), value] for key, value in request.items()]
        lines.append(md_table(["字段", "内容"], rows))
    else:
        lines.append("_未提供或未找到请求结果文件。_\n")

    lines.append("## 模型端抓取的 Shape")
    lines.append("")
    lines.append(md_table(
        ["项目", "内容"],
        [
            ["Shape 汇总 CSV", shape_info["summary"] or "未找到"],
            ["Shape 明细 CSV", shape_info["detail"] or "未找到"],
            ["调优输入文件", shape_info["tuning_input"] or "未找到"],
            ["解析到的 GEMM 记录数", shape_info["detail_count"]],
            ["去重后的调优输入行数", shape_info["tuning_line_count"]],
        ],
    ))
    shape_rows = []
    for row in shape_info["rows"][:40]:
        shape_rows.append(
            [
                row.get("trans", ""),
                row.get("M", ""),
                row.get("N_range", row.get("N", "")),
                row.get("K", ""),
                row.get("tp", ""),
            ]
        )
    lines.append(md_table(["转置", "M", "N 范围", "K", "TP"], shape_rows))
    if len(shape_info["rows"]) > 40:
        lines.append("_仅展示前 40 组 shape。_\n")

    lines.append("## GEMM 算子性能")
    lines.append("")
    lines.append(md_table(
        ["项目", "内容"],
        [
            ["调优前性能文件", perf["baseline"]["path"] or "未提供"],
            ["调优后性能文件", perf["tuned"]["path"] or "未提供"],
            ["调优前解析状态", perf["baseline"]["note"] or "已解析"],
            ["调优后解析状态", perf["tuned"]["note"] or "已解析"],
        ],
    ))
    if perf["rows"]:
        lines.append(md_table(
            ["Shape key", "指标", "调优前", "调优后", "改善幅度", "判断方向"],
            perf["rows"],
        ))
    else:
        lines.append(
            "_未找到可对比的调优前/调优后 GEMM 性能记录。"
            "请提供带有匹配 shape key 的 `--baseline-perf` 和 `--tuned-perf` CSV/log 文件，报告会自动补齐该表格。_\n"
        )

    lines.append("## 调优产物")
    lines.append("")
    lines.append(md_table(
        ["项目", "内容"],
        [
            ["最终调优文件或目录", tuning_artifact or "未找到"],
            ["调优后端", args.backend],
        ],
    ))

    lines.append("## 模型端使用方式")
    lines.append("")
    lines.append("启动模型服务前设置以下环境变量：")
    lines.append("")
    lines.append("```bash")
    lines.append("export %s" % usage_env)
    if args.service_script:
        lines.append("bash %s" % args.service_script)
    else:
        lines.append("bash /path/to/run_model.sh")
    lines.append("```")
    lines.append("")
    lines.append(usage_note)
    lines.append("")

    lines.append("## 验证备注")
    lines.append("")
    notes = []
    if not tuning_artifact:
        notes.append("- 未找到最终调优产物；需要完成 tuning 后再把这份报告作为最终结果。")
    if not perf["rows"]:
        notes.append("- GEMM 算子调优前/调优后性能对比不完整。")
    if not shape_info["rows"]:
        notes.append("- 未找到 shape 汇总记录。")
    if not request:
        notes.append("- 未找到正确性请求结果。")
    if not notes:
        notes.append("- shape 抓取、请求验证、调优产物和性能对比均已记录。")
    lines.extend(notes)
    lines.append("")

    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("[OK] wrote %s" % output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
