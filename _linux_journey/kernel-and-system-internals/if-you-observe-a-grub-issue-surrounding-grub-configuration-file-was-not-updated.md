---
title: "If You Observe a GRUB Issue Surrounding GRUB Configuration was Not Updated"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "you", "observe", "grub", "issue"]
---

# If You Observe a GRUB Issue Surrounding GRUB Configuration was Not Updated

* The log message would be something like this:

```
"Running `grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg' will overwrite the GRUB wrapper.",
"Please run `grub2-mkconfig -o /boot/grub2/grub.cfg' instead to update grub.cfg.",
"GRUB configuration file was not updated."
```

* Then run:

```
grub2-mkconfig -o /boot/grub2/grub.cfg
```
