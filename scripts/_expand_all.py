#!/usr/bin/env python3
"""Expand curriculum_data.py + exercises_data.py into a complete learning guide.

Run from repo: python3 scripts/_expand_all.py
Then: python3 scripts/write_curriculum.py && ./scripts/smoke_test.sh
"""
from __future__ import annotations

import importlib.util
import re
import textwrap
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def load_modules():
    spec = importlib.util.spec_from_file_location("cd", SCRIPTS / "curriculum_data.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return list(m.MODULES)


def assemble_body(title: str, t: dict) -> str:
    cmds = t["cmds"]  # [(bash, sample, interp), ...]
    parts = []
    for i, (bash, sample, interp) in enumerate(cmds, 1):
        parts.append(
            f"### Example {i}\n\n```bash\n{bash.strip()}\n```\n\n"
            f"Sample output:\n\n```text\n{sample.strip()}\n```\n\n"
            f"**Interpretation:** {interp.strip()}\n"
        )
    fail_rows = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in t["fails"])
    lab = "\n".join(f"{i}. {s}" for i, s in enumerate(t["lab"], 1))
    concepts = t["concepts"].strip()
    body = f"""## Why this matters

{t['scenario'].strip()}

## Core concepts

{concepts}

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

{chr(10).join(parts)}

## Mini-lab

{lab}

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
{fail_rows}

## Study tip for {title}

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.
"""
    body = body.strip()
    # Optional depth section — once, not repeated filler.
    body += """

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.
"""
    return body.strip() + "\n"


# Compact topic specs: scenario, concepts, cmds[(bash,sample,interp)], lab[], fails[], guide, examples
TOPICS: dict[int, dict] = {
    0: {
        "scenario": (
            "It is 02:14 and a product page is 'down'. Stakeholders ask if it is DNS, the load balancer, "
            "TLS, or the app. Without a mental model of clients, packets, ports, and protocols, you jump "
            "between dashboards. Orientation trains a safe lab habit and a daily toolkit so every later "
            "lesson maps to something you can type under pressure."
        ),
        "concepts": """
- **Host**: machine with interfaces; **packet/frame**: chunk with headers; **protocol**: agreed rules.
- **Port**: application endpoint on a host (TCP/UDP). Same IP can host many services via different ports.
- **Client/server**: initiator vs listener — but roles flip (e.g. callbacks, peer protocols).
- Practice loop: attempt → struggle → solution → rewrite. Typing beats highlighting.
- Lab stack: laptop terminal + Linux VM (`ip`, `ss`, `nft`) + optional second VM for path tests.
""",
        "cmds": [
            (
                "ping -c 3 1.1.1.1\ndig example.com +short\ncurl -sS -o /dev/null -w '%{http_code} %{time_total}\\n' https://example.com",
                "64 bytes from 1.1.1.1: icmp_seq=1 ttl=57 time=12.1 ms\n...\n93.184.216.34\n200 0.182",
                "ICMP reachability, DNS A answer, and HTTP status/latency are three different layers of evidence. Collect all three before blaming 'the network'.",
            ),
            (
                "# Linux\nss -tulpn | head\nip -br addr\n# macOS analogues\n# netstat -anv | head; ifconfig en0",
                "udp UNCONN 0 0 0.0.0.0:53 ...\ntcp LISTEN 0 128 0.0.0.0:22 ...\neth0 UP 192.168.1.20/24",
                "`ss` shows listeners (who accepts connections). `ip -br addr` shows L3 addresses on interfaces. Knowing both prevents 'port open' vs 'wrong IP' confusion.",
            ),
            (
                "traceroute -n 1.1.1.1 2>/dev/null | head -5 || traceroute 1.1.1.1 | head -5",
                "1 192.168.1.1 1.2 ms\n2 10.0.0.1 8.4 ms\n3 1.1.1.1 12.0 ms",
                "Path hops are clues, not proof of the fault. Firewalls may hide hops (`* * *`). Still useful to see whether you leave the LAN.",
            ),
        ],
        "lab": [
            "Create a `lab-notes.md` and paste outputs of ping, dig, curl write-out, and ss/netstat.",
            "Start a tiny listener (`python3 -m http.server 8080`) and curl `http://127.0.0.1:8080/` — prove client/server locally.",
            "List five tools you will use daily and one sentence each on when.",
            "Tomorrow: rewrite the greetings/tooling exercise from memory before reopening solutions.",
        ],
        "fails": [
            ("Only reading PDFs", "No motor memory", "Type every example"),
            ("Practicing on prod", "Blast radius / policy risk", "Use VMs and approved lab nets"),
            ("Jumping to cloud GUIs", "Skips fundamentals", "Finish host toolkit first"),
            ("`curl` fails, blame DNS immediately", "Wrong layer guess", "Check dig and ping separately"),
        ],
        "guide": (
            "Implement three helpers: `greet` (friendly hello), `daily_tool_count_min` (minimum toolkit size taught: 5), "
            "and `study_loop` (the four-step practice phrase). Comments above each function should say *when* you use the idea on-call."
        ),
        "examples": (
            "`greet Net` → `Hello, Net`. `daily_tool_count_min` → `5`. "
            "`study_loop` → `attempt-struggle-solution-rewrite`."
        ),
    },
    1: {
        "scenario": (
            "A ticket says 'L7 is fine but L4 is broken'. If you casually mix OSI and TCP/IP vocabulary, "
            "you will chase HTTP dashboards while SYN packets never complete. Layer literacy tells you which "
            "tool speaks which layer — curl vs ss vs ping vs ARP — and stops wasted escalations."
        ),
        "concepts": """
| OSI idea | TCP/IP | Examples | Tools |
|----------|--------|----------|-------|
| L7 App | App | HTTP, DNS, SSH | curl, dig, openssl |
| L4 Transport | TCP/UDP | ports, sessions | ss, nc, tcpdump port |
| L3 Network | IP | routing, ICMP | ip route, ping, traceroute |
| L2 Data link | Link | MAC, ARP, Ethernet | ip neigh, tcpdump -e |
| L1 Physical | wires/radio | link up/down | ip link, ethtool |

HTTPS does **not** replace TCP — TLS rides on a TCP (or QUIC/UDP) session. Ports are L4 identifiers; MACs are L2.
""",
        "cmds": [
            (
                "dig example.com +short\nping -c 2 example.com\ncurl -sS -o /dev/null -w '%{http_code}\\n' https://example.com",
                "93.184.216.34\n64 bytes from ... time=20 ms\n200",
                "DNS (app naming) → ICMP (L3 reachability) → HTTPS (app over TLS/TCP). Failure at each step points to a different layer.",
            ),
            (
                "ss -tlnp | head -5\n# macOS: netstat -an | grep LISTEN | head",
                "LISTEN 0 128 0.0.0.0:443 ...",
                "Listening sockets prove an L4 endpoint exists locally. If ss shows nothing on 443 but curl to remote works, the problem is elsewhere.",
            ),
            (
                "curl -vI https://example.com 2>&1 | head -35",
                "* Connected to example.com (93.184.216.34) port 443\n* SSL connection using TLSv1.3\n< HTTP/2 200",
                "Verbose curl reveals TCP connect then TLS then HTTP — a live layer walkthrough.",
            ),
        ],
        "lab": [
            "Draw the path of `https://example.com` and label each step with a tool.",
            "For a local `python3 -m http.server 8000`, identify L4 port and L7 protocol.",
            "Answer: which layer are ports? MACs? TLS relative to TCP?",
        ],
        "fails": [
            ("Calling IPs 'MAC addresses'", "L2/L3 confusion", "ip neigh vs ip addr"),
            ("Thinking HTTPS replaces TCP", "Missing transport", "curl -v connect line"),
            ("Blaming DNS for TCP RST", "Wrong layer", "dig OK + ss/tcpdump"),
            ("Tool soup without layer map", "No hypothesis", "Pick one layer's tool"),
        ],
        "guide": (
            "Implement `layer_for_ports`, `layer_for_mac`, `layer_for_http`, and `tls_rides_on` "
            "returning the layer labels taught in the mapping table (L4, L2, L7, TCP)."
        ),
        "examples": "`layer_for_ports` → `L4`; `layer_for_mac` → `L2`; `layer_for_http` → `L7`; `tls_rides_on` → `TCP`.",
    },
}


