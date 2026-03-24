---
title: "Initramfs Explanation"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "initramfs", "explanation"]
---

As far as I know, initramfs is a temporary file system used during the initial stages of the Linux kernel boot process. It contains essential files and drivers required to mount the actual root file system.

Kernel modules are loaded into kernel space, hence the term "kernel modules". (Whether they're done by initramfs or rootfs doesn't matter.)

The loading is initially done by a user space tool such as udev or modprobe, which uses libkmod to find the necessary module, then invokes the init_module(2) system call to transfer it into kernel space.

The initramfs is not limited to only loading kernel modules, however; it can run any userspace tools – including modprobe/insmod to load kernel modules, of course, but it can also include userspace daemons if necessary (e.g. ntfs-3g if your rootfs is on NTFS, or iscsid if it's an iSCSI volume).