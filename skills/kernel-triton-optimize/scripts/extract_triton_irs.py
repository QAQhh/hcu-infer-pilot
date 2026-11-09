#!/usr/bin/env python3
"""Locate Triton IR/cache/code-object files for a profiled Python kernel."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path


def _candidate_roots(iter_dir: str) -> list[Path]:
    explicit_roots: list[Path] = []
    for env in ("TRITON_CACHE_DIR", "MLIR_DUMP_PATH", "AMDGCN_ENABLE_DUMP_PATH"):
        value = os.environ.get(env)
        if value:
            explicit_roots.append(Path(value))
    if explicit_roots:
        return [p for p in explicit_roots if p.exists()]
    roots: list[Path] = []
    roots.append(Path.home() / ".triton" / "cache")
    roots.append(Path(iter_dir))
    return [p for p in roots if p.exists()]


def _jit_name_hints(kernel: Path) -> set[str]:
    if not kernel.is_file():
        return set()
    try:
        text = kernel.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return set()
    names: set[str] = set()
    matches = re.finditer(r"@triton\.jit[^\n]*\n(?:[ \t]*@[^\n]*\n)*[ \t]*def[ \t]+([A-Za-z_][A-Za-z0-9_]*)", text)
    for match in matches:
        names.add(match.group(1))
    return names


def _artifact_matches(path: Path, *, hints: set[str], since_unix: float | None) -> bool:
    if since_unix is not None:
        try:
            return path.stat().st_mtime >= since_unix
        except OSError:
            return False
    if hints:
        stem = path.stem
        return any(hint == stem or hint in stem for hint in hints)
    # No filtering criteria — match everything as a fallback
    return True


def _collect(root: Path, *, hints: set[str], since_unix: float | None, max_files_per_kind: int) -> tuple[dict[str, list[str]], dict[str, int]]:
    buckets: dict[str, list[tuple[float, str]]] = {
        "ttir": [],
        "ttgir": [],
        "llvm_ir": [],
        "amdgcn": [],
        "hsaco": [],
        "metadata": [],
    }
    skipped = {key: 0 for key in buckets}
    suffix_map = {
        ".ttir": "ttir",
        ".ttgir": "ttgir",
        ".llir": "llvm_ir",
        ".ll": "llvm_ir",
        ".bc": "llvm_ir",
        ".amdgcn": "amdgcn",
        ".hsaco": "hsaco",
        ".json": "metadata",
    }
    for path in root.rglob("*"):
        if "artifacts" in path.parts or "irs" in path.parts:
            continue
        if not path.is_file():
            continue
        bucket = suffix_map.get(path.suffix.lower())
        if not bucket:
            continue
        if not _artifact_matches(path, hints=hints, since_unix=since_unix):
            skipped[bucket] += 1
            continue
        try:
            mtime = path.stat().st_mtime
        except OSError:
            mtime = 0.0
        buckets[bucket].append((mtime, str(path.resolve())))

    out: dict[str, list[str]] = {}
    for key, values in buckets.items():
        values.sort(reverse=True)
        if max_files_per_kind > 0 and len(values) > max_files_per_kind:
            skipped[key] += len(values) - max_files_per_kind
            values = values[:max_files_per_kind]
        out[key] = [value for _, value in values]
    return out, skipped


def _merge(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    for key, values in b.items():
        a.setdefault(key, [])
        for value in values:
            if value not in a[key]:
                a[key].append(value)
    return a


def _archive_cache_dirs(artifacts: dict[str, list[str]], archive_dir: str) -> list[dict]:
    if not archive_dir:
        return []
    archive_root = Path(archive_dir)
    archive_root.mkdir(parents=True, exist_ok=True)
    source_dirs: list[Path] = []
    seen: set[str] = set()
    for paths in artifacts.values():
        for value in paths:
            parent = Path(value).parent
            key = str(parent.resolve())
            if key not in seen and parent.is_dir():
                source_dirs.append(parent)
                seen.add(key)

    archived: list[dict] = []
    used_names: set[str] = set()
    for src in source_dirs:
        name = src.name or "cache_dir"
        dest_name = name
        suffix = 1
        while dest_name in used_names:
            suffix += 1
            dest_name = f"{name}_{suffix}"
        used_names.add(dest_name)
        dest = archive_root / dest_name
        shutil.copytree(src, dest, dirs_exist_ok=True)
        archived.append({"source": str(src.resolve()), "archive": str(dest.resolve())})
    return archived


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", required=True)
    parser.add_argument("--iter-dir", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--active-config-json", default="{}")
    parser.add_argument("--since-unix", type=float, default=None)
    parser.add_argument("--max-files-per-kind", type=int, default=64)
    parser.add_argument("--archive-dir", default="", help="Optional directory to copy matched Triton cache config directories into.")
    args = parser.parse_args()

    artifacts = {"ttir": [], "ttgir": [], "llvm_ir": [], "amdgcn": [], "hsaco": [], "metadata": []}
    skipped = {key: 0 for key in artifacts}
    hints = _jit_name_hints(Path(args.kernel))
    roots = _candidate_roots(args.iter_dir)
    for root in roots:
        collected, root_skipped = _collect(
            root,
            hints=hints,
            since_unix=args.since_unix,
            max_files_per_kind=args.max_files_per_kind,
        )
        _merge(artifacts, collected)
        for key, value in root_skipped.items():
            skipped[key] = skipped.get(key, 0) + value
    code_objects = list(dict.fromkeys(artifacts.get("hsaco", [])))
    archived_cache_dirs = _archive_cache_dirs(artifacts, args.archive_dir)
    status = "ok" if code_objects else "partial" if any(artifacts.values()) else "not_found"
    try:
        active_config = json.loads(args.active_config_json)
    except json.JSONDecodeError:
        active_config = {}
    result = {
        "kernel": str(Path(args.kernel).resolve()),
        "active_config": active_config,
        "cache_roots": [str(p.resolve()) for p in roots],
        "kernel_name_hints": sorted(hints),
        "since_unix": args.since_unix,
        "artifacts": artifacts,
        "code_objects": code_objects,
        "archived_cache_dirs": archived_cache_dirs,
        "skipped_file_counts": skipped,
        "status": status,
        "notes": (
            []
            if code_objects
            else [
                "No hsaco/code object found; ISA verification will be inconclusive.",
            ]
        )
        + (
            []
            if artifacts.get("ttgir")
            else ["No .ttgir found; TTGIR verification in isa_check.py will be inconclusive."]
        ),
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
