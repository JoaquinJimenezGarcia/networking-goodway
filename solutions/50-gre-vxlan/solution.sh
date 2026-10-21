#!/usr/bin/env bash
# VXLAN is an.
vxlan_is_an() { printf "%s\n" "overlay"; }

# VXLAN commonly encapsulates over.
vxlan_over() { printf "%s\n" "UDP"; }

# GRE is primarily a.
gre_is_a() { printf "%s\n" "tunnel"; }
