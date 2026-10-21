#!/usr/bin/env bash
# Reliable ordered transport name.
reliable_transport() { printf "%s\n" "TCP"; }

# Best-effort datagram transport.
datagram_transport() { printf "%s\n" "UDP"; }

# First packet flag client sends in TCP handshake.
tcp_first_flag() { printf "%s\n" "SYN"; }
