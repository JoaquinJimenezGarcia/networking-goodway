---
title: "50. Tunnels: GRE/VXLAN Overlay Awareness"
---

# 50. Tunnels: GRE/VXLAN Overlay Awareness

**Phase:** Phase 9 — VPN, tunnels, and overlays  
**Estimated time:** 1–2 days  
**Slug:** `50-gre-vxlan`

## Learning objectives

- Explain overlays vs underlays
- Know VXLAN for multi-tenant/datacenter
- See Linux vxlan devices
- Relate to cloud SDN

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
ip link show type vxlan
ip -d link show
# example create is lab-only and environment-specific
```

Overlays carry L2/L3 over underlay IP. MTU and encapsulation overhead matter again.

## Common mistakes

- Ignoring underlay MTU
- Debugging only overlay IPs
- No mapping of VNI/tenants

## Exercises

Work in `exercises/50-gre-vxlan/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/50-gre-vxlan/` until after an honest attempt.**

## Self-check

1. Overlay vs underlay?
2. VXLAN common use?
3. Why MTU again?

## Further reading

- https://www.rfc-editor.org/rfc/rfc7348
