---
title: "How Create Zfs Pool For Single Disk"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "zfs", "pool", "single"]
---

sudo zpool create -f -o ashift=12 -m /mnt/pool-hotel/ pool-hotel ata-DISK_SERIAL_3