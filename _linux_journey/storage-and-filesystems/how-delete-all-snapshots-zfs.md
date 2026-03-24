---
title: "How Delete All Snapshots Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "delete", "all", "snapshots", "zfs"]
---

zfs list -H -o name -t snapshot | xargs -n1 zfs destroy