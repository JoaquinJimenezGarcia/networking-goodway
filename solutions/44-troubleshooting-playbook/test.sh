#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
pass=0
fail=0
assert_eq() {
  local got=$1 want=$2 msg=${3:-}
  if [[ "$got" == "$want" ]]; then
    pass=$((pass + 1))
  else
    echo "FAIL $msg: got='$got' want='$want'" >&2
    fail=$((fail + 1))
  fi
}
# shellcheck disable=SC1091
source "$ROOT/solution.sh"
run_tests() {
  assert_eq "$(first_troubleshoot_layer)" "local"
}
run_tests
echo "Passed $pass failed $fail"
[[ "$fail" -eq 0 ]]
