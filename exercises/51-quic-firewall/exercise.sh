#!/usr/bin/env bash
# HTTP/3 uses UDP port.
http3_uses_udp_port() { printf "%s\n" ""; }

# Middleboxes that assume only TCP 443 may break.
broken_by_tcp_assume() { printf "%s\n" ""; }

# Allowlisting only TCP can block.
allowlist_tcp_blocks() { printf "%s\n" ""; }
