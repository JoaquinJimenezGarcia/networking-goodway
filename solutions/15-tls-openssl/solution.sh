#!/usr/bin/env bash
# openssl x509 flag showing validity dates.
openssl_dates_flag() { printf "%s\n" "-dates"; }

# Why pass -servername to s_client (acronym).
sni_acronym() { printf "%s\n" "SNI"; }

# Certificate field listing hostnames (acronym).
san_acronym() { printf "%s\n" "SAN"; }
