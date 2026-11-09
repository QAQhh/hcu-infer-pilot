#!/usr/bin/env python3
"""Summarize DriveDreamer step-timing JSON without inventing missing data."""

import argparse
import csv
import io
import json
import math
import statistics as stats
import sys
import tempfile
from pathlib import Path


METRICS = (
    "total_s",
    "data_wait_s",
    "forward_loss_s",
    "backward_optimizer_s",
    "stage_vae_encode_s",
    "stage_unet_s",
    "stage_backward_s",
    "stage_optimizer_step_s",
    "stage_ema_step_s",
)
GLOBAL_BATCH_KEYS = ("global_batch", "global_batch_size")
MICRO_BATCH_KEYS = ("micro_batch", "micro_batch_size", "per_device_train_batch_size")
ACCUMULATION_KEYS = ("gradient_accumulation_steps", "grad_accum_steps")
WORLD_SIZE_KEYS = ("world_size", "data_parallel_world_size", "dp_world_size")


def percentile(values, pct):
    ordered = sorted(values)
    if not ordered:
        return None
    k = (len(ordered) - 1) * pct / 100.0
    lo, hi = math.floor(k), math.ceil(k)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] * (hi - k) + ordered[hi] * (k - lo)


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def positive_integer(value, label):
    if isinstance(value, bool) or not finite_number(value):
        raise ValueError(f"{label} must be a finite positive integer")
    number = float(value)
    if number <= 0 or not number.is_integer():
        raise ValueError(f"{label} must be a finite positive integer")
    return int(number)


def json_number(value):
    if value is None:
        return None
    number = float(value)
    if math.isfinite(number):
        return number
    if math.isnan(number):
        return "NaN"
    return "Infinity" if number > 0 else "-Infinity"


def load_rows(path):
    with path.open("r", encoding="utf-8") as handle:
        rows = json.load(handle)
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{path}: expected a non-empty JSON list")
    if not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"{path}: every row must be an object")
    return rows


def select_rows(rows, start, tail):
    selected = []
    previous_step = None
    for row in rows:
        if "local_step" not in row:
            raise ValueError("every timing row must contain local_step")
        step = positive_integer(row["local_step"], "local_step")
        if previous_step is not None and step <= previous_step:
            raise ValueError("local_step values must be unique and strictly increasing in file order")
        previous_step = step
        if step >= start:
            selected.append(row)
    if tail:
        selected = selected[-tail:]
    return selected


def first_consistent_positive_integer(rows, keys, label):
    observed = set()
    for row in rows:
        present = [key for key in keys if row.get(key) is not None]
        if len(present) > 1:
            values = {positive_integer(row[key], key) for key in present}
            if len(values) != 1:
                raise ValueError(f"conflicting {label} fields in one row")
        for key in present:
            observed.add(positive_integer(row[key], key))
    if len(observed) > 1:
        raise ValueError(f"conflicting {label} values across timing rows")
    if len(observed) == 1:
        return observed.pop()
    return None


def infer_global_batch(rows, override, allow_mismatch=False):
    direct = first_consistent_positive_integer(rows, GLOBAL_BATCH_KEYS, "global batch")
    micro = first_consistent_positive_integer(rows, MICRO_BATCH_KEYS, "micro batch")
    accumulation = first_consistent_positive_integer(rows, ACCUMULATION_KEYS, "gradient accumulation")
    world = first_consistent_positive_integer(rows, WORLD_SIZE_KEYS, "world size")
    derived = micro * accumulation * world if all(value is not None for value in (micro, accumulation, world)) else None
    if direct is not None and derived is not None and direct != derived:
        raise ValueError(f"direct global batch {direct} conflicts with derived value {derived}")
    observed = direct if direct is not None else derived

    if override is not None:
        cli = positive_integer(override, "--global-batch")
        if observed is not None and cli != observed and not allow_mismatch:
            raise ValueError(
                f"--global-batch {cli} conflicts with timing evidence {observed}; "
                "use --allow-batch-mismatch only after documenting why the timing metadata is wrong"
            )
        return cli, "cli_override_mismatch_acknowledged" if observed not in (None, cli) else "cli"
    if direct is not None:
        return direct, "timing_json_global"
    if derived is not None:
        return derived, "timing_json_micro_x_accum_x_world"
    return None, "unresolved"


