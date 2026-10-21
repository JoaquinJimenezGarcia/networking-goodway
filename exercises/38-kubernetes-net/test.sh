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
  assert_eq "$(k8s_cluster_dns)" "CoreDNS"
  assert_eq "$(k8s_stable_vip_object)" "Service"
  assert_eq "$(k8s_policy_sidecar_mesh)" "mesh"
}
run_tests
echo "Passed $pass failed $fail"
[[ "$fail" -eq 0 ]]
