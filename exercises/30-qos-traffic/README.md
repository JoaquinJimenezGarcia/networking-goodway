# Exercise: 30. Latency, Bandwidth, Loss, and QoS Basics

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Separate latency vs bandwidth problems
- Measure with simple tools
- Explain bufferbloat idea
- Know QoS is policy + queuing

## Task

Edit `exercise.sh` and implement `curl_ttfb_var`, `curl_dns_time_var`, `latency_summary_stat`. Each function is a tiny retrieval drill for **Latency, Bandwidth, Loss, and QoS Basics** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/30-qos-traffic/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `curl_ttfb_var` → `%{time_starttransfer}`; `curl_dns_time_var` → `%{time_namelookup}`; `latency_summary_stat` → `percentiles`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/30-qos-traffic/`.**
