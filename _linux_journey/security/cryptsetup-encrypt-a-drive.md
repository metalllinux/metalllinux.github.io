---
title: "Cryptsetup Encrypt A Drive"
category: "security"
tags: ["security", "cryptsetup", "encrypt", "drive"]
---

cryptsetup --verbose --verify-passphrase luksFormat /dev/partition-name

cryptsetup luksOpen /dev/partition-name partition-name

mkfs.ext4 /dev/mapper/partition-name