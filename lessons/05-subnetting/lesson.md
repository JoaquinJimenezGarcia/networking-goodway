---
title: "05. Subnetting and CIDR (with practice)"
---

# 05. Subnetting and CIDR (with practice)

**Phase:** Phase 2 — Addressing and subnets  
**Estimated time:** 2–3 days  
**Slug:** `05-subnetting`

## Learning objectives

- Convert prefix lengths to masks
- Compute network/broadcast/usable hosts
- Choose subnets for labs
- Use `ipcalc`/`sipcalc` or manual method

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## CIDR quick facts

`192.168.10.0/24` → mask `255.255.255.0` → 256 addresses → 254 usable (typical).

Host bits = 32 - prefix. Usable ≈ 2^hostbits − 2 (except some special cases).

```bash
# If installed
ipcalc 192.168.10.0/24
sipcalc 10.0.0.0/12

# Python one-liner helper (lab)
python3 - <<'PY'
import ipaddress
n=ipaddress.ip_network('192.168.10.0/24')
print(n.network_address, n.broadcast_address, n.num_addresses)
PY
```

## Common prefixes

| Prefix | Hosts (approx usable) | Typical use |
|--------|-----------------------|-------------|
| /32 | 1 | single host route |
| /30 | 2 | point-to-point |
| /24 | 254 | small LAN |
| /16 | ~65k | large private |
| /0 | default | everything |

## Common mistakes

- Off-by-one in usable host counts
- Overlapping subnets in VPCs
- Using /24 everywhere without design

## Exercises

Work in `exercises/05-subnetting/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/05-subnetting/` until after an honest attempt.**

## Self-check

1. How many host bits in /26?
2. What does /32 mean?
3. Why avoid overlapping CIDRs?

## Further reading

- https://www.rfc-editor.org/rfc/rfc4632
