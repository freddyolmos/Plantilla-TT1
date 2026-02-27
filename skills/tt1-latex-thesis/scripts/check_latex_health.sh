#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-.}"
LOG_FILE="${ROOT_DIR%/}/tmp_latex_health.log"

pushd "$ROOT_DIR" >/dev/null

if ! command -v latexmk >/dev/null 2>&1; then
  echo "ERROR: latexmk is not installed."
  popd >/dev/null
  exit 2
fi

set +e
latexmk -pdf -interaction=nonstopmode main.tex >"$LOG_FILE" 2>&1
LATEX_EXIT=$?
set -e

SCAN_LOG="main.log"
if [[ ! -f "$SCAN_LOG" ]]; then
  SCAN_LOG="$LOG_FILE"
fi

HAS_ERROR=0

if rg -n "^! LaTeX Error:" "$SCAN_LOG" >/dev/null 2>&1; then
  HAS_ERROR=1
  echo "LaTeX errors:" 
  rg -n "^! LaTeX Error:" "$SCAN_LOG"
fi

UNDEF_PATTERNS='Citation .* undefined|Reference .* undefined|There were undefined references|There were undefined citations'
if rg -n "$UNDEF_PATTERNS" "$SCAN_LOG" >/dev/null 2>&1; then
  HAS_ERROR=1
  echo "Undefined references/citations:"
  rg -n "$UNDEF_PATTERNS" "$SCAN_LOG"
fi

if [[ "$LATEX_EXIT" -ne 0 || "$HAS_ERROR" -ne 0 ]]; then
  echo "FAIL: see $LOG_FILE"
  popd >/dev/null
  exit 1
fi

echo "OK: LaTeX build and reference checks passed."
rm -f "$LOG_FILE"
popd >/dev/null
