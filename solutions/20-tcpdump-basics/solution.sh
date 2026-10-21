#!/usr/bin/env bash
# BPF filter for DNS.
tcpdump_dns_filter() { printf "%s\n" "port 53"; }

# tcpdump flag to avoid name resolution.
tcpdump_numeric_flag() { printf "%s\n" "-n"; }

# Write packets to file flag.
tcpdump_write_flag() { printf "%s\n" "-w"; }
