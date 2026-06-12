#!/usr/bin/env python3
import argparse
import os
import re
import sys


ORDER = [
    "mode",
    "source",
    "hardware_type",
    "strategy",
    "gpu_ids",
    "should_clean",
    "chunk_size",
    "tune_warmup_times",
    "tune_loop_times",
    "bench_warmup_times",
    "bench_loop_times",
    "test_times",
    "enable_bestkernel_csv",
    "cu_count",
    "update_target_config",
    "enable_mk_n_threshold",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Update rocBLAS auto_select configs/tuning_args.txt."
    )
    parser.add_argument("--file", required=True, help="Path to tuning_args.txt")
    parser.add_argument("--mode", default="user")
    parser.add_argument("--source", default="layer3", choices=["layer3", "layer4", "csv"])
    parser.add_argument("--hardware-type", default="NMZ")
    parser.add_argument("--strategy", default="common")
    parser.add_argument("--gpu-ids", default="0 1 2 3 4 5 6 7")
    parser.add_argument("--should-clean", default="0", choices=["0", "1"])
    parser.add_argument("--chunk-size", default="10")
    parser.add_argument("--tune-warmup-times", default="2")
    parser.add_argument("--tune-loop-times", default="4")
    parser.add_argument("--bench-warmup-times", default="2")
    parser.add_argument("--bench-loop-times", default="10")
    parser.add_argument("--test-times", default="2")
    parser.add_argument("--enable-bestkernel-csv", default="0", choices=["0", "1"])
    parser.add_argument("--cu-count", default="72")
    parser.add_argument("--update-target-config", default="0", choices=["0", "1"])
    parser.add_argument("--enable-mk-n-threshold", default="0", choices=["0", "1"])
    parser.add_argument(
        "--dry-run", action="store_true", help="Print updated content without writing"
    )
    return parser.parse_args()


def values_from_args(args):
    return {
        "mode": args.mode,
        "source": args.source,
        "hardware_type": args.hardware_type,
        "strategy": args.strategy,
        "gpu_ids": args.gpu_ids,
        "should_clean": args.should_clean,
        "chunk_size": args.chunk_size,
        "tune_warmup_times": args.tune_warmup_times,
        "tune_loop_times": args.tune_loop_times,
        "bench_warmup_times": args.bench_warmup_times,
        "bench_loop_times": args.bench_loop_times,
        "test_times": args.test_times,
        "enable_bestkernel_csv": args.enable_bestkernel_csv,
        "cu_count": args.cu_count,
        "update_target_config": args.update_target_config,
        "enable_mk_n_threshold": args.enable_mk_n_threshold,
    }


def update_content(content, values):
    seen = set()
    output = []
    pattern = re.compile(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*)\s*=\s*([^#\n]*)(.*)$")

    for line in content.splitlines():
        match = pattern.match(line)
        if not match:
            output.append(line)
            continue
        prefix, key, old_value, suffix = match.groups()
        if key not in values:
            output.append(line)
            continue
        seen.add(key)
        spacing = ""
        if suffix and not suffix.startswith(" "):
            spacing = " "
        output.append("%s%s=%s%s%s" % (prefix, key, values[key], spacing, suffix))

    missing = [key for key in ORDER if key in values and key not in seen]
    if missing:
        if output and output[-1].strip():
            output.append("")
        output.append("# Added by gemm-tuning skill")
        for key in missing:
            output.append("%s=%s" % (key, values[key]))

    return "\n".join(output) + "\n"


def main():
    args = parse_args()
    values = values_from_args(args)

    if not os.path.exists(args.file):
        print("[ERROR] file not found: %s" % args.file, file=sys.stderr)
        return 1

    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    updated = update_content(content, values)

    if args.dry_run:
        sys.stdout.write(updated)
        return 0

    with open(args.file, "w", encoding="utf-8") as f:
        f.write(updated)
    print("[OK] updated %s" % args.file)
    for key in ORDER:
        if key in values:
            print("  %s=%s" % (key, values[key]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

