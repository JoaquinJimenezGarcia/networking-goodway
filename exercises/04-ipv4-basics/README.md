# Exercise: 04. IPv4 Basics: Addresses, Classes Myth, Private Ranges

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Read IPv4 addresses and dotted decimal
- Know RFC1918 private ranges
- Explain public vs private vs loopback
- Use commands to show addresses on a host

## Task

Edit `exercise.sh` and implement `is_private`, `loopback_cidr`, `link_local_prefix`. Each function is a tiny retrieval drill for **IPv4 Basics: Addresses, Classes Myth, Private Ranges** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 4 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/04-ipv4-basics/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `is_private 10.0.0.1` → `yes`; `is_private 8.8.8.8` → `no`; `loopback_cidr` → `127.0.0.0/8`; `link_local_prefix` → `169.254`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/04-ipv4-basics/`.**