# Unique on-call scenarios for modules that are not hand-authored in TOPICS/reg_overrides.
SCENARIOS: dict[int, str] = {
    4: "A host can reach the internet but a teammate cannot SSH to it using what they think is a 'public' address — they pasted a 10.x address into a ticket. Private ranges, public space, and the 'classes are dead, CIDR won' story stop that class of confusion.",
    5: "Security asks for a /27 for a new service; capacity planning assumed a /24. Getting host counts, network/broadcast, and usable ranges wrong either wastes address space or causes painful renumbering later.",
    6: "Half your clients prefer AAAA and half prefer A. Dual-stack misconfig shows up as 'works on my machine' — IPv6-only path broken, Happy Eyeballs hiding latency, or forgotten AAAA firewall holes.",
    7: "Someone added a secondary IP and 'the service is bound wrong'. `ip addr` / `ip route` / `ip route get` are how you prove which address and which egress path the kernel actually chooses.",
    8: "Users say 'the network is slow'. Ping loss, traceroute stars, and mtr asymmetry tell different stories — path diagnosis separates LAN, ISP, and far-end issues before you open a cloud ticket.",
    9: "Deploy claims the app listens on 8080; curl from another host times out. `ss`/`lsof` show whether anything listens, on which address (127.0.0.1 vs 0.0.0.0), and which process owns the socket.",
    10: "You need a quick TCP check, a one-shot HTTP listener, or a port forward without standing up nginx. `nc`/`socat` are the multitool — dangerous in the wrong hands, indispensable in a lab.",
    11: "An API 'loses' messages under load while metrics look fine. TCP retransmits vs UDP datagram drops change the design: reliability at L4 vs in the application.",
    12: "Browser fails, `ping` to an IP works. That is DNS until proven otherwise — resolvers, record types, TTL, and `dig` literacy cut hours off incidents.",
    13: "One office gets NXDOMAIN, another gets the old A record, CI gets SERVFAIL. Split-horizon, cache poisoning of your brain (stale TTL), and upstream SERVFAIL need different fixes.",
    14: "Swagger 'works' but production clients fail. `curl -v`, method/headers, redirects, and write-out timings expose what GUIs hide.",
    15: "Mobile users see certificate warnings; desktop is fine. SNI, chain incompleteness, and clock skew are TLS issues you prove with `openssl s_client`, not by restarting the app randomly.",
    16: "Packets leave the wrong NIC after a secondary default route appears. Routing tables and `ip route get` are the source of truth for egress.",
    17: "A static route 'worked until the peer renumbered'. Knowing when static is enough vs when OSPF/BGP (or cloud route propagation) must own the path prevents fragile snowflakes.",
    18: "Hairpin NAT: phone on Wi-Fi cannot reach the home server via the public hostname, but LTE works. PAT/NAT behavior and loopback/hairpin expectations explain it.",
    19: "Fresh VM: curl works locally, remote times out. Host firewall default-drop, wrong zone, or forgotten allow for the service port — `nft`/`iptables`/`ufw` show policy, not vibes.",
    20: "Metrics say error rate up; app logs are clean. A 30-second `tcpdump` with a tight BPF often shows RSTs, retransmits, or the wrong VIP before you guess.",
    21: "pcap in hand, chaos in the UI. Follow TCP streams, decode TLS to the point you are allowed, and filter noise — Wireshark/tshark turn bytes into a story.",
    22: "Laptop has an APIPA/link-local address and no default route. DHCP discover/offer/request/ack failed — lease, relay, or server scope issues.",
    23: "Same switch, 'can't ping' — different VLANs. Trunks, access ports, and tagged frames are why L2 adjacency is not guaranteed by a shared chassis.",
    24: "Corp VPN connects but SaaS apps hang. Tunnel type (WireGuard/IPsec/OpenVPN), split tunnel, and MTU interact; VPN literacy prevents 'disable VPN' as the only fix.",
    25: "Need a DB on a private host via bastion for five minutes. SSH `-L`/`-R`/`-D` is the tactical tunnel — wrong direction is the usual bug.",
    26: "One backend is sick but still in pool; 1/N users fail. Health checks, idle timeouts, and L4 vs L7 balancing decide whether you drain or page.",
    27: "App sees client IP as the proxy. `X-Forwarded-For` / `X-Real-IP` trust boundaries and TLS termination location are reverse-proxy essentials.",
    28: "CDN serves HTTP/3; corporate firewall UDP/443 is blocked. HTTP/2 multiplexing vs QUIC changes middlebox behavior — awareness prevents false 'site down' reports.",
    29: "Purge didn't purge. Cache-Control, Vary, and which layer cached (browser vs CDN vs origin) explain ghost content.",
    30: "Link is '1 Gbps' but app SLO is latency. Bandwidth vs latency vs loss vs jitter — and crude QoS expectations — change which knob you turn.",
    31: "Inventory a lab VLAN you own. nmap is a permission-bound tool: scope, rate, and interpreting open/filtered/closed without turning it into an outage.",
    32: "Traffic to a partner AS takes a scenic route. BGP is how the Internet chooses paths — enough theory to read a traceroute and a looking glass without pretending to be a NOC.",
    33: "Users in APAC hit the US origin. Anycast DNS/CDN and GeoDNS are how global traffic steers — and how stale DNS fights you.",
    34: "Marketing mail lands in spam. MX, SPF, DKIM, DMARC are DNS-shaped email auth — broken records look like 'email networking' not 'app bugs'.",
    35: "TLS and Kerberos fail after a VM snapshot. Clock skew breaks auth; NTP/chrony is network-critical infrastructure.",
    36: "Wired fine, Wi-Fi flaky. RF congestion, roaming, and captive portals are still networking — isolate WLAN before blaming the API.",
    37: "Health check to `localhost` inside a container always passes while the published port is dead. Bridge/CNI/`localhost` traps are container networking 101.",
    38: "Service A cannot reach Service B by DNS name. ClusterIP, kube-proxy/CNI, NetworkPolicy, and CoreDNS search paths are the Kubernetes network map.",
    39: "Private subnet instances cannot apt-get. Route tables, IGW vs NAT gateway, and subnet roles in a VPC explain egress.",
    40: "SG allows 443; NACL misses ephemeral return ports. Stateful vs stateless policy layers — plus host firewalls — stack in confusing ways.",
    41: "Zero-trust service mesh wants identity, not IPs. mTLS client certs prove workload identity — different failure mode than server-only TLS.",
    42: "Resolver validates DNSSEC and a domain suddenly SERVFAILs. Bogus signatures vs insecure delegation — awareness keeps you from 'fixing' DNS insecurely as a habit.",
    43: "Three dashboards disagree. RED/USE metrics, flow logs, and traces must correlate on identity (IP, service, trace-id) or you drown.",
    44: "Incident channel is chaotic. A repeatable layer-ordered playbook (path → DNS → listen/connect → TLS → app) is the difference between calm and thrash.",
    45: "High connection churn exhausts sockets. Softirq, backlog, ephemeral ports, and buffer tuning — intro only, with 'measure first' discipline.",
    46: "Mobile apps, browsers, and partners share one edge. API gateways add auth, rate limit, and routing — and new failure domains at the edge.",
    47: "VPN as the only trust boundary is failing. Zero trust shifts to identity, device posture, and per-request auth — networking still matters for enforcement points.",
    48: "Build a tiny path: DNS → route → listen → TLS → HTTP. Capstone labs glue earlier tools into one story you can demo.",
    49: "Interview or outage: you blank on flags. A cheatsheet drill forces retrieval of `ip`/`ss`/`dig`/`curl`/`tcpdump` under time pressure.",
    50: "Overlays everywhere: cloud networks, Kubernetes, DC fabrics. GRE/VXLAN awareness explains extra headers, MTU, and 'which IP do ACLs see?'.",
    51: "QUIC and HTTP/3 confuse stateful firewalls expecting TCP. Middlebox behavior toward UDP/443 and encrypted ClientHello is modern edge reality.",
    52: "Whiteboard: 'packets won't flow'. Interview/oncall drills reward structured differential diagnosis, not trivia lists.",
    53: "Multi-host lab: wire addressing, routing, DNS, and a small service. Capstone proves you can build, not only read.",
    54: "Someone broke the lab on purpose. Debug with evidence only — no config archaeology until measurements demand it.",
    55: "Ship a small app edge: TLS, reverse proxy, health checks, minimal firewall. Capstone for secure-enough production instincts.",
}


