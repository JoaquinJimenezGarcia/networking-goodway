---
title: "15. TLS, Certificates, and openssl s_client"
---

# 15. TLS, Certificates, and openssl s_client

**Phase:** Phase 5 — HTTP, TLS, and APIs  
**Estimated time:** 2 days  
**Slug:** `15-tls-openssl`

## Learning objectives

- Inspect remote certificates
- Check expiry and SANs
- Understand chain of trust
- Test TLS versions/ciphers at a basic level

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates

echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -ext subjectAltName

# show chain
echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null | head -80

# expiry monitoring style
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -enddate

# curl certificate peek
curl -vI https://example.com 2>&1 | grep -E 'SSL|subject|expire|issuer'
```

## Common mistakes

- Disabling verification with -k in production
- Missing intermediate certs
- Not monitoring expiry

## Exercises

Work in `exercises/15-tls-openssl/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/15-tls-openssl/` until after an honest attempt.**

## Self-check

1. Why servername/SNI?
2. How view expiry?
3. What is a SAN?

## Further reading

- https://www.openssl.org/docs/man3.0/man1/openssl-s_client.html
