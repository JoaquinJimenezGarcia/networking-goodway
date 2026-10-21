#!/usr/bin/env bash
# Host bits for a prefix length /N.
host_bits() { printf "%s\n" "$((32 - $1))"; }

# Usable hosts estimate for /24 (2^8-2).
usable_hosts_24() { printf "%s\n" "254"; }

# Does longer prefix mean smaller or larger network? smaller/larger.
longer_prefix_means() { printf "%s\n" "smaller"; }
