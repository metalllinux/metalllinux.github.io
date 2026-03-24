---
title: "How Add Zstd Compression To A Pool In Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "add", "zstd", "compression", "pool"]
---

`sudo zfs set compression=zstd-19 pool-alpha`

`zstd` has a default compression of `3` on ZFS and can be set from `1~19`