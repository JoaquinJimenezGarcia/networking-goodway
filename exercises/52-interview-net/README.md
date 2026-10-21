# Exercise: 52. Networking Interview & Oncall Drills

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain issues aloud with structure
- Whiteboard a path
- Solve timed scenarios
- Prioritize user impact

## Task

Edit `exercise.sh` and implement `verify_after_fix`, `hypothesis_first`, `one_layer_at_a_time`. Each function is a tiny retrieval drill for **Networking Interview & Oncall Drills** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/52-interview-net/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `verify_after_fix` → `yes`; `hypothesis_first` → `yes`; `one_layer_at_a_time` → `yes`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/52-interview-net/`.**
