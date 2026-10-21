#!/usr/bin/env bash
# L3 proof tool.
l3_proof_tool() { printf "%s\n" "ping"; }

# L4 connect check tool.
l4_proof_tool() { printf "%s\n" "nc"; }

# Name resolution proof tool.
dns_proof_tool() { printf "%s\n" "dig"; }
