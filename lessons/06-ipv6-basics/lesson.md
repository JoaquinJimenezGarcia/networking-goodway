---
title: "06. IPv6 Basics and Dual-Stack Commands"
---

# 06. IPv6 Basics and Dual-Stack Commands

**Phase:** Phase 2 — Addressing and subnets  
**Estimated time:** 1–2 days  
**Slug:** `06-ipv6-basics`

## Learning objectives

- Read IPv6 addresses and `::` compression
- Know link-local `fe80::/10`
- Query AAAA records
- Test connectivity with ping6/curl -6

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Addresses
ip -6 addr show                 # Linux
ifconfig en0 | grep inet6       # macOS

# DNS AAAA
dig example.com AAAA +short
dig -t AAAA example.com +short

# Connectivity
ping6 -c 2 2606:4700:4700::1111
curl -6 -I https://example.com
curl -6 https://api64.ipify.org

# Prefer v4 or v6 in curl
curl -4 -I https://example.com
curl -6 -I https://example.com
```

Link-local addresses need a scope/interface: `fe80::1%eth0`.

## Common mistakes

- Forgetting `%iface` on link-local
- Disabling IPv6 and breaking dual-stack apps randomly
- Assuming no AAAA means host is down

## Exercises

Work in `exercises/06-ipv6-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/06-ipv6-basics/` until after an honest attempt.**

## Self-check

1. What starts with fe80::?
2. How query AAAA with dig?
3. curl flag to force IPv6?

## Further reading

- https://www.rfc-editor.org/rfc/rfc8200
