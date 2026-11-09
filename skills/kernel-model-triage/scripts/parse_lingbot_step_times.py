#!/usr/bin/env python3
"""Parse LingBot StepTime logs with an auditable global-batch calculation."""

import argparse
import json
import math
import re
import statistics
import sys
import tempfile
from pathlib import Path


STEP_RE = re.compile(r"\bStepTime\s*(?:[:=]\s*)?([0-9]+(?:\.[0-9]+)?)\s*s\b", re.IGNORECASE)
CONFIG_KEYS = (
    "micro_batch_size",
    "gradient_accumulation_steps",
    "data_parallel_shard_size",
    "data_parallel_replicate_size",
    "max_steps",
)


def percentile(values, q):
    if not values:
        return None
    ordered = sorted(values)
    index = (len(ordered) - 1) * q
    lo, hi = math.floor(index), math.ceil(index)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] * (hi - index) + ordered[hi] * (index - lo)


def positive_integer(value, label):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} must be a positive integer") from None
    if isinstance(value, bool) or value is None or not math.isfinite(number) or number <= 0 or not number.is_integer():
        raise ValueError(f"{label} must be a positive integer")
    return int(number)


def parse_train_scalars(path):
    """Read only simple numeric keys from a top-level train YAML mapping."""
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"config must be a regular non-symlink file: {path}")
    if path.stat().st_size > 2 * 1024 * 1024:
        raise ValueError(f"config exceeds 2 MiB: {path}")
    values = {}
    in_train = False
    for raw in path.read_text(encoding="utf-8", errors="strict").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line:
            continue
        if re.match(r"^train:\s*$", line):
            in_train = True
            continue
        if in_train and re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:\s*", line):
            break
        if not in_train:
            continue
        match = re.match(r"^\s+([A-Za-z_][A-Za-z0-9_]*):\s*([0-9]+(?:\.[0-9]+)?)\s*$", line)
        if match and match.group(1) in CONFIG_KEYS:
            values[match.group(1)] = float(match.group(2))
    return values


