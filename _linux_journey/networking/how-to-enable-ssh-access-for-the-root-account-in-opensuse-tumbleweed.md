---
title: "How to Enable SSH Access on the Root User's Account in openSUSE Tumbleweed"
category: "networking"
tags: ["networking", "enable", "ssh", "access", "root"]
---

# How to Enable SSH Access on the Root User's Account in openSUSE Tumbleweed

Edit `/usr/etc/ssh/sshd_config`

Change `PermitRootLogin` to `PermitRootLogin yes`

Restart `sshd`:
```
systemctl restart sshd
```
