#!/usr/bin/env python3
"""Static review hints for correctness and performance risks in HIP kernels."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    pattern: re.Pattern[str]
    message: str


@dataclass
class Finding:
    rule_id: str
    severity: str
    path: str
    line: int
    column: int
    message: str
    snippet: str


RULES = [
    Rule("RUNTIME_SHARED_BLOCKDIM", "high", re.compile(r"__shared__\s+[^;\n]+\[[^\]]*blockDim[^\]]*\]"), "Static shared-memory extent depends on launch-time blockDim; use a compile-time bound or extern __shared__ with launch bytes."),
    Rule("WARPSIZE_SHARED_EXTENT", "medium", re.compile(r"__shared__\s+[^;\n]+\[[^\]]*warpSize[^\]]*\]"), "warpSize is target/compiler-sensitive in a static extent; use an explicit compile-time specialization or extern __shared__, then compile every declared arch."),
    Rule("GFX936_ONLY", "high", re.compile(r"defined\s*\(\s*__gfx936__\s*\)|#\s*(?:if|ifdef)\s+__gfx936__"), "Determine whether correctness must cover gfx938, but do not mechanically OR arch macros for raw features; use separately probed paths and a generic fallback."),
    Rule("COMBINED_GFX936_GFX938_GATE", "medium", re.compile(r"(?:defined\s*\(\s*__gfx936__\s*\)[^\n]*\|\|[^\n]*defined\s*\(\s*__gfx938__\s*\)|defined\s*\(\s*__gfx938__\s*\)[^\n]*\|\|[^\n]*defined\s*\(\s*__gfx936__\s*\))"), "A combined gfx936/gfx938 gate is not feature evidence; split raw builtin/MFMA/atomic paths unless this portable branch was independently validated on both arches."),
    Rule("FAKE_GFX_WILDCARD", "high", re.compile(r"__gfx9(?:XX|xx)__"), "This is not a real architecture macro; use exact compiler-defined macros and a fallback."),
    Rule("SHUFFLE_NO_WIDTH", "medium", re.compile(r"__(?:shfl|shfl_down|shfl_up|shfl_xor)\s*\([^,]+,[^,\)]+\)"), "Shuffle may rely on full-wave default width; verify the logical group and active lanes."),
    Rule("SHFL_XOR_REVIEW", "medium", re.compile(r"__shfl_xor(?:_sync)?\s*\("), "HIP width does not isolate an arbitrary XOR mask: require a power-of-two width, laneMask < width, and a source lane inside the intended logical group."),
    Rule("WARP32_LITERAL", "medium", re.compile(r"(?:%|/|&|>>|\bWARP_SIZE\s*(?:=|\())\s*(?:31|32|5)\b|0xffffffff(?:u|ull)?\b", re.IGNORECASE), "Possible logical-warp32 assumption; preserve group semantics explicitly."),
    Rule("BALLOT_32BIT", "high", re.compile(r"\bunsigned(?:\s+int)?\s+\w+\s*=\s*__ballot\s*\(|__popc\s*\([^;\n]*__ballot"), "Ballot result or popcount may truncate a wave64 mask; verify the target type and logical group."),
    Rule("SYNCWARP", "high", re.compile(r"__syncwarp\s*\("), "Review execution and memory-ordering semantics; do not mechanically remove."),
    Rule("RAW_AMD_BUILTIN", "high", re.compile(r"__builtin_amdgcn_[A-Za-z0-9_]+"), "Raw architecture builtin needs compiler/arch probes, disassembly, correctness tests, and a standard fallback."),
    Rule("FAST_MATH", "medium", re.compile(r"(?:-ffast-math|--use_fast_math|__(?:expf|logf|sinf|cosf|frsqrt_rn|fdividef)\s*\()"), "Approximate math changes numerics; require an explicit error budget and model gate."),
    Rule("ATOMIC", "info", re.compile(r"\batomic(?:Add|CAS|Exch|Min|Max|And|Or|Xor)\s*\("), "Measure conflict/lowering and verify determinism/gradient semantics before replacing."),
    Rule("DEVICE_SYNCHRONIZE", "medium", re.compile(r"\bhipDeviceSynchronize\s*\("), "Device-wide synchronization may serialize the workload; justify or narrow the dependency."),
    Rule("CONTIGUOUS_OR_CLONE", "info", re.compile(r"\.contiguous\s*\(|\.clone\s*\("), "Count wrapper layout/copy cost in operator E2E and remove only with a proven contract."),
]

SUFFIXES = {".hip", ".cu", ".cuh", ".cpp", ".cc", ".cxx", ".h", ".hpp"}


def iter_files(root: Path):
    if not root.exists():
        raise FileNotFoundError(f"scan path does not exist: {root}")
    if root.is_file():
        if root.suffix.lower() not in SUFFIXES:
            raise RuntimeError(f"unsupported source suffix: {root}")
        yield root
        return
    if not root.is_dir():
        raise RuntimeError(f"scan path is neither a file nor a directory: {root}")
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUFFIXES:
            yield path


def _find_matching_paren(text: str, opening: int) -> int | None:
    depth = 0
    quote: str | None = None
    index = opening
    while index < len(text):
        char = text[index]
        if quote is not None:
            if char == "\\":
                index += 2
                continue
            if char == quote:
                quote = None
            index += 1
            continue
        if text.startswith("//", index):
            newline = text.find("\n", index + 2)
            index = len(text) if newline < 0 else newline + 1
            continue
        if text.startswith("/*", index):
            closing = text.find("*/", index + 2)
            index = len(text) if closing < 0 else closing + 2
            continue
        if char in {'"', "'"}:
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def _split_top_level_arguments(payload: str) -> list[str]:
    arguments = []
    start = 0
    paren = bracket = brace = 0
    quote: str | None = None
    index = 0
    while index < len(payload):
        char = payload[index]
        if quote is not None:
            if char == "\\":
                index += 2
                continue
            if char == quote:
                quote = None
            index += 1
            continue
        if payload.startswith("//", index):
            newline = payload.find("\n", index + 2)
            index = len(payload) if newline < 0 else newline + 1
            continue
        if payload.startswith("/*", index):
            closing = payload.find("*/", index + 2)
            index = len(payload) if closing < 0 else closing + 2
            continue
        if char in {'"', "'"}:
            quote = char
        elif char == "(":
            paren += 1
        elif char == ")":
            paren -= 1
        elif char == "[":
            bracket += 1
        elif char == "]":
            bracket -= 1
        elif char == "{":
            brace += 1
        elif char == "}":
            brace -= 1
        elif char == "," and paren == bracket == brace == 0:
            arguments.append(payload[start:index].strip())
            start = index + 1
        index += 1
    arguments.append(payload[start:].strip())
    return arguments


def _is_default_stream(expression: str) -> bool:
    expression = re.sub(r"/\*.*?\*/", "", expression, flags=re.DOTALL)
    expression = re.sub(r"//[^\n]*", "", expression)
    compact = re.sub(r"\s+", "", expression)
    return bool(
        re.fullmatch(
            r"(?:0[xX]0|0)[uUlL]*|NULL|nullptr|hipStreamDefault|hipStreamLegacy|\(hipStream_t\)(?:0[xX]0|0)[uUlL]*|static_cast<hipStream_t>\((?:0[xX]0|0)[uUlL]*\)",
            compact,
        )
    )


def _finding_at(path: Path, text: str, offset: int, rule_id: str, severity: str, message: str) -> Finding:
    line_number = text.count("\n", 0, offset) + 1
    line_start = text.rfind("\n", 0, offset) + 1
    line_end = text.find("\n", offset)
    if line_end < 0:
        line_end = len(text)
    return Finding(rule_id, severity, str(path), line_number, offset - line_start + 1, message, text[line_start:line_end].strip()[:240])


def _scan_default_stream_launches(path: Path, text: str) -> list[Finding]:
    findings = []
    message = "Kernel launch selects the default/legacy stream; framework extensions should pass the current stream unless the contract explicitly requires default-stream semantics."

    for match in re.finditer(r"\bhipLaunchKernelGGL\s*\(", text):
        opening = text.find("(", match.start())
        closing = _find_matching_paren(text, opening)
        if closing is None:
            continue
        arguments = _split_top_level_arguments(text[opening + 1 : closing])
        if len(arguments) >= 5 and _is_default_stream(arguments[4]):
            findings.append(_finding_at(path, text, match.start(), "DEFAULT_STREAM_LAUNCH", "high", message))

    cursor = 0
    while True:
        opening = text.find("<<<", cursor)
        if opening < 0:
            break
        closing = text.find(">>>", opening + 3)
        if closing < 0:
            break
        arguments = _split_top_level_arguments(text[opening + 3 : closing])
        stream_is_omitted = len(arguments) in {2, 3}
        stream_is_explicit_default = len(arguments) >= 4 and _is_default_stream(arguments[3])
        if stream_is_omitted or stream_is_explicit_default:
            findings.append(_finding_at(path, text, opening, "DEFAULT_STREAM_LAUNCH", "high", message))
        cursor = closing + 3
    return findings


def scan(paths: list[Path]) -> list[Finding]:
    findings = []
    for root in paths:
        files = list(iter_files(root))
        if not files:
            raise RuntimeError(f"no scannable HIP/C++ source files under: {root}")
        for path in files:
            try:
                source = path.read_text(errors="replace")
            except OSError as error:
                raise RuntimeError(f"cannot read source file {path}: {error}") from error
            for line_number, line in enumerate(source.splitlines(), 1):
                for rule in RULES:
                    for match in rule.pattern.finditer(line):
                        findings.append(Finding(rule.rule_id, rule.severity, str(path), line_number, match.start() + 1, rule.message, line.strip()[:240]))
            findings.extend(_scan_default_stream_launches(path, source))
    return findings


def self_test() -> None:
    sample = """#if defined(__gfx936__) || defined(__gfx938__)
