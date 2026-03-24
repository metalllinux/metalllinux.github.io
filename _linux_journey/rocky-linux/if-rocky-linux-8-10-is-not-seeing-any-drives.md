---
title: "If Rocky Linux 8.10 Is Not Seeing Any Drives"
category: "rocky-linux"
tags: ["rocky-linux", "rocky", "linux", "seeing", "any"]
---

* Drop into a shell with `ctrl + alt + F2` during the Anaconda Installer.
* Check the drive does not have any EFI partitions using `fdisk /dev/<drive_name>`
* Wipe all partitions on the drive using `wipefs -af /dev/<drive_name>`
* The installer should then recongise the drives and continue.