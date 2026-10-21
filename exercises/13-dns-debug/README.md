# Exercise: 13. DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Differentiate NXDOMAIN vs timeout vs SERVFAIL
- Inspect /etc/resolv.conf and systemd-resolved
- Debug search domains
- Handle private DNS vs public DNS conflicts

## Task

Edit `exercise.sh` and implement `nxdomain_means`, `servfail_means`, `split_dns_name`. Each function is a tiny retrieval drill for **DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/13-dns-debug/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `nxdomain_means` → `name-not-exist`; `servfail_means` → `resolver-error`; `split_dns_name` → `split-horizon`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/13-dns-debug/`.**
