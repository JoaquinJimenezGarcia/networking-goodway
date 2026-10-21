#!/usr/bin/env bash
# Capstone needs a.
capstone_needs() { printf "%s\n" "diagram"; }

# Document addressing plan? yes/no.
need_address_plan() { printf "%s\n" "yes"; }

# Prove east-west and north-south paths? yes/no.
prove_paths() { printf "%s\n" "yes"; }
