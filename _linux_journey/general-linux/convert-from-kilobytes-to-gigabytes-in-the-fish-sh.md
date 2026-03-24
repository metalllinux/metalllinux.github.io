---
title: "Convert From Kilobytes To Gigabytes In The Fish Sh"
category: "general-linux"
tags: ["convert", "kilobytes", "gigabytes", "fish"]
---

```
set kb <kb_value_here>
set gb (math $kb / 1024 / 1024)
echo "$kb KB = $gb GB"
```