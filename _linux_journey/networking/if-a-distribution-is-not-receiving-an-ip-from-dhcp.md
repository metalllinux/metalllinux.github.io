---
title: "If A Distribution Is Not Receiving An Ip From Dhcp"
category: "networking"
tags: ["networking", "distribution", "receiving", "dhcp"]
---

Check that ONBOOT is set to yes in /etc/sysconfig/network-scripts/[adapter_name]
Reboot or run `ifdown [adapter_name]` and `ifup [adapter_name]`