#!/usr/bin/env bash
# Latency better reported as.
latency_better_as() { printf "%s\n" "percentiles"; }

# Three pillars often listed with metrics/logs/?.
third_obs_pillar() { printf "%s\n" "traces"; }

# Synthetic check synonym.
synthetic_check_name() { printf "%s\n" "probe"; }
