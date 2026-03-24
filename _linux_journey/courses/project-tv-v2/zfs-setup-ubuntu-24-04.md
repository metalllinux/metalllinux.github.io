---
title: "Zfs Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "zfs", "setup", "ubuntu"]
---

* Install the `zfsutils-linux` package:
```
sudo apt install -y zfsutils-linux
```
* Verify the installation was successful:
```
zfs version
```
* Load the ZFS kernel module:
```
sudo modprobe zfs
```
* Check that the `zfs` module is loaded:
```
lsmod | grep zfs
```