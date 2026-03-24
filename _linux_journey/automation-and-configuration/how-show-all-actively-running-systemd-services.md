---
title: "How Show All Actively Running Systemd Services"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "show", "all", "actively", "running"]
---

```
systemctl list-units --type=service --state=running
```