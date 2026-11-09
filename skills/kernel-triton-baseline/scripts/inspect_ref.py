#!/usr/bin/env python3
"""Inspect a Python/Torch/Triton reference before Triton baseline generation."""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
from pathlib import Path
from typing import Any


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _name(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    if isinstance(node, ast.Call):
        return _name(node.func)
    return ""


class Inspector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.calls: list[str] = []
        self.copy_targets: list[str] = []
        self.returns = False

    def visit_Call(self, node: ast.Call) -> Any:
        name = _name(node.func)
        if name:
            self.calls.append(name)
        if name.endswith(".copy_") and isinstance(node.func, ast.Attribute):
            target = _name(node.func.value)
            if target:
                self.copy_targets.append(target)
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> Any:
        self.returns = node.value is not None
        self.generic_visit(node)


def _function_info(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> dict:
    insp = Inspector()
    insp.visit(fn)
    decorators = [_name(d) for d in fn.decorator_list]
    return {
        "name": fn.name,
        "lineno": fn.lineno,
        "args": [a.arg for a in fn.args.args],
        "decorators": [d for d in decorators if d],
        "is_triton_kernel": any("triton.jit" in d or d == "jit" for d in decorators),
        "calls": sorted(set(insp.calls)),
        "copy_targets": sorted(set(insp.copy_targets)),
        "has_return_value": insp.returns,
    }


def inspect(ref: str, dims: dict) -> dict:
    suffix = Path(ref).suffix.lower()
    if suffix in {".cu", ".cuh", ".cc", ".cpp", ".cxx", ".hip"}:
        return inspect_native_kernel(ref, dims)

    source = Path(ref).read_text(encoding="utf-8", errors="ignore")
    tree = ast.parse(source, filename=ref)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module)
    functions = [_function_info(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    plain = [f for f in functions if not f["is_triton_kernel"]]
    chosen = next((f for f in plain if f["name"] in {"reference", "torch_ref", "golden", "ref", "forward"}), plain[0] if plain else None)
    call_text = " ".join(" ".join(f["calls"]) for f in functions).lower()
    dim_keys = {k.upper() for k in dims}
    op_kind = "matmul" if {"M", "N", "K"}.issubset(dim_keys) or "matmul" in call_text or "tl.dot" in call_text else "reduction" if "sum" in call_text else "elementwise" if "N" in dim_keys else "unknown"
    tensor_args = []
    output_args = []
    if chosen:
        output_args = list(chosen.get("copy_targets", []))
        tensor_args = [a for a in chosen["args"] if a not in dims]
    return {
        "ref_file": os.path.abspath(ref),
        "dims": dims,
        "imports": sorted(set(imports)),
        "functions": functions,
        "chosen_reference": chosen,
        "classification": {"op_kind": op_kind, "frameworks": sorted({x.split(".")[0] for x in imports})},
        "signature_hint": {"tensor_args": tensor_args, "output_args": output_args, "dim_args": list(dims), "return_style": "inplace" if output_args else "returns_tensor"},
        "unsupported_assumptions": [] if chosen else ["no plain Python reference candidate found"],
    }


def _clean_cuda_arg(arg: str) -> dict:
    text = " ".join(arg.strip().split())
    name_match = re.search(r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:\[[^\]]*\])?$", text)
    name = name_match.group(1) if name_match else text
    is_pointer = "*" in text or "[" in text
    is_const = bool(re.search(r"\bconst\b", text))
    dtype = "float32" if re.search(r"\bfloat\b", text) else "int32" if re.search(r"\bint\b", text) else "unknown"
    return {"raw": text, "name": name, "is_pointer": is_pointer, "is_const": is_const, "dtype": dtype}


def _infer_cuda_op(body: str, output: str, inputs: list[str]) -> str:
    body_compact = re.sub(r"\s+", "", body.lower())
    if re.search(rf"atomicadd\s*\(\s*{re.escape(output)}\b", body, re.IGNORECASE):
        return "reduction"
    if "atomicadd" in body_compact and len(inputs) <= 1:
        return "reduction"
    if len(inputs) == 1 and re.search(r"\bfor\b", body, re.IGNORECASE) and "+=" in body:
        return "reduction"
    assign_re = re.compile(rf"{re.escape(output)}\s*\[[^\]]+\]\s*=\s*([^;]+);")
    match = assign_re.search(body)
    rhs = match.group(1) if match else body
    if len(inputs) >= 2:
        a, b = re.escape(inputs[0]), re.escape(inputs[1])
        if re.search(rf"{a}\s*\[[^\]]+\]\s*\+\s*{b}\s*\[[^\]]+\]", rhs):
            return "elementwise_add"
        if re.search(rf"{a}\s*\[[^\]]+\]\s*\*\s*{b}\s*\[[^\]]+\]", rhs):
            return "elementwise_mul"
    if inputs and re.search(rf"{re.escape(inputs[0])}\s*\[[^\]]+\]", rhs):
        return "elementwise_copy"
    return "elementwise_unknown"


def inspect_native_kernel(ref: str, dims: dict) -> dict:
    source = Path(ref).read_text(encoding="utf-8", errors="ignore")
    language = "hipc" if Path(ref).suffix.lower() == ".hip" else "cuda"
    kernel_match = re.search(
        r"__global__\s+void\s+([A-Za-z_][A-Za-z0-9_]*)\s*\((.*?)\)\s*\{",
        source,
        re.DOTALL,
    )
    unsupported: list[str] = []
    if not kernel_match:
        unsupported.append("no __global__ void kernel signature found")
        kernel_name = "kernel"
        args: list[dict] = []
        body = source
    else:
        kernel_name = kernel_match.group(1)
        args = [_clean_cuda_arg(part) for part in kernel_match.group(2).split(",") if part.strip()]
        # Extract body using brace counting (greedy regex is unreliable)
        brace_start = kernel_match.end() - 1  # position of the opening {
        depth = 0
        body_end = brace_start
        for i in range(brace_start, len(source)):
            if source[i] == "{":
                depth += 1
            elif source[i] == "}":
                depth -= 1
                if depth == 0:
                    body_end = i
                    break
        body = source[brace_start + 1:body_end]

    pointer_args = [a for a in args if a.get("is_pointer")]
    output_args = [a["name"] for a in pointer_args if not a.get("is_const") or a["name"].lower() in {"out", "output", "c"}]
    if not output_args and pointer_args:
        output_args = [pointer_args[-1]["name"]]
    output = output_args[0] if output_args else "out"
    tensor_args = [a["name"] for a in pointer_args if a["name"] != output]
    dim_args = [k for k in dims]
    if not tensor_args:
        unsupported.append("no input pointer args inferred")

    dim_keys = {k.upper() for k in dims}
    if {"M", "N", "K"}.issubset(dim_keys):
        op_kind = "matmul"
    else:
        op_kind = _infer_cuda_op(body, output, tensor_args)
        if op_kind == "elementwise_unknown":
            unsupported.append(
                f"unsupported {language.upper()} RHS expression; generated baseline may need manual ref/kernel edits"
            )
    chosen = {
        "name": kernel_name,
        "lineno": 1,
        "args": [a["name"] for a in args],
        "decorators": ["__global__"],
        "is_triton_kernel": False,
        "language": language,
        "calls": [],
        "copy_targets": output_args,
        "has_return_value": False,
    }
    return {
        "ref_file": os.path.abspath(ref),
        "dims": dims,
        "imports": [],
        "functions": [chosen],
        "chosen_reference": chosen,
        "classification": {"op_kind": op_kind, "frameworks": [language]},
        "signature_hint": {
            "tensor_args": tensor_args,
            "output_args": output_args,
            "dim_args": dim_args,
            "return_style": "inplace",
            "cuda_args": args,
        },
        "unsupported_assumptions": unsupported,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", required=True)
    parser.add_argument("--dims", default="")
    parser.add_argument("--dims-file", default="")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    if args.dims_file:
        dims = json.loads(Path(args.dims_file).read_text(encoding="utf-8"))
    elif args.dims:
        dims = json.loads(args.dims)
    else:
        raise SystemExit("provide --dims JSON or --dims-file")
    result = inspect(args.ref, dims)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
