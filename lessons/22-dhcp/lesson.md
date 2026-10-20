---
title: "22. DHCP and Address Assignment"
---

# 22. DHCP and Address Assignment

**Phase:** Phase 7 — L2, switching, and local nets  
**Estimated time:** 1 day  
**Slug:** `22-dhcp`

## Learning objectives

- Explain Discover/Offer/Request/Ack
- Inspect leases
- Debug 'got 169.254'
- Know static vs DHCP tradeoffs

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Linux NetworkManager
nmcli device show
# leases locations vary
ls /var/lib/dhcp/ 2>/dev/null
journalctl -u NetworkManager | grep -i dhcp | tail

# macOS
ipconfig getpacket en0
```

`169.254.x.x` usually means DHCP failed → link-local fallback.

## Common mistakes

- Two DHCP servers fighting on a LAN
- Tiny pools exhausting leases
- Static IP colliding with DHCP pool

## Exercises

Work in `exercises/22-dhcp/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/22-dhcp/` until after an honest attempt.**

## Self-check

1. DORA steps?
2. What does 169.254 suggest?
3. DHCP vs static when?

## Further reading

- https://www.rfc-editor.org/rfc/rfc2131
