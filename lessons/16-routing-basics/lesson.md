---
title: "16. Routing Tables and Default Gateways"
---

# 16. Routing Tables and Default Gateways

**Phase:** Phase 6 — Routing  
**Estimated time:** 1–2 days  
**Slug:** `16-routing-basics`

## Learning objectives

- Read a routing table
- Explain longest-prefix match
- Find default gateway
- Use ip route get / route get

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Linux
ip route
ip route show table main
ip route get 1.1.1.1
ip route get 10.0.0.5 from 10.0.0.10 iif eth0

# macOS
netstat -rn
route -n get default
route -n get 1.1.1.1
```

**Longest prefix match**: more specific routes win (`10.0.1.0/24` over `10.0.0.0/8`).

## Common mistakes

- Two default routes without understanding metrics
- Asymmetric routing surprises
- Deleting default route remotely without console

## Exercises

Work in `exercises/16-routing-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/16-routing-basics/` until after an honest attempt.**

## Self-check

1. What is 0.0.0.0/0?
2. What wins: /8 or /24?
3. Command: which route to 1.1.1.1?

## Further reading

- https://man7.org/linux/man-pages/man8/ip-route.8.html
