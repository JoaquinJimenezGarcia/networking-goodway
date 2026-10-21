#!/usr/bin/env bash
# What ARP maps.
arp_maps() { printf "%s\n" "IP-to-MAC"; }

# Does ARP cross routers? yes/no.
arp_crosses_routers() { printf "%s\n" "no"; }

# Modern Linux neighbor command (two words).
linux_neigh_cmd() { printf "%s\n" "ip neigh"; }
