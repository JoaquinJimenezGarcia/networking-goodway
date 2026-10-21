#!/usr/bin/env bash
# Safe default inbound policy.
safe_default_inbound() { printf "%s\n" "deny"; }

# Modern Linux firewall framework.
linux_fw_modern() { printf "%s\n" "nftables"; }

# Ubuntu-friendly firewall frontend.
ubuntu_fw_frontend() { printf "%s\n" "ufw"; }
