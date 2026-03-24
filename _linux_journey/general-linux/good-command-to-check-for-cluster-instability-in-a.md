---
title: "Good Command To Check For Cluster Instability In A"
category: "general-linux"
tags: ["good", "command", "check", "cluster", "instability"]
---

```
grep cluster messages | awk '{$1=$2=$3=$6=""; if($9~/\//){$9=""}; print}' | sort | uniq -c | sort -rn
```