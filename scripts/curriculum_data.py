#!/usr/bin/env python3
"""Networking Goodway curriculum modules 00–55 (command-heavy)."""

from __future__ import annotations

MODULES: list[dict] = []


def add(n, slug, title, phase, days, objectives, body, pitfalls, checks, reading, ex_kind):
    MODULES.append(
        dict(
            n=n,
            slug=f"{n:02d}-{slug}",
            title=title,
            phase=phase,
            days=days,
            objectives=objectives,
            body=body,
            pitfalls=pitfalls,
            checks=checks,
            reading=reading,
            ex_kind=ex_kind,
        )
    )


P0 = "Phase 0 — Orientation"
P1 = "Phase 1 — Models and packets"
P2 = "Phase 2 — Addressing and subnets"
P3 = "Phase 3 — Host networking toolkit"
P4 = "Phase 4 — DNS"
P5 = "Phase 5 — HTTP, TLS, and APIs"
P6 = "Phase 6 — Routing"
P7 = "Phase 7 — L2, switching, and local nets"
P8 = "Phase 8 — Firewalls, NAT, and policy"
P9 = "Phase 9 — VPN, tunnels, and overlays"
P10 = "Phase 10 — Load balancing and proxies"
P11 = "Phase 11 — Observability and troubleshooting"
P12 = "Phase 12 — Cloud, containers, and modern nets"
P13 = "Phase 13 — Capstones"

add(
    0,
    "orientation",
    "Orientation: How Networks Work and How to Practice",
    P0,
    "1 day",
    [
        "Explain clients, servers, packets, and protocols at a beginner level",
        "Set up a safe practice lab (VM + localhost tools)",
        "Adopt attempt → struggle → solution → rewrite",
        "Know which tools you will use daily",
    ],
    """
## Mental model

A **network** moves messages between programs on machines.

- **Host**: a computer with one or more network interfaces
- **Packet/frame**: a chunk of data with headers (addresses, ports, etc.)
- **Protocol**: agreed rules (IP, TCP, UDP, HTTP, DNS, …)
- **Port**: number identifying an application endpoint on a host

```text
Browser  --HTTP-->  Web server
   |                   |
  TCP                 TCP
   |                   |
  IP                  IP
   +-------- link -----+
```

## Practice lab

1. Your laptop terminal (many commands work on macOS/Linux)
2. A Linux VM for `ip`, `ss`, `nft`, systemd-resolved
3. Optional second VM to ping/ssh between hosts

## Daily toolkit (you will master these)

```bash
ping -c 3 1.1.1.1
traceroute example.com          # or traceroute / tracert
dig example.com +short
curl -I https://example.com
ss -tulpn                       # Linux; macOS: netstat -anv
ip addr                         # Linux; macOS: ifconfig / ipconfig getifaddr en0
```

## Study method

Read PDF → type every example → finish `exercises/NN-*/` (`./test.sh`) → only then open solutions → rewrite next day.
""",
    [
        "Only reading without typing commands",
        "Practicing against production systems without approval",
        "Skipping fundamentals and jumping to cloud GUIs",
    ],
    [
        "What is a port?",
        "Name five daily networking commands",
        "Why use a lab VM?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc1122"],
    "orient_hello",
)

add(
    1,
    "osi-tcpip",
    "OSI vs TCP/IP Models (with packet walkthrough)",
    P1,
    "1–2 days",
    [
        "Map OSI layers to TCP/IP layers",
        "Trace a request layer-by-layer",
        "Identify which tool inspects which layer",
        "Stop mixing L2/L3/L4 terms casually",
    ],
    """
## Useful mapping

| OSI idea | TCP/IP | Examples | Tools |
|----------|--------|----------|-------|
| L7 App | App | HTTP, DNS, SSH | curl, dig, openssl |
| L4 Transport | TCP/UDP | ports, reliability | ss, netstat, nc |
| L3 Network | IP | routing, ICMP | ip route, ping, traceroute |
| L2 Data link | Ethernet/Wi-Fi | MAC, ARP | ip neigh, arp, tcpdump -e |
| L1 Physical | wires/radio | link up/down | ip link, ethtool |

## Packet walk (simplified)

Opening `https://example.com`:

1. DNS (app) resolves name → IP (`dig`)
2. TCP connects to `IP:443` (handshake)
3. TLS negotiates encryption (`openssl s_client`)
4. HTTP request/response (`curl -v`)

```bash
# See layers in one debug session
dig example.com +short
ping -c 2 example.com
curl -vI https://example.com 2>&1 | head -40
```
""",
    [
        "Calling IP addresses \"MAC addresses\"",
        "Thinking HTTPS replaces TCP",
        "Blaming DNS for every failure without evidence",
    ],
    [
        "Which layer are ports?",
        "Which layer are MAC addresses?",
        "Where does TLS sit relative to TCP?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc1122"],
    "layer_ports",
)

add(
    2,
    "encapsulation",
    "Encapsulation, Headers, and MTU",
    P1,
    "1–2 days",
    [
        "Explain encapsulation/decapsulation",
        "Define MTU and fragmentation issues",
        "Use ping to probe path MTU ideas",
        "Recognize common header sizes intuitively",
    ],
    """
## Encapsulation

Each layer wraps the payload from above:

```text
[Eth][IP][TCP][HTTP data........]
```

## MTU

Maximum payload size on a link (Ethernet often 1500). Too-large packets may fragment or drop (especially with VPN overhead).

```bash
# Linux: show interface MTU
ip link show
# Probe large ping (may need root / may be blocked)
ping -c 2 -M do -s 1472 1.1.1.1    # Linux DF bit
ping -c 2 -D -s 1472 1.1.1.1       # macOS-style
```

## tcpdump glimpse

```bash
sudo tcpdump -ni any -c 5 icmp
sudo tcpdump -ni eth0 -c 5 host example.com and port 443
```
""",
    [
        "Ignoring MTU after adding VPN/overlays",
        "Blackhole path MTU (DF set, ICMP blocked)",
        "Capturing on the wrong interface",
    ],
    [
        "What does MTU mean?",
        "Why do VPNs lower effective MTU?",
        "Name a capture tool",
    ],
    ["https://www.rfc-editor.org/rfc/rfc1191"],
    "mtu_quiz",
)

add(
    3,
    "ethernet-mac-arp",
    "Ethernet, MAC Addresses, and ARP",
    P7,
    "1–2 days",
    [
        "Read MAC addresses and ARP tables",
        "Explain ARP purpose on a LAN",
        "Detect basic ARP issues",
        "Use neighbor tables on modern Linux",
    ],
    """
## Commands

```bash
# Linux
ip link show
ip neigh show
ip -s link
# older
arp -n

# macOS
ifconfig en0
arp -an
```

ARP maps **IP → MAC** on the local subnet so frames can be delivered.

```bash
ping -c 1 192.168.1.1
ip neigh show          # entry should appear as REACHABLE/DELAY/...
```

## Useful tcpdump for ARP

```bash
sudo tcpdump -ni eth0 arp
```
""",
    [
        "Expecting ARP to work across routers (it doesn't)",
        "Duplicate IPs causing flapping ARP",
        "Hardcoding MAC allowlists without ops process",
    ],
    [
        "ARP maps what to what?",
        "Does ARP cross routers?",
        "Command to show neighbors on Linux?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc826"],
    "arp_map",
)

