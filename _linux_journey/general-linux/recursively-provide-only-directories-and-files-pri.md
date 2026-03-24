---
title: "Recursively Provide Only Directories And Files Pri"
category: "general-linux"
tags: ["recursively", "provide", "only", "directories", "files"]
---

Directories
find /path/to/base/dir -type d -exec chmod 755 {} +

Files
find /path/to/base/dir -type f -exec chmod 644 {} +
