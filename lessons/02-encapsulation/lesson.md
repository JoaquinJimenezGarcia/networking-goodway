---
title: "02. Encapsulation, Headers, and MTU"
---

# 02. Encapsulation, Headers, and MTU

**Phase:** Phase 1 — Models and packets  
**Estimated time:** 1–2 days  
**Slug:** `02-encapsulation`

## Learning objectives

- Explain encapsulation/decapsulation
- Define MTU and fragmentation issues
- Use ping to probe path MTU ideas
- Recognize common header sizes intuitively

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Encapsulation

Each layer wraps the payload from above:

```text
[Eth][IP][TCP][HTTP data........]
```

## MTU

Maximum payload size on a link (Ethernet often 1500). Too-large packets may fragment or drop (especially with VPN overhead).

```bash
# Linux: show interface MTU
ip link show
# Probe large ping (may need root / may be blocked)
ping -c 2 -M do -s 1472 1.1.1.1    # Linux DF bit
ping -c 2 -D -s 1472 1.1.1.1       # macOS-style
```

## tcpdump glimpse

```bash
sudo tcpdump -ni any -c 5 icmp
sudo tcpdump -ni eth0 -c 5 host example.com and port 443
```

## Common mistakes

- Ignoring MTU after adding VPN/overlays
- Blackhole path MTU (DF set, ICMP blocked)
- Capturing on the wrong interface

## Exercises

Work in `exercises/02-encapsulation/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/02-encapsulation/` until after an honest attempt.**

## Self-check

1. What does MTU mean?
2. Why do VPNs lower effective MTU?
3. Name a capture tool

## Further reading

- https://www.rfc-editor.org/rfc/rfc1191
