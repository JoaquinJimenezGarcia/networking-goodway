---
title: "34. Email Networking: MX, SPF, DKIM, DMARC"
---

# 34. Email Networking: MX, SPF, DKIM, DMARC

**Phase:** Phase 4 — DNS  
**Estimated time:** 1–2 days  
**Slug:** `34-email-dns`

## Learning objectives

- Query MX records
- Read SPF TXT basics
- Know DKIM/DMARC roles
- Debug delivery with headers

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
dig example.com MX +short
dig example.com TXT +short
dig _dmarc.example.com TXT +short
# DKIM selectors vary; example pattern:
# dig selector._domainkey.example.com TXT +short
```

SPF authorizes senders; DKIM signs messages; DMARC policy aligns them. Networking + DNS + mail servers intertwine.

## Common mistakes

- Permissive SPF (+all)
- No DMARC on important domains
- Forgetting PTR for mail IPs

## Exercises

Work in `exercises/34-email-dns/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/34-email-dns/` until after an honest attempt.**

## Self-check

1. MX purpose?
2. SPF stored as what record?
3. DMARC policy domain pattern?

## Further reading

- https://www.rfc-editor.org/rfc/rfc7208
