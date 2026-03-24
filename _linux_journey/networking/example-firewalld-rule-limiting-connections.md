---
title: "Example Firewalld Rule Limiting Connections"
category: "networking"
tags: ["networking", "example", "firewalld", "rule", "limiting"]
---

```
firewall-cmd --permanent --add-rich-rule='rule service name="ssh" limit value="10/m" accept'
```