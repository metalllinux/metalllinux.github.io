---
title: "Create Samba Share On Zfs"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "create", "samba", "share", "zfs"]
---

  860  sudo zfs create pool-alpha/test_share
  861  sudo zfs set sharesmb=on pool-alpha/test_share
  862  sudo chown -R user:user /mnt/pool-alpha/test_share/
  864  sudo smbpasswd -a user
