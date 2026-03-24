---
title: "How to Move All Directories Up by One Level"
category: "general-linux"
tags: ["move", "all", "directories", "one", "level"]
---

# How to Move All Directories Up by One Level
```
find ~/Documents/notes -mindepth 1 -maxdepth 1 -type d -exec mv {} ~/Documents/ \;
```
