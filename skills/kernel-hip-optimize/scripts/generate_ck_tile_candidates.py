#!/usr/bin/env python3
"""Probe CK Tile availability and emit candidate guidance.

This script is a guardrail for CK Tile automation.  It records whether CK Tile
headers/examples are available and writes a candidate manifest.  Actual CK Tile
branch generation should only be enabled for a target family after a generated
source compiles under the active DTK.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _find_ck_tile_include() -> str:
    candidates: list[str] = []
    for var in ("CK_TILE_PATH", "CK_TILE_INCLUDE_DIR", "CK_PATH", "COMPOSABLE_KERNEL_PATH"):
        value = os.environ.get(var, "").strip()
        if value:
            candidates.extend([value, os.path.join(value, "include")])
    candidates.extend(sorted(glob.glob("/opt/dtk*/**/include", recursive=True)))
    candidates.extend(sorted(glob.glob("/opt/rocm*/**/include", recursive=True)))
    candidates.extend(["/opt/dtk/include", "/opt/rocm/include", "/usr/local/include"])
    seen = set()
    for item in candidates:
        path = os.path.abspath(item)
        if path in seen:
            continue
        seen.add(path)
        if os.path.isdir(os.path.join(path, "ck_tile")):
            return path
    return ""


def _op_family(state: dict[str, Any]) -> str:
    dims = state.get("dims", {}) or {}
    if {"M", "N", "K"}.issubset(dims):
        return "gemm"
    if {"M", "N"}.issubset(dims):
        return "norm_or_2d"
    return "unknown"


def _template_status(template: str) -> tuple[bool, str]:
    if not template:
        return False, "no template provided"
    path = Path(template).expanduser().resolve()
    if not path.is_file():
        return False, f"template not found: {path}"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "ck_tile" not in text and "ck::" not in text:
        return False, "template does not look like CK Tile source"
    if 'extern "C" void solve' not in text:
        return False, "template must expose extern \"C\" void solve(...)"
    return True, str(path)


def run(args: argparse.Namespace) -> dict[str, Any]:
    state = _read_json(Path(args.state).expanduser().resolve())
    include_dir = _find_ck_tile_include()
    family = args.family or _op_family(state)
    available = bool(include_dir)
    template_ready, template_note = _template_status(args.template)
    template_path = template_note if template_ready else ""
    candidates: list[dict[str, Any]] = []
    if available and family == "gemm":
        candidates = [
            {
                "family": "gemm",
                "pipeline": "MmacGemmPipelineAGmemBGmemCRegV1",
                "tile_candidates": [
                    {"m": 128, "n": 128, "k": 32},
                    {"m": 64, "n": 128, "k": 32},
                    {"m": 128, "n": 64, "k": 32},
                ],
                "status": "scaffold_required",
                "note": "Use local CK Tile examples/headers to instantiate a source. Do not mark implemented until benchmark.py compiles it as ck_tile.",
            }
        ]
    elif available and family in {"norm", "norm_or_2d"}:
        candidates = [
            {
                "family": "normalization",
                "pipeline": "layernorm2d/rmsnorm2d family",
                "status": "scaffold_required",
                "note": "Use local CK Tile normalization examples if present; keep fallback HIP branch until compiled.",
            }
        ]

    copied_template = ""
    manifest = {
        "state": str(Path(args.state).expanduser().resolve()),
        "ck_tile_available": available,
        "include_dir": include_dir,
        "family": family,
        "candidates": candidates,
        "template_ready": template_ready,
        "template": template_path,
        "ready_for_auto_branch_generation": bool(available and template_ready),
        "env_for_auto_kernel_optimize": f"HYGON_CK_TILE_TEMPLATE={template_path}" if available and template_ready else "",
        "reason": (
            "CK Tile template can be handed to auto_kernel_optimize through HYGON_CK_TILE_TEMPLATE"
            if available and template_ready
            else template_note
            if available
            else "CK Tile headers not found"
        ),
    }
    out = Path(args.out).expanduser().resolve() if args.out else Path(state["run_dir"]) / "ck_tile_candidates.json"
    if available and template_ready and args.copy_template:
        copied = out.parent / "ck_tile_template.hip"
        shutil.copy2(template_path, copied)
        copied_template = str(copied)
        manifest["template"] = copied_template
        manifest["env_for_auto_kernel_optimize"] = f"HYGON_CK_TILE_TEMPLATE={copied_template}"
    _write_json(out, manifest)
    manifest["out"] = str(out)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe CK Tile candidate availability")
    parser.add_argument("--state", required=True)
    parser.add_argument("--family", default="")
    parser.add_argument("--template", default="", help="Optional validated CK Tile source exposing extern C solve(...).")
    parser.add_argument("--copy-template", action="store_true", help="Copy template beside ck_tile_candidates.json and reference the copy.")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
