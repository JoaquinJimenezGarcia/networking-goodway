---
title: "20. tcpdump Basics for Engineers"
---

# 20. tcpdump Basics for Engineers

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 2 days  
**Slug:** `20-tcpdump-basics`

## Learning objectives

- Capture with filters
- Write/read pcap files
- Read flags and ports
- Minimize capture blast radius

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
sudo tcpdump -ni eth0 -c 20
sudo tcpdump -ni any port 53
sudo tcpdump -ni eth0 host 10.0.0.5 and tcp port 443
sudo tcpdump -ni eth0 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'

# write / read
sudo tcpdump -ni eth0 -w /tmp/cap.pcap -c 100
tcpdump -nr /tmp/cap.pcap | head
tcpdump -nr /tmp/cap.pcap -A | head

# useful verbosity
sudo tcpdump -ni eth0 -vv -c 10 port 443
```

Wireshark GUI is great for deeper analysis of the same pcaps.

## Common mistakes

- Capturing on prod without policy
- Huge unfiltered captures filling disks
- Sniffing secrets on shared networks

## Exercises

Work in `exercises/20-tcpdump-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/20-tcpdump-basics/` until after an honest attempt.**

## Self-check

1. Filter for DNS?
2. Flag to write pcap?
3. Read pcap without capture?

## Further reading

- https://www.tcpdump.org/manpages/tcpdump.1.html
