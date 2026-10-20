---
title: "01. OSI vs TCP/IP Models (with packet walkthrough)"
---

# 01. OSI vs TCP/IP Models (with packet walkthrough)

**Phase:** Phase 1 — Models and packets  
**Estimated time:** 1–2 days  
**Slug:** `01-osi-tcpip`

## Learning objectives

- Map OSI layers to TCP/IP layers
- Trace a request layer-by-layer
- Identify which tool inspects which layer
- Stop mixing L2/L3/L4 terms casually

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Useful mapping

| OSI idea | TCP/IP | Examples | Tools |
|----------|--------|----------|-------|
| L7 App | App | HTTP, DNS, SSH | curl, dig, openssl |
| L4 Transport | TCP/UDP | ports, reliability | ss, netstat, nc |
| L3 Network | IP | routing, ICMP | ip route, ping, traceroute |
| L2 Data link | Ethernet/Wi-Fi | MAC, ARP | ip neigh, arp, tcpdump -e |
| L1 Physical | wires/radio | link up/down | ip link, ethtool |

## Packet walk (simplified)

Opening `https://example.com`:

1. DNS (app) resolves name → IP (`dig`)
2. TCP connects to `IP:443` (handshake)
3. TLS negotiates encryption (`openssl s_client`)
4. HTTP request/response (`curl -v`)

```bash
# See layers in one debug session
dig example.com +short
ping -c 2 example.com
curl -vI https://example.com 2>&1 | head -40
```

## Common mistakes

- Calling IP addresses "MAC addresses"
- Thinking HTTPS replaces TCP
- Blaming DNS for every failure without evidence

## Exercises

Work in `exercises/01-osi-tcpip/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/01-osi-tcpip/` until after an honest attempt.**

## Self-check

1. Which layer are ports?
2. Which layer are MAC addresses?
3. Where does TLS sit relative to TCP?

## Further reading

- https://www.rfc-editor.org/rfc/rfc1122
