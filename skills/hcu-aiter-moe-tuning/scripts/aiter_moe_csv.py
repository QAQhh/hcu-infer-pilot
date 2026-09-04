#!/usr/bin/env python3
"""Collect and safely manage AITER ASM fused-MoE tuning CSVs."""

import argparse
import csv
import math
import os
import re
import shutil
import stat
from collections import Counter
from datetime import datetime
from pathlib import Path


INPUT_COLUMNS = [
    "quant_type",
    "indtype",
    "token",
    "inter_dim",
    "model_dim",
    "expert",
    "topk",
    "q_size_n",
    "q_size_k",
]
FULL_KEY_COLUMNS = ["arch"] + INPUT_COLUMNS
TUNED_COLUMNS = FULL_KEY_COLUMNS + ["sol_type", "sol_id", "time_us"]
OBSERVED_RUNTIME_KEY_COLUMNS = [
    "arch", "quant_type", "token", "inter_dim", "model_dim", "expert", "topk"
]
POSITIVE_INT_COLUMNS = ["token", "inter_dim", "model_dim", "expert", "topk"]
NONNEGATIVE_INT_COLUMNS = ["q_size_n", "q_size_k"]
ASM_SOLUTION_RE = re.compile(r"^[0-9]+\+[0-9]+$")
LOG_PAIR_RE = re.compile(
    r"\b(arch|quant(?:_type)?|tokens?|inter_dim|model_dim|expert|topk|"
    r"q_size_n|q_size_k)\s*[:=]\s*([A-Za-z0-9_.+\-]+)"
)

HCU_89_TOKENS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    20, 24, 28, 32, 34, 36, 40, 44, 48, 56, 64, 68, 72, 80, 88, 96,
    104, 112, 128, 144, 160, 192, 224, 256, 320, 384, 448, 512, 576,
    640, 704, 768, 832, 896, 960, 1024, 1152, 1280, 1408, 1536, 1664,
    1792, 1920, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096,
    4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192, 10240, 12288,
    14336, 16384, 17408, 24576, 32768, 40960, 49152, 57344, 65536,
]


def fail(message):
    raise SystemExit("ERROR: " + message)


def read_csv(path):
    path = Path(path)
    if not path.is_file():
        fail("CSV does not exist: {}".format(path))
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            fail("CSV has no header: {}".format(path))
        return reader.fieldnames, list(reader)


def normalized_key(row, columns):
    return tuple(str(row.get(column, "")).strip() for column in columns)


