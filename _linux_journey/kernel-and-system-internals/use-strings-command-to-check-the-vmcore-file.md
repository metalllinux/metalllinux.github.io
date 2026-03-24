---
title: "Use Strings Command To Check The Vmcore File"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "strings", "command", "check", "vmcore"]
---

The vmcore file is a binary file so in order to understand some of the things it contains is better to use strings command and grep for kernel. This is a good way to confirm the kernel used by the client OS. This is an important step as this warranties the success or the failure of the investigation.

strings vmcore | grep BOOT
[BOOT_IMAGE=/vmlinuz-3.10.0-1160.108.1.el7.x86_64root=/dev/mapper/centos-root ro crashkernel=128M rd.lvm.lv=c

There are several lines that confirms the kernel version. Once confirmed, we can move to the next step.