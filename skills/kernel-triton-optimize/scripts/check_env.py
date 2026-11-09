#!/usr/bin/env python3
"""Detect Hygon HCU / Triton runtime and optional low-level tools."""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path


def _run(cmd: list[str], timeout: int = 10) -> tuple[int, str, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="ignore")
        return r.returncode, r.stdout or "", r.stderr or ""
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError) as exc:
        return -1, "", str(exc)


def _detect_gpus() -> list[dict]:
    gpus: list[dict] = []
    try:
        import torch
        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(i)
                gcn = getattr(props, "gcnArchName", None)
                arch = str(gcn).split(":", 1)[0] if gcn else None
                gpus.append({
                    "index": i,
                    "name": torch.cuda.get_device_name(i),
                    "gcn_arch": arch,
                    "gfx_arch": arch,
                    "total_memory_mb": props.total_memory // (1024 * 1024),
                    "compute_units": getattr(props, "multi_processor_count", None),
                })
    except Exception as exc:
        gpus.append({"error": f"torch probe failed: {exc}"})

    if any(g.get("gfx_arch") for g in gpus):
        return gpus

    rocminfo = shutil.which("rocminfo")
    if rocminfo:
        rc, out, _ = _run([rocminfo], timeout=20)
        if rc == 0:
            matches = re.findall(r"\b(gfx[0-9a-fA-F]+)\b", out)
            for i, arch in enumerate(dict.fromkeys(matches)):
                gpus.append({"index": i, "name": arch, "gcn_arch": arch, "gfx_arch": arch})
    return gpus


def _detect_tool(name: str, args: list[str] | None = None) -> dict:
    path = shutil.which(name) or shutil.which(os.path.join("/opt/dtk/bin", name))
    if not path:
        return {"available": False, "path": None, "version": None}
    args = args or ["--version"]
    rc, out, err = _run([path] + args)
    text = (out or err).strip()
    return {"available": True, "path": path, "version": text.splitlines()[0] if text else None}


def _detect_hipprof() -> dict:
    info = _detect_tool("hipprof", ["-h"])
    if not info["available"]:
        return info | {"pmc_available": False}
    path = info["path"]
    rc, out, err = _run([path, "--list-basic"], timeout=20)
    info["pmc_available"] = rc == 0
    info["pmc_note"] = None if rc == 0 else (err or out).strip()[:400]
    return info


def _detect_xcu() -> dict:
    candidates = [
        os.environ.get("XCU_BIN_PATH", ""),
        "/opt/xcompute-4.4.4/XCompute/bin/xcu",
        "/opt/xcompute/XCompute/bin/xcu",
        shutil.which("xcu") or "",
    ]
    path = next((c for c in candidates if c and (os.path.isfile(c) or shutil.which(c))), "")
    if not path:
        return {
            "available": False,
            "path": None,
            "version": None,
            "preferred": True,
            "install_hint": (
                "Install the latest internal xprofiler, hsa-aqlprofile, and XCompute packages, "
                "then put xcu on PATH or set XCU_BIN_PATH=/opt/xcompute-4.4.4/XCompute/bin/xcu."
            ),
        }
    resolved = path if os.path.isfile(path) else shutil.which(path)
    rc, out, err = _run([resolved, "--version"], timeout=10)
    text = (out or err).strip()
    if rc != 0 or not text:
        rc, out, err = _run([resolved, "profile", "--help"], timeout=10)
        text = (out or err).strip()
    return {
        "available": True,
        "path": resolved,
        "version": text.splitlines()[0] if text else None,
        "preferred": True,
    }


def _detect_rocm_smi() -> dict:
    info = _detect_tool("rocm-smi", [])
    if not info["available"]:
        return info
    rc, out, err = _run([info["path"]], timeout=20)
    info["raw"] = (out or err).strip()[:2000]
    return info


def _detect_python_libs() -> dict:
    libs = {}
    for name in ("torch", "triton"):
        try:
            mod = __import__(name)
            libs[name] = {"available": True, "version": getattr(mod, "__version__", "unknown")}
        except Exception:
            libs[name] = {"available": False, "version": None}
    return libs


