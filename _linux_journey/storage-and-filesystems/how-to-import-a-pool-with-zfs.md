---
title: "How To Import A Pool With Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "import", "pool", "zfs"]
---

sudo zpool import POOL_NAME

May have to do `sudo zpool import POOL_NAME -f` if it has been accessed on another system.