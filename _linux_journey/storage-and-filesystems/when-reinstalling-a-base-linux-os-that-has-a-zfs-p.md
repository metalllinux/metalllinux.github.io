---
title: "When Reinstalling A Base Linux Os That Has A Zfs P"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "when", "reinstalling", "base", "linux"]
---

* Firstly use `zfs pool export <pool_name>` to bring the pool down.
* Reinstall or change the Linux OS.
* Import the pool again with `zfs pool import`zpool export