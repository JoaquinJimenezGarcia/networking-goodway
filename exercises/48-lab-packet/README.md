# Exercise: 48. Lab: Build a Mini Network Path

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Connect two VMs via private network
- Set addresses/routes manually
- Verify with ping/curl/tcpdump
- Document the path

## Task

Edit `exercise.sh` and implement `l3_proof_tool`, `l4_proof_tool`, `dns_proof_tool`. Each function is a tiny retrieval drill for **Lab: Build a Mini Network Path** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/48-lab-packet/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `l3_proof_tool` → `ping`; `l4_proof_tool` → `nc`; `dns_proof_tool` → `dig`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/48-lab-packet/`.**
