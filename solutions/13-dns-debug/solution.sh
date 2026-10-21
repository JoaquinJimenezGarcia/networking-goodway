#!/usr/bin/env bash
# What NXDOMAIN means (kebab).
nxdomain_means() { printf "%s\n" "name-not-exist"; }

# Likely meaning of SERVFAIL (kebab).
servfail_means() { printf "%s\n" "resolver-error"; }

# Different answers inside vs outside VPN is called (kebab).
split_dns_name() { printf "%s\n" "split-horizon"; }
