# Exercise: 21. Reading Flows: Wireshark/tshark Essentials

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Open pcaps in Wireshark/tshark
- Follow TCP streams
- Apply display filters
- Export objects carefully

## Task

Edit `exercise.sh` and implement `tshark_display_filter_flag`, `tshark_read_flag`, `packet_gui_tool`. Each function is a tiny retrieval drill for **Reading Flows: Wireshark/tshark Essentials** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/21-wireshark-flow/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `tshark_display_filter_flag` → `-Y`; `tshark_read_flag` → `-r`; `packet_gui_tool` → `wireshark`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/21-wireshark-flow/`.**