def default_topic(m: dict) -> dict:
    """Fallback rich topic built from module metadata when not hand-authored."""
    slug = m["slug"]
    title = m["title"]
    objs = m["objectives"]
    kind = m["ex_kind"]
    n = m["n"]
    scenario = SCENARIOS.get(
        n,
        (
            f"Incidents touching **{title}** punish vague mental models. "
            f"This lesson builds command-level fluency and failure modes so you gather evidence "
            f"(reachability, naming, policy, identity) before changing production."
        ),
    )
    concepts = "What you must be able to explain:\n\n" + "\n".join(f"- {o}" for o in objs)
    concepts += f"""

Mental model for `{slug}` (exercise kind `{kind}`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.
"""
    # Pick command sets by phase keywords
    phase = m["phase"]
    cmds = []
    if "DNS" in title or "dns" in slug or "Email" in title:
        cmds = [
            (
                "dig example.com A +short\ndig example.com AAAA +short\ndig example.com NS +short",
                "93.184.216.34\n2606:2800:220:1:248:1893:25c8:1946\na.iana-servers.net.",
                "A/AAAA/NS answers show what clients may use. Empty AAAA is not always an error on IPv4-only paths.",
            ),
            (
                "dig @1.1.1.1 example.com +noall +answer +stats",
                "example.com. 300 IN A 93.184.216.34\n;; Query time: 18 msec\n;; SERVER: 1.1.1.1#53",
                "Pinning `@resolver` removes 'which stub resolver?' ambiguity. Query time and SERVER lines matter when comparing sites.",
            ),
            (
                "dig not-a-real-xyz.invalid A +noall +comments 2>/dev/null | head -20",
                ";; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: ...",
                "NXDOMAIN means the name does not exist at the queried view — different from timeout or SERVFAIL.",
            ),
        ]
    elif "TLS" in title or "openssl" in slug or "mTLS" in title or "HTTP" in title or "curl" in slug or "CDN" in title or "proxy" in slug or "gateway" in title or "QUIC" in title or "Load" in title:
        cmds = [
            (
                "curl -I https://example.com 2>&1 | head -15",
                "HTTP/2 200\ncontent-type: text/html\ncache-control: max-age=...",
                "Response line and headers are L7 evidence after TCP/TLS succeeded.",
            ),
            (
                "curl -sS -o /dev/null -w 'code=%{http_code} ttfb=%{time_starttransfer} total=%{time_total} ver=%{http_version}\\n' https://example.com",
                "code=200 ttfb=0.120 total=0.180 ver=2",
                "Write-out metrics separate connect delay from first-byte and total time — essential for gateway/CDN debates.",
            ),
            (
                "echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -subject -dates",
                "subject=CN = example.com\nnotBefore=...\nnotAfter=...",
                "Certificate identity and expiry are independent of HTTP 200. SNI (`-servername`) selects the cert on shared IPs.",
            ),
        ]
    elif "tcpdump" in slug or "wireshark" in slug or "tshark" in slug or "nmap" in slug:
        cmds = [
            (
                "sudo tcpdump -ni any -c 5 udp port 53",
                "12:01:01.1 IP 10.0.0.5.53122 > 1.1.1.1.53: UDP, length 32\n12:01:01.2 IP 1.1.1.1.53 > 10.0.0.5.53122: UDP, length 48",
                "BPF `port 53` captures DNS. Direction and lengths hint query vs response. Always capture only systems you may test.",
            ),
            (
                "sudo tcpdump -ni any -c 8 'tcp port 443 and (tcp[tcpflags] & tcp-syn != 0)'",
                "... Flags [S], ...\n... Flags [S.], ...",
                "SYN and SYN-ACK prove handshake progress. SYN with no reply suggests drop/filter/blackhole along the path.",
            ),
            (
                "tshark -r /tmp/lab.pcap -Y 'dns' -c 5 2>/dev/null || echo 'save a pcap first: sudo tcpdump -w /tmp/lab.pcap -c 20 port 53'",
                "1 0.000000 10.0.0.5 → 1.1.1.1 DNS 74 Standard query A example.com",
                "Display filters (`-Y`) slice a saved capture without re-running traffic — safer on busy hosts.",
            ),
        ]
    elif "firewall" in slug or "Security" in title or "NAT" in title or "Zero" in title or "middlebox" in slug:
        cmds = [
            (
                "sudo nft list ruleset 2>/dev/null | head -40 || sudo iptables -L -n -v | head -40",
                "table inet filter {\n  chain input { type filter hook input priority filter; policy drop;",
                "Default **drop/deny** on inbound is the safe posture. Counters (iptables -v) show which rule matches.",
            ),
            (
                "ss -tlnp | head\ncurl -sS -o /dev/null -w '%{http_code}\\n' --connect-timeout 2 http://127.0.0.1:9 || echo 'timeout/fail expected'",
                "LISTEN ...\ntimeout/fail expected",
                "Listeners vs policy: a service may listen yet still be unreachable remotely if SG/NACL/nft drops mid-path.",
            ),
            (
                "ping -c 2 -W 1 10.255.255.254 || true\n# compare to: nc -vz -w 2 host 443",
                "100% packet loss",
                "Silent drops often look like timeouts, not TCP RST. That distinction drives 'firewall vs app refused' decisions.",
            ),
        ]
    elif "VPN" in title or "tunnel" in slug or "SSH" in title or "VXLAN" in title or "GRE" in title or "WireGuard" in title:
        cmds = [
            (
                "ip -br link; ip route | head\n# After VPN up, compare default route and MTU",
                "wg0 UP ...\ndefault via 10.10.0.1 dev wg0\nmtu 1420",
                "Tunnels add outer headers → lower effective MTU. Blackhole PMTUD is a classic VPN failure mode.",
            ),
            (
                "ping -c 2 -M do -s 1472 1.1.1.1 2>&1 | head -5 || ping -c 2 -D -s 1472 1.1.1.1 2>&1 | head -5",
                "Frag needed / Message too long / 100% loss",
                "Large DF probes failing after VPN connect points to MTU/MSS issues — lower MSS/MTU or fix ICMP PTB.",
            ),
            (
                "ssh -N -L 8080:127.0.0.1:80 user@bastion  # example local forward (lab)\necho 'local forward uses -L; remote -R; dynamic -D'",
                "(ssh holds open; curl localhost:8080 hits remote :80)",
                "SSH forwards are tactical tunnels. Know `-L` vs `-R` direction before debugging 'connection refused' on the wrong host.",
            ),
        ]
    elif "container" in slug or "kubernetes" in slug or "cloud" in slug or "VPC" in title:
        cmds = [
            (
                "docker network ls 2>/dev/null; ip -br addr | head\n# kubectl get svc,ep -A 2>/dev/null | head",
                "NETWORK ID ... bridge ...\neth0 ... 10.0.0.5/24\ncni0 ... 10.244.0.1/24",
                "Bridge/CNI interfaces explain why `localhost` inside a container is not the host — classic false-positive health check.",
            ),
            (
                "getent hosts kubernetes.default.svc.cluster.local 2>/dev/null || echo 'CoreDNS path: svc.namespace.svc.cluster.local'",
                "10.96.0.1 kubernetes.default.svc.cluster.local",
                "Cluster DNS (CoreDNS) answers service names. Wrong search domain → NXDOMAIN that works with FQDN.",
            ),
            (
                "# Cloud mental model (AWS-style)\necho 'public subnet → IGW; private subnet egress → NAT gateway; SG stateful; NACL stateless'",
                "private_subnet_egress_via=NAT-gateway",
                "Route tables decide egress path. Security groups dropping return traffic look like timeouts.",
            ),
        ]
    elif "capstone" in slug or "Interview" in title or "Cheatsheet" in title or "Lab:" in title or "playbook" in slug or "Observability" in title or "Performance" in title:
        cmds = [
            (
                "ping -c 2 1.1.1.1; dig example.com +short; curl -sS -o /dev/null -w '%{http_code}\\n' https://example.com; ss -tln | head",
                "icmp ok / A record / 200 / LISTEN lines",
                "Playbook order: local stack → L3 → DNS → L4 listen/connect → L7. Capstones and interviews reward this sequence.",
            ),
            (
                "ip route get 1.1.1.1; traceroute -n 1.1.1.1 2>/dev/null | head -4 || true",
                "1.1.1.1 via 192.168.1.1 dev eth0 src 192.168.1.20\n1 192.168.1.1",
                "`ip route get` is the fastest 'which path would this host take?' check on Linux.",
            ),
            (
                "curl -sS -o /dev/null -w 'namelookup=%{time_namelookup} connect=%{time_connect} ttfb=%{time_starttransfer}\\n' https://example.com",
                "namelookup=0.020 connect=0.040 ttfb=0.120",
                "Percentiles beat averages for latency SLOs; single curl samples teach which phase dominates.",
            ),
        ]
    else:
        # Host networking / routing / L2 defaults
        cmds = [
            (
                "ip -br addr; ip route; ip route get 1.1.1.1",
                "eth0 UP 192.168.1.20/24\ndefault via 192.168.1.1 dev eth0\n1.1.1.1 via 192.168.1.1 dev eth0 src 192.168.1.20",
                "`ip route get` shows the chosen route, egress device, and preferred source — gold for 'why did it leave this NIC?' questions.",
            ),
            (
                "ping -c 3 1.1.1.1\nss -tulpn | head\n# macOS: netstat -anv | head",
                "3 packets transmitted, 3 received\nudp ... :53\ntcp LISTEN ... :22",
                "ICMP OK proves basic L3; ss proves local listeners. Combine with ARP/neigh when LAN peers fail.",
            ),
            (
                "ip neigh show | head\nping -c 1 $(ip route | awk '/default/ {print $3; exit}')",
                "192.168.1.1 dev eth0 lladdr ... REACHABLE\n64 bytes from gateway",
                "Neighbor/ARP state validates L2 adjacency to the gateway before you blame the wider internet.",
            ),
        ]
    lab = [
        f"Re-type every worked command for **{title}** and paste outputs into lab notes.",
        "Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.",
        "Write a 5-line playbook: symptom → first command → expected healthy output.",
        "Complete the exercise stubs; then explain each function's return value without looking.",
    ]
    fails = [
        (p if len(p) < 40 else p[:37] + "...", "See common mistakes", "Re-run lesson commands")
        for p in m["pitfalls"][:3]
    ]
    fails.append(("Timeout with no RST", "Silent drop / blackhole", "tcpdump + compare path"))
    # guide/examples filled later per kind if missing
    return {
        "scenario": scenario,
        "concepts": concepts,
        "cmds": cmds,
        "lab": lab,
        "fails": fails,
        "guide": "",
        "examples": "",
    }


