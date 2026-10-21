#!/usr/bin/env bash
# Postmortem must include (kebab).
postmortem_must_include() { printf "%s\n" "root-cause"; }

# Include timeline? yes/no.
postmortem_timeline() { printf "%s\n" "yes"; }

# Include verification steps? yes/no.
postmortem_verify() { printf "%s\n" "yes"; }
