---
title: "Create Samba Share On Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "samba", "share", "zfs"]
---

  860  sudo zfs create dethklok/test_share
  861  sudo zfs set sharesmb=on dethklok/test_share
  862  sudo chown -R howard:howard /mnt/dethklok/test_share/
  864  sudo smbpasswd -a howard
