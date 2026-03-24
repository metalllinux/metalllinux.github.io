---
title: "Reasons Why GRUB Does Not Regenerate if the Packages are Updated"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "reasons", "grub", "regenerate", "grub"]
---

# Reasons Why GRUB Does Not Regenerate if the Packages are Updated

From another thread, this is not an issue with the previous ISO we delivered and it seems to be an issue with possibly a new ISO that the customer is building post-delivery. The issue seems to be an update to the grub2 package where it won't allow a user to do grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg anymore so in their new ISO they need to remove that line in their kickstart so that error doesn't cause their install to quit early.

