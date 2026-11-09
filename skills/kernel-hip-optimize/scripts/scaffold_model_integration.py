#!/usr/bin/env python3
"""Scaffold a model-local PyTorch extension wrapper for a selected HIP kernel.

The scaffold is intentionally opt-in.  It creates files that can be imported by
the project and guarded by an environment variable; it does not patch model
source automatically.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _find_best_kernel(run_dir: Path) -> Path:
    state = _read_json(run_dir / "state.json")
    best = Path(str(state.get("best_file") or "")).expanduser()
    if best.is_file():
        return best
    for ext in (".hip", ".cpp", ".cc", ".cxx", ".cu"):
        for path in run_dir.glob(f"iterv*/kernel{ext}"):
            if path.is_file():
                return path
    raise SystemExit(f"no HIP/C++ kernel found under {run_dir}")


def _solve_signature_text(text: str) -> str:
    match = re.search(r'extern\s+"C"\s+void\s+solve\s*\(([\s\S]*?)\)\s*\{', text)
    return match.group(1) if match else ""


def _parse_solve_params(text: str) -> list[dict[str, Any]]:
    signature = _solve_signature_text(text)
    params: list[dict[str, Any]] = []
    if not signature:
        return params
    for raw in signature.split(","):
        token = " ".join(re.sub(r"\b__restrict__\b|\brestrict\b|\b__restrict\b", "", raw).split())
        if not token:
            continue
        is_const = bool(re.search(r"\bconst\b", token))
        clean = re.sub(r"\bconst\b", "", token).strip()
        ptr = re.match(r"(?P<type>float|double)\s*\*\s*(?P<name>[A-Za-z_]\w*)$", clean)
        if ptr:
            params.append({"kind": "ptr", "type": ptr.group("type"), "name": ptr.group("name"), "is_const": is_const, "raw": raw.strip()})
            continue
        scalar = re.match(r"(?P<type>int|long|size_t|unsigned\s+int)\s+(?P<name>[A-Za-z_]\w*)$", clean)
        if scalar:
            params.append({"kind": "scalar", "type": scalar.group("type"), "name": scalar.group("name"), "is_const": False, "raw": raw.strip()})
            continue
        params.append({"kind": "unknown", "name": "", "raw": raw.strip()})
    return params


def _detect_wrapper_contract(kernel: Path, state: dict[str, Any]) -> dict[str, Any]:
    text = kernel.read_text(encoding="utf-8", errors="ignore")
    params = _parse_solve_params(text)
    dims = state.get("dims", {}) or {}
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = [item for item in params if item.get("kind") == "scalar"]
    if params and not any(item.get("kind") == "unknown" for item in params):
        if len(const_ptrs) == 1 and len(out_ptrs) == 1 and any(item.get("name") == "N" for item in scalars):
            return {"kind": "flat_unary", "params": params, "dims": dims}
        if len(const_ptrs) == 2 and len(out_ptrs) == 1 and {"M", "N", "K"}.issubset({item.get("name") for item in scalars}):
            return {"kind": "matmul", "params": params, "dims": dims}
    return {"kind": "manual", "params": params, "dims": dims}


def _dtype_cpp(dtype: str) -> str:
    return "double" if dtype == "double" else "float"


def _flat_unary_cpp(ext_name: str, contract: dict[str, Any]) -> str:
    params = contract["params"]
    input_ptr = next(item for item in params if item.get("kind") == "ptr" and item.get("is_const"))
    out_ptr = next(item for item in params if item.get("kind") == "ptr" and not item.get("is_const"))
    dtype = _dtype_cpp(str(input_ptr.get("type") or "float"))
    solve_decl = ", ".join(item["raw"] for item in params)
    return f'''#include <torch/extension.h>
#include <limits>

extern "C" void solve({solve_decl});

torch::Tensor forward(torch::Tensor input) {{
    TORCH_CHECK(input.is_cuda(), "input must be on HCU/CUDA device");
    TORCH_CHECK(input.is_contiguous(), "input must be contiguous");
    TORCH_CHECK(input.scalar_type() == torch::kFloat32, "generated wrapper currently expects float32");
    auto out = torch::empty_like(input);
    int64_t numel64 = input.numel();
    TORCH_CHECK(numel64 <= std::numeric_limits<int>::max(), "N exceeds int range");
    solve(
        input.data_ptr<{dtype}>(),
        out.data_ptr<{dtype}>(),
        static_cast<int>(numel64)
    );
    return out;
}}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {{
    m.def("forward", &forward, "{ext_name} flat unary forward");
}}
'''


def _matmul_cpp(ext_name: str, contract: dict[str, Any]) -> str:
    params = contract["params"]
    const_ptrs = [item for item in params if item.get("kind") == "ptr" and item.get("is_const")]
    out_ptr = next(item for item in params if item.get("kind") == "ptr" and not item.get("is_const"))
    dtype = _dtype_cpp(str(out_ptr.get("type") or "float"))
    solve_decl = ", ".join(item["raw"] for item in params)
    return f'''#include <torch/extension.h>
#include <limits>

extern "C" void solve({solve_decl});

torch::Tensor forward(torch::Tensor a, torch::Tensor b) {{
    TORCH_CHECK(a.is_cuda() && b.is_cuda(), "inputs must be on HCU/CUDA device");
    TORCH_CHECK(a.dim() == 2 && b.dim() == 2, "generated wrapper expects 2D matrices");
    TORCH_CHECK(a.size(1) == b.size(0), "matmul K dimension mismatch");
    TORCH_CHECK(a.scalar_type() == torch::kFloat32 && b.scalar_type() == torch::kFloat32, "generated wrapper currently expects float32");
    auto a_contig = a.contiguous();
    auto b_contig = b.contiguous();
    int64_t m64 = a_contig.size(0);
    int64_t k64 = a_contig.size(1);
    int64_t n64 = b_contig.size(1);
    TORCH_CHECK(m64 <= std::numeric_limits<int>::max() && n64 <= std::numeric_limits<int>::max() && k64 <= std::numeric_limits<int>::max(), "dims exceed int range");
    auto out = torch::empty({{m64, n64}}, a_contig.options());
    solve(
        a_contig.data_ptr<{dtype}>(),
        b_contig.data_ptr<{dtype}>(),
        out.data_ptr<{dtype}>(),
        static_cast<int>(m64),
        static_cast<int>(n64),
        static_cast<int>(k64)
    );
    return out;
}}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {{
    m.def("forward", &forward, "{ext_name} matmul forward");
}}
'''


def _manual_cpp_source(ext_name: str, kernel_basename: str) -> str:
    return f'''#include <torch/extension.h>

// Generated integration scaffold.  The raw HIP source is copied next to this
// file as {kernel_basename}.  Fill in argument marshalling for the exact model
// contract before enabling in production.

torch::Tensor forward(torch::Tensor input) {{
    TORCH_CHECK(input.is_cuda(), "input must be on HCU/CUDA device");
    return input;
}}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {{
    m.def("forward", &forward, "{ext_name} forward scaffold");
}}
'''


def _cpp_source(ext_name: str, kernel_basename: str, contract: dict[str, Any]) -> str:
    if contract.get("kind") == "flat_unary":
        return _flat_unary_cpp(ext_name, contract)
    if contract.get("kind") == "matmul":
        return _matmul_cpp(ext_name, contract)
    return _manual_cpp_source(ext_name, kernel_basename)


def _python_wrapper(ext_name: str, env_var: str) -> str:
    return f'''from __future__ import annotations

import os
from pathlib import Path

import torch
from torch.utils.cpp_extension import load


_MODULE = None


def enabled() -> bool:
    return os.environ.get("{env_var}", "0").lower() in {{"1", "true", "yes", "on"}}


def _load_module():
    global _MODULE
    if _MODULE is not None:
        return _MODULE
    root = Path(__file__).resolve().parent
    _MODULE = load(
        name="{ext_name}",
        sources=[str(root / "{ext_name}.cpp"), str(root / "kernel.hip")],
        extra_cflags=["-O3"],
        extra_cuda_cflags=["-O3"],
        verbose=bool(int(os.environ.get("{env_var}_VERBOSE", "0"))),
    )
    return _MODULE


def forward_or_fallback(fallback_fn, *args, **kwargs):
    if not enabled():
        return fallback_fn(*args, **kwargs)
    module = _load_module()
    try:
        return module.forward(*args, **kwargs)
    except Exception:
        if os.environ.get("{env_var}_STRICT", "0") == "1":
            raise
        return fallback_fn(*args, **kwargs)
'''


def _integration_readme(ext_name: str, env_var: str, contract: dict[str, Any]) -> str:
    kind = contract.get("kind", "manual")
    if kind == "flat_unary":
        call = "optimized = wrapper.forward_or_fallback(lambda x: fallback_fn(x), x)"
    elif kind == "matmul":
        call = "optimized = wrapper.forward_or_fallback(lambda a, b: fallback_fn(a, b), a, b)"
    else:
        call = "optimized = wrapper.forward_or_fallback(fallback_fn, *args, **kwargs)"
    return f"""# Model Integration Scaffold