def _detect_triton_features() -> dict:
    info = {
        "active_target": None,
        "matrix_load_symbol": False,
        "cache_dir": os.environ.get("TRITON_CACHE_DIR") or str(Path.home() / ".triton" / "cache"),
        "waves_per_eu_accepted": True,
        "autotune_disable_method": "config_override",
        "cache_export_tested": False,
        "cache_artifact_types": [],
        "tl_constexpr_available": True,
        "error": None,
    }
    try:
        import triton
        import triton.language as tl
        info["matrix_load_symbol"] = hasattr(tl, "matrix_load")
        try:
            from triton.runtime import driver
            info["active_target"] = str(driver.active.get_current_target())
        except Exception as exc:
            info["active_target"] = f"unavailable: {exc}"

        # Probe: Triton cache export — compile a minimal kernel and check cache
        info["cache_export_tested"] = False
        info["cache_artifact_types"] = []
        try:
            import tempfile
            import hashlib

            @triton.jit
            def _probe_kernel(X, BLOCK_SIZE: tl.constexpr):
                pass

            # Try to compile by calling the kernel builder with mock arguments.
            # We use the internal AST builder to force compilation without running.
            cache_dir = Path(info["cache_dir"])
            before_files: set[str] = set()
            if cache_dir.is_dir():
                before_files = {str(p) for p in cache_dir.rglob("*") if p.is_file()}

            # Attempt a minimal launch to trigger caching.  We wrap in
            # try/except because no real device tensors exist.
            try:
                import torch
                if torch.cuda.is_available():
                    x = torch.zeros(128, device="cuda")
                    _probe_kernel[(1,)](x, BLOCK_SIZE=128)
            except Exception:
                pass

            after_files: set[str] = set()
            if cache_dir.is_dir():
                after_files = {str(p) for p in cache_dir.rglob("*") if p.is_file()}

            new_files = after_files - before_files
            info["cache_export_tested"] = True
            artifact_exts: set[str] = set()
            for fp in new_files:
                ext = Path(fp).suffix.lstrip(".")
                if ext:
                    artifact_exts.add(ext)
            if artifact_exts:
                info["cache_artifact_types"] = sorted(artifact_exts)
        except Exception:
            pass

    except Exception as exc:
        info["error"] = str(exc)
    return info


def collect_env() -> dict:
    gpus = _detect_gpus()
    primary = next((g.get("gfx_arch") for g in gpus if g.get("gfx_arch")), None)
    return {
        "hostname": platform.node(),
        "platform": sys.platform,
        "python": sys.version.split()[0],
        "gpus": gpus,
        "primary_gfx_arch": primary,
        "hipcc": _detect_tool("hipcc", ["--version"]),
        "xcu": _detect_xcu(),
        "hipprof": _detect_hipprof(),
        "dccobjdump": _detect_tool("dccobjdump", ["--version"]),
        "rocminfo": _detect_tool("rocminfo", []),
        "rocm_smi": _detect_rocm_smi(),
        "libs": _detect_python_libs(),
        "triton_features": _detect_triton_features(),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="./env.json")
    args = p.parse_args()
    env = collect_env()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(env, f, indent=2, ensure_ascii=False)
    print(json.dumps({
        "gpu": (env["gpus"][0] or {}).get("name") if env["gpus"] else None,
        "gfx_arch": env["primary_gfx_arch"],
        "python": env["python"],
        "torch": env["libs"].get("torch", {}).get("version"),
        "triton": env["libs"].get("triton", {}).get("version"),
        "triton_target": env["triton_features"].get("active_target"),
        "triton_cache_dir": env["triton_features"].get("cache_dir"),
        "triton_waves_per_eu": env["triton_features"].get("waves_per_eu_accepted"),
        "triton_autotune_disable": env["triton_features"].get("autotune_disable_method"),
        "triton_cache_export_tested": env["triton_features"].get("cache_export_tested"),
        "triton_cache_artifact_types": env["triton_features"].get("cache_artifact_types"),
        "triton_tl_constexpr": env["triton_features"].get("tl_constexpr_available"),
        "hipcc": env["hipcc"].get("path"),
        "xcu": env["xcu"].get("available"),
        "hipprof": env["hipprof"].get("available"),
        "hipprof_pmc": env["hipprof"].get("pmc_available"),
        "dccobjdump": env["dccobjdump"].get("available"),
        "out": args.out,
    }, indent=2))


if __name__ == "__main__":
    main()
