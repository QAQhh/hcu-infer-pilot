#!/usr/bin/env bash
#
# Install all maintained DCU-Infer-Pilot skills.
#
# By default this installs to Codex:
#   ${CODEX_HOME:-$HOME/.codex}/skills
#
# The script installs the skills maintained by this repository and skips
# vendored/example skills embedded under cookbook or evidence snapshots.
#
# Usage:
#   ./install_all_skills.sh
#   ./install_all_skills.sh --target codex
#   ./install_all_skills.sh --target claude
#   ./install_all_skills.sh --target both
#   ./install_all_skills.sh --copy --force
#   ./install_all_skills.sh --dry-run

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
REPO_ROOT="${REPO_ROOT:-$SCRIPT_DIR}"

TARGET="codex"
MODE="symlink"
FORCE="false"
DRY_RUN="false"

CODEX_SKILLS_DIR="${CODEX_SKILLS_DIR:-${CODEX_HOME:-${HOME}/.codex}/skills}"
CLAUDE_SKILLS_DIR="${CLAUDE_SKILLS_DIR:-${HOME}/.claude/skills}"

HUMANIZE_ROOT="${REPO_ROOT}/skills/lightop-skills/humanize"
HUMANIZE_SKILLS_ROOT="${HUMANIZE_ROOT}/skills"
KERNELPILOT_ROOT="${REPO_ROOT}/skills/lightop-skills"

REGULAR_SKILLS=(
  "llm-serving-auto-benchmark|${REPO_ROOT}/skills/llm-serving-auto-benchmark"
  "llm-torch-profiler-analysis|${REPO_ROOT}/skills/llm-torch-profiler-analysis"
  "model-architecture-diagram|${REPO_ROOT}/skills/model-architecture-diagram"
  "model-compute-simulation|${REPO_ROOT}/skills/model-compute-simulation"
  "sglang-prod-incident-triage|${REPO_ROOT}/skills/sglang-prod-incident-triage"
  "sglang-sota-humanize-loop|${REPO_ROOT}/skills/sglang-sota-humanize-loop"
  "vllm-pr-summary|${REPO_ROOT}/skills/vllm-pr-summary"
  "model-pr-optimization-history|${REPO_ROOT}/model-pr-optimization-history"
  "model-pr-optimization-hg-history|${REPO_ROOT}/model-pr-optimization-hg-history"
  "lightop-kernel-knowledge|${REPO_ROOT}/skills/lightop-skills/knowledge"
  "hcu-aiter-moe-tuning|${REPO_ROOT}/skills/hcu-aiter-moe-tuning"
  "kb-update|${REPO_ROOT}/skills/kb-update"
  "kb-ingest|${REPO_ROOT}/skills/kb-ingest"
  "kb-search|${REPO_ROOT}/skills/kb-search"
  "hipblaslt-rocblas-tuning|${REPO_ROOT}/skills/hipblaslt-rocblas-tuning"
)

HUMANIZE_SKILLS=(
  "ask-codex|ask-codex"
  "ask-gemini|ask-gemini"
  "humanize|humanize"
  "humanize-gen-plan|humanize-gen-plan"
  "humanize-refine-plan|humanize-refine-plan"
  "humanize-rlcr|humanize-rlcr"
  "lightop-kernel-agent-loop|humanize-kernel-agent-loop"
  "dcu-profiler-report|ncu-report"
)

usage() {
  cat <<'EOF'
Install all maintained DCU-Infer-Pilot skills.

Usage:
  install_all_skills.sh [options]

Options:
  --target MODE             codex|claude|both (default: codex)
  --codex-skills-dir PATH   Codex skills dir (default: ${CODEX_HOME:-~/.codex}/skills)
  --claude-skills-dir PATH  Claude skills dir (default: ~/.claude/skills)
  --repo-root PATH          DCU-Infer-Pilot root (default: script directory)
  --link                    Install regular skills as symlinks (default)
  --copy                    Copy regular skills instead of symlinking
  --force                   Replace existing target skill directories/symlinks
  --dry-run                 Print actions without writing
  -h, --help                Show this help

Installed skills:
  llm-serving-auto-benchmark
  llm-torch-profiler-analysis
  model-architecture-diagram
  model-compute-simulation
  sglang-prod-incident-triage
  sglang-sota-humanize-loop
  vllm-pr-summary
  model-pr-optimization-history
  model-pr-optimization-hg-history
  lightop-kernel-knowledge
  hcu-aiter-moe-tuning
  kb-update
  kb-ingest
  kb-search
  hipblaslt-rocblas-tuning
  ask-codex
  ask-gemini
  humanize
  humanize-gen-plan
  humanize-refine-plan
  humanize-rlcr
  lightop-kernel-agent-loop
  dcu-profiler-report

Notes:
  - Vendored/example skills under cookbook and evidence snapshots are skipped.
  - Humanize skills are always copied and hydrated so command paths point to
    the installed runtime bundle.
EOF
}

