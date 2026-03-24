---
title: "How To Format A Device As Fat32"
category: "general-linux"
tags: ["format", "device", "fat32"]
---

```
sudo mkfs.vfat -F 32 /dev/sd<LETTER><PARTITION_NUMBER>
```