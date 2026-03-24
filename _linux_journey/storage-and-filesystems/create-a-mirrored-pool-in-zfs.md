---
title: "Create A Mirrored Pool In Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "mirrored", "pool", "zfs"]
---

`sudo zpool create -f -o ashift=12 -m /mnt/pool-alpha/ pool-alpha mirror ata-DISK_SERIAL_1 ata-DISK_SERIAL_2`