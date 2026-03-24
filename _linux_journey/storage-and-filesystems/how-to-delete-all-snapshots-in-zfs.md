---
title: "How To Delete All Snapshots In Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "delete", "all", "snapshots", "zfs"]
---

* Switch to the `root` account.
* Use the following:
```
zfs list -H -o name -t snapshot | xargs -n1 zfs destroy
```