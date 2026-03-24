---
title: "Linux ARP Table Overflow"
category: "general-linux"
tags: ["linux", "arp", "table", "overflow", "ryan"]
---

# Linux ARP Table Overflow

[November 19, 2022](https://blog.rdorman.net/linux-arp-table-overflow/)

TL;DR – The `sysdig` utility can help you find the process sending ARP requests.

I recently ran into a problem with my “core” server. Its a trusty little Ubuntu 22.04.1 box that wears a lot of hats. In order to combine all of the functions it requires it has some more exotic network setups such as client VPNs, policy based routing, IPv6 an multiple wired and wireless interfaces. Linux is incredibly powerful but sometimes getting advanced features to work using the distro’s native tools is tough… but that’s not the point here.

I woke up this morning to DNS resolution being extremely slow, web pages for my monitoring system not fully loading, the general signs that something was up.

Taking a look at /var/log/syslog I found this message repeated over and over again:

`neighbour: arp_cache: neighbor table overflow!`

A quick look at the table with `arp -a` showed 1000’s of incomplete entries like the ones below

```
? (172.18.0.8) at <incomplete> on br-55a80fab0a50
? (172.18.1.192) at <incomplete> on br-55a80fab0a50
? (172.18.2.152) at <incomplete> on br-55a80fab0a50
? (192.168.1.191) at <incomplete> on eno1
? (172.18.0.51) at <incomplete> on br-55a80fab0a50
? (172.18.1.203) at <incomplete> on br-55a80fab0a50
? (172.18.2.131) at <incomplete> on br-55a80fab0a50
? (192.168.1.170) at <incomplete> on eno1
? (172.18.0.62) at <incomplete> on br-55a80fab0a50
? (172.18.1.246) at <incomplete> on br-55a80fab0a50
? (172.18.2.142) at <incomplete> on br-55a80fab0a50
? (192.168.1.213) at <incomplete> on eno1
? (172.18.0.41) at <incomplete> on br-55a80fab0a50
? (172.18.1.225) at <incomplete> on br-55a80fab0a50
? (172.18.2.185) at <incomplete> on br-55a80fab0a50
? (192.168.1.192) at <incomplete> on eno1
? (172.18.0.84) at <incomplete> on br-55a80fab0a50
? (172.18.1.236) at <incomplete> on br-55a80fab0a50
? (172.18.2.164) at <incomplete> on br-55a80fab0a50
? (192.168.1.203) at <incomplete> on eno1
? (172.18.0.95) at <incomplete> on br-55a80fab0a50
? (172.18.1.23) at <incomplete> on br-55a80fab0a50
? (172.18.2.175) at <incomplete> on br-55a80fab0a50
? (192.168.1.246) at <incomplete> on eno1
? (172.18.0.74) at <incomplete> on br-55a80fab0a50
? (172.18.1.2) at <incomplete> on br-55a80fab0a50
? (172.18.2.218) at <incomplete> on br-55a80fab0a50
? (192.168.1.225) at <incomplete> on eno1
```

This is obviously the symptom of SOMETHING scanning the network for usable IP’s. Because my docker virtual interfaces are all /16’s that’s 65k of addresses per docker network (i have 4) that its blasting all over the place.

You CAN clear the entire arp table with

`ip -s -s neigh flush all`

You can only delete individual entries with the standard `arp` command

Doesn’t matter however, flushing the table just filled it up with more entries as fast as they could be deleted.

Remember I said this box wears a lot of hats? That means there are a lot of places where this traffic could be coming from. Since this was only ARP traffic, and incomplete at that, I couldn’t use `tcpdump` or `lsof` (despite trying) to track down the source.

I eventually found [this incredible article](https://unix.stackexchange.com/questions/343855/how-does-one-determine-the-process-causing-an-arp-request) which sent me down the right path with a utility I had never heard of: `sysdig`

Sysdig was installed with standard apt commands but had some interesting post-installation instructions. It requires a kernel module that must be loaded at boot and must be properly signed in the UEFI world to not throw boot problems.

When you install sysdig it will ask you for a password, you only use this once so its not that critical. After the install is complete, reboot the system and a TUI will appear with options to allow you to install the MOK. Use the password you set above when prompted (it will not display \*\*\* or characters on the screen when typing). After the MOK was installed I was able to run this command as root:

`sysdig fd.rip=`x.x.x.x

x.x.x.x equaled one of the bogus IPs from the incomplete ARP entries.

Sure enough, it showed me the process. In my case it was a Homebridge plugin that creates motion sensors in Apple HomeKit based on the presence (or lack thereof) of a MAC address on your network. On a typical system scanning your local network isn’t that big a deal (tho not ideal) as people tend to run a /24. With all of the docker interfaces I just had too many potential IPs to scan.

[Linux](https://blog.rdorman.net/tag/linux/)

[My Journey to IPv6: Part 3 – Outbound Firewall](https://blog.rdorman.net/my-journey-to-ipv6-part-3/)

[Triggering HomeKit Automations with a Fortigate](https://blog.rdorman.net/triggering-homekit-automations-with-a-fortigate/)

### Leave a Reply

<a id="email-notes"></a>Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Save my name, email, and website in this browser for the next time I comment.

- [Howtos](https://blog.rdorman.net/category/howtos/)
- [Tips](https://blog.rdorman.net/category/tips/)

[AVD](https://blog.rdorman.net/tag/avd/) [AWS Workspaces](https://blog.rdorman.net/tag/aws-workspaces/) [Azure](https://blog.rdorman.net/tag/azure/) [Edge Workspaces](https://blog.rdorman.net/tag/edge-workspaces/) [Fortigate](https://blog.rdorman.net/tag/fortigate/) [FSLogix](https://blog.rdorman.net/tag/fslogix/) [GlobalProtect](https://blog.rdorman.net/tag/globalprotect/) [Intune](https://blog.rdorman.net/tag/intune/) [iOS](https://blog.rdorman.net/tag/ios/) [IPv6](https://blog.rdorman.net/tag/ipv6/) [JAMF](https://blog.rdorman.net/tag/jamf/) [Linux](https://blog.rdorman.net/tag/linux/) [MDM](https://blog.rdorman.net/tag/mdm/) [OneDrive](https://blog.rdorman.net/tag/onedrive/) [Palo Alto](https://blog.rdorman.net/tag/palo-alto/) [PowerAutomate](https://blog.rdorman.net/tag/powerautomate/) [PowerBI](https://blog.rdorman.net/tag/powerbi/) [PowerShell](https://blog.rdorman.net/tag/powershell/) [RDS](https://blog.rdorman.net/tag/rds/) [Security](https://blog.rdorman.net/tag/security/) [Teams](https://blog.rdorman.net/tag/teams/) [Windows](https://blog.rdorman.net/tag/windows/)

© Ryan Dorman 2022