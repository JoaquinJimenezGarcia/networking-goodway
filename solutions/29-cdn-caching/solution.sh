#!/usr/bin/env bash
# Primary HTTP caching header.
header_for_caching() { printf "%s\n" "Cache-Control"; }

# CDN role in one word.
cdn_role() { printf "%s\n" "cache"; }

# Validation header often paired with caches.
cache_validator_header() { printf "%s\n" "ETag"; }
