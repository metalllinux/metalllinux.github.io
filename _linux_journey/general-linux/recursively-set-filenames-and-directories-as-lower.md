---
title: "Recursively Set Filenames And Directories As Lower"
category: "general-linux"
tags: ["recursively", "filenames", "directories", "lower"]
---

```
for f in `find .`; do mv -v "$f" "`echo $f | tr '[A-Z]' '[a-z]'`"; done
```