# Exercise: 16. Routing Tables and Default Gateways

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Read a routing table
- Explain longest-prefix match
- Find default gateway
- Use ip route get / route get

## Task

Edit `exercise.sh` and implement `default_route_cidr`, `longest_prefix_wins`, `linux_route_get`. Each function is a tiny retrieval drill for **Routing Tables and Default Gateways** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/16-routing-basics/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `default_route_cidr` → `0.0.0.0/0`; `longest_prefix_wins` → `/24`; `linux_route_get` → `ip route get`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/16-routing-basics/`.**
