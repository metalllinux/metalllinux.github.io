---
title: "How to Quickly and Easily Erase a Disk with dd"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "quickly", "easily", "erase", "disk"]
---

# How to Quickly and Easily Erase a Disk with dd

* Boot an openSUSE ISO.

* Go to `more`.

* Select `rescue system`.

* Login as `root` (no password needed).

```
sudo dd if=/dev/zero of=/dev/sdX bs=1M status=progress oflag=direct
```

`oflag=direct` bypasses the OS cache, which can improve performance.
