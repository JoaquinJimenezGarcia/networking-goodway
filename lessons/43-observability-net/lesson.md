---
title: "43. Network Observability: Metrics, Logs, Traces"
---

# 43. Network Observability: Metrics, Logs, Traces

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1–2 days  
**Slug:** `43-observability-net`

## Learning objectives

- Define golden network signals
- Instrument latency/errors from clients
- Use flow logs conceptually
- Correlate app traces with net failures

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Signals: reachability, RTT, loss, DNS latency, TLS latency, saturation, error rates.

```bash
# continuous simple probe
while true; do
  curl -sS -o /dev/null -w '%{http_code} %{time_total}\n' https://example.com || echo fail
  sleep 2
done
```

Cloud flow logs / VPC logs help prove whether packets left a NIC/SG.

## Common mistakes

- Metrics without alerts
- Only average latency
- No probe from multiple regions

## Exercises

Work in `exercises/43-observability-net/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/43-observability-net/` until after an honest attempt.**

## Self-check

1. Name four golden signals
2. Why percentiles?
3. Flow logs help prove what?

## Further reading

- https://sre.google/sre-book/monitoring-distributed-systems/