# Hand-authored overrides for early core modules (2-10) — remaining use default_topic + light patches
reg_overrides = {
    2: {
        "scenario": (
            "After enabling a VPN, large uploads hang while small pings work. That is classic MTU/encapsulation pain: "
            "each tunnel header steals bytes from the payload budget. Understanding encapsulation and path MTU keeps "
            "you from blaming the application for silent blackholes."
        ),
        "concepts": """
Encapsulation wraps upper-layer payloads:

```text
[Eth][IP][TCP][HTTP...]
```

- **MTU**: max payload on a link (Ethernet often **1500**).
- VPN/overlay headers reduce effective MTU (e.g. 1420).
- DF (don't fragment) + blocked ICMP "Packet Too Big" → blackhole.
- Rough sizes: Ethernet header 14 (+4 VLAN), IPv4 ~20, TCP ~20 — intuition for MSS clamping.
""",
        "cmds": [
            (
                "ip link show | sed -n '1,12p'\n# look for mtu 1500 / 9000 / 1420",
                "2: eth0: <BROADCAST,MULTICAST,UP> mtu 1500 ...\n3: wg0: ... mtu 1420 ...",
                "Interface MTU is local. Path MTU can be lower than any single hop you admin.",
            ),
            (
                "ping -c 2 -M do -s 1472 1.1.1.1 2>&1 | head -8 || ping -c 2 -D -s 1472 1.1.1.1 2>&1 | head -8",
                "1472 + 28 = 1500 on IPv4; success means path accepted DF full-size frames (or middlebox lies).",
                "1472 data bytes + 20 IPv4 + 8 ICMP ≈ 1500. Failure after VPN strongly suggests overhead.",
            ),
            (
                "sudo tcpdump -ni any -c 5 icmp",
                "IP a > b: ICMP echo request\nIP b > a: ICMP echo reply",
                "Confirm ICMP is not blocked if you rely on PMTUD. Many 'mystery hangs' are PTB filtered.",
            ),
        ],
        "lab": [
            "Record MTU on eth0 and any tunnel interface.",
            "Run DF ping at 1472 and at 1400; note difference with VPN on/off.",
            "Capture 5 ICMP packets while pinging; identify request/reply.",
        ],
        "fails": [
            ("Large transfers hang, small OK", "MTU/PMTUD blackhole", "DF ping + lower MSS"),
            ("VPN works for SSH not HTTPS uploads", "Effective MTU", "Check tunnel MTU"),
            ("No ICMP PTB", "Firewall too strict", "Allow PTB or clamp MSS"),
            ("Capturing wrong iface", "Missed packets", "tcpdump -ni any briefly"),
        ],
        "guide": "Implement `ethernet_typical_mtu`, `vpn_overhead_effect` (returns `lowers-MTU`), and `df_ping_purpose` (`probe-path-MTU`).",
        "examples": "`ethernet_typical_mtu` → `1500`; `vpn_overhead_effect` → `lowers-MTU`; `df_ping_purpose` → `probe-path-MTU`.",
    },
    3: {
        "scenario": (
            "Two VMs on the same subnet cannot talk, yet both ping 8.8.8.8. Often the gateway works (so 'internet is fine') "
            "while ARP/neighbor resolution between peers is broken — duplicate IP, wrong VLAN, or isolated port. "
            "Ethernet/MAC/ARP literacy is how you prove L2 adjacency."
        ),
        "concepts": """
- Ethernet delivers frames using **MAC** addresses on a broadcast domain.
- **ARP** (IPv4) maps **IP → MAC** on the local subnet only — it does **not** cross routers.
- Linux `ip neigh` is the modern neighbor table; `arp -n` still appears in tribal knowledge.
- Symptoms of duplicate IP: flapping MAC for one IP, intermittent reachability.
""",
        "cmds": [
            (
                "ip -br link; ip neigh show | head\n# macOS: ifconfig en0; arp -an | head",
                "eth0 UP ...\n192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE",
                "REACHABLE to the gateway MAC means L2 to default router is OK.",
            ),
            (
                "ping -c 1 192.168.1.1; ip neigh show | head",
                "64 bytes from 192.168.1.1\n192.168.1.1 ... REACHABLE",
                "Traffic populates/ refreshes neighbor entries — empty table after idle is normal.",
            ),
            (
                "sudo tcpdump -ni eth0 -c 6 arp",
                "Request who-has 192.168.1.50 tell 192.168.1.20\nReply 192.168.1.50 is-at aa:bb:...",
                "Seeing requests without replies isolates 'who isn't answering ARP'.",
            ),
        ],
        "lab": [
            "Ping gateway; confirm neigh entry.",
            "Ping a same-subnet peer; capture ARP.",
            "Explain why ARP cannot resolve an IP on another subnet.",
        ],
        "fails": [
            ("ARP across routers expected", "L2 boundary misunderstanding", "Check same subnet/mask"),
            ("Flapping connectivity", "Duplicate IP", "Watch neigh MAC changes"),
            ("Wrong VLAN", "No ARP replies", "Confirm switchport VLAN"),
            ("Stale FAIL neigh", "Old negative cache", "ip neigh flush / retry"),
        ],
        "guide": "Implement `arp_maps` (`IP-to-MAC`), `arp_crosses_routers` (`no`), and `linux_neigh_cmd` (`ip neigh`).",
        "examples": "`arp_maps` → `IP-to-MAC`; `arp_crosses_routers` → `no`; `linux_neigh_cmd` → `ip neigh`.",
    },
}

for n, d in reg_overrides.items():
    TOPICS[n] = d


# ---------------------------------------------------------------------------
# Exercises: each kind -> (starter, solution, tests)
# ---------------------------------------------------------------------------

def drill(funcs_starter_sol: list[tuple[str, str, str]], tests: list[tuple[str, str]]):
    """funcs: list of (comment, starter_line, sol_line) OR use triples of name logic.

    Actually pass list of (comment, name, starter_body_inner, sol_body_inner)
    """
    starter_parts = []
    sol_parts = []
    def _to_printf(inner: str) -> str:
        """Use printf so values like -n are not eaten by bash echo."""
        raw = inner.strip()
        if raw == 'echo ""':
            return 'printf "%s\\n" ""'
        m = re.match(r"^echo\s+(.+)$", raw)
        if not m:
            return inner
        arg = m.group(1).strip()
        if (arg.startswith("'") and arg.endswith("'")) or (
            arg.startswith('"') and arg.endswith('"')
        ):
            arg = arg[1:-1]
        # Escape for double-quoted printf format operand
        arg_esc = arg.replace("\\", "\\\\").replace('"', '\\"')
        return f'printf "%s\\n" "{arg_esc}"'

    for comment, name, starter_inner, sol_inner in funcs_starter_sol:
        # Bash one-liners require a semicolon before closing `}`
        s_inner = _to_printf(starter_inner.rstrip())
        o_inner = _to_printf(sol_inner.rstrip())
        if not s_inner.endswith(";"):
            s_inner += ";"
        if not o_inner.endswith(";"):
            o_inner += ";"
        starter_parts.append(f"# {comment}\n{name}() {{ {s_inner} }}")
        sol_parts.append(f"# {comment}\n{name}() {{ {o_inner} }}")
    return ("\n\n".join(starter_parts), "\n\n".join(sol_parts), tests)


EX: dict[str, tuple[str, str, list[tuple[str, str]]]] = {}


def put(kind, funcs, tests):
    EX[kind] = drill(funcs, tests)


# Each: (comment, fn_name, starter_inner, sol_inner)
put(
    "orient_hello",
    [
        ("Return a greeting for onboarding checks.", "greet", 'echo ""', 'echo "Hello, $1"'),
        ("Minimum size of the daily networking toolkit from the lesson.", "daily_tool_count_min", 'echo ""', "echo 5"),
        ("Four-step study loop as kebab-case words.", "study_loop", 'echo ""', 'echo "attempt-struggle-solution-rewrite"'),
    ],
    [("$(greet Net)", "Hello, Net"), ("$(daily_tool_count_min)", "5"), ("$(study_loop)", "attempt-struggle-solution-rewrite")],
)

put(
    "layer_ports",
    [
        ("OSI/TCPIP layer where TCP/UDP ports live.", "layer_for_ports", 'echo ""', "echo L4"),
        ("Layer for MAC addresses.", "layer_for_mac", 'echo ""', "echo L2"),
        ("Layer for HTTP.", "layer_for_http", 'echo ""', "echo L7"),
        ("TLS commonly rides on this transport (classic HTTPS).", "tls_rides_on", 'echo ""', "echo TCP"),
    ],
    [("$(layer_for_ports)", "L4"), ("$(layer_for_mac)", "L2"), ("$(layer_for_http)", "L7"), ("$(tls_rides_on)", "TCP")],
)

