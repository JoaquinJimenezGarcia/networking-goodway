# Exercise: 43. Network Observability: Metrics, Logs, Traces

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Define golden network signals
- Instrument latency/errors from clients
- Use flow logs conceptually
- Correlate app traces with net failures

## Task

Edit `exercise.sh` and implement `latency_better_as`, `third_obs_pillar`, `synthetic_check_name`. Each function is a tiny retrieval drill for **Network Observability: Metrics, Logs, Traces** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/43-observability-net/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `latency_better_as` → `percentiles`; `third_obs_pillar` → `traces`; `synthetic_check_name` → `probe`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/43-observability-net/`.**
