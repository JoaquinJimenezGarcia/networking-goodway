#!/usr/bin/env bash
# Prefix when DHCP fails (APIPA).
dhcp_fail_prefix() { printf "%s\n" "169.254"; }

# Protocol that assigns addresses on LAN.
addr_assign_proto() { printf "%s\n" "DHCP"; }

# IPv6 cousin often used instead of DHCPv6 on LANs.
ipv6_autoconfig() { printf "%s\n" "SLAAC"; }
