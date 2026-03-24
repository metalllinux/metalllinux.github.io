---
title: "/etc/fstab: static file system information."
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "current", "fstab", "config"]
---

# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a device; this may
# be used with UUID= as a more robust way to name devices that works even if
# disks are added and removed. See fstab(5).
#
# <file system>             <mount point>  <type>  <options>  <dump>  <pass>
UUID=6D75-7792                            /boot/efi      vfat    defaults,noatime 0 2
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /              btrfs   subvol=/@,defaults,noatime,compress=zstd 0 0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /home          btrfs   subvol=/@home,defaults,noatime,compress=zstd
0 0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /root          btrfs   subvol=/@root,defaults,noatime,compress=zstd
0 0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /srv           btrfs   subvol=/@srv,defaults,noatime,compress=zstd 0
0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /var/cache     btrfs   subvol=/@cache,defaults,noatime,compress=zstd
0 0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /var/log       btrfs   subvol=/@log,defaults,noatime,compress=zstd 0
0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /var/tmp       btrfs   subvol=/@tmp,defaults,noatime,compress=zstd 0
0
tmpfs                                     /tmp           tmpfs   defaults,noatime,mode=1777 0 0

UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /mnt/pool-india btrfs defaults,compress=zstd 0 0
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /mnt/pool-juliet btrfs defaults,compress=zstd 0 0