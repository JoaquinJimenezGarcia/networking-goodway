#!/usr/bin/env bash
# mTLS expands to (kebab).
mtls_means() { printf "%s\n" "mutual-TLS"; }

# Both peers present a.
mtls_both_present() { printf "%s\n" "certificate"; }

# Service identity often bound to.
service_identity_bound_to() { printf "%s\n" "certificate"; }
