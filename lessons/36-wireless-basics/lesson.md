---
title: "36. Wi-Fi Networking Essentials"
---

# 36. Wi-Fi Networking Essentials

**Phase:** Phase 7 — L2, switching, and local nets  
**Estimated time:** 1 day  
**Slug:** `36-wireless-basics`

## Learning objectives

- SSID/BSSID/RSSI concepts
- Distinguish Wi-Fi vs ethernet failures
- Scan networks on Linux/macOS
- Know channels/interference exist

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Linux (if available)
iwdev wlan0 link
iwlist wlan0 scan 2>/dev/null | head
nmcli device wifi list

# macOS
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
```

Many "network down" tickets are Wi-Fi; wire in to isolate.

## Common mistakes

- Debugging TCP apps while on captive portal
- Ignoring 2.4GHz congestion
- VPN+Wi-Fi Power save weirdness

## Exercises

Work in `exercises/36-wireless-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/36-wireless-basics/` until after an honest attempt.**

## Self-check

1. SSID vs BSSID?
2. First isolation step?
3. RSSI rough meaning?

## Further reading

- https://linuxwireless.sipsolutions.net/
