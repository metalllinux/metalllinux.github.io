---
title: "Read Messages From The Kernel"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "read", "messages", "kernel"]
---

* Function in the Linux Kernel is the function called `printk()`. Similar to C's `printf()`.
	* The message is then sent to a RAM buffer and the system console.
	* Important messages are displayed on the system console.
	* Logging daemon may send to a file as well.
* Kernel is written in C with a little bit of Assembly.
* Command `dmesg` shows the RAM buffer messages from the Kernel.
	* Shows only messages since the system has booted.
* `dmesg` is only a finite size and older messages are removed.
* `systemd` journals all messages in `/var/log/messages`
* Can also check Kernel messages with `journalctl -t kernel`. See messages that come directly from the Kernel and not those being stored in log files on the disk.
* Can also do `journalctl -t kernel -f` and it will follow any new messages that are printed by the Kernel.
* Example `dmesg` check is `dmesg | grep command`
* Will show:
```
[    0.035138] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-25-generic root=UUID=ca2eb2d6-2fc2-4c9e-8001-11190efd85ee ro quiet splash radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1 vt.handoff=7
[    0.035300] Unknown kernel command line parameters "splash BOOT_IMAGE=/boot/vmlinuz-6.5.0-25-generic", will be passed to user space.
```
* Shows the path name to the Kernel file itself.
* `root=UUID` identifies the disk and partition for the root filesystem.
* These are passed to the Kernel from the bootloader.
* Bootloader can pass multiple parameters to the Kernel.
	* `ro` read-only. When the Kernel boots, it will mount the filesystem read-only to begin with. Then is checked for consistency. If you don't have a corrupted disk or anything like that, it will mount it `rw`. We don't want things to change, whilst checking the Kernel, hence `ro`.
* For Journal Control (journalctl). The journalctl command does its own paging (no need for `less`)
* Running `journalctl -t kernel | grep command` can show the amount of times the machine has booted:
```
 3月 18 08:58:44 explosion kernel: Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-25-generic root=UUID=ca2eb2d6-2fc2-4c9e-8001-11190efd85ee ro quiet splash radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1 vt.handoff=7
 3月 18 08:58:44 explosion kernel: Unknown kernel command line parameters "splash BOOT_IMAGE=/boot/vmlinuz-6.5.0-25-generic", will be passed to user space.
```
* Can check the journal command with in real-time with:
```
journalctl -t kernel -f
```