---
title: "How To Filter All Messages Between Two Time Points"
category: "general-linux"
tags: ["filter", "all", "messages", "between", "two"]
---

```
awk '$0 >= "Feb  5 11:00:00" && $0 < "Feb  5 12:00:00"' <file>
```