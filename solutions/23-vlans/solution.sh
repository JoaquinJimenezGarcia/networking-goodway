#!/usr/bin/env bash
# VLAN tagging standard.
vlan_tag_standard() { printf "%s\n" "802.1Q"; }

# Port carrying multiple VLANs is a.
multi_vlan_port() { printf "%s\n" "trunk"; }

# Broadcast domain separation feature name.
l2_segment_feature() { printf "%s\n" "VLAN"; }