add(
    4,
    "ipv4-basics",
    "IPv4 Basics: Addresses, Classes Myth, Private Ranges",
    P2,
    "1–2 days",
    [
        "Read IPv4 addresses and dotted decimal",
        "Know RFC1918 private ranges",
        "Explain public vs private vs loopback",
        "Use commands to show addresses on a host",
    ],
    """
## Special addresses

| Range | Meaning |
|-------|---------|
| 127.0.0.0/8 | loopback |
| 10.0.0.0/8 | private |
| 172.16.0.0/12 | private |
| 192.168.0.0/16 | private |
| 169.254.0.0/16 | link-local (APIPA) |
| 0.0.0.0/0 | default route |

```bash
# Linux
ip -4 addr show
ip route show
# macOS
ipconfig getifaddr en0
route -n get default
# both
ping -c 2 127.0.0.1
```

## Check public IP (from host)

```bash
curl -4 ifconfig.me
curl -4 https://api.ipify.org
dig +short myip.opendns.com @resolver1.opendns.com
```
""",
    [
        "Assuming classful addressing still rules the internet",
        "Using public IPs on lab LANs carelessly",
        "Confusing link-local with routable",
    ],
    [
        "Name three private ranges",
        "What is 127.0.0.1?",
        "How print IPv4 addresses on Linux?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc1918"],
    "ipv4_private",
)

add(
    5,
    "subnetting",
    "Subnetting and CIDR (with practice)",
    P2,
    "2–3 days",
    [
        "Convert prefix lengths to masks",
        "Compute network/broadcast/usable hosts",
        "Choose subnets for labs",
        "Use `ipcalc`/`sipcalc` or manual method",
    ],
    """
## CIDR quick facts

`192.168.10.0/24` → mask `255.255.255.0` → 256 addresses → 254 usable (typical).

Host bits = 32 - prefix. Usable ≈ 2^hostbits − 2 (except some special cases).

```bash
# If installed
ipcalc 192.168.10.0/24
sipcalc 10.0.0.0/12

# Python one-liner helper (lab)
python3 - <<'PY'
import ipaddress
n=ipaddress.ip_network('192.168.10.0/24')
print(n.network_address, n.broadcast_address, n.num_addresses)
PY
```

## Common prefixes

| Prefix | Hosts (approx usable) | Typical use |
|--------|-----------------------|-------------|
| /32 | 1 | single host route |
| /30 | 2 | point-to-point |
| /24 | 254 | small LAN |
| /16 | ~65k | large private |
| /0 | default | everything |
""",
    [
        "Off-by-one in usable host counts",
        "Overlapping subnets in VPCs",
        "Using /24 everywhere without design",
    ],
    [
        "How many host bits in /26?",
        "What does /32 mean?",
        "Why avoid overlapping CIDRs?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc4632"],
    "cidr_hosts",
)

add(
    6,
    "ipv6-basics",
    "IPv6 Basics and Dual-Stack Commands",
    P2,
    "1–2 days",
    [
        "Read IPv6 addresses and `::` compression",
        "Know link-local `fe80::/10`",
        "Query AAAA records",
        "Test connectivity with ping6/curl -6",
    ],
    """
```bash
# Addresses
ip -6 addr show                 # Linux
ifconfig en0 | grep inet6       # macOS

# DNS AAAA
dig example.com AAAA +short
dig -t AAAA example.com +short

# Connectivity
ping6 -c 2 2606:4700:4700::1111
curl -6 -I https://example.com
curl -6 https://api64.ipify.org

# Prefer v4 or v6 in curl
curl -4 -I https://example.com
curl -6 -I https://example.com
```

Link-local addresses need a scope/interface: `fe80::1%eth0`.
""",
    [
        "Forgetting `%iface` on link-local",
        "Disabling IPv6 and breaking dual-stack apps randomly",
        "Assuming no AAAA means host is down",
    ],
    [
        "What starts with fe80::?",
        "How query AAAA with dig?",
        "curl flag to force IPv6?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc8200"],
    "ipv6_aaaa",
)

add(
    7,
    "ip-command",
    "The ip Command Deep Dive (addr, link, route)",
    P3,
    "2 days",
    [
        "Use ip addr/link/route fluently",
        "Bring interfaces up/down (lab)",
        "Add/delete routes temporarily",
        "Prefer ip over deprecated ifconfig on Linux",
    ],
    """
## Essential `ip` examples (Linux)

```bash
ip addr show
ip -br addr                         # brief
ip link show
ip link set eth0 up
ip link set eth0 down

ip route show
ip route get 1.1.1.1                # which path would kernel use?
ip route add 10.50.0.0/16 via 10.0.0.1
ip route del 10.50.0.0/16

ip -s link show eth0                # counters RX/TX errors
ip monitor all                      # watch changes live
```

## macOS cousins

```bash
ifconfig
route -n get default
networksetup -listallhardwareports
```
""",
    [
        "Making persistent mistakes thinking `ip route add` survives reboot (needs netplan/NetworkManager/systemd-networkd)",
        "typos adding routes that blackhole traffic",
        "changing production without console access",
    ],
    [
        "Command to show routes?",
        "What does `ip route get` do?",
        "Brief address listing flag?",
    ],
    ["https://man7.org/linux/man-pages/man8/ip.8.html"],
    "ip_route_get",
)

add(
    8,
    "ping-traceroute",
    "ping, traceroute/mtr, and Path Diagnosis",
    P3,
    "1–2 days",
    [
        "Use ping meaningfully (and know its limits)",
        "Read traceroute hops",
        "Use mtr for combined view",
        "Distinguish loss at hop vs destination",
    ],
    """
```bash
ping -c 5 1.1.1.1
ping -c 5 -W 1 example.com          # timeout per probe (Linux)
ping -c 5 -t 1 example.com          # macOS timeout seconds

traceroute example.com
traceroute -n example.com           # numeric, no DNS delay
# Linux often:
tracepath example.com

# Best interactive tool if installed:
mtr -rwzc 50 example.com
mtr -6 example.com
```

**ICMP may be rate-limited or blocked.** Failed ping ≠ host down. Correlate with TCP checks (`curl`, `nc`).

```bash
# TCP-aware path tools (if installed)
tcptraceroute example.com 443
```
""",
    [
        "Declaring outage from a single ping fail",
        "Misreading traceroute stars as always \"down\"",
        "No DNS-less (`-n`) when DNS is broken",
    ],
    [
        "Why ping can lie?",
        "What does mtr combine?",
        "Why traceroute -n?",
    ],
    ["https://www.rfc-editor.org/rfc/rfc792"],
    "ping_count",
)

