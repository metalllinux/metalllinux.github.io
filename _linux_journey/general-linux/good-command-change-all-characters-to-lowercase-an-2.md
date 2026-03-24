---
title: "Good Command Change All Characters To Lowercase An"
category: "general-linux"
tags: ["good", "command", "change", "all", "characters"]
---

```
for file in *; do mv "$file" `echo $file | tr ' ' '_' | tr '[:upper:]' '[:lower:]'`  ; done
```