#!/usr/bin/env bash
# HTTP path-based balancing layer.
http_path_balancing_layer() { printf "%s\n" "L7"; }

# TCP/UDP port-only balancing layer.
port_only_balancing_layer() { printf "%s\n" "L4"; }

# Probe that removes bad backends.
backend_probe_name() { printf "%s\n" "health-check"; }
