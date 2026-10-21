#!/usr/bin/env bash
# Packet drop often looks like.
packet_drop_often_looks_like() { printf "%s\n" "timeout"; }

# AWS SG statefulness: stateful or stateless?
sg_statefulness() { printf "%s\n" "stateful"; }

# NACL statefulness: stateful or stateless?
nacl_statefulness() { printf "%s\n" "stateless"; }
