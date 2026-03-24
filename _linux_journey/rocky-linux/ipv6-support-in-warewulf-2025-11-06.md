---
title: "Ipv6 Support In Warewulf 2025 11 06"
category: "rocky-linux"
tags: ["rocky-linux", "ipv6", "support", "warewulf"]
---

Current IPv6 Support Status
Warewulf has basic IPv6 support that was introduced in version 4.3.0 and has been progressively improved.
As of v4.6.3, IPv6 is now supported during the iPXE network boot process, which is a significant step toward full IPv6 provisioning support. https://warewulf.org/docs/main/release/v4.6.3.html#ipv6-support
Configuration
To enable IPv6 in Warewulf, you need to configure the ipaddr6 parameter in warewulf.conf:
The IPv6 address must be specified in CIDR notation. When configured, Warewulf will automatically derive the IPv6 network prefix.
Example configuration:
ipaddr6: "2001:db8::1/64"
This will automatically set IPv6net to 2001:db8::
Provisioning Process
During the iPXE boot stage, Warewulf detects whether the request is coming from an IPv6 client and adjusts the authority URL accordingly:
The system supports both IPv4 and IPv6 simultaneously, with the provisioning logic automatically selecting the appropriate protocol based on the client's request.
Network Configuration
The network overlays (ifcfg, wicked, NetworkManager, etc.) include IPv6 configuration options.
Notes
Important limitations: While IPv6 support exists, it's still evolving. The v4.6.3 release notes specifically mention that IPv6 support during iPXE boot is "one step towards improving overall IPv6 support," indicating that full IPv6 provisioning may not be completely feature-complete yet.
There is no dedicated whitepaper or comprehensive guide specifically for IPv6 provisioning in the current documentation. The IPv6 functionality is documented through release notes and configuration file documentation.

The v4.6.3 release notes specifically mention that IPv6 support during iPXE boot is "one step towards improving overall IPv6 support"; however, at this time, full IPv6 provisioning may not be completely feature-complete.
