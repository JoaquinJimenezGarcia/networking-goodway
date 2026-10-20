---
title: "26. Load Balancing Concepts and Health Checks"
---

# 26. Load Balancing Concepts and Health Checks

**Phase:** Phase 10 — Load balancing and proxies  
**Estimated time:** 1–2 days  
**Slug:** `26-load-balancing`

## Learning objectives

- Explain L4 vs L7 balancing
- Know health checks and draining
- Recognize algorithms (round-robin, least-conn)
- See nginx upstream basics

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

L4: TCP/UDP (IP:port). L7: HTTP paths/headers.

```bash
# Probe backends yourself
for b in 10.0.0.11 10.0.0.12; do
  curl -sS -o /dev/null -w "$b %{http_code}\n" --connect-timeout 1 http://$b/healthz || echo "$b down"
done
```

Nginx sketch: `upstream`, `proxy_pass`, health via separate checks/sidecar.

## Common mistakes

- No health checks
- Balancing without shared session strategy when needed
- Draining ignored during deploys

## Exercises

Work in `exercises/26-load-balancing/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/26-load-balancing/` until after an honest attempt.**

## Self-check

1. L4 vs L7?
2. Why health checks?
3. What is draining?

## Further reading

- https://nginx.org/en/docs/http/load_balancing.html
