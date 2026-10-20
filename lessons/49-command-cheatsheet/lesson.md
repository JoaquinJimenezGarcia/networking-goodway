---
title: "49. Command Cheatsheet Consolidation Drill"
---

# 49. Command Cheatsheet Consolidation Drill

**Phase:** Phase 3 — Host networking toolkit  
**Estimated time:** 1–2 days  
**Slug:** `49-command-cheatsheet`

## Learning objectives

- Memorize a personal daily cheatsheet
- Group tools by layer
- Practice without looking
- Keep a living notes file

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

## Must-know roster

```bash
ip -br a; ip r; ip neigh
ss -tulpn
ping -c 3 <t>; mtr -rwzc 50 <t>
dig <name> +short; dig @1.1.1.1 <name>
curl -vI --max-time 5 https://<t>
openssl s_client -connect host:443 -servername host
nc -vz -w 3 host 443
sudo tcpdump -ni any -c 20 host <t>
```

Rebuild this list from memory as the exercise.

## Common mistakes

- Huge unsorted note dumps
- Never practicing recall
- Tools without understanding

## Exercises

Work in `exercises/49-command-cheatsheet/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/49-command-cheatsheet/` until after an honest attempt.**

## Self-check

1. Name two tools per L3/L4/L7
2. Why cheatsheets help oncalls?
3. What belongs in daily roster?

## Further reading

- https://wiki.archlinux.org/title/Network_configuration
