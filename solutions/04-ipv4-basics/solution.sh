#!/usr/bin/env bash
is_private() { case "$1" in 10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) echo yes ;; *) echo no ;; esac; }
