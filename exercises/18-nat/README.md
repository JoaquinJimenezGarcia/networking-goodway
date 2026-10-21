# Exercise: 18. NAT, PAT, and Hairpinning

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain source NAT / PAT for internet egress
- Understand destination NAT / port forwards
- Spot NAT in troubleshooting
- Know hairpin NAT issues

## Task

Edit `exercise.sh` and implement `many_to_one_nat_name`, `hairpin_name`, `iptables_nat_table`. Each function is a tiny retrieval drill for **NAT, PAT, and Hairpinning** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/18-nat/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `many_to_one_nat_name` → `PAT`; `hairpin_name` → `hairpin`; `iptables_nat_table` → `nat`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/18-nat/`.**