Extension: `{ext_name}`

Detected wrapper contract: `{kind}`

Use an environment variable gate at the model callsite:

```python
from . import wrapper

{call}
```

Validation mode:

```bash
{env_var}=1 {env_var}_STRICT=1 python <your_correctness_test.py>
```

Benchmark mode:

```bash
{env_var}=1 python <your_benchmark.py>
```

If contract is `manual`, fill `{ext_name}.cpp` argument marshalling before enabling.
"""


def _smoke_py(ext_name: str, env_var: str, contract: dict[str, Any]) -> str:
    kind = contract.get("kind", "manual")
    if kind == "flat_unary":
        body = """    x = torch.randn(1024, device="cuda")
    y = wrapper.forward_or_fallback(lambda t: t, x)
    torch.cuda.synchronize()
    print({"shape": tuple(y.shape), "dtype": str(y.dtype), "device": str(y.device)})
"""
    elif kind == "matmul":
        body = """    a = torch.randn(32, 64, device="cuda")
    b = torch.randn(64, 16, device="cuda")
    y = wrapper.forward_or_fallback(lambda x, z: x @ z, a, b)
    torch.cuda.synchronize()
    print({"shape": tuple(y.shape), "dtype": str(y.dtype), "device": str(y.device)})
"""
    else:
        body = """    print("manual contract: fill C++ argument marshalling before smoke test")
