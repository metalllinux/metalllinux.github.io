---
title: "Kernel Components"
category: "lpic-2"
tags: ["lpic-2", "kernel", "components"]
---

* Directly connects hardware to software.
* Governs multiple pieces of software so they do not collide.
* Windows has the NTOS Kernel.
* Mac has the Mac Kernel.
	* Built on top of BSD Unix.
* Doesn't provide SysV-Init, systemd, GNU Toolset (with Bash, Vi and so on), X, Wayland and more.
* It provides a memory manager to control things going in and out of memory.
* It has a process manager, when an application executes, it is the kernel that executes the actual application and then passes it into memory.
* It has hardware control, initialises the hardware and provides the driver interface to it.
* It has the disk file system to work with systems like EXT4, XFS, BTFS, ZFS etc.
* The Kernel is a binary.
* The Kernel is stored in a non-encrypted partition, which is `/boot`.
	* The key file in `/boot` is `vmlinuz`. That is the Kernel.
	* Run `ls -l` and you can see where the file is symlinked to. As an example:
```
lrwxrwxrwx 1 root root        25 Jan 15 21:31 vmlinuz -> vmlinuz-5.15.0-91-generic
```
* Updating the Linux Kernel usually keeps an older verison available to look at as well.
* The `z` in `vmlinuz` means that it has been compressed with `gzip`.
* `vmlinux` means that it is uncompressed.
	* Can also be compressed with `bzip` as well if you see the format is different.
* Will definitely see `vmlinuz` in RHEL, Ubuntu, Debian and so on.
* Linux has a Monolithic Kernel. 
* There are two classes of Kernel:
	* Monolithic
		* Everything in the operating system runs in Kernel space.
		* Typically faster than Micro Kernel due to having everything available.
		* Linux does something interesting - it uses Kernel Modules.
			* Kernel Modules can be dynamically loaded.
			* An example Module would be a RAID driver for a RAID controller. We need a driver for that, which works with the RAID controller. 
			* For a Monolithic Kernel, the driver would need to be part of that Kernel.
			* If you take that same Kernel however and install it on your laptop, your laptop does not need that RAID driver.
				* With Kernel Modules, we can dynamically load and unload them as needed.
			* When the modules are loaded into RAM, the Kernel is able to grab the modules it needs and load them into Kernel space.
			* In RAM, it is all one giant memory address space.
			* Some of the modules are required, before the Kernel even starts.
			* There is another symlink file called `initrd.img`. Example below:
			* `lrwxrwxrwx 1 root root        28 Jan 15 21:31 initrd.img -> initrd.img-5.15.0-91-generic`.
				* It stands for Initialiastion RAM Disk Image.
					* It is a virtual disk.
					* `grub` looks for the Kernel and it will look for the RAM Disk at the same time.
						* `grub` will read that disk into RAM and create a virtual temporary file system.
							* That wil contain the modules that the Kernel immediately needs.
								* It can use those to read the disk and then load everything else afterwards. 
									* The size of the `initrd.img` file depends on your hardware.
										* If you go to `/lib/modules`, there is where all of the modules are installed.
										* Will see separate directories for each Kernel.
										* This is an example output: `myuser@myhost:/lib/modules/5.15.0-91-generic$ ls
build   kernel         modules.alias.bin  modules.builtin.alias.bin  modules.builtin.modinfo  modules.dep.bin  modules.order    modules.symbols      vdso
initrd  modules.alias  modules.builtin    modules.builtin.bin        modules.dep              modules.devname  modules.softdep  modules.symbols.bin
`
										* The modules that are in the `initrd` directory, those are the ones that will end up in the RAM Disk.
										* The modules are that are in the `kernel` directory are loaded after the Kernel is up.
										* Within the `kernel` directory, you'll see directories for all of the different sub-systems like this: `myuser@myhost:/lib/modules/5.15.0-91-generic/kernel$ ls
arch  block  crypto  drivers  fs  kernel  lib  mm  net  samples  sound  ubuntu  v4l2loopback  zfs`
										* `block` is for block storage. `net` will have network such as `ipv4`.
		* You can check if you have the Kernel source code installed. Then you will have the Kernel documentation available. This will be in `/usr/src`. Then you can go into that directory and find a directory called `documentation`
		* kernel.org is where you get the documentation and can download the Kernel.
		* What are `linux-headers` in the `/usr/src` directory.
			* When you compile a binary, the binary has to talk to the Linux API and talk to the Kernel.
				* People don't need the entire set of source code. The subset of the source code is called `headers`. 
				* The `headers` are a list of all fhe functions defined in the Linux source code and the output they expect. Then don't have to compile it against the entire source code and it makes compiling much faster and takes up less space.
				* 
										
				* RAID Controllers are a good example of something that needs drivers, before the Kernel is able to start.
	* Micro Kernel
		* The Kernel is as small as possible. 
		* Everything else runs in userspace (a different set of memory).
			* Can then call the Kernel via a safe API.
		* Typically more complex and have more dependencies.