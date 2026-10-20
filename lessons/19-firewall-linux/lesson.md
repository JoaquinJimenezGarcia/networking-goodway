---
title: "19. Host Firewalls: nftables, iptables, ufw"
---

# 19. Host Firewalls: nftables, iptables, ufw

**Phase:** Phase 8 — Firewalls, NAT, and policy  
**Estimated time:** 2 days  
**Slug:** `19-firewall-linux`

## Learning objectives

- List rules and policies
- Allow least ports
- Test with care to avoid lockout
- Prefer high-level tools when enough

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# ufw (Ubuntu)
sudo ufw status verbose
sudo ufw default deny incoming
sudo ufw allow OpenSSH
sudo ufw allow 443/tcp
sudo ufw enable

# nftables
sudo nft list ruleset
# iptables legacy
sudo iptables -L -n -v
sudo iptables -S
```

Remote changes: keep an active console/session; allow SSH **before** enabling default deny.

## Common mistakes

- Locking yourself out
- Disabling firewall instead of opening one port
- Forgetting IPv6 (`ip6tables`/`ufw`)

## Exercises

Work in `exercises/19-firewall-linux/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/19-firewall-linux/` until after an honest attempt.**

## Self-check

1. ufw allow SSH command idea?
2. Why console access?
3. nft list command?

## Further reading

- https://wiki.nftables.org/
