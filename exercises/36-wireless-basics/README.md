# Exercise: 36. Wi-Fi Networking Essentials

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- SSID/BSSID/RSSI concepts
- Distinguish Wi-Fi vs ethernet failures
- Scan networks on Linux/macOS
- Know channels/interference exist

## Task

Edit `exercise.sh` and implement `wifi_name_broadcast`, `wifi_layer_family`, `wifi_symptom`. Each function is a tiny retrieval drill for **Wi-Fi Networking Essentials** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/36-wireless-basics/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `wifi_name_broadcast` → `SSID`; `wifi_layer_family` → `L1-L2`; `wifi_symptom` → `drops`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/36-wireless-basics/`.**
