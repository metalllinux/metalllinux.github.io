---
title: "Good Command To Check For Killed Services In An So"
category: "general-linux"
tags: ["good", "command", "check", "killed", "services"]
---

```
grep killed daemon.log | awk '{$1=$2=$3=""; print}' | sort | uniq -c | sort -rn
```