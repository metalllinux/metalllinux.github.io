---
title: "If Zfs Reports That It Is Not Installed Properly"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "zfs", "reports", "installed", "properly"]
---

Please run the following:

sudo apt-get install --reinstall zfs-dkms zfsutils-linux

After reinstalling the packages, try loading the ZFS module again using the modprobe command:

sudo modprobe zfs

If the issue persists, you can try manually building and installing the ZFS kernel module from source by following the instructions provided in the ZFS documentation for your operating system.