---
title: "21. Reading Flows: Wireshark/tshark Essentials"
---

# 21. Reading Flows: Wireshark/tshark Essentials

**Phase:** Phase 11 — Observability and troubleshooting  
**Estimated time:** 1–2 days  
**Slug:** `21-wireshark-flow`

## Learning objectives

- Open pcaps in Wireshark/tshark
- Follow TCP streams
- Apply display filters
- Export objects carefully

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# tshark CLI examples
tshark -r cap.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri
tshark -r cap.pcap -Y 'dns' -c 20
tshark -r cap.pcap -q -z conv,tcp
tshark -r cap.pcap -Y 'tls.handshake.type == 1' -V | head
```

Display filter examples (Wireshark): `ip.addr==10.0.0.5`, `tcp.port==443`, `http`, `dns.flags.rcode != 0`.

## Common mistakes

- Assuming encrypted payloads are readable
- Over-trusting reassembly on packet loss
- Sharing pcaps with secrets

## Exercises

Work in `exercises/21-wireshark-flow/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/21-wireshark-flow/` until after an honest attempt.**

## Self-check

1. Follow TCP stream purpose?
2. tshark -Y meaning?
3. Filter for DNS errors idea?

## Further reading

- https://www.wireshark.org/docs/