add(
    9,
    "ss-netstat-lsof",
    "ss, netstat, and lsof: See What Is Listening",
    P3,
    "1–2 days",
    [
        "List listening sockets and established connections",
        "Map ports to processes",
        "Use lsof for file/socket detectives",
        "Spot TIME_WAIT / CLOSE_WAIT patterns",
    ],
    """
```bash
# Linux preferred
ss -tulpn
ss -s
ss -tan state established
ss -tan 'sport = :443'
ss -tanp | head

# macOS / older
netstat -anv
netstat -an | grep LISTEN

# Who owns a port?
sudo lsof -iTCP:22 -sTCP:LISTEN
sudo lsof -i :5432
sudo fuser -v 80/tcp                 # Linux psmisc
```

## Reading states

- `LISTEN` — server waiting
- `ESTAB`/`ESTABLISHED` — connected
- `TIME-WAIT` — normal after close (high volume can be OK)
- `CLOSE-WAIT` — often app not closing sockets (bug)
""",
    [
        "Killing TIME_WAIT thinking it's a leak",
        "Forgetting sudo for process names in ss -p",
        "Ignoring IPv6 listeners (`ss -tulpn` shows both)",
    ],
    [
        "ss flags for TCP/UDP listen + process?",
        "lsof command for port 22?",
        "CLOSE-WAIT often means?",
    ],
    ["https://man7.org/linux/man-pages/man8/ss.8.html"],
    "ss_flags",
)

add(
    10,
    "nc-socat",
    "nc/ncat and socat: Swiss Army Networking",
    P3,
    "1–2 days",
    [
        "Test TCP/UDP ports with nc",
        "Create quick lab listeners",
        "Banner-grab carefully in labs",
        "Know socat for advanced relays",
    ],
    """
```bash
# Port check
nc -vz example.com 443
nc -vz -w 3 10.0.0.5 22
# UDP (partial signal)
nc -vzu 1.1.1.1 53

# Quick listener (lab only)
nc -l 9090
# other terminal:
echo hello | nc 127.0.0.1 9090

# HTTP over nc (lab)
printf 'GET / HTTP/1.0\\r\\nHost: example.com\\r\\n\\r\\n' | nc example.com 80 | head

# socat examples (if installed)
socat - TCP:example.com:80
socat TCP-LISTEN:8080,fork TCP:127.0.0.1:80
```

Use only on systems you own/are allowed to test.
""",
    [
        "Leaving lab listeners on 0.0.0.0 in untrusted networks",
        "Assuming UDP nc success means healthy service",
        "Using nc for production TLS (prefer openssl/curl)",
    ],
    [
        "nc flag for zero-I/O port scan style connect?",
        "How listen on 9090?",
        "Why UDP checks are weaker?",
    ],
    ["https://nmap.org/ncat/"],
    "nc_vz",
)

add(11, "tcp-udp", "TCP vs UDP, Handshakes, and Reliability", P1, "1–2 days",
    ["Contrast TCP and UDP properties", "Explain three-way handshake conceptually", "Know when UDP is preferred", "Observe TCP with ss/tcpdump"],
    """
## TCP vs UDP

| | TCP | UDP |
|---|-----|-----|
| Connection | yes | no |
| Reliable delivery | yes | best-effort |
| Ordered | yes | no |
| Use cases | HTTP, SSH | DNS, QUIC/games, media |

```bash
# Established TCP
ss -tan state established | head
# Capture handshake (lab)
sudo tcpdump -ni any -c 20 'tcp[tcpflags] & (tcp-syn) != 0'
# UDP DNS
sudo tcpdump -ni any -c 5 udp port 53
```

SYN → SYN-ACK → ACK establishes TCP. FIN/RST close or reset.
""",
    ["Using UDP and expecting TCP guarantees", "SYN floods without rate limits", "Forcing TCP where UDP+app reliability fits"],
    ["Three-way handshake steps?", "Is DNS always UDP?", "Command to show established TCP?"],
    ["https://www.rfc-editor.org/rfc/rfc9293"],
    "tcp_vs_udp")

add(12, "dns-basics", "DNS Basics: Resolvers, Records, dig", P4, "2 days",
    ["Query A/AAAA/CNAME/MX/TXT/NS", "Explain recursive vs authoritative", "Use dig/drill/nslookup", "Read TTL and caching implications"],
    """
```bash
dig example.com A +short
dig example.com AAAA +short
dig example.com NS +short
dig example.com MX +short
dig example.com TXT +short
dig www.github.com CNAME +short

dig example.com +noall +answer
dig @1.1.1.1 example.com A
dig example.com +trace                 # walk from root (noisy)

# reverse DNS
dig -x 1.1.1.1 +short

# see full timing
dig example.com | grep -E 'Query time|SERVER'
```

```bash
# macOS/Linux alternatives
host example.com
nslookup example.com
getent hosts example.com
```
""",
    ["Flushing caches randomly as first step", "Ignoring TTL when debugging 'still old IP'", "Using +trace against rate-limited networks carelessly"],
    ["dig for AAAA?", "What is +short?", "Recursive vs authoritative?"],
    ["https://www.rfc-editor.org/rfc/rfc1035"],
    "dig_short")

add(13, "dns-debug", "DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon", P4, "1–2 days",
    ["Differentiate NXDOMAIN vs timeout vs SERVFAIL", "Inspect /etc/resolv.conf and systemd-resolved", "Debug search domains", "Handle private DNS vs public DNS conflicts"],
    """
```bash
cat /etc/resolv.conf
resolvectl status                 # systemd-resolved
resolvectl query example.com

# Compare resolvers
dig @8.8.8.8 internal.corp.example A +time=2
dig @10.0.0.2 internal.corp.example A +time=2

# Common response codes in dig output: NOERROR, NXDOMAIN, SERVFAIL, REFUSED
dig not-a-real-domain-xyz.invalid A
```

**Split-horizon**: internal and public names return different answers — corporate VPN classic.
""",
    ["Pointing corp laptops at 8.8.8.8 and breaking private zones", "Ignoring search domain appending", "Hardcoding IPs forever instead of fixing DNS"],
    ["NXDOMAIN meaning?", "SERVFAIL meaning?", "Why VPN DNS matters?"],
    ["https://man7.org/linux/man-pages/man5/resolv.conf.5.html"],
    "dns_nx")

add(14, "http-basics", "HTTP from the CLI: curl Mastery", P5, "2 days",
    ["Use curl for GET/POST/headers/status", "Follow redirects consciously", "Set timeouts for scripts", "Save bodies and write-out metrics"],
    """
```bash
curl -I https://example.com
curl -sS -o /dev/null -w '%{http_code} %{time_total}\\n' https://example.com
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
""",
    ["No timeouts in scripts", "Logging secrets in -v output", "Using -k forever"],
    ["Flag for headers only?", "How print status code?", "Why max-time?"],
    ["https://curl.se/docs/manpage.html"],
    "curl_code")

add(15, "tls-openssl", "TLS, Certificates, and openssl s_client", P5, "2 days",
    ["Inspect remote certificates", "Check expiry and SANs", "Understand chain of trust", "Test TLS versions/ciphers at a basic level"],
    """
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
""",
    ["Disabling verification with -k in production", "Missing intermediate certs", "Not monitoring expiry"],
    ["Why servername/SNI?", "How view expiry?", "What is a SAN?"],
    ["https://www.openssl.org/docs/man3.0/man1/openssl-s_client.html"],
    "tls_enddate")

