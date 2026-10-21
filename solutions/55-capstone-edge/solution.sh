#!/usr/bin/env bash
# Edge should terminate.
edge_should_terminate() { printf "%s\n" "TLS"; }

# Forward client IP only from.
forward_ip_from() { printf "%s\n" "trusted-proxies-only"; }

# Health checks must hit.
health_checks_hit() { printf "%s\n" "upstream"; }
