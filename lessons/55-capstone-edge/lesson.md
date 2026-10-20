---
title: "55. Capstone: Secure Edge for a Small App"
---

# 55. Capstone: Secure Edge for a Small App

**Phase:** Phase 13 — Capstones  
**Estimated time:** 4–6 days  
**Slug:** `55-capstone-edge`

## Learning objectives

- Terminate TLS at edge
- Reverse proxy to app
- Firewall + SSH hardening + health checks
- Probe latency/error metrics

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Mission

Deploy a small app behind:

- Reverse proxy with TLS (lab certs OK)
- Health checks and structured logs
- Host firewall
- Optional WireGuard admin access instead of public SSH
- Simple uptime probe script with curl timings
- Runbook for cert renewal and failure modes

## Rubric

- Least privilege exposure
- Clear 502/504 debugging notes
- Evidence of probe dashboard/log
- Graceful reloads

## Common mistakes

- App exposed directly on :80 public
- No health checks
- Certs without renewal plan

## Exercises

Work in `exercises/55-capstone-edge/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/55-capstone-edge/` until after an honest attempt.**

## Self-check

1. What is public?
2. How detect expiry?
3. How prove health?

## Further reading

- https://nginx.org/en/docs/
