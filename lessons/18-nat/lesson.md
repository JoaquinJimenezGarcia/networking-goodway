---
title: "18. NAT, PAT, and Hairpinning"
---

# 18. NAT, PAT, and Hairpinning

**Phase:** Phase 8 — Firewalls, NAT, and policy  
**Estimated time:** 1–2 days  
**Slug:** `18-nat`

## Learning objectives

- Explain source NAT / PAT for internet egress
- Understand destination NAT / port forwards
- Spot NAT in troubleshooting
- Know hairpin NAT issues

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Home routers rewrite many private IPs to one public IP (**PAT**).

```bash
# On Linux NAT host (lab, nftables/iptables)
sudo iptables -t nat -L -n -v
sudo nft list table nat 2>/dev/null

# See public IP from behind NAT
curl -4 ifconfig.me
```

Symptoms of NAT: inbound connections fail without port forwards; "peer sees wrong address" in VoIP/P2P.

## Common mistakes

- Exposing RDP/SSH via risky UPnP without care
- Overlapping NATed ranges in VPN merges
- Assuming inbound works like outbound

## Exercises

Work in `exercises/18-nat/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/18-nat/` until after an honest attempt.**

## Self-check

1. PAT means?
2. Why inbound fails by default?
3. Table name for iptables NAT?

## Further reading

- https://www.rfc-editor.org/rfc/rfc3022
