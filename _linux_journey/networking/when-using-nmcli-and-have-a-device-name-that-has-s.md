---
title: "When Using Nmcli And Have A Device Name That Has S"
category: "networking"
tags: ["networking", "when", "nmcli", "device", "name"]
---

Use double quotes to select it:
```
sudo nmcli connection modify "Wired connection 1" ipv4.gateway <GATEWAY_IP>
```