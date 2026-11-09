#!/usr/bin/env python3
"""Extract only StepTime log content proven to belong to the current run."""

import argparse
import json
import re
import tempfile
from pathlib import Path


STEP_RE = re.compile(rb"\bStepTime\s*(?:[:=]\s*)?[0-9]+(?:\.[0-9]+)?\s*s\b", re.IGNORECASE)
MAX_BYTES = 512 * 1024 * 1024


def read_regular(path, required=False):
    if not path or not path.exists():
        if required:
            raise ValueError(f"required file does not exist: {path}")
        return None
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"refusing non-regular or symlinked file: {path}")
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise ValueError(f"file exceeds {MAX_BYTES} bytes: {path}")
    return path.read_bytes()


def candidate_from_project_log(current, before, marker):
    current_bytes = read_regular(current)
    if current_bytes is None:
        return None, "project_log_missing"
    before_bytes = read_regular(before) if before else None
    marker_stat = marker.stat()
    current_stat = current.stat()

    if before_bytes is not None and current_bytes.startswith(before_bytes):
        appended = current_bytes[len(before_bytes) :]
        if appended:
            return appended, "project_log_appended"
        return None, "project_log_unchanged"
    if current_stat.st_mtime_ns >= marker_stat.st_mtime_ns and current_bytes != before_bytes:
        return current_bytes, "project_log_created_or_replaced_after_marker"
    return None, "project_log_not_proven_current"


def extract(current, before, launcher, marker):
    read_regular(marker, required=True)
    payload, source = candidate_from_project_log(current, before, marker)
    if payload is not None and STEP_RE.search(payload):
        return payload, source

    launcher_bytes = read_regular(launcher, required=True)
    if launcher.stat().st_mtime_ns < marker.stat().st_mtime_ns:
        raise ValueError("launcher log predates the run marker")
    if not STEP_RE.search(launcher_bytes):
        detail = source if payload is None else f"{source}_without_step_times"
        raise ValueError(f"no current-run StepTime samples; project={detail}, launcher=no_step_times")
    return launcher_bytes, "current_launcher_log"


def self_test():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        before = root / "before.log"
        current = root / "log.txt"
        launcher = root / "launcher.log"
        marker = root / "marker"
        output = root / "out.log"
        before.write_bytes(b"old StepTime 9.0s\n")
        current.write_bytes(before.read_bytes())
        marker.touch()
        current.write_bytes(before.read_bytes() + b"new StepTime 1.0s\n")
        launcher.write_bytes(b"launcher StepTime 1.1s\n")
        payload, source = extract(current, before, launcher, marker)
        assert payload == b"new StepTime 1.0s\n" and source == "project_log_appended"
        output.write_bytes(payload)
        assert STEP_RE.search(output.read_bytes())

        current.write_bytes(before.read_bytes())
        payload, source = extract(current, before, launcher, marker)
        assert source == "current_launcher_log" and b"1.1s" in payload
    print("self-test: PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", type=Path, help="Project log after training.")
    parser.add_argument("--before", type=Path, help="Exact pre-run project-log snapshot, if one existed.")
    parser.add_argument("--launcher", type=Path, help="Run-scoped launcher stdout/stderr log.")
    parser.add_argument("--marker", type=Path, help="Run-start marker created immediately before launch.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    missing = [name for name in ("current", "launcher", "marker", "output") if getattr(args, name) is None]
    if missing:
        parser.error("required unless --self-test: " + ", ".join("--" + name.replace("_", "-") for name in missing))
    payload, source = extract(args.current, args.before, args.launcher, args.marker)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    if args.metadata:
        args.metadata.write_text(
            json.dumps(
                {"source": source, "bytes": len(payload), "step_time_samples": len(STEP_RE.findall(payload))},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    print(f"source={source} bytes={len(payload)} step_time_samples={len(STEP_RE.findall(payload))}")


if __name__ == "__main__":
    main()
