---
title: "27. Reverse Proxies: TLS Termination and Headers"
---

# 27. Reverse Proxies: TLS Termination and Headers

**Phase:** Phase 10 — Load balancing and proxies  
**Estimated time:** 1–2 days  
**Slug:** `27-reverse-proxy`

## Learning objectives

- Terminate TLS at proxy
- Pass X-Forwarded-* carefully
- Preserve client IP with real_ip
- Log correctly

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# App sees proxy IP unless headers configured
curl -H 'X-Forwarded-For: 1.2.3.4' http://localhost:8080/ || true

# Test proxy locally
curl -I https://localhost --cacert lab-ca.pem
curl -I http://localhost/api
```

Trust `X-Forwarded-For` **only** from trusted proxies — otherwise clients can spoof.

## Common mistakes

- Trusting XFF from the internet
- Mixed content / wrong redirect schemes
- Huge header sizes without limits

## Exercises

Work in `exercises/27-reverse-proxy/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/27-reverse-proxy/` until after an honest attempt.**

## Self-check

1. TLS termination meaning?
2. Why not trust XFF blindly?
3. real_ip purpose?

## Further reading

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
