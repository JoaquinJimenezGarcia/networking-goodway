#!/usr/bin/env bash
# Ping exactly three probes (two-token form).
ping_three() { printf "%s\n" "ping -c 3"; }

# Tool that shows per-hop latency along a path.
path_hop_tool() { printf "%s\n" "traceroute"; }

# Continuous ping+loss tool often used by operators.
loss_path_tool() { printf "%s\n" "mtr"; }
