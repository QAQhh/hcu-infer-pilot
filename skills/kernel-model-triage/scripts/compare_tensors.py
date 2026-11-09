#!/usr/bin/env python3
"""Compare tensor trees saved by torch.save and emit machine-readable metrics."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path


def load_torch():
    try:
        import torch
    except ImportError as exc:
        raise SystemExit("PyTorch is required to compare .pt/.pth tensor trees") from exc
    return torch


def flatten(value, prefix: str = "root"):
    torch = load_torch()
    if torch.is_tensor(value):
        return {prefix: value.detach().cpu()}
    if isinstance(value, dict):
        result = {}
        for key in sorted(value, key=str):
            result.update(flatten(value[key], f"{prefix}.{key}"))
        return result
    if isinstance(value, (list, tuple)):
        result = {}
        for index, item in enumerate(value):
            result.update(flatten(item, f"{prefix}[{index}]"))
        return result
    return {}


def tensor_metrics(reference, candidate, atol: float, rtol: float, equal_nan: bool, allow_dtype_mismatch: bool) -> dict:
    torch = load_torch()
    result = {
        "reference_shape": list(reference.shape),
        "candidate_shape": list(candidate.shape),
        "reference_dtype": str(reference.dtype),
        "candidate_dtype": str(candidate.dtype),
    }
    if reference.shape != candidate.shape:
        result.update({"allclose": False, "reason": "shape_mismatch"})
        return result
    if reference.dtype != candidate.dtype and not allow_dtype_mismatch:
        result.update({"allclose": False, "reason": "dtype_mismatch"})
        return result
    if not (reference.is_floating_point() or reference.is_complex()) and not (candidate.is_floating_point() or candidate.is_complex()):
        equal = reference.equal(candidate)
        result.update({"allclose": bool(equal), "finite_elements": int(reference.numel()), "mismatch_count": int((reference != candidate).sum().item()), "comparison": "exact_integer_or_bool"})
        return result
    ref = reference.to(torch.float64) if not reference.is_complex() else reference.to(torch.complex128)
    cand = candidate.to(torch.float64) if not candidate.is_complex() else candidate.to(torch.complex128)
    ref_finite = torch.isfinite(ref)
    cand_finite = torch.isfinite(cand)
    finite = ref_finite & cand_finite
    result["reference_nonfinite"] = int((~ref_finite).sum().item())
    result["candidate_nonfinite"] = int((~cand_finite).sum().item())
    result["nonfinite_position_mismatch"] = int((ref_finite != cand_finite).sum().item())
    result["allclose"] = bool(torch.allclose(ref, cand, atol=atol, rtol=rtol, equal_nan=equal_nan))
    if finite.any():
        delta = (ref[finite] - cand[finite]).abs()
        denominator = ref[finite].abs().clamp_min(max(atol, torch.finfo(torch.float64).tiny))
        relative = delta / denominator
        tolerance = atol + rtol * ref[finite].abs()
        result.update({
            "finite_elements": int(finite.sum().item()),
            "max_abs": float(delta.max().item()),
            "mean_abs": float(delta.mean().item()),
            "rmse": float(torch.sqrt(torch.mean(delta.square())).item()),
            "max_rel": float(relative.max().item()),
            "mean_rel": float(relative.mean().item()),
            "mismatch_count": int((delta > tolerance).sum().item()),
        })
    else:
        result["finite_elements"] = 0
    return result


def safe_load(path: Path, unsafe_pickle: bool):
    torch = load_torch()
    if unsafe_pickle:
        return torch.load(path, map_location="cpu", weights_only=False)
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except TypeError as exc:
        raise RuntimeError("this PyTorch lacks weights_only loading; upgrade PyTorch or use --unsafe-pickle only for a trusted file") from exc


def compare_files(reference_path: Path, candidate_path: Path, atol: float, rtol: float, equal_nan: bool, unsafe_pickle: bool = False, allow_dtype_mismatch: bool = False) -> dict:
    reference = flatten(safe_load(reference_path, unsafe_pickle))
    candidate = flatten(safe_load(candidate_path, unsafe_pickle))
    keys = sorted(set(reference) | set(candidate))
    per_key = {}
    for key in keys:
        if key not in reference:
            per_key[key] = {"allclose": False, "reason": "missing_in_reference"}
        elif key not in candidate:
            per_key[key] = {"allclose": False, "reason": "missing_in_candidate"}
        else:
            per_key[key] = tensor_metrics(reference[key], candidate[key], atol, rtol, equal_nan, allow_dtype_mismatch)
    return {
        "reference": str(reference_path),
        "candidate": str(candidate_path),
        "atol": atol,
        "rtol": rtol,
        "equal_nan": equal_nan,
        "unsafe_pickle": unsafe_pickle,
        "allow_dtype_mismatch": allow_dtype_mismatch,
        "allclose": bool(per_key) and all(item.get("allclose", False) for item in per_key.values()),
        "reason": None if per_key else "no_tensors_found",
        "reference_tensor_count": len(reference),
        "candidate_tensor_count": len(candidate),
        "keys": per_key,
    }


def self_test() -> None:
    try:
        import torch
    except ImportError:
        print("self-test: SKIP (PyTorch is not installed in this validation runtime)")
        return
    with tempfile.TemporaryDirectory() as directory:
        reference = Path(directory) / "reference.pt"
        candidate = Path(directory) / "candidate.pt"
        torch.save({"x": torch.tensor([1.0, 2.0]), "nested": [torch.tensor([3.0])], "ids": torch.tensor([2**60, 7])}, reference)
        torch.save({"x": torch.tensor([1.0, 2.00001]), "nested": [torch.tensor([3.0])], "ids": torch.tensor([2**60, 7])}, candidate)
        result = compare_files(reference, candidate, 1e-4, 1e-4, False)
        assert result["allclose"]
        assert len(result["keys"]) == 3
        assert result["keys"]["root.ids"]["comparison"] == "exact_integer_or_bool"
        torch.save({"metadata": "no tensors"}, reference)
        torch.save({"metadata": "still no tensors"}, candidate)
        empty = compare_files(reference, candidate, 0.0, 0.0, False)
        assert not empty["allclose"] and empty["reason"] == "no_tensors_found"
    print("self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("reference", nargs="?", type=Path)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--atol", type=float, default=0.0)
    parser.add_argument("--rtol", type=float, default=0.0)
    parser.add_argument("--equal-nan", action="store_true")
    parser.add_argument("--allow-dtype-mismatch", action="store_true", help="Compare values after promotion even when tensor dtypes differ.")
    parser.add_argument("--unsafe-pickle", action="store_true", help="Allow arbitrary pickle loading. Use only for files you fully trust.")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.reference is None or args.candidate is None:
        parser.error("reference and candidate are required unless --self-test is used")
    if args.atol < 0 or args.rtol < 0:
        parser.error("--atol and --rtol must be non-negative")
    result = compare_files(args.reference, args.candidate, args.atol, args.rtol, args.equal_nan, args.unsafe_pickle, args.allow_dtype_mismatch)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, allow_nan=False)
    print()
    return 0 if result["allclose"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