__shared__ float shared[blockDim.x / 64];
__shared__ float wave_values[warpSize];
float x = __shfl_down(v, 16);
float y = __shfl_xor(v, 16, 32);
unsigned mask = __ballot(pred);
__syncwarp();
atomicAdd(out, x);
hipLaunchKernelGGL(HIP_KERNEL_NAME(foo<float, 4>), dim3(1, 2), dim3(64), 0, 0, out);
foo<<<grid, block>>>(out);
foo<<<grid, block, 0, hipStreamDefault>>>(out);
hipLaunchKernelGGL(foo, grid, block, 0, current_stream, out);
foo<<<grid, block, 0, current_stream>>>(out);
#endif
"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "sample.hip"
        path.write_text(sample)
        findings = scan([path])
        identifiers = {item.rule_id for item in findings}
        assert {"GFX936_ONLY", "COMBINED_GFX936_GFX938_GATE", "RUNTIME_SHARED_BLOCKDIM", "WARPSIZE_SHARED_EXTENT", "SHUFFLE_NO_WIDTH", "SHFL_XOR_REVIEW", "BALLOT_32BIT", "SYNCWARP", "ATOMIC", "DEFAULT_STREAM_LAUNCH"} <= identifiers
        assert sum(item.rule_id == "DEFAULT_STREAM_LAUNCH" for item in findings) == 3

        empty = Path(directory) / "empty"
        empty.mkdir()
        for invalid in (Path(directory) / "missing", empty):
            try:
                scan([invalid])
            except (FileNotFoundError, RuntimeError):
                pass
            else:
                raise AssertionError(f"scanner did not fail closed for {invalid}")
    print("self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.paths:
        parser.error("at least one source path is required")
    try:
        findings = scan(args.paths)
    except (OSError, RuntimeError) as error:
        print(f"scan error: {error}", file=sys.stderr)
        return 2
    if args.format == "json":
        json.dump([asdict(item) for item in findings], sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        for item in findings:
            print(f"{item.path}:{item.line}:{item.column}: {item.severity} {item.rule_id}: {item.message}")
            print(f"  {item.snippet}")
        print(f"findings: {len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
