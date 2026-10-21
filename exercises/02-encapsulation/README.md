# Exercise: 02. Encapsulation, Headers, and MTU

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain encapsulation/decapsulation
- Define MTU and fragmentation issues
- Use ping to probe path MTU ideas
- Recognize common header sizes intuitively

## Task

Implement `ethernet_typical_mtu`, `vpn_overhead_effect` (returns `lowers-MTU`), and `df_ping_purpose` (`probe-path-MTU`).

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/02-encapsulation/` | Peek only after a real attempt |

## Examples / expected behavior

`ethernet_typical_mtu` → `1500`; `vpn_overhead_effect` → `lowers-MTU`; `df_ping_purpose` → `probe-path-MTU`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/02-encapsulation/`.**
