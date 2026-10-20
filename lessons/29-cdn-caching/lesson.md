---
title: "29. CDNs, Caching, and Cache Headers"
---

# 29. CDNs, Caching, and Cache Headers

**Phase:** Phase 10 — Load balancing and proxies  
**Estimated time:** 1–2 days  
**Slug:** `29-cdn-caching`

## Learning objectives

- Read Cache-Control/ETag/Age
- Differentiate CDN edge vs origin issues
- Purge/invalidate conceptually
- Debug with response headers

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
curl -sI https://example.com | grep -iE 'cache-control|etag|age|cf-|x-cache|server'
curl -sI -H 'Cache-Control: no-cache' https://example.com | head
```

When users see old content: TTL, Vary headers, stale-while-revalidate, regional POPs, or local browser cache.

## Common mistakes

- Caching personalized/private responses publicly
- No versioning of static assets
- Purging entire site for one file habitually

## Exercises

Work in `exercises/29-cdn-caching/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/29-cdn-caching/` until after an honest attempt.**

## Self-check

1. Age header meaning?
2. Why asset fingerprinting?
3. Private vs public cache?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9111
