---
title: "32. How the Internet Routes: BGP at a Glance"
---

# 32. How the Internet Routes: BGP at a Glance

**Phase:** Phase 6 — Routing  
**Estimated time:** 1–2 days  
**Slug:** `32-bgp-internet`

## Learning objectives

- Explain ASNs and prefixes
- Understand announcements/withdrawals
- Use looking glasses / whois / bgp tools
- Know why leaks/hijacks matter

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
whois 1.1.1.1 | head -40
whois -h whois.radb.net -- '-i origin AS13335' 2>/dev/null | head
# public helpers
curl -s https://ipinfo.io/1.1.1.1
dig +short 1.1.1.1.origin.asn.cymru.com TXT
```

BGP picks paths between Autonomous Systems. Mis-announcements can blackhole or hijack traffic — RPKI/filtering mitigate.

## Common mistakes

- Thinking traceroute equals BGP path always
- Ignoring prefix ownership
- Lab experiments on real upstreams

## Exercises

Work in `exercises/32-bgp-internet/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/32-bgp-internet/` until after an honest attempt.**

## Self-check

1. What is an ASN?
2. What does whois help show?
3. Why RPKI?

## Further reading

- https://www.rfc-editor.org/rfc/rfc4271
