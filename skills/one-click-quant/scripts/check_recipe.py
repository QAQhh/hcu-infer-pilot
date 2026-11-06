#!/usr/bin/env python3
# Copyright (c) 2026 Hygon Information Technology Co., Ltd.
# SPDX-License-Identifier: Apache-2.0
"""Validate a preprocess recipe YAML against known transforms / adapter registry.

Requires Python >= 3.8 (repo runtime). Usage from repo root:

  python3 .cursor/skills/one-click-quant/scripts/check_recipe.py preprocess/recipes/deepseek_v3.yaml
"""

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

KNOWN_TRANSFORMS = ("quarot", "flex_awq_ssz", "flex_smooth_quant")
TRANSFORMS_NEEDING_INCLUDE = ("flex_awq_ssz", "flex_smooth_quant")


def _repo_root() -> Path:
    # .../one-click-quant/.cursor/skills/one-click-quant/scripts/check_recipe.py
    return Path(__file__).resolve().parents[4]


def _load_yaml(path: Path) -> Dict[str, Any]:
    try:
        import yaml
    except ImportError as e:
        raise SystemExit("PyYAML required: {}".format(e))
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise SystemExit(
            "{}: root must be a mapping, got {}".format(path, type(data).__name__)
        )
    return data


def _adapter_registry() -> Optional[Dict[str, Any]]:
    root = _repo_root()
    root_s = str(root)
    if root_s not in sys.path:
        sys.path.insert(0, root_s)
    try:
        from preprocess.adapters import ADAPTER_REGISTRY  # type: ignore

        return dict(ADAPTER_REGISTRY)
    except Exception as e:  # noqa: BLE001
        print(
            "WARN: cannot import ADAPTER_REGISTRY ({}); skip adapter registration check".format(
                e
            )
        )
        return None


def check_recipe(path: Path) -> List[str]:
    errors = []  # type: List[str]
    recipe = _load_yaml(path)

    adapter = recipe.get("adapter") or recipe.get("model")
    if not adapter:
        errors.append("missing `adapter:` (or legacy `model:`)")
    else:
        registry = _adapter_registry()
        if registry is not None:
            key = str(adapter).strip()
            if key not in registry and key.replace("-", "_") not in registry:
                known = ", ".join(sorted(set(registry)))
                errors.append(
                    "adapter '{}' not in ADAPTER_REGISTRY (known: {})".format(
                        adapter, known
                    )
                )

    transforms = recipe.get("transforms")
    if transforms is None:
        errors.append("missing `transforms:` list")
        transforms = []
    elif not isinstance(transforms, list) or not transforms:
        errors.append("`transforms:` must be a non-empty list")
        transforms = []
    else:
        for name in transforms:
            if name not in KNOWN_TRANSFORMS:
                errors.append(
                    "unknown transform '{}' (known: {})".format(
                        name, ", ".join(KNOWN_TRANSFORMS)
                    )
                )

    for name in transforms:
        if name not in TRANSFORMS_NEEDING_INCLUDE:
            continue
        block = recipe.get(name)
        if not isinstance(block, dict):
            errors.append("`{}:` block missing or not a mapping".format(name))
            continue
        include = block.get("include")
        if not include:
            errors.append("`{}.include` missing or empty".format(name))
        elif not isinstance(include, list):
            errors.append("`{}.include` must be a list".format(name))

    if "quarot" in transforms:
        block = recipe.get("quarot")
        if block is not None and not isinstance(block, dict):
            errors.append("`quarot:` must be a mapping when present")

    if recipe.get("use_calib_acts") is True:
        errors.append(
            "top-level use_calib_acts is ignored; set per-transform "
            "(flex_awq_ssz / flex_smooth_quant)"
        )

    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("recipe", type=Path, help="Path to recipe YAML")
    args = p.parse_args()
    path = args.recipe
    if not path.is_file():
        print("ERROR: file not found: {}".format(path))
        return 2

    errors = check_recipe(path)
    if errors:
        print("FAIL {}".format(path))
        for e in errors:
            print("  - {}".format(e))
        return 1

    print("OK {}".format(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
