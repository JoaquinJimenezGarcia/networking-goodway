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
Type every command yourself and keep a lab notes file.

## Why this matters

A ticket says 'L7 is fine but L4 is broken'. If you casually mix OSI and TCP/IP vocabulary, you will chase HTTP dashboards while SYN packets never complete. Layer literacy tells you which tool speaks which layer — curl vs ss vs ping vs ARP — and stops wasted escalations.

## Core concepts

| OSI idea | TCP/IP | Examples | Tools |
|----------|--------|----------|-------|
| L7 App | App | HTTP, DNS, SSH | curl, dig, openssl |
| L4 Transport | TCP/UDP | ports, sessions | ss, nc, tcpdump port |
| L3 Network | IP | routing, ICMP | ip route, ping, traceroute |
| L2 Data link | Link | MAC, ARP, Ethernet | ip neigh, tcpdump -e |
| L1 Physical | wires/radio | link up/down | ip link, ethtool |

HTTPS does **not** replace TCP — TLS rides on a TCP (or QUIC/UDP) session. Ports are L4 identifiers; MACs are L2.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
dig example.com +short
ping -c 2 example.com
curl -sS -o /dev/null -w '%{http_code}\n' https://example.com
```

Sample output:

```text
93.184.216.34
64 bytes from ... time=20 ms
200
```

**Interpretation:** DNS (app naming) → ICMP (L3 reachability) → HTTPS (app over TLS/TCP). Failure at each step points to a different layer.

### Example 2

```bash
ss -tlnp | head -5
# macOS: netstat -an | grep LISTEN | head
```

Sample output:

```text
LISTEN 0 128 0.0.0.0:443 ...
```

**Interpretation:** Listening sockets prove an L4 endpoint exists locally. If ss shows nothing on 443 but curl to remote works, the problem is elsewhere.

### Example 3

```bash
curl -vI https://example.com 2>&1 | head -35
```

Sample output:

```text
* Connected to example.com (93.184.216.34) port 443
* SSL connection using TLSv1.3
< HTTP/2 200
```

**Interpretation:** Verbose curl reveals TCP connect then TLS then HTTP — a live layer walkthrough.


## Mini-lab

1. Draw the path of `https://example.com` and label each step with a tool.
2. For a local `python3 -m http.server 8000`, identify L4 port and L7 protocol.
3. Answer: which layer are ports? MACs? TLS relative to TCP?

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Calling IPs 'MAC addresses' | L2/L3 confusion | ip neigh vs ip addr |
| Thinking HTTPS replaces TCP | Missing transport | curl -v connect line |
| Blaming DNS for TCP RST | Wrong layer | dig OK + ss/tcpdump |
| Tool soup without layer map | No hypothesis | Pick one layer's tool |

## Study tip for OSI vs TCP/IP Models (with packet walkthrough)

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Calling IP addresses "MAC addresses"
- Thinking HTTPS replaces TCP
- Blaming DNS for every failure without evidence

## Exercises

Work in `exercises/01-osi-tcpip/`. Read that folder's `README.md` before coding.

```bash
cd exercises/01-osi-tcpip
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Implement `layer_for_ports`, `layer_for_mac`, `layer_for_http`, and `tls_rides_on` returning the layer labels taught in the mapping table (L4, L2, L7, TCP).

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/01-osi-tcpip/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. Which layer are ports?
2. Which layer are MAC addresses?
3. Where does TLS sit relative to TCP?

## Further reading

- https://www.rfc-editor.org/rfc/rfc1122
