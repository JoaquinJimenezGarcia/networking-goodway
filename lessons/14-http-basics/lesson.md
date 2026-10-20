---
title: "14. HTTP from the CLI: curl Mastery"
---

# 14. HTTP from the CLI: curl Mastery

**Phase:** Phase 5 — HTTP, TLS, and APIs  
**Estimated time:** 2 days  
**Slug:** `14-http-basics`

## Learning objectives

- Use curl for GET/POST/headers/status
- Follow redirects consciously
- Set timeouts for scripts
- Save bodies and write-out metrics

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
curl -I https://example.com
curl -sS -o /dev/null -w '%{http_code} %{time_total}\n' https://example.com
curl -v https://example.com 2>&1 | head -50

# headers and methods
curl -H 'Accept: application/json' https://httpbin.org/get
curl -X POST -H 'Content-Type: application/json' -d '{"a":1}' https://httpbin.org/post

# redirects
curl -I https://google.com
curl -IL https://google.com              # follow
curl --max-redirs 2 -IL https://google.com

# timeouts (critical in automation)
curl --connect-timeout 2 --max-time 10 https://example.com

# HTTP/2 / HTTP/3 if supported
curl -I --http2 https://example.com
curl -I --http3 https://example.com      # if build supports
```

## Common mistakes

- No timeouts in scripts
- Logging secrets in -v output
- Using -k forever

## Exercises

Work in `exercises/14-http-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/14-http-basics/` until after an honest attempt.**

## Self-check

1. Flag for headers only?
2. How print status code?
3. Why max-time?

## Further reading

- https://curl.se/docs/manpage.html
