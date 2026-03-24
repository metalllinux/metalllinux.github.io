---
title: "When Tuning Kernel Parameters, If There Are 2 Or M"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "when", "tuning", "kernel", "parameters"]
---

For example, if you have the following:
```
net.ipv4.udp_mem = 11416320 15221760 22832640
```
To change the above values, we do:
```
su -
sysctl -w net.ipv4.udp_mem='<value_1 value_2 value_3>' >> /etc/sysctl.conf
```