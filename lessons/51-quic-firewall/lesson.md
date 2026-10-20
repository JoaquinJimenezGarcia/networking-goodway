---
title: "51. Firewalls, Middleboxes, and Modern Protocols"
---

# 51. Firewalls, Middleboxes, and Modern Protocols

**Phase:** Phase 8 — Firewalls, NAT, and policy  
**Estimated time:** 1 day  
**Slug:** `51-quic-firewall`

## Learning objectives

- Know middleboxes can break UDP/QUIC
- Test fallbacks
- Design allowlists for new protocols
- Document egress needs

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
curl -I --http3-only https://example.com || echo 'blocked or unsupported'
curl -I --http2 https://example.com
# observe which ports egress needs
nc -vzu -w 2 1.1.1.1 443 || true
```

Enterprise networks that hard-block UDP may degrade HTTP/3; apps should fallback gracefully.

## Common mistakes

- Blind UDP blocks without measurement
- Assuming middleboxes are transparent
- No inventory of required egress

## Exercises

Work in `exercises/51-quic-firewall/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/51-quic-firewall/` until after an honest attempt.**

## Self-check

1. Why UDP 443 matters?
2. What is a middlebox?
3. Fallback strategy?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9308
