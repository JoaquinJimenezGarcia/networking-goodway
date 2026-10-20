---
title: "03. Ethernet, MAC Addresses, and ARP"
---

# 03. Ethernet, MAC Addresses, and ARP

**Phase:** Phase 7 — L2, switching, and local nets  
**Estimated time:** 1–2 days  
**Slug:** `03-ethernet-mac-arp`

## Learning objectives

- Read MAC addresses and ARP tables
- Explain ARP purpose on a LAN
- Detect basic ARP issues
- Use neighbor tables on modern Linux

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Commands

```bash
# Linux
ip link show
ip neigh show
ip -s link
# older
arp -n

# macOS
ifconfig en0
arp -an
```

ARP maps **IP → MAC** on the local subnet so frames can be delivered.

```bash
ping -c 1 192.168.1.1
ip neigh show          # entry should appear as REACHABLE/DELAY/...
```

## Useful tcpdump for ARP

```bash
sudo tcpdump -ni eth0 arp
```

## Common mistakes

- Expecting ARP to work across routers (it doesn't)
- Duplicate IPs causing flapping ARP
- Hardcoding MAC allowlists without ops process

## Exercises

Work in `exercises/03-ethernet-mac-arp/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/03-ethernet-mac-arp/` until after an honest attempt.**

## Self-check

1. ARP maps what to what?
2. Does ARP cross routers?
3. Command to show neighbors on Linux?

## Further reading

- https://www.rfc-editor.org/rfc/rfc826
