---
title: "02. Encapsulation, Headers, and MTU"
---

# 02. Encapsulation, Headers, and MTU

**Phase:** Phase 1 — Models and packets  
**Estimated time:** 1–2 days  
**Slug:** `02-encapsulation`

## Learning objectives

- Explain encapsulation/decapsulation
- Define MTU and fragmentation issues
- Use ping to probe path MTU ideas
- Recognize common header sizes intuitively

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

After enabling a VPN, large uploads hang while small pings work. That is classic MTU/encapsulation pain: each tunnel header steals bytes from the payload budget. Understanding encapsulation and path MTU keeps you from blaming the application for silent blackholes.

## Core concepts

Encapsulation wraps upper-layer payloads:

```text
[Eth][IP][TCP][HTTP...]
```

- **MTU**: max payload on a link (Ethernet often **1500**).
- VPN/overlay headers reduce effective MTU (e.g. 1420).
- DF (don't fragment) + blocked ICMP "Packet Too Big" → blackhole.
- Rough sizes: Ethernet header 14 (+4 VLAN), IPv4 ~20, TCP ~20 — intuition for MSS clamping.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
ip link show | sed -n '1,12p'
# look for mtu 1500 / 9000 / 1420
```

Sample output:

```text
2: eth0: <BROADCAST,MULTICAST,UP> mtu 1500 ...
3: wg0: ... mtu 1420 ...
```

**Interpretation:** Interface MTU is local. Path MTU can be lower than any single hop you admin.

### Example 2

```bash
ping -c 2 -M do -s 1472 1.1.1.1 2>&1 | head -8 || ping -c 2 -D -s 1472 1.1.1.1 2>&1 | head -8
```

Sample output:

```text
1472 + 28 = 1500 on IPv4; success means path accepted DF full-size frames (or middlebox lies).
```

**Interpretation:** 1472 data bytes + 20 IPv4 + 8 ICMP ≈ 1500. Failure after VPN strongly suggests overhead.

### Example 3

```bash
sudo tcpdump -ni any -c 5 icmp
```

Sample output:

```text
IP a > b: ICMP echo request
IP b > a: ICMP echo reply
```

**Interpretation:** Confirm ICMP is not blocked if you rely on PMTUD. Many 'mystery hangs' are PTB filtered.


## Mini-lab

1. Record MTU on eth0 and any tunnel interface.
2. Run DF ping at 1472 and at 1400; note difference with VPN on/off.
3. Capture 5 ICMP packets while pinging; identify request/reply.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Large transfers hang, small OK | MTU/PMTUD blackhole | DF ping + lower MSS |
| VPN works for SSH not HTTPS uploads | Effective MTU | Check tunnel MTU |
| No ICMP PTB | Firewall too strict | Allow PTB or clamp MSS |
| Capturing wrong iface | Missed packets | tcpdump -ni any briefly |

## Study tip for Encapsulation, Headers, and MTU

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Ignoring MTU after adding VPN/overlays
- Blackhole path MTU (DF set, ICMP blocked)
- Capturing on the wrong interface

## Exercises

Work in `exercises/02-encapsulation/`. Read that folder's `README.md` before coding.

```bash
cd exercises/02-encapsulation
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Implement `ethernet_typical_mtu`, `vpn_overhead_effect` (returns `lowers-MTU`), and `df_ping_purpose` (`probe-path-MTU`).

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/02-encapsulation/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. What does MTU mean?
2. Why do VPNs lower effective MTU?
3. Name a capture tool

## Further reading

- https://www.rfc-editor.org/rfc/rfc1191
