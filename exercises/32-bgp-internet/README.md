# Exercise: 32. How the Internet Routes: BGP at a Glance

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain ASNs and prefixes
- Understand announcements/withdrawals
- Use looking glasses / whois / bgp tools
- Know why leaks/hijacks matter

## Task

Edit `exercise.sh` and implement `asn_means`, `as_route_protocol`, `ip_block_name`. Each function is a tiny retrieval drill for **How the Internet Routes: BGP at a Glance** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/32-bgp-internet/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `asn_means` → `autonomous-system-number`; `as_route_protocol` → `BGP`; `ip_block_name` → `prefixes`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/32-bgp-internet/`.**