add(16, "routing-basics", "Routing Tables and Default Gateways", P6, "1–2 days",
    ["Read a routing table", "Explain longest-prefix match", "Find default gateway", "Use ip route get / route get"],
    """
```bash
# Linux
ip route
ip route show table main
ip route get 1.1.1.1
ip route get 10.0.0.5 from 10.0.0.10 iif eth0

# macOS
netstat -rn
route -n get default
route -n get 1.1.1.1
```

**Longest prefix match**: more specific routes win (`10.0.1.0/24` over `10.0.0.0/8`).
""",
    ["Two default routes without understanding metrics", "Asymmetric routing surprises", "Deleting default route remotely without console"],
    ["What is 0.0.0.0/0?", "What wins: /8 or /24?", "Command: which route to 1.1.1.1?"],
    ["https://man7.org/linux/man-pages/man8/ip-route.8.html"],
    "route_default")

add(17, "static-dynamic-routing", "Static vs Dynamic Routing Concepts", P6, "1–2 days",
    ["Contrast static routes vs OSPF/BGP ideas", "Know when static is enough", "Explain convergence at a high level", "Read simple BGP/OSPF vocabulary"],
    """
Static routes: operator-defined, simple, brittle at scale.
Dynamic protocols: OSPF/IS-IS inside orgs; **BGP** between orgs/internet.

```bash
# You may see learned routes on routers/VMs with routing daemons
ip route show protocol bgp 2>/dev/null
vtysh -c 'show ip route' 2>/dev/null   # FRR/Quagga style labs
```

Lab idea: FRRouting in VMs — not required for every exercise, but valuable later.
""",
    ["Injecting static routes that fight BGP", "No documentation of static routes", "Assuming cloud route tables behave like home Wi-Fi"],
    ["When static routes shine?", "BGP used where?", "What is convergence?"],
    ["https://www.rfc-editor.org/rfc/rfc4271"],
    "routing_bgp")

add(18, "nat", "NAT, PAT, and Hairpinning", P8, "1–2 days",
    ["Explain source NAT / PAT for internet egress", "Understand destination NAT / port forwards", "Spot NAT in troubleshooting", "Know hairpin NAT issues"],
    """
Home routers rewrite many private IPs to one public IP (**PAT**).

```bash
# On Linux NAT host (lab, nftables/iptables)
sudo iptables -t nat -L -n -v
sudo nft list table nat 2>/dev/null

# See public IP from behind NAT
curl -4 ifconfig.me
```

Symptoms of NAT: inbound connections fail without port forwards; \"peer sees wrong address\" in VoIP/P2P.
""",
    ["Exposing RDP/SSH via risky UPnP without care", "Overlapping NATed ranges in VPN merges", "Assuming inbound works like outbound"],
    ["PAT means?", "Why inbound fails by default?", "Table name for iptables NAT?"],
    ["https://www.rfc-editor.org/rfc/rfc3022"],
    "nat_pat")

add(19, "firewall-linux", "Host Firewalls: nftables, iptables, ufw", P8, "2 days",
    ["List rules and policies", "Allow least ports", "Test with care to avoid lockout", "Prefer high-level tools when enough"],
    """
```bash
# ufw (Ubuntu)
sudo ufw status verbose
sudo ufw default deny incoming
sudo ufw allow OpenSSH
sudo ufw allow 443/tcp
sudo ufw enable

# nftables
sudo nft list ruleset
# iptables legacy
sudo iptables -L -n -v
sudo iptables -S
```

Remote changes: keep an active console/session; allow SSH **before** enabling default deny.
""",
    ["Locking yourself out", "Disabling firewall instead of opening one port", "Forgetting IPv6 (`ip6tables`/`ufw`)"],
    ["ufw allow SSH command idea?", "Why console access?", "nft list command?"],
    ["https://wiki.nftables.org/"],
    "fw_default")

add(20, "tcpdump-basics", "tcpdump Basics for Engineers", P11, "2 days",
    ["Capture with filters", "Write/read pcap files", "Read flags and ports", "Minimize capture blast radius"],
    """
```bash
sudo tcpdump -ni eth0 -c 20
sudo tcpdump -ni any port 53
sudo tcpdump -ni eth0 host 10.0.0.5 and tcp port 443
sudo tcpdump -ni eth0 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'

# write / read
sudo tcpdump -ni eth0 -w /tmp/cap.pcap -c 100
tcpdump -nr /tmp/cap.pcap | head
tcpdump -nr /tmp/cap.pcap -A | head

# useful verbosity
sudo tcpdump -ni eth0 -vv -c 10 port 443
```

Wireshark GUI is great for deeper analysis of the same pcaps.
""",
    ["Capturing on prod without policy", "Huge unfiltered captures filling disks", "Sniffing secrets on shared networks"],
    ["Filter for DNS?", "Flag to write pcap?", "Read pcap without capture?"],
    ["https://www.tcpdump.org/manpages/tcpdump.1.html"],
    "tcpdump_port")

add(21, "wireshark-flow", "Reading Flows: Wireshark/tshark Essentials", P11, "1–2 days",
    ["Open pcaps in Wireshark/tshark", "Follow TCP streams", "Apply display filters", "Export objects carefully"],
    """
```bash
# tshark CLI examples
tshark -r cap.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri
tshark -r cap.pcap -Y 'dns' -c 20
tshark -r cap.pcap -q -z conv,tcp
tshark -r cap.pcap -Y 'tls.handshake.type == 1' -V | head
```

Display filter examples (Wireshark): `ip.addr==10.0.0.5`, `tcp.port==443`, `http`, `dns.flags.rcode != 0`.
""",
    ["Assuming encrypted payloads are readable", "Over-trusting reassembly on packet loss", "Sharing pcaps with secrets"],
    ["Follow TCP stream purpose?", "tshark -Y meaning?", "Filter for DNS errors idea?"],
    ["https://www.wireshark.org/docs/"],
    "tshark_dns")

add(22, "dhcp", "DHCP and Address Assignment", P7, "1 day",
    ["Explain Discover/Offer/Request/Ack", "Inspect leases", "Debug 'got 169.254'", "Know static vs DHCP tradeoffs"],
    """
```bash
# Linux NetworkManager
nmcli device show
# leases locations vary
ls /var/lib/dhcp/ 2>/dev/null
journalctl -u NetworkManager | grep -i dhcp | tail

# macOS
ipconfig getpacket en0
```

`169.254.x.x` usually means DHCP failed → link-local fallback.
""",
    ["Two DHCP servers fighting on a LAN", "Tiny pools exhausting leases", "Static IP colliding with DHCP pool"],
    ["DORA steps?", "What does 169.254 suggest?", "DHCP vs static when?"],
    ["https://www.rfc-editor.org/rfc/rfc2131"],
    "dhcp_apipa")

add(23, "vlans", "VLANs and Trunking Concepts", P7, "1–2 days",
    ["Explain VLAN segmentation", "Understand access vs trunk ports", "Know 802.1Q tagging idea", "See VLAN subinterfaces on Linux"],
    """
```bash
# Linux VLAN subinterface example (lab)
sudo ip link add link eth0 name eth0.20 type vlan id 20
sudo ip addr add 10.20.0.10/24 dev eth0.20
sudo ip link set eth0.20 up
ip -d link show eth0.20
```

VLANs split broadcast domains — security/ops boundary, not magic encryption.
""",
    ["Using VLANs as only security control", "Native VLAN mismatches", "Overlapping IP plans across VLANs without routing"],
    ["Access vs trunk?", "802.1Q does what?", "Do VLANs encrypt?"],
    ["https://www.rfc-editor.org/rfc/rfc3069"],
    "vlan_tag")

