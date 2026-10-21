#!/usr/bin/env bash
# Anycast means (kebab).
anycast_means() { printf "%s\n" "same-IP-many-places"; }

# DNS often uses anycast for this role.
anycast_dns_role() { printf "%s\n" "resolver"; }

# GeoDNS steers users using mostly.
geodns_steers_with() { printf "%s\n" "DNS"; }
