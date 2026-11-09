#!/usr/bin/env python3
"""GPU 规格参数查询工具（计划实现）。
当前阶段：请直接使用 references/gpu参数对比.csv 获取硬件参数。
"""
import sys, csv
from pathlib import Path

# Shared GPU spec CSV (唯一一份在 fundamentals/cuda-to-hip/references/)
_SCRIPTS = Path(__file__).parent
CSV_PATH = _SCRIPTS.parent.parent.parent / "fundamentals" / "cuda-to-hip" / "references" / "gpu参数对比.csv"
# path: skills/fundamentals/cuda-to-hip/references/gpu参数对比.csv

def get_gpu_specs(gpu_name: str = None):
    """从 CSV 读取 GPU 规格参数。"""
    if not CSV_PATH.exists():
        print(f"错误: CSV 文件不存在: {CSV_PATH}", file=sys.stderr)
        print("提示: 请确保 references/gpu参数对比.csv 存在", file=sys.stderr)
        sys.exit(1)

    with open(CSV_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if gpu_name is None or gpu_name.lower() in str(row).lower():
                print(row)

    if gpu_name:
        print(f"\n未找到 '{gpu_name}' 的精确匹配。请检查 CSV 文件。")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="GPU 硬件参数查询")
    parser.add_argument("--gpu", help="GPU 名称过滤 (如 H20, BW1000)")
    args = parser.parse_args()
    get_gpu_specs(args.gpu)
