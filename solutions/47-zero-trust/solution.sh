#!/usr/bin/env bash
# Zero trust rejects (kebab).
zero_trust_rejects() { printf "%s\n" "location-only-trust"; }

# Prefer verify every request: yes/no.
verify_every_request() { printf "%s\n" "yes"; }

# Identity over network location: identity/location?
prefer_identity_or_location() { printf "%s\n" "identity"; }
