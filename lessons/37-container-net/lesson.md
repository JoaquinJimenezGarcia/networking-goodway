---
title: "37. Container Networking: Bridge, CNI, localhost Traps"
---

# 37. Container Networking: Bridge, CNI, localhost Traps

**Phase:** Phase 12 — Cloud, containers, and modern nets  
**Estimated time:** 2 days  
**Slug:** `37-container-net`

## Learning objectives

- Explain docker bridge basics
- Publish ports correctly
- Debug DNS inside containers
- Avoid localhost confusion

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
docker network ls
docker run --rm curlimages/curl:latest curl -4 -I https://example.com
docker run --rm -p 8080:80 nginx
curl -I http://127.0.0.1:8080

# inspect
docker network inspect bridge | head
nsenter tips / ip netns (advanced Linux)
```

`localhost` inside a container is the container, not the host. Use host gateway / service names / published ports.

## Common mistakes

- --network host as default
- Assuming container DNS equals host DNS always
- Publishing all ports broadly

## Exercises

Work in `exercises/37-container-net/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/37-container-net/` until after an honest attempt.**

## Self-check

1. localhost in container means?
2. -p 8080:80 meaning?
3. docker network ls purpose?

## Further reading

- https://docs.docker.com/network/
