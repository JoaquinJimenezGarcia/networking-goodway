---
title: "44. Networking Troubleshooting Playbook"
---

# 44. Networking Troubleshooting Playbook

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 2 days  
**Slug:** `44-troubleshooting-playbook`

## Learning objectives

- Apply a layered checklist
- Capture evidence before changing things
- Bisect path: local → LAN → WAN → DNS → TLS → app
- Write crisp incident notes

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Checklist

```bash
# 1) Local
ip -br addr; ip route; scutil --dns 2>/dev/null | head
# 2) L2/L3
ping -c 2 <gw>; ip neigh
# 3) DNS
dig example.com +time=1
# 4) TCP
nc -vz -w 3 example.com 443
# 5) TLS/HTTP
curl -vI --max-time 5 https://example.com
# 6) Capture if needed
sudo tcpdump -ni any -c 50 host example.com
```

Change one variable at a time. Record timestamps.

## Common mistakes

- Shotgun restarts
- No notes
- Skipping DNS

## Exercises

Work in `exercises/44-troubleshooting-playbook/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/44-troubleshooting-playbook/` until after an honest attempt.**

## Self-check

1. First three checks?
2. Why evidence before reboot?
3. Where capture fits?

## Further reading

- https://sre.google/sre-book/
