---
title: "How To Create, Format And Mount A Luks Drive"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "format", "mount", "luks"]
---

 288  sudo cryptsetup luksFormat --type luks2 /dev/sdf
  289  sudo cryptsetup -v luksOpen /dev/sdf twinkletits
  290  mkfs.ext4 /dev/mapper/twinkletits
  291  sudo apt install mkfs
  292  sudo mkfs.ext4 /dev/mapper/twinkletits
  293  mkdir /mnt/twinkletits
  294  sudo mkdir /mnt/twinkletits
  295  mount -v /dev/mapper/twinkletits /mnt/twinkletits/
  296  sudo mount -v /dev/mapper/twinkletits /mnt/twinkletits/
  297  sudo chown howard:howard -R /mnt/twinkletits/