put(
    "mtu_quiz",
    [
        ("Typical Ethernet MTU in bytes.", "ethernet_typical_mtu", 'echo ""', "echo 1500"),
        ("What VPN headers usually do to effective MTU.", "vpn_overhead_effect", 'echo ""', 'echo "lowers-MTU"'),
        ("Why run large DF pings.", "df_ping_purpose", 'echo ""', 'echo "probe-path-MTU"'),
    ],
    [("$(ethernet_typical_mtu)", "1500"), ("$(vpn_overhead_effect)", "lowers-MTU"), ("$(df_ping_purpose)", "probe-path-MTU")],
)

put(
    "arp_map",
    [
        ("What ARP maps.", "arp_maps", 'echo ""', 'echo "IP-to-MAC"'),
        ("Does ARP cross routers? yes/no.", "arp_crosses_routers", 'echo ""', "echo no"),
        ("Modern Linux neighbor command (two words).", "linux_neigh_cmd", 'echo ""', 'echo "ip neigh"'),
    ],
    [("$(arp_maps)", "IP-to-MAC"), ("$(arp_crosses_routers)", "no"), ("$(linux_neigh_cmd)", "ip neigh")],
)

put(
    "ipv4_private",
    [
        ("yes/no if address is RFC1918-ish private (simplified).", "is_private", 'echo ""', 'case "$1" in 10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) echo yes ;; *) echo no ;; esac'),
        ("Loopback CIDR taught in the lesson.", "loopback_cidr", 'echo ""', 'echo "127.0.0.0/8"'),
        ("Link-local / APIPA prefix.", "link_local_prefix", 'echo ""', "echo 169.254"),
    ],
    [("$(is_private 10.0.0.1)", "yes"), ("$(is_private 8.8.8.8)", "no"), ("$(loopback_cidr)", "127.0.0.0/8"), ("$(link_local_prefix)", "169.254")],
)

put(
    "cidr_hosts",
    [
        ("Host bits for a prefix length /N.", "host_bits", 'echo ""', "echo $((32 - $1))"),
        ("Usable hosts estimate for /24 (2^8-2).", "usable_hosts_24", 'echo ""', "echo 254"),
        ("Does longer prefix mean smaller or larger network? smaller/larger.", "longer_prefix_means", 'echo ""', "echo smaller"),
    ],
    [("$(host_bits 24)", "8"), ("$(host_bits 26)", "6"), ("$(usable_hosts_24)", "254"), ("$(longer_prefix_means)", "smaller")],
)

put(
    "ipv6_aaaa",
    [
        ("DNS type for IPv6 addresses.", "dig_aaaa_type", 'echo ""', "echo AAAA"),
        ("IPv6 loopback address.", "ipv6_loopback", 'echo ""', "echo ::1"),
        ("Flag often used with dig for brief answers.", "dig_brief_flag", 'echo ""', 'echo "+short"'),
    ],
    [("$(dig_aaaa_type)", "AAAA"), ("$(ipv6_loopback)", "::1"), ("$(dig_brief_flag)", "+short")],
)

put(
    "ip_route_get",
    [
        ("Linux command to ask which route a destination would take (three words).", "cmd_route_get", 'echo ""', 'echo "ip route get"'),
        ("Show addresses briefly (two words).", "cmd_addr_brief", 'echo ""', 'echo "ip -br addr"'),
        ("Show link layer devices (two words).", "cmd_link_show", 'echo ""', 'echo "ip link"'),
    ],
    [("$(cmd_route_get)", "ip route get"), ("$(cmd_addr_brief)", "ip -br addr"), ("$(cmd_link_show)", "ip link")],
)

put(
    "ping_count",
    [
        ("Ping exactly three probes (two-token form).", "ping_three", 'echo ""', 'echo "ping -c 3"'),
        ("Tool that shows per-hop latency along a path.", "path_hop_tool", 'echo ""', "echo traceroute"),
        ("Continuous ping+loss tool often used by operators.", "loss_path_tool", 'echo ""', "echo mtr"),
    ],
    [("$(ping_three)", "ping -c 3"), ("$(path_hop_tool)", "traceroute"), ("$(loss_path_tool)", "mtr")],
)

put(
    "ss_flags",
    [
        ("Common ss flags for TCP/UDP listen with process.", "ss_listen_flags", 'echo ""', 'echo "-tulpn"'),
        ("Older command still seen on some systems.", "legacy_netstat", 'echo ""', "echo netstat"),
        ("Which tool maps sockets to processes by name often with -i/:port.", "files_ports_tool", 'echo ""', "echo lsof"),
    ],
    [("$(ss_listen_flags)", "-tulpn"), ("$(legacy_netstat)", "netstat"), ("$(files_ports_tool)", "lsof")],
)

put(
    "nc_vz",
    [
        ("nc flags for verbose zero-I/O connect check.", "nc_port_check_flags", 'echo ""', 'echo "-vz"'),
        ("Example listen on 9090 with nc -l (token).", "nc_listen_flag", 'echo ""', "echo -l"),
        ("More powerful relay/multipurpose cousin of nc.", "swiss_army_relay", 'echo ""', "echo socat"),
    ],
    [("$(nc_port_check_flags)", "-vz"), ("$(nc_listen_flag)", "-l"), ("$(swiss_army_relay)", "socat")],
)

put(
    "tcp_vs_udp",
    [
        ("Reliable ordered transport name.", "reliable_transport", 'echo ""', "echo TCP"),
        ("Best-effort datagram transport.", "datagram_transport", 'echo ""', "echo UDP"),
        ("First packet flag client sends in TCP handshake.", "tcp_first_flag", 'echo ""', "echo SYN"),
    ],
    [("$(reliable_transport)", "TCP"), ("$(datagram_transport)", "UDP"), ("$(tcp_first_flag)", "SYN")],
)

put(
    "dig_short",
    [
        ("dig option for brief answers.", "dig_short_flags", 'echo ""', 'echo "+short"'),
        ("Record type for IPv4.", "dns_type_a", 'echo ""', "echo A"),
        ("Record type for mail exchangers.", "dns_type_mx", 'echo ""', "echo MX"),
    ],
    [("$(dig_short_flags)", "+short"), ("$(dns_type_a)", "A"), ("$(dns_type_mx)", "MX")],
)

put(
    "dns_nx",
    [
        ("What NXDOMAIN means (kebab).", "nxdomain_means", 'echo ""', 'echo "name-not-exist"'),
        ("Likely meaning of SERVFAIL (kebab).", "servfail_means", 'echo ""', 'echo "resolver-error"'),
        ("Different answers inside vs outside VPN is called (kebab).", "split_dns_name", 'echo ""', 'echo "split-horizon"'),
    ],
    [("$(nxdomain_means)", "name-not-exist"), ("$(servfail_means)", "resolver-error"), ("$(split_dns_name)", "split-horizon")],
)

put(
    "curl_code",
    [
        ("curl flag for headers/response line only.", "curl_head_flag", 'echo ""', 'echo "-I"'),
        ("Write-out variable for HTTP status.", "curl_status_var", 'echo ""', 'echo "%{http_code}"'),
        ("Follow redirects flag.", "curl_follow_flag", 'echo ""', "echo -L"),
    ],
    [("$(curl_head_flag)", "-I"), ("$(curl_status_var)", "%{http_code}"), ("$(curl_follow_flag)", "-L")],
)

put(
    "tls_enddate",
    [
        ("openssl x509 flag showing validity dates.", "openssl_dates_flag", 'echo ""', 'echo "-dates"'),
        ("Why pass -servername to s_client (acronym).", "sni_acronym", 'echo ""', "echo SNI"),
        ("Certificate field listing hostnames (acronym).", "san_acronym", 'echo ""', "echo SAN"),
    ],
    [("$(openssl_dates_flag)", "-dates"), ("$(sni_acronym)", "SNI"), ("$(san_acronym)", "SAN")],
)

put(
    "route_default",
    [
        ("IPv4 default route CIDR.", "default_route_cidr", 'echo ""', 'echo "0.0.0.0/0"'),
        ("Which wins: more-specific /24 or /8? answer /24 or /8.", "longest_prefix_wins", 'echo ""', "echo /24"),
        ("Linux command words to resolve route for a dest.", "linux_route_get", 'echo ""', 'echo "ip route get"'),
    ],
    [("$(default_route_cidr)", "0.0.0.0/0"), ("$(longest_prefix_wins)", "/24"), ("$(linux_route_get)", "ip route get")],
)

put(
    "routing_bgp",
    [
        ("Internet inter-domain routing protocol.", "internet_routing_protocol", 'echo ""', "echo BGP"),
        ("Intra-org link-state protocol often compared.", "igp_example", 'echo ""', "echo OSPF"),
        ("Operator-defined routes are called.", "operator_routes", 'echo ""', "echo static"),
    ],
    [("$(internet_routing_protocol)", "BGP"), ("$(igp_example)", "OSPF"), ("$(operator_routes)", "static")],
)

