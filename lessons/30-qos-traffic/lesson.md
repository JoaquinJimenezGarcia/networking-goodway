---
title: "30. Latency, Bandwidth, Loss, and QoS Basics"
---

# 30. Latency, Bandwidth, Loss, and QoS Basics

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1–2 days  
**Slug:** `30-qos-traffic`

## Learning objectives

- Separate latency vs bandwidth problems
- Measure with simple tools
- Explain bufferbloat idea
- Know QoS is policy + queuing

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# rough latency
ping -c 20 1.1.1.1
# throughput tools if installed
iperf3 -c iperf.example.com
# DNS/app latency
curl -sS -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\n' https://example.com
```

Slow downloads can be bandwidth; slow pages often DNS/TLS/TTFB/app.

## Common mistakes

- Buying more bandwidth for a latency-bound app
- Ignoring Wi-Fi interference
- No baseline metrics

## Exercises

Work in `exercises/30-qos-traffic/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/30-qos-traffic/` until after an honest attempt.**

## Self-check

1. TTFB meaning?
2. ping measures what?
3. Bandwidth fix won't help when?

## Further reading

- https://www.bufferbloat.net/projects/