def resolve_global_batch(args):
    config_values = parse_train_scalars(args.config) if args.config else {}
    config_micro = config_values.get("micro_batch_size")
    config_accumulation = config_values.get("gradient_accumulation_steps")
    requested_micro = args.micro_batch
    requested_accumulation = args.gradient_accumulation
    micro = requested_micro if requested_micro is not None else config_micro
    accumulation = (
        requested_accumulation
        if requested_accumulation is not None
        else config_accumulation
    )
    micro = positive_integer(micro, "micro batch") if micro is not None else None
    accumulation = positive_integer(accumulation, "gradient accumulation") if accumulation is not None else None
    if requested_micro is not None and config_micro is not None and micro != positive_integer(config_micro, "config micro batch"):
        if not args.allow_batch_mismatch:
            raise ValueError("CLI micro batch conflicts with config; use --allow-batch-mismatch only with reviewed evidence")
    if requested_accumulation is not None and config_accumulation is not None and accumulation != positive_integer(config_accumulation, "config gradient accumulation"):
        if not args.allow_batch_mismatch:
            raise ValueError("CLI gradient accumulation conflicts with config; use --allow-batch-mismatch only with reviewed evidence")
    shard = config_values.get("data_parallel_shard_size")
    replicate = config_values.get("data_parallel_replicate_size")
    if (shard is None) != (replicate is None):
        raise ValueError("config must provide both data_parallel_shard_size and data_parallel_replicate_size")
    config_data_parallel = (
        positive_integer(shard, "config data-parallel shard")
        * positive_integer(replicate, "config data-parallel replicate")
        if shard is not None and replicate is not None
        else None
    )
    requested_data_parallel = (
        positive_integer(args.data_parallel_size, "CLI data parallel size")
        if args.data_parallel_size is not None
        else None
    )
    actual_world = args.actual_world_size
    if actual_world is not None:
        actual_world = positive_integer(actual_world, "actual world size")
        if config_data_parallel is not None and config_data_parallel != actual_world:
            if not args.allow_topology_mismatch:
                raise ValueError(
                    f"actual world size {actual_world} conflicts with config data parallel size "
                    f"{int(config_data_parallel)}; use --allow-topology-mismatch only with reviewed topology evidence"
                )
        if requested_data_parallel is not None and requested_data_parallel != actual_world and not args.allow_topology_mismatch:
            raise ValueError(
                f"CLI data parallel size {requested_data_parallel} conflicts with actual world size {actual_world}; "
                "use --allow-topology-mismatch only with reviewed topology evidence"
            )
    if (
        requested_data_parallel is not None
        and config_data_parallel is not None
        and requested_data_parallel != config_data_parallel
        and not args.allow_topology_mismatch
    ):
        raise ValueError(
            f"CLI data parallel size {requested_data_parallel} conflicts with config value {config_data_parallel}; "
            "use --allow-topology-mismatch only with reviewed topology evidence"
        )
    data_parallel = requested_data_parallel if requested_data_parallel is not None else (
        actual_world if actual_world is not None else config_data_parallel
    )

    derived = None
    if micro is not None and accumulation is not None and data_parallel is not None:
        derived = micro * accumulation * positive_integer(data_parallel, "data parallel size")

    factors = {
        "micro_batch_size": micro,
        "gradient_accumulation_steps": accumulation,
        "data_parallel_size": positive_integer(data_parallel, "data parallel size") if data_parallel is not None else None,
        "config_data_parallel_size": int(config_data_parallel) if config_data_parallel is not None else None,
        "actual_world_size": actual_world,
        "config_values": config_values,
    }

    warnings = []
    if args.global_batch is not None:
        batch = positive_integer(args.global_batch, "global batch")
        if derived is not None and batch != derived:
            if not args.allow_batch_mismatch:
                raise ValueError(
                    f"CLI global batch {batch} conflicts with factor-derived value {derived}; "
                    "use --allow-batch-mismatch only after documenting why the factors are wrong"
                )
            warnings.append(f"CLI global batch {batch} overrides factor-derived value {derived} by explicit acknowledgement")
        return batch, "cli_mismatch_acknowledged" if derived not in (None, batch) else "cli", factors, warnings
    if derived is not None:
        return derived, "config_or_cli_factors", factors, warnings
    warnings.append("global batch unresolved; samples/s intentionally omitted")
    return None, "unresolved", factors, warnings


def summarize(step_times, warmup, global_batch):
    if warmup < 0:
        raise ValueError("--warmup must be non-negative")
    stable = step_times[warmup:]
    if not stable:
        raise ValueError("no stable StepTime samples remain after warmup")
    if any(not math.isfinite(value) or value <= 0 for value in stable):
        raise ValueError("StepTime samples must be finite and positive")
    mean = statistics.mean(stable)
    median = statistics.median(stable)
    result = {
        "all_steps": len(step_times),
        "warmup_steps": min(warmup, len(step_times)),
        "stable_steps": len(stable),
        "step_time_s": {
            "mean": mean,
            "median": median,
            "p50": percentile(stable, 0.50),
            "p90": percentile(stable, 0.90),
            "p95": percentile(stable, 0.95),
            "min": min(stable),
            "max": max(stable),
            "cv": statistics.pstdev(stable) / mean if len(stable) > 1 and mean else None,
        },
        "aggregate_samples_per_s": global_batch * len(stable) / sum(stable) if global_batch else None,
        "median_step_equivalent_samples_per_s": global_batch / median if global_batch else None,
    }
    return result