def metric_stats(rows, metric):
    values = [float(row[metric]) for row in rows if finite_number(row.get(metric))]
    if not values:
        return None
    return {
        "n": len(values),
        "median_s": stats.median(values),
        "mean_s": stats.mean(values),
        "p90_s": percentile(values, 90),
        "max_s": max(values),
    }


def summarize(label, rows, start, tail, global_batch, allow_batch_mismatch=False):
    selected = select_rows(rows, start, tail)
    if not selected:
        raise ValueError(f"{label}: no rows after filtering")
    for row in selected:
        for metric in METRICS:
            if metric not in row:
                continue
            if not finite_number(row[metric]):
                raise ValueError(f"{label}: {metric} must be finite when present")
            if metric == "total_s" and float(row[metric]) <= 0:
                raise ValueError(f"{label}: total_s must be strictly positive")
            if metric != "total_s" and float(row[metric]) < 0:
                raise ValueError(f"{label}: {metric} must be non-negative")
    batch, batch_source = infer_global_batch(selected, global_batch, allow_batch_mismatch)
    metrics = {name: value for name in METRICS if (value := metric_stats(selected, name)) is not None}

    losses = [(int(row["local_step"]), float(row["loss"])) for row in selected if isinstance(row.get("loss"), (int, float))]
    nan_steps = [step for step, loss in losses if not math.isfinite(loss)]
    finite_losses = [(step, loss) for step, loss in losses if math.isfinite(loss)]
    total_values = [float(row["total_s"]) for row in selected if finite_number(row.get("total_s")) and float(row["total_s"]) > 0]
    total_median = stats.median(total_values) if total_values else None
    aggregate_throughput = batch * len(total_values) / sum(total_values) if batch and total_values else None

    summary = {
        "label": label,
        "step_start": int(selected[0]["local_step"]),
        "step_end": int(selected[-1]["local_step"]),
        "rows": len(selected),
        "global_batch": batch,
        "global_batch_source": batch_source,
        "aggregate_samples_per_s": aggregate_throughput,
        "median_step_equivalent_samples_per_s": batch / total_median if batch and total_median else None,
        "throughput_valid_steps": len(total_values),
        "throughput_coverage": len(total_values) / len(selected),
        "metrics": metrics,
        "loss": {
            "observations": len(losses),
            "nonfinite_count": len(nan_steps),
            "nonfinite_steps": nan_steps[:50],
            "first": json_number(losses[0][1]) if losses else None,
            "last": json_number(losses[-1][1]) if losses else None,
            "last_finite": finite_losses[-1][1] if finite_losses else None,
        },
        "warnings": [],
    }
    if batch is None:
        summary["warnings"].append("global batch unresolved; throughput intentionally omitted")
    if len(total_values) != len(selected):
        summary["warnings"].append(
            f"throughput uses {len(total_values)}/{len(selected)} rows with finite positive total_s"
        )
    missing = [metric for metric in METRICS if metric not in metrics]
    if missing:
        summary["warnings"].append("missing metrics: " + ", ".join(missing))
    return selected, summary


def paired_loss_diff(left_label, left_rows, right_label, right_rows):
    def loss_by_step(rows):
        result = {}
        for row in rows:
            if "local_step" in row and isinstance(row.get("loss"), (int, float)):
                result[int(row["local_step"])] = float(row["loss"])
        return result

    left, right = loss_by_step(left_rows), loss_by_step(right_rows)
    shared = sorted(set(left) & set(right))
    diffs, nonfinite_mismatches = [], []
    for step in shared:
        a, b = left[step], right[step]
        if not (math.isfinite(a) and math.isfinite(b)):
            if math.isfinite(a) != math.isfinite(b):
                nonfinite_mismatches.append(step)
            continue
        diffs.append(abs(a - b))
    return {
        "left": left_label,
        "right": right_label,
        "shared_steps": len(shared),
        "finite_pairs": len(diffs),
        "max_abs_diff": max(diffs) if diffs else None,
        "median_abs_diff": stats.median(diffs) if diffs else None,
        "mean_abs_diff": stats.mean(diffs) if diffs else None,
        "nonfinite_mismatch_steps": nonfinite_mismatches[:50],
    }