"""
    return f'''from __future__ import annotations

import os

import torch

import wrapper


def main():
    os.environ.setdefault("{env_var}", "1")
{body}


if __name__ == "__main__":
    main()
'''


def run(args: argparse.Namespace) -> dict[str, Any]:
    run_dir = Path(args.run_dir).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    kernel = Path(args.kernel).expanduser().resolve() if args.kernel else _find_best_kernel(run_dir)
    if not kernel.is_file():
        raise SystemExit(f"kernel not found: {kernel}")
    state = _read_json(run_dir / "state.json") if (run_dir / "state.json").is_file() else {}
    contract = _detect_wrapper_contract(kernel, state)
    ext_name = args.name
    env_var = args.env_var

    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(kernel, out_dir / "kernel.hip")
    _write(out_dir / f"{ext_name}.cpp", _cpp_source(ext_name, "kernel.hip", contract))
    _write(out_dir / "wrapper.py", _python_wrapper(ext_name, env_var))
    _write(out_dir / "README.integration.md", _integration_readme(ext_name, env_var, contract))
    _write(out_dir / "smoke_integration.py", _smoke_py(ext_name, env_var, contract))
    manifest = {
        "run_dir": str(run_dir),
        "kernel": str(kernel),
        "out_dir": str(out_dir),
        "extension_name": ext_name,
        "env_var": env_var,
        "detected_contract": contract,
        "files": {
            "kernel": str(out_dir / "kernel.hip"),
            "cpp": str(out_dir / f"{ext_name}.cpp"),
            "wrapper": str(out_dir / "wrapper.py"),
            "readme": str(out_dir / "README.integration.md"),
            "smoke": str(out_dir / "smoke_integration.py"),
        },
        "status": "wrapper_generated" if contract.get("kind") in {"flat_unary", "matmul"} else "scaffold_only",
        "next_steps": [
            "Run smoke_integration.py in the target DTK/PyTorch container.",
            f"Import wrapper.forward_or_fallback(...) at the model callsite and guard with {env_var}=1.",
            f"Use {env_var}_STRICT=1 during validation to fail fast instead of falling back.",
        ],
    }
    _write(out_dir / "integration_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a PyTorch extension integration scaffold for a selected HIP kernel")
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--kernel", default="")
    parser.add_argument("--name", default="hygon_custom_op")
    parser.add_argument("--env-var", default="HYGON_CUSTOM_OP")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