def self_test():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        log = root / "train.log"
        config = root / "config.yaml"
        log.write_text("StepTime 2.0s\nStepTime: 1.0s\nStepTime=1.2s\n", encoding="utf-8")
        config.write_text(
            "train:\n  micro_batch_size: 4\n  gradient_accumulation_steps: 2\n"
            "  data_parallel_shard_size: 8\n  data_parallel_replicate_size: 1\n",
            encoding="utf-8",
        )
        parsed = [float(value) for value in STEP_RE.findall(log.read_text(encoding="utf-8"))]
        assert len(parsed) == 3
        values = parse_train_scalars(config)
        assert values["micro_batch_size"] == 4
        class Args:
            pass
        args = Args()
        args.config, args.micro_batch, args.gradient_accumulation = config, None, None
        args.data_parallel_size, args.global_batch = None, None
        args.actual_world_size, args.allow_topology_mismatch, args.allow_batch_mismatch = 8, False, False
        batch, source, _, _ = resolve_global_batch(args)
        assert batch == 64 and source == "config_or_cli_factors"
        result = summarize(parsed, 1, batch)
        assert result["stable_steps"] == 2
        args.actual_world_size = 4
        try:
            resolve_global_batch(args)
        except ValueError as error:
            assert "actual world size" in str(error)
        else:
            raise AssertionError("topology mismatch must fail closed")
        args.actual_world_size = 8
        args.micro_batch = 3
        try:
            resolve_global_batch(args)
        except ValueError as error:
            assert "micro batch conflicts" in str(error)
        else:
            raise AssertionError("factor mismatch must fail closed")
    print("self-test: PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", nargs="?", type=Path)
    parser.add_argument("--config", type=Path, help="LingBot YAML used to derive batch factors.")
    parser.add_argument("--global-batch", type=float, help="Verified global batch; overrides derived factors.")
    parser.add_argument("--micro-batch", type=float)
    parser.add_argument("--gradient-accumulation", type=float)
    parser.add_argument("--data-parallel-size", type=float)
    parser.add_argument(
        "--actual-world-size",
        type=float,
        help="Observed launcher worker/device count. Bundled FSDP configs require this to match data-parallel size.",
    )
    parser.add_argument("--allow-topology-mismatch", action="store_true", help="Acknowledge a reviewed non-1:1 worker/DP topology.")
    parser.add_argument("--allow-batch-mismatch", action="store_true", help="Acknowledge an intentional CLI global-batch override.")
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--tail", type=int, help="Keep the last N parsed steps before discarding warmup; defaults to config max_steps when available.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.log is None:
        parser.error("log is required unless --self-test is used")

    if args.log.is_symlink() or not args.log.is_file():
        raise SystemExit(f"log must be a regular non-symlink file: {args.log}")
    if args.log.stat().st_size > 512 * 1024 * 1024:
        raise SystemExit(f"log exceeds 512 MiB: {args.log}")
    text = args.log.read_text(encoding="utf-8", errors="ignore")
    step_times = [float(value) for value in STEP_RE.findall(text)]
    if not step_times:
        raise SystemExit(f"no StepTime samples found in {args.log}")
    batch, source, batch_factors, warnings = resolve_global_batch(args)
    if args.tail is not None and args.tail < 1:
        parser.error("--tail must be a positive integer")
    config_max_steps = batch_factors["config_values"].get("max_steps")
    tail = args.tail if args.tail is not None else (
        positive_integer(config_max_steps, "config max_steps") if config_max_steps is not None else None
    )
    selected_times = step_times[-tail:] if tail else step_times
    if tail and len(step_times) < tail:
        warnings.append(f"log has {len(step_times)} StepTime samples, fewer than requested tail {tail}")
    if len(selected_times) - args.warmup < 20:
        warnings.append("fewer than 20 stable samples; treat throughput as a smoke result")
    payload = {
        "log": str(args.log),
        "config": str(args.config) if args.config else None,
        "global_batch": batch,
        "global_batch_source": source,
        "batch_factors": batch_factors,
        "parsed_steps": len(step_times),
        "tail_steps": tail,
        **summarize(selected_times, args.warmup, batch),
        "warnings": warnings,
    }
    rendered = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
