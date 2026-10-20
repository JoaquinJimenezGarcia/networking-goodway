---
title: "42. DNSSEC and DNS Security Awareness"
---

# 42. DNSSEC and DNS Security Awareness

**Phase:** Phase 4 — DNS  
**Estimated time:** 1 day  
**Slug:** `42-dns-dnssec`

## Learning objectives

- Know what DNSSEC protects
- See AD flag in dig
- Understand it does not encrypt DNS
- Prefer DoH/DoT for privacy

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
dig example.com +dnssec +noall +answer +comments
dig example.com +dnssec | grep -E 'flags:|RRSIG'
# DoH example via curl
curl -sH 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=example.com&type=A' | head -c 200; echo
```

DNSSEC → authenticity/integrity. DoH/DoT → privacy on path to resolver.

## Common mistakes

- Thinking DNSSEC hides queries
- Broken middleboxes failing DNSSEC validation
- No monitoring of DNSSEC expirations for your zones

## Exercises

Work in `exercises/42-dns-dnssec/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/42-dns-dnssec/` until after an honest attempt.**

## Self-check

1. DNSSEC vs DoH?
2. dig flag to request DNSSEC records?
3. What problem DNSSEC does not solve?

## Further reading

- https://www.rfc-editor.org/rfc/rfc4033
