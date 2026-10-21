# Exercise: 05. Subnetting and CIDR (with practice)

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Convert prefix lengths to masks
- Compute network/broadcast/usable hosts
- Choose subnets for labs
- Use `ipcalc`/`sipcalc` or manual method

## Task

Edit `exercise.sh` and implement `host_bits`, `usable_hosts_24`, `longer_prefix_means`. Each function is a tiny retrieval drill for **Subnetting and CIDR (with practice)** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 4 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/05-subnetting/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `host_bits 24` → `8`; `host_bits 26` → `6`; `usable_hosts_24` → `254`; `longer_prefix_means` → `smaller`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/05-subnetting/`.**
