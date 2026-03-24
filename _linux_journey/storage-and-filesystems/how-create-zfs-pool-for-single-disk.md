---
title: "How Create Zfs Pool For Single Disk"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "zfs", "pool", "single"]
---

sudo zpool create -f -o ashift=12 -m /mnt/ravenwood/ ravenwood ata-Samsung_SSD_860_EVO_500GB_S4FNNE0M734821D