add(24, "vpn-basics", "VPN Basics: IPsec, WireGuard, OpenVPN", P9, "2 days",
    ["Contrast VPN types at a high level", "Read WireGuard quick configs conceptually", "Troubleshoot VPN DNS and routes", "Watch MTU/overhead issues"],
    """
```bash
# WireGuard (if installed)
sudo wg
sudo wg show
ip route | grep -E 'wg|tun|tun0'

# OpenVPN legacy style
ip addr show tun0
```

Common failures: missing routes, DNS still public, MTU blackholes, firewall blocking UDP 51820/1194.

```bash
ping -c 2 10.0.0.1                 # internal after VPN
dig @10.0.0.2 internal.service A
curl -I https://internal.service
```
""",
    ["Full-tunnel VPN without need (hairpin pain)", "Split tunnel missing critical routes", "Ignoring MTU"],
    ["WireGuard show command?", "Typical WG port?", "Why MTU drops with VPN?"],
    ["https://www.wireguard.com/"],
    "vpn_mtu")

add(25, "ssh-tunnels", "SSH Tunnels and Port Forwards", P9, "1–2 days",
    ["Use local/remote/dynamic SSH forwards", "Access private admin UIs safely", "Avoid standing tunnels forever without need", "Combine with ProxyJump"],
    """
```bash
# Local forward: local 8080 -> remote's localhost:80 via ssh host
ssh -L 8080:127.0.0.1:80 user@bastion

# Remote forward
ssh -R 9090:127.0.0.1:3000 user@bastion

# Dynamic SOCKS
ssh -D 1080 user@bastion
curl --socks5-hostname 127.0.0.1:1080 https://example.com

# Jump host
ssh -J bastion user@internal
# ~/.ssh/config: ProxyJump bastion
```
""",
    ["Exposing binds on 0.0.0.0 unintentionally", "Long-lived tunnels as permanent VPN substitute without review", "Forgetting ExitOnForwardFailure"],
    ["-L meaning?", "-D meaning?", "ProxyJump purpose?"],
    ["https://man.openbsd.org/ssh"],
    "ssh_L")

add(26, "load-balancing", "Load Balancing Concepts and Health Checks", P10, "1–2 days",
    ["Explain L4 vs L7 balancing", "Know health checks and draining", "Recognize algorithms (round-robin, least-conn)", "See nginx upstream basics"],
    """
L4: TCP/UDP (IP:port). L7: HTTP paths/headers.

```bash
# Probe backends yourself
for b in 10.0.0.11 10.0.0.12; do
  curl -sS -o /dev/null -w "$b %{http_code}\\n" --connect-timeout 1 http://$b/healthz || echo "$b down"
done
```

Nginx sketch: `upstream`, `proxy_pass`, health via separate checks/sidecar.
""",
    ["No health checks", "Balancing without shared session strategy when needed", "Draining ignored during deploys"],
    ["L4 vs L7?", "Why health checks?", "What is draining?"],
    ["https://nginx.org/en/docs/http/load_balancing.html"],
    "lb_l4l7")

add(27, "reverse-proxy", "Reverse Proxies: TLS Termination and Headers", P10, "1–2 days",
    ["Terminate TLS at proxy", "Pass X-Forwarded-* carefully", "Preserve client IP with real_ip", "Log correctly"],
    """
```bash
# App sees proxy IP unless headers configured
curl -H 'X-Forwarded-For: 1.2.3.4' http://localhost:8080/ || true

# Test proxy locally
curl -I https://localhost --cacert lab-ca.pem
curl -I http://localhost/api
```

Trust `X-Forwarded-For` **only** from trusted proxies — otherwise clients can spoof.
""",
    ["Trusting XFF from the internet", "Mixed content / wrong redirect schemes", "Huge header sizes without limits"],
    ["TLS termination meaning?", "Why not trust XFF blindly?", "real_ip purpose?"],
    ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For"],
    "xff_trust")

add(28, "http2-quic", "HTTP/2, HTTP/3, and QUIC Awareness", P5, "1 day",
    ["Know why HTTP/2 multiplexes", "Understand QUIC runs on UDP", "Probe protocol with curl", "Relate to CDNs"],
    """
```bash
curl -I --http1.1 https://example.com
curl -I --http2 https://example.com
curl -I --http3-only https://example.com 2>/dev/null || echo 'http3 not in this curl'
curl -sS -o /dev/null -w '%{http_version}\\n' https://example.com
```

QUIC/HTTP3 can improve lossy networks; middleboxes sometimes break UDP.
""",
    ["Assuming HTTP/3 always faster", "Blocking UDP 443 enterprise-wide accidentally", "Ignoring fallback to TCP"],
    ["HTTP/2 main benefit?", "QUIC transport?", "curl write-out for version?"],
    ["https://www.rfc-editor.org/rfc/rfc9114"],
    "http_version")

add(29, "cdn-caching", "CDNs, Caching, and Cache Headers", P10, "1–2 days",
    ["Read Cache-Control/ETag/Age", "Differentiate CDN edge vs origin issues", "Purge/invalidate conceptually", "Debug with response headers"],
    """
```bash
curl -sI https://example.com | grep -iE 'cache-control|etag|age|cf-|x-cache|server'
curl -sI -H 'Cache-Control: no-cache' https://example.com | head
```

When users see old content: TTL, Vary headers, stale-while-revalidate, regional POPs, or local browser cache.
""",
    ["Caching personalized/private responses publicly", "No versioning of static assets", "Purging entire site for one file habitually"],
    ["Age header meaning?", "Why asset fingerprinting?", "Private vs public cache?"],
    ["https://www.rfc-editor.org/rfc/rfc9111"],
    "cache_control")

add(30, "qos-traffic", "Latency, Bandwidth, Loss, and QoS Basics", P11, "1–2 days",
    ["Separate latency vs bandwidth problems", "Measure with simple tools", "Explain bufferbloat idea", "Know QoS is policy + queuing"],
    """
```bash
# rough latency
ping -c 20 1.1.1.1
# throughput tools if installed
iperf3 -c iperf.example.com
# DNS/app latency
curl -sS -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\\n' https://example.com
```

Slow downloads can be bandwidth; slow pages often DNS/TLS/TTFB/app.
""",
    ["Buying more bandwidth for a latency-bound app", "Ignoring Wi-Fi interference", "No baseline metrics"],
    ["TTFB meaning?", "ping measures what?", "Bandwidth fix won't help when?"],
    ["https://www.bufferbloat.net/projects/"],
    "curl_timing")

