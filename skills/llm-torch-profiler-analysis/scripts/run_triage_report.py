#!/usr/bin/env python3
"""Run profiler triage and write a logged markdown report."""

from __future__ import annotations

import argparse
import datetime as dt
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Sequence


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_SKILLS_DIR = SKILL_DIR.parents[1]
ANALYZE_SCRIPT = SKILL_DIR / "scripts" / "analyze_llm_torch_profile.py"
DIAGRAM_SCRIPT = (
    REPO_SKILLS_DIR
    / "skills"
    / "model-architecture-diagram"
    / "scripts"
    / "model_architecture_diagram.py"
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", required=True, type=Path, help="报告和日志输出目录。")
    parser.add_argument("--input", type=Path, help="已有 profile 目录或 trace.json(.gz)。")
    parser.add_argument("--framework", default="auto", help="框架名，默认 auto。")
    parser.add_argument("--model", default="", help="模型名，用于插入结构图。")
    parser.add_argument(
        "--report-name",
        default="torch_profiler_analysis.md",
        help="最终 markdown 报告文件名。",
    )
    parser.add_argument(
        "--log-name",
        default="terminal_commands.log",
        help="终端命令日志文件名。",
    )
    parser.add_argument(
        "--analysis-name",
        default="analysis_stdout.txt",
        help="原始分析 stdout 文件名。",
    )
    args, extra = parser.parse_known_args(argv)
    args.extra_analyze_args = extra
    if args.extra_analyze_args and args.extra_analyze_args[0] == "--":
        args.extra_analyze_args = args.extra_analyze_args[1:]
    if not args.input:
        parser.error("--input is required for existing trace triage.")
    return args


def shell_join(argv: Sequence[str]) -> str:
    return shlex.join(str(item) for item in argv)


def append_command_log(log_path: Path, command: Sequence[str], cwd: Path) -> None:
    timestamp = dt.datetime.now().isoformat(timespec="seconds")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] cwd={cwd}\n")
        f.write(shell_join(command) + "\n\n")


def run_capture(command: Sequence[str], cwd: Path, log_path: Path) -> subprocess.CompletedProcess[str]:
    append_command_log(log_path, command, cwd)
    return subprocess.run(
        list(command),
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def diagram_markdown(model: str, work_dir: Path, log_path: Path) -> str:
    if not model:
        return "未指定模型名，跳过模型结构图。\n"
    if not DIAGRAM_SCRIPT.exists():
        return f"未找到 model-architecture-diagram 解析脚本：`{DIAGRAM_SCRIPT}`。\n"

    command = [sys.executable, str(DIAGRAM_SCRIPT), model]
    result = run_capture(command, work_dir, log_path)
    if result.returncode != 0:
        return (
            f"模型结构图生成失败，命令退出码 {result.returncode}。\n\n"
            "```text\n"
            f"{result.stderr.strip()}\n"
            "```\n"
        )
    return result.stdout.strip() + "\n"


def build_report(
    *,
    args: argparse.Namespace,
    analyze_command: Sequence[str],
    analysis_stdout: str,
    analysis_stderr: str,
    analysis_returncode: int,
    diagram_md: str,
    analysis_path: Path,
    log_path: Path,
) -> str:
    now = dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        "# LLM Torch Profiler 分析报告",
        "",
        "## 元信息",
        "",
        f"- 生成时间：`{now}`",
        f"- 输入 trace/profile：`{args.input.resolve()}`",
        f"- 框架：`{args.framework}`",
        f"- 模型：`{args.model or '未指定'}`",
        f"- 工作目录：`{args.work_dir.resolve()}`",
        f"- 终端命令日志：`{log_path}`",
        f"- 原始分析输出：`{analysis_path}`",
        f"- 分析命令退出码：`{analysis_returncode}`",
        "",
        "## 模型结构图",
        "",
        diagram_md.strip(),
        "",
        "## 执行命令",
        "",
        "```bash",
        shell_join(analyze_command),
        "```",
        "",
    ]
    if analysis_stderr.strip():
        lines.extend(
            [
                "## 分析 stderr",
                "",
                "```text",
                analysis_stderr.strip(),
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## Profiler 分析结果",
            "",
            analysis_stdout.strip() or "_分析脚本没有输出内容。_",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    work_dir = args.work_dir.expanduser().resolve()
    work_dir.mkdir(parents=True, exist_ok=True)
    log_path = work_dir / args.log_name
    analysis_path = work_dir / args.analysis_name
    report_path = work_dir / args.report_name

    self_command = [sys.executable, str(Path(__file__).resolve()), *(argv or sys.argv[1:])]
    append_command_log(log_path, self_command, Path.cwd())

    analyze_command = [
        sys.executable,
        str(ANALYZE_SCRIPT),
        "--input",
        str(args.input.expanduser().resolve()),
        "--framework",
        args.framework,
        *args.extra_analyze_args,
    ]
    result = run_capture(analyze_command, SKILL_DIR, log_path)
    analysis_path.write_text(result.stdout, encoding="utf-8")
    if result.stderr:
        (work_dir / "analysis_stderr.txt").write_text(result.stderr, encoding="utf-8")

    diagram_md = diagram_markdown(args.model, work_dir, log_path)
    report = build_report(
        args=args,
        analyze_command=analyze_command,
        analysis_stdout=result.stdout,
        analysis_stderr=result.stderr,
        analysis_returncode=result.returncode,
        diagram_md=diagram_md,
        analysis_path=analysis_path,
        log_path=log_path,
    )
    report_path.write_text(report, encoding="utf-8")
    print(report_path)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
