#!/usr/bin/env bash
# curl flag for headers/response line only.
curl_head_flag() { printf "%s\n" "-I"; }

# Write-out variable for HTTP status.
curl_status_var() { printf "%s\n" "%{http_code}"; }

# Follow redirects flag.
curl_follow_flag() { printf "%s\n" "-L"; }
