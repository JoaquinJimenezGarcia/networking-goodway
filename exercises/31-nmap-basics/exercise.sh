#!/usr/bin/env bash
# nmap scanning requires this.
nmap_requires() { printf "%s\n" ""; }

# Common quick connect-scan flag set often taught as -sT or -sS; return sS for SYN.
nmap_syn_flag() { printf "%s\n" ""; }

# Version detection flag.
nmap_version_flag() { printf "%s\n" ""; }
