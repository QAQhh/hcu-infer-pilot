#!/usr/bin/env python3
"""迁移报告生成器（计划实现）。
当前阶段：请手动整理 report/ 目录中的 Markdown 报告。
预期输入：report/<算子名>_optimization_<TIMESTAMP>.md 格式的迁移中间产物。
"""
import sys
from pathlib import Path


def generate_report(input_md: str, output_html: str = None):
    """从迁移中间产物 Markdown 生成最终报告。"""
    input_path = Path(input_md)
    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_md}", file=sys.stderr)
        sys.exit(1)

    print(f"读取: {input_path}")
    print("报告生成功能计划在后续版本实现。")
    print(f"建议: 手动将 {input_path} 转为 PDF/HTML 提交。")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="迁移报告生成")
    parser.add_argument("input", help="输入 Markdown 文件")
    parser.add_argument("--output", help="输出文件 (可选)")
    args = parser.parse_args()
    generate_report(args.input, args.output)
