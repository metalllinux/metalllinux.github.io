---
title: "How To Permanently Set Kernel Parameters"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "permanently", "kernel", "parameters"]
---

`su -`
`sysctl -w <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE> >> /etc/sysctl.conf`
Applied instantly and survive a reboot.

To temporarily tune the parameters, can do:
```
sysctl <TUNABLE_CLASS>.<PARAMETER>=<TARGET_VALUE>
```