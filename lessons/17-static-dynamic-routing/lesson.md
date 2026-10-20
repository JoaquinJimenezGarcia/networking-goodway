---
title: "17. Static vs Dynamic Routing Concepts"
---

# 17. Static vs Dynamic Routing Concepts

**Phase:** Phase 6 — Routing  
**Estimated time:** 1–2 days  
**Slug:** `17-static-dynamic-routing`

## Learning objectives

- Contrast static routes vs OSPF/BGP ideas
- Know when static is enough
- Explain convergence at a high level
- Read simple BGP/OSPF vocabulary

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Static routes: operator-defined, simple, brittle at scale.
Dynamic protocols: OSPF/IS-IS inside orgs; **BGP** between orgs/internet.

```bash
# You may see learned routes on routers/VMs with routing daemons
ip route show protocol bgp 2>/dev/null
vtysh -c 'show ip route' 2>/dev/null   # FRR/Quagga style labs
```

Lab idea: FRRouting in VMs — not required for every exercise, but valuable later.

## Common mistakes

- Injecting static routes that fight BGP
- No documentation of static routes
- Assuming cloud route tables behave like home Wi-Fi

## Exercises

Work in `exercises/17-static-dynamic-routing/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/17-static-dynamic-routing/` until after an honest attempt.**

## Self-check

1. When static routes shine?
2. BGP used where?
3. What is convergence?

## Further reading

- https://www.rfc-editor.org/rfc/rfc4271
