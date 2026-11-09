#!/usr/bin/env python3
"""Verify claimed Triton methods against TTGIR and final HCU ISA evidence.

Evidence layers (no LLVM IR / .llir):
  - ttgir: Triton cache ``.ttgir`` MLIR (``tt.`` / ``ttg.`` / ``amdg.`` ops)
  - isa: Triton cache ``.amdgcn`` assembly plus ``dccobjdump`` on hsaco code objects

Signatures: ``references/hcu_triton_isa_signatures.json`` (``ttgir_patterns``,
``isa_patterns``, ``ttgir_check_optional``, ``isa_check_optional`` only).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SIGNATURES = SCRIPT_DIR.parent / "references" / "hcu_triton_isa_signatures.json"
MAX_ARTIFACT_BYTES = 20_000_000


def _read(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write(iter_dir: str, result: dict) -> None:
    out = Path(iter_dir) / "isa_check.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")


def _read_artifact_text(paths: list[str]) -> tuple[str, list[str]]:
    texts: list[str] = []
    errors: list[str] = []
    for raw in paths:
        path = Path(raw)
        if not path.is_file():
            errors.append(f"missing artifact: {raw}")
            continue
        try:
            size = path.stat().st_size
        except OSError as exc:
            errors.append(f"{raw}: {exc}")
            continue
        if size > MAX_ARTIFACT_BYTES:
            errors.append(f"artifact too large, skipped: {raw}")
            continue
        try:
            texts.append(path.read_text(encoding="utf-8", errors="ignore"))
        except OSError as exc:
            errors.append(f"{raw}: {exc}")
    return "\n".join(texts), errors


def _dump_isa(binary: str, arch: str = "") -> tuple[str, list[str]]:
    errors: list[str] = []
    texts: list[str] = []
    with tempfile.TemporaryDirectory(prefix="hygon_triton_isa_") as td:
        out_dir = Path(td) / "dump"
        out_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            "dccobjdump",
            f"--inputs={os.path.abspath(binary)}",
            "--show-sass",
            "--show-instruction-encoding",
            "--separate-functions",
            f"--output={out_dir}",
        ]
        if arch:
            cmd.insert(2, f"--architecture={arch}")
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", timeout=90)
            texts.extend([proc.stdout or "", proc.stderr or ""])
            if proc.returncode != 0:
                errors.append(f"{' '.join(cmd)} rc={proc.returncode}")
        except (OSError, subprocess.TimeoutExpired) as exc:
            errors.append(str(exc))
        for path in out_dir.rglob("*"):
            if path.is_file() and path.stat().st_size < MAX_ARTIFACT_BYTES:
                try:
                    texts.append(path.read_text(encoding="utf-8", errors="ignore"))
                except OSError:
                    pass
    return "\n".join(texts), errors


def _match_patterns(patterns: list[str], text: str, *, require_any: bool) -> tuple[bool, list[str], list[str]]:
    found: list[str] = []
    missing: list[str] = []
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            found.append(pattern)
        else:
            missing.append(pattern)
    if require_any:
        return bool(found), found, missing
    return not missing, found, missing


def _evaluate_layer(
    layer: str,
    patterns: list[str],
    text: str,
    *,
    optional: bool,
    available: bool,
    require_any: bool,
) -> dict:
    result = {
        "layer": layer,
        "applicable": bool(patterns),
        "optional": optional,
        "available": available,
        "patterns_checked": patterns,
        "patterns_found": [],
        "patterns_missing": [],
        "verified": False,
        "inconclusive": False,
    }
    if not patterns:
        result["verified"] = False
        result["note"] = f"no automated {layer}_patterns defined"
        return result
    if not available or not text.strip():
        result["inconclusive"] = not optional
        result["verified"] = optional
        result["note"] = f"{layer} artifacts unavailable"
        return result
    verified, found, missing = _match_patterns(patterns, text, require_any=require_any)
    result["patterns_found"] = found
    result["patterns_missing"] = missing
    result["verified"] = verified
    result["inconclusive"] = False
    return result


def _combine_layers(ttgir: dict, isa: dict) -> tuple[bool, bool, str | None]:
    if ttgir.get("applicable") and ttgir.get("available") and not ttgir.get("verified") and not ttgir.get("optional"):
        return False, False, "ttgir_patterns_missing"
    if isa.get("applicable") and isa.get("available") and not isa.get("verified") and not isa.get("optional"):
        return False, False, "isa_patterns_missing"

    inconclusive = bool(ttgir.get("inconclusive") or isa.get("inconclusive"))

    if not ttgir.get("applicable") and not isa.get("applicable"):
        return False, inconclusive, None

    required_parts: list[bool] = []
    optional_parts: list[bool] = []
    for layer in (ttgir, isa):
        if not layer.get("applicable"):
            continue
        if layer.get("available"):
            if layer.get("optional"):
                optional_parts.append(bool(layer.get("verified")))
            else:
                required_parts.append(bool(layer.get("verified")))
        elif not layer.get("optional"):
            inconclusive = True

    if required_parts:
        return all(required_parts), inconclusive, None
    if optional_parts:
        return any(optional_parts), inconclusive, None
    return False, inconclusive, None


def _method_patterns(meta: dict, layer: str) -> list[str]:
    if layer == "ttgir":
        return list(meta.get("ttgir_patterns", []))
    return list(meta.get("isa_patterns", []))


def _method_optional(meta: dict, layer: str, patterns: list[str]) -> bool:
    if layer == "ttgir":
        return bool(
            meta.get(
                "ttgir_check_optional",
                meta.get("isa_check_optional", False) or not patterns,
            )
        )
    return bool(meta.get("isa_check_optional", False) or not patterns)


def _collect_isa_text(amdgcn_paths: list[str], code_objects: list[str], arch: str) -> tuple[str, list[str]]:
    """Merge .amdgcn cache text with dccobjdump output from hsaco binaries."""
    texts: list[str] = []
    errors: list[str] = []
    amdgcn_text, read_errors = _read_artifact_text(amdgcn_paths)
    errors.extend(read_errors)
    if amdgcn_text.strip():
        texts.append(amdgcn_text)
    for binary in code_objects:
        dump_text, dump_errors = _dump_isa(binary, arch)
        if dump_text.strip():
            texts.append(dump_text)
        errors.extend(dump_errors)
    return "\n".join(texts), errors


def _check_method(method_id: str, ttgir_text: str, isa_text: str, signatures: dict) -> dict:
    meta = signatures.get("methods", {}).get(method_id, {})
    ttgir_patterns = _method_patterns(meta, "ttgir")
    isa_patterns = _method_patterns(meta, "isa")
    automated_check_applicable = bool(ttgir_patterns or isa_patterns)
    require_any = bool(meta.get("require_any", True))
    ttgir_optional = _method_optional(meta, "ttgir", ttgir_patterns)
    isa_optional = _method_optional(meta, "isa", isa_patterns)

    ttgir = _evaluate_layer(
        "ttgir",
        ttgir_patterns,
        ttgir_text,
        optional=ttgir_optional,
        available=bool(ttgir_text.strip()),
        require_any=require_any,
    )
    isa = _evaluate_layer(
        "isa",
        isa_patterns,
        isa_text,
        optional=isa_optional,
        available=bool(isa_text.strip()),
        require_any=require_any,
    )
    verified, inconclusive, failure = _combine_layers(ttgir, isa)
    return {
        "method_id": method_id,
        "verified": verified,
        "inconclusive": inconclusive,
        "implementation_failed": failure is not None,
        "failure_reason": failure,
        "automated_check_applicable": automated_check_applicable,
        "auto_delta_required": not automated_check_applicable,
        "manual_evidence_required": not automated_check_applicable,
        "ttgir": ttgir,
        "isa": isa,
        "patterns_checked": ttgir_patterns + isa_patterns,
        "patterns_found": ttgir.get("patterns_found", []) + isa.get("patterns_found", []),
        "patterns_missing": ttgir.get("patterns_missing", []) + isa.get("patterns_missing", []),
    }


def _inconclusive_checks(methods: list[dict], *, reason: str) -> list[dict]:
    empty_layer = {"layer": "ttgir", "applicable": False, "verified": False, "inconclusive": True}
    return [
        {
            "method_id": m.get("id", "unknown"),
            "verified": False,
            "inconclusive": True,
            "implementation_failed": False,
            "failure_reason": None,
            "note": reason,
            "ttgir": {**empty_layer},
            "isa": {**empty_layer, "layer": "isa"},
            "patterns_checked": [],
            "patterns_found": [],
            "patterns_missing": [],
        }
        for m in methods
    ]


def run(state_path: str, iteration: int, signatures_path: str | None = None) -> dict:
    state = _read(state_path)
    iter_dir = os.path.join(state["run_dir"], f"iterv{iteration}")
    methods_path = os.path.join(iter_dir, "methods.json")
    methods = _read(methods_path).get("methods", []) if os.path.isfile(methods_path) else []
    signatures = _read(signatures_path or DEFAULT_SIGNATURES) if os.path.isfile(signatures_path or DEFAULT_SIGNATURES) else {"methods": {}}
    manifest_path = os.path.join(iter_dir, "artifact_manifest.json")
    manifest = _read(manifest_path) if os.path.isfile(manifest_path) else {}
    artifacts = manifest.get("artifacts") or {}
    code_objects = manifest.get("code_objects") or []
    ttgir_paths = artifacts.get("ttgir") or []
    amdgcn_paths = artifacts.get("amdgcn") or []

    ttgir_text, ttgir_read_errors = _read_artifact_text(ttgir_paths)
    if not code_objects and not ttgir_paths and not amdgcn_paths:
        result = {
            "status": "inconclusive",
            "reason": "no Triton ttgir, amdgcn, or hsaco/code object located",
            "artifact_manifest": manifest_path if os.path.isfile(manifest_path) else None,
            "ttgir": ttgir_paths,
            "amdgcn": amdgcn_paths,
            "code_objects": code_objects,
            "checks": _inconclusive_checks(methods, reason="compiler artifacts unavailable"),
        }
        _write(iter_dir, result)
        print(json.dumps(result, indent=2))
        return result

    arch = state.get("env", {}).get("primary_gfx_arch") or state.get("target_arch") or ""
    isa_text, dump_errors = _collect_isa_text(amdgcn_paths, code_objects, arch)
    dump_errors = list(ttgir_read_errors) + dump_errors

    checks = [_check_method(m.get("id", "unknown"), ttgir_text, isa_text, signatures) for m in methods]
    has_isa = bool(isa_text.strip())
    has_ttgir = bool(ttgir_text.strip())
    if not has_isa and not has_ttgir:
        status = "inconclusive"
    elif any(c.get("implementation_failed") for c in checks):
        status = "failed"
    elif any(c.get("inconclusive") for c in checks):
        status = "partial"
    else:
        status = "ok"

    result = {
        "status": status,
        "code_objects": code_objects,
        "amdgcn": amdgcn_paths,
        "ttgir": ttgir_paths,
        "arch": arch,
        "dump_errors": dump_errors,
        "ttgir_lines": len(ttgir_text.splitlines()),
        "isa_lines": len(isa_text.splitlines()),
        "checks": checks,
    }
    _write(iter_dir, result)
    print(json.dumps(result, indent=2))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--iter", type=int, required=True)
    parser.add_argument("--signatures", default=None)
    args = parser.parse_args()
    run(args.state, args.iter, args.signatures)


if __name__ == "__main__":
    main()
