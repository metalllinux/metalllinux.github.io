---
title: "How Export A Zfs Pool For Use On Another System"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "export", "zfs", "pool", "another"]
---

```
sudo zpool export <pool_name>
```
Find the pool name from `zpool status`