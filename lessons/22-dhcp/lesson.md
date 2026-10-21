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
Type every command yourself and keep a lab notes file.

## Why this matters

Laptop has an APIPA/link-local address and no default route. DHCP discover/offer/request/ack failed — lease, relay, or server scope issues.

## Core concepts

What you must be able to explain:

- Explain Discover/Offer/Request/Ack
- Inspect leases
- Debug 'got 169.254'
- Know static vs DHCP tradeoffs

Mental model for `22-dhcp` (exercise kind `dhcp_apipa`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
ip -br addr; ip route; ip route get 1.1.1.1
```

Sample output:

```text
eth0 UP 192.168.1.20/24
default via 192.168.1.1 dev eth0
1.1.1.1 via 192.168.1.1 dev eth0 src 192.168.1.20
```

**Interpretation:** `ip route get` shows the chosen route, egress device, and preferred source — gold for 'why did it leave this NIC?' questions.

### Example 2

```bash
ping -c 3 1.1.1.1
ss -tulpn | head
# macOS: netstat -anv | head
```

Sample output:

```text
3 packets transmitted, 3 received
udp ... :53
tcp LISTEN ... :22
```

**Interpretation:** ICMP OK proves basic L3; ss proves local listeners. Combine with ARP/neigh when LAN peers fail.

### Example 3

```bash
ip neigh show | head
ping -c 1 $(ip route | awk '/default/ {print $3; exit}')
```

Sample output:

```text
192.168.1.1 dev eth0 lladdr ... REACHABLE
64 bytes from gateway
```

**Interpretation:** Neighbor/ARP state validates L2 adjacency to the gateway before you blame the wider internet.


## Mini-lab

1. Re-type every worked command for **DHCP and Address Assignment** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Two DHCP servers fighting on a LAN | See common mistakes | Re-run lesson commands |
| Tiny pools exhausting leases | See common mistakes | Re-run lesson commands |
| Static IP colliding with DHCP pool | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for DHCP and Address Assignment

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Two DHCP servers fighting on a LAN
- Tiny pools exhausting leases
- Static IP colliding with DHCP pool

## Exercises

Work in `exercises/22-dhcp/`. Read that folder's `README.md` before coding.

```bash
cd exercises/22-dhcp
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `dhcp_fail_prefix`, `addr_assign_proto`, `ipv6_autoconfig`. Each function is a tiny retrieval drill for **DHCP and Address Assignment** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/22-dhcp/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. DORA steps?
2. What does 169.254 suggest?
3. DHCP vs static when?

## Further reading

- https://www.rfc-editor.org/rfc/rfc2131
