---
title: "How To Copy All Files In One Directory To Another"
category: "general-linux"
tags: ["copy", "all", "files", "one", "directory"]
---

```
rsync -AvP /mnt/silver25/handbrake/completed_encodes/* myuser@192.168.1.101:/mnt/server-a/films/
```