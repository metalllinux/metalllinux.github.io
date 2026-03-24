---
title: "How Stop Multiple Systemd Services"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "stop", "multiple", "systemd", "services"]
---

Using brace expansion:
```
sudo systemctl stop elasticsearch{a..f}
```