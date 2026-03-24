---
title: "What Is The Linux Kernel"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "linux", "kernel"]
---

* The kernel often has a name of `vmlinuz-<KERNEL VERSION>`
* Program needs to be loaded into memory and ran.
* That operation is performed by a bootloader. Like GRUB.
* GRUB reads the Kernel file from disk into memory and transfers control afterwards.
* Kernel has commandline parameters and GRUB is responsbile for passing those to the Kernel.
* The Linux Kernel has an API.
* Functions we can call from userspace into the Kernel -> These are `System Calls`.
* The Linux Kernel also provides virtual filesystem entries.
* `proc`
* `sys`
* `debugfs`
* Through the above 3 filesystems, we can directly interact with the Kernel.
* We can use these to get information and change things within the Kernel.
* Filesystem has Device Files (system calls).
* Interact with Device Drivers, by performing operations on the Device Files.
* Standard system calls like "Read", "Write" and "Open".
* Kernel is a gatekeeper and:
	* Enforce privileges (in Linux, these are called capabilities).
		* Checks the capabilities of a process, to see if it is allowed to perform the require operation.
		* `root` processes have a large set of capabilities.
	* CPUs have instructions that only allow the CPU to execute them, when the CPU itself is in a supervisory mode.
		* The supervisory mode is when we execute inside the Kernel.
		* There are Assembly language instructions, that can only be executed by the Kernel.
	* Linux Kernel implements security policies.
		* Underlying mechanisms of SELinux.
	* Kernel provides access to controlled hardware and other resources.
* The Kernel is modular.
	* The Kernel image itself is small.
	* The Kernel image is sufficient to boot to User Space.
		* Allows the start of processes.
	* Once we have processes, we can load additional functionality into the Kernel, via a loadable Kernel Object mechanism.
	* We can load the drivers that we need. No need to load drivers for hardware that is not present.