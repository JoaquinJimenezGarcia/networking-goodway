# Exercise: 09. ss, netstat, and lsof: See What Is Listening

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- List listening sockets and established connections
- Map ports to processes
- Use lsof for file/socket detectives
- Spot TIME_WAIT / CLOSE_WAIT patterns

## Task

Edit `exercise.sh` and implement `ss_listen_flags`, `legacy_netstat`, `files_ports_tool`. Each function is a tiny retrieval drill for **ss, netstat, and lsof: See What Is Listening** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/09-ss-netstat-lsof/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `ss_listen_flags` → `-tulpn`; `legacy_netstat` → `netstat`; `files_ports_tool` → `lsof`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/09-ss-netstat-lsof/`.**
