---
title: "3.3.5 Ensure broadcast ICMP requests are ignored - 'net.ipv4.icmp_echo_ignore_broadcasts = 0'"
category: "general-linux"
tags: ["ensure", "broadcast", "icmp", "requests", "are"]
---

net.ipv4.icmp_echo_ignore_broadcasts=1

# 3.3.5 Ensure broadcast ICMP requests are ignored - 'net.ipv4.icmp_echo_ignore_broadcasts = 0'

##### Warning! Audit Deprecated

This audit has been deprecated and will be removed in a future update.

[View Next Audit Version](https://www.tenable.com/audits/CIS_Rocky_Linux_8_v2.0.0_L1_Server)

#### Information

Setting net.ipv4.icmp_echo_ignore_broadcasts to 1 will cause the system to ignore all ICMP echo and timestamp requests to broadcast and multicast addresses.  
  
Rationale:  
  
Accepting ICMP echo and timestamp requests with broadcast or multicast destinations for your network could be used to trick your host into starting (or participating) in a Smurf attack. A Smurf attack relies on an attacker sending large amounts of ICMP broadcast messages with a spoofed source address. All hosts receiving this message and responding would send echo-reply messages back to the spoofed address, which is probably not routable. If many hosts respond to the packets, the amount of traffic on the network could be significantly multiplied.  

#### Solution

Set the following parameters in /etc/sysctl.conf or a /etc/sysctl.d/\* file:  
Example:  
  
\# printf '  
net.ipv4.icmp_echo_ignore_broadcasts = 1  
' >> /etc/sysctl.d/60-netipv4_sysctl.conf  
  
Run the following command to set the active kernel parameters:  
  
\# {  
sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1  
sysctl -w net.ipv4.route.flush=1  
}  
  
  
  
  
Additional Information:  
  
NIST SP 800-53 Rev. 5:  
  
CM-1  
  
CM-2  
  
CM-6  
  
CM-7  
  
IA-5  

#### See Also

https://workbench.cisecurity.org/files/3807

#### Item Details

**Audit Name:** [CIS Rocky Linux 8 Server L1 v1.0.0](https://www.tenable.com/audits/CIS_Rocky_Linux_8_v1.0.0_L1_Server)

**References:** [CSCv7|9.2](https://www.tenable.com/audits/references/CSCv7/9.2)

**Plugin:** Unix

**Control ID:** [25c0e2bb7fa75bdf475547c9de72f77e9553087b409bdecc5026d28665c45f96](https://www.tenable.com/audits/items/search?q=controlId%3A%2825c0e2bb7fa75bdf475547c9de72f77e9553087b409bdecc5026d28665c45f96%29)

- [Tenable.com](https://www.tenable.com/)
- [Community & Support](https://community.tenable.com)
- [Documentation](https://docs.tenable.com)
- [Education](https://university.tenable.com)

- © 2025 Tenable®, Inc. All Rights Reserved
- [Privacy Policy](https://www.tenable.com/privacy-policy)
- [Legal](https://www.tenable.com/legal)
- [508 Compliance](https://www.tenable.com/section-508-voluntary-product-accessibility)