#!/usr/bin/env bash
# ASN expands to (kebab).
asn_means() { printf "%s\n" "autonomous-system-number"; }

# Protocol that exchanges routes between ASes.
as_route_protocol() { printf "%s\n" "BGP"; }

# IP blocks announced by ASes are called.
ip_block_name() { printf "%s\n" "prefixes"; }
