#!/usr/bin/env python3
import argparse
import os
import sys


HIPBLASLT_PATTERNS = [
    "HIPBLASLT_TUNING_OVERRIDE_FILE is the correct setting",
    "problem_override_from_file",
    "Find solution with index",
]

ROCBLAS_PATTERNS = [
    "ROCBLAS_TENSILE_LIBPATH",
    "library_gpu",
    "Tensile",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check service logs for evidence that GEMM tuning was used."
    )
    parser.add_argument("--log", required=True, help="Service log to inspect")
    parser.add_argument(
        "--expect",
        action="append",
        choices=["hipblaslt", "rocblas"],
        required=True,
        help="Expected tuning backend. Can be repeated.",
    )
    return parser.parse_args()


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def check_patterns(name, text, patterns, require_all):
    hits = [pattern for pattern in patterns if pattern in text]
    missing = [pattern for pattern in patterns if pattern not in text]
    print("[%s]" % name)
    for pattern in hits:
        print("  hit: %s" % pattern)
    for pattern in missing:
        print("  missing: %s" % pattern)
    if require_all:
        return len(missing) == 0
    return len(hits) > 0


def main():
    args = parse_args()
    if not os.path.exists(args.log):
        print("[ERROR] log not found: %s" % args.log, file=sys.stderr)
        return 1

    text = read_text(args.log)
    ok = True

    if "hipblaslt" in args.expect:
        ok = check_patterns("hipblaslt", text, HIPBLASLT_PATTERNS, True) and ok

    if "rocblas" in args.expect:
        # rocBLAS logs vary by DTK version, so require at least one indicator.
        ok = check_patterns("rocblas", text, ROCBLAS_PATTERNS, False) and ok

    if ok:
        print("[OK] expected tuning evidence found")
        return 0

    print("[ERROR] expected tuning evidence missing", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

