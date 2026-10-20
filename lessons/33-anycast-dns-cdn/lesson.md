---
title: "33. Anycast, GeoDNS, and Global Traffic"
---

# 33. Anycast, GeoDNS, and Global Traffic

**Phase:** Phase 10 — Load balancing and proxies  
**Estimated time:** 1 day  
**Slug:** `33-anycast-dns-cdn`

## Learning objectives

- Explain anycast routing idea
- Contrast with unicast
- Relate to DNS/CDN POPs
- Debug geo differences

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Anycast: same IP announced from many places; users hit nearby POP.

```bash
dig +short one.one.one.one
ping -c 2 1.1.1.1
curl -s https://cloudflare.com/cdn-cgi/trace | head
curl -sI https://example.com | grep -i cf-ray
```

Different resolvers/regions may see different answers (GeoDNS).

## Common mistakes

- Expecting one physical server behind 1.1.1.1
- Debugging only from one region
- Ignoring resolver location effects

## Exercises

Work in `exercises/33-anycast-dns-cdn/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/33-anycast-dns-cdn/` until after an honest attempt.**

## Self-check

1. Anycast vs unicast?
2. Why region matters?
3. CDN POP meaning?

## Further reading

- https://www.cloudflare.com/learning/cdn/glossary/anycast-network/
