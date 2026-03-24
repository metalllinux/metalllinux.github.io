---
title: "Kernel Command Line Parameters"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "kernel", "command", "line", "parameters"]
---

* Kernel can get command-line processes from GRUB and that affects how the Kernel functions.
* Any arguments however on the GRUB command-line that the Kernel doesn't recognise, these are then ignored.
* A daemon or program in User Space may look at the Kernel command-line arguments. In particular, look for one that it is interested in.
* Can have multiple ways of booting your Kernel in your GRUB configuration. This can affect how a daemon works.
* Kernel Parameters - in the kernel source tree, this is `Documentation/kernel-parameters.txt`.
* Many are registered `with_setup()` in source.
* In the kernel's paramters, many functions call.
* If trying to see what the command does, the command is also set up using a macro.
* Under `/usr/src/linux-<version>/Documentation/admin-guide`, there is a `kernel-parameters.txt` file.
	* Not available on my system.
* `rdinit`  - specifies what program the kernel should run as the first process, when it starts up with the RAM filesystem image.
	* When GRUB loads the kernel, it also loads a filesystem image. It has `/`, `bin` and so on. Inside that is one called `init`, which is ran by default. 
	* The kernel on desktops and servers is going to have two inits. 
		* Firstly the RAM filesystem image, which gets some initial modules started.
		* Then, the regular `init` from the disk runs, typically `systemd`.
			* RD Init affects the first init. 
			* You can specify a pathname to that first filesystem image. 
			* The filesystem image may not have BASH, but it may have the SH shell.
			* Runs `/bin/sh` on the console. This will be `root`.
	* There is also `init=` and you can specify a program on your disk to run instead of `systemd`.
		* Can do `init=/bin/bash`, can be placed in the system as `root` without the password.
* `rfkill.default_state`
	* If you set this to 0 on the command line, the kernel boots into Airplane mode and does not allow any RF out.