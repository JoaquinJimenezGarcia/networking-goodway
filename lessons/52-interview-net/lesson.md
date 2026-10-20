---
title: "52. Networking Interview & Oncall Drills"
---

# 52. Networking Interview & Oncall Drills

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 2 days  
**Slug:** `52-interview-net`

## Learning objectives

- Explain issues aloud with structure
- Whiteboard a path
- Solve timed scenarios
- Prioritize user impact

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Scenarios:

- Users in one city cannot login
- Intermittent TLS failures
- DNS works for you, not for customers
- Pod cannot reach DB
- Site slow only on mobile networks

Use the playbook; narrate evidence.

## Common mistakes

- Jumping to rare root causes first
- No communication
- Fixing without verifying

## Exercises

Work in `exercises/52-interview-net/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/52-interview-net/` until after an honest attempt.**

## Self-check

1. One-city issue first suspects?
2. TLS intermittent ideas?
3. Verify how?

## Further reading

- https://sre.google/sre-book/managing-incidents/
