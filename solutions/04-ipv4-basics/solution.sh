#!/usr/bin/env bash
# yes/no if address is RFC1918-ish private (simplified).
is_private() { case "$1" in 10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) echo yes ;; *) echo no ;; esac; }

# Loopback CIDR taught in the lesson.
loopback_cidr() { printf "%s\n" "127.0.0.0/8"; }

# Link-local / APIPA prefix.
link_local_prefix() { printf "%s\n" "169.254"; }
