#!/usr/bin/env python3
"""Exercise starters/solutions/tests keyed by ex_kind."""

# kind -> (starter_body, solution_body, [(got_shell_expr, want), ...])
EX: dict[str, tuple[str, str, list[tuple[str, str]]]] = {
    'orient_hello': (
        '# Return a greeting for onboarding checks.\ngreet() { printf "%s\\n" ""; }\n\n# Minimum size of the daily networking toolkit from the lesson.\ndaily_tool_count_min() { printf "%s\\n" ""; }\n\n# Four-step study loop as kebab-case words.\nstudy_loop() { printf "%s\\n" ""; }',
        '# Return a greeting for onboarding checks.\ngreet() { printf "%s\\n" "Hello, $1"; }\n\n# Minimum size of the daily networking toolkit from the lesson.\ndaily_tool_count_min() { printf "%s\\n" "5"; }\n\n# Four-step study loop as kebab-case words.\nstudy_loop() { printf "%s\\n" "attempt-struggle-solution-rewrite"; }',
        [('$(greet Net)', 'Hello, Net'), ('$(daily_tool_count_min)', '5'), ('$(study_loop)', 'attempt-struggle-solution-rewrite')],
    ),
    'layer_ports': (
        '# OSI/TCPIP layer where TCP/UDP ports live.\nlayer_for_ports() { printf "%s\\n" ""; }\n\n# Layer for MAC addresses.\nlayer_for_mac() { printf "%s\\n" ""; }\n\n# Layer for HTTP.\nlayer_for_http() { printf "%s\\n" ""; }\n\n# TLS commonly rides on this transport (classic HTTPS).\ntls_rides_on() { printf "%s\\n" ""; }',
        '# OSI/TCPIP layer where TCP/UDP ports live.\nlayer_for_ports() { printf "%s\\n" "L4"; }\n\n# Layer for MAC addresses.\nlayer_for_mac() { printf "%s\\n" "L2"; }\n\n# Layer for HTTP.\nlayer_for_http() { printf "%s\\n" "L7"; }\n\n# TLS commonly rides on this transport (classic HTTPS).\ntls_rides_on() { printf "%s\\n" "TCP"; }',
        [('$(layer_for_ports)', 'L4'), ('$(layer_for_mac)', 'L2'), ('$(layer_for_http)', 'L7'), ('$(tls_rides_on)', 'TCP')],
    ),
    'mtu_quiz': (
        '# Typical Ethernet MTU in bytes.\nethernet_typical_mtu() { printf "%s\\n" ""; }\n\n# What VPN headers usually do to effective MTU.\nvpn_overhead_effect() { printf "%s\\n" ""; }\n\n# Why run large DF pings.\ndf_ping_purpose() { printf "%s\\n" ""; }',
        '# Typical Ethernet MTU in bytes.\nethernet_typical_mtu() { printf "%s\\n" "1500"; }\n\n# What VPN headers usually do to effective MTU.\nvpn_overhead_effect() { printf "%s\\n" "lowers-MTU"; }\n\n# Why run large DF pings.\ndf_ping_purpose() { printf "%s\\n" "probe-path-MTU"; }',
        [('$(ethernet_typical_mtu)', '1500'), ('$(vpn_overhead_effect)', 'lowers-MTU'), ('$(df_ping_purpose)', 'probe-path-MTU')],
    ),
    'arp_map': (
        '# What ARP maps.\narp_maps() { printf "%s\\n" ""; }\n\n# Does ARP cross routers? yes/no.\narp_crosses_routers() { printf "%s\\n" ""; }\n\n# Modern Linux neighbor command (two words).\nlinux_neigh_cmd() { printf "%s\\n" ""; }',
        '# What ARP maps.\narp_maps() { printf "%s\\n" "IP-to-MAC"; }\n\n# Does ARP cross routers? yes/no.\narp_crosses_routers() { printf "%s\\n" "no"; }\n\n# Modern Linux neighbor command (two words).\nlinux_neigh_cmd() { printf "%s\\n" "ip neigh"; }',
        [('$(arp_maps)', 'IP-to-MAC'), ('$(arp_crosses_routers)', 'no'), ('$(linux_neigh_cmd)', 'ip neigh')],
    ),
    'ipv4_private': (
        '# yes/no if address is RFC1918-ish private (simplified).\nis_private() { printf "%s\\n" ""; }\n\n# Loopback CIDR taught in the lesson.\nloopback_cidr() { printf "%s\\n" ""; }\n\n# Link-local / APIPA prefix.\nlink_local_prefix() { printf "%s\\n" ""; }',
        '# yes/no if address is RFC1918-ish private (simplified).\nis_private() { case "$1" in 10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) echo yes ;; *) echo no ;; esac; }\n\n# Loopback CIDR taught in the lesson.\nloopback_cidr() { printf "%s\\n" "127.0.0.0/8"; }\n\n# Link-local / APIPA prefix.\nlink_local_prefix() { printf "%s\\n" "169.254"; }',
        [('$(is_private 10.0.0.1)', 'yes'), ('$(is_private 8.8.8.8)', 'no'), ('$(loopback_cidr)', '127.0.0.0/8'), ('$(link_local_prefix)', '169.254')],
    ),
    'cidr_hosts': (
        '# Host bits for a prefix length /N.\nhost_bits() { printf "%s\\n" ""; }\n\n# Usable hosts estimate for /24 (2^8-2).\nusable_hosts_24() { printf "%s\\n" ""; }\n\n# Does longer prefix mean smaller or larger network? smaller/larger.\nlonger_prefix_means() { printf "%s\\n" ""; }',
        '# Host bits for a prefix length /N.\nhost_bits() { printf "%s\\n" "$((32 - $1))"; }\n\n# Usable hosts estimate for /24 (2^8-2).\nusable_hosts_24() { printf "%s\\n" "254"; }\n\n# Does longer prefix mean smaller or larger network? smaller/larger.\nlonger_prefix_means() { printf "%s\\n" "smaller"; }',
        [('$(host_bits 24)', '8'), ('$(host_bits 26)', '6'), ('$(usable_hosts_24)', '254'), ('$(longer_prefix_means)', 'smaller')],
    ),
    'ipv6_aaaa': (
        '# DNS type for IPv6 addresses.\ndig_aaaa_type() { printf "%s\\n" ""; }\n\n# IPv6 loopback address.\nipv6_loopback() { printf "%s\\n" ""; }\n\n# Flag often used with dig for brief answers.\ndig_brief_flag() { printf "%s\\n" ""; }',
        '# DNS type for IPv6 addresses.\ndig_aaaa_type() { printf "%s\\n" "AAAA"; }\n\n# IPv6 loopback address.\nipv6_loopback() { printf "%s\\n" "::1"; }\n\n# Flag often used with dig for brief answers.\ndig_brief_flag() { printf "%s\\n" "+short"; }',
        [('$(dig_aaaa_type)', 'AAAA'), ('$(ipv6_loopback)', '::1'), ('$(dig_brief_flag)', '+short')],
    ),
    'ip_route_get': (
        '# Linux command to ask which route a destination would take (three words).\ncmd_route_get() { printf "%s\\n" ""; }\n\n# Show addresses briefly (two words).\ncmd_addr_brief() { printf "%s\\n" ""; }\n\n# Show link layer devices (two words).\ncmd_link_show() { printf "%s\\n" ""; }',
        '# Linux command to ask which route a destination would take (three words).\ncmd_route_get() { printf "%s\\n" "ip route get"; }\n\n# Show addresses briefly (two words).\ncmd_addr_brief() { printf "%s\\n" "ip -br addr"; }\n\n# Show link layer devices (two words).\ncmd_link_show() { printf "%s\\n" "ip link"; }',
        [('$(cmd_route_get)', 'ip route get'), ('$(cmd_addr_brief)', 'ip -br addr'), ('$(cmd_link_show)', 'ip link')],
    ),
    'ping_count': (
        '# Ping exactly three probes (two-token form).\nping_three() { printf "%s\\n" ""; }\n\n# Tool that shows per-hop latency along a path.\npath_hop_tool() { printf "%s\\n" ""; }\n\n# Continuous ping+loss tool often used by operators.\nloss_path_tool() { printf "%s\\n" ""; }',
        '# Ping exactly three probes (two-token form).\nping_three() { printf "%s\\n" "ping -c 3"; }\n\n# Tool that shows per-hop latency along a path.\npath_hop_tool() { printf "%s\\n" "traceroute"; }\n\n# Continuous ping+loss tool often used by operators.\nloss_path_tool() { printf "%s\\n" "mtr"; }',
        [('$(ping_three)', 'ping -c 3'), ('$(path_hop_tool)', 'traceroute'), ('$(loss_path_tool)', 'mtr')],
    ),
    'ss_flags': (
        '# Common ss flags for TCP/UDP listen with process.\nss_listen_flags() { printf "%s\\n" ""; }\n\n# Older command still seen on some systems.\nlegacy_netstat() { printf "%s\\n" ""; }\n\n# Which tool maps sockets to processes by name often with -i/:port.\nfiles_ports_tool() { printf "%s\\n" ""; }',
        '# Common ss flags for TCP/UDP listen with process.\nss_listen_flags() { printf "%s\\n" "-tulpn"; }\n\n# Older command still seen on some systems.\nlegacy_netstat() { printf "%s\\n" "netstat"; }\n\n# Which tool maps sockets to processes by name often with -i/:port.\nfiles_ports_tool() { printf "%s\\n" "lsof"; }',
        [('$(ss_listen_flags)', '-tulpn'), ('$(legacy_netstat)', 'netstat'), ('$(files_ports_tool)', 'lsof')],
    ),
    'nc_vz': (
        '# nc flags for verbose zero-I/O connect check.\nnc_port_check_flags() { printf "%s\\n" ""; }\n\n# Example listen on 9090 with nc -l (token).\nnc_listen_flag() { printf "%s\\n" ""; }\n\n# More powerful relay/multipurpose cousin of nc.\nswiss_army_relay() { printf "%s\\n" ""; }',
        '# nc flags for verbose zero-I/O connect check.\nnc_port_check_flags() { printf "%s\\n" "-vz"; }\n\n# Example listen on 9090 with nc -l (token).\nnc_listen_flag() { printf "%s\\n" "-l"; }\n\n# More powerful relay/multipurpose cousin of nc.\nswiss_army_relay() { printf "%s\\n" "socat"; }',
        [('$(nc_port_check_flags)', '-vz'), ('$(nc_listen_flag)', '-l'), ('$(swiss_army_relay)', 'socat')],
    ),
    'tcp_vs_udp': (
        '# Reliable ordered transport name.\nreliable_transport() { printf "%s\\n" ""; }\n\n# Best-effort datagram transport.\ndatagram_transport() { printf "%s\\n" ""; }\n\n# First packet flag client sends in TCP handshake.\ntcp_first_flag() { printf "%s\\n" ""; }',
        '# Reliable ordered transport name.\nreliable_transport() { printf "%s\\n" "TCP"; }\n\n# Best-effort datagram transport.\ndatagram_transport() { printf "%s\\n" "UDP"; }\n\n# First packet flag client sends in TCP handshake.\ntcp_first_flag() { printf "%s\\n" "SYN"; }',
        [('$(reliable_transport)', 'TCP'), ('$(datagram_transport)', 'UDP'), ('$(tcp_first_flag)', 'SYN')],
    ),
    'dig_short': (
        '# dig option for brief answers.\ndig_short_flags() { printf "%s\\n" ""; }\n\n# Record type for IPv4.\ndns_type_a() { printf "%s\\n" ""; }\n\n# Record type for mail exchangers.\ndns_type_mx() { printf "%s\\n" ""; }',
        '# dig option for brief answers.\ndig_short_flags() { printf "%s\\n" "+short"; }\n\n# Record type for IPv4.\ndns_type_a() { printf "%s\\n" "A"; }\n\n# Record type for mail exchangers.\ndns_type_mx() { printf "%s\\n" "MX"; }',
        [('$(dig_short_flags)', '+short'), ('$(dns_type_a)', 'A'), ('$(dns_type_mx)', 'MX')],
    ),
    'dns_nx': (
        '# What NXDOMAIN means (kebab).\nnxdomain_means() { printf "%s\\n" ""; }\n\n# Likely meaning of SERVFAIL (kebab).\nservfail_means() { printf "%s\\n" ""; }\n\n# Different answers inside vs outside VPN is called (kebab).\nsplit_dns_name() { printf "%s\\n" ""; }',
        '# What NXDOMAIN means (kebab).\nnxdomain_means() { printf "%s\\n" "name-not-exist"; }\n\n# Likely meaning of SERVFAIL (kebab).\nservfail_means() { printf "%s\\n" "resolver-error"; }\n\n# Different answers inside vs outside VPN is called (kebab).\nsplit_dns_name() { printf "%s\\n" "split-horizon"; }',
        [('$(nxdomain_means)', 'name-not-exist'), ('$(servfail_means)', 'resolver-error'), ('$(split_dns_name)', 'split-horizon')],
    ),
    'curl_code': (
        '# curl flag for headers/response line only.\ncurl_head_flag() { printf "%s\\n" ""; }\n\n# Write-out variable for HTTP status.\ncurl_status_var() { printf "%s\\n" ""; }\n\n# Follow redirects flag.\ncurl_follow_flag() { printf "%s\\n" ""; }',
        '# curl flag for headers/response line only.\ncurl_head_flag() { printf "%s\\n" "-I"; }\n\n# Write-out variable for HTTP status.\ncurl_status_var() { printf "%s\\n" "%{http_code}"; }\n\n# Follow redirects flag.\ncurl_follow_flag() { printf "%s\\n" "-L"; }',
        [('$(curl_head_flag)', '-I'), ('$(curl_status_var)', '%{http_code}'), ('$(curl_follow_flag)', '-L')],
    ),
    'tls_enddate': (
        '# openssl x509 flag showing validity dates.\nopenssl_dates_flag() { printf "%s\\n" ""; }\n\n# Why pass -servername to s_client (acronym).\nsni_acronym() { printf "%s\\n" ""; }\n\n# Certificate field listing hostnames (acronym).\nsan_acronym() { printf "%s\\n" ""; }',
        '# openssl x509 flag showing validity dates.\nopenssl_dates_flag() { printf "%s\\n" "-dates"; }\n\n# Why pass -servername to s_client (acronym).\nsni_acronym() { printf "%s\\n" "SNI"; }\n\n# Certificate field listing hostnames (acronym).\nsan_acronym() { printf "%s\\n" "SAN"; }',
        [('$(openssl_dates_flag)', '-dates'), ('$(sni_acronym)', 'SNI'), ('$(san_acronym)', 'SAN')],
    ),
    'route_default': (
        '# IPv4 default route CIDR.\ndefault_route_cidr() { printf "%s\\n" ""; }\n\n# Which wins: more-specific /24 or /8? answer /24 or /8.\nlongest_prefix_wins() { printf "%s\\n" ""; }\n\n# Linux command words to resolve route for a dest.\nlinux_route_get() { printf "%s\\n" ""; }',
        '# IPv4 default route CIDR.\ndefault_route_cidr() { printf "%s\\n" "0.0.0.0/0"; }\n\n# Which wins: more-specific /24 or /8? answer /24 or /8.\nlongest_prefix_wins() { printf "%s\\n" "/24"; }\n\n# Linux command words to resolve route for a dest.\nlinux_route_get() { printf "%s\\n" "ip route get"; }',
        [('$(default_route_cidr)', '0.0.0.0/0'), ('$(longest_prefix_wins)', '/24'), ('$(linux_route_get)', 'ip route get')],
    ),
    'routing_bgp': (
        '# Internet inter-domain routing protocol.\ninternet_routing_protocol() { printf "%s\\n" ""; }\n\n# Intra-org link-state protocol often compared.\nigp_example() { printf "%s\\n" ""; }\n\n# Operator-defined routes are called.\noperator_routes() { printf "%s\\n" ""; }',
        '# Internet inter-domain routing protocol.\ninternet_routing_protocol() { printf "%s\\n" "BGP"; }\n\n# Intra-org link-state protocol often compared.\nigp_example() { printf "%s\\n" "OSPF"; }\n\n# Operator-defined routes are called.\noperator_routes() { printf "%s\\n" "static"; }',
        [('$(internet_routing_protocol)', 'BGP'), ('$(igp_example)', 'OSPF'), ('$(operator_routes)', 'static')],
    ),
    'nat_pat': (
        '# Many-private-to-one-public NAT name.\nmany_to_one_nat_name() { printf "%s\\n" ""; }\n\n# Accessing internal VIP via public IP from inside needs.\nhairpin_name() { printf "%s\\n" ""; }\n\n# iptables table where NAT rules live.\niptables_nat_table() { printf "%s\\n" ""; }',
        '# Many-private-to-one-public NAT name.\nmany_to_one_nat_name() { printf "%s\\n" "PAT"; }\n\n# Accessing internal VIP via public IP from inside needs.\nhairpin_name() { printf "%s\\n" "hairpin"; }\n\n# iptables table where NAT rules live.\niptables_nat_table() { printf "%s\\n" "nat"; }',
        [('$(many_to_one_nat_name)', 'PAT'), ('$(hairpin_name)', 'hairpin'), ('$(iptables_nat_table)', 'nat')],
    ),
    'fw_default': (
        '# Safe default inbound policy.\nsafe_default_inbound() { printf "%s\\n" ""; }\n\n# Modern Linux firewall framework.\nlinux_fw_modern() { printf "%s\\n" ""; }\n\n# Ubuntu-friendly firewall frontend.\nubuntu_fw_frontend() { printf "%s\\n" ""; }',
        '# Safe default inbound policy.\nsafe_default_inbound() { printf "%s\\n" "deny"; }\n\n# Modern Linux firewall framework.\nlinux_fw_modern() { printf "%s\\n" "nftables"; }\n\n# Ubuntu-friendly firewall frontend.\nubuntu_fw_frontend() { printf "%s\\n" "ufw"; }',
        [('$(safe_default_inbound)', 'deny'), ('$(linux_fw_modern)', 'nftables'), ('$(ubuntu_fw_frontend)', 'ufw')],
    ),
    'tcpdump_port': (
        '# BPF filter for DNS.\ntcpdump_dns_filter() { printf "%s\\n" ""; }\n\n# tcpdump flag to avoid name resolution.\ntcpdump_numeric_flag() { printf "%s\\n" ""; }\n\n# Write packets to file flag.\ntcpdump_write_flag() { printf "%s\\n" ""; }',
        '# BPF filter for DNS.\ntcpdump_dns_filter() { printf "%s\\n" "port 53"; }\n\n# tcpdump flag to avoid name resolution.\ntcpdump_numeric_flag() { printf "%s\\n" "-n"; }\n\n# Write packets to file flag.\ntcpdump_write_flag() { printf "%s\\n" "-w"; }',
        [('$(tcpdump_dns_filter)', 'port 53'), ('$(tcpdump_numeric_flag)', '-n'), ('$(tcpdump_write_flag)', '-w')],
    ),
    'tshark_dns': (
        '# tshark display filter flag.\ntshark_display_filter_flag() { printf "%s\\n" ""; }\n\n# Read capture file flag.\ntshark_read_flag() { printf "%s\\n" ""; }\n\n# GUI cousin of tshark.\npacket_gui_tool() { printf "%s\\n" ""; }',
        '# tshark display filter flag.\ntshark_display_filter_flag() { printf "%s\\n" "-Y"; }\n\n# Read capture file flag.\ntshark_read_flag() { printf "%s\\n" "-r"; }\n\n# GUI cousin of tshark.\npacket_gui_tool() { printf "%s\\n" "wireshark"; }',
        [('$(tshark_display_filter_flag)', '-Y'), ('$(tshark_read_flag)', '-r'), ('$(packet_gui_tool)', 'wireshark')],
    ),
    'dhcp_apipa': (
        '# Prefix when DHCP fails (APIPA).\ndhcp_fail_prefix() { printf "%s\\n" ""; }\n\n# Protocol that assigns addresses on LAN.\naddr_assign_proto() { printf "%s\\n" ""; }\n\n# IPv6 cousin often used instead of DHCPv6 on LANs.\nipv6_autoconfig() { printf "%s\\n" ""; }',
        '# Prefix when DHCP fails (APIPA).\ndhcp_fail_prefix() { printf "%s\\n" "169.254"; }\n\n# Protocol that assigns addresses on LAN.\naddr_assign_proto() { printf "%s\\n" "DHCP"; }\n\n# IPv6 cousin often used instead of DHCPv6 on LANs.\nipv6_autoconfig() { printf "%s\\n" "SLAAC"; }',
        [('$(dhcp_fail_prefix)', '169.254'), ('$(addr_assign_proto)', 'DHCP'), ('$(ipv6_autoconfig)', 'SLAAC')],
    ),
    'vlan_tag': (
        '# VLAN tagging standard.\nvlan_tag_standard() { printf "%s\\n" ""; }\n\n# Port carrying multiple VLANs is a.\nmulti_vlan_port() { printf "%s\\n" ""; }\n\n# Broadcast domain separation feature name.\nl2_segment_feature() { printf "%s\\n" ""; }',
        '# VLAN tagging standard.\nvlan_tag_standard() { printf "%s\\n" "802.1Q"; }\n\n# Port carrying multiple VLANs is a.\nmulti_vlan_port() { printf "%s\\n" "trunk"; }\n\n# Broadcast domain separation feature name.\nl2_segment_feature() { printf "%s\\n" "VLAN"; }',
        [('$(vlan_tag_standard)', '802.1Q'), ('$(multi_vlan_port)', 'trunk'), ('$(l2_segment_feature)', 'VLAN')],
    ),
    'vpn_mtu': (
        '# VPNs often lower this.\nvpn_often_lowers() { printf "%s\\n" ""; }\n\n# Popular modern VPN that uses UDP usually.\nmodern_vpn_example() { printf "%s\\n" ""; }\n\n# Classic site-to-site VPN suite acronym.\nclassic_vpn_suite() { printf "%s\\n" ""; }',
        '# VPNs often lower this.\nvpn_often_lowers() { printf "%s\\n" "MTU"; }\n\n# Popular modern VPN that uses UDP usually.\nmodern_vpn_example() { printf "%s\\n" "WireGuard"; }\n\n# Classic site-to-site VPN suite acronym.\nclassic_vpn_suite() { printf "%s\\n" "IPsec"; }',
        [('$(vpn_often_lowers)', 'MTU'), ('$(modern_vpn_example)', 'WireGuard'), ('$(classic_vpn_suite)', 'IPsec')],
    ),
    'ssh_L': (
        '# ssh local forward flag.\nssh_local_forward_flag() { printf "%s\\n" ""; }\n\n# ssh remote forward flag.\nssh_remote_forward_flag() { printf "%s\\n" ""; }\n\n# ssh dynamic SOCKS flag.\nssh_dynamic_flag() { printf "%s\\n" ""; }',
        '# ssh local forward flag.\nssh_local_forward_flag() { printf "%s\\n" "-L"; }\n\n# ssh remote forward flag.\nssh_remote_forward_flag() { printf "%s\\n" "-R"; }\n\n# ssh dynamic SOCKS flag.\nssh_dynamic_flag() { printf "%s\\n" "-D"; }',
        [('$(ssh_local_forward_flag)', '-L'), ('$(ssh_remote_forward_flag)', '-R'), ('$(ssh_dynamic_flag)', '-D')],
    ),
    'lb_l4l7': (
        '# HTTP path-based balancing layer.\nhttp_path_balancing_layer() { printf "%s\\n" ""; }\n\n# TCP/UDP port-only balancing layer.\nport_only_balancing_layer() { printf "%s\\n" ""; }\n\n# Probe that removes bad backends.\nbackend_probe_name() { printf "%s\\n" ""; }',
        '# HTTP path-based balancing layer.\nhttp_path_balancing_layer() { printf "%s\\n" "L7"; }\n\n# TCP/UDP port-only balancing layer.\nport_only_balancing_layer() { printf "%s\\n" "L4"; }\n\n# Probe that removes bad backends.\nbackend_probe_name() { printf "%s\\n" "health-check"; }',
        [('$(http_path_balancing_layer)', 'L7'), ('$(port_only_balancing_layer)', 'L4'), ('$(backend_probe_name)', 'health-check')],
    ),
    'xff_trust': (
        '# Who may set X-Forwarded-For you trust (kebab).\nxff_trust_from() { printf "%s\\n" ""; }\n\n# Proxy that terminates client TLS often called.\ntls_edge_role() { printf "%s\\n" ""; }\n\n# Header commonly used for original client proto.\nproto_forward_header() { printf "%s\\n" ""; }',
        '# Who may set X-Forwarded-For you trust (kebab).\nxff_trust_from() { printf "%s\\n" "trusted-proxies-only"; }\n\n# Proxy that terminates client TLS often called.\ntls_edge_role() { printf "%s\\n" "TLS-termination"; }\n\n# Header commonly used for original client proto.\nproto_forward_header() { printf "%s\\n" "X-Forwarded-Proto"; }',
        [('$(xff_trust_from)', 'trusted-proxies-only'), ('$(tls_edge_role)', 'TLS-termination'), ('$(proto_forward_header)', 'X-Forwarded-Proto')],
    ),
    'http_version': (
        '# curl write-out for HTTP version.\ncurl_http_version_writeout() { printf "%s\\n" ""; }\n\n# HTTP/3 transport protocol name.\nhttp3_transport() { printf "%s\\n" ""; }\n\n# HTTP/3 typical UDP port.\nhttp3_udp_port() { printf "%s\\n" ""; }',
        '# curl write-out for HTTP version.\ncurl_http_version_writeout() { printf "%s\\n" "%{http_version}"; }\n\n# HTTP/3 transport protocol name.\nhttp3_transport() { printf "%s\\n" "QUIC"; }\n\n# HTTP/3 typical UDP port.\nhttp3_udp_port() { printf "%s\\n" "443"; }',
        [('$(curl_http_version_writeout)', '%{http_version}'), ('$(http3_transport)', 'QUIC'), ('$(http3_udp_port)', '443')],
    ),
    'cache_control': (
        '# Primary HTTP caching header.\nheader_for_caching() { printf "%s\\n" ""; }\n\n# CDN role in one word.\ncdn_role() { printf "%s\\n" ""; }\n\n# Validation header often paired with caches.\ncache_validator_header() { printf "%s\\n" ""; }',
        '# Primary HTTP caching header.\nheader_for_caching() { printf "%s\\n" "Cache-Control"; }\n\n# CDN role in one word.\ncdn_role() { printf "%s\\n" "cache"; }\n\n# Validation header often paired with caches.\ncache_validator_header() { printf "%s\\n" "ETag"; }',
        [('$(header_for_caching)', 'Cache-Control'), ('$(cdn_role)', 'cache'), ('$(cache_validator_header)', 'ETag')],
    ),
    'curl_timing': (
        '# curl write-out closest to TTFB.\ncurl_ttfb_var() { printf "%s\\n" ""; }\n\n# Write-out for DNS phase.\ncurl_dns_time_var() { printf "%s\\n" ""; }\n\n# Latency SLOs prefer this summary statistic.\nlatency_summary_stat() { printf "%s\\n" ""; }',
        '# curl write-out closest to TTFB.\ncurl_ttfb_var() { printf "%s\\n" "%{time_starttransfer}"; }\n\n# Write-out for DNS phase.\ncurl_dns_time_var() { printf "%s\\n" "%{time_namelookup}"; }\n\n# Latency SLOs prefer this summary statistic.\nlatency_summary_stat() { printf "%s\\n" "percentiles"; }',
        [('$(curl_ttfb_var)', '%{time_starttransfer}'), ('$(curl_dns_time_var)', '%{time_namelookup}'), ('$(latency_summary_stat)', 'percentiles')],
    ),
    'nmap_auth': (
        '# nmap scanning requires this.\nnmap_requires() { printf "%s\\n" ""; }\n\n# Common quick connect-scan flag set often taught as -sT or -sS; return sS for SYN.\nnmap_syn_flag() { printf "%s\\n" ""; }\n\n# Version detection flag.\nnmap_version_flag() { printf "%s\\n" ""; }',
        '# nmap scanning requires this.\nnmap_requires() { printf "%s\\n" "authorization"; }\n\n# Common quick connect-scan flag set often taught as -sT or -sS; return sS for SYN.\nnmap_syn_flag() { printf "%s\\n" "-sS"; }\n\n# Version detection flag.\nnmap_version_flag() { printf "%s\\n" "-sV"; }',
        [('$(nmap_requires)', 'authorization'), ('$(nmap_syn_flag)', '-sS'), ('$(nmap_version_flag)', '-sV')],
    ),
    'asn_quiz': (
        '# ASN expands to (kebab).\nasn_means() { printf "%s\\n" ""; }\n\n# Protocol that exchanges routes between ASes.\nas_route_protocol() { printf "%s\\n" ""; }\n\n# IP blocks announced by ASes are called.\nip_block_name() { printf "%s\\n" ""; }',
        '# ASN expands to (kebab).\nasn_means() { printf "%s\\n" "autonomous-system-number"; }\n\n# Protocol that exchanges routes between ASes.\nas_route_protocol() { printf "%s\\n" "BGP"; }\n\n# IP blocks announced by ASes are called.\nip_block_name() { printf "%s\\n" "prefixes"; }',
        [('$(asn_means)', 'autonomous-system-number'), ('$(as_route_protocol)', 'BGP'), ('$(ip_block_name)', 'prefixes')],
    ),
    'anycast_quiz': (
        '# Anycast means (kebab).\nanycast_means() { printf "%s\\n" ""; }\n\n# DNS often uses anycast for this role.\nanycast_dns_role() { printf "%s\\n" ""; }\n\n# GeoDNS steers users using mostly.\ngeodns_steers_with() { printf "%s\\n" ""; }',
        '# Anycast means (kebab).\nanycast_means() { printf "%s\\n" "same-IP-many-places"; }\n\n# DNS often uses anycast for this role.\nanycast_dns_role() { printf "%s\\n" "resolver"; }\n\n# GeoDNS steers users using mostly.\ngeodns_steers_with() { printf "%s\\n" "DNS"; }',
        [('$(anycast_means)', 'same-IP-many-places'), ('$(anycast_dns_role)', 'resolver'), ('$(geodns_steers_with)', 'DNS')],
    ),
    'mx_quiz': (
        '# Mail exchanger DNS record.\nmail_dns_record() { printf "%s\\n" ""; }\n\n# Sender policy framework record purpose acronym.\nspf_acronym() { printf "%s\\n" ""; }\n\n# Domain alignment reporting framework with DKIM/SPF.\ndmarc_acronym() { printf "%s\\n" ""; }',
        '# Mail exchanger DNS record.\nmail_dns_record() { printf "%s\\n" "MX"; }\n\n# Sender policy framework record purpose acronym.\nspf_acronym() { printf "%s\\n" "SPF"; }\n\n# Domain alignment reporting framework with DKIM/SPF.\ndmarc_acronym() { printf "%s\\n" "DMARC"; }',
        [('$(mail_dns_record)', 'MX'), ('$(spf_acronym)', 'SPF'), ('$(dmarc_acronym)', 'DMARC')],
    ),
    'ntp_quiz': (
        '# Preferred timezone for logs.\npreferred_log_timezone() { printf "%s\\n" ""; }\n\n# Protocol that syncs clocks.\ntime_sync_proto() { printf "%s\\n" ""; }\n\n# TLS cert validity depends on correct.\ncerts_need_correct() { printf "%s\\n" ""; }',
        '# Preferred timezone for logs.\npreferred_log_timezone() { printf "%s\\n" "UTC"; }\n\n# Protocol that syncs clocks.\ntime_sync_proto() { printf "%s\\n" "NTP"; }\n\n# TLS cert validity depends on correct.\ncerts_need_correct() { printf "%s\\n" "time"; }',
        [('$(preferred_log_timezone)', 'UTC'), ('$(time_sync_proto)', 'NTP'), ('$(certs_need_correct)', 'time')],
    ),
    'wifi_quiz': (
        '# Wi-Fi network name broadcast.\nwifi_name_broadcast() { printf "%s\\n" ""; }\n\n# Wi-Fi operates primarily as which OSI layer family? L1-L2 or L3?\nwifi_layer_family() { printf "%s\\n" ""; }\n\n# Roaming issues often look like which intermittent symptom?\nwifi_symptom() { printf "%s\\n" ""; }',
        '# Wi-Fi network name broadcast.\nwifi_name_broadcast() { printf "%s\\n" "SSID"; }\n\n# Wi-Fi operates primarily as which OSI layer family? L1-L2 or L3?\nwifi_layer_family() { printf "%s\\n" "L1-L2"; }\n\n# Roaming issues often look like which intermittent symptom?\nwifi_symptom() { printf "%s\\n" "drops"; }',
        [('$(wifi_name_broadcast)', 'SSID'), ('$(wifi_layer_family)', 'L1-L2'), ('$(wifi_symptom)', 'drops')],
    ),
    'docker_localhost': (
        '# localhost inside a container is.\nlocalhost_in_container_is() { printf "%s\\n" ""; }\n\n# Default docker network driver often.\ndocker_default_network() { printf "%s\\n" ""; }\n\n# Plugin model name for container networking in k8s ecosystem.\ncontainer_net_plugin_model() { printf "%s\\n" ""; }',
        '# localhost inside a container is.\nlocalhost_in_container_is() { printf "%s\\n" "the-container"; }\n\n# Default docker network driver often.\ndocker_default_network() { printf "%s\\n" "bridge"; }\n\n# Plugin model name for container networking in k8s ecosystem.\ncontainer_net_plugin_model() { printf "%s\\n" "CNI"; }',
        [('$(localhost_in_container_is)', 'the-container'), ('$(docker_default_network)', 'bridge'), ('$(container_net_plugin_model)', 'CNI')],
    ),
    'k8s_svc': (
        '# Cluster DNS implementation commonly.\nk8s_cluster_dns() { printf "%s\\n" ""; }\n\n# Object that gives stable virtual IP to pods.\nk8s_stable_vip_object() { printf "%s\\n" ""; }\n\n# East-west policy engine often discussed with k8s (one word).\nk8s_policy_sidecar_mesh() { printf "%s\\n" ""; }',
        '# Cluster DNS implementation commonly.\nk8s_cluster_dns() { printf "%s\\n" "CoreDNS"; }\n\n# Object that gives stable virtual IP to pods.\nk8s_stable_vip_object() { printf "%s\\n" "Service"; }\n\n# East-west policy engine often discussed with k8s (one word).\nk8s_policy_sidecar_mesh() { printf "%s\\n" "mesh"; }',
        [('$(k8s_cluster_dns)', 'CoreDNS'), ('$(k8s_stable_vip_object)', 'Service'), ('$(k8s_policy_sidecar_mesh)', 'mesh')],
    ),
    'vpc_cidrs': (
        '# Private subnet egress usually via.\nprivate_subnet_egress_via() { printf "%s\\n" ""; }\n\n# Public subnet internet via.\npublic_subnet_egress_via() { printf "%s\\n" ""; }\n\n# Cloud routing object mapping destinations.\ncloud_route_object() { printf "%s\\n" ""; }',
        '# Private subnet egress usually via.\nprivate_subnet_egress_via() { printf "%s\\n" "NAT-gateway"; }\n\n# Public subnet internet via.\npublic_subnet_egress_via() { printf "%s\\n" "IGW"; }\n\n# Cloud routing object mapping destinations.\ncloud_route_object() { printf "%s\\n" "route-table"; }',
        [('$(private_subnet_egress_via)', 'NAT-gateway'), ('$(public_subnet_egress_via)', 'IGW'), ('$(cloud_route_object)', 'route-table')],
    ),
    'sg_timeout': (
        '# Packet drop often looks like.\npacket_drop_often_looks_like() { printf "%s\\n" ""; }\n\n# AWS SG statefulness: stateful or stateless?\nsg_statefulness() { printf "%s\\n" ""; }\n\n# NACL statefulness: stateful or stateless?\nnacl_statefulness() { printf "%s\\n" ""; }',
        '# Packet drop often looks like.\npacket_drop_often_looks_like() { printf "%s\\n" "timeout"; }\n\n# AWS SG statefulness: stateful or stateless?\nsg_statefulness() { printf "%s\\n" "stateful"; }\n\n# NACL statefulness: stateful or stateless?\nnacl_statefulness() { printf "%s\\n" "stateless"; }',
        [('$(packet_drop_often_looks_like)', 'timeout'), ('$(sg_statefulness)', 'stateful'), ('$(nacl_statefulness)', 'stateless')],
    ),
    'mtls_quiz': (
        '# mTLS expands to (kebab).\nmtls_means() { printf "%s\\n" ""; }\n\n# Both peers present a.\nmtls_both_present() { printf "%s\\n" ""; }\n\n# Service identity often bound to.\nservice_identity_bound_to() { printf "%s\\n" ""; }',
        '# mTLS expands to (kebab).\nmtls_means() { printf "%s\\n" "mutual-TLS"; }\n\n# Both peers present a.\nmtls_both_present() { printf "%s\\n" "certificate"; }\n\n# Service identity often bound to.\nservice_identity_bound_to() { printf "%s\\n" "certificate"; }',
        [('$(mtls_means)', 'mutual-TLS'), ('$(mtls_both_present)', 'certificate'), ('$(service_identity_bound_to)', 'certificate')],
    ),
    'dnssec_quiz': (
        '# DNSSEC primarily protects.\ndnssec_protects() { printf "%s\\n" ""; }\n\n# DNSSEC does not encrypt this property of queries by itself.\ndnssec_not_encrypt() { printf "%s\\n" ""; }\n\n# Validation failure should not be silently ignored: yes/no.\ndnssec_fail_closed_idea() { printf "%s\\n" ""; }',
        '# DNSSEC primarily protects.\ndnssec_protects() { printf "%s\\n" "authenticity"; }\n\n# DNSSEC does not encrypt this property of queries by itself.\ndnssec_not_encrypt() { printf "%s\\n" "privacy"; }\n\n# Validation failure should not be silently ignored: yes/no.\ndnssec_fail_closed_idea() { printf "%s\\n" "yes"; }',
        [('$(dnssec_protects)', 'authenticity'), ('$(dnssec_not_encrypt)', 'privacy'), ('$(dnssec_fail_closed_idea)', 'yes')],
    ),
    'obs_probe': (
        '# Latency better reported as.\nlatency_better_as() { printf "%s\\n" ""; }\n\n# Three pillars often listed with metrics/logs/?.\nthird_obs_pillar() { printf "%s\\n" ""; }\n\n# Synthetic check synonym.\nsynthetic_check_name() { printf "%s\\n" ""; }',
        '# Latency better reported as.\nlatency_better_as() { printf "%s\\n" "percentiles"; }\n\n# Three pillars often listed with metrics/logs/?.\nthird_obs_pillar() { printf "%s\\n" "traces"; }\n\n# Synthetic check synonym.\nsynthetic_check_name() { printf "%s\\n" "probe"; }',
        [('$(latency_better_as)', 'percentiles'), ('$(third_obs_pillar)', 'traces'), ('$(synthetic_check_name)', 'probe')],
    ),
    'playbook_order': (
        '# First troubleshoot layer/focus.\nfirst_troubleshoot_layer() { printf "%s\\n" ""; }\n\n# After local L3, check this naming system.\nafter_l3_check() { printf "%s\\n" ""; }\n\n# Prove a listener exists with.\nprove_listener_with() { printf "%s\\n" ""; }',
        '# First troubleshoot layer/focus.\nfirst_troubleshoot_layer() { printf "%s\\n" "local"; }\n\n# After local L3, check this naming system.\nafter_l3_check() { printf "%s\\n" "DNS"; }\n\n# Prove a listener exists with.\nprove_listener_with() { printf "%s\\n" "ss"; }',
        [('$(first_troubleshoot_layer)', 'local'), ('$(after_l3_check)', 'DNS'), ('$(prove_listener_with)', 'ss')],
    ),
    'perf_sysctl': (
        '# Order: measure then.\nmeasure_then() { printf "%s\\n" ""; }\n\n# Kernel knobs interface name.\nkernel_knobs_iface() { printf "%s\\n" ""; }\n\n# Blind tuning without baseline is.\nblind_tuning_is() { printf "%s\\n" ""; }',
        '# Order: measure then.\nmeasure_then() { printf "%s\\n" "tune"; }\n\n# Kernel knobs interface name.\nkernel_knobs_iface() { printf "%s\\n" "sysctl"; }\n\n# Blind tuning without baseline is.\nblind_tuning_is() { printf "%s\\n" "harmful"; }',
        [('$(measure_then)', 'tune'), ('$(kernel_knobs_iface)', 'sysctl'), ('$(blind_tuning_is)', 'harmful')],
    ),
    'gw_504': (
        '# HTTP 504 often means (kebab).\nhttp_504_often() { printf "%s\\n" ""; }\n\n# HTTP 502 often means (kebab).\nhttp_502_often() { printf "%s\\n" ""; }\n\n# Edge pattern terminating TLS then proxying is.\nedge_pattern() { printf "%s\\n" ""; }',
        '# HTTP 504 often means (kebab).\nhttp_504_often() { printf "%s\\n" "upstream-timeout"; }\n\n# HTTP 502 often means (kebab).\nhttp_502_often() { printf "%s\\n" "bad-gateway"; }\n\n# Edge pattern terminating TLS then proxying is.\nedge_pattern() { printf "%s\\n" "reverse-proxy"; }',
        [('$(http_504_often)', 'upstream-timeout'), ('$(http_502_often)', 'bad-gateway'), ('$(edge_pattern)', 'reverse-proxy')],
    ),
    'zt_quiz': (
        '# Zero trust rejects (kebab).\nzero_trust_rejects() { printf "%s\\n" ""; }\n\n# Prefer verify every request: yes/no.\nverify_every_request() { printf "%s\\n" ""; }\n\n# Identity over network location: identity/location?\nprefer_identity_or_location() { printf "%s\\n" ""; }',
        '# Zero trust rejects (kebab).\nzero_trust_rejects() { printf "%s\\n" "location-only-trust"; }\n\n# Prefer verify every request: yes/no.\nverify_every_request() { printf "%s\\n" "yes"; }\n\n# Identity over network location: identity/location?\nprefer_identity_or_location() { printf "%s\\n" "identity"; }',
        [('$(zero_trust_rejects)', 'location-only-trust'), ('$(verify_every_request)', 'yes'), ('$(prefer_identity_or_location)', 'identity')],
    ),
    'lab_pair': (
        '# L3 proof tool.\nl3_proof_tool() { printf "%s\\n" ""; }\n\n# L4 connect check tool.\nl4_proof_tool() { printf "%s\\n" ""; }\n\n# Name resolution proof tool.\ndns_proof_tool() { printf "%s\\n" ""; }',
        '# L3 proof tool.\nl3_proof_tool() { printf "%s\\n" "ping"; }\n\n# L4 connect check tool.\nl4_proof_tool() { printf "%s\\n" "nc"; }\n\n# Name resolution proof tool.\ndns_proof_tool() { printf "%s\\n" "dig"; }',
        [('$(l3_proof_tool)', 'ping'), ('$(l4_proof_tool)', 'nc'), ('$(dns_proof_tool)', 'dig')],
    ),
    'cheat_count': (
        '# Daily tool count minimum from consolidation drill.\ndaily_tool_count_min() { printf "%s\\n" ""; }\n\n# Must include packet capture tool.\ncapture_tool() { printf "%s\\n" ""; }\n\n# Must include HTTP client.\nhttp_client_tool() { printf "%s\\n" ""; }',
        '# Daily tool count minimum from consolidation drill.\ndaily_tool_count_min() { printf "%s\\n" "8"; }\n\n# Must include packet capture tool.\ncapture_tool() { printf "%s\\n" "tcpdump"; }\n\n# Must include HTTP client.\nhttp_client_tool() { printf "%s\\n" "curl"; }',
        [('$(daily_tool_count_min)', '8'), ('$(capture_tool)', 'tcpdump'), ('$(http_client_tool)', 'curl')],
    ),
    'vxlan_quiz': (
        '# VXLAN is an.\nvxlan_is_an() { printf "%s\\n" ""; }\n\n# VXLAN commonly encapsulates over.\nvxlan_over() { printf "%s\\n" ""; }\n\n# GRE is primarily a.\ngre_is_a() { printf "%s\\n" ""; }',
        '# VXLAN is an.\nvxlan_is_an() { printf "%s\\n" "overlay"; }\n\n# VXLAN commonly encapsulates over.\nvxlan_over() { printf "%s\\n" "UDP"; }\n\n# GRE is primarily a.\ngre_is_a() { printf "%s\\n" "tunnel"; }',
        [('$(vxlan_is_an)', 'overlay'), ('$(vxlan_over)', 'UDP'), ('$(gre_is_a)', 'tunnel')],
    ),
    'middlebox_quiz': (
        '# HTTP/3 uses UDP port.\nhttp3_uses_udp_port() { printf "%s\\n" ""; }\n\n# Middleboxes that assume only TCP 443 may break.\nbroken_by_tcp_assume() { printf "%s\\n" ""; }\n\n# Allowlisting only TCP can block.\nallowlist_tcp_blocks() { printf "%s\\n" ""; }',
        '# HTTP/3 uses UDP port.\nhttp3_uses_udp_port() { printf "%s\\n" "443"; }\n\n# Middleboxes that assume only TCP 443 may break.\nbroken_by_tcp_assume() { printf "%s\\n" "QUIC"; }\n\n# Allowlisting only TCP can block.\nallowlist_tcp_blocks() { printf "%s\\n" "UDP"; }',
        [('$(http3_uses_udp_port)', '443'), ('$(broken_by_tcp_assume)', 'QUIC'), ('$(allowlist_tcp_blocks)', 'UDP')],
    ),
    'interview_drill': (
        '# Verify after fix? yes/no.\nverify_after_fix() { printf "%s\\n" ""; }\n\n# State a hypothesis before tooling? yes/no.\nhypothesis_first() { printf "%s\\n" ""; }\n\n# Gather evidence at one layer at a time? yes/no.\none_layer_at_a_time() { printf "%s\\n" ""; }',
        '# Verify after fix? yes/no.\nverify_after_fix() { printf "%s\\n" "yes"; }\n\n# State a hypothesis before tooling? yes/no.\nhypothesis_first() { printf "%s\\n" "yes"; }\n\n# Gather evidence at one layer at a time? yes/no.\none_layer_at_a_time() { printf "%s\\n" "yes"; }',
        [('$(verify_after_fix)', 'yes'), ('$(hypothesis_first)', 'yes'), ('$(one_layer_at_a_time)', 'yes')],
    ),
    'cap_lab': (
        '# Capstone needs a.\ncapstone_needs() { printf "%s\\n" ""; }\n\n# Document addressing plan? yes/no.\nneed_address_plan() { printf "%s\\n" ""; }\n\n# Prove east-west and north-south paths? yes/no.\nprove_paths() { printf "%s\\n" ""; }',
        '# Capstone needs a.\ncapstone_needs() { printf "%s\\n" "diagram"; }\n\n# Document addressing plan? yes/no.\nneed_address_plan() { printf "%s\\n" "yes"; }\n\n# Prove east-west and north-south paths? yes/no.\nprove_paths() { printf "%s\\n" "yes"; }',
        [('$(capstone_needs)', 'diagram'), ('$(need_address_plan)', 'yes'), ('$(prove_paths)', 'yes')],
    ),
    'cap_break': (
        '# Postmortem must include (kebab).\npostmortem_must_include() { printf "%s\\n" ""; }\n\n# Include timeline? yes/no.\npostmortem_timeline() { printf "%s\\n" ""; }\n\n# Include verification steps? yes/no.\npostmortem_verify() { printf "%s\\n" ""; }',
        '# Postmortem must include (kebab).\npostmortem_must_include() { printf "%s\\n" "root-cause"; }\n\n# Include timeline? yes/no.\npostmortem_timeline() { printf "%s\\n" "yes"; }\n\n# Include verification steps? yes/no.\npostmortem_verify() { printf "%s\\n" "yes"; }',
        [('$(postmortem_must_include)', 'root-cause'), ('$(postmortem_timeline)', 'yes'), ('$(postmortem_verify)', 'yes')],
    ),
    'cap_edge': (
        '# Edge should terminate.\nedge_should_terminate() { printf "%s\\n" ""; }\n\n# Forward client IP only from.\nforward_ip_from() { printf "%s\\n" ""; }\n\n# Health checks must hit.\nhealth_checks_hit() { printf "%s\\n" ""; }',
        '# Edge should terminate.\nedge_should_terminate() { printf "%s\\n" "TLS"; }\n\n# Forward client IP only from.\nforward_ip_from() { printf "%s\\n" "trusted-proxies-only"; }\n\n# Health checks must hit.\nhealth_checks_hit() { printf "%s\\n" "upstream"; }',
        [('$(edge_should_terminate)', 'TLS'), ('$(forward_ip_from)', 'trusted-proxies-only'), ('$(health_checks_hit)', 'upstream')],
    ),
}
