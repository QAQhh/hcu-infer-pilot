#!/usr/bin/env python3
"""Prune accepted Hygon Triton configs to a small maintainable registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--accepted", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--max-per-shape", type=int, default=1)
    args = parser.parse_args()
    data = json.loads(Path(args.accepted).read_text(encoding="utf-8"))
    grouped: dict[str, list[dict]] = {}
    for item in data:
        key = json.dumps({
            "arch": item.get("arch"),
            "op_kind": item.get("op_kind"),
            "shape_guard": item.get("shape_guard"),
            "dtype": item.get("dtype"),
            "layout": item.get("layout"),
        }, sort_keys=True)
        grouped.setdefault(key, []).append(item)
    pruned = []
    for items in grouped.values():
        items.sort(key=lambda x: x.get("evidence", {}).get("median_ms", float("inf")))
        pruned.extend(items[: args.max_per_shape])
    Path(args.out).write_text(json.dumps(pruned, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"input": len(data), "output": len(pruned), "out": args.out}, indent=2))


if __name__ == "__main__":
    main()
