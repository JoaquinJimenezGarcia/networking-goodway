---
title: "28. HTTP/2, HTTP/3, and QUIC Awareness"
---

# 28. HTTP/2, HTTP/3, and QUIC Awareness

**Phase:** Phase 5 — HTTP, TLS, and APIs  
**Estimated time:** 1 day  
**Slug:** `28-http2-quic`

## Learning objectives

- Know why HTTP/2 multiplexes
- Understand QUIC runs on UDP
- Probe protocol with curl
- Relate to CDNs

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
curl -I --http1.1 https://example.com
curl -I --http2 https://example.com
curl -I --http3-only https://example.com 2>/dev/null || echo 'http3 not in this curl'
curl -sS -o /dev/null -w '%{http_version}\n' https://example.com
```

QUIC/HTTP3 can improve lossy networks; middleboxes sometimes break UDP.

## Common mistakes

- Assuming HTTP/3 always faster
- Blocking UDP 443 enterprise-wide accidentally
- Ignoring fallback to TCP

## Exercises

Work in `exercises/28-http2-quic/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/28-http2-quic/` until after an honest attempt.**

## Self-check

1. HTTP/2 main benefit?
2. QUIC transport?
3. curl write-out for version?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9114
