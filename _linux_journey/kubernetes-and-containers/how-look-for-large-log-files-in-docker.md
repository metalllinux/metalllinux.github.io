---
title: "How Look For Large Log Files In Docker"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "look", "large", "log", "files"]
---

```
sudo find /var/lib/docker -type f -name "*json.log" -exec du -h {} \; | sort -hr
```