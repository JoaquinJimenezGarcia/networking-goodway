#!/usr/bin/env bash
# IPv4 default route CIDR.
default_route_cidr() { printf "%s\n" "0.0.0.0/0"; }

# Which wins: more-specific /24 or /8? answer /24 or /8.
longest_prefix_wins() { printf "%s\n" "/24"; }

# Linux command words to resolve route for a dest.
linux_route_get() { printf "%s\n" "ip route get"; }
