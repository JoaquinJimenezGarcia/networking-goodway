#!/usr/bin/env bash
# dig option for brief answers.
dig_short_flags() { printf "%s\n" "+short"; }

# Record type for IPv4.
dns_type_a() { printf "%s\n" "A"; }

# Record type for mail exchangers.
dns_type_mx() { printf "%s\n" "MX"; }
