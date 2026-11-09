#!/usr/bin/env python3
"""End-to-end orchestrator (v2 — roofline-driven, branch-and-select).

Subcommands:
  setup       Steps 0-1 plus 2a/2b for iter 1:
              check_env, preflight, init, seed baseline, profile+roofline
  open-iter   Steps 2a/2b: profile best_input → hcu_top → roofline → axis budgets
  close-iter  Steps 2f-2k: branch explore → champion → profile+IRs → ablate → ISA check → update
  finalize    Step 3: after required final tuning iteration, emit final_kernel.py,
              final_config.json, final manifest, summary.md

Agent-side SKILL.md steps 2c-2e/2g happen outside this script:
query KB, choose methods, write branch kernels, and repair failed branches.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KERNEL_EXTS = (".hip", ".cu", ".cpp", ".cc", ".cxx", ".py")


def _add_config_args(parser: argparse.ArgumentParser) -> None:
    """Add config-related CLI arguments to a subparser."""
    parser.add_argument("--config-json", type=str, default="",
                        help="Inline JSON config for benchmark overrides")
    parser.add_argument("--config-path", type=str, default="",
                        help="Path to a JSON config file for benchmark overrides")
    parser.add_argument("--config-key", type=str, default="",
                        help="Dot-separated key to select a sub-config within --config-path")
    parser.add_argument("--disable-autotune", action="store_true", default=False,
                        help="Disable triton.autotune in benchmark runs")
    parser.add_argument("--target-arch", type=str, default="",
                        help="Target architecture (e.g. gfx90a) for compilation")


def _config_args_to_cmd(args) -> list[str]:
    """Return a list of command-line flag strings for the config args."""
    cmd: list[str] = []
    if getattr(args, "config_json", ""):
        cmd += ["--config-json", args.config_json]
    if getattr(args, "config_path", ""):
        cmd += ["--config-path", args.config_path]
    if getattr(args, "config_key", ""):
        cmd += ["--config-key", args.config_key]
    if getattr(args, "disable_autotune", False):
        cmd += ["--disable-autotune"]
    if getattr(args, "target_arch", ""):
        cmd += ["--target-arch", args.target_arch]
    return cmd


def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    print(f"[run] {' '.join(cmd)}", file=sys.stderr)
    return subprocess.run(cmd, text=True, **kw)


def _read(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write(path: str, payload: dict) -> None:
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def _dims_from_json(value: str) -> dict:
    try:
        dims = json.loads(value) if value else {}
    except json.JSONDecodeError as exc:
        sys.exit(f"--dims must be valid JSON: {exc}")
    if not isinstance(dims, dict):
        sys.exit("--dims must decode to a JSON object")
    return dims


def _dims_argv(dims: dict) -> list[str]:
    return [f"--{k}={v}" for k, v in dims.items()]


def _ptr_size_argv(ptr_size: int) -> list[str]:
    return ["--ptr-size", str(ptr_size)] if ptr_size and ptr_size > 0 else []


def _source_autotune_status(path: str) -> dict:
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {
            "path": path,
            "exists": False,
            "has_triton_autotune": False,
            "mentions_autotune": False,
            "has_winner_provenance": False,
        }
    return {
        "path": os.path.abspath(path),
        "exists": True,
        "has_triton_autotune": bool(re_search_autotune(text)),
        "mentions_autotune": "autotune" in text.lower(),
        "has_winner_provenance": _has_autotune_winner_provenance(text),
    }


def re_search_autotune(text: str) -> bool:
    return "@triton.autotune" in text or "triton.autotune(" in text


def _has_autotune_winner_provenance(text: str) -> bool:
    lowered = text.lower()
    if "autotune" not in lowered or "winner" not in lowered:
        return False
    markers = (
        "AUTOTUNE_BASELINE_PROVENANCE",
        "AUTOTUNE_WINNER_CONFIG",
        "DEFAULT_CONFIG_SOURCE",
        "native_autotune_winner",
        "triton_autotune_best_config",
    )
    return any(marker in text for marker in markers)


def _has_explicit_config(args) -> bool:
    return bool(getattr(args, "config_json", "") or getattr(args, "config_path", ""))


def _resolve_source_path(raw: str, case_dir: str) -> str | None:
    if not raw:
        return None
    token = str(raw).strip().split()[0].strip("'\"")
    if not token:
        return None
    if ":" in token and not os.path.exists(token):
        token = token.split(":", 1)[0]
    if not token.endswith(KERNEL_EXTS):
        return None
    path = Path(token)
    if not path.is_absolute():
        path = Path(case_dir) / path
    return str(path.resolve())


def _manifest_source_candidates(case_dir: str) -> list[str]:
    manifest = Path(case_dir) / "baseline_manifest.json"
    if not manifest.is_file():
        return []
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except Exception:
        return []
    raw_values: list[str] = []

    def visit(value) -> None:
        if isinstance(value, str):
            raw_values.append(value)
        elif isinstance(value, dict):
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(payload)
    out: list[str] = []
    for value in raw_values:
        resolved = _resolve_source_path(value, case_dir)
        if resolved:
            out.append(resolved)
    return out


def _native_source_statuses(args, state: dict) -> list[dict]:
    baseline_original = os.path.abspath(state.get("baseline_file_original") or state.get("baseline_file") or "")
    case_dir = os.path.dirname(baseline_original) if baseline_original else os.getcwd()
    candidates: list[str] = []
    for raw in getattr(args, "native_source", []) or []:
        resolved = _resolve_source_path(raw, case_dir)
        if resolved:
            candidates.append(resolved)
    candidates.extend(_manifest_source_candidates(case_dir))
    if baseline_original:
        candidates.append(baseline_original)

    seen = set()
    statuses = []
    for path in candidates:
        abspath = os.path.abspath(path)
        if abspath in seen:
            continue
        seen.add(abspath)
        status = _source_autotune_status(abspath)
        if status.get("exists"):
            statuses.append(status)
    return statuses


def _record_baseline_autotune_state(state_path: str, payload: dict) -> None:
    state = _read(state_path)
    state["baseline_autotune"] = payload
    _write(state_path, state)


def _fail_baseline_autotune(state_path: str, payload: dict, guidance: str) -> None:
    payload["guidance"] = guidance
    _record_baseline_autotune_state(state_path, payload)
    sys.exit(guidance)


def _maybe_probe_baseline_autotune(args, state_path: str) -> dict | None:
    """Probe an autotuned baseline once, then return a fixed config to seed with.

    This only works when the benchmark-compatible baseline exposes the selected
    config through setup()/bench.json.active_config. If the native demo had
    autotune but the provided baseline wrapper already removed it, the wrapper
    must bake the native winner or the user must pass --config-json/path.
    """
    state = _read(state_path)
    baseline_file = state["baseline_file"]
    status = _source_autotune_status(baseline_file)
    native_statuses = _native_source_statuses(args, state)
    native_autotune_sources = [
        item for item in native_statuses
        if item.get("has_triton_autotune")
        and os.path.abspath(item.get("path", "")) != os.path.abspath(baseline_file)
    ]
    payload = {
        "mode": args.baseline_autotune,
        "baseline_file": baseline_file,
        "baseline_file_original": state.get("baseline_file_original"),
        "baseline_status": status,
        "native_sources": native_statuses,
        "status": "not_required",
    }

    if args.baseline_autotune == "off":
        payload["status"] = "disabled"
        _record_baseline_autotune_state(state_path, payload)
        return None
    if _has_explicit_config(args):
        payload["status"] = "skipped_explicit_fixed_config"
        _record_baseline_autotune_state(state_path, payload)
        return None
    if not status["has_triton_autotune"]:
        if native_autotune_sources:
            if status.get("has_winner_provenance"):
                payload["status"] = "wrapper_claims_native_autotune_winner"
                _record_baseline_autotune_state(state_path, payload)
                return None
            payload["status"] = "native_autotune_removed_without_winner"
            sources = ", ".join(item["path"] for item in native_autotune_sources)
            _fail_baseline_autotune(
                state_path,
                payload,
                "Native source uses @triton.autotune but the benchmark baseline has removed it "
                "without fixed-winner provenance. Run the original autotune space first and pass "
                f"--config-json/--config-path, or bake AUTOTUNE_BASELINE_PROVENANCE into the wrapper. Sources: {sources}",
            )
        if status["mentions_autotune"]:
            if status.get("has_winner_provenance"):
                payload["status"] = "wrapper_claims_native_autotune_winner"
                _record_baseline_autotune_state(state_path, payload)
                return None
            payload["status"] = "autotune_removed_without_winner"
            _fail_baseline_autotune(
                state_path,
                payload,
                "Baseline mentions autotune but has no active triton.autotune decorator and no "
                "winner provenance. Run the original autotune before deleting it, or pass "
                "--config-json/--config-path with the native winner.",
            )
        _record_baseline_autotune_state(state_path, payload)
        return None

    run_dir = state["run_dir"]
    out_dir = os.path.join(run_dir, "baseline")
    os.makedirs(out_dir, exist_ok=True)
    json_out = os.path.join(out_dir, "autotune_probe_bench.json")
    log_out = os.path.join(out_dir, "autotune_probe.stderr.txt")
    dims = _dims_from_json(args.dims)
    cmd = [
        sys.executable, os.path.abspath(args.benchmark), baseline_file,
        "--ref", state["ref_file"],
        "--warmup", str(args.autotune_warmup),
        "--repeat", str(args.autotune_repeat),
        "--json-out", json_out,
    ] + _ptr_size_argv(state.get("ptr_size", 0)) + _dims_argv(dims)
    if getattr(args, "target_arch", ""):
        cmd.extend(["--target-arch", args.target_arch])

    env = os.environ.copy()
    env.setdefault("TRITON_PRINT_AUTOTUNING", "1")
    probe = _run(cmd, capture_output=True, env=env)
    with open(log_out, "w", encoding="utf-8") as f:
        f.write("---STDOUT---\n")
        f.write(probe.stdout or "")
        f.write("\n---STDERR---\n")
        f.write(probe.stderr or "")

    payload.update({
        "status": "probe_failed" if probe.returncode != 0 else "probed",
        "probe_bench": json_out,
        "probe_log": log_out,
        "returncode": probe.returncode,
    })
    bench = _read(json_out) if os.path.isfile(json_out) else {}
    active = bench.get("active_config")
    passed = bool(bench.get("correctness", {}).get("passed", False))
    payload["correctness_passed"] = passed
    payload["selected_config"] = active if isinstance(active, dict) else None
    payload["selected_config_key"] = bench.get("config_key")
    payload["probe_ms"] = (bench.get("kernel") or {}).get("average_ms")

    if not passed or not isinstance(active, dict) or not active:
        payload["status"] = "probe_no_fixed_config"
        _fail_baseline_autotune(
            state_path,
            payload,
            "Autotune probe did not expose a non-empty bench.json.active_config. "
            "Keep the original autotune wrapper probeable until Triton Autotuner.best_config can be "
            "recorded, then bake that native winner into DEFAULT_CONFIG or pass --config-json/--config-path.",
        )

    payload["status"] = "fixed_from_autotune_probe"
    _record_baseline_autotune_state(state_path, payload)
    return dict(active)


def _last_iteration(state: dict) -> int:
    values = [0]
    for item in state.get("history", []) or []:
        if isinstance(item, dict) and item.get("iter") is not None:
            try:
                values.append(int(item["iter"]))
            except Exception:
                pass
    for item in state.get("roofline_history", []) or []:
        if isinstance(item, dict) and item.get("iter") is not None:
            try:
                values.append(int(item["iter"]))
            except Exception:
                pass
    for item in state.get("tune_history", []) or []:
        if isinstance(item, dict) and item.get("iter") is not None:
            try:
                values.append(int(item["iter"]))
            except Exception:
                pass
    return max(values or [0])


def _final_tune_required(state: dict) -> bool:
    if state.get("final_tune", {}).get("completed"):
        return False
    if state.get("effective_methods"):
        return True
    for item in state.get("history", []) or []:
        if isinstance(item, dict) and item.get("status") == "improved":
            return True
    baseline_file = os.path.abspath(state.get("baseline_file") or "")
    best_file = os.path.abspath(state.get("best_file") or "")
    return bool(baseline_file and best_file and baseline_file != best_file)


def _profile_cmd(state_path: str, iteration: int, which: str, benchmark: str, args) -> list[str]:
    return [
        sys.executable, str(SCRIPT_DIR / "profile_hcu.py"),
        "--state", state_path,
        "--iter", str(iteration),
        "--which", which,
        "--benchmark", os.path.abspath(benchmark),
    ] + _config_args_to_cmd(args)


def _profile_artifact_from_top(iter_dir: str, default_path: str) -> str:
    top_path = os.path.join(iter_dir, "hcu_top.json")
    if not os.path.isfile(top_path):
        return default_path
    try:
        top = _read(top_path)
    except Exception:
        return default_path
    return top.get("profiler_output") or top.get("xcu_output") or top.get("hipprof_output") or default_path


# ---------------------------------------------------------------------------
# setup  —  SKILL.md steps 0-1, then 2a/2b for iter 1
# ---------------------------------------------------------------------------

def cmd_setup(args):
    env_json = os.path.abspath(args.env_out or "./env.json")

    # Step 0: check_env
    rc = _run([sys.executable, str(SCRIPT_DIR / "check_env.py"),
               "--out", env_json]).returncode
    if rc != 0:
        sys.exit(f"check_env failed rc={rc}")

    # Step 0: preflight validates the setup()/run_kernel() and ref contracts
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "preflight.py"),
        "--baseline", os.path.abspath(args.baseline),
        "--ref", os.path.abspath(args.ref),
        "--dims", args.dims,
    ]).returncode
    if rc != 0:
        sys.exit("preflight failed — fix baseline/ref/dims above, then retry")

    # Step 1: init run dir + state
    init_cmd = [
        sys.executable, str(SCRIPT_DIR / "state.py"), "init",
        "--baseline", os.path.abspath(args.baseline),
        "--ref", os.path.abspath(args.ref),
        "--iterations", str(args.iterations),
        "--ncu-num", str(args.ncu_num),
        "--branches", str(args.branches),
        "--dims", args.dims,
        "--env", env_json,
        "--noise-threshold-pct", str(args.noise_threshold_pct),
        "--ptr-size", str(args.ptr_size),
    ]
    if args.shape_family:
        init_cmd.extend(["--shape-family", args.shape_family])
    if args.allow_nested_run_baseline:
        init_cmd.append("--allow-nested-run-baseline")
    if args.allow_duplicate_dims:
        init_cmd.append("--allow-duplicate-dims")
    init = _run(init_cmd, capture_output=True)
    if init.returncode != 0:
        sys.stderr.write(init.stderr or "")
        sys.exit("state init failed")
    sys.stderr.write(init.stderr or "")

    init_info = {}
    try:
        init_info = json.loads(init.stdout or "{}")
    except json.JSONDecodeError:
        for line in reversed((init.stdout or "").splitlines()):
            line = line.strip()
            if line.startswith("{") and line.endswith("}"):
                try:
                    init_info = json.loads(line)
                    break
                except json.JSONDecodeError:
                    continue
    run_dir = init_info.get("run_dir")
    state_path = init_info.get("state")
    if not run_dir or not state_path:
        sys.exit(f"could not parse state init output:\n{init.stdout}")

    autotuned_config = _maybe_probe_baseline_autotune(args, state_path)
    if autotuned_config:
        args.config_json = json.dumps(autotuned_config, separators=(",", ":"))
        args.config_path = ""
        if not args.config_key:
            state = _read(state_path)
            key = (state.get("baseline_autotune") or {}).get("selected_config_key")
            args.config_key = str(key or "autotune_probe_best")
        args.disable_autotune = True

    # Step 1: seed baseline
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "run_iteration.py"), "seed-baseline",
        "--state", state_path,
        "--benchmark", os.path.abspath(args.benchmark),
        "--warmup", str(args.warmup),
        "--repeat", str(args.repeat),
    ] + _config_args_to_cmd(args)).returncode
    if rc != 0:
        sys.exit("baseline seed failed")

    # Step 2a for iter 1: profile best_input
    rc = _run(_profile_cmd(state_path, 1, "best_input", args.benchmark, args)).returncode
    if rc != 0:
        print("[warn] HCU profiling failed or degraded", file=sys.stderr)

    # Step 2b for iter 1: roofline
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "roofline.py"),
        "--state", state_path,
        "--iter", "1",
    ]).returncode

    # Step 2b: check for near-peak early stop
    iter_dir = os.path.join(run_dir, "iterv1")
    roofline_path = os.path.join(iter_dir, "roofline.json")
    early_stop = False
    if os.path.isfile(roofline_path):
        roofline = _read(roofline_path)
        early_stop = roofline.get("near_peak", False)

    print(json.dumps({
        "run_dir": run_dir,
        "state": state_path,
        "env": env_json,
        "early_stop": early_stop,
        "next_step": (
            "On the local agent/control host, first run the Semantic Pre-Pass: write "
            "iterv1/analysis.md with Kernel Computation Logic, Formula-First Analysis, Loop / Candidate Inventory, "
            "and Semantic Pre-Pass Result; inspect references/triton_semantic_prepass.md and "
            "references/triton_optimization_memory.md. Record any source rewrite with "
            "scripts/record_attempt.py --kind semantic_rewrite as pending/success/failure based on evidence, "
            "and optionally write iterv1/tuning_space.json. Then run "
            "scripts/tune_configs.py --search-level broad before method selection; it records one consolidated config_tune event. After tuning, run scripts/query_kb.py --out-dir iterv1 "
            "before writing methods/branches. The agent should then read iterv1/kb_evidence.md or "
            "kb_unavailable.json, iterv1/roofline.json (for axis budgets), iterv1/hcu_top.json, "
            "iterv1/tune_results.json or accepted_configs.json when present, and state.json, then write "
            f"iterv1/branches/b{{1..K}}/kernel.<ext>, iterv1/methods.json, "
            "and iterv1/analysis.md. "
            "After that, run: orchestrate.py close-iter --run-dir <run_dir> --iter 1"
        ) if not early_stop else "Near roofline — consider stopping.",
    }, indent=2))


# ---------------------------------------------------------------------------
# open-iter  —  SKILL.md steps 2a/2b for iteration N
# ---------------------------------------------------------------------------

def cmd_open_iter(args):
    state_path = os.path.join(args.run_dir, "state.json")
    if not os.path.isfile(state_path):
        sys.exit(f"state.json missing: {state_path}")

    state = _read(state_path)

    # Step 2a: profile best_input for this iter
    rc = _run(_profile_cmd(state_path, args.iter, "best_input", args.benchmark, args)).returncode
    if rc != 0:
        print("[warn] HCU profiling failed or degraded", file=sys.stderr)

    # Step 2b: roofline + axis budgets
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "roofline.py"),
        "--state", state_path,
        "--iter", str(args.iter),
    ]).returncode

    # Step 2b: check for near-peak early stop
    iter_dir = os.path.join(args.run_dir, f"iterv{args.iter}")
    roofline_path = os.path.join(iter_dir, "roofline.json")
    early_stop = False
    if os.path.isfile(roofline_path):
        roofline = _read(roofline_path)
        early_stop = roofline.get("near_peak", False)

    # Prepare branch dirs for agent-side step 2e
    num_branches = state.get("branches", 4)
    branches_dir = os.path.join(iter_dir, "branches")
    for b in range(1, num_branches + 1):
        os.makedirs(os.path.join(branches_dir, f"b{b}"), exist_ok=True)

    print(json.dumps({
        "iter": args.iter,
        "early_stop": early_stop,
        "branches_dir": branches_dir,
        "num_branches": num_branches,
        "next_step": (
            f"On the local agent/control host, carry forward or update Kernel Computation Logic and "
            f"Formula-First Analysis in iterv{args.iter}/analysis.md, including Semantic Pre-Pass Result when it changes. If source/config assumptions changed, "
            f"record any semantic rewrite with scripts/record_attempt.py, optionally update "
            f"iterv{args.iter}/tuning_space.json, and rerun scripts/tune_configs.py --search-level broad. "
            f"Then run scripts/query_kb.py --out-dir iterv{args.iter} before writing methods/branches. "
            f"The agent should then read iterv{args.iter}/kb_evidence.md or kb_unavailable.json, "
            f"iterv{args.iter}/roofline.json, hcu_top.json, and tune_results.json when present, "
            f"write {num_branches} branch kernels under iterv{args.iter}/branches/b{{1..{num_branches}}}/kernel.<ext>, "
            f"plus iterv{args.iter}/methods.json and iterv{args.iter}/analysis.md. "
            f"Then run: orchestrate.py close-iter --run-dir {args.run_dir} --iter {args.iter}"
        ) if not early_stop else "Near roofline — consider stopping.",
    }, indent=2))


# ---------------------------------------------------------------------------
# close-iter  —  SKILL.md steps 2f-2k
# ---------------------------------------------------------------------------

def cmd_close_iter(args):
    state_path = os.path.join(args.run_dir, "state.json")
    if not os.path.isfile(state_path):
        sys.exit(f"state.json missing: {state_path}")

    state = _read(state_path)
    iter_dir = os.path.join(args.run_dir, f"iterv{args.iter}")
    methods_json = os.path.join(iter_dir, "methods.json")
    if not os.path.isfile(methods_json):
        sys.exit(f"methods.json missing at {methods_json}")

    # Validate agent-side step 2d output before exploring branches.
    analysis_path = os.path.join(iter_dir, "analysis.md")
    analysis_check = _run([
        sys.executable, str(SCRIPT_DIR / "validate_methods.py"),
        "--analysis", analysis_path,
    ], capture_output=True)
    if analysis_check.returncode != 0:
        try:
            payload = json.loads(analysis_check.stdout or "{}")
            errors = payload.get("errors", [analysis_check.stdout or "analysis.md invalid"])
        except json.JSONDecodeError:
            errors = [analysis_check.stdout or analysis_check.stderr or "analysis.md invalid"]
        print(json.dumps({
            "iter": args.iter,
            "status": "analysis_invalid",
            "errors": errors,
            "guidance": (
                "Write a non-placeholder ## Kernel Computation Logic section in "
                f"{analysis_path} before close-iter."
            ),
        }, indent=2))
        sys.exit(3)

    # Step 2f: branch explore — compile + benchmark all branches
    branch_result = _run([
        sys.executable, str(SCRIPT_DIR / "branch_explore.py"),
        "--state", state_path,
        "--iter", str(args.iter),
        "--benchmark", os.path.abspath(args.benchmark),
        "--warmup", str(args.warmup),
        "--repeat", str(args.repeat),
    ] + _config_args_to_cmd(args), capture_output=True)
    sys.stderr.write(branch_result.stderr or "")

    if branch_result.returncode == 2:
        # Step 2g: agent repairs failed/invalid branches, then retries close-iter.
        print(json.dumps({
            "iter": args.iter,
            "status": "all_branches_failed",
            "guidance": "The agent should fix the kernels and retry close-iter.",
        }, indent=2))
        sys.exit(2)
    if branch_result.returncode != 0:
        sys.exit(f"branch_explore failed rc={branch_result.returncode}")

    # Find champion kernel
    kernel = None
    for ext in KERNEL_EXTS:
        candidate = os.path.join(iter_dir, f"kernel{ext}")
        if os.path.isfile(candidate):
            kernel = candidate
            break
    if not kernel:
        sys.exit(f"No champion kernel found after branch_explore")

    bench_json = os.path.join(iter_dir, "bench.json")
    if not os.path.isfile(bench_json):
        sys.exit(f"bench.json missing for champion")

    bench = _read(bench_json)
    passed = bool(bench.get("correctness", {}).get("passed", False))

    if not passed:
        # Step 2g: agent repairs validation failures, then retries close-iter.
        print(json.dumps({
            "iter": args.iter,
            "status": "validation_failed",
            "bench_json": bench_json,
            "guidance": "The agent should fix the kernel and re-run close-iter.",
        }, indent=2))
        sys.exit(2)

    # Step 2h: profile champion and capture Triton IR/cache artifacts.
    profile_cmd = _profile_cmd(state_path, args.iter, "kernel", args.benchmark, args)
    profile_cmd.append("--promote-if-best")
    rc = _run(profile_cmd).returncode
    if rc != 0:
        print("[warn] HCU profiling of champion failed", file=sys.stderr)

    # Step 2i: ablation attribution (optional — runs if ablation kernels exist)
    attribution_path = os.path.join(iter_dir, "attribution.json")
    ablation_dir = os.path.join(iter_dir, "ablations")
    if os.path.isdir(ablation_dir):
        _run([
            sys.executable, str(SCRIPT_DIR / "ablate.py"),
            "--state", state_path,
            "--iter", str(args.iter),
            "--benchmark", os.path.abspath(args.benchmark),
        ] + _config_args_to_cmd(args))

    # Step 2j: HCU ISA verification
    isa_check_path = os.path.join(iter_dir, "isa_check.json")
    _run([
        sys.executable, str(SCRIPT_DIR / "isa_check.py"),
        "--state", state_path,
        "--iter", str(args.iter),
    ])

    # Step 2k: update state
    update_cmd = [
        sys.executable, str(SCRIPT_DIR / "state.py"), "update",
        "--state", state_path,
        "--iter", str(args.iter),
        "--kernel", kernel,
        "--bench", bench_json,
        "--methods-json", methods_json,
        "--retries", str(args.retries),
    ] + _config_args_to_cmd(args)
    if os.path.isfile(attribution_path):
        update_cmd.extend(["--attribution", attribution_path])
    if os.path.isfile(isa_check_path):
        update_cmd.extend(["--isa-check", isa_check_path])

    rc = _run(update_cmd).returncode
    if rc != 0:
        sys.exit("state update failed")

    state = _read(state_path)
    hipprof_output = _profile_artifact_from_top(iter_dir, os.path.join(iter_dir, "kernel.hipprof"))
    if os.path.abspath(state.get("best_file", "")) == os.path.abspath(kernel):
        _run([
            sys.executable, str(SCRIPT_DIR / "state.py"), "set-best-hipprof-output",
            "--state", state_path,
            "--hipprof-output", hipprof_output,
        ])

    # Open next iteration with steps 2a/2b if needed.
    state = _read(state_path)
    next_iter = args.iter + 1
    if next_iter <= state["iterations_total"]:
        # Steps 2a/2b for next iter: profile best_input + roofline
        _run(_profile_cmd(state_path, next_iter, "best_input", args.benchmark, args))
        _run([
            sys.executable, str(SCRIPT_DIR / "roofline.py"),
            "--state", state_path,
            "--iter", str(next_iter),
        ])

        # Step 2b: check for near-peak early stop
        roofline_path = os.path.join(state["run_dir"], f"iterv{next_iter}", "roofline.json")
        early_stop = False
        if os.path.isfile(roofline_path):
            roofline = _read(roofline_path)
            early_stop = roofline.get("near_peak", False)
    else:
        early_stop = False

    print(json.dumps({
        "iter": args.iter,
        "status": "closed",
        "best_ms": state.get("best_metric_ms"),
        "next_iter": next_iter if next_iter <= state["iterations_total"] else None,
        "early_stop": early_stop,
        "state": state_path,
    }, indent=2))


# ---------------------------------------------------------------------------
# finalize  —  SKILL.md step 3
# ---------------------------------------------------------------------------

def cmd_finalize(args):
    state_path = os.path.join(args.run_dir, "state.json")
    state = _read(state_path)
    if _final_tune_required(state) and not args.skip_final_tune_check:
        final_iter = _last_iteration(state) + 1
        message = {
            "error": "final_tune_required",
            "reason": (
                "A prior iteration promoted a source rewrite, method, or faster champion. "
                "Run a final fixed-config tuning iteration before finalize, or pass "
                "--skip-final-tune-check and document the skip reason in summary.md."
            ),
            "suggested_iter": final_iter,
            "suggested_command": (
                f"python {SCRIPT_DIR / 'tune_configs.py'} --state {state_path} "
                f"--iter {final_iter} --which best_input --search-level broad "
                f"--max-configs 64 --final-tune --promote-if-better"
            ),
        }
        print(json.dumps(message, indent=2), file=sys.stderr)
        sys.exit(2)
    summary_path = os.path.join(args.run_dir, "summary.md")
    final_kernel_path = os.path.join(args.run_dir, "final_kernel.py")
    final_config_path = os.path.join(args.run_dir, "final_config.json")
    final_manifest_path = os.path.join(args.run_dir, "final_kernel_manifest.json")
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "finalize_kernel.py"),
        "--state", state_path,
        "--out", final_kernel_path,
        "--config-out", final_config_path,
        "--manifest-out", final_manifest_path,
    ]).returncode
    if rc != 0:
        sys.exit("final kernel generation failed")
    rc = _run([
        sys.executable, str(SCRIPT_DIR / "summarize.py"),
        "--state", state_path,
        "--out", summary_path,
    ]).returncode
    if rc != 0:
        sys.exit("summarize failed")
    print(json.dumps({
        "summary": summary_path,
        "final_kernel": final_kernel_path,
        "final_config": final_config_path,
        "final_manifest": final_manifest_path,
    }, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    _default_bench = str(SCRIPT_DIR / "benchmark.py")

    ps = sub.add_parser("setup")
    ps.add_argument("--baseline", required=True)
    ps.add_argument("--ref", required=True)
    ps.add_argument("--benchmark", default=_default_bench)
    ps.add_argument("--iterations", type=int, default=3)
    ps.add_argument("--ncu-num", type=int, default=5)
    ps.add_argument("--branches", type=int, default=4)
    ps.add_argument("--dims", required=True, help="JSON dict of name->int")
    ps.add_argument("--noise-threshold-pct", type=float, default=2.0)
    ps.add_argument("--ptr-size", type=int, default=0)
    ps.add_argument("--env-out", type=str, default="")
    ps.add_argument("--warmup", type=int, default=10)
    ps.add_argument("--repeat", type=int, default=20)
    ps.add_argument("--baseline-autotune", choices=["auto", "off", "force"], default="auto",
                    help=(
                        "When the benchmark baseline still uses triton.autotune and no fixed config "
                        "was provided, probe once with autotune enabled, then seed baseline with the "
                        "reported active_config under --disable-autotune. auto/force fail if native "
                        "autotune evidence exists but no fixed winner can be recovered."
                    ))
    ps.add_argument("--native-source", action="append", default=[],
                    help=(
                        "Original source file that still owns the Triton autotune space. Repeatable; "
                        "relative paths resolve from the baseline's case directory."
                    ))
    ps.add_argument("--autotune-warmup", type=int, default=5,
                    help="Warmup iterations for the setup-time baseline autotune probe.")
    ps.add_argument("--autotune-repeat", type=int, default=10,
                    help="Timed repeats for the setup-time baseline autotune probe.")
    ps.add_argument("--shape-family", type=str, default="",
                    help="Optional shape family label recorded in state.json.")
    ps.add_argument("--allow-nested-run-baseline", action="store_true",
                    help="Allow setup from a baseline under an existing run_* directory.")
    ps.add_argument("--allow-duplicate-dims", action="store_true",
                    help="Allow creating another run_* with dims matching an existing sibling run.")
    _add_config_args(ps)
    ps.set_defaults(func=cmd_setup)

    po = sub.add_parser("open-iter")
    po.add_argument("--run-dir", required=True)
    po.add_argument("--iter", type=int, required=True)
    po.add_argument("--benchmark", default=_default_bench)
    _add_config_args(po)
    po.set_defaults(func=cmd_open_iter)

    pc = sub.add_parser("close-iter")
    pc.add_argument("--run-dir", required=True)
    pc.add_argument("--iter", type=int, required=True)
    pc.add_argument("--benchmark", default=_default_bench)
    pc.add_argument("--warmup", type=int, default=10)
    pc.add_argument("--repeat", type=int, default=20)
    pc.add_argument("--retries", type=int, default=0)
    _add_config_args(pc)
    pc.set_defaults(func=cmd_close_iter)

    pf = sub.add_parser("finalize")
    pf.add_argument("--run-dir", required=True)
    pf.add_argument("--skip-final-tune-check", action="store_true",
                    help="Allow finalize without the required final tuning iteration; summary.md must document the reason.")
    pf.set_defaults(func=cmd_finalize)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
