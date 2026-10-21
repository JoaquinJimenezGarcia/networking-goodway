# Exercise: 44. Networking Troubleshooting Playbook

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Apply a layered checklist
- Capture evidence before changing things
- Bisect path: local → LAN → WAN → DNS → TLS → app
- Write crisp incident notes

## Task

Edit `exercise.sh` and implement `first_troubleshoot_layer`, `after_l3_check`, `prove_listener_with`. Each function is a tiny retrieval drill for **Networking Troubleshooting Playbook** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/44-troubleshooting-playbook/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `first_troubleshoot_layer` → `local`; `after_l3_check` → `DNS`; `prove_listener_with` → `ss`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/44-troubleshooting-playbook/`.**
