---
title: "24. VPN Basics: IPsec, WireGuard, OpenVPN"
---

# 24. VPN Basics: IPsec, WireGuard, OpenVPN

**Phase:** Phase 9 — VPN, tunnels, and overlays  
**Estimated time:** 2 days  
**Slug:** `24-vpn-basics`

## Learning objectives

- Contrast VPN types at a high level
- Read WireGuard quick configs conceptually
- Troubleshoot VPN DNS and routes
- Watch MTU/overhead issues

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# WireGuard (if installed)
sudo wg
sudo wg show
ip route | grep -E 'wg|tun|tun0'

# OpenVPN legacy style
ip addr show tun0
```

Common failures: missing routes, DNS still public, MTU blackholes, firewall blocking UDP 51820/1194.

```bash
ping -c 2 10.0.0.1                 # internal after VPN
dig @10.0.0.2 internal.service A
curl -I https://internal.service
```

## Common mistakes

- Full-tunnel VPN without need (hairpin pain)
- Split tunnel missing critical routes
- Ignoring MTU

## Exercises

Work in `exercises/24-vpn-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/24-vpn-basics/` until after an honest attempt.**

## Self-check

1. WireGuard show command?
2. Typical WG port?
3. Why MTU drops with VPN?

## Further reading

- https://www.wireguard.com/
