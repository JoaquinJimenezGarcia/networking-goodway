---
title: "48. Lab: Build a Mini Network Path"
---

# 48. Lab: Build a Mini Network Path

**Phase:** Phase 0 — Orientation  
**Estimated time:** 2 days  
**Slug:** `48-lab-packet`

## Learning objectives

- Connect two VMs via private network
- Set addresses/routes manually
- Verify with ping/curl/tcpdump
- Document the path

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Suggested lab:

1. VM A `10.10.0.1/24`, VM B `10.10.0.2/24`
2. `ping` both ways
3. Run `python3 -m http.server 8080` on B; `curl` from A
4. `tcpdump` the handshake
5. Add a third "router" VM later for multi-hop

```bash
sudo ip addr add 10.10.0.1/24 dev eth1
sudo ip link set eth1 up
ping -c 3 10.10.0.2
```

## Common mistakes

- Using public internet for first labs
- No snapshots before routing experiments
- Overlapping subnets

## Exercises

Work in `exercises/48-lab-packet/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/48-lab-packet/` until after an honest attempt.**

## Self-check

1. What proves L3 connectivity?
2. How prove HTTP path?
3. Why tcpdump?

## Further reading

- https://netdevops.me/
