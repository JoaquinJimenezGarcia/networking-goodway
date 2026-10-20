---
title: "11. TCP vs UDP, Handshakes, and Reliability"
---

# 11. TCP vs UDP, Handshakes, and Reliability

**Phase:** Phase 1 — Models and packets  
**Estimated time:** 1–2 days  
**Slug:** `11-tcp-udp`

## Learning objectives

- Contrast TCP and UDP properties
- Explain three-way handshake conceptually
- Know when UDP is preferred
- Observe TCP with ss/tcpdump

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## TCP vs UDP

| | TCP | UDP |
|---|-----|-----|
| Connection | yes | no |
| Reliable delivery | yes | best-effort |
| Ordered | yes | no |
| Use cases | HTTP, SSH | DNS, QUIC/games, media |

```bash
# Established TCP
ss -tan state established | head
# Capture handshake (lab)
sudo tcpdump -ni any -c 20 'tcp[tcpflags] & (tcp-syn) != 0'
# UDP DNS
sudo tcpdump -ni any -c 5 udp port 53
```

SYN → SYN-ACK → ACK establishes TCP. FIN/RST close or reset.

## Common mistakes

- Using UDP and expecting TCP guarantees
- SYN floods without rate limits
- Forcing TCP where UDP+app reliability fits

## Exercises

Work in `exercises/11-tcp-udp/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/11-tcp-udp/` until after an honest attempt.**

## Self-check

1. Three-way handshake steps?
2. Is DNS always UDP?
3. Command to show established TCP?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9293
