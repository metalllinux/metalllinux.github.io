---
title: "Useful Command To Capture Input From Different Com"
category: "general-linux"
tags: ["useful", "command", "capture", "input", "different"]
---

* Example:
```
set -x; lsblk; echo " "; lsblk -f; echo " "; cat /etc/crypttab; echo " "; cat /etc/fstab; echo " "; cat /etc/default/grub; echo " "; cat /proc/cmdline; echo " "; cryptsetup luksDump /dev/sdb3; echo " "; clevis luks list -d /dev/sdb3; set +x
```