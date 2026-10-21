#!/usr/bin/env bash
# First troubleshoot layer/focus.
first_troubleshoot_layer() { printf "%s\n" "local"; }

# After local L3, check this naming system.
after_l3_check() { printf "%s\n" "DNS"; }

# Prove a listener exists with.
prove_listener_with() { printf "%s\n" "ss"; }
