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
Type every command yourself and keep a lab notes file.

## Why this matters

Two VMs on the same subnet cannot talk, yet both ping 8.8.8.8. Often the gateway works (so 'internet is fine') while ARP/neighbor resolution between peers is broken — duplicate IP, wrong VLAN, or isolated port. Ethernet/MAC/ARP literacy is how you prove L2 adjacency.

## Core concepts

- Ethernet delivers frames using **MAC** addresses on a broadcast domain.
- **ARP** (IPv4) maps **IP → MAC** on the local subnet only — it does **not** cross routers.
- Linux `ip neigh` is the modern neighbor table; `arp -n` still appears in tribal knowledge.
- Symptoms of duplicate IP: flapping MAC for one IP, intermittent reachability.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
ip -br link; ip neigh show | head
# macOS: ifconfig en0; arp -an | head
```

Sample output:

```text
eth0 UP ...
192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

**Interpretation:** REACHABLE to the gateway MAC means L2 to default router is OK.

### Example 2

```bash
ping -c 1 192.168.1.1; ip neigh show | head
```

Sample output:

```text
64 bytes from 192.168.1.1
192.168.1.1 ... REACHABLE
```

**Interpretation:** Traffic populates/ refreshes neighbor entries — empty table after idle is normal.

### Example 3

```bash
sudo tcpdump -ni eth0 -c 6 arp
```

Sample output:

```text
Request who-has 192.168.1.50 tell 192.168.1.20
Reply 192.168.1.50 is-at aa:bb:...
```

**Interpretation:** Seeing requests without replies isolates 'who isn't answering ARP'.


## Mini-lab

1. Ping gateway; confirm neigh entry.
2. Ping a same-subnet peer; capture ARP.
3. Explain why ARP cannot resolve an IP on another subnet.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| ARP across routers expected | L2 boundary misunderstanding | Check same subnet/mask |
| Flapping connectivity | Duplicate IP | Watch neigh MAC changes |
| Wrong VLAN | No ARP replies | Confirm switchport VLAN |
| Stale FAIL neigh | Old negative cache | ip neigh flush / retry |

## Study tip for Ethernet, MAC Addresses, and ARP

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Expecting ARP to work across routers (it doesn't)
- Duplicate IPs causing flapping ARP
- Hardcoding MAC allowlists without ops process

## Exercises

Work in `exercises/03-ethernet-mac-arp/`. Read that folder's `README.md` before coding.

```bash
cd exercises/03-ethernet-mac-arp
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Implement `arp_maps` (`IP-to-MAC`), `arp_crosses_routers` (`no`), and `linux_neigh_cmd` (`ip neigh`).

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/03-ethernet-mac-arp/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. ARP maps what to what?
2. Does ARP cross routers?
3. Command to show neighbors on Linux?

## Further reading

- https://www.rfc-editor.org/rfc/rfc826
