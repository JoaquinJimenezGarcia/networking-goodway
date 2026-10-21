#!/usr/bin/env bash
# localhost inside a container is.
localhost_in_container_is() { printf "%s\n" "the-container"; }

# Default docker network driver often.
docker_default_network() { printf "%s\n" "bridge"; }

# Plugin model name for container networking in k8s ecosystem.
container_net_plugin_model() { printf "%s\n" "CNI"; }
