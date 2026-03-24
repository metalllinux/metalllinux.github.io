---
title: "How To List All Systemd Units In An Inactive State"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "list", "all", "systemd", "units"]
---

```
systemctl list-units --type=service --state=inactive
```