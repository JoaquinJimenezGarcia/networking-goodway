#!/usr/bin/env bash
# DNS type for IPv6 addresses.
dig_aaaa_type() { printf "%s\n" "AAAA"; }

# IPv6 loopback address.
ipv6_loopback() { printf "%s\n" "::1"; }

# Flag often used with dig for brief answers.
dig_brief_flag() { printf "%s\n" "+short"; }
