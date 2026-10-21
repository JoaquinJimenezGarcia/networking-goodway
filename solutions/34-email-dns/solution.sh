#!/usr/bin/env bash
# Mail exchanger DNS record.
mail_dns_record() { printf "%s\n" "MX"; }

# Sender policy framework record purpose acronym.
spf_acronym() { printf "%s\n" "SPF"; }

# Domain alignment reporting framework with DKIM/SPF.
dmarc_acronym() { printf "%s\n" "DMARC"; }
