---
title: "Understanding The Bootloader Grub"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "understanding", "bootloader", "grub"]
---

* Embedded devices such as Android have a different bootloader, but for Desktop and Servers - GRUB is the main one.
* GRUB comes after POST and BIOS.
* Some part of GRUB will be available on the disk for the BIOS to find. The BIOS finds that and GRUB can load more of itself in.
* GRUB loads the Kernel, initla root filesystem into memory, sets up the Kernel command line and transfers control to the Kernel.
	* The file it loads is VMLINUZ for the Kernel and the Initial Root Filesystem.
	* The Initial Root Filesystem is a RAM disk image with `/etc` and other basic directories. This helps load drivers, that the Kernel requires and can then continue to boot.
	* GRUB knows what options to pass to the Kernel.
	* GRUB can be interrupted before it starts Linux.
	* Can change how it boots Linux and which Kernel it is going to boot. In addition, retrieving a Kernel over the network.
* GRUB has support for filesystems. GRUB can find files like Kernel files by name.
	* Can search for a file and also do `file name completion` (when pressing `tab`)
* More commands with `man -k grub` and will list all commands with the keyword `grub`.