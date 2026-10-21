#!/usr/bin/env bash
# nc flags for verbose zero-I/O connect check.
nc_port_check_flags() { printf "%s\n" "-vz"; }

# Example listen on 9090 with nc -l (token).
nc_listen_flag() { printf "%s\n" "-l"; }

# More powerful relay/multipurpose cousin of nc.
swiss_army_relay() { printf "%s\n" "socat"; }
