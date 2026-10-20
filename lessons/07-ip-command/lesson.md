---
title: "07. The ip Command Deep Dive (addr, link, route)"
---

# 07. The ip Command Deep Dive (addr, link, route)

**Phase:** Phase 3 — Host networking toolkit  
**Estimated time:** 2 days  
**Slug:** `07-ip-command`

## Learning objectives

- Use ip addr/link/route fluently
- Bring interfaces up/down (lab)
- Add/delete routes temporarily
- Prefer ip over deprecated ifconfig on Linux

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Essential `ip` examples (Linux)

```bash
ip addr show
ip -br addr                         # brief
ip link show
ip link set eth0 up
ip link set eth0 down

ip route show
ip route get 1.1.1.1                # which path would kernel use?
ip route add 10.50.0.0/16 via 10.0.0.1
ip route del 10.50.0.0/16

ip -s link show eth0                # counters RX/TX errors
ip monitor all                      # watch changes live
```

## macOS cousins

```bash
ifconfig
route -n get default
networksetup -listallhardwareports
```

## Common mistakes

- Making persistent mistakes thinking `ip route add` survives reboot (needs netplan/NetworkManager/systemd-networkd)
- typos adding routes that blackhole traffic
- changing production without console access

## Exercises

Work in `exercises/07-ip-command/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/07-ip-command/` until after an honest attempt.**

## Self-check

1. Command to show routes?
2. What does `ip route get` do?
3. Brief address listing flag?

## Further reading

- https://man7.org/linux/man-pages/man8/ip.8.html