add(31, "nmap-basics", "Scanning Basics with nmap (Lab Only)", P11, "1–2 days",
    ["Scan ports ethically in labs", "Interpret open/closed/filtered", "Use service version detection carefully", "Never scan without authorization"],
    """
**Only scan networks you own or have written permission to test.**

```bash
nmap -sn 192.168.1.0/24                 # ping sweep (lab)
nmap -sT -p 22,80,443 192.168.1.10
nmap -sV -p 443 example.com             # version detect
nmap -sU -p 53 192.168.1.1              # UDP (noisy/slow)
nmap -oA labscan 192.168.1.10           # output basename
```

filtered ≠ closed. Firewalls create ambiguity.
""",
    ["Scanning the internet 'for practice'", "Aggressive scans on fragile devices", "Ignoring legal/ToS boundaries"],
    ["When is scanning legal?", "open vs filtered?", "-sV meaning?"],
    ["https://nmap.org/book/man.html"],
    "nmap_auth")

add(32, "bgp-internet", "How the Internet Routes: BGP at a Glance", P6, "1–2 days",
    ["Explain ASNs and prefixes", "Understand announcements/withdrawals", "Use looking glasses / whois / bgp tools", "Know why leaks/hijacks matter"],
    """
```bash
whois 1.1.1.1 | head -40
whois -h whois.radb.net -- '-i origin AS13335' 2>/dev/null | head
# public helpers
curl -s https://ipinfo.io/1.1.1.1
dig +short 1.1.1.1.origin.asn.cymru.com TXT
```

BGP picks paths between Autonomous Systems. Mis-announcements can blackhole or hijack traffic — RPKI/filtering mitigate.
""",
    ["Thinking traceroute equals BGP path always", "Ignoring prefix ownership", "Lab experiments on real upstreams"],
    ["What is an ASN?", "What does whois help show?", "Why RPKI?"],
    ["https://www.rfc-editor.org/rfc/rfc4271"],
    "asn_quiz")

add(33, "anycast-dns-cdn", "Anycast, GeoDNS, and Global Traffic", P10, "1 day",
    ["Explain anycast routing idea", "Contrast with unicast", "Relate to DNS/CDN POPs", "Debug geo differences"],
    """
Anycast: same IP announced from many places; users hit nearby POP.

```bash
dig +short one.one.one.one
ping -c 2 1.1.1.1
curl -s https://cloudflare.com/cdn-cgi/trace | head
curl -sI https://example.com | grep -i cf-ray
```

Different resolvers/regions may see different answers (GeoDNS).
""",
    ["Expecting one physical server behind 1.1.1.1", "Debugging only from one region", "Ignoring resolver location effects"],
    ["Anycast vs unicast?", "Why region matters?", "CDN POP meaning?"],
    ["https://www.cloudflare.com/learning/cdn/glossary/anycast-network/"],
    "anycast_quiz")

add(34, "email-dns", "Email Networking: MX, SPF, DKIM, DMARC", P4, "1–2 days",
    ["Query MX records", "Read SPF TXT basics", "Know DKIM/DMARC roles", "Debug delivery with headers"],
    """
```bash
dig example.com MX +short
dig example.com TXT +short
dig _dmarc.example.com TXT +short
# DKIM selectors vary; example pattern:
# dig selector._domainkey.example.com TXT +short
```

SPF authorizes senders; DKIM signs messages; DMARC policy aligns them. Networking + DNS + mail servers intertwine.
""",
    ["Permissive SPF (+all)", "No DMARC on important domains", "Forgetting PTR for mail IPs"],
    ["MX purpose?", "SPF stored as what record?", "DMARC policy domain pattern?"],
    ["https://www.rfc-editor.org/rfc/rfc7208"],
    "mx_quiz")

add(35, "ntp-time", "Time Sync and Why Networks Care", P11, "1 day",
    ["Check clock sync", "Explain skew impact on TLS/auth/logs", "Use timedatectl/chronyc/ntpstat", "Correlate multi-host timelines"],
    """
```bash
date -u
timedatectl status                    # systemd
chronyc tracking 2>/dev/null
sntp time.google.com 2>/dev/null
```

Skew breaks Kerberos, confuses logs, and can invalidate TLS seemingly randomly.
""",
    ["Disabling NTP in VMs", "Comparing logs without timezone discipline", "Huge leap smears ignored"],
    ["Why TLS cares about time?", "timedatectl purpose?", "UTC recommendation?"],
    ["https://www.rfc-editor.org/rfc/rfc5905"],
    "ntp_quiz")

add(36, "wireless-basics", "Wi-Fi Networking Essentials", P7, "1 day",
    ["SSID/BSSID/RSSI concepts", "Distinguish Wi-Fi vs ethernet failures", "Scan networks on Linux/macOS", "Know channels/interference exist"],
    """
```bash
# Linux (if available)
iwdev wlan0 link
iwlist wlan0 scan 2>/dev/null | head
nmcli device wifi list

# macOS
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
```

Many \"network down\" tickets are Wi-Fi; wire in to isolate.
""",
    ["Debugging TCP apps while on captive portal", "Ignoring 2.4GHz congestion", "VPN+Wi-Fi Power save weirdness"],
    ["SSID vs BSSID?", "First isolation step?", "RSSI rough meaning?"],
    ["https://linuxwireless.sipsolutions.net/"],
    "wifi_quiz")

add(37, "container-net", "Container Networking: Bridge, CNI, localhost Traps", P12, "2 days",
    ["Explain docker bridge basics", "Publish ports correctly", "Debug DNS inside containers", "Avoid localhost confusion"],
    """
```bash
docker network ls
docker run --rm curlimages/curl:latest curl -4 -I https://example.com
docker run --rm -p 8080:80 nginx
curl -I http://127.0.0.1:8080

# inspect
docker network inspect bridge | head
nsenter tips / ip netns (advanced Linux)
```

`localhost` inside a container is the container, not the host. Use host gateway / service names / published ports.
""",
    ["--network host as default", "Assuming container DNS equals host DNS always", "Publishing all ports broadly"],
    ["localhost in container means?", "-p 8080:80 meaning?", "docker network ls purpose?"],
    ["https://docs.docker.com/network/"],
    "docker_localhost")

add(38, "kubernetes-net", "Kubernetes Networking Concepts for Engineers", P12, "2 days",
    ["Pod/Service/ClusterIP/NodePort/Ingress ideas", "kubectl network debugging basics", "CoreDNS importance", "NetworkPolicy awareness"],
    """
```bash
kubectl get svc -A
kubectl get endpoints -A | head
kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl run netshoot --rm -it --image=nicolaka/netshoot -- /bin/bash
# inside: dig kubernetes.default.svc.cluster.local; curl svcname
kubectl exec -it deploy/myapp -- ss -tulpn
```

If DNS in cluster breaks, \"everything is broken\". NetworkPolicies can deny silently.
""",
    ["kubectl apply without understanding Services", "Using NodePort on cloud without LB", "Flat allow-all policies forever"],
    ["ClusterIP purpose?", "CoreDNS role?", "NetworkPolicy default deny effect?"],
    ["https://kubernetes.io/docs/concepts/services-networking/"],
    "k8s_svc")

