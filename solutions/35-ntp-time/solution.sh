#!/usr/bin/env bash
# Preferred timezone for logs.
preferred_log_timezone() { printf "%s\n" "UTC"; }

# Protocol that syncs clocks.
time_sync_proto() { printf "%s\n" "NTP"; }

# TLS cert validity depends on correct.
certs_need_correct() { printf "%s\n" "time"; }
