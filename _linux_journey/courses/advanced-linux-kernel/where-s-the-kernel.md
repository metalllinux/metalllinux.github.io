---
title: "Where S The Kernel"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "where", "kernel"]
---

* Check `/boot`
* We can find the Kernel we are using, it has to start with `vmlinuz` and an example is here: `vmlinuz-6.5.0-21-generic`.
* Confirm with `uname -r`
* The `vmlinuz` file is compressed.
* The `vmlinuz` file is loaded into memory by GRUB. GRUB will then transfer control to it.
* Do not delete this file.