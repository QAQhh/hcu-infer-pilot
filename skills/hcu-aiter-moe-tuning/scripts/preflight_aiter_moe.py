#!/usr/bin/env python3
"""Read-only preflight for an HCU AITER ASM MoE tuning run."""

import argparse
import importlib.util
import os
import re
from pathlib import Path


def fail(message):
    raise SystemExit("ERROR: " + message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aiter-root", type=Path, required=True)
    parser.add_argument("--aiter-python-root", type=Path)
    parser.add_argument("--quant-type", required=True)
    parser.add_argument("--expected-arch", required=True)
    parser.add_argument("--mode", choices=("no-shuffle", "shuffle"), required=True)
    parser.add_argument("--skip-gpu", action="store_true")
    args = parser.parse_args()

    root = args.aiter_root.resolve()
    problem_file = root / "moe_tune" / "moe_problem.py"
    required = [
        root / "moe_tune" / "moe_tune_runner.py",
        problem_file,
        root / "moe_tune" / "moe_tuner.py",
        root / "aiter" / "fused_moe_asm_wna16.py",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail("missing AITER files: {}".format(missing))

    problem_text = problem_file.read_text(encoding="utf-8")
    if args.quant_type not in problem_text:
        fail("tuner does not contain quant type {!r}".format(args.quant_type))
    if "find_asm_solutions" not in problem_text:
        fail("tuner does not expose ASM solution search")

    active_shuffle_weights = re.findall(
        r"^\s*self\.w[12]_qweight\s*=\s*asm_shuffle_weight_b8\s*\(",
        problem_text,
        flags=re.MULTILINE,
    )
    shuffle_markers = re.findall(
        r"\b([01])\s*,\s*#\s*shuffle\b", problem_text
    )
    named_shuffle = re.findall(
        r"\b(?:use_)?shuffle\s*=\s*([01])\b", problem_text
    )
    call_values = shuffle_markers if shuffle_markers else named_shuffle
    if not call_values:
        fail("cannot determine the tuner's shuffle call argument")

    if args.mode == "no-shuffle":
        if active_shuffle_weights:
            fail("active shuffled-weight statements found in no-shuffle mode")
        if set(call_values) != {"0"}:
            fail("cannot confirm shuffle=0 in tuner call")
    else:
        if len(active_shuffle_weights) < 2:
            fail("shuffle mode requires active w1 and w2 weight transforms")
        if set(call_values) != {"1"}:
            fail("cannot confirm shuffle=1 in tuner call")

    source_runtime = root / "aiter" / "fused_moe_asm_wna16.py"
    runtime_text = source_runtime.read_text(encoding="utf-8")
    if args.quant_type not in runtime_text:
        fail("AITER source runtime lacks quant type {!r}".format(args.quant_type))

    spec = importlib.util.find_spec("aiter")
    if spec is None or spec.origin is None:
        fail("cannot import aiter from the current Python environment")
    import_origin = Path(spec.origin).resolve()
    imported_runtime = import_origin.parent / "fused_moe_asm_wna16.py"
    if not imported_runtime.is_file():
        fail("imported AITER lacks {}".format(imported_runtime))
    if args.quant_type not in imported_runtime.read_text(encoding="utf-8"):
        fail("imported AITER runtime lacks quant type {!r}".format(args.quant_type))
    if args.aiter_python_root:
        python_root = args.aiter_python_root.resolve()
        if python_root != import_origin and python_root not in import_origin.parents:
            fail(
                "imported AITER is outside --aiter-python-root: origin={}, root={}".format(
                    import_origin, python_root
                )
            )

    print("aiter_root={}".format(root))
    print("aiter_import={}".format(import_origin))
    print("quant_type={} mode={}".format(args.quant_type, args.mode))
    print(
        "visibility HIP_VISIBLE_DEVICES={!r} ROCR_VISIBLE_DEVICES={!r} GPU_ARCHS={!r}".format(
            os.getenv("HIP_VISIBLE_DEVICES"),
            os.getenv("ROCR_VISIBLE_DEVICES"),
            os.getenv("GPU_ARCHS"),
        )
    )
    if os.getenv("GPU_ARCHS") and os.getenv("GPU_ARCHS") != args.expected_arch:
        fail(
            "GPU_ARCHS={!r}, expected {!r}".format(
                os.getenv("GPU_ARCHS"), args.expected_arch
            )
        )

    if args.skip_gpu:
        print("gpu_check=SKIPPED")
        return

    try:
        import torch
    except ImportError as exc:
        fail("cannot import torch: {}".format(exc))
    if not torch.cuda.is_available():
        fail("ROCm GPU is not visible to torch")
    arch = torch.cuda.get_device_properties(0).gcnArchName.split(":")[0]
    if arch != args.expected_arch:
        fail("expected {}, got {}".format(args.expected_arch, arch))
    print("torch={} hip={}".format(torch.__version__, torch.version.hip))
    print(
        "gpu={} arch={} visible_devices={}".format(
            torch.cuda.get_device_name(0), arch, torch.cuda.device_count()
        )
    )


if __name__ == "__main__":
    main()
