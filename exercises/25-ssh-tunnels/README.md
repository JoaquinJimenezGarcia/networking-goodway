# Exercise: 25. SSH Tunnels and Port Forwards

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Use local/remote/dynamic SSH forwards
- Access private admin UIs safely
- Avoid standing tunnels forever without need
- Combine with ProxyJump

## Task

Edit `exercise.sh` and implement `ssh_local_forward_flag`, `ssh_remote_forward_flag`, `ssh_dynamic_flag`. Each function is a tiny retrieval drill for **SSH Tunnels and Port Forwards** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/25-ssh-tunnels/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `ssh_local_forward_flag` → `-L`; `ssh_remote_forward_flag` → `-R`; `ssh_dynamic_flag` → `-D`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/25-ssh-tunnels/`.**
