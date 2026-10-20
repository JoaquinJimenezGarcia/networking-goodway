---
title: "00. Orientation: How Networks Work and How to Practice"
---

# 00. Orientation: How Networks Work and How to Practice

**Phase:** Phase 0 — Orientation  
**Estimated time:** 1 day  
**Slug:** `00-orientation`

## Learning objectives

- Explain clients, servers, packets, and protocols at a beginner level
- Set up a safe practice lab (VM + localhost tools)
- Adopt attempt → struggle → solution → rewrite
- Know which tools you will use daily

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Mental model

A **network** moves messages between programs on machines.

- **Host**: a computer with one or more network interfaces
- **Packet/frame**: a chunk of data with headers (addresses, ports, etc.)
- **Protocol**: agreed rules (IP, TCP, UDP, HTTP, DNS, …)
- **Port**: number identifying an application endpoint on a host

```text
Browser  --HTTP-->  Web server
   |                   |
  TCP                 TCP
   |                   |
  IP                  IP
   +-------- link -----+
```

## Practice lab

1. Your laptop terminal (many commands work on macOS/Linux)
2. A Linux VM for `ip`, `ss`, `nft`, systemd-resolved
3. Optional second VM to ping/ssh between hosts

## Daily toolkit (you will master these)

```bash
ping -c 3 1.1.1.1
traceroute example.com          # or traceroute / tracert
dig example.com +short
curl -I https://example.com
ss -tulpn                       # Linux; macOS: netstat -anv
ip addr                         # Linux; macOS: ifconfig / ipconfig getifaddr en0
```

## Study method

Read PDF → type every example → finish `exercises/NN-*/` (`./test.sh`) → only then open solutions → rewrite next day.

## Common mistakes

- Only reading without typing commands
- Practicing against production systems without approval
- Skipping fundamentals and jumping to cloud GUIs

## Exercises

Work in `exercises/00-orientation/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/00-orientation/` until after an honest attempt.**

## Self-check

1. What is a port?
2. Name five daily networking commands
3. Why use a lab VM?

## Further reading

- https://www.rfc-editor.org/rfc/rfc1122