put(
    "nat_pat",
    [
        ("Many-private-to-one-public NAT name.", "many_to_one_nat_name", 'echo ""', "echo PAT"),
        ("Accessing internal VIP via public IP from inside needs.", "hairpin_name", 'echo ""', "echo hairpin"),
        ("iptables table where NAT rules live.", "iptables_nat_table", 'echo ""', "echo nat"),
    ],
    [("$(many_to_one_nat_name)", "PAT"), ("$(hairpin_name)", "hairpin"), ("$(iptables_nat_table)", "nat")],
)

put(
    "fw_default",
    [
        ("Safe default inbound policy.", "safe_default_inbound", 'echo ""', "echo deny"),
        ("Modern Linux firewall framework.", "linux_fw_modern", 'echo ""', "echo nftables"),
        ("Ubuntu-friendly firewall frontend.", "ubuntu_fw_frontend", 'echo ""', "echo ufw"),
    ],
    [("$(safe_default_inbound)", "deny"), ("$(linux_fw_modern)", "nftables"), ("$(ubuntu_fw_frontend)", "ufw")],
)

put(
    "tcpdump_port",
    [
        ("BPF filter for DNS.", "tcpdump_dns_filter", 'echo ""', 'echo "port 53"'),
        ("tcpdump flag to avoid name resolution.", "tcpdump_numeric_flag", 'echo ""', "echo -n"),
        ("Write packets to file flag.", "tcpdump_write_flag", 'echo ""', "echo -w"),
    ],
    [("$(tcpdump_dns_filter)", "port 53"), ("$(tcpdump_numeric_flag)", "-n"), ("$(tcpdump_write_flag)", "-w")],
)

put(
    "tshark_dns",
    [
        ("tshark display filter flag.", "tshark_display_filter_flag", 'echo ""', 'echo "-Y"'),
        ("Read capture file flag.", "tshark_read_flag", 'echo ""', "echo -r"),
        ("GUI cousin of tshark.", "packet_gui_tool", 'echo ""', "echo wireshark"),
    ],
    [("$(tshark_display_filter_flag)", "-Y"), ("$(tshark_read_flag)", "-r"), ("$(packet_gui_tool)", "wireshark")],
)

put(
    "dhcp_apipa",
    [
        ("Prefix when DHCP fails (APIPA).", "dhcp_fail_prefix", 'echo ""', "echo 169.254"),
        ("Protocol that assigns addresses on LAN.", "addr_assign_proto", 'echo ""', "echo DHCP"),
        ("IPv6 cousin often used instead of DHCPv6 on LANs.", "ipv6_autoconfig", 'echo ""', "echo SLAAC"),
    ],
    [("$(dhcp_fail_prefix)", "169.254"), ("$(addr_assign_proto)", "DHCP"), ("$(ipv6_autoconfig)", "SLAAC")],
)

put(
    "vlan_tag",
    [
        ("VLAN tagging standard.", "vlan_tag_standard", 'echo ""', 'echo "802.1Q"'),
        ("Port carrying multiple VLANs is a.", "multi_vlan_port", 'echo ""', "echo trunk"),
        ("Broadcast domain separation feature name.", "l2_segment_feature", 'echo ""', "echo VLAN"),
    ],
    [("$(vlan_tag_standard)", "802.1Q"), ("$(multi_vlan_port)", "trunk"), ("$(l2_segment_feature)", "VLAN")],
)

put(
    "vpn_mtu",
    [
        ("VPNs often lower this.", "vpn_often_lowers", 'echo ""', "echo MTU"),
        ("Popular modern VPN that uses UDP usually.", "modern_vpn_example", 'echo ""', "echo WireGuard"),
        ("Classic site-to-site VPN suite acronym.", "classic_vpn_suite", 'echo ""', "echo IPsec"),
    ],
    [("$(vpn_often_lowers)", "MTU"), ("$(modern_vpn_example)", "WireGuard"), ("$(classic_vpn_suite)", "IPsec")],
)

put(
    "ssh_L",
    [
        ("ssh local forward flag.", "ssh_local_forward_flag", 'echo ""', 'echo "-L"'),
        ("ssh remote forward flag.", "ssh_remote_forward_flag", 'echo ""', 'echo "-R"'),
        ("ssh dynamic SOCKS flag.", "ssh_dynamic_flag", 'echo ""', 'echo "-D"'),
    ],
    [("$(ssh_local_forward_flag)", "-L"), ("$(ssh_remote_forward_flag)", "-R"), ("$(ssh_dynamic_flag)", "-D")],
)

put(
    "lb_l4l7",
    [
        ("HTTP path-based balancing layer.", "http_path_balancing_layer", 'echo ""', "echo L7"),
        ("TCP/UDP port-only balancing layer.", "port_only_balancing_layer", 'echo ""', "echo L4"),
        ("Probe that removes bad backends.", "backend_probe_name", 'echo ""', 'echo "health-check"'),
    ],
    [("$(http_path_balancing_layer)", "L7"), ("$(port_only_balancing_layer)", "L4"), ("$(backend_probe_name)", "health-check")],
)

put(
    "xff_trust",
    [
        ("Who may set X-Forwarded-For you trust (kebab).", "xff_trust_from", 'echo ""', 'echo "trusted-proxies-only"'),
        ("Proxy that terminates client TLS often called.", "tls_edge_role", 'echo ""', 'echo "TLS-termination"'),
        ("Header commonly used for original client proto.", "proto_forward_header", 'echo ""', 'echo "X-Forwarded-Proto"'),
    ],
    [("$(xff_trust_from)", "trusted-proxies-only"), ("$(tls_edge_role)", "TLS-termination"), ("$(proto_forward_header)", "X-Forwarded-Proto")],
)

put(
    "http_version",
    [
        ("curl write-out for HTTP version.", "curl_http_version_writeout", 'echo ""', 'echo "%{http_version}"'),
        ("HTTP/3 transport protocol name.", "http3_transport", 'echo ""', "echo QUIC"),
        ("HTTP/3 typical UDP port.", "http3_udp_port", 'echo ""', "echo 443"),
    ],
    [("$(curl_http_version_writeout)", "%{http_version}"), ("$(http3_transport)", "QUIC"), ("$(http3_udp_port)", "443")],
)

put(
    "cache_control",
    [
        ("Primary HTTP caching header.", "header_for_caching", 'echo ""', 'echo "Cache-Control"'),
        ("CDN role in one word.", "cdn_role", 'echo ""', "echo cache"),
        ("Validation header often paired with caches.", "cache_validator_header", 'echo ""', "echo ETag"),
    ],
    [("$(header_for_caching)", "Cache-Control"), ("$(cdn_role)", "cache"), ("$(cache_validator_header)", "ETag")],
)

put(
    "curl_timing",
    [
        ("curl write-out closest to TTFB.", "curl_ttfb_var", 'echo ""', 'echo "%{time_starttransfer}"'),
        ("Write-out for DNS phase.", "curl_dns_time_var", 'echo ""', 'echo "%{time_namelookup}"'),
        ("Latency SLOs prefer this summary statistic.", "latency_summary_stat", 'echo ""', "echo percentiles"),
    ],
    [("$(curl_ttfb_var)", "%{time_starttransfer}"), ("$(curl_dns_time_var)", "%{time_namelookup}"), ("$(latency_summary_stat)", "percentiles")],
)

put(
    "nmap_auth",
    [
        ("nmap scanning requires this.", "nmap_requires", 'echo ""', "echo authorization"),
        ("Common quick connect-scan flag set often taught as -sT or -sS; return sS for SYN.", "nmap_syn_flag", 'echo ""', "echo -sS"),
        ("Version detection flag.", "nmap_version_flag", 'echo ""', "echo -sV"),
    ],
    [("$(nmap_requires)", "authorization"), ("$(nmap_syn_flag)", "-sS"), ("$(nmap_version_flag)", "-sV")],
)

put(
    "asn_quiz",
    [
        ("ASN expands to (kebab).", "asn_means", 'echo ""', 'echo "autonomous-system-number"'),
        ("Protocol that exchanges routes between ASes.", "as_route_protocol", 'echo ""', "echo BGP"),
        ("IP blocks announced by ASes are called.", "ip_block_name", 'echo ""', "echo prefixes"),
    ],
    [("$(asn_means)", "autonomous-system-number"), ("$(as_route_protocol)", "BGP"), ("$(ip_block_name)", "prefixes")],
)

put(
    "anycast_quiz",
    [
        ("Anycast means (kebab).", "anycast_means", 'echo ""', 'echo "same-IP-many-places"'),
        ("DNS often uses anycast for this role.", "anycast_dns_role", 'echo ""', "echo resolver"),
        ("GeoDNS steers users using mostly.", "geodns_steers_with", 'echo ""', "echo DNS"),
    ],
    [("$(anycast_means)", "same-IP-many-places"), ("$(anycast_dns_role)", "resolver"), ("$(geodns_steers_with)", "DNS")],
)

put(
    "mx_quiz",
    [
        ("Mail exchanger DNS record.", "mail_dns_record", 'echo ""', "echo MX"),
        ("Sender policy framework record purpose acronym.", "spf_acronym", 'echo ""', "echo SPF"),
        ("Domain alignment reporting framework with DKIM/SPF.", "dmarc_acronym", 'echo ""', "echo DMARC"),
    ],
    [("$(mail_dns_record)", "MX"), ("$(spf_acronym)", "SPF"), ("$(dmarc_acronym)", "DMARC")],
)

