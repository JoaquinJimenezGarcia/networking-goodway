# Exercise: 54. Capstone: Broken Network Challenge

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Debug planted failures
- Produce timeline + root cause
- Fix with minimal change
- Write postmortem

## Task

Edit `exercise.sh` and implement `postmortem_must_include`, `postmortem_timeline`, `postmortem_verify`. Each function is a tiny retrieval drill for **Capstone: Broken Network Challenge** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/54-capstone-debug/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `postmortem_must_include` → `root-cause`; `postmortem_timeline` → `yes`; `postmortem_verify` → `yes`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/54-capstone-debug/`.**
