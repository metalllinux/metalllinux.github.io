---
title: "How To Create, Format And Mount A Luks Drive"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "format", "mount", "luks"]
---

 288  sudo cryptsetup luksFormat --type luks2 /dev/sdf
  289  sudo cryptsetup -v luksOpen /dev/sdf pool-kilo
  290  mkfs.ext4 /dev/mapper/pool-kilo
  291  sudo apt install mkfs
  292  sudo mkfs.ext4 /dev/mapper/pool-kilo
  293  mkdir /mnt/pool-kilo
  294  sudo mkdir /mnt/pool-kilo
  295  mount -v /dev/mapper/pool-kilo /mnt/pool-kilo/
  296  sudo mount -v /dev/mapper/pool-kilo /mnt/pool-kilo/
  297  sudo chown user:user -R /mnt/pool-kilo/
