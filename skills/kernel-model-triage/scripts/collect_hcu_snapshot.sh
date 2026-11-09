#!/usr/bin/env bash
set -u
umask 077

raw_identifiers=0
if [ "${1:-}" = "--raw-identifiers" ]; then
  raw_identifiers=1
  shift
fi
if [ "$#" -ne 0 ]; then
  printf 'Usage: %s [--raw-identifiers]\n' "$0" >&2
  exit 2
fi

section() {
  printf '\n## %s\n\n' "$1"
}

run_if_present() {
  local command_name="$1"
  shift
  if command -v "$command_name" >/dev/null 2>&1; then
    printf '```text\n'
    "$@" 2>&1 || true
    printf '```\n'
  else
    printf 'NOT_AVAILABLE: %s\n' "$command_name"
  fi
}

section "Snapshot metadata"
printf 'timestamp: %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
if [ "${raw_identifiers}" -eq 1 ]; then
  printf 'hostname: %s\n' "$(hostname 2>/dev/null || printf unknown)"
  printf 'user: %s\n' "$(id -un 2>/dev/null || printf unknown)"
  printf 'identifier_mode: RAW_SENSITIVE\n'
else
  printf 'hostname: REDACTED\nuser: REDACTED\nidentifier_mode: redacted_default\n'
fi

section "Host"
if [ "${raw_identifiers}" -eq 1 ]; then
  run_if_present uname uname -a
else
  run_if_present uname uname -srm
fi
run_if_present lscpu lscpu
run_if_present numactl numactl --hardware

section "HCU inventory"
if command -v hy-smi >/dev/null 2>&1; then
  hy_smi_queries=("--showproductname" "--showcunum" "--showmeminfo vram" "--showbus" "--showdriverversion" "--showtoponuma" "--showtopo")
  if [ "${raw_identifiers}" -eq 1 ]; then
    hy_smi_queries+=("--showhw")
  fi
  for args in "${hy_smi_queries[@]}"; do
    printf '### hy-smi %s\n\n```text\n' "$args"
    # shellcheck disable=SC2086
    hy-smi $args 2>&1 || true
    printf '```\n'
  done
else
  printf 'NOT_AVAILABLE: hy-smi\n'
fi

section "Compiler and runtime"
run_if_present hipcc hipcc --version
if command -v python3 >/dev/null 2>&1; then
  printf '```text\n'
  python3 - <<'PY' 2>&1 || true
try:
    import torch
    print("torch:", torch.__version__)
    print("torch.version.hip:", torch.version.hip)
    print("device_count:", torch.cuda.device_count())
    for index in range(torch.cuda.device_count()):
        prop = torch.cuda.get_device_properties(index)
        fields = {
            "name": getattr(prop, "name", None),
            "total_memory": getattr(prop, "total_memory", None),
            "multi_processor_count": getattr(prop, "multi_processor_count", None),
            "gcnArchName": getattr(prop, "gcnArchName", None),
            "warp_size": getattr(prop, "warp_size", None),
        }
        print(index, fields)
except Exception as exc:
    print("torch_probe_error:", repr(exc))
PY
  printf '```\n'
else
  printf 'NOT_AVAILABLE: python3\n'
fi

section "Curated execution variables"
for name in \
  HIP_VISIBLE_DEVICES ROCR_VISIBLE_DEVICES PYTORCH_ROCM_ARCH \
  OMP_NUM_THREADS MKL_NUM_THREADS OPENBLAS_NUM_THREADS NUMEXPR_NUM_THREADS \
  OPENCV_FOR_THREADS_NUM MIOPEN_FIND_MODE PYTORCH_MIOPEN_SUGGEST_NHWC \
  TORCH_LOGS TORCHDYNAMO_DISABLE; do
  if [ "${!name+x}" = x ]; then
    printf '%s=%s\n' "$name" "${!name}"
  else
    printf '%s=UNSET\n' "$name"
  fi
done

section "Container context"
if [ -f /.dockerenv ]; then
  printf 'inside_container: true\n'
else
  printf 'inside_container: false\n'
fi
if command -v docker >/dev/null 2>&1; then
  run_if_present docker docker version
fi
