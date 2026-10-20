---
title: "09. ss, netstat, and lsof: See What Is Listening"
---

# 09. ss, netstat, and lsof: See What Is Listening

**Phase:** Phase 3 — Host networking toolkit  
**Estimated time:** 1–2 days  
**Slug:** `09-ss-netstat-lsof`

## Learning objectives

- List listening sockets and established connections
- Map ports to processes
- Use lsof for file/socket detectives
- Spot TIME_WAIT / CLOSE_WAIT patterns

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Linux preferred
ss -tulpn
ss -s
ss -tan state established
ss -tan 'sport = :443'
ss -tanp | head

# macOS / older
netstat -anv
netstat -an | grep LISTEN

# Who owns a port?
sudo lsof -iTCP:22 -sTCP:LISTEN
sudo lsof -i :5432
sudo fuser -v 80/tcp                 # Linux psmisc
```

## Reading states

- `LISTEN` — server waiting
- `ESTAB`/`ESTABLISHED` — connected
- `TIME-WAIT` — normal after close (high volume can be OK)
- `CLOSE-WAIT` — often app not closing sockets (bug)

## Common mistakes

- Killing TIME_WAIT thinking it's a leak
- Forgetting sudo for process names in ss -p
- Ignoring IPv6 listeners (`ss -tulpn` shows both)

## Exercises

Work in `exercises/09-ss-netstat-lsof/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/09-ss-netstat-lsof/` until after an honest attempt.**

## Self-check

1. ss flags for TCP/UDP listen + process?
2. lsof command for port 22?
3. CLOSE-WAIT often means?

## Further reading

- https://man7.org/linux/man-pages/man8/ss.8.html
