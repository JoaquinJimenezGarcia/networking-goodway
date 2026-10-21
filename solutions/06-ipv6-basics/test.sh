#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
pass=0
fail=0
assert_eq() {
  # Assign after `local` so values like -n are not parsed as local(1) flags.
  local got want msg
  got=$1
  want=$2
  msg=${3:-}
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
  assert_eq "$(dig_aaaa_type)" "AAAA"
  assert_eq "$(ipv6_loopback)" "::1"
  assert_eq "$(dig_brief_flag)" "+short"
}
run_tests
echo "Passed $pass failed $fail"
[[ "$fail" -eq 0 ]]