log() {
  printf '[install-DCU-Infer-Pilot] %s\n' "$*"
}

die() {
  printf '[install-DCU-Infer-Pilot] Error: %s\n' "$*" >&2
  exit 1
}

resolve_repo_root() {
  REPO_ROOT="$(cd "$REPO_ROOT" 2>/dev/null && pwd || true)"
  [[ -n "$REPO_ROOT" ]] || die "could not resolve repo root"
  [[ -f "${REPO_ROOT}/README.md" ]] || die "README.md not found under repo root: $REPO_ROOT"

  HUMANIZE_ROOT="${REPO_ROOT}/skills/lightop-skills/humanize"
  HUMANIZE_SKILLS_ROOT="${HUMANIZE_ROOT}/skills"
  KERNELPILOT_ROOT="${REPO_ROOT}/skills/lightop-skills"

  REGULAR_SKILLS=(
    "llm-serving-auto-benchmark|${REPO_ROOT}/skills/llm-serving-auto-benchmark"
    "llm-torch-profiler-analysis|${REPO_ROOT}/skills/llm-torch-profiler-analysis"
    "model-architecture-diagram|${REPO_ROOT}/skills/model-architecture-diagram"
    "model-compute-simulation|${REPO_ROOT}/skills/model-compute-simulation"
    "sglang-prod-incident-triage|${REPO_ROOT}/skills/sglang-prod-incident-triage"
    "sglang-sota-humanize-loop|${REPO_ROOT}/skills/sglang-sota-humanize-loop"
    "vllm-pr-summary|${REPO_ROOT}/skills/vllm-pr-summary"
    "model-pr-optimization-history|${REPO_ROOT}/model-pr-optimization-history"
    "model-pr-optimization-hg-history|${REPO_ROOT}/model-pr-optimization-hg-history"
    "lightop-kernel-knowledge|${REPO_ROOT}/skills/lightop-skills/knowledge"
    "hcu-aiter-moe-tuning|${REPO_ROOT}/skills/hcu-aiter-moe-tuning"
    "kb-update|${REPO_ROOT}/skills/kb-update"
    "kb-ingest|${REPO_ROOT}/skills/kb-ingest"
    "kb-search|${REPO_ROOT}/skills/kb-search"
    "hipblaslt-rocblas-tuning|${REPO_ROOT}/skills/hipblaslt-rocblas-tuning"
  )
}

preflight() {
  local entry name src folder

  for entry in "${REGULAR_SKILLS[@]}"; do
    IFS='|' read -r name src <<< "$entry"
    [[ -f "${src}/SKILL.md" ]] || die "missing ${name}: ${src}/SKILL.md"
  done

  for entry in "${HUMANIZE_SKILLS[@]}"; do
    IFS='|' read -r name folder <<< "$entry"
    [[ -f "${HUMANIZE_SKILLS_ROOT}/${folder}/SKILL.md" ]] || die "missing ${name}: ${HUMANIZE_SKILLS_ROOT}/${folder}/SKILL.md"
  done

  for src in scripts hooks prompt-template templates config agents; do
    [[ -d "${HUMANIZE_ROOT}/${src}" ]] || die "missing Humanize runtime dir: ${HUMANIZE_ROOT}/${src}"
  done
}

prepare_target_root() {
  local skills_dir="$1"
  if [[ "$DRY_RUN" == "true" ]]; then
    log "DRY-RUN mkdir -p ${skills_dir}"
  else
    mkdir -p "$skills_dir"
  fi
}

replace_or_skip_target() {
  local target="$1"

  if [[ -e "$target" || -L "$target" ]]; then
    if [[ "$FORCE" != "true" ]]; then
      log "skip existing: ${target} (use --force to replace)"
      return 1
    fi

    if [[ "$DRY_RUN" == "true" ]]; then
      log "DRY-RUN remove existing: ${target}"
    else
      rm -rf "$target"
    fi
  fi

  return 0
}

copy_dir() {
  local src="$1"
  local dst="$2"

  if [[ "$DRY_RUN" == "true" ]]; then
    log "DRY-RUN copy ${src} -> ${dst}"
    return
  fi

  mkdir -p "$(dirname "$dst")"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$src/" "$dst/"
  else
    mkdir -p "$dst"
    cp -a "$src/." "$dst/"
  fi
}

