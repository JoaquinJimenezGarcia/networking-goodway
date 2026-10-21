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
source "$ROOT/exercise.sh"
run_tests() {
  assert_eq "$(is_private 10.0.0.1)" "yes"
  assert_eq "$(is_private 8.8.8.8)" "no"
  assert_eq "$(loopback_cidr)" "127.0.0.0/8"
  assert_eq "$(link_local_prefix)" "169.254"
}
run_tests
echo "Passed $pass failed $fail"
[[ "$fail" -eq 0 ]]
