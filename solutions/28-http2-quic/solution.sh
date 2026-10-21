#!/usr/bin/env bash
# curl write-out for HTTP version.
curl_http_version_writeout() { printf "%s\n" "%{http_version}"; }

# HTTP/3 transport protocol name.
http3_transport() { printf "%s\n" "QUIC"; }

# HTTP/3 typical UDP port.
http3_udp_port() { printf "%s\n" "443"; }