def atomic_write_csv(path, fieldnames, rows, overwrite=False, mode=0o644):
    path = Path(path)
    if path.exists() and not overwrite:
        fail("output already exists; pass --force or choose another path: {}".format(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(".{}.tmp.{}".format(path.name, os.getpid()))
    try:
        with temporary.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(str(temporary), mode)
        os.replace(str(temporary), str(path))
    finally:
        if temporary.exists():
            temporary.unlink()


def validate_rows(path, kind, arch=None, reference=None, allow_empty=False):
    fieldnames, rows = read_csv(path)
    required = INPUT_COLUMNS if kind == "input" else TUNED_COLUMNS
    missing_columns = [column for column in required if column not in fieldnames]
    if missing_columns:
        fail("{} is missing columns: {}".format(path, missing_columns))
    if not rows and not allow_empty:
        fail("CSV has no data rows: {}".format(path))

    errors = []
    row_keys = []
    seen_arches = set()
    for line_number, row in enumerate(rows, start=2):
        for column in ("quant_type", "indtype"):
            if not row.get(column, "").strip():
                errors.append("line {}: empty {}".format(line_number, column))
        for column in POSITIVE_INT_COLUMNS:
            try:
                if int(row[column]) <= 0:
                    raise ValueError
            except (KeyError, TypeError, ValueError):
                errors.append(
                    "line {}: invalid positive {}={!r}".format(
                        line_number, column, row.get(column)
                    )
                )
        for column in NONNEGATIVE_INT_COLUMNS:
            try:
                if int(row[column]) < 0:
                    raise ValueError
            except (KeyError, TypeError, ValueError):
                errors.append(
                    "line {}: invalid nonnegative {}={!r}".format(
                        line_number, column, row.get(column)
                    )
                )

        if kind == "tuned":
            row_arch = row.get("arch", "").strip()
            seen_arches.add(row_arch)
            if not row_arch:
                errors.append("line {}: empty arch".format(line_number))
            if arch and row_arch != arch:
                errors.append(
                    "line {}: arch={!r}, expected {!r}".format(
                        line_number, row_arch, arch
                    )
                )
            if row.get("sol_type", "").strip().lower() != "asm":
                errors.append(
                    "line {}: sol_type={!r}, expected 'asm'".format(
                        line_number, row.get("sol_type")
                    )
                )
            if not ASM_SOLUTION_RE.fullmatch(row.get("sol_id", "").strip()):
                errors.append(
                    "line {}: invalid ASM sol_id={!r}".format(
                        line_number, row.get("sol_id")
                    )
                )
            try:
                elapsed = float(row["time_us"])
                if not math.isfinite(elapsed) or elapsed <= 0:
                    raise ValueError
            except (KeyError, TypeError, ValueError):
                errors.append(
                    "line {}: invalid positive time_us={!r}".format(
                        line_number, row.get("time_us")
                    )
                )
            row_keys.append(normalized_key(row, FULL_KEY_COLUMNS))
        else:
            row_keys.append(normalized_key(row, INPUT_COLUMNS))

    if kind == "tuned" and len(seen_arches) > 1:
        errors.append("tuned result mixes architectures: {}".format(sorted(seen_arches)))
    duplicates = [key for key, count in Counter(row_keys).items() if count > 1]
    if duplicates:
        errors.append("duplicate logical keys: {}".format(duplicates[:10]))

    if reference:
        reference_fields, reference_rows = read_csv(reference)
        missing_reference = [
            column for column in INPUT_COLUMNS if column not in reference_fields
        ]
        if missing_reference:
            errors.append("reference is missing columns: {}".format(missing_reference))
        else:
            reference_keys = {
                normalized_key(row, INPUT_COLUMNS) for row in reference_rows
            }
            actual_keys = {
                normalized_key(row, INPUT_COLUMNS) for row in rows
            }
            if actual_keys != reference_keys:
                errors.append(
                    "key set differs from reference: missing={}, extra={}".format(
                        sorted(reference_keys - actual_keys)[:20],
                        sorted(actual_keys - reference_keys)[:20],
                    )
                )

    if errors:
        preview = "\n".join("  - " + item for item in errors[:30])
        suffix = "" if len(errors) <= 30 else "\n  ... {} more".format(len(errors) - 30)
        fail("{} failed validation:\n{}{}".format(path, preview, suffix))
    return fieldnames, rows


def parse_tokens_text(text):
    values = []
    for item in re.split(r"[\s,]+", text.strip()):
        if not item:
            continue
        try:
            value = int(item)
        except ValueError:
            fail("invalid token value: {!r}".format(item))
        if value <= 0:
            fail("token values must be positive: {}".format(value))
        values.append(value)
    if not values:
        fail("token list is empty")
    return sorted(set(values))


def command_generate(args):
    if args.token_grid:
        tokens = list(HCU_89_TOKENS)
    elif args.tokens:
        tokens = parse_tokens_text(args.tokens)
    else:
        tokens = parse_tokens_text(args.token_file.read_text(encoding="utf-8"))
    rows = []
    for token in tokens:
        rows.append(
            {
                "quant_type": args.quant_type,
                "indtype": args.indtype,
                "token": token,
                "inter_dim": args.inter_dim,
                "model_dim": args.model_dim,
                "expert": args.expert,
                "topk": args.topk,
                "q_size_n": args.q_size_n,
                "q_size_k": args.q_size_k,
            }
        )
    atomic_write_csv(args.output, INPUT_COLUMNS, rows, args.force)
    validate_rows(args.output, "input")
    print("generated={} rows={}".format(args.output, len(rows)))


def parse_log_line(line):
    values = {}
    for key, value in LOG_PAIR_RE.findall(line):
        normalized = {
            "quant": "quant_type",
            "quant_type": "quant_type",
            "token": "token",
            "tokens": "token",
        }.get(key, key)
        values[normalized] = value
    required = {
        "arch", "quant_type", "token", "inter_dim", "model_dim", "expert", "topk"
    }
    return values if required.issubset(values) else None


def command_collect(args):
    parsed = []
    matching_lines = 0
    for log_path in args.logs:
        if not log_path.is_file():
            fail("log does not exist: {}".format(log_path))
        with log_path.open(encoding="utf-8", errors="replace") as handle:
            for line in handle:
                values = parse_log_line(line)
                if values is None:
                    continue
                matching_lines += 1
                if args.arch and values["arch"] != args.arch:
                    continue
                if args.quant_type and values["quant_type"] != args.quant_type:
                    continue
                parsed.append(values)
    if not parsed:
        fail("no matching AITER MoE size lines found")
    arches = sorted({row["arch"] for row in parsed})
    if len(arches) != 1:
        fail("logs contain multiple architectures {}; pass --arch".format(arches))

    unique = {}
    for item in parsed:
        row = {
            "quant_type": item["quant_type"],
            "indtype": args.indtype,
            "token": int(item["token"]),
            "inter_dim": int(item["inter_dim"]),
            "model_dim": int(item["model_dim"]),
            "expert": int(item["expert"]),
            "topk": int(item["topk"]),
            "q_size_n": int(item.get("q_size_n", args.q_size_n)),
            "q_size_k": int(item.get("q_size_k", args.q_size_k)),
        }
        unique[normalized_key(row, INPUT_COLUMNS)] = row
    rows = sorted(
        unique.values(),
        key=lambda row: (
            row["quant_type"], row["indtype"], row["inter_dim"],
            row["model_dim"], row["expert"], row["topk"],
            row["q_size_n"], row["q_size_k"], row["token"],
        ),
    )
    atomic_write_csv(args.output, INPUT_COLUMNS, rows, args.force)
    validate_rows(args.output, "input")
    print(
        "collected={} arch={} parsed_lines={} unique_rows={}".format(
            args.output, arches[0], matching_lines, len(rows)
        )
    )


def command_validate(args):
    _, rows = validate_rows(args.csv, args.kind, args.arch, args.reference)
    tokens = [int(row["token"]) for row in rows]
    print(
        "validated={} kind={} rows={} token_min={} token_max={}".format(
            args.csv, args.kind, len(rows), min(tokens), max(tokens)
        )
    )


def command_dedup(args):
    if args.input.resolve() == args.output.resolve():
        fail("dedup output must differ from input so the raw file is preserved")
    fieldnames, rows = read_csv(args.input)
    if all(column in fieldnames for column in TUNED_COLUMNS):
        columns = FULL_KEY_COLUMNS
    elif all(column in fieldnames for column in INPUT_COLUMNS):
        columns = INPUT_COLUMNS
    else:
        fail("input is neither an AITER untuned nor tuned CSV")

    selected = []
    seen = set()
    iterable = reversed(rows) if args.keep == "last" else rows
    for row in iterable:
        item_key = normalized_key(row, columns)
        if item_key not in seen:
            seen.add(item_key)
            selected.append(row)
    if args.keep == "last":
        selected.reverse()
    atomic_write_csv(args.output, fieldnames, selected, args.force)
    print(
        "deduplicated={} input_rows={} output_rows={} removed={} keep={}".format(
            args.output, len(rows), len(selected), len(rows) - len(selected), args.keep
        )
    )


def command_coverage(args):
    if args.missing_output and args.input.resolve() == args.missing_output.resolve():
        fail("--missing-output must differ from --input")
    _, input_rows = validate_rows(args.input, "input")
    table_fields, table_rows = read_csv(args.table)
    required = FULL_KEY_COLUMNS + ["sol_type", "sol_id"]
    missing_columns = [column for column in required if column not in table_fields]
    if missing_columns:
        fail("table is missing columns: {}".format(missing_columns))

    valid_table_keys = set()
    for row in table_rows:
        if (
            row.get("sol_type", "").strip().lower() == "asm"
            and ASM_SOLUTION_RE.fullmatch(row.get("sol_id", "").strip())
        ):
            valid_table_keys.add(normalized_key(row, FULL_KEY_COLUMNS))

    missing_rows = []
    covered = 0
    for row in input_rows:
        item_key = tuple([args.arch] + list(normalized_key(row, INPUT_COLUMNS)))
        if item_key in valid_table_keys:
            covered += 1
        else:
            missing_rows.append(row)

    print(
        "arch={} requested={} covered={} missing={} table={}".format(
            args.arch, len(input_rows), covered, len(missing_rows), args.table
        )
    )
    if missing_rows:
        print("missing_tokens=" + ",".join(row["token"] for row in missing_rows))
    if args.missing_output:
        atomic_write_csv(
            args.missing_output, INPUT_COLUMNS, missing_rows, args.force
        )
        print("missing_output={}".format(args.missing_output))
    if args.require_complete and missing_rows:
        raise SystemExit(1)


def command_merge(args):
    if args.source.resolve() == args.target.resolve():
        fail("--source and --target must differ")
    if args.in_place and (not args.reference or not args.arch):
        fail("in-place merge requires both --reference and --arch")
    if not args.in_place:
        if args.output.resolve() in (args.target.resolve(), args.source.resolve()):
            fail("non-destructive --output must differ from --target and --source")
    source_fields, source_rows = validate_rows(
        args.source, "tuned", args.arch, args.reference
    )
    target_fields, target_rows = read_csv(args.target)
    if set(source_fields) != set(target_fields):
        fail(
            "CSV schemas differ: target={}, source={}".format(
                target_fields, source_fields
            )
        )

    target_by_runtime_key = {}
    for row in target_rows:
        runtime_key = normalized_key(row, OBSERVED_RUNTIME_KEY_COLUMNS)
        target_by_runtime_key.setdefault(runtime_key, []).append(row)
    runtime_collisions = []
    for source_row in source_rows:
        runtime_key = normalized_key(source_row, OBSERVED_RUNTIME_KEY_COLUMNS)
        for target_row in target_by_runtime_key.get(runtime_key, []):
            if normalized_key(source_row, FULL_KEY_COLUMNS) != normalized_key(
                target_row, FULL_KEY_COLUMNS
            ):
                runtime_collisions.append(
                    {
                        "runtime_key": runtime_key,
                        "source_indtype_q": normalized_key(
                            source_row, ["indtype", "q_size_n", "q_size_k"]
                        ),
                        "target_indtype_q": normalized_key(
                            target_row, ["indtype", "q_size_n", "q_size_k"]
                        ),
                    }
                )
    if runtime_collisions and not args.allow_runtime_key_collision:
        fail(
            "source collides with existing rows under an observed reduced AITER "
            "runtime key; inspect the target revision or pass "
            "--allow-runtime-key-collision only when proven safe: {}".format(
                runtime_collisions[:5]
            )
        )

    source_keys = {
        normalized_key(row, FULL_KEY_COLUMNS) for row in source_rows
    }
    merged = [
        row for row in target_rows
        if normalized_key(row, FULL_KEY_COLUMNS) not in source_keys
    ] + source_rows

    if args.in_place:
        output = args.target
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = args.target.with_name(args.target.name + ".bak." + timestamp)
        if backup.exists():
            fail("backup already exists: {}".format(backup))
        shutil.copy2(str(args.target), str(backup))
        mode = stat.S_IMODE(args.target.stat().st_mode)
        atomic_write_csv(output, target_fields, merged, overwrite=True, mode=mode)
        print("backup={}".format(backup))
    else:
        output = args.output
        mode = stat.S_IMODE(args.target.stat().st_mode)
        atomic_write_csv(output, target_fields, merged, args.force, mode=mode)
    print(
        "merged={} old_rows={} source_rows={} total_rows={}".format(
            output, len(target_rows), len(source_rows), len(merged)
        )
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description="AITER ASM fused-MoE size CSV utility"
    )
    subparsers = parser.add_subparsers(dest="command")

    generate = subparsers.add_parser("generate", help="generate an untuned CSV")
    generate.add_argument("--quant-type", required=True)
    generate.add_argument("--indtype", required=True)
    generate.add_argument("--inter-dim", type=int, required=True)
    generate.add_argument("--model-dim", type=int, required=True)
    generate.add_argument("--expert", type=int, required=True)
    generate.add_argument("--topk", type=int, required=True)
    generate.add_argument("--q-size-n", type=int, default=0)
    generate.add_argument("--q-size-k", type=int, default=0)
    token_source = generate.add_mutually_exclusive_group(required=True)
    token_source.add_argument("--tokens", help="comma/space-separated token sizes")
    token_source.add_argument("--token-file", type=Path)
    token_source.add_argument("--token-grid", choices=("hcu-89",))
    generate.add_argument("--output", type=Path, required=True)
    generate.add_argument("--force", action="store_true")
    generate.set_defaults(func=command_generate)

    collect = subparsers.add_parser("collect", help="parse AITER size logs")
    collect.add_argument("logs", type=Path, nargs="+")
    collect.add_argument("--arch")
    collect.add_argument("--quant-type")
    collect.add_argument("--indtype", default="torch.bfloat16")
    collect.add_argument("--q-size-n", type=int, default=0)
    collect.add_argument("--q-size-k", type=int, default=0)
    collect.add_argument("--output", type=Path, required=True)
    collect.add_argument("--force", action="store_true")
    collect.set_defaults(func=command_collect)

    validate = subparsers.add_parser("validate", help="validate a CSV")
    validate.add_argument("--csv", type=Path, required=True)
    validate.add_argument("--kind", choices=("input", "tuned"), required=True)
    validate.add_argument("--arch")
    validate.add_argument("--reference", type=Path)
    validate.set_defaults(func=command_validate)

    dedup = subparsers.add_parser("dedup", help="deduplicate a CSV by full key")
    dedup.add_argument("--input", type=Path, required=True)
    dedup.add_argument("--output", type=Path, required=True)
    dedup.add_argument("--keep", choices=("first", "last"), default="last")
    dedup.add_argument("--force", action="store_true")
    dedup.set_defaults(func=command_dedup)

    coverage = subparsers.add_parser("coverage", help="check exact table coverage")
    coverage.add_argument("--input", type=Path, required=True)
    coverage.add_argument("--table", type=Path, required=True)
    coverage.add_argument("--arch", required=True)
    coverage.add_argument("--missing-output", type=Path)
    coverage.add_argument("--require-complete", action="store_true")
    coverage.add_argument("--force", action="store_true")
    coverage.set_defaults(func=command_coverage)

    merge = subparsers.add_parser("merge", help="merge tuned rows by full key")
    merge.add_argument("--target", type=Path, required=True)
    merge.add_argument("--source", type=Path, required=True)
    merge.add_argument("--arch")
    merge.add_argument("--reference", type=Path)
    destination = merge.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output", type=Path)
    destination.add_argument("--in-place", action="store_true")
    merge.add_argument("--force", action="store_true")
    merge.add_argument("--allow-runtime-key-collision", action="store_true")
    merge.set_defaults(func=command_merge)
    return parser


def main():
    args = build_parser().parse_args()
    if not hasattr(args, "func"):
        fail("choose one command: generate, collect, validate, dedup, coverage, or merge")
    for name in ("inter_dim", "model_dim", "expert", "topk"):
        if hasattr(args, name) and getattr(args, name) <= 0:
            fail("--{} must be positive".format(name.replace("_", "-")))
    for name in ("q_size_n", "q_size_k"):
        if hasattr(args, name) and getattr(args, name) < 0:
            fail("--{} must be nonnegative".format(name.replace("_", "-")))
    args.func(args)


if __name__ == "__main__":
    main()
