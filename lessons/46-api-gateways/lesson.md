---
title: "46. API Gateways and Edge Patterns"
---

# 46. API Gateways and Edge Patterns

**Phase:** Phase 10 — Load balancing and proxies  
**Estimated time:** 1–2 days  
**Slug:** `46-api-gateways`

## Learning objectives

- Place auth/rate-limit/WAF at edge
- Distinguish gateway vs service mesh
- Debug 502/503/504 meanings
- Trace request IDs across hops

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
curl -I https://api.example.com/v1/health
curl -sS -o /dev/null -w '%{http_code}\n' https://api.example.com/v1/missing
# common gateway timeouts -> 504
```

502 bad gateway (upstream nonsense), 503 unavailable, 504 timeout — start at proxy logs + upstream health.

## Common mistakes

- Business logic only in gateway forever
- No correlation IDs
- Retry storms without backoff

## Exercises

Work in `exercises/46-api-gateways/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/46-api-gateways/` until after an honest attempt.**

## Self-check

1. 504 often means?
2. 502 hints?
3. Why request IDs?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9110
