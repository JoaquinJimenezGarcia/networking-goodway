#!/usr/bin/env python3
"""Exercise starters/solutions/tests keyed by ex_kind."""

# kind -> (starter_body, solution_body, [(got_shell_expr, want), ...])
EX: dict[str, tuple[str, str, list[tuple[str, str]]]] = {
    "orient_hello": (
        'greet() { echo ""; }',
        'greet() { echo "Hello, $1"; }',
        [("$(greet Net)", "Hello, Net")],
    ),
    "layer_ports": (
        'layer_for_ports() { echo ""; }',
        "layer_for_ports() { echo L4; }",
        [("$(layer_for_ports)", "L4")],
    ),
    "mtu_quiz": (
        'ethernet_typical_mtu() { echo ""; }',
        "ethernet_typical_mtu() { echo 1500; }",
        [("$(ethernet_typical_mtu)", "1500")],
    ),
    "arp_map": (
        'arp_maps() { echo ""; }',
        'arp_maps() { echo "IP-to-MAC"; }',
        [("$(arp_maps)", "IP-to-MAC")],
    ),
    "ipv4_private": (
        'is_private() { echo ""; }',
        'is_private() { case "$1" in 10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) echo yes ;; *) echo no ;; esac; }',
        [("$(is_private 10.0.0.1)", "yes"), ("$(is_private 8.8.8.8)", "no")],
    ),
    "cidr_hosts": (
        'host_bits() { echo ""; }',
        "host_bits() { echo $((32 - $1)); }",
        [("$(host_bits 24)", "8"), ("$(host_bits 26)", "6")],
    ),
    "ipv6_aaaa": (
        'dig_aaaa_type() { echo ""; }',
        "dig_aaaa_type() { echo AAAA; }",
        [("$(dig_aaaa_type)", "AAAA")],
    ),
    "ip_route_get": (
        'cmd_route_get() { echo ""; }',
        'cmd_route_get() { echo "ip route get"; }',
        [("$(cmd_route_get)", "ip route get")],
    ),
    "ping_count": (
        'ping_three() { echo ""; }',
        'ping_three() { echo "ping -c 3"; }',
        [("$(ping_three)", "ping -c 3")],
    ),
    "ss_flags": (
        'ss_listen_flags() { echo ""; }',
        'ss_listen_flags() { echo "-tulpn"; }',
        [("$(ss_listen_flags)", "-tulpn")],
    ),
    "nc_vz": (
        'nc_port_check_flags() { echo ""; }',
        'nc_port_check_flags() { echo "-vz"; }',
        [("$(nc_port_check_flags)", "-vz")],
    ),
    "tcp_vs_udp": (
        'reliable_transport() { echo ""; }',
        "reliable_transport() { echo TCP; }",
        [("$(reliable_transport)", "TCP")],
    ),
    "dig_short": (
        'dig_short_flags() { echo ""; }',
        'dig_short_flags() { echo "+short"; }',
        [("$(dig_short_flags)", "+short")],
    ),
    "dns_nx": (
        'nxdomain_means() { echo ""; }',
        'nxdomain_means() { echo "name-not-exist"; }',
        [("$(nxdomain_means)", "name-not-exist")],
    ),
    "curl_code": (
        'curl_head_flag() { echo ""; }',
        'curl_head_flag() { echo "-I"; }',
        [("$(curl_head_flag)", "-I")],
    ),
    "tls_enddate": (
        'openssl_dates_flag() { echo ""; }',
        'openssl_dates_flag() { echo "-dates"; }',
        [("$(openssl_dates_flag)", "-dates")],
    ),
    "route_default": (
        'default_route_cidr() { echo ""; }',
        'default_route_cidr() { echo "0.0.0.0/0"; }',
        [("$(default_route_cidr)", "0.0.0.0/0")],
    ),
    "routing_bgp": (
        'internet_routing_protocol() { echo ""; }',
        "internet_routing_protocol() { echo BGP; }",
        [("$(internet_routing_protocol)", "BGP")],
    ),
    "nat_pat": (
        'many_to_one_nat_name() { echo ""; }',
        "many_to_one_nat_name() { echo PAT; }",
        [("$(many_to_one_nat_name)", "PAT")],
    ),
    "fw_default": (
        'safe_default_inbound() { echo ""; }',
        "safe_default_inbound() { echo deny; }",
        [("$(safe_default_inbound)", "deny")],
    ),
    "tcpdump_port": (
        'tcpdump_dns_filter() { echo ""; }',
        'tcpdump_dns_filter() { echo "port 53"; }',
        [("$(tcpdump_dns_filter)", "port 53")],
    ),
    "tshark_dns": (
        'tshark_display_filter_flag() { echo ""; }',
        'tshark_display_filter_flag() { echo "-Y"; }',
        [("$(tshark_display_filter_flag)", "-Y")],
    ),
    "dhcp_apipa": (
        'dhcp_fail_prefix() { echo ""; }',
        'dhcp_fail_prefix() { echo "169.254"; }',
        [("$(dhcp_fail_prefix)", "169.254")],
    ),
    "vlan_tag": (
        'vlan_tag_standard() { echo ""; }',
        'vlan_tag_standard() { echo "802.1Q"; }',
        [("$(vlan_tag_standard)", "802.1Q")],
    ),
    "vpn_mtu": (
        'vpn_often_lowers() { echo ""; }',
        "vpn_often_lowers() { echo MTU; }",
        [("$(vpn_often_lowers)", "MTU")],
    ),
    "ssh_L": (
        'ssh_local_forward_flag() { echo ""; }',
        'ssh_local_forward_flag() { echo "-L"; }',
        [("$(ssh_local_forward_flag)", "-L")],
    ),
    "lb_l4l7": (
        'http_path_balancing_layer() { echo ""; }',
        "http_path_balancing_layer() { echo L7; }",
        [("$(http_path_balancing_layer)", "L7")],
    ),
    "xff_trust": (
        'xff_trust_from() { echo ""; }',
        'xff_trust_from() { echo "trusted-proxies-only"; }',
        [("$(xff_trust_from)", "trusted-proxies-only")],
    ),
    "http_version": (
        'curl_http_version_writeout() { echo ""; }',
        'curl_http_version_writeout() { echo "%{http_version}"; }',
        [("$(curl_http_version_writeout)", "%{http_version}")],
    ),
    "cache_control": (
        'header_for_caching() { echo ""; }',
        'header_for_caching() { echo "Cache-Control"; }',
        [("$(header_for_caching)", "Cache-Control")],
    ),
    "curl_timing": (
        'curl_ttfb_var() { echo ""; }',
        'curl_ttfb_var() { echo "%{time_starttransfer}"; }',
        [("$(curl_ttfb_var)", "%{time_starttransfer}")],
    ),
    "nmap_auth": (
        'nmap_requires() { echo ""; }',
        "nmap_requires() { echo authorization; }",
        [("$(nmap_requires)", "authorization")],
    ),
    "asn_quiz": (
        'asn_means() { echo ""; }',
        'asn_means() { echo "autonomous-system-number"; }',
        [("$(asn_means)", "autonomous-system-number")],
    ),
    "anycast_quiz": (
        'anycast_means() { echo ""; }',
        'anycast_means() { echo "same-IP-many-places"; }',
        [("$(anycast_means)", "same-IP-many-places")],
    ),
    "mx_quiz": (
        'mail_dns_record() { echo ""; }',
        "mail_dns_record() { echo MX; }",
        [("$(mail_dns_record)", "MX")],
    ),
    "ntp_quiz": (
        'preferred_log_timezone() { echo ""; }',
        "preferred_log_timezone() { echo UTC; }",
        [("$(preferred_log_timezone)", "UTC")],
    ),
    "wifi_quiz": (
        'wifi_name_broadcast() { echo ""; }',
        "wifi_name_broadcast() { echo SSID; }",
        [("$(wifi_name_broadcast)", "SSID")],
    ),
    "docker_localhost": (
        'localhost_in_container_is() { echo ""; }',
        'localhost_in_container_is() { echo "the-container"; }',
        [("$(localhost_in_container_is)", "the-container")],
    ),
    "k8s_svc": (
        'k8s_cluster_dns() { echo ""; }',
        "k8s_cluster_dns() { echo CoreDNS; }",
        [("$(k8s_cluster_dns)", "CoreDNS")],
    ),
    "vpc_cidrs": (
        'private_subnet_egress_via() { echo ""; }',
        'private_subnet_egress_via() { echo "NAT-gateway"; }',
        [("$(private_subnet_egress_via)", "NAT-gateway")],
    ),
    "sg_timeout": (
        'packet_drop_often_looks_like() { echo ""; }',
        "packet_drop_often_looks_like() { echo timeout; }",
        [("$(packet_drop_often_looks_like)", "timeout")],
    ),
    "mtls_quiz": (
        'mtls_means() { echo ""; }',
        'mtls_means() { echo "mutual-TLS"; }',
        [("$(mtls_means)", "mutual-TLS")],
    ),
    "dnssec_quiz": (
        'dnssec_protects() { echo ""; }',
        "dnssec_protects() { echo authenticity; }",
        [("$(dnssec_protects)", "authenticity")],
    ),
    "obs_probe": (
        'latency_better_as() { echo ""; }',
        "latency_better_as() { echo percentiles; }",
        [("$(latency_better_as)", "percentiles")],
    ),
    "playbook_order": (
        'first_troubleshoot_layer() { echo ""; }',
        "first_troubleshoot_layer() { echo local; }",
        [("$(first_troubleshoot_layer)", "local")],
    ),
    "perf_sysctl": (
        'measure_then() { echo ""; }',
        "measure_then() { echo tune; }",
        [("$(measure_then)", "tune")],
    ),
    "gw_504": (
        'http_504_often() { echo ""; }',
        'http_504_often() { echo "upstream-timeout"; }',
        [("$(http_504_often)", "upstream-timeout")],
    ),
    "zt_quiz": (
        'zero_trust_rejects() { echo ""; }',
        'zero_trust_rejects() { echo "location-only-trust"; }',
        [("$(zero_trust_rejects)", "location-only-trust")],
    ),
    "lab_pair": (
        'l3_proof_tool() { echo ""; }',
        "l3_proof_tool() { echo ping; }",
        [("$(l3_proof_tool)", "ping")],
    ),
    "cheat_count": (
        'daily_tool_count_min() { echo ""; }',
        "daily_tool_count_min() { echo 8; }",
        [("$(daily_tool_count_min)", "8")],
    ),
    "vxlan_quiz": (
        'vxlan_is_an() { echo ""; }',
        "vxlan_is_an() { echo overlay; }",
        [("$(vxlan_is_an)", "overlay")],
    ),
    "middlebox_quiz": (
        'http3_uses_udp_port() { echo ""; }',
        "http3_uses_udp_port() { echo 443; }",
        [("$(http3_uses_udp_port)", "443")],
    ),
    "interview_drill": (
        'verify_after_fix() { echo ""; }',
        "verify_after_fix() { echo yes; }",
        [("$(verify_after_fix)", "yes")],
    ),
    "cap_lab": (
        'capstone_needs() { echo ""; }',
        "capstone_needs() { echo diagram; }",
        [("$(capstone_needs)", "diagram")],
    ),
    "cap_break": (
        'postmortem_must_include() { echo ""; }',
        'postmortem_must_include() { echo "root-cause"; }',
        [("$(postmortem_must_include)", "root-cause")],
    ),
    "cap_edge": (
        'edge_should_terminate() { echo ""; }',
        "edge_should_terminate() { echo TLS; }",
        [("$(edge_should_terminate)", "TLS")],
    ),
}
