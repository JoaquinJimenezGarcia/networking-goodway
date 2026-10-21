#!/usr/bin/env bash
# yes/no if address is RFC1918-ish private (simplified).
is_private() { printf "%s\n" ""; }

# Loopback CIDR taught in the lesson.
loopback_cidr() { printf "%s\n" ""; }

# Link-local / APIPA prefix.
link_local_prefix() { printf "%s\n" ""; }
