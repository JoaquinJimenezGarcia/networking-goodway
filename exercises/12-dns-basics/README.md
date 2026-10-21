# Exercise: 12. DNS Basics: Resolvers, Records, dig

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Query A/AAAA/CNAME/MX/TXT/NS
- Explain recursive vs authoritative
- Use dig/drill/nslookup
- Read TTL and caching implications

## Task

Edit `exercise.sh` and implement `dig_short_flags`, `dns_type_a`, `dns_type_mx`. Each function is a tiny retrieval drill for **DNS Basics: Resolvers, Records, dig** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/12-dns-basics/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `dig_short_flags` → `+short`; `dns_type_a` → `A`; `dns_type_mx` → `MX`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/12-dns-basics/`.**
