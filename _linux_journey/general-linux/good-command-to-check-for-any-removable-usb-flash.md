---
title: "Good Command To Check For Any Removable Usb Flash"
category: "general-linux"
tags: ["good", "command", "check", "any", "removable"]
---

```
echo "removable: $(cat /sys/block/sdc/removable), ro: $(cat /sys/block/sdc/ro), hidden: $(cat /sys/block/sdc/hidden), size: $(cat /sys/block/sdc/size), model: $(cat /sys/block/sdc/device/model)"
```