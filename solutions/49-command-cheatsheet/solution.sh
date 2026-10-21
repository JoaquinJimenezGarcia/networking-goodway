#!/usr/bin/env bash
# Daily tool count minimum from consolidation drill.
daily_tool_count_min() { printf "%s\n" "8"; }

# Must include packet capture tool.
capture_tool() { printf "%s\n" "tcpdump"; }

# Must include HTTP client.
http_client_tool() { printf "%s\n" "curl"; }
