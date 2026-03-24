---
title: "Useful DNS-related commands, dig, nslookup and host"
category: "networking"
tags: ["networking", "useful", "dns", "related", "troubleshooting"]
---

# Useful DNS-related commands, dig, nslookup and host

1. **dig +short HOST.COM**:
   - The `dig` command is used for querying DNS (Domain Name System) servers. It retrieves information about DNS records for a given domain.
   - The `+short` option simplifies the output by displaying only the IP addresses associated with the domain `HOST.COM`.

2. **host HOST.COM**:
   - The `host` command is another tool for DNS lookup. It provides detailed information about the domain `HOST.COM`, including its IP addresses, mail servers, and other DNS records.

3. **nslookup HOST.COM**:
   - The `nslookup` command is used to query DNS servers and obtain domain name or IP address mapping. It provides detailed information about the domain `HOST.COM`, similar to the `host` command.
