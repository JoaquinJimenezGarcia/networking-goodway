#!/usr/bin/env bash
# Linux command to ask which route a destination would take (three words).
cmd_route_get() { printf "%s\n" "ip route get"; }

# Show addresses briefly (two words).
cmd_addr_brief() { printf "%s\n" "ip -br addr"; }

# Show link layer devices (two words).
cmd_link_show() { printf "%s\n" "ip link"; }
