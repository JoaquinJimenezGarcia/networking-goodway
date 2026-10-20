---
title: "45. Host Network Performance Tuning Intro"
---

# 45. Host Network Performance Tuning Intro

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1–2 days  
**Slug:** `45-performance-tuning`

## Learning objectives

- Inspect RX/TX errors and drops
- Know ephemerial port exhaustion exists
- Tune carefully with evidence
- Relate to ulimit/somaxconn

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
ip -s link
netstat -s | head -50                   # or ss -s
cat /proc/sys/net/ipv4/ip_local_port_range   # Linux
sysctl net.core.somaxconn
ss -s
```

High `CLOSE-WAIT`/`TIME-WAIT`, port range exhaustion, NIC errors — measure first, then tune.

## Common mistakes

- sysctl cargo cult from blogs
- Raising limits hiding leaks
- Ignoring NIC hardware offload/errors

## Exercises

Work in `exercises/45-performance-tuning/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/45-performance-tuning/` until after an honest attempt.**

## Self-check

1. Where see interface drops?
2. Ephemeral ports why?
3. Measure before tune?

## Further reading

- https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
