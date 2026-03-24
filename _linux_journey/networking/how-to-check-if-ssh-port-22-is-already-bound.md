---
title: "How To Check If Ssh Port 22 Is Already Bound"
category: "networking"
tags: ["networking", "check", "ssh", "port", "already"]
---

```
sudo netstat -tuln | grep ':22'
```