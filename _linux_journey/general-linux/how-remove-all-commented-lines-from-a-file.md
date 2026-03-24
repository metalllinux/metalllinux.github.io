---
title: "How Remove All Commented Lines From A File"
category: "general-linux"
tags: ["remove", "all", "commented", "lines", "file"]
---

```
sed -i '/^\s*#/d' <FILE>
```