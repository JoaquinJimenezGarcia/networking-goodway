# Exercise: 55. Capstone: Secure Edge for a Small App

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Terminate TLS at edge
- Reverse proxy to app
- Firewall + SSH hardening + health checks
- Probe latency/error metrics

## Task

Edit `exercise.sh` and implement `edge_should_terminate`, `forward_ip_from`, `health_checks_hit`. Each function is a tiny retrieval drill for **Capstone: Secure Edge for a Small App** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/55-capstone-edge/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `edge_should_terminate` → `TLS`; `forward_ip_from` → `trusted-proxies-only`; `health_checks_hit` → `upstream`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/55-capstone-edge/`.**
