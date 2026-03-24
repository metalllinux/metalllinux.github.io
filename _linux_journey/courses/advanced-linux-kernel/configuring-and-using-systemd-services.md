---
title: "Booting - Process 1 and Startup Services"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "configuring", "systemd", "services"]
---

### Booting - Process 1 and Startup Services
* The Initial Root Filesystem looks like this:
![Screenshot from 2024-05-21 22-23-07.png](../../_resources/Screenshot%20from%202024-05-21%2022-23-07.png)
* This is mounted on `/`.
* Linux always needs a `root` filesystem.
* We call this filesystem `initrd` --> Initial RAM Disk (older style, used to be formatted with EXT2) or RAM Filesystem (this is different, as this filesystem can grow and shrink), used to provide drivers and support for mounting the system's real root filesystem.
* Inside the `root` filesystem, there is a program that the kernel runs first. 
	* This is `init` from `initrd` and the kernel can look for other names as well.
### The First Process (from disk)
* When `init` from `initrd` terminates, the Linux kernel starts `init` again. This time from the real filesystem, which is commonly on the disk.
	* If you have an `init` that is a soft link to something else, the kernel will run that instead.
		* `init` is usually a softlink to `systemd` now.
	* This is responsible for starting up services such as daemons, like a web server.