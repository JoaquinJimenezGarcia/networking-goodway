#!/usr/bin/env bash
# HTTP 504 often means (kebab).
http_504_often() { printf "%s\n" "upstream-timeout"; }

# HTTP 502 often means (kebab).
http_502_often() { printf "%s\n" "bad-gateway"; }

# Edge pattern terminating TLS then proxying is.
edge_pattern() { printf "%s\n" "reverse-proxy"; }
