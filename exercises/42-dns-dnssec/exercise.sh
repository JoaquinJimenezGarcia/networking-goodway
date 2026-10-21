#!/usr/bin/env bash
# DNSSEC primarily protects.
dnssec_protects() { printf "%s\n" ""; }

# DNSSEC does not encrypt this property of queries by itself.
dnssec_not_encrypt() { printf "%s\n" ""; }

# Validation failure should not be silently ignored: yes/no.
dnssec_fail_closed_idea() { printf "%s\n" ""; }
