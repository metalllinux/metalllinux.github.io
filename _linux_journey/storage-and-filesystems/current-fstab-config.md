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
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /              btrfs   subvol=/@,defaults,noatime,compress=zstd 0 0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /home          btrfs   subvol=/@home,defaults,noatime,compress=zstd
0 0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /root          btrfs   subvol=/@root,defaults,noatime,compress=zstd
0 0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /srv           btrfs   subvol=/@srv,defaults,noatime,compress=zstd 0
0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /var/cache     btrfs   subvol=/@cache,defaults,noatime,compress=zstd
0 0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /var/log       btrfs   subvol=/@log,defaults,noatime,compress=zstd 0
0
UUID=62956c80-7740-402c-95f9-9c78acb6b3dd /var/tmp       btrfs   subvol=/@tmp,defaults,noatime,compress=zstd 0
0
tmpfs                                     /tmp           tmpfs   defaults,noatime,mode=1777 0 0

UUID=60dc7b10-6eaf-45e5-9700-e9871348da84 /mnt/remeltindtdrinc btrfs defaults,compress=zstd 0 0
UUID=a1af14c0-ef76-4425-a1dc-9c4c3034c98a /mnt/meaddle btrfs defaults,compress=zstd 0 0