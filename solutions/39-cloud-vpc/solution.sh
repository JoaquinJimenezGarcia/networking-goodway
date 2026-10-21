#!/usr/bin/env bash
# Private subnet egress usually via.
private_subnet_egress_via() { printf "%s\n" "NAT-gateway"; }

# Public subnet internet via.
public_subnet_egress_via() { printf "%s\n" "IGW"; }

# Cloud routing object mapping destinations.
cloud_route_object() { printf "%s\n" "route-table"; }