def emit_csv(payload):
    def safe_cell(value):
        if isinstance(value, str) and value[:1] in {"=", "+", "-", "@"}:
            return "'" + value
        return value

    flat = []
    for run in payload["runs"]:
        row = {key: value for key, value in run.items() if key not in {"metrics", "loss", "warnings"}}
        for metric, values in run["metrics"].items():
            for stat_name, value in values.items():
                row[f"{metric}_{stat_name}"] = value
        row.update({f"loss_{key}": value for key, value in run["loss"].items() if not isinstance(value, list)})
        row["warnings"] = "; ".join(run["warnings"])
        flat.append({key: safe_cell(value) for key, value in row.items()})
    output = io.StringIO()
    keys = sorted({key for row in flat for key in row})
    writer = csv.DictWriter(output, fieldnames=keys)
    writer.writeheader()
    writer.writerows(flat)
    return output.getvalue()


def self_test():
    rows = [
        {"local_step": 1, "total_s": 2.0, "loss": 1.0},
        {"local_step": 2, "total_s": 1.0, "loss": 0.8},
        {"local_step": 3, "total_s": 1.2, "loss": float("nan")},
    ]
    _, summary = summarize("test", rows, 2, 0, 16)
    assert summary["rows"] == 2
    assert summary["median_step_equivalent_samples_per_s"] is not None
    assert summary["aggregate_samples_per_s"] is not None
    assert summary["metrics"].get("data_wait_s") is None
    _, unresolved = summarize("test", rows, 1, 0, None)
    assert unresolved["global_batch"] is None
    metadata_rows = [
        {"local_step": 1, "total_s": 1.0, "micro_batch_size": 2, "gradient_accumulation_steps": 4, "world_size": 8}
    ]
    _, derived = summarize("derived", metadata_rows, 1, 0, None)
    assert derived["global_batch"] == 64
    try:
        summarize("mismatch", metadata_rows, 1, 0, 32)
    except ValueError as error:
        assert "conflicts" in str(error)
    else:
        raise AssertionError("batch mismatch must fail closed")
    try:
        summarize("bad-order", [rows[1], rows[0]], 1, 0, None)
    except ValueError as error:
        assert "strictly increasing" in str(error)
    else:
        raise AssertionError("out-of-order steps must fail closed")
    try:
        summarize("bad-time", [{"local_step": 1, "total_s": -1.0}], 1, 0, None)
    except ValueError as error:
        assert "strictly positive" in str(error)
    else:
        raise AssertionError("non-positive total_s must fail closed")
    assert emit_csv({"runs": [{"label": "=formula", "metrics": {}, "loss": {}, "warnings": []}]})
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "rows.json"
        path.write_text(json.dumps(rows), encoding="utf-8")
        assert len(load_rows(path)) == 3
    print("self-test: PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1, help="Minimum local_step to include.")
    parser.add_argument("--tail", type=int, default=0, help="Keep the last N selected rows.")
    parser.add_argument("--global-batch", help="Verified finite positive integer global batch; otherwise infer from timing rows.")
    parser.add_argument(
        "--allow-batch-mismatch",
        action="store_true",
        help="Acknowledge that --global-batch intentionally overrides contradictory timing metadata.",
    )
    parser.add_argument("--format", choices=("json", "csv"), default="json")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--label", nargs=2, action="append", metavar=("LABEL", "JSON"))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.label:
        parser.error("at least one --label LABEL JSON is required")
    if args.tail < 0:
        parser.error("--tail must be non-negative")
    if args.start < 1:
        parser.error("--start must be a positive integer")

    summaries, filtered = [], []
    for label, path_text in args.label:
        selected, summary = summarize(
            label,
            load_rows(Path(path_text)),
            args.start,
            args.tail,
            args.global_batch,
            args.allow_batch_mismatch,
        )
        summaries.append(summary)
        filtered.append((label, selected))
    payload = {"runs": summaries}
    if len(filtered) == 2:
        payload["paired_loss"] = paired_loss_diff(filtered[0][0], filtered[0][1], filtered[1][0], filtered[1][1])
    if args.format == "json":
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2, allow_nan=False)
        print()
    else:
        print(emit_csv(payload), end="")


if __name__ == "__main__":
    main()
