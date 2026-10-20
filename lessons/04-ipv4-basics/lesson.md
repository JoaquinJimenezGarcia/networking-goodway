---
title: "04. IPv4 Basics: Addresses, Classes Myth, Private Ranges"
---

# 04. IPv4 Basics: Addresses, Classes Myth, Private Ranges

**Phase:** Phase 2 — Addressing and subnets  
**Estimated time:** 1–2 days  
**Slug:** `04-ipv4-basics`

## Learning objectives

- Read IPv4 addresses and dotted decimal
- Know RFC1918 private ranges
- Explain public vs private vs loopback
- Use commands to show addresses on a host

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Special addresses

| Range | Meaning |
|-------|---------|
| 127.0.0.0/8 | loopback |
| 10.0.0.0/8 | private |
| 172.16.0.0/12 | private |
| 192.168.0.0/16 | private |
| 169.254.0.0/16 | link-local (APIPA) |
| 0.0.0.0/0 | default route |

```bash
# Linux
ip -4 addr show
ip route show
# macOS
ipconfig getifaddr en0
route -n get default
# both
ping -c 2 127.0.0.1
```

## Check public IP (from host)

```bash
curl -4 ifconfig.me
curl -4 https://api.ipify.org
dig +short myip.opendns.com @resolver1.opendns.com
```

## Common mistakes

- Assuming classful addressing still rules the internet
- Using public IPs on lab LANs carelessly
- Confusing link-local with routable

## Exercises

Work in `exercises/04-ipv4-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/04-ipv4-basics/` until after an honest attempt.**

## Self-check

1. Name three private ranges
2. What is 127.0.0.1?
3. How print IPv4 addresses on Linux?

## Further reading

- https://www.rfc-editor.org/rfc/rfc1918
