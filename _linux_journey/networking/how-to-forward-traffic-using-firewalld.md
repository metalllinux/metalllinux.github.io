---
title: "How To Forward Traffic Using Firewalld"
category: "networking"
tags: ["networking", "forward", "traffic", "firewalld"]
---

```
sudo firewall-cmd --add-forward-port=port=514:proto=udp:toport=1514 --permanent
```
```
sudo firewall-cmd --reload
```