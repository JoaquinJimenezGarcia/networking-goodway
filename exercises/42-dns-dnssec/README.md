# Exercise: 42. DNSSEC and DNS Security Awareness

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Know what DNSSEC protects
- See AD flag in dig
- Understand it does not encrypt DNS
- Prefer DoH/DoT for privacy

## Task

Edit `exercise.sh` and implement `dnssec_protects`, `dnssec_not_encrypt`, `dnssec_fail_closed_idea`. Each function is a tiny retrieval drill for **DNSSEC and DNS Security Awareness** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/42-dns-dnssec/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `dnssec_protects` → `authenticity`; `dnssec_not_encrypt` → `privacy`; `dnssec_fail_closed_idea` → `yes`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/42-dns-dnssec/`.**
