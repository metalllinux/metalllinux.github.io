---
title: "How Change Timeout Option And Initial Option To Hi"
category: "general-linux"
tags: ["change", "timeout", "option", "initial", "option"]
---

Under `/etc/default/grub`, add `GRUB_RECORDFAIL_TIMEOUT=<number_of_seconds>`.
Set `GRUB_DEFAULT=<option_in_list_you_want_to_choose>`
Then run `sudo update-grub` and `reboot`.