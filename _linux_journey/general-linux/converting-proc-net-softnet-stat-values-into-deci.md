---
title: "Converting Proc Net Softnet Stat Values Into Deci"
category: "general-linux"
tags: ["converting", "proc", "net", "softnet", "stat"]
---

awk '{for (i=1; i<=NF; i++) printf strtonum("0x" $i) (i==NF?"\n":" ")}' /proc/net/softnet_stat | column -t
First column: The total number of received frames
Second column: The number of dropped frames because of a full backlog queue
Last column: The CPU core number 