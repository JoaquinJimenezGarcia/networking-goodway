---
title: "25. SSH Tunnels and Port Forwards"
---

# 25. SSH Tunnels and Port Forwards

**Phase:** Phase 9 — VPN, tunnels, and overlays  
**Estimated time:** 1–2 days  
**Slug:** `25-ssh-tunnels`

## Learning objectives

- Use local/remote/dynamic SSH forwards
- Access private admin UIs safely
- Avoid standing tunnels forever without need
- Combine with ProxyJump

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Local forward: local 8080 -> remote's localhost:80 via ssh host
ssh -L 8080:127.0.0.1:80 user@bastion

# Remote forward
ssh -R 9090:127.0.0.1:3000 user@bastion

# Dynamic SOCKS
ssh -D 1080 user@bastion
curl --socks5-hostname 127.0.0.1:1080 https://example.com

# Jump host
ssh -J bastion user@internal
# ~/.ssh/config: ProxyJump bastion
```

## Common mistakes

- Exposing binds on 0.0.0.0 unintentionally
- Long-lived tunnels as permanent VPN substitute without review
- Forgetting ExitOnForwardFailure

## Exercises

Work in `exercises/25-ssh-tunnels/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/25-ssh-tunnels/` until after an honest attempt.**

## Self-check

1. -L meaning?
2. -D meaning?
3. ProxyJump purpose?

## Further reading

- https://man.openbsd.org/ssh
