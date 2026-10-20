---
title: "53. Capstone: Multi-Host Lab Network"
---

# 53. Capstone: Multi-Host Lab Network

**Phase:** Phase 13 — Capstones  
**Estimated time:** 3–5 days  
**Slug:** `53-capstone-lab-net`

## Learning objectives

- Build 3-node lab with routing
- Provide DNS or /etc/hosts strategy
- Serve HTTP via proxy
- Document addressing & runbook

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Mission

- 3 Linux VMs: client, router/proxy, server
- Static IPs + routes
- `curl` from client to service via proxy
- tcpdump evidence of path
- Basic firewall allowing only needed ports
- Written network diagram + runbook

## Rubric

- Correct routing table
- Evidence captures
- Least ports open
- Clean reboot persistence notes

## Common mistakes

- DHCP chaos without notes
- No diagram
- All ports open

## Exercises

Work in `exercises/53-capstone-lab-net/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/53-capstone-lab-net/` until after an honest attempt.**

## Self-check

1. What is the next hop from client?
2. Which ports open?
3. How prove path?

## Further reading

- https://netdevops.me/
