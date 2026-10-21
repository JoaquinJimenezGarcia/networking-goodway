#!/usr/bin/env bash
# Common ss flags for TCP/UDP listen with process.
ss_listen_flags() { printf "%s\n" ""; }

# Older command still seen on some systems.
legacy_netstat() { printf "%s\n" ""; }

# Which tool maps sockets to processes by name often with -i/:port.
files_ports_tool() { printf "%s\n" ""; }
