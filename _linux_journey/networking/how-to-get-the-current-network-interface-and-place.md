---
title: "How To Get The Current Network Interface And Place"
category: "networking"
tags: ["networking", "current", "network", "interface", "place"]
---

```
CURRENT_INTERFACE=$(ip route | awk '/default/ {print $5}')
```