---
title: "08. ping, traceroute/mtr, and Path Diagnosis"
---

# 08. ping, traceroute/mtr, and Path Diagnosis

**Phase:** Phase 3 — Host networking toolkit  
**Estimated time:** 1–2 days  
**Slug:** `08-ping-traceroute`

## Learning objectives

- Use ping meaningfully (and know its limits)
- Read traceroute hops
- Use mtr for combined view
- Distinguish loss at hop vs destination

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
ping -c 5 1.1.1.1
ping -c 5 -W 1 example.com          # timeout per probe (Linux)
ping -c 5 -t 1 example.com          # macOS timeout seconds

traceroute example.com
traceroute -n example.com           # numeric, no DNS delay
# Linux often:
tracepath example.com

# Best interactive tool if installed:
mtr -rwzc 50 example.com
mtr -6 example.com
```

**ICMP may be rate-limited or blocked.** Failed ping ≠ host down. Correlate with TCP checks (`curl`, `nc`).

```bash
# TCP-aware path tools (if installed)
tcptraceroute example.com 443
```

## Common mistakes

- Declaring outage from a single ping fail
- Misreading traceroute stars as always "down"
- No DNS-less (`-n`) when DNS is broken

## Exercises

Work in `exercises/08-ping-traceroute/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/08-ping-traceroute/` until after an honest attempt.**

## Self-check

1. Why ping can lie?
2. What does mtr combine?
3. Why traceroute -n?

## Further reading

- https://www.rfc-editor.org/rfc/rfc792