add(39, "cloud-vpc", "Cloud VPCs: Subnets, Route Tables, Gateways", P12, "2 days",
    ["Map VPC/subnet/route table/IGW/NAT", "Design public vs private subnets", "Avoid overlapping CIDRs for peering", "Read cloud route tables like `ip route`"],
    """
Mental model maps cleanly to Linux routing:

- Route table → `ip route`
- SG/NACL → host/network firewalls
- NAT gateway → SNAT egress
- IGW → public path

```bash
# From a cloud VM
ip route
curl -4 ifconfig.me
# AWS metadata example (know IMDSv2!) — prefer cloud CLI offline study if unsure
```

Always plan non-overlapping CIDRs for future peering/VPN.
""",
    ["All subnets public", "Overlapping 10.0.0.0/8 everywhere", "No egress strategy for private subnets"],
    ["Private subnet egress via?", "Why non-overlapping CIDRs?", "SG stateful meaning roughly?"],
    ["https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"],
    "vpc_cidrs")

add(40, "security-groups", "Security Groups vs NACLs vs Host Firewalls", P8, "1–2 days",
    ["Contrast SG/NACL/host firewall layers", "Write least-privilege allowlists", "Debug timeouts vs resets", "Trace which layer drops"],
    """
Timeouts often mean **drop** (SG/NACL/firewall). Immediate RST may mean closed port on host.

```bash
# Client evidence
curl -v --connect-timeout 3 https://target:443 || true
nc -vz -w 3 target 443

# On host
ss -tulpn | grep 443
sudo nft list ruleset | head
```

Layered controls: cloud SG + host nft/ufw + app auth.
""",
    ["0.0.0.0/0 on SSH in prod", "Only SGs, no host hardening", "Changing three layers at once"],
    ["Timeout often means?", "RST often means?", "Why defense in depth?"],
    ["https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"],
    "sg_timeout")

add(41, "tls-mtls", "mTLS and Service Identity Intro", P5, "1–2 days",
    ["Explain client certificates", "Contrast mTLS vs token auth", "Inspect cert fields for clients", "Know mesh (Istio/Linkerd) uses mTLS"],
    """
```bash
# Server requesting client cert will fail without key/cert
curl -v --cert client.pem --key client-key.pem https://mtls.example.lab/ || true
openssl x509 -in client.pem -noout -subject -dates
```

mTLS authenticates both sides at TLS layer — powerful inside private service meshes.
""",
    ["Long-lived client certs without rotation", "Skipping revocation strategy", "Mixing mTLS and permissive plaintext elsewhere"],
    ["mTLS means?", "curl flags for client cert?", "Mesh relation?"],
    ["https://www.rfc-editor.org/rfc/rfc8446"],
    "mtls_quiz")

add(42, "dns-dnssec", "DNSSEC and DNS Security Awareness", P4, "1 day",
    ["Know what DNSSEC protects", "See AD flag in dig", "Understand it does not encrypt DNS", "Prefer DoH/DoT for privacy"],
    """
```bash
dig example.com +dnssec +noall +answer +comments
dig example.com +dnssec | grep -E 'flags:|RRSIG'
# DoH example via curl
curl -sH 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=example.com&type=A' | head -c 200; echo
```

DNSSEC → authenticity/integrity. DoH/DoT → privacy on path to resolver.
""",
    ["Thinking DNSSEC hides queries", "Broken middleboxes failing DNSSEC validation", "No monitoring of DNSSEC expirations for your zones"],
    ["DNSSEC vs DoH?", "dig flag to request DNSSEC records?", "What problem DNSSEC does not solve?"],
    ["https://www.rfc-editor.org/rfc/rfc4033"],
    "dnssec_quiz")

add(43, "observability-net", "Network Observability: Metrics, Logs, Traces", P11, "1–2 days",
    ["Define golden network signals", "Instrument latency/errors from clients", "Use flow logs conceptually", "Correlate app traces with net failures"],
    """
Signals: reachability, RTT, loss, DNS latency, TLS latency, saturation, error rates.

```bash
# continuous simple probe
while true; do
  curl -sS -o /dev/null -w '%{http_code} %{time_total}\\n' https://example.com || echo fail
  sleep 2
done
```

Cloud flow logs / VPC logs help prove whether packets left a NIC/SG.
""",
    ["Metrics without alerts", "Only average latency", "No probe from multiple regions"],
    ["Name four golden signals", "Why percentiles?", "Flow logs help prove what?"],
    ["https://sre.google/sre-book/monitoring-distributed-systems/"],
    "obs_probe")

add(44, "troubleshooting-playbook", "Networking Troubleshooting Playbook", P11, "2 days",
    ["Apply a layered checklist", "Capture evidence before changing things", "Bisect path: local → LAN → WAN → DNS → TLS → app", "Write crisp incident notes"],
    """
## Checklist

```bash
# 1) Local
ip -br addr; ip route; scutil --dns 2>/dev/null | head
# 2) L2/L3
ping -c 2 <gw>; ip neigh
# 3) DNS
dig example.com +time=1
# 4) TCP
nc -vz -w 3 example.com 443
# 5) TLS/HTTP
curl -vI --max-time 5 https://example.com
# 6) Capture if needed
sudo tcpdump -ni any -c 50 host example.com
```

Change one variable at a time. Record timestamps.
""",
    ["Shotgun restarts", "No notes", "Skipping DNS"],
    ["First three checks?", "Why evidence before reboot?", "Where capture fits?"],
    ["https://sre.google/sre-book/"],
    "playbook_order")

add(45, "performance-tuning", "Host Network Performance Tuning Intro", P11, "1–2 days",
    ["Inspect RX/TX errors and drops", "Know ephemerial port exhaustion exists", "Tune carefully with evidence", "Relate to ulimit/somaxconn"],
    """
```bash
ip -s link
netstat -s | head -50                   # or ss -s
cat /proc/sys/net/ipv4/ip_local_port_range   # Linux
sysctl net.core.somaxconn
ss -s
```

High `CLOSE-WAIT`/`TIME-WAIT`, port range exhaustion, NIC errors — measure first, then tune.
""",
    ["sysctl cargo cult from blogs", "Raising limits hiding leaks", "Ignoring NIC hardware offload/errors"],
    ["Where see interface drops?", "Ephemeral ports why?", "Measure before tune?"],
    ["https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt"],
    "perf_sysctl")

add(46, "api-gateways", "API Gateways and Edge Patterns", P10, "1–2 days",
    ["Place auth/rate-limit/WAF at edge", "Distinguish gateway vs service mesh", "Debug 502/503/504 meanings", "Trace request IDs across hops"],
    """
```bash
curl -I https://api.example.com/v1/health
curl -sS -o /dev/null -w '%{http_code}\\n' https://api.example.com/v1/missing
# common gateway timeouts -> 504
```

502 bad gateway (upstream nonsense), 503 unavailable, 504 timeout — start at proxy logs + upstream health.
""",
    ["Business logic only in gateway forever", "No correlation IDs", "Retry storms without backoff"],
    ["504 often means?", "502 hints?", "Why request IDs?"],
    ["https://www.rfc-editor.org/rfc/rfc9110"],
    "gw_504")

