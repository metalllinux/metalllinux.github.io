---
title: "How To Permanently Enable A Port In Firewalld"
category: "networking"
tags: ["networking", "permanently", "enable", "port", "firewalld"]
---

```
sudo firewall-cmd --permanent --add-port=<PORT_HERE>/<tcp/udp>
```
* Example:
```
sudo firewall-cmd --permanent --add-port=5173/tcp
```