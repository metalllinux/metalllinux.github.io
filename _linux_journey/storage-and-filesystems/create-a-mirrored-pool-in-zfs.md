---
title: "Create A Mirrored Pool In Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "mirrored", "pool", "zfs"]
---

`sudo zpool create -f -o ashift=12 -m /mnt/dethklok/ dethklok mirror ata-WDC_WD40EZAZ-00SF3B0_WD-WX22D808TZXD ata-ST4000DM004-2CV104_ZTT5FNTT`