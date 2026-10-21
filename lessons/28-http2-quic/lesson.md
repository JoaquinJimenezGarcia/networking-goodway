---
title: "28. HTTP/2, HTTP/3, and QUIC Awareness"
---

# 28. HTTP/2, HTTP/3, and QUIC Awareness

**Phase:** Phase 5 — HTTP, TLS, and APIs  
**Estimated time:** 1 day  
**Slug:** `28-http2-quic`

## Learning objectives

- Know why HTTP/2 multiplexes
- Understand QUIC runs on UDP
- Probe protocol with curl
- Relate to CDNs

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

CDN serves HTTP/3; corporate firewall UDP/443 is blocked. HTTP/2 multiplexing vs QUIC changes middlebox behavior — awareness prevents false 'site down' reports.

## Core concepts

What you must be able to explain:

- Know why HTTP/2 multiplexes
- Understand QUIC runs on UDP
- Probe protocol with curl
- Relate to CDNs

Mental model for `28-http2-quic` (exercise kind `http_version`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
curl -I https://example.com 2>&1 | head -15
```

Sample output:

```text
HTTP/2 200
content-type: text/html
cache-control: max-age=...
```

**Interpretation:** Response line and headers are L7 evidence after TCP/TLS succeeded.

### Example 2

```bash
curl -sS -o /dev/null -w 'code=%{http_code} ttfb=%{time_starttransfer} total=%{time_total} ver=%{http_version}\n' https://example.com
```

Sample output:

```text
code=200 ttfb=0.120 total=0.180 ver=2
```

**Interpretation:** Write-out metrics separate connect delay from first-byte and total time — essential for gateway/CDN debates.

### Example 3

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -subject -dates
```

Sample output:

```text
subject=CN = example.com
notBefore=...
notAfter=...
```

**Interpretation:** Certificate identity and expiry are independent of HTTP 200. SNI (`-servername`) selects the cert on shared IPs.


## Mini-lab

1. Re-type every worked command for **HTTP/2, HTTP/3, and QUIC Awareness** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Assuming HTTP/3 always faster | See common mistakes | Re-run lesson commands |
| Blocking UDP 443 enterprise-wide acci... | See common mistakes | Re-run lesson commands |
| Ignoring fallback to TCP | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for HTTP/2, HTTP/3, and QUIC Awareness

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Assuming HTTP/3 always faster
- Blocking UDP 443 enterprise-wide accidentally
- Ignoring fallback to TCP

## Exercises

Work in `exercises/28-http2-quic/`. Read that folder's `README.md` before coding.

```bash
cd exercises/28-http2-quic
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `curl_http_version_writeout`, `http3_transport`, `http3_udp_port`. Each function is a tiny retrieval drill for **HTTP/2, HTTP/3, and QUIC Awareness** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/28-http2-quic/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. HTTP/2 main benefit?
2. QUIC transport?
3. curl write-out for version?

## Further reading

- https://www.rfc-editor.org/rfc/rfc9114
