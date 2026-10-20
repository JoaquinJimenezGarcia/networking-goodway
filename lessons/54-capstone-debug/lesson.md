---
title: "54. Capstone: Broken Network Challenge"
---

# 54. Capstone: Broken Network Challenge

**Phase:** Phase 13 — Capstones  
**Estimated time:** 2–4 days  
**Slug:** `54-capstone-debug`

## Learning objectives

- Debug planted failures
- Produce timeline + root cause
- Fix with minimal change
- Write postmortem

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Break a snapshot on purpose (wrong route, bad DNS, blocked SG, MTU, expired cert, hosts file typo). Restore service with postmortem:

Impact → Timeline → Root cause → Fix → Prevention

## Common mistakes

- Recreate VMs instead of debugging
- Changing everything
- No postmortem

## Exercises

Work in `exercises/54-capstone-debug/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/54-capstone-debug/` until after an honest attempt.**

## Self-check

1. Root cause?
2. Evidence?
3. Prevention?

## Further reading

- https://sre.google/sre-book/postmortem-culture/
