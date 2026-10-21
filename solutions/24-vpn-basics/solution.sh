#!/usr/bin/env bash
# VPNs often lower this.
vpn_often_lowers() { printf "%s\n" "MTU"; }

# Popular modern VPN that uses UDP usually.
modern_vpn_example() { printf "%s\n" "WireGuard"; }

# Classic site-to-site VPN suite acronym.
classic_vpn_suite() { printf "%s\n" "IPsec"; }
