---
title: "How To Check If An Iso Is Uefi Or Legacy Bios Boot"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "check", "iso", "uefi", "legacy"]
---

```
find <DIRECTORY_OF_MOUNTED_ISO> -type f | grep -i "EFI/BOOT/bootx64.efi"
```