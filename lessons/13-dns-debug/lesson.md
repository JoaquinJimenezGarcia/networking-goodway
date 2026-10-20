---
title: "13. DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon"
---

# 13. DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon

**Phase:** Phase 4 — DNS  
**Estimated time:** 1–2 days  
**Slug:** `13-dns-debug`

## Learning objectives

- Differentiate NXDOMAIN vs timeout vs SERVFAIL
- Inspect /etc/resolv.conf and systemd-resolved
- Debug search domains
- Handle private DNS vs public DNS conflicts

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
cat /etc/resolv.conf
resolvectl status                 # systemd-resolved
resolvectl query example.com

# Compare resolvers
dig @8.8.8.8 internal.corp.example A +time=2
dig @10.0.0.2 internal.corp.example A +time=2

# Common response codes in dig output: NOERROR, NXDOMAIN, SERVFAIL, REFUSED
dig not-a-real-domain-xyz.invalid A
```

**Split-horizon**: internal and public names return different answers — corporate VPN classic.

## Common mistakes

- Pointing corp laptops at 8.8.8.8 and breaking private zones
- Ignoring search domain appending
- Hardcoding IPs forever instead of fixing DNS

## Exercises

Work in `exercises/13-dns-debug/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/13-dns-debug/` until after an honest attempt.**

## Self-check

1. NXDOMAIN meaning?
2. SERVFAIL meaning?
3. Why VPN DNS matters?

## Further reading

- https://man7.org/linux/man-pages/man5/resolv.conf.5.html
