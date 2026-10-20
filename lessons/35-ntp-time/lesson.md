---
title: "35. Time Sync and Why Networks Care"
---

# 35. Time Sync and Why Networks Care

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1 day  
**Slug:** `35-ntp-time`

## Learning objectives

- Check clock sync
- Explain skew impact on TLS/auth/logs
- Use timedatectl/chronyc/ntpstat
- Correlate multi-host timelines

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
date -u
timedatectl status                    # systemd
chronyc tracking 2>/dev/null
sntp time.google.com 2>/dev/null
```

Skew breaks Kerberos, confuses logs, and can invalidate TLS seemingly randomly.

## Common mistakes

- Disabling NTP in VMs
- Comparing logs without timezone discipline
- Huge leap smears ignored

## Exercises

Work in `exercises/35-ntp-time/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/35-ntp-time/` until after an honest attempt.**

## Self-check

1. Why TLS cares about time?
2. timedatectl purpose?
3. UTC recommendation?

## Further reading

- https://www.rfc-editor.org/rfc/rfc5905
