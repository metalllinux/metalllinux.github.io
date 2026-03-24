---
title: "Good Example Wireshark Filters"
category: "general-linux"
tags: ["good", "example", "wireshark", "filters"]
---

```
sip.Status-Code >= 400 && sip.Status-Code <= 499
sip.Status-Code >= 400 && sip.Status-Code <= 499 && not sip.Status-Code == 487
sip.Status-Code == 580
```