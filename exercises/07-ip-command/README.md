# Exercise: 07. The ip Command Deep Dive (addr, link, route)

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Use ip addr/link/route fluently
- Bring interfaces up/down (lab)
- Add/delete routes temporarily
- Prefer ip over deprecated ifconfig on Linux

## Task

Edit `exercise.sh` and implement `cmd_route_get`, `cmd_addr_brief`, `cmd_link_show`. Each function is a tiny retrieval drill for **The ip Command Deep Dive (addr, link, route)** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/07-ip-command/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `cmd_route_get` → `ip route get`; `cmd_addr_brief` → `ip -br addr`; `cmd_link_show` → `ip link`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/07-ip-command/`.**
