---
title: "How To Constantly Show The Size Of A Directory"
category: "general-linux"
tags: ["constantly", "show", "size", "directory"]
---

```
watch -n0.1 "du -h --max-depth=1 | grep '\.'"
```