install_regular_skill() {
  local skills_dir="$1"
  local name="$2"
  local src="$3"
  local target="${skills_dir}/${name}"

  if ! replace_or_skip_target "$target"; then
    return 0
  fi

  if [[ "$MODE" == "symlink" ]]; then
    if [[ "$DRY_RUN" == "true" ]]; then
      log "DRY-RUN link ${target} -> ${src}"
    else
      ln -s "$src" "$target"
      log "linked ${name}"
    fi
  else
    copy_dir "$src" "$target"
    log "copied ${name}"
  fi
}

hydrate_file() {
  local src="$1"
  local dst="$2"
  local runtime_root="$3"

  if [[ "$DRY_RUN" == "true" ]]; then
    log "DRY-RUN hydrate ${src} -> ${dst}"
    return
  fi

  mkdir -p "$(dirname "$dst")"
  _HYDRATE_RUNTIME_ROOT="$runtime_root" \
  _HYDRATE_KERNELPILOT_ROOT="$KERNELPILOT_ROOT" \
    awk '{
      gsub(/\{\{HUMANIZE_RUNTIME_ROOT\}\}/, ENVIRON["_HYDRATE_RUNTIME_ROOT"]);
      gsub(/\{\{KERNELPILOT_ROOT\}\}/, ENVIRON["_HYDRATE_KERNELPILOT_ROOT"]);
      print
    }' "$src" > "$dst"
}

install_humanize_runtime() {
  local skills_dir="$1"
  local runtime_target="${skills_dir}/humanize"
  local component

  if [[ "$DRY_RUN" != "true" ]]; then
    mkdir -p "$runtime_target"
  fi

  for component in scripts hooks prompt-template templates config agents; do
    local src="${HUMANIZE_ROOT}/${component}"
    local dst="${runtime_target}/${component}"
    if [[ "$DRY_RUN" == "true" ]]; then
      log "DRY-RUN install Humanize runtime ${component}"
    else
      rm -rf "$dst"
      copy_dir "$src" "$dst"
    fi
  done
}

install_humanize_skill() {
  local skills_dir="$1"
  local name="$2"
  local folder="$3"
  local src="${HUMANIZE_SKILLS_ROOT}/${folder}"
  local target="${skills_dir}/${name}"
  local runtime_root="${skills_dir}/humanize"

  if ! replace_or_skip_target "$target"; then
    return 0
  fi

  if [[ "$DRY_RUN" != "true" ]]; then
    mkdir -p "$target"
  fi

  hydrate_file "${src}/SKILL.md" "${target}/SKILL.md" "$runtime_root"

  log "installed ${name}"
}

install_to_dir() {
  local skills_dir="$1"
  local label="$2"
  local entry name src folder

  log "target: ${label}"
  log "skills dir: ${skills_dir}"
  prepare_target_root "$skills_dir"

  for entry in "${REGULAR_SKILLS[@]}"; do
    IFS='|' read -r name src <<< "$entry"
    install_regular_skill "$skills_dir" "$name" "$src"
  done

  install_humanize_runtime "$skills_dir"

  for entry in "${HUMANIZE_SKILLS[@]}"; do
    IFS='|' read -r name folder <<< "$entry"
    install_humanize_skill "$skills_dir" "$name" "$folder"
  done
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      [[ -n "${2:-}" ]] || die "--target requires a value"
      case "$2" in
        codex|claude|both) TARGET="$2" ;;
        *) die "--target must be codex, claude, or both" ;;
      esac
      shift 2
      ;;
    --codex-skills-dir)
      [[ -n "${2:-}" ]] || die "--codex-skills-dir requires a value"
      CODEX_SKILLS_DIR="$2"
      shift 2
      ;;
    --claude-skills-dir)
      [[ -n "${2:-}" ]] || die "--claude-skills-dir requires a value"
      CLAUDE_SKILLS_DIR="$2"
      shift 2
      ;;
    --repo-root)
      [[ -n "${2:-}" ]] || die "--repo-root requires a value"
      REPO_ROOT="$2"
      shift 2
      ;;
    --link)
      MODE="symlink"
      shift
      ;;
    --copy)
      MODE="copy"
      shift
      ;;
    --force)
      FORCE="true"
      shift
      ;;
    --dry-run)
      DRY_RUN="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
done

resolve_repo_root
preflight

log "repo root: ${REPO_ROOT}"
log "mode: ${MODE}"
log "force: ${FORCE}"
log "dry-run: ${DRY_RUN}"

case "$TARGET" in
  codex)
    install_to_dir "$CODEX_SKILLS_DIR" "codex"
    ;;
  claude)
    install_to_dir "$CLAUDE_SKILLS_DIR" "claude"
    ;;
  both)
    install_to_dir "$CODEX_SKILLS_DIR" "codex"
    install_to_dir "$CLAUDE_SKILLS_DIR" "claude"
    ;;
esac

log "done"