put(
    "ntp_quiz",
    [
        ("Preferred timezone for logs.", "preferred_log_timezone", 'echo ""', "echo UTC"),
        ("Protocol that syncs clocks.", "time_sync_proto", 'echo ""', "echo NTP"),
        ("TLS cert validity depends on correct.", "certs_need_correct", 'echo ""', "echo time"),
    ],
    [("$(preferred_log_timezone)", "UTC"), ("$(time_sync_proto)", "NTP"), ("$(certs_need_correct)", "time")],
)

put(
    "wifi_quiz",
    [
        ("Wi-Fi network name broadcast.", "wifi_name_broadcast", 'echo ""', "echo SSID"),
        ("Wi-Fi operates primarily as which OSI layer family? L1-L2 or L3?", "wifi_layer_family", 'echo ""', "echo L1-L2"),
        ("Roaming issues often look like which intermittent symptom?", "wifi_symptom", 'echo ""', "echo drops"),
    ],
    [("$(wifi_name_broadcast)", "SSID"), ("$(wifi_layer_family)", "L1-L2"), ("$(wifi_symptom)", "drops")],
)

put(
    "docker_localhost",
    [
        ("localhost inside a container is.", "localhost_in_container_is", 'echo ""', 'echo "the-container"'),
        ("Default docker network driver often.", "docker_default_network", 'echo ""', "echo bridge"),
        ("Plugin model name for container networking in k8s ecosystem.", "container_net_plugin_model", 'echo ""', "echo CNI"),
    ],
    [("$(localhost_in_container_is)", "the-container"), ("$(docker_default_network)", "bridge"), ("$(container_net_plugin_model)", "CNI")],
)

put(
    "k8s_svc",
    [
        ("Cluster DNS implementation commonly.", "k8s_cluster_dns", 'echo ""', "echo CoreDNS"),
        ("Object that gives stable virtual IP to pods.", "k8s_stable_vip_object", 'echo ""', "echo Service"),
        ("East-west policy engine often discussed with k8s (one word).", "k8s_policy_sidecar_mesh", 'echo ""', "echo mesh"),
    ],
    [("$(k8s_cluster_dns)", "CoreDNS"), ("$(k8s_stable_vip_object)", "Service"), ("$(k8s_policy_sidecar_mesh)", "mesh")],
)

put(
    "vpc_cidrs",
    [
        ("Private subnet egress usually via.", "private_subnet_egress_via", 'echo ""', 'echo "NAT-gateway"'),
        ("Public subnet internet via.", "public_subnet_egress_via", 'echo ""', "echo IGW"),
        ("Cloud routing object mapping destinations.", "cloud_route_object", 'echo ""', 'echo "route-table"'),
    ],
    [("$(private_subnet_egress_via)", "NAT-gateway"), ("$(public_subnet_egress_via)", "IGW"), ("$(cloud_route_object)", "route-table")],
)

put(
    "sg_timeout",
    [
        ("Packet drop often looks like.", "packet_drop_often_looks_like", 'echo ""', "echo timeout"),
        ("AWS SG statefulness: stateful or stateless?", "sg_statefulness", 'echo ""', "echo stateful"),
        ("NACL statefulness: stateful or stateless?", "nacl_statefulness", 'echo ""', "echo stateless"),
    ],
    [("$(packet_drop_often_looks_like)", "timeout"), ("$(sg_statefulness)", "stateful"), ("$(nacl_statefulness)", "stateless")],
)

put(
    "mtls_quiz",
    [
        ("mTLS expands to (kebab).", "mtls_means", 'echo ""', 'echo "mutual-TLS"'),
        ("Both peers present a.", "mtls_both_present", 'echo ""', "echo certificate"),
        ("Service identity often bound to.", "service_identity_bound_to", 'echo ""', "echo certificate"),
    ],
    [("$(mtls_means)", "mutual-TLS"), ("$(mtls_both_present)", "certificate"), ("$(service_identity_bound_to)", "certificate")],
)

put(
    "dnssec_quiz",
    [
        ("DNSSEC primarily protects.", "dnssec_protects", 'echo ""', "echo authenticity"),
        ("DNSSEC does not encrypt this property of queries by itself.", "dnssec_not_encrypt", 'echo ""', "echo privacy"),
        ("Validation failure should not be silently ignored: yes/no.", "dnssec_fail_closed_idea", 'echo ""', "echo yes"),
    ],
    [("$(dnssec_protects)", "authenticity"), ("$(dnssec_not_encrypt)", "privacy"), ("$(dnssec_fail_closed_idea)", "yes")],
)

put(
    "obs_probe",
    [
        ("Latency better reported as.", "latency_better_as", 'echo ""', "echo percentiles"),
        ("Three pillars often listed with metrics/logs/?.", "third_obs_pillar", 'echo ""', "echo traces"),
        ("Synthetic check synonym.", "synthetic_check_name", 'echo ""', "echo probe"),
    ],
    [("$(latency_better_as)", "percentiles"), ("$(third_obs_pillar)", "traces"), ("$(synthetic_check_name)", "probe")],
)

put(
    "playbook_order",
    [
        ("First troubleshoot layer/focus.", "first_troubleshoot_layer", 'echo ""', "echo local"),
        ("After local L3, check this naming system.", "after_l3_check", 'echo ""', "echo DNS"),
        ("Prove a listener exists with.", "prove_listener_with", 'echo ""', "echo ss"),
    ],
    [("$(first_troubleshoot_layer)", "local"), ("$(after_l3_check)", "DNS"), ("$(prove_listener_with)", "ss")],
)

put(
    "perf_sysctl",
    [
        ("Order: measure then.", "measure_then", 'echo ""', "echo tune"),
        ("Kernel knobs interface name.", "kernel_knobs_iface", 'echo ""', "echo sysctl"),
        ("Blind tuning without baseline is.", "blind_tuning_is", 'echo ""', "echo harmful"),
    ],
    [("$(measure_then)", "tune"), ("$(kernel_knobs_iface)", "sysctl"), ("$(blind_tuning_is)", "harmful")],
)

put(
    "gw_504",
    [
        ("HTTP 504 often means (kebab).", "http_504_often", 'echo ""', 'echo "upstream-timeout"'),
        ("HTTP 502 often means (kebab).", "http_502_often", 'echo ""', 'echo "bad-gateway"'),
        ("Edge pattern terminating TLS then proxying is.", "edge_pattern", 'echo ""', 'echo "reverse-proxy"'),
    ],
    [("$(http_504_often)", "upstream-timeout"), ("$(http_502_often)", "bad-gateway"), ("$(edge_pattern)", "reverse-proxy")],
)

put(
    "zt_quiz",
    [
        ("Zero trust rejects (kebab).", "zero_trust_rejects", 'echo ""', 'echo "location-only-trust"'),
        ("Prefer verify every request: yes/no.", "verify_every_request", 'echo ""', "echo yes"),
        ("Identity over network location: identity/location?", "prefer_identity_or_location", 'echo ""', "echo identity"),
    ],
    [("$(zero_trust_rejects)", "location-only-trust"), ("$(verify_every_request)", "yes"), ("$(prefer_identity_or_location)", "identity")],
)

put(
    "lab_pair",
    [
        ("L3 proof tool.", "l3_proof_tool", 'echo ""', "echo ping"),
        ("L4 connect check tool.", "l4_proof_tool", 'echo ""', "echo nc"),
        ("Name resolution proof tool.", "dns_proof_tool", 'echo ""', "echo dig"),
    ],
    [("$(l3_proof_tool)", "ping"), ("$(l4_proof_tool)", "nc"), ("$(dns_proof_tool)", "dig")],
)

put(
    "cheat_count",
    [
        ("Daily tool count minimum from consolidation drill.", "daily_tool_count_min", 'echo ""', "echo 8"),
        ("Must include packet capture tool.", "capture_tool", 'echo ""', "echo tcpdump"),
        ("Must include HTTP client.", "http_client_tool", 'echo ""', "echo curl"),
    ],
    [("$(daily_tool_count_min)", "8"), ("$(capture_tool)", "tcpdump"), ("$(http_client_tool)", "curl")],
)

put(
    "vxlan_quiz",
    [
        ("VXLAN is an.", "vxlan_is_an", 'echo ""', "echo overlay"),
        ("VXLAN commonly encapsulates over.", "vxlan_over", 'echo ""', "echo UDP"),
        ("GRE is primarily a.", "gre_is_a", 'echo ""', "echo tunnel"),
    ],
    [("$(vxlan_is_an)", "overlay"), ("$(vxlan_over)", "UDP"), ("$(gre_is_a)", "tunnel")],
)