add(47, "zero-trust", "Zero Trust Networking Ideas", P9, "1 day",
    ["Move beyond flat VPN trust", "Prefer identity-aware access", "Least privilege paths", "Combine device posture + user identity"],
    """
Zero trust: never trust network location alone. Authenticate/authorize continuously.

Practical steps: SSO, short-lived certs, mTLS/mesh, per-service policies, avoid huge flat /16 VPNs with implicit trust.

```bash
# Still verify paths explicitly
curl -I https://internal.example.com
# without VPN / with identity proxy patterns (org-specific)
```
""",
    ["VPN equals secure forever", "Flat allow-all east-west", "Long-lived shared secrets"],
    ["Zero trust core idea?", "Risk of flat VPN?", "Short-lived creds why?"],
    ["https://www.nist.gov/publications/zero-trust-architecture"],
    "zt_quiz")

add(48, "lab-packet", "Lab: Build a Mini Network Path", P0, "2 days",
    ["Connect two VMs via private network", "Set addresses/routes manually", "Verify with ping/curl/tcpdump", "Document the path"],
    """
Suggested lab:

1. VM A `10.10.0.1/24`, VM B `10.10.0.2/24`
2. `ping` both ways
3. Run `python3 -m http.server 8080` on B; `curl` from A
4. `tcpdump` the handshake
5. Add a third \"router\" VM later for multi-hop

```bash
sudo ip addr add 10.10.0.1/24 dev eth1
sudo ip link set eth1 up
ping -c 3 10.10.0.2
```
""",
    ["Using public internet for first labs", "No snapshots before routing experiments", "Overlapping subnets"],
    ["What proves L3 connectivity?", "How prove HTTP path?", "Why tcpdump?"],
    ["https://netdevops.me/"],
    "lab_pair")

add(49, "command-cheatsheet", "Command Cheatsheet Consolidation Drill", P3, "1–2 days",
    ["Memorize a personal daily cheatsheet", "Group tools by layer", "Practice without looking", "Keep a living notes file"],
    """
## Must-know roster

```bash
ip -br a; ip r; ip neigh
ss -tulpn
ping -c 3 <t>; mtr -rwzc 50 <t>
dig <name> +short; dig @1.1.1.1 <name>
curl -vI --max-time 5 https://<t>
openssl s_client -connect host:443 -servername host
nc -vz -w 3 host 443
sudo tcpdump -ni any -c 20 host <t>
```

Rebuild this list from memory as the exercise.
""",
    ["Huge unsorted note dumps", "Never practicing recall", "Tools without understanding"],
    ["Name two tools per L3/L4/L7", "Why cheatsheets help oncalls?", "What belongs in daily roster?"],
    ["https://wiki.archlinux.org/title/Network_configuration"],
    "cheat_count")

add(50, "gre-vxlan", "Tunnels: GRE/VXLAN Overlay Awareness", P9, "1–2 days",
    ["Explain overlays vs underlays", "Know VXLAN for multi-tenant/datacenter", "See Linux vxlan devices", "Relate to cloud SDN"],
    """
```bash
ip link show type vxlan
ip -d link show
# example create is lab-only and environment-specific
```

Overlays carry L2/L3 over underlay IP. MTU and encapsulation overhead matter again.
""",
    ["Ignoring underlay MTU", "Debugging only overlay IPs", "No mapping of VNI/tenants"],
    ["Overlay vs underlay?", "VXLAN common use?", "Why MTU again?"],
    ["https://www.rfc-editor.org/rfc/rfc7348"],
    "vxlan_quiz")

add(51, "quic-firewall", "Firewalls, Middleboxes, and Modern Protocols", P8, "1 day",
    ["Know middleboxes can break UDP/QUIC", "Test fallbacks", "Design allowlists for new protocols", "Document egress needs"],
    """
```bash
curl -I --http3-only https://example.com || echo 'blocked or unsupported'
curl -I --http2 https://example.com
# observe which ports egress needs
nc -vzu -w 2 1.1.1.1 443 || true
```

Enterprise networks that hard-block UDP may degrade HTTP/3; apps should fallback gracefully.
""",
    ["Blind UDP blocks without measurement", "Assuming middleboxes are transparent", "No inventory of required egress"],
    ["Why UDP 443 matters?", "What is a middlebox?", "Fallback strategy?"],
    ["https://www.rfc-editor.org/rfc/rfc9308"],
    "middlebox_quiz")

add(52, "interview-net", "Networking Interview & Oncall Drills", P11, "2 days",
    ["Explain issues aloud with structure", "Whiteboard a path", "Solve timed scenarios", "Prioritize user impact"],
    """
Scenarios:

- Users in one city cannot login
- Intermittent TLS failures
- DNS works for you, not for customers
- Pod cannot reach DB
- Site slow only on mobile networks

Use the playbook; narrate evidence.
""",
    ["Jumping to rare root causes first", "No communication", "Fixing without verifying"],
    ["One-city issue first suspects?", "TLS intermittent ideas?", "Verify how?"],
    ["https://sre.google/sre-book/managing-incidents/"],
    "interview_drill")

add(53, "capstone-lab-net", "Capstone: Multi-Host Lab Network", P13, "3–5 days",
    ["Build 3-node lab with routing", "Provide DNS or /etc/hosts strategy", "Serve HTTP via proxy", "Document addressing & runbook"],
    """
## Mission

- 3 Linux VMs: client, router/proxy, server
- Static IPs + routes
- `curl` from client to service via proxy
- tcpdump evidence of path
- Basic firewall allowing only needed ports
- Written network diagram + runbook

## Rubric

- Correct routing table
- Evidence captures
- Least ports open
- Clean reboot persistence notes
""",
    ["DHCP chaos without notes", "No diagram", "All ports open"],
    ["What is the next hop from client?", "Which ports open?", "How prove path?"],
    ["https://netdevops.me/"],
    "cap_lab")

add(54, "capstone-debug", "Capstone: Broken Network Challenge", P13, "2–4 days",
    ["Debug planted failures", "Produce timeline + root cause", "Fix with minimal change", "Write postmortem"],
    """
Break a snapshot on purpose (wrong route, bad DNS, blocked SG, MTU, expired cert, hosts file typo). Restore service with postmortem:

Impact → Timeline → Root cause → Fix → Prevention
""",
    ["Recreate VMs instead of debugging", "Changing everything", "No postmortem"],
    ["Root cause?", "Evidence?", "Prevention?"],
    ["https://sre.google/sre-book/postmortem-culture/"],
    "cap_break")

add(55, "capstone-edge", "Capstone: Secure Edge for a Small App", P13, "4–6 days",
    ["Terminate TLS at edge", "Reverse proxy to app", "Firewall + SSH hardening + health checks", "Probe latency/error metrics"],
    """
## Mission

Deploy a small app behind:

- Reverse proxy with TLS (lab certs OK)
- Health checks and structured logs
- Host firewall
- Optional WireGuard admin access instead of public SSH
- Simple uptime probe script with curl timings
- Runbook for cert renewal and failure modes

## Rubric

- Least privilege exposure
- Clear 502/504 debugging notes
- Evidence of probe dashboard/log
- Graceful reloads
""",
    ["App exposed directly on :80 public", "No health checks", "Certs without renewal plan"],
    ["What is public?", "How detect expiry?", "How prove health?"],
    ["https://nginx.org/en/docs/"],
    "cap_edge")
