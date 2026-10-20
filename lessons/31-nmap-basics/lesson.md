---
title: "31. Scanning Basics with nmap (Lab Only)"
---

# 31. Scanning Basics with nmap (Lab Only)

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1–2 days  
**Slug:** `31-nmap-basics`

## Learning objectives

- Scan ports ethically in labs
- Interpret open/closed/filtered
- Use service version detection carefully
- Never scan without authorization

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

**Only scan networks you own or have written permission to test.**

```bash
nmap -sn 192.168.1.0/24                 # ping sweep (lab)
nmap -sT -p 22,80,443 192.168.1.10
nmap -sV -p 443 example.com             # version detect
nmap -sU -p 53 192.168.1.1              # UDP (noisy/slow)
nmap -oA labscan 192.168.1.10           # output basename
```

filtered ≠ closed. Firewalls create ambiguity.

## Common mistakes

- Scanning the internet 'for practice'
- Aggressive scans on fragile devices
- Ignoring legal/ToS boundaries

## Exercises

Work in `exercises/31-nmap-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/31-nmap-basics/` until after an honest attempt.**

## Self-check

1. When is scanning legal?
2. open vs filtered?
3. -sV meaning?

## Further reading

- https://nmap.org/book/man.html