put(
    "middlebox_quiz",
    [
        ("HTTP/3 uses UDP port.", "http3_uses_udp_port", 'echo ""', "echo 443"),
        ("Middleboxes that assume only TCP 443 may break.", "broken_by_tcp_assume", 'echo ""', "echo QUIC"),
        ("Allowlisting only TCP can block.", "allowlist_tcp_blocks", 'echo ""', "echo UDP"),
    ],
    [("$(http3_uses_udp_port)", "443"), ("$(broken_by_tcp_assume)", "QUIC"), ("$(allowlist_tcp_blocks)", "UDP")],
)

put(
    "interview_drill",
    [
        ("Verify after fix? yes/no.", "verify_after_fix", 'echo ""', "echo yes"),
        ("State a hypothesis before tooling? yes/no.", "hypothesis_first", 'echo ""', "echo yes"),
        ("Gather evidence at one layer at a time? yes/no.", "one_layer_at_a_time", 'echo ""', "echo yes"),
    ],
    [("$(verify_after_fix)", "yes"), ("$(hypothesis_first)", "yes"), ("$(one_layer_at_a_time)", "yes")],
)

put(
    "cap_lab",
    [
        ("Capstone needs a.", "capstone_needs", 'echo ""', "echo diagram"),
        ("Document addressing plan? yes/no.", "need_address_plan", 'echo ""', "echo yes"),
        ("Prove east-west and north-south paths? yes/no.", "prove_paths", 'echo ""', "echo yes"),
    ],
    [("$(capstone_needs)", "diagram"), ("$(need_address_plan)", "yes"), ("$(prove_paths)", "yes")],
)

put(
    "cap_break",
    [
        ("Postmortem must include (kebab).", "postmortem_must_include", 'echo ""', 'echo "root-cause"'),
        ("Include timeline? yes/no.", "postmortem_timeline", 'echo ""', "echo yes"),
        ("Include verification steps? yes/no.", "postmortem_verify", 'echo ""', "echo yes"),
    ],
    [("$(postmortem_must_include)", "root-cause"), ("$(postmortem_timeline)", "yes"), ("$(postmortem_verify)", "yes")],
)

put(
    "cap_edge",
    [
        ("Edge should terminate.", "edge_should_terminate", 'echo ""', "echo TLS"),
        ("Forward client IP only from.", "forward_ip_from", 'echo ""', 'echo "trusted-proxies-only"'),
        ("Health checks must hit.", "health_checks_hit", 'echo ""', "echo upstream"),
    ],
    [("$(edge_should_terminate)", "TLS"), ("$(forward_ip_from)", "trusted-proxies-only"), ("$(health_checks_hit)", "upstream")],
)


GUIDE_FALLBACK = {
    # filled from EX function names if topic guide empty
}


def guide_for(kind: str, title: str) -> str:
    starter, _, tests = EX[kind]
    names = []
    for line in starter.splitlines():
        if "() {" in line:
            names.append(line.split("()")[0].strip())
    named = ", ".join(f"`{n}`" for n in names)
    return (
        f"Edit `exercise.sh` and implement {named}. Each function is a tiny retrieval drill for **{title}** — "
        f"return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing "
        f"when you would use that fact on-call. Run `./test.sh` until all {len(tests)} assertions pass."
    )


def examples_for(kind: str) -> str:
    _, _, tests = EX[kind]
    parts = []
    for got, want in tests:
        # got like $(fn args)
        inner = got.strip()
        if inner.startswith("$(") and inner.endswith(")"):
            call = inner[2:-1]
        else:
            call = inner
        parts.append(f"`{call}` → `{want}`")
    return "Expected: " + "; ".join(parts) + "."


def py_str(s: str) -> str:
    return repr(s)


def emit_curriculum(modules: list[dict]) -> str:
    phases = {
        "P0": "Phase 0 — Orientation",
        "P1": "Phase 1 — Models and packets",
        "P2": "Phase 2 — Addressing and subnets",
        "P3": "Phase 3 — Host networking toolkit",
        "P4": "Phase 4 — DNS",
        "P5": "Phase 5 — HTTP, TLS, and APIs",
        "P6": "Phase 6 — Routing",
        "P7": "Phase 7 — L2, switching, and local nets",
        "P8": "Phase 8 — Firewalls, NAT, and policy",
        "P9": "Phase 9 — VPN, tunnels, and overlays",
        "P10": "Phase 10 — Load balancing and proxies",
        "P11": "Phase 11 — Observability and troubleshooting",
        "P12": "Phase 12 — Cloud, containers, and modern nets",
        "P13": "Phase 13 — Capstones",
    }
    # reverse map phase string to const
    phase_const = {v: k for k, v in phases.items()}

    out = []
    out.append('#!/usr/bin/env python3')
    out.append('"""Networking Goodway curriculum modules 00–55 (command-heavy)."""')
    out.append("")
    out.append("from __future__ import annotations")
    out.append("")
    out.append("MODULES: list[dict] = []")
    out.append("")
    out.append(
        """
def add(
    n,
    slug,
    title,
    phase,
    days,
    objectives,
    body,
    pitfalls,
    checks,
    reading,
    ex_kind,
    exercise_guide="",
    exercise_examples="",
):
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
            exercise_guide=exercise_guide,
            exercise_examples=exercise_examples,
        )
    )
""".rstrip()
    )
    out.append("")
    for k, v in phases.items():
        out.append(f'{k} = "{v}"')
    out.append("")

    for m in modules:
        n = m["n"]
        slug = m["slug"].split("-", 1)[1]
        topic = TOPICS.get(n) or default_topic(m)
        # merge hand topic missing guide
        if not topic.get("guide"):
            topic = {**topic, "guide": guide_for(m["ex_kind"], m["title"])}
        if not topic.get("examples"):
            topic = {**topic, "examples": examples_for(m["ex_kind"])}
        # ensure TOPICS hand entries also get body assembly fields
        if n in TOPICS and "cmds" not in topic:
            raise SystemExit(f"bad topic {n}")
        if n not in TOPICS:
            # default_topic already complete
            pass
        body = assemble_body(m["title"], topic)
        pc = phase_const[m["phase"]]
        out.append(f"add(")
        out.append(f"    {n},")
        out.append(f"    {py_str(slug)},")
        out.append(f"    {py_str(m['title'])},")
        out.append(f"    {pc},")
        out.append(f"    {py_str(m['days'])},")
        out.append(f"    {py_str(m['objectives'])},")
        out.append(f"    {py_str(body)},")
        out.append(f"    {py_str(m['pitfalls'])},")
        out.append(f"    {py_str(m['checks'])},")
        out.append(f"    {py_str(m['reading'])},")
        out.append(f"    {py_str(m['ex_kind'])},")
        out.append(f"    exercise_guide={py_str(topic['guide'])},")
        out.append(f"    exercise_examples={py_str(topic['examples'])},")
        out.append(f")")
        out.append("")
    return "\n".join(out) + "\n"


def emit_exercises() -> str:
    out = [
        "#!/usr/bin/env python3",
        '"""Exercise starters/solutions/tests keyed by ex_kind."""',
        "",
        "# kind -> (starter_body, solution_body, [(got_shell_expr, want), ...])",
        "EX: dict[str, tuple[str, str, list[tuple[str, str]]]] = {",
    ]
    for kind, (starter, sol, tests) in EX.items():
        out.append(f"    {py_str(kind)}: (")
        out.append(f"        {py_str(starter)},")
        out.append(f"        {py_str(sol)},")
        out.append(f"        {py_str(tests)},")
        out.append(f"    ),")
    out.append("}")
    out.append("")
    return "\n".join(out)


def main():
    modules = load_modules()
    # Enrich TOPICS 0,1 already; ensure guides for hand topics
    for n, topic in list(TOPICS.items()):
        m = next(x for x in modules if x["n"] == n)
        if not topic.get("guide"):
            topic["guide"] = guide_for(m["ex_kind"], m["title"])
        if not topic.get("examples"):
            topic["examples"] = examples_for(m["ex_kind"])

    # Validate all kinds present
    used = {m["ex_kind"] for m in modules}
    missing = used - set(EX)
    if missing:
        raise SystemExit(f"EX missing kinds: {sorted(missing)}")

    cur = emit_curriculum(modules)
    ex = emit_exercises()
    (SCRIPTS / "curriculum_data.py").write_text(cur, encoding="utf-8")
    (SCRIPTS / "exercises_data.py").write_text(ex, encoding="utf-8")

    # stats
    spec = importlib.util.spec_from_file_location("cd2", SCRIPTS / "curriculum_data.py")
    m2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m2)
    bodies = [len(x["body"].strip()) for x in m2.MODULES]
    guides = sum(1 for x in m2.MODULES if x.get("exercise_guide"))
    print(f"modules={len(m2.MODULES)} body_chars min/med/max={min(bodies)}/{sorted(bodies)[len(bodies)//2]}/{max(bodies)}")
    print(f"guides={guides} exercise_kinds={len(EX)}")
    # function counts
    import re

    fn_counts = []
    for k, (st, _, tests) in EX.items():
        fn_counts.append((k, len(re.findall(r"^\\w+\\(\\)", st, re.M)), len(tests)))
    print("sample kinds fn/tests:", fn_counts[:3], "...", fn_counts[-2:])


if __name__ == "__main__":
    main()
