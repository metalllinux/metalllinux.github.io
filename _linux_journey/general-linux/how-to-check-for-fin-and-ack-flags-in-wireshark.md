---
title: "How To Check For Fin And Ack Flags In Wireshark"
category: "general-linux"
tags: ["check", "fin", "ack", "flags", "wireshark"]
---

```
tcp.flags.fin==1 && tcp.flags.ack==1
```