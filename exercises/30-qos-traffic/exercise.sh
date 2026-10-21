#!/usr/bin/env bash
# curl write-out closest to TTFB.
curl_ttfb_var() { printf "%s\n" ""; }

# Write-out for DNS phase.
curl_dns_time_var() { printf "%s\n" ""; }

# Latency SLOs prefer this summary statistic.
latency_summary_stat() { printf "%s\n" ""; }
