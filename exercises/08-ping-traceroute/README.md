# Exercise: 08. ping, traceroute/mtr, and Path Diagnosis

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Use ping meaningfully (and know its limits)
- Read traceroute hops
- Use mtr for combined view
- Distinguish loss at hop vs destination

## Task

Edit `exercise.sh` and implement `ping_three`, `path_hop_tool`, `loss_path_tool`. Each function is a tiny retrieval drill for **ping, traceroute/mtr, and Path Diagnosis** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/08-ping-traceroute/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `ping_three` → `ping -c 3`; `path_hop_tool` → `traceroute`; `loss_path_tool` → `mtr`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/08-ping-traceroute/`.**
