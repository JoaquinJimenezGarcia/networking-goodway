---
title: "10. nc/ncat and socat: Swiss Army Networking"
---

# 10. nc/ncat and socat: Swiss Army Networking

**Phase:** Phase 3 — Host networking toolkit  
**Estimated time:** 1–2 days  
**Slug:** `10-nc-socat`

## Learning objectives

- Test TCP/UDP ports with nc
- Create quick lab listeners
- Banner-grab carefully in labs
- Know socat for advanced relays

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Port check
nc -vz example.com 443
nc -vz -w 3 10.0.0.5 22
# UDP (partial signal)
nc -vzu 1.1.1.1 53

# Quick listener (lab only)
nc -l 9090
# other terminal:
echo hello | nc 127.0.0.1 9090

# HTTP over nc (lab)
printf 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n' | nc example.com 80 | head

# socat examples (if installed)
socat - TCP:example.com:80
socat TCP-LISTEN:8080,fork TCP:127.0.0.1:80
```

Use only on systems you own/are allowed to test.

## Common mistakes

- Leaving lab listeners on 0.0.0.0 in untrusted networks
- Assuming UDP nc success means healthy service
- Using nc for production TLS (prefer openssl/curl)

## Exercises

Work in `exercises/10-nc-socat/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/10-nc-socat/` until after an honest attempt.**

## Self-check

1. nc flag for zero-I/O port scan style connect?
2. How listen on 9090?
3. Why UDP checks are weaker?

## Further reading

- https://nmap.org/ncat/
