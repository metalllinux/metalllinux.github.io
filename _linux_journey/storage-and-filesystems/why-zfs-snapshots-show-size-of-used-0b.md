---
title: "Why Zfs Snapshots Show Size Of Used 0B"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "zfs", "snapshots", "show", "size"]
---

```
A snapshot will only increase in size if you change or delete files which were present in the data set at the time the snapshot was taken.

ZFS is using copy-on-write snapshots, meaning that if a data block is about to be changed, a new copy of the block including the changes is being written to a different location in the storage pool and references in the relevant data set / volume are updated.

Snapshots have a size of zero if none of the blocks that were used by the data set at the time of the snapshot have been modified, thus the snapshot only differs from the current version of the data set in metadata only.
```