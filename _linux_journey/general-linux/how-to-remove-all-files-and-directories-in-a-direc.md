---
title: "How To Remove All Files And Directories In A Direc"
category: "general-linux"
tags: ["remove", "all", "files", "directories", "direc"]
---

```
find . ! -name '<FILE_YOU_WANT_TO_KEEP>' -exec rm -rf {} +
```