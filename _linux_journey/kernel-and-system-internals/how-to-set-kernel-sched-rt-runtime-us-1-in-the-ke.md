---
title: "How To Set Kernel.Sched Rt Runtime Us= 1 In The Ke"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "kernelsched", "runtime"]
---

Edit `GRUB_CMDLINE_LINUX` in `etc/default/grub`
Add `kernel.sched_rt_runtime_us=-1` to the line.
Run `grub2-mkconfig -o /boot/grub2/grub.cfg` and then reboot the system.
