---
title: "Awk Command To Show All Lines Between Two Timestam"
category: "editors-and-tools"
tags: ["editors-and-tools", "awk", "command", "show", "all"]
---

```
awk '$0 >= "2025-01-16T13:24:55+0000" && $0 <= "2025-01-16T14:58:25+0000"' <FILE>
```
* `$0` refers to the entire line.