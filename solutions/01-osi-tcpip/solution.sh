#!/usr/bin/env bash
# OSI/TCPIP layer where TCP/UDP ports live.
layer_for_ports() { printf "%s\n" "L4"; }

# Layer for MAC addresses.
layer_for_mac() { printf "%s\n" "L2"; }

# Layer for HTTP.
layer_for_http() { printf "%s\n" "L7"; }

# TLS commonly rides on this transport (classic HTTPS).
tls_rides_on() { printf "%s\n" "TCP"; }
