#!/usr/bin/env python3
"""Extract a kernel handoff contract from a reference or optimization context.

The output is compatible with run_kernel_handoff.py.  It is deliberately
conservative: if a runnable Python oracle or stable dims are missing, it emits a
blocked handoff instead of inventing a benchmark contract.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from inspect_ref import inspect_ref  # noqa: E402


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _dims_from_text(text: str) -> dict[str, int]:
    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"dims must be valid JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise SystemExit("dims must be a JSON object")
    out: dict[str, int] = {}
    for key, value in raw.items():
        if isinstance(value, bool):
            continue
        try:
            out[str(key)] = int(value)
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"dims value for {key!r} must be int-like") from exc
    return out


def _load_dims(args: argparse.Namespace, payload: dict[str, Any] | None = None) -> dict[str, int]:
    if args.dims_file:
        return _dims_from_text(Path(args.dims_file).expanduser().read_text(encoding="utf-8"))
    if args.dims:
        return _dims_from_text(args.dims)
    if payload:
        manifest = payload.get("kernel_handoff_manifest", payload)
        contract = manifest.get("operator_contract", {}) if isinstance(manifest, dict) else {}
        dims = contract.get("dims")
        if isinstance(dims, dict):
            return _dims_from_text(json.dumps(dims))
    return {}


def _ptr_size_hint(dims: dict[str, int]) -> int:
    if {"M", "N", "K"}.issubset(dims):
        return max(dims["M"] * dims["K"], dims["K"] * dims["N"], dims["M"] * dims["N"])
    if {"B", "M", "N"}.issubset(dims):
        return dims["B"] * dims["M"] * dims["N"]
    if "N" in dims:
        return dims["N"]
    positives = [v for v in dims.values() if v > 0]
    return max(positives) if positives else 0


def _resolve(path_text: str, workdir: str = "") -> str:
    path = Path(path_text).expanduser()
    if path.is_absolute():
        return str(path)
    if workdir:
        candidate = (Path(workdir).expanduser() / path).resolve()
        if candidate.exists():
            return str(candidate)
    return str(path.resolve())


def _existing_manifest(payload: dict[str, Any], dims: dict[str, int]) -> dict[str, Any] | None:
    manifest = payload.get("kernel_handoff_manifest", payload)
    if not isinstance(manifest, dict):
        return None
    if "routing" not in manifest or "handoff_targets" not in manifest:
        return None
    if dims:
        manifest = json.loads(json.dumps(manifest))
        contract = manifest.setdefault("operator_contract", {})
        contract.setdefault("dims", dims)
        contract.setdefault("ptr_size_hint", _ptr_size_hint(dims))
        for target_name in ("baseline_generator", "kernel_optimizer"):
            target = (manifest.setdefault("handoff_targets", {}) or {}).setdefault(target_name, {})
            target.setdefault("dims", dims)
            target.setdefault("ptr_size_hint", _ptr_size_hint(dims))
    return manifest


def _pick_ref_from_context(payload: dict[str, Any], workdir: str) -> str:
    manifest = payload.get("kernel_handoff_manifest", payload)
    if isinstance(manifest, dict):
        contract = manifest.get("operator_contract", {}) or {}
        preferred = contract.get("preferred_reference", {}) or {}
        if preferred.get("path"):
            return _resolve(str(preferred["path"]), workdir)
        for item in contract.get("reference_candidates", []) or []:
            if isinstance(item, dict) and item.get("path"):
                return _resolve(str(item["path"]), workdir)
    return ""


def _op_from_analysis(analysis: dict[str, Any]) -> str:
    return str((analysis.get("classification") or {}).get("op_kind") or "unknown")


def _reference_semantic_fields(analysis: dict[str, Any], dims: dict[str, int]) -> dict[str, Any]:
    hint = analysis.get("signature_hint") or {}
    chosen = analysis.get("chosen_reference") or {}
    tensor_args = [str(item) for item in hint.get("tensor_args", []) or []]
    output_args = [str(item) for item in hint.get("output_args", []) or []]
    subscripts = [str(item) for item in chosen.get("subscripts", []) or []]
    calls = " ".join(str(item) for item in chosen.get("calls", []) or [])
    names = " ".join(tensor_args + output_args + subscripts)
    index_like = [name for name in tensor_args if re.search(r"(idx|index|indices|offset|offsets|ids|bucket|rowptr|indptr)", name, re.I)]
    mask_like = [name for name in tensor_args if re.search(r"(mask|valid|predicate)", name, re.I)]
    ragged_like = [name for name in tensor_args if re.search(r"(offset|offsets|rowptr|row_ptr|indptr|lengths?|cu_seqlens|seq_offsets|jagged|ragged)", name, re.I)]
    return {
        "arity": {
            "input_count": len(tensor_args),
            "output_count": len(output_args) if output_args else int(bool(chosen.get("has_return_value"))),
            "multiple_outputs": len(output_args) > 1,
        },
        "dtype": {
            "pointer_dtypes": {},
            "mixed_dtype": "dtype" in names.lower() or "to(" in calls,
            "index_params": index_like,
            "dtype_status": "unknown_from_python_reference",
        },
        "shape": {
            "dims": dims,
            "dynamic_shape_params": [str(item) for item in hint.get("dim_args", []) or []],
            "ptr_size_hint": _ptr_size_hint(dims),
        },
        "layout": {
            "stride_params": [name for name in tensor_args if re.search(r"(stride|ld|pitch)", name, re.I)],
            "has_stride_params": any(re.search(r"(stride|ld|pitch)", name, re.I) for name in tensor_args),
            "contiguous_assumption": not any(re.search(r"(stride|ld|pitch)", name, re.I) for name in tensor_args),
        },
        "mask": {
            "mask_params": mask_like,
            "has_mask": bool(mask_like or re.search(r"(masked_fill|where|mask)", calls, re.I)),
        },
        "ragged_jagged": {
            "metadata_params": ragged_like,
            "has_ragged_metadata": bool(ragged_like),
        },
        "workspace": {
            "workspace_params": [name for name in tensor_args if re.search(r"(workspace|scratch|temp|tmp|buffer|reserve)", name, re.I)],
            "has_workspace": any(re.search(r"(workspace|scratch|temp|tmp|buffer|reserve)", name, re.I) for name in tensor_args),
        },
        "aliasing": {
            "in_place_alias_candidates": output_args,
            "requires_manual_alias_check": bool(output_args),
        },
        "indexing": {
            "index_params": index_like,
            "uses_atomic": False,
            "atomic_ops": [],
        },
    }


def _kernel_kind(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".hip":
        return "hip_source"
    if suffix == ".cu":
        return "cuda_source"
    if suffix in {".cpp", ".cc", ".cxx"}:
        return "cpp_source"
    if suffix == ".py":
        return "python_source"
    return "source"


def _solve_signature_text(text: str) -> str:
    match = re.search(r'extern\s+"C"\s+void\s+solve\s*\(([\s\S]*?)\)\s*\{', text)
    return match.group(1) if match else ""


def _clean_param_token(token: str) -> str:
    token = re.sub(r"/\*.*?\*/", "", token, flags=re.S)
    token = re.sub(r"//[^\n]*", "", token)
    token = re.sub(r"\b__restrict__\b|\b__restrict\b|\brestrict\b", "", token)
    return " ".join(token.split())


def _parse_solve_params(path: str) -> list[dict[str, Any]]:
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    signature = _solve_signature_text(text)
    if not signature:
        return []
    params: list[dict[str, Any]] = []
    for raw in signature.split(","):
        token = _clean_param_token(raw)
        if not token:
            continue
        is_const = bool(re.search(r"\bconst\b", token))
        clean = re.sub(r"\bconst\b", "", token).strip()
        ptr = re.match(
            r"(?P<type>float|double|int|long|short|char|unsigned\s+char|unsigned\s+short|unsigned\s+int)\s*\*\s*(?P<name>[A-Za-z_]\w*)$",
            clean,
        )
        if ptr:
            params.append(
                {
                    "kind": "ptr",
                    "type": " ".join(ptr.group("type").split()),
                    "name": ptr.group("name"),
                    "is_const": is_const,
                    "raw": raw.strip(),
                }
            )
            continue
        scalar = re.match(r"(?P<type>int|long|size_t|unsigned\s+int)\s+(?P<name>[A-Za-z_]\w*)$", clean)
        if scalar:
            params.append(
                {
                    "kind": "scalar",
                    "type": " ".join(scalar.group("type").split()),
                    "name": scalar.group("name"),
                    "is_const": False,
                    "raw": raw.strip(),
                }
            )
            continue
        params.append({"kind": "unknown", "name": "", "raw": raw.strip()})
    return params


def _compact_source(text: str) -> str:
    return re.sub(r"\s+", "", text)


def _dtype_kind(dtype: str) -> str:
    normalized = " ".join(str(dtype).split())
    if normalized in {"float", "double"}:
        return "floating"
    if normalized in {"int", "long", "short", "char", "unsigned char", "unsigned short", "unsigned int"}:
        return "integer"
    return "unknown"


def _semantic_fields(params: list[dict[str, Any]], dims: dict[str, int], text: str = "") -> dict[str, Any]:
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    inputs = [item for item in ptrs if item.get("is_const")]
    outputs = [item for item in ptrs if not item.get("is_const")]
    scalars = [item for item in params if item.get("kind") == "scalar"]
    scalar_names = [str(item.get("name") or "") for item in scalars]
    ptr_dtypes = {str(item.get("name")): str(item.get("type")) for item in ptrs}
    input_dtypes = {str(item.get("name")): str(item.get("type")) for item in inputs}
    output_dtypes = {str(item.get("name")): str(item.get("type")) for item in outputs}
    dtype_set = sorted(set(ptr_dtypes.values()))
    index_params = [
        item for item in inputs
        if _dtype_kind(str(item.get("type"))) == "integer"
        or re.search(r"(idx|index|indices|offset|offsets|ids|bucket|rowptr|indptr)", str(item.get("name")), re.I)
    ]
    data_params = [item for item in ptrs if _dtype_kind(str(item.get("type"))) == "floating"]
    stride_params = [name for name in scalar_names if re.search(r"(stride|ld|pitch)", name, re.I)]
    dynamic_shape_params = [
        name for name in scalar_names
        if name not in stride_params and re.search(r"^(n|m|k|b|h|w|c|d|rows?|cols?|len|length|size|num_|.*_size$)", name, re.I)
    ]
    workspace_params = [
        item for item in ptrs
        if re.search(r"(workspace|scratch|temp|tmp|buffer|reserve)", str(item.get("name")), re.I)
    ]
    mask_params = [
        item for item in ptrs
        if re.search(r"(mask|valid|predicate)", str(item.get("name")), re.I)
    ]
    ragged_params = [
        item for item in ptrs
        if re.search(r"(offset|offsets|rowptr|row_ptr|indptr|lengths?|cu_seqlens|seq_offsets|jagged|ragged)", str(item.get("name")), re.I)
    ]
    compact = _compact_source(text)
    atomic_ops = sorted(set(re.findall(r"\batomic(?:Add|Max|Min|CAS|Exch|Or|And)\b", text)))
    has_mask_expr = bool(re.search(r"\bif\s*\([^)]*(?:mask|valid|predicate)", text, re.I))
    writes_to_input_name = {str(item.get("name")) for item in inputs} & {str(item.get("name")) for item in outputs}
    output_name_tokens = {re.sub(r"^(out|output|dst|y|z)_?", "", str(item.get("name")), flags=re.I) for item in outputs}
    input_name_tokens = {re.sub(r"^(in|input|src|x)_?", "", str(item.get("name")), flags=re.I) for item in inputs}
    alias_candidates = sorted(
        name for name in (output_name_tokens & input_name_tokens)
        if name and name not in {"out", "input", "src", "dst", "x", "y", "z"}
    )
    has_indexed_write = any(re.search(rf"\b{re.escape(str(out.get('name')))}\s*\[[^]]*(idx|index|indices|offset|ids)", compact, re.I) for out in outputs)
    has_indexed_read = any(re.search(rf"\b{re.escape(str(inp.get('name')))}\s*\[[^]]*(idx|index|indices|offset|ids)", compact, re.I) for inp in inputs)
    return {
        "arity": {
            "input_count": len(inputs),
            "output_count": len(outputs),
            "scalar_count": len(scalars),
            "multiple_outputs": len(outputs) > 1,
        },
        "dtype": {
            "pointer_dtypes": ptr_dtypes,
            "input_dtypes": input_dtypes,
            "output_dtypes": output_dtypes,
            "mixed_dtype": len(dtype_set) > 1,
            "floating_params": [str(item.get("name")) for item in data_params],
            "index_params": [str(item.get("name")) for item in index_params],
        },
        "shape": {
            "dims": dims,
            "dynamic_shape_params": dynamic_shape_params,
            "scalar_params": scalar_names,
            "ptr_size_hint": _ptr_size_hint(dims),
        },
        "layout": {
            "stride_params": stride_params,
            "has_stride_params": bool(stride_params),
            "contiguous_assumption": not bool(stride_params),
            "layout_rank_hint": len(dynamic_shape_params) or len(dims),
        },
        "mask": {
            "mask_params": [str(item.get("name")) for item in mask_params],
            "has_mask_expr": has_mask_expr,
            "has_mask": bool(mask_params or has_mask_expr),
        },
        "ragged_jagged": {
            "metadata_params": [str(item.get("name")) for item in ragged_params],
            "has_ragged_metadata": bool(ragged_params),
        },
        "workspace": {
            "workspace_params": [str(item.get("name")) for item in workspace_params],
            "has_workspace": bool(workspace_params),
        },
        "aliasing": {
            "in_place_alias_candidates": alias_candidates,
            "exact_input_output_name_overlap": sorted(writes_to_input_name),
            "requires_manual_alias_check": bool(alias_candidates or writes_to_input_name),
        },
        "indexing": {
            "index_params": [str(item.get("name")) for item in index_params],
            "has_indexed_read": has_indexed_read,
            "has_indexed_write": has_indexed_write,
            "atomic_ops": atomic_ops,
            "uses_atomic": bool(atomic_ops),
        },
    }


def _classify_kernel_contract(path: str, dims: dict[str, int]) -> dict[str, Any]:
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        text = ""
    params = _parse_solve_params(path)
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    inputs = [item for item in ptrs if item.get("is_const")]
    outputs = [item for item in ptrs if not item.get("is_const")]
    scalars = [item for item in params if item.get("kind") == "scalar"]
    scalar_names = {str(item.get("name")) for item in scalars}
    unsupported = [item.get("raw", "") for item in params if item.get("kind") == "unknown"]
    family = "unknown"
    generators: list[str] = []
    compact = _compact_source(text)
    semantics = _semantic_fields(params, dims, text)
    if len(inputs) == 1 and len(outputs) == 1 and "N" in scalar_names:
        out = outputs[0]["name"]
        src = inputs[0]["name"]
        if f"{out}[i]={src}[i]" in compact or f"{out}[idx]={src}[idx]" in compact:
            family = "flat_copy"
            generators = ["flat_copy_float4", "flat_copy_two_per_thread", "flat_elementwise_coarsened"]
        elif f"{out}[i]=" in compact or f"{out}[idx]=" in compact:
            family = "flat_elementwise"
            generators = ["flat_elementwise_coarsened"]
    if len(inputs) >= 2 and len(outputs) == 1 and "N" in scalar_names:
        out = outputs[0]["name"]
        indexed_inputs = [item["name"] for item in inputs if f"{item['name']}[i]" in compact or f"{item['name']}[idx]" in compact]
        if len(indexed_inputs) >= 2 and (f"{out}[i]=" in compact or f"{out}[idx]=" in compact):
            family = "flat_axpy"
            generators = ["flat_axpy_vectorized", "flat_elementwise_coarsened"]
    if len(inputs) >= 2 and len(outputs) == 1 and "N" in scalar_names:
        out = outputs[0]["name"]
        index_inputs = [
            item for item in inputs
            if _dtype_kind(str(item.get("type"))) == "integer"
            or re.search(r"(idx|index|indices|ids)", str(item.get("name")), re.I)
        ]
        data_inputs = [item for item in inputs if _dtype_kind(str(item.get("type"))) == "floating"]
        for index in index_inputs:
            idx = str(index["name"])
            for data in data_inputs:
                src = str(data["name"])
                if re.search(rf"{re.escape(out)}\[(?:i|idx)\]={re.escape(src)}\[{re.escape(idx)}\[(?:i|idx)\]\]", compact):
                    family = "gather"
                    generators = ["gather_coalesced", "gather_coarsened"]
                elif re.search(rf"{re.escape(out)}\[{re.escape(idx)}\[(?:i|idx)\]\]={re.escape(src)}\[(?:i|idx)\]", compact):
                    family = "scatter"
                    generators = ["scatter_coarsened"]
                elif (
                    re.search(rf"atomicAdd\(&?{re.escape(out)}\[{re.escape(idx)}\[(?:i|idx)\]\],?{re.escape(src)}\[(?:i|idx)\]\)", compact)
                    or re.search(rf"{re.escape(out)}\[{re.escape(idx)}\[(?:i|idx)\]\]\+={re.escape(src)}\[(?:i|idx)\]", compact)
                ):
                    family = "index_add"
                    generators = ["index_add_atomic_coarsened"]
    if len(inputs) == 1 and len(outputs) == 1 and "N" in scalar_names:
        src = inputs[0]["name"]
        out = outputs[0]["name"]
        if (f"{src}[i]" in compact and ("sum+=" in compact or "acc+=" in compact)) and (f"{out}[0]=" in compact or f"atomicAdd({out}" in compact):
            family = "flat_reduction_sum"
            generators = ["flat_reduction_block_sum"]
    if family in {"unknown", "flat_elementwise"} and len(inputs) >= 1 and len(outputs) >= 1:
        if "expf(" in compact and ("sum" in compact or "denom" in compact) and len(scalar_names) >= 2:
            family = "softmax"
            generators = ["softmax_row_block"]
        elif ("rsqrtf(" in compact or "sqrtf(" in compact) and ("mean" in compact or "var" in compact or "sumsq" in compact) and len(scalar_names) >= 2:
            family = "layernorm"
            generators = ["layernorm_row_block"]
    if {"M", "N", "K"}.issubset(scalar_names) and len(inputs) >= 2 and len(outputs) >= 1:
        a, b, out = inputs[0]["name"], inputs[1]["name"], outputs[0]["name"]
        if f"{a}[row*K+k]" in compact and f"{b}[k*N+col]" in compact and f"{out}[row*N+col]" in compact:
            family = "matmul"
            generators = ["matmul_tiled_lds"]
    if family == "unknown":
        if {"M", "N", "K"}.issubset(dims):
            family = "matmul_like"
        elif "N" in dims:
            family = "flat_like"
    return {
        "solve_signature": params,
        "inputs": inputs,
        "outputs": outputs,
        "scalars": scalars,
        "unsupported_params": unsupported,
        "semantic_fields": semantics,
        "operator_family": family,
        "supported_generators": generators,
        "signature_status": "present" if params else "missing",
    }


def _contract_from_existing_kernel(args: argparse.Namespace, dims: dict[str, int]) -> dict[str, Any] | None:
    if not args.baseline:
        return None
    baseline = _resolve(args.baseline, args.workdir)
    ref = _resolve(args.ref, args.workdir) if args.ref else ""
    missing: list[str] = []
    if not Path(baseline).is_file():
        missing.append(f"baseline_kernel_file:{baseline}")
    if not ref or not Path(ref).is_file():
        missing.append("python_reference_path")
    if not dims:
        missing.append("dims")

    ready = not missing
    ptr_size = _ptr_size_hint(dims)
    kernel_contract = _classify_kernel_contract(baseline, dims) if Path(baseline).is_file() else {}
    if kernel_contract.get("unsupported_params"):
        missing.append("parseable_solve_signature")
        ready = False
    op_kind = args.candidate_op or str(kernel_contract.get("operator_family") or "") or ("matmul" if {"M", "N", "K"}.issubset(dims) else "elementwise" if "N" in dims else "unknown")
    baseline_candidate = {
        "path": baseline,
        "exists": Path(baseline).is_file(),
        "kind": _kernel_kind(baseline),
        "scope": "baseline_kernel",
        "axis": "kernel",
        "placement": "op-site",
        "reason": "provided to extract_contract.py --baseline",
    }
    ref_candidate = {
        "path": ref,
        "exists": bool(ref and Path(ref).is_file()),
        "kind": "python_source",
        "scope": "reference",
        "axis": "kernel",
        "placement": "op-site",
        "reason": "provided to extract_contract.py --ref",
    }
    return {
        "manifest_version": "1.0",
        "source": {
            "analysis_kind": "contract_extractor_existing_kernel",
            "framework": "python,hip",
            "workdir": str(Path(args.workdir).expanduser().resolve()) if args.workdir else os.getcwd(),
        },
        "routing": {
            "recommended_route": "kernel_optimization" if ready else "blocked",
            "route_reason": "baseline kernel, Python reference, and dims are present" if ready else "existing-kernel handoff is incomplete",
            "route_action": "run kernel optimizer directly" if ready else "fix missing fields first",
            "primary_axis": "kernel",
            "handoff_decision": "ready_for_kernel_optimizer" if ready else "blocked",
            "handoff_ready": ready,
            "route_allows_kernel": ready,
        },
        "hotspot": {
            "operator_family": op_kind,
            "candidate_op": args.candidate_op or op_kind,
            "candidate_scope": args.candidate_scope or "baseline_kernel",
            "top_kernels": [],
        },
        "operator_contract": {
            "reference_status": "present" if ref_candidate["exists"] else "missing",
            "preferred_reference": ref_candidate,
            "reference_candidates": [ref_candidate] if ref else [],
            "baseline_status": "present" if baseline_candidate["exists"] else "missing",
            "preferred_baseline": baseline_candidate,
            "dims_status": "present" if dims else "missing",
            "dims_source": "extract_contract.py",
            "dims": dims,
            "ptr_size_hint": ptr_size,
            "kernel_signature": kernel_contract.get("solve_signature", []),
            "kernel_inputs": kernel_contract.get("inputs", []),
            "kernel_outputs": kernel_contract.get("outputs", []),
            "kernel_scalars": kernel_contract.get("scalars", []),
            "semantic_fields": kernel_contract.get("semantic_fields", {}),
            "supported_generators": kernel_contract.get("supported_generators", []),
            "dtype_layout_notes": [
                "Existing baseline mode does not prove dtype/layout semantics; benchmark.py correctness remains the contract gate."
            ],
            "contract_notes": kernel_contract.get("unsupported_params", []),
        },
        "handoff_targets": {
            "baseline_generator": {
                "ready": False,
                "missing_fields": ["not_needed_existing_baseline"] if ready else missing,
                "preferred_reference_path": ref,
                "preferred_reference_kind": "python_source",
                "dims": dims,
                "ptr_size_hint": ptr_size,
            },
            "kernel_optimizer": {
                "ready": ready,
                "missing_fields": missing,
                "baseline_kernel_path": baseline,
                "python_reference_path": ref,
                "dims": dims,
                "ptr_size_hint": ptr_size,
            },
        },
        "evidence": {
            "summary": {
                "classification": "existing-kernel-contract",
                "reason": "contract extracted from provided baseline kernel, Python reference, and explicit dims",
                "top_kernel_name": Path(baseline).name,
                "top_kernel_share_pct": 0.0,
            }
        },
        "next_actions": [
            {
                "priority": "P0",
                "condition": "optimizer_ready" if ready else "contract_incomplete",
                "action": "run run_kernel_handoff.py --manifest <this-file> --auto-loop" if ready else "provide --baseline, --ref, and --dims",
                "reason": "optimizer direct path requires a baseline kernel, a Python oracle, and dims",
            }
        ],
    }


def _contract_from_reference(args: argparse.Namespace, dims: dict[str, int]) -> dict[str, Any]:
    if not args.ref:
        return _blocked_manifest("missing_reference", "pass --ref or provide an optimization_context with a reference candidate", dims)
    ref = _resolve(args.ref, args.workdir)
    if not Path(ref).is_file():
        return _blocked_manifest("missing_reference", f"reference file not found: {ref}", dims)
    if not dims:
        return _blocked_manifest("missing_dims", "pass --dims or --dims-file; dims are required for benchmarkable kernel handoff", dims)

    analysis = inspect_ref(ref, dims)
    op_kind = _op_from_analysis(analysis)
    unsupported = list(analysis.get("unsupported_assumptions") or [])
    ready = not unsupported and bool((analysis.get("signature_hint") or {}).get("tensor_args"))
    ptr_size = _ptr_size_hint(dims)
    candidate = {
        "path": ref,
        "exists": True,
        "kind": "python_source",
        "scope": "reference",
        "axis": "kernel",
        "placement": "op-site",
        "reason": "extracted by extract_contract.py",
        "target_line": int((analysis.get("chosen_reference") or {}).get("lineno") or 0),
    }
    missing = []
    if not ready:
        missing.extend(unsupported or ["reference oracle is not strong enough"])
    return {
        "manifest_version": "1.0",
        "source": {
            "analysis_kind": "contract_extractor",
            "framework": ",".join((analysis.get("classification") or {}).get("frameworks") or ["python"]),
            "workdir": str(Path(args.workdir).expanduser().resolve()) if args.workdir else os.getcwd(),
        },
        "routing": {
            "recommended_route": "kernel_optimization" if ready else "blocked",
            "route_reason": "reference and dims are present" if ready else "kernel handoff contract is incomplete",
            "route_action": "run kernel-hip-baseline then kernel optimizer" if ready else "fix missing fields first",
            "primary_axis": "kernel",
            "handoff_decision": "ready_for_baseline_generator" if ready else "blocked",
            "handoff_ready": ready,
            "route_allows_kernel": ready,
        },
        "hotspot": {
            "operator_family": op_kind,
            "candidate_op": args.candidate_op or op_kind,
            "candidate_scope": args.candidate_scope or "reference",
            "top_kernels": [],
        },
        "operator_contract": {
            "reference_status": "present",
            "preferred_reference": candidate,
            "reference_candidates": [candidate],
            "dims_status": "present",
            "dims_source": "extract_contract.py",
            "dims": dims,
            "ptr_size_hint": ptr_size,
            "semantic_fields": _reference_semantic_fields(analysis, dims),
            "dtype_layout_notes": [
                "Extractor does not prove dtype/layout/mask semantics; baseline generation must preserve these in baseline_manifest.json."
            ],
            "contract_notes": unsupported,
        },
        "handoff_targets": {
            "baseline_generator": {
                "ready": ready,
                "missing_fields": missing,
                "preferred_reference_path": ref,
                "preferred_reference_kind": "python_source",
                "dims": dims,
                "ptr_size_hint": ptr_size,
            },
            "kernel_optimizer": {
                "ready": False,
                "missing_fields": ["baseline_kernel_file"],
                "baseline_kernel_path": "",
                "python_reference_path": ref,
                "dims": dims,
                "ptr_size_hint": ptr_size,
            },
        },
        "evidence": {
            "summary": {
                "classification": "kernel-contract",
                "reason": "contract extracted from reference source and explicit dims",
                "top_kernel_name": "",
                "top_kernel_share_pct": 0.0,
            }
        },
        "next_actions": [
            {
                "priority": "P0",
                "condition": "baseline_ready" if ready else "contract_incomplete",
                "action": "run run_kernel_handoff.py --manifest <this-file> --auto-loop" if ready else "provide a stronger reference(...) and dims",
                "reason": "baseline-generator requires a stable Python oracle and dims",
            }
        ],
    }


def _blocked_manifest(status: str, reason: str, dims: dict[str, int]) -> dict[str, Any]:
    return {
        "manifest_version": "1.0",
        "source": {"analysis_kind": "contract_extractor"},
        "routing": {
            "recommended_route": "blocked",
            "route_reason": reason,
            "route_action": "complete the kernel handoff contract",
            "primary_axis": "kernel",
            "handoff_decision": status,
            "handoff_ready": False,
            "route_allows_kernel": False,
        },
        "hotspot": {"operator_family": "unknown", "candidate_op": "", "top_kernels": []},
        "operator_contract": {"reference_status": "missing", "dims_status": "present" if dims else "missing", "dims": dims},
        "handoff_targets": {
            "baseline_generator": {"ready": False, "missing_fields": [status], "dims": dims, "ptr_size_hint": _ptr_size_hint(dims)},
            "kernel_optimizer": {"ready": False, "missing_fields": ["baseline_kernel_file", status], "dims": dims, "ptr_size_hint": _ptr_size_hint(dims)},
        },
        "next_actions": [{"priority": "P0", "action": reason}],
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    payload = _read_json(Path(args.context).expanduser()) if args.context else {}
    dims = _load_dims(args, payload)
    if payload:
        existing = _existing_manifest(payload, dims)
        if existing and not args.force_reextract:
            return existing
        if not args.ref:
            args.ref = _pick_ref_from_context(payload, args.workdir)
    existing_kernel = _contract_from_existing_kernel(args, dims)
    if existing_kernel is not None:
        return existing_kernel
    return _contract_from_reference(args, dims)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a kernel handoff manifest from a reference or optimization context")
    parser.add_argument("--context", default="", help="optimization_context.json or existing kernel_handoff_manifest.json")
    parser.add_argument("--ref", default="", help="Python reference file exposing reference/torch_ref/golden/ref/oracle/gold")
    parser.add_argument("--baseline", default="", help="Existing HIP/CUDA/C++ kernel exposing solve(...); skips baseline generation when valid")
    parser.add_argument("--dims", default="", help="JSON dims, for example '{\"M\":1024,\"N\":1024,\"K\":1024}'")
    parser.add_argument("--dims-file", default="")
    parser.add_argument("--workdir", default="")
    parser.add_argument("--candidate-op", default="")
    parser.add_argument("--candidate-scope", default="")
    parser.add_argument("--force-reextract", action="store_true")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    manifest = run(args)
    text = json.dumps(manifest, ensure_ascii=False, indent=2)
    print(text)
    if args.out:
        _write_json(Path(args.out).expanduser(), manifest)


if __name__ == "__main__":
    main()
