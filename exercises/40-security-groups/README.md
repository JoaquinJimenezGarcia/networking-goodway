# Exercise: 40. Security Groups vs NACLs vs Host Firewalls

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Contrast SG/NACL/host firewall layers
- Write least-privilege allowlists
- Debug timeouts vs resets
- Trace which layer drops

## Task

Edit `exercise.sh` and implement `packet_drop_often_looks_like`, `sg_statefulness`, `nacl_statefulness`. Each function is a tiny retrieval drill for **Security Groups vs NACLs vs Host Firewalls** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/40-security-groups/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `packet_drop_often_looks_like` → `timeout`; `sg_statefulness` → `stateful`; `nacl_statefulness` → `stateless`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/40-security-groups/`.